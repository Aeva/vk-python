
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
            if not supports_present.value:
                continue
            match = VK_QUEUE_GRAPHICS_BIT | VK_QUEUE_COMPUTE_BIT | VK_QUEUE_TRANSFER_BIT
            if (queue_family.queueFlags.value & match):
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
        self.swapchain_create_info.imageUsage = VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT.value
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
            image_view_create_info.subresourceRange.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT.value
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
