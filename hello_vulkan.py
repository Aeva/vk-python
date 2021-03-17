
import os
import time
import sdl2
import sdl2.ext
import sdl2.vulkan
from vulkan import *
from ctypes import *


def vk_get(vk_fn, result_type, *args):
    count = c_uint32()
    vk_fn(*(list(args) + [byref(count), None]))
    array = (result_type * count.value)()
    vk_fn(*(list(args) + [byref(count), array]))
    return array


class VulkanWindow:
    def __init__(self, title, width, height, position=None, flags=0, validate=True):
        flags = flags | sdl2.SDL_WINDOW_VULKAN
        self.title = title
        self.width = width
        self.height = height
        self.validate = validate
        self.sdl_window = sdl2.ext.Window(title, size=(width, height), flags=flags)
        self.teardown = []
        self.create_instance()
        self.select_adapter()
        self.setup_surface()
        self.setup_device()
        self.setup_swapchain()
        self.setup_frames()
        self.setup_depth_buffer()
        self.setup_render_pass()
        self.setup_frame_buffers()
        self.setup_pipeline()

    def create_instance(self):
        app_info = VkApplicationInfo()
        app_info.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO
        app_info.pNext = None
        app_info.pApplicationName = self.title.encode()
        app_info.applicationVersion = 1
        app_info.pEngineName = self.title.encode()
        app_info.engineVersion = 0
        app_info.apiVersion = VK_API_VERSION_1_0

        instance_extensions = vk_get(sdl2.vulkan.SDL_Vulkan_GetInstanceExtensions, c_char_p, self.sdl_window.window)

        print("Found the following instance extensions:")
        for extension in instance_extensions:
            print(f" - {extension.decode('utf-8')}")

        validation_layer = c_char_p(b"VK_LAYER_KHRONOS_validation")

        instance_create_info = VkInstanceCreateInfo()
        instance_create_info.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
        instance_create_info.pNext = None
        instance_create_info.flags = 0
        instance_create_info.pApplicationInfo = pointer(app_info)
        instance_create_info.enabledExtensionCount = len(instance_extensions)
        instance_create_info.ppEnabledExtensionNames = instance_extensions
        instance_create_info.enabledLayerCount = 1 if self.validate else 0
        instance_create_info.ppEnabledLayerNames = pointer(validation_layer) if self.validate else None

        self.instance = VkInstance()
        result = vkCreateInstance(byref(instance_create_info), None, byref(self.instance))
        assert(result == VK_SUCCESS)
        self.teardown.append(self._destroy_instance)

    def use_adapter(self, adapter):
        self.adapter = adapter
        vkGetPhysicalDeviceMemoryProperties(self.adapter, byref(self.adapter_memory_properties))
        print(f"Using GPU: {self.adapter_properties.deviceName.decode()}")

    def select_adapter(self):
        self.adapter = None
        self.adapter_properties = VkPhysicalDeviceProperties()
        self.adapter_memory_properties = VkPhysicalDeviceMemoryProperties()
        adapters = vk_get(vkEnumeratePhysicalDevices, VkPhysicalDevice, self.instance)
        if len(adapters) == 0:
            raise RuntimeError("No GPUs found!")
        for candidate in adapters:
            vkGetPhysicalDeviceProperties(candidate, byref(self.adapter_properties))
            if (self.adapter_properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU):
                self.use_adapter(candidate)
                return
        for candidate in adapters:
            vkGetPhysicalDeviceProperties(candidate, byref(self.adapter_properties))
            if (self.adapter_properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU):
                self.use_adapter(candidate)
                return
        vkGetPhysicalDeviceProperties(adapters[0], byref(self.adapter_properties))
        self.use_adapter(adapters[0])

    def setup_surface(self):
        self.surface = VkSurfaceKHR()
        sdl2.vulkan.SDL_Vulkan_CreateSurface(
            self.sdl_window.window,
            cast(pointer(self.instance), POINTER(sdl2.vulkan.VkInstance)).contents,
            cast(pointer(self.surface), POINTER(sdl2.vulkan.VkSurfaceKHR)))
        assert(self.surface)
        surface_formats = vk_get(vkGetPhysicalDeviceSurfaceFormatsKHR, VkSurfaceFormatKHR, self.adapter, self.surface)
        self.surface_format = surface_formats[0]
        self.teardown.append(self._destroy_surface)

    def setup_device(self):
        queue_familes = vk_get(vkGetPhysicalDeviceQueueFamilyProperties, VkQueueFamilyProperties, self.adapter)
        self.queue_index = None
        self.queue_family = None
        for queue_index, queue_family in enumerate(queue_familes):
            supports_present = VkBool32()
            vkGetPhysicalDeviceSurfaceSupportKHR(self.adapter, queue_index, self.surface, byref(supports_present))
            if not supports_present:
                continue
            match = VK_QUEUE_GRAPHICS_BIT | VK_QUEUE_COMPUTE_BIT | VK_QUEUE_TRANSFER_BIT
            if (queue_family.queueFlags & match):
                self.queue_index = queue_index
                self.queue_family = queue_family
                break
        assert(self.queue_index is not None)

        queue_priority = c_float()
        device_queue_create_info = VkDeviceQueueCreateInfo()
        device_queue_create_info.sType = VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO
        device_queue_create_info.pNext = None
        device_queue_create_info.flags = 0
        device_queue_create_info.queueFamilyIndex = self.queue_index
        device_queue_create_info.queueCount = 1
        device_queue_create_info.pQueuePriorities = pointer(queue_priority)

        device_extensions = c_char_p(b"VK_KHR_swapchain")

        device_create_info = VkDeviceCreateInfo()
        device_create_info.sType = VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO
        device_create_info.pNext = None
        device_create_info.flags = 0
        device_create_info.queueCreateInfoCount = 1
        device_create_info.pQueueCreateInfos = pointer(device_queue_create_info)
        device_create_info.enabledExtensionCount = 1
        device_create_info.ppEnabledExtensionNames = pointer(device_extensions)
        device_create_info.enabledLayerCount = 0
        device_create_info.ppEnabledLayerNames = None
        device_create_info.pEnabledFeatures = None

        self.device = VkDevice()
        result = vkCreateDevice(self.adapter, byref(device_create_info), None, byref(self.device))
        assert(result == VK_SUCCESS)
        self.teardown.append(self._destroy_device)

    def setup_swapchain(self):
        queue_index = c_uint32(self.queue_index)
        self.swapchain_create_info = VkSwapchainCreateInfoKHR()
        self.swapchain_create_info.sType = VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR
        self.swapchain_create_info.pNext = None
        self.swapchain_create_info.flags = 0
        self.swapchain_create_info.surface = self.surface
        self.swapchain_create_info.minImageCount = 2
        self.swapchain_create_info.imageFormat = self.surface_format.format
        self.swapchain_create_info.imageColorSpace = self.surface_format.colorSpace
        self.swapchain_create_info.imageExtent.width = self.width
        self.swapchain_create_info.imageExtent.height = self.height
        self.swapchain_create_info.imageArrayLayers = 1
        self.swapchain_create_info.imageUsage = VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT
        self.swapchain_create_info.imageSharingMode = VK_SHARING_MODE_EXCLUSIVE
        self.swapchain_create_info.queueFamilyIndexCount = 1
        self.swapchain_create_info.pQueueFamilyIndices = pointer(queue_index)
        self.swapchain_create_info.preTransform = VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR
        self.swapchain_create_info.compositeAlpha = VK_COMPOSITE_ALPHA_OPAQUE_BIT_KHR
        self.swapchain_create_info.presentMode = VK_PRESENT_MODE_FIFO_KHR
        self.swapchain_create_info.clipped = True
        self.swapchain_create_info.oldSwapchain = None
        self.swapchain = VkSwapchainKHR()
        result = vkCreateSwapchainKHR(self.device, byref(self.swapchain_create_info), None, byref(self.swapchain))
        assert(result == VK_SUCCESS)
        self.teardown.append(self._destroy_swapchain)

    def setup_frames(self):
        self.swapchain_images = vk_get(vkGetSwapchainImagesKHR, VkImage, self.device, self.swapchain)
        self.swapchain_views = []
        self.command_pools = []
        for image in self.swapchain_images:
            image_view_create_info = VkImageViewCreateInfo()
            image_view_create_info.sType = VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO
            image_view_create_info.pNext = None
            image_view_create_info.flags = 0
            image_view_create_info.image = image
            image_view_create_info.viewType = VK_IMAGE_VIEW_TYPE_2D
            image_view_create_info.format = self.surface_format.format
            image_view_create_info.components.r = VK_COMPONENT_SWIZZLE_IDENTITY
            image_view_create_info.components.g = VK_COMPONENT_SWIZZLE_IDENTITY
            image_view_create_info.components.b = VK_COMPONENT_SWIZZLE_IDENTITY
            image_view_create_info.components.a = VK_COMPONENT_SWIZZLE_IDENTITY
            image_view_create_info.subresourceRange.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT
            image_view_create_info.subresourceRange.baseMipLevel = 0
            image_view_create_info.subresourceRange.levelCount = 1
            image_view_create_info.subresourceRange.baseArrayLayer = 0
            image_view_create_info.subresourceRange.layerCount = 1
            view = VkImageView()
            vkCreateImageView(self.device, byref(image_view_create_info), None, byref(view))
            self.swapchain_views.append(view)
            command_pool_create_info = VkCommandPoolCreateInfo()
            command_pool_create_info.sType = VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO
            command_pool_create_info.pNext = None
            command_pool_create_info.queueFamilyIndex = self.queue_index
            command_pool_create_info.flags = 0
            command_pool = VkCommandPool()
            vkCreateCommandPool(self.device, byref(command_pool_create_info), None, byref(command_pool))
            self.command_pools.append(command_pool)
        fence_create_info = VkFenceCreateInfo()
        fence_create_info.sType = VK_STRUCTURE_TYPE_FENCE_CREATE_INFO
        fence_create_info.pNext = None
        fence_create_info.flags = 0
        self.frame_fence = VkFence()
        vkCreateFence(self.device, fence_create_info, None, byref(self.frame_fence))
        semaphore_create_info = VkSemaphoreCreateInfo()
        semaphore_create_info.sType = VK_STRUCTURE_TYPE_SEMAPHORE_CREATE_INFO
        semaphore_create_info.pNext = None
        semaphore_create_info.flags = 0
        self.swapchain_semaphore = VkSemaphore()
        vkCreateSemaphore(self.device, semaphore_create_info, None, byref(self.swapchain_semaphore))
        self.teardown.append(self._destroy_frame)

    def get_depth_tiling_mode(self, depth_format):
        depth_format_properties = VkFormatProperties()
        vkGetPhysicalDeviceFormatProperties(self.adapter, depth_format, byref(depth_format_properties))
        if (depth_format_properties.optimalTilingFeatures & VK_FORMAT_FEATURE_DEPTH_STENCIL_ATTACHMENT_BIT):
            return VK_IMAGE_TILING_OPTIMAL
        elif (depth_format_properties.linearTilingFeatures & VK_FORMAT_FEATURE_DEPTH_STENCIL_ATTACHMENT_BIT):
            return VK_IMAGE_TILING_LINEAR
        else:
            raise RuntimeError(f"Cannot determine the tiling mode for {str(depth_format)}")

    def get_image_alloc_info(self, image, property_flags):
        memory_requirements = VkMemoryRequirements()
        vkGetImageMemoryRequirements(self.device, image, byref(memory_requirements));

        allocate_info = VkMemoryAllocateInfo()
        allocate_info.sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO
        allocate_info.pNext = None
        allocate_info.allocationSize = memory_requirements.size

        for index, memory_type in enumerate(self.adapter_memory_properties.memoryTypes):
            memory_type_bit = 1 << index
            matches_bits = (memory_requirements.memoryTypeBits & memory_type_bit) == memory_type_bit
            matches_properties = (memory_type.propertyFlags & property_flags) == property_flags
            if matches_bits and matches_properties:
                allocate_info.memoryTypeIndex = index
                return allocate_info

        error = "Unable to find a memory type index matching the following flags:\n"
        for flag in VkMemoryPropertyFlags(property_flags).get_active():
            error += f" - {str(flag)}\n"
        raise RuntimeError(error)

    def setup_depth_buffer(self):
        depth_buffer_create_info = VkImageCreateInfo()
        depth_buffer_create_info.sType = VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO
        depth_buffer_create_info.pNext = None
        depth_buffer_create_info.imageType = VK_IMAGE_TYPE_2D
        depth_buffer_create_info.format = VK_FORMAT_D16_UNORM
        depth_buffer_create_info.extent.width = self.width
        depth_buffer_create_info.extent.height = self.height
        depth_buffer_create_info.extent.depth = 1
        depth_buffer_create_info.mipLevels = 1
        depth_buffer_create_info.arrayLayers = 1
        depth_buffer_create_info.samples = VK_SAMPLE_COUNT_1_BIT
        depth_buffer_create_info.tiling = self.get_depth_tiling_mode(VK_FORMAT_D16_UNORM)
        depth_buffer_create_info.initialLayout = VK_IMAGE_LAYOUT_UNDEFINED
        depth_buffer_create_info.usage = VK_IMAGE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT
        depth_buffer_create_info.queueFamilyIndexCount = 0
        depth_buffer_create_info.pQueueFamilyIndices = None
        depth_buffer_create_info.sharingMode = VK_SHARING_MODE_EXCLUSIVE
        depth_buffer_create_info.flags = 0
        self.depth_buffer_image = VkImage()
        result = vkCreateImage(self.device, byref(depth_buffer_create_info), None, byref(self.depth_buffer_image))
        assert(result == VK_SUCCESS)

        depth_buffer_allocation_info = self.get_image_alloc_info(self.depth_buffer_image, VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT)
        self.depth_buffer_memory = VkDeviceMemory()
        result = vkAllocateMemory(self.device, byref(depth_buffer_allocation_info), None, byref(self.depth_buffer_memory))
        assert(result == VK_SUCCESS)
        relust = vkBindImageMemory(self.device, self.depth_buffer_image, self.depth_buffer_memory, 0)
        assert(result == VK_SUCCESS)

        image_view_create_info = VkImageViewCreateInfo()
        image_view_create_info.sType = VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO
        image_view_create_info.pNext = None
        image_view_create_info.flags = 0
        image_view_create_info.image = self.depth_buffer_image
        image_view_create_info.format = depth_buffer_create_info.format
        image_view_create_info.viewType = VK_IMAGE_VIEW_TYPE_2D
        image_view_create_info.components.r = VK_COMPONENT_SWIZZLE_IDENTITY
        image_view_create_info.components.g = VK_COMPONENT_SWIZZLE_IDENTITY
        image_view_create_info.components.b = VK_COMPONENT_SWIZZLE_IDENTITY
        image_view_create_info.components.a = VK_COMPONENT_SWIZZLE_IDENTITY
        image_view_create_info.subresourceRange.aspectMask = VK_IMAGE_ASPECT_DEPTH_BIT
        image_view_create_info.subresourceRange.baseMipLevel = 0
        image_view_create_info.subresourceRange.levelCount = depth_buffer_create_info.mipLevels
        image_view_create_info.subresourceRange.baseArrayLayer = 0
        image_view_create_info.subresourceRange.layerCount = depth_buffer_create_info.arrayLayers
        self.depth_buffer_view = VkImageView()
        result = vkCreateImageView(self.device, byref(image_view_create_info), None, byref(self.depth_buffer_view))
        assert(result == VK_SUCCESS)
        self.teardown.append(self._destroy_depth_image)

    def setup_render_pass(self):
        attachments = (VkAttachmentDescription * 2)()
        attachments[0].flags = 0
        attachments[0].format = self.surface_format.format
        attachments[0].samples = VK_SAMPLE_COUNT_1_BIT
        attachments[0].loadOp = VK_ATTACHMENT_LOAD_OP_CLEAR
        attachments[0].storeOp = VK_ATTACHMENT_STORE_OP_STORE
        attachments[0].stencilLoadOp = VK_ATTACHMENT_LOAD_OP_DONT_CARE
        attachments[0].stencilStoreOp = VK_ATTACHMENT_STORE_OP_DONT_CARE
        attachments[0].initialLayout = VK_IMAGE_LAYOUT_UNDEFINED
        attachments[0].finalLayout = VK_IMAGE_LAYOUT_PRESENT_SRC_KHR
        attachments[1].flags = 0
        attachments[1].format = VK_FORMAT_D16_UNORM
        attachments[1].samples = VK_SAMPLE_COUNT_1_BIT
        attachments[1].loadOp = VK_ATTACHMENT_LOAD_OP_CLEAR
        attachments[1].storeOp = VK_ATTACHMENT_STORE_OP_DONT_CARE
        attachments[1].stencilLoadOp = VK_ATTACHMENT_LOAD_OP_DONT_CARE
        attachments[1].stencilStoreOp = VK_ATTACHMENT_STORE_OP_DONT_CARE
        attachments[1].initialLayout = VK_IMAGE_LAYOUT_UNDEFINED
        attachments[1].finalLayout = VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL

        attachment_refs = (VkAttachmentReference * 2)()
        attachment_refs[0].attachment = 0
        attachment_refs[0].layout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL
        attachment_refs[1].attachment = 1
        attachment_refs[1].layout = VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL

        subpass_desc = VkSubpassDescription()
        subpass_desc.flags = 0
        subpass_desc.pipelineBindPoint = VK_PIPELINE_BIND_POINT_GRAPHICS
        subpass_desc.inputAttachmentCount = 0
        subpass_desc.pInputAttachments = None
        subpass_desc.colorAttachmentCount = 1
        subpass_desc.pColorAttachments = pointer(attachment_refs[0])
        subpass_desc.pResolveAttachments = None
        subpass_desc.pDepthStencilAttachment = pointer(attachment_refs[1])
        subpass_desc.preserveAttachmentCount = 0
        subpass_desc.pPreserveAttachments = None

        subpass_dependency = VkSubpassDependency()
        subpass_dependency.srcSubpass = VK_SUBPASS_EXTERNAL
        subpass_dependency.dstSubpass = 0
        subpass_dependency.srcStageMask = VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT
        subpass_dependency.dstStageMask = VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT
        subpass_dependency.srcAccessMask = 0
        subpass_dependency.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT
        subpass_dependency.dependencyFlags = 0

        render_pass_create_info = VkRenderPassCreateInfo()
        render_pass_create_info.sType = VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO
        render_pass_create_info.pNext = None
        render_pass_create_info.attachmentCount = 2
        render_pass_create_info.pAttachments = attachments
        render_pass_create_info.subpassCount = 1
        render_pass_create_info.pSubpasses = pointer(subpass_desc)
        render_pass_create_info.dependencyCount = 1
        render_pass_create_info.pDependencies = pointer(subpass_dependency)

        self.render_pass = VkRenderPass()
        result = vkCreateRenderPass(self.device, render_pass_create_info, None, byref(self.render_pass))
        assert(result == VK_SUCCESS)
        self.teardown.append(self._destroy_render_pass)

    def setup_frame_buffers(self):
        image_views = (VkImageView * 2)()
        image_views[1] = self.depth_buffer_view
        frame_buffer_create_info = VkFramebufferCreateInfo()
        frame_buffer_create_info.sType = VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO
        frame_buffer_create_info.pNext = None
        frame_buffer_create_info.renderPass = self.render_pass
        frame_buffer_create_info.attachmentCount = 2
        frame_buffer_create_info.pAttachments = image_views
        frame_buffer_create_info.width = self.width
        frame_buffer_create_info.height = self.height
        frame_buffer_create_info.layers = 1

        self.frame_buffers = []
        for swapchain_view in self.swapchain_views:
            image_views[0] = swapchain_view
            frame_buffer = VkFramebuffer()
            result = vkCreateFramebuffer(self.device, frame_buffer_create_info, None, byref(frame_buffer))
            assert(result == VK_SUCCESS)
            self.frame_buffers.append(frame_buffer)

        self.teardown.append(self._destroy_frame_buffers)

    def load_shader_module(self, spirv_path):
        with open(os.path.join("shaders", spirv_path), "rb") as infile:
            bytes = infile.read()
        shader_module_create_info = VkShaderModuleCreateInfo()
        shader_module_create_info.sType = VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO
        shader_module_create_info.pNext = None
        shader_module_create_info.flags = 0
        shader_module_create_info.codeSize = len(bytes)
        shader_module_create_info.pCode = ctypes.cast(c_char_p(bytes), POINTER(c_uint32))
        module = VkShaderModule();
        result = vkCreateShaderModule(self.device, byref(shader_module_create_info), None, byref(module))
        assert(result == VK_SUCCESS)
        return module

    def setup_pipeline(self):
        self.vertex_shader = self.load_shader_module("test.vs.spv")
        self.fragment_shader = self.load_shader_module("test.fs.spv")
        shader_stages_create_info = (VkPipelineShaderStageCreateInfo * 2)()
        shader_stages_create_info[0].sType = VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO
        shader_stages_create_info[0].pNext = None
        shader_stages_create_info[0].flags = 0
        shader_stages_create_info[0].stage = VK_SHADER_STAGE_VERTEX_BIT
        shader_stages_create_info[0].module = self.vertex_shader
        shader_stages_create_info[0].pName = b"main"
        shader_stages_create_info[0].pSpecializationInfo = None
        shader_stages_create_info[1].sType = VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO
        shader_stages_create_info[1].pNext = None
        shader_stages_create_info[1].flags = 0
        shader_stages_create_info[1].stage = VK_SHADER_STAGE_FRAGMENT_BIT
        shader_stages_create_info[1].module = self.fragment_shader
        shader_stages_create_info[1].pName = b"main"
        shader_stages_create_info[1].pSpecializationInfo = None
        pipeline_layout_create_info = VkPipelineLayoutCreateInfo()
        pipeline_layout_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO
        pipeline_layout_create_info.pNext = None
        pipeline_layout_create_info.pushConstantRangeCount = 0
        pipeline_layout_create_info.pPushConstantRanges = None
        pipeline_layout_create_info.setLayoutCount = 0
        pipeline_layout_create_info.pSetLayouts = None

        self.pipeline_layout = VkPipelineLayout()
        result = vkCreatePipelineLayout(self.device, byref(pipeline_layout_create_info), None, byref(self.pipeline_layout))
        assert(result == VK_SUCCESS)

        enabled_dynamic_states = (c_int * 2)()
        enabled_dynamic_states[0] = VK_DYNAMIC_STATE_VIEWPORT
        enabled_dynamic_states[1] = VK_DYNAMIC_STATE_SCISSOR
        dynamic_state_create_info = VkPipelineDynamicStateCreateInfo()
        dynamic_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO
        dynamic_state_create_info.pNext = None
        dynamic_state_create_info.flags = 0
        dynamic_state_create_info.dynamicStateCount = 2
        dynamic_state_create_info.pDynamicStates = enabled_dynamic_states

        vertex_input_state_create_info = VkPipelineVertexInputStateCreateInfo()
        vertex_input_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO
        vertex_input_state_create_info.pNext = None
        vertex_input_state_create_info.flags = 0
        vertex_input_state_create_info.vertexBindingDescriptionCount = 0
        vertex_input_state_create_info.pVertexBindingDescriptions = None
        vertex_input_state_create_info.vertexAttributeDescriptionCount = 0
        vertex_input_state_create_info.pVertexAttributeDescriptions = None

        input_assembly_state_create_info = VkPipelineInputAssemblyStateCreateInfo()
        input_assembly_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO
        input_assembly_state_create_info.pNext = None
        input_assembly_state_create_info.flags = 0
        input_assembly_state_create_info.topology = VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST
        input_assembly_state_create_info.primitiveRestartEnable = VK_FALSE

        rasterization_state_create_info = VkPipelineRasterizationStateCreateInfo()
        rasterization_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO
        rasterization_state_create_info.pNext = None
        rasterization_state_create_info.flags = 0
        rasterization_state_create_info.depthClampEnable = VK_FALSE
        rasterization_state_create_info.rasterizerDiscardEnable = VK_FALSE
        rasterization_state_create_info.polygonMode = VK_POLYGON_MODE_FILL
        rasterization_state_create_info.cullMode = VK_CULL_MODE_BACK_BIT
        rasterization_state_create_info.frontFace = VK_FRONT_FACE_CLOCKWISE
        rasterization_state_create_info.depthBiasEnable = VK_FALSE
        rasterization_state_create_info.depthBiasConstantFactor = 0
        rasterization_state_create_info.depthBiasClamp = 0
        rasterization_state_create_info.depthBiasSlopeFactor = 0
        rasterization_state_create_info.lineWidth = 1.0

        color_blend_attachment_state_create_info = VkPipelineColorBlendAttachmentState()
        color_blend_attachment_state_create_info.blendEnable = VK_FALSE
        color_blend_attachment_state_create_info.srcColorBlendFactor = VK_BLEND_FACTOR_ZERO
        color_blend_attachment_state_create_info.dstColorBlendFactor = VK_BLEND_FACTOR_ZERO
        color_blend_attachment_state_create_info.colorBlendOp = VK_BLEND_OP_ADD
        color_blend_attachment_state_create_info.srcAlphaBlendFactor = VK_BLEND_FACTOR_ZERO
        color_blend_attachment_state_create_info.dstAlphaBlendFactor = VK_BLEND_FACTOR_ZERO
        color_blend_attachment_state_create_info.alphaBlendOp = VK_BLEND_OP_ADD
        color_blend_attachment_state_create_info.colorWriteMask = 0

        color_blend_state_create_info = VkPipelineColorBlendStateCreateInfo()
        color_blend_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO
        color_blend_state_create_info.pNext = None;
        color_blend_state_create_info.flags = 0
        color_blend_state_create_info.logicOpEnable = VK_FALSE
        color_blend_state_create_info.logicOp = VK_LOGIC_OP_NO_OP
        color_blend_state_create_info.attachmentCount = 1
        color_blend_state_create_info.pAttachments = pointer(color_blend_attachment_state_create_info)
        color_blend_state_create_info.blendConstants[0] = 1.0
        color_blend_state_create_info.blendConstants[1] = 1.0
        color_blend_state_create_info.blendConstants[2] = 1.0
        color_blend_state_create_info.blendConstants[3] = 1.0

        viewport_state_create_info = VkPipelineViewportStateCreateInfo()
        viewport_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO
        viewport_state_create_info.pNext = None
        viewport_state_create_info.flags = 0
        viewport_state_create_info.viewportCount = 1
        viewport_state_create_info.pViewports = None
        viewport_state_create_info.scissorCount = 1
        viewport_state_create_info.pScissors = None

        depth_stencil_state_create_info = VkPipelineDepthStencilStateCreateInfo()
        depth_stencil_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO
        depth_stencil_state_create_info.pNext = None
        depth_stencil_state_create_info.flags = 0
        depth_stencil_state_create_info.depthTestEnable = VK_TRUE
        depth_stencil_state_create_info.depthWriteEnable = VK_TRUE
        depth_stencil_state_create_info.depthCompareOp = VK_COMPARE_OP_LESS_OR_EQUAL
        depth_stencil_state_create_info.depthBoundsTestEnable = VK_FALSE
        depth_stencil_state_create_info.stencilTestEnable = VK_FALSE
        depth_stencil_state_create_info.front.failOp = VK_STENCIL_OP_KEEP
        depth_stencil_state_create_info.front.passOp = VK_STENCIL_OP_KEEP
        depth_stencil_state_create_info.front.depthFailOp = VK_STENCIL_OP_KEEP
        depth_stencil_state_create_info.front.compareOp = VK_COMPARE_OP_ALWAYS
        depth_stencil_state_create_info.front.compareMask = 0
        depth_stencil_state_create_info.front.writeMask = 0
        depth_stencil_state_create_info.front.reference = 0
        depth_stencil_state_create_info.back.failOp = VK_STENCIL_OP_KEEP
        depth_stencil_state_create_info.back.passOp = VK_STENCIL_OP_KEEP
        depth_stencil_state_create_info.back.depthFailOp = VK_STENCIL_OP_KEEP
        depth_stencil_state_create_info.back.compareOp = VK_COMPARE_OP_ALWAYS
        depth_stencil_state_create_info.back.compareMask = 0
        depth_stencil_state_create_info.back.writeMask = 0
        depth_stencil_state_create_info.back.reference = 0
        depth_stencil_state_create_info.minDepthBounds = 0
        depth_stencil_state_create_info.maxDepthBounds = 0

        multisample_state_create_info = VkPipelineMultisampleStateCreateInfo()
        multisample_state_create_info.sType = VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO
        multisample_state_create_info.pNext = None
        multisample_state_create_info.flags = 0
        multisample_state_create_info.rasterizationSamples = VK_SAMPLE_COUNT_1_BIT
        multisample_state_create_info.sampleShadingEnable = VK_FALSE
        multisample_state_create_info.minSampleShading = 0.0
        multisample_state_create_info.pSampleMask = None
        multisample_state_create_info.alphaToCoverageEnable = VK_FALSE
        multisample_state_create_info.alphaToOneEnable = VK_FALSE

        graphics_pipeline_create_info = VkGraphicsPipelineCreateInfo()
        graphics_pipeline_create_info.sType = VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO
        graphics_pipeline_create_info.pNext = None
        graphics_pipeline_create_info.flags = 0
        graphics_pipeline_create_info.stageCount = 2
        graphics_pipeline_create_info.pStages = shader_stages_create_info
        graphics_pipeline_create_info.pVertexInputState = pointer(vertex_input_state_create_info)
        graphics_pipeline_create_info.pInputAssemblyState = pointer(input_assembly_state_create_info)
        graphics_pipeline_create_info.pTessellationState = None
        graphics_pipeline_create_info.pViewportState = pointer(viewport_state_create_info)
        graphics_pipeline_create_info.pRasterizationState = pointer(rasterization_state_create_info)
        graphics_pipeline_create_info.pMultisampleState = pointer(multisample_state_create_info)
        graphics_pipeline_create_info.pDepthStencilState = pointer(depth_stencil_state_create_info)
        graphics_pipeline_create_info.pColorBlendState = pointer(color_blend_state_create_info)
        graphics_pipeline_create_info.pDynamicState = pointer(dynamic_state_create_info)
        graphics_pipeline_create_info.layout = self.pipeline_layout
        graphics_pipeline_create_info.renderPass = self.render_pass
        graphics_pipeline_create_info.subpass = 0
        graphics_pipeline_create_info.basePipelineHandle = None
        graphics_pipeline_create_info.basePipelineIndex = 0

        self.graphics_pipeline = VkPipeline()
        result = vkCreateGraphicsPipelines(self.device, None, 1, byref(graphics_pipeline_create_info), None, byref(self.graphics_pipeline))
        self.teardown.append(self._destroy_pipeline)

    def _destroy_pipeline(self):
        vkDestroyPipeline(self.device, self.graphics_pipeline, None)
        vkDestroyPipelineLayout(self.device, self.pipeline_layout, None)
        vkDestroyShaderModule(self.device, self.vertex_shader, None)
        vkDestroyShaderModule(self.device, self.fragment_shader, None)

    def _destroy_frame_buffers(self):
        for frame_buffer in self.frame_buffers:
            vkDestroyFramebuffer(self.device, frame_buffer, None)

    def _destroy_render_pass(self):
        vkDestroyRenderPass(self.device, self.render_pass, None)

    def _destroy_depth_image(self):
        vkDestroyImageView(self.device, self.depth_buffer_view, None)
        vkFreeMemory(self.device, self.depth_buffer_memory, None)
        vkDestroyImage(self.device, self.depth_buffer_image, None)

    def _destroy_frame(self):
        vkDestroySemaphore(self.device, self.swapchain_semaphore, None)
        vkDestroyFence(self.device, self.frame_fence, None)
        for command_pool in self.command_pools:
            vkDestroyCommandPool(self.device, command_pool, None)
        for view in self.swapchain_views:
            vkDestroyImageView(self.device, view, None)

    def _destroy_swapchain(self):
        vkDestroySwapchainKHR(self.device, self.swapchain, None)

    def _destroy_device(self):
        vkDestroyDevice(self.device, None)

    def _destroy_surface(self):
        vkDestroySurfaceKHR(self.instance, self.surface, None)

    def _destroy_instance(self):
        vkDestroyInstance(self.instance, None)

    def shutdown(self):
        for callback in self.teardown[::-1]:
            callback()
        self.teardown = []

    def pump_events(self):
        return not sdl2.SDL_QuitRequested()


if __name__ == "__main__":
    sdl2.ext.init()
    window = VulkanWindow("Hello World!", 800, 600, flags=sdl2.SDL_WINDOW_RESIZABLE)
    while window.pump_events():
        time.sleep(0.01)
    window.shutdown()
    sdl2.ext.quit()
