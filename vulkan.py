
import ctypes
import platform

if ctypes.sizeof(ctypes.c_void_p) != 8:
    raise RuntimeError("Only 64 bit is supported.")

VK_USE_PLATFORM_XLIB_KHR = False
VK_USE_PLATFORM_XLIB_XRANDR_EXT = False
VK_USE_PLATFORM_XCB_KHR = False
VK_USE_PLATFORM_WAYLAND_KHR = False
VK_USE_PLATFORM_DIRECTFB_EXT = False
VK_USE_PLATFORM_ANDROID_KHR = False
VK_USE_PLATFORM_WIN32_KHR = False
VK_USE_PLATFORM_VI_NN = False
VK_USE_PLATFORM_IOS_MVK = False
VK_USE_PLATFORM_MACOS_MVK = False
VK_USE_PLATFORM_METAL_EXT = False
VK_USE_PLATFORM_FUCHSIA = False
VK_USE_PLATFORM_GGP = False
VK_ENABLE_BETA_EXTENSIONS = False

def VK_MAKE_VERSION(major, minor, patch):
    return ctypes.c_uint32(major << 22 | minor << 12 | patch)

VK_DLL = None
VK_FUNCTYPE = None
if platform.system() == "Windows":
    VK_DLL = ctypes.windll.LoadLibrary("vulkan-1")
    VK_FUNCTYPE = ctypes.WINFUNCTYPE
    VK_USE_PLATFORM_WIN32_KHR = True
    import ctypes.wintypes
    class SECURITY_ATTRIBUTES(ctypes.Structure):
        _fields_ = [
            ("nLength", ctypes.wintypes.DWORD),
            ("lpSecurityDescriptor", ctypes.wintypes.LPVOID),
            ("bInheritHandle", ctypes.wintypes.BOOL),
        ]

elif platform.system() == "Linux":
    VK_DLL = ctypes.cdll.LoadLibrary("libvulkan.so.1")
    VK_FUNCTYPE = ctypes.CFUNCTYPE
else:
    raise RuntimeError(f"Unsupported platform: {platform.system()}")

def vk_instance_fn(name, proto):
    def wrapper(vk_instance, *args):
        addr = vkGetInstanceProcAddr(ctypes.cast(vk_instance, VkInstance), name)
        if addr:
            fn = ctypes.cast(addr, proto)
            return fn(vk_instance, *args)
        else:
            raise RuntimeError
    return wrapper

def vk_device_fn(name, proto):
    def wrapper(vk_device, *args):
        addr = vkGetDeviceProcAddr(ctypes.cast(vk_device, VkDevice), name)
        if addr:
            fn = ctypes.cast(addr, proto)
            return fn(vk_device, *args)
        else:
            raise RuntimeError
    return wrapper

class c_enum(ctypes.c_int):
    names = {}
    def __str__(self):
        return self.names.get(self.value, str(self.value))
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return float(self.value)
    def __eq__(self, other):
        return self.value == int(other)
    def __lt__(self, other):
        return self.value < int(other)
    def __le__(self, other):
        return self.value <= int(other)
    def __gt__(self, other):
        return self.value > int(other)
    def __ge__(self, other):
        return self.value >= int(other)
    def __add__(self, other):
        return self.value + int(other)
    def __sub__(self, other):
        return self.value - int(other)
    def __mul__(self, other):
        return self.value * int(other)
    def __truediv__(self, other):
        return self.value / int(other)
    def __floordiv__(self, other):
        return self.value // int(other)
    def __mod__(self, other):
        return self.value % int(other)
    def __pow__(self, other):
        return self.value ** int(other)
    def __lshift__(self, other):
        return self.value << int(other)
    def __rshift__(self, other):
        return self.value >> int(other)
    def __and__(self, other):
        return self.value & int(other)
    def __xor__(self, other):
        return self.value ^ int(other)
    def __or__(self, other):
        return self.value | int(other)
    def __radd__(self, other):
        return int(other) + self.value
    def __rsub__(self, other):
        return int(other) - self.value
    def __rmul__(self, other):
        return int(other) * self.value
    def __rtruediv__(self, other):
        return int(other) / self.value
    def __rfloordiv__(self, other):
        return int(other) // self.value
    def __rmod__(self, other):
        return int(other) % self.value
    def __rpow__(self, other):
        return int(other) ** self.value
    def __rlshift__(self, other):
        return int(other) << self.value
    def __rrshift__(self, other):
        return int(other) >> self.value
    def __rand__(self, other):
        return int(other) & self.value
    def __rxor__(self, other):
        return int(other) ^ self.value
    def __ror__(self, other):
        return int(other) | self.value

#=============================================================================#
# The remainder of this file was generated automatically from the Vulkan API  #
# Registry XML file.                                                          #
#=============================================================================#

VK_API_VERSION = VK_MAKE_VERSION(1, 0, 0)
VK_API_VERSION_1_0 = VK_MAKE_VERSION(1, 0, 0)
VK_API_VERSION_1_1 = VK_MAKE_VERSION(1, 1, 0)
VK_API_VERSION_1_2 = VK_MAKE_VERSION(1, 2, 0)
VK_HEADER_VERSION = 162

ANativeWindow = type('ANativeWindow', (ctypes.Structure,), dict())
AHardwareBuffer = type('AHardwareBuffer', (ctypes.Structure,), dict())
CAMetalLayer = type('CAMetalLayer', (ctypes.Structure,), dict())
VkSampleMask = type('VkSampleMask', (ctypes.c_uint32,), dict())
VkBool32 = type('VkBool32', (ctypes.c_uint32,), dict())
VkFlags = type('VkFlags', (ctypes.c_uint32,), dict())
VkDeviceSize = type('VkDeviceSize', (ctypes.c_uint64,), dict())
VkDeviceAddress = type('VkDeviceAddress', (ctypes.c_uint64,), dict())

VkFramebufferCreateFlags = type('VkFramebufferCreateFlags', (VkFlags,), dict())
VkQueryPoolCreateFlags = type('VkQueryPoolCreateFlags', (VkFlags,), dict())
VkRenderPassCreateFlags = type('VkRenderPassCreateFlags', (VkFlags,), dict())
VkSamplerCreateFlags = type('VkSamplerCreateFlags', (VkFlags,), dict())
VkPipelineLayoutCreateFlags = type('VkPipelineLayoutCreateFlags', (VkFlags,), dict())
VkPipelineCacheCreateFlags = type('VkPipelineCacheCreateFlags', (VkFlags,), dict())
VkPipelineDepthStencilStateCreateFlags = type('VkPipelineDepthStencilStateCreateFlags', (VkFlags,), dict())
VkPipelineDynamicStateCreateFlags = type('VkPipelineDynamicStateCreateFlags', (VkFlags,), dict())
VkPipelineColorBlendStateCreateFlags = type('VkPipelineColorBlendStateCreateFlags', (VkFlags,), dict())
VkPipelineMultisampleStateCreateFlags = type('VkPipelineMultisampleStateCreateFlags', (VkFlags,), dict())
VkPipelineRasterizationStateCreateFlags = type('VkPipelineRasterizationStateCreateFlags', (VkFlags,), dict())
VkPipelineViewportStateCreateFlags = type('VkPipelineViewportStateCreateFlags', (VkFlags,), dict())
VkPipelineTessellationStateCreateFlags = type('VkPipelineTessellationStateCreateFlags', (VkFlags,), dict())
VkPipelineInputAssemblyStateCreateFlags = type('VkPipelineInputAssemblyStateCreateFlags', (VkFlags,), dict())
VkPipelineVertexInputStateCreateFlags = type('VkPipelineVertexInputStateCreateFlags', (VkFlags,), dict())
VkPipelineShaderStageCreateFlags = type('VkPipelineShaderStageCreateFlags', (VkFlags,), dict())
VkDescriptorSetLayoutCreateFlags = type('VkDescriptorSetLayoutCreateFlags', (VkFlags,), dict())
VkBufferViewCreateFlags = type('VkBufferViewCreateFlags', (VkFlags,), dict())
VkInstanceCreateFlags = type('VkInstanceCreateFlags', (VkFlags,), dict())
VkDeviceCreateFlags = type('VkDeviceCreateFlags', (VkFlags,), dict())
VkDeviceQueueCreateFlags = type('VkDeviceQueueCreateFlags', (VkFlags,), dict())
VkQueueFlags = type('VkQueueFlags', (VkFlags,), dict())
VkMemoryPropertyFlags = type('VkMemoryPropertyFlags', (VkFlags,), dict())
VkMemoryHeapFlags = type('VkMemoryHeapFlags', (VkFlags,), dict())
VkAccessFlags = type('VkAccessFlags', (VkFlags,), dict())
VkBufferUsageFlags = type('VkBufferUsageFlags', (VkFlags,), dict())
VkBufferCreateFlags = type('VkBufferCreateFlags', (VkFlags,), dict())
VkShaderStageFlags = type('VkShaderStageFlags', (VkFlags,), dict())
VkImageUsageFlags = type('VkImageUsageFlags', (VkFlags,), dict())
VkImageCreateFlags = type('VkImageCreateFlags', (VkFlags,), dict())
VkImageViewCreateFlags = type('VkImageViewCreateFlags', (VkFlags,), dict())
VkPipelineCreateFlags = type('VkPipelineCreateFlags', (VkFlags,), dict())
VkColorComponentFlags = type('VkColorComponentFlags', (VkFlags,), dict())
VkFenceCreateFlags = type('VkFenceCreateFlags', (VkFlags,), dict())
VkSemaphoreCreateFlags = type('VkSemaphoreCreateFlags', (VkFlags,), dict())
VkFormatFeatureFlags = type('VkFormatFeatureFlags', (VkFlags,), dict())
VkQueryControlFlags = type('VkQueryControlFlags', (VkFlags,), dict())
VkQueryResultFlags = type('VkQueryResultFlags', (VkFlags,), dict())
VkShaderModuleCreateFlags = type('VkShaderModuleCreateFlags', (VkFlags,), dict())
VkEventCreateFlags = type('VkEventCreateFlags', (VkFlags,), dict())
VkCommandPoolCreateFlags = type('VkCommandPoolCreateFlags', (VkFlags,), dict())
VkCommandPoolResetFlags = type('VkCommandPoolResetFlags', (VkFlags,), dict())
VkCommandBufferResetFlags = type('VkCommandBufferResetFlags', (VkFlags,), dict())
VkCommandBufferUsageFlags = type('VkCommandBufferUsageFlags', (VkFlags,), dict())
VkQueryPipelineStatisticFlags = type('VkQueryPipelineStatisticFlags', (VkFlags,), dict())
VkMemoryMapFlags = type('VkMemoryMapFlags', (VkFlags,), dict())
VkImageAspectFlags = type('VkImageAspectFlags', (VkFlags,), dict())
VkSparseMemoryBindFlags = type('VkSparseMemoryBindFlags', (VkFlags,), dict())
VkSparseImageFormatFlags = type('VkSparseImageFormatFlags', (VkFlags,), dict())
VkSubpassDescriptionFlags = type('VkSubpassDescriptionFlags', (VkFlags,), dict())
VkPipelineStageFlags = type('VkPipelineStageFlags', (VkFlags,), dict())
VkSampleCountFlags = type('VkSampleCountFlags', (VkFlags,), dict())
VkAttachmentDescriptionFlags = type('VkAttachmentDescriptionFlags', (VkFlags,), dict())
VkStencilFaceFlags = type('VkStencilFaceFlags', (VkFlags,), dict())
VkCullModeFlags = type('VkCullModeFlags', (VkFlags,), dict())
VkDescriptorPoolCreateFlags = type('VkDescriptorPoolCreateFlags', (VkFlags,), dict())
VkDescriptorPoolResetFlags = type('VkDescriptorPoolResetFlags', (VkFlags,), dict())
VkDependencyFlags = type('VkDependencyFlags', (VkFlags,), dict())
VkSubgroupFeatureFlags = type('VkSubgroupFeatureFlags', (VkFlags,), dict())
VkIndirectCommandsLayoutUsageFlagsNV = type('VkIndirectCommandsLayoutUsageFlagsNV', (VkFlags,), dict())
VkIndirectStateFlagsNV = type('VkIndirectStateFlagsNV', (VkFlags,), dict())
VkGeometryFlagsKHR = type('VkGeometryFlagsKHR', (VkFlags,), dict())
VkGeometryFlagsNV = VkGeometryFlagsKHR
VkGeometryInstanceFlagsKHR = type('VkGeometryInstanceFlagsKHR', (VkFlags,), dict())
VkGeometryInstanceFlagsNV = VkGeometryInstanceFlagsKHR
VkBuildAccelerationStructureFlagsKHR = type('VkBuildAccelerationStructureFlagsKHR', (VkFlags,), dict())
VkBuildAccelerationStructureFlagsNV = VkBuildAccelerationStructureFlagsKHR
VkPrivateDataSlotCreateFlagsEXT = type('VkPrivateDataSlotCreateFlagsEXT', (VkFlags,), dict())
VkAccelerationStructureCreateFlagsKHR = type('VkAccelerationStructureCreateFlagsKHR', (VkFlags,), dict())
VkDescriptorUpdateTemplateCreateFlags = type('VkDescriptorUpdateTemplateCreateFlags', (VkFlags,), dict())
VkDescriptorUpdateTemplateCreateFlagsKHR = VkDescriptorUpdateTemplateCreateFlags
VkPipelineCreationFeedbackFlagsEXT = type('VkPipelineCreationFeedbackFlagsEXT', (VkFlags,), dict())
VkPerformanceCounterDescriptionFlagsKHR = type('VkPerformanceCounterDescriptionFlagsKHR', (VkFlags,), dict())
VkAcquireProfilingLockFlagsKHR = type('VkAcquireProfilingLockFlagsKHR', (VkFlags,), dict())
VkSemaphoreWaitFlags = type('VkSemaphoreWaitFlags', (VkFlags,), dict())
VkSemaphoreWaitFlagsKHR = VkSemaphoreWaitFlags
VkPipelineCompilerControlFlagsAMD = type('VkPipelineCompilerControlFlagsAMD', (VkFlags,), dict())
VkShaderCorePropertiesFlagsAMD = type('VkShaderCorePropertiesFlagsAMD', (VkFlags,), dict())
VkDeviceDiagnosticsConfigFlagsNV = type('VkDeviceDiagnosticsConfigFlagsNV', (VkFlags,), dict())
VkCompositeAlphaFlagsKHR = type('VkCompositeAlphaFlagsKHR', (VkFlags,), dict())
VkDisplayPlaneAlphaFlagsKHR = type('VkDisplayPlaneAlphaFlagsKHR', (VkFlags,), dict())
VkSurfaceTransformFlagsKHR = type('VkSurfaceTransformFlagsKHR', (VkFlags,), dict())
VkSwapchainCreateFlagsKHR = type('VkSwapchainCreateFlagsKHR', (VkFlags,), dict())
VkDisplayModeCreateFlagsKHR = type('VkDisplayModeCreateFlagsKHR', (VkFlags,), dict())
VkDisplaySurfaceCreateFlagsKHR = type('VkDisplaySurfaceCreateFlagsKHR', (VkFlags,), dict())
VkAndroidSurfaceCreateFlagsKHR = type('VkAndroidSurfaceCreateFlagsKHR', (VkFlags,), dict())
VkViSurfaceCreateFlagsNN = type('VkViSurfaceCreateFlagsNN', (VkFlags,), dict())
VkWaylandSurfaceCreateFlagsKHR = type('VkWaylandSurfaceCreateFlagsKHR', (VkFlags,), dict())
VkWin32SurfaceCreateFlagsKHR = type('VkWin32SurfaceCreateFlagsKHR', (VkFlags,), dict())
VkXlibSurfaceCreateFlagsKHR = type('VkXlibSurfaceCreateFlagsKHR', (VkFlags,), dict())
VkXcbSurfaceCreateFlagsKHR = type('VkXcbSurfaceCreateFlagsKHR', (VkFlags,), dict())
VkDirectFBSurfaceCreateFlagsEXT = type('VkDirectFBSurfaceCreateFlagsEXT', (VkFlags,), dict())
VkIOSSurfaceCreateFlagsMVK = type('VkIOSSurfaceCreateFlagsMVK', (VkFlags,), dict())
VkMacOSSurfaceCreateFlagsMVK = type('VkMacOSSurfaceCreateFlagsMVK', (VkFlags,), dict())
VkMetalSurfaceCreateFlagsEXT = type('VkMetalSurfaceCreateFlagsEXT', (VkFlags,), dict())
VkImagePipeSurfaceCreateFlagsFUCHSIA = type('VkImagePipeSurfaceCreateFlagsFUCHSIA', (VkFlags,), dict())
VkStreamDescriptorSurfaceCreateFlagsGGP = type('VkStreamDescriptorSurfaceCreateFlagsGGP', (VkFlags,), dict())
VkHeadlessSurfaceCreateFlagsEXT = type('VkHeadlessSurfaceCreateFlagsEXT', (VkFlags,), dict())
VkPeerMemoryFeatureFlags = type('VkPeerMemoryFeatureFlags', (VkFlags,), dict())
VkPeerMemoryFeatureFlagsKHR = VkPeerMemoryFeatureFlags
VkMemoryAllocateFlags = type('VkMemoryAllocateFlags', (VkFlags,), dict())
VkMemoryAllocateFlagsKHR = VkMemoryAllocateFlags
VkDeviceGroupPresentModeFlagsKHR = type('VkDeviceGroupPresentModeFlagsKHR', (VkFlags,), dict())
VkDebugReportFlagsEXT = type('VkDebugReportFlagsEXT', (VkFlags,), dict())
VkCommandPoolTrimFlags = type('VkCommandPoolTrimFlags', (VkFlags,), dict())
VkCommandPoolTrimFlagsKHR = VkCommandPoolTrimFlags
VkExternalMemoryHandleTypeFlagsNV = type('VkExternalMemoryHandleTypeFlagsNV', (VkFlags,), dict())
VkExternalMemoryFeatureFlagsNV = type('VkExternalMemoryFeatureFlagsNV', (VkFlags,), dict())
VkExternalMemoryHandleTypeFlags = type('VkExternalMemoryHandleTypeFlags', (VkFlags,), dict())
VkExternalMemoryHandleTypeFlagsKHR = VkExternalMemoryHandleTypeFlags
VkExternalMemoryFeatureFlags = type('VkExternalMemoryFeatureFlags', (VkFlags,), dict())
VkExternalMemoryFeatureFlagsKHR = VkExternalMemoryFeatureFlags
VkExternalSemaphoreHandleTypeFlags = type('VkExternalSemaphoreHandleTypeFlags', (VkFlags,), dict())
VkExternalSemaphoreHandleTypeFlagsKHR = VkExternalSemaphoreHandleTypeFlags
VkExternalSemaphoreFeatureFlags = type('VkExternalSemaphoreFeatureFlags', (VkFlags,), dict())
VkExternalSemaphoreFeatureFlagsKHR = VkExternalSemaphoreFeatureFlags
VkSemaphoreImportFlags = type('VkSemaphoreImportFlags', (VkFlags,), dict())
VkSemaphoreImportFlagsKHR = VkSemaphoreImportFlags
VkExternalFenceHandleTypeFlags = type('VkExternalFenceHandleTypeFlags', (VkFlags,), dict())
VkExternalFenceHandleTypeFlagsKHR = VkExternalFenceHandleTypeFlags
VkExternalFenceFeatureFlags = type('VkExternalFenceFeatureFlags', (VkFlags,), dict())
VkExternalFenceFeatureFlagsKHR = VkExternalFenceFeatureFlags
VkFenceImportFlags = type('VkFenceImportFlags', (VkFlags,), dict())
VkFenceImportFlagsKHR = VkFenceImportFlags
VkSurfaceCounterFlagsEXT = type('VkSurfaceCounterFlagsEXT', (VkFlags,), dict())
VkPipelineViewportSwizzleStateCreateFlagsNV = type('VkPipelineViewportSwizzleStateCreateFlagsNV', (VkFlags,), dict())
VkPipelineDiscardRectangleStateCreateFlagsEXT = type('VkPipelineDiscardRectangleStateCreateFlagsEXT', (VkFlags,), dict())
VkPipelineCoverageToColorStateCreateFlagsNV = type('VkPipelineCoverageToColorStateCreateFlagsNV', (VkFlags,), dict())
VkPipelineCoverageModulationStateCreateFlagsNV = type('VkPipelineCoverageModulationStateCreateFlagsNV', (VkFlags,), dict())
VkPipelineCoverageReductionStateCreateFlagsNV = type('VkPipelineCoverageReductionStateCreateFlagsNV', (VkFlags,), dict())
VkValidationCacheCreateFlagsEXT = type('VkValidationCacheCreateFlagsEXT', (VkFlags,), dict())
VkDebugUtilsMessageSeverityFlagsEXT = type('VkDebugUtilsMessageSeverityFlagsEXT', (VkFlags,), dict())
VkDebugUtilsMessageTypeFlagsEXT = type('VkDebugUtilsMessageTypeFlagsEXT', (VkFlags,), dict())
VkDebugUtilsMessengerCreateFlagsEXT = type('VkDebugUtilsMessengerCreateFlagsEXT', (VkFlags,), dict())
VkDebugUtilsMessengerCallbackDataFlagsEXT = type('VkDebugUtilsMessengerCallbackDataFlagsEXT', (VkFlags,), dict())
VkDeviceMemoryReportFlagsEXT = type('VkDeviceMemoryReportFlagsEXT', (VkFlags,), dict())
VkPipelineRasterizationConservativeStateCreateFlagsEXT = type('VkPipelineRasterizationConservativeStateCreateFlagsEXT', (VkFlags,), dict())
VkDescriptorBindingFlags = type('VkDescriptorBindingFlags', (VkFlags,), dict())
VkDescriptorBindingFlagsEXT = VkDescriptorBindingFlags
VkConditionalRenderingFlagsEXT = type('VkConditionalRenderingFlagsEXT', (VkFlags,), dict())
VkResolveModeFlags = type('VkResolveModeFlags', (VkFlags,), dict())
VkResolveModeFlagsKHR = VkResolveModeFlags
VkPipelineRasterizationStateStreamCreateFlagsEXT = type('VkPipelineRasterizationStateStreamCreateFlagsEXT', (VkFlags,), dict())
VkPipelineRasterizationDepthClipStateCreateFlagsEXT = type('VkPipelineRasterizationDepthClipStateCreateFlagsEXT', (VkFlags,), dict())
VkSwapchainImageUsageFlagsANDROID = type('VkSwapchainImageUsageFlagsANDROID', (VkFlags,), dict())
VkToolPurposeFlagsEXT = type('VkToolPurposeFlagsEXT', (VkFlags,), dict())

VkInstance = ctypes.POINTER(type('VkInstance', (ctypes.Structure,), dict()))
VkPhysicalDevice = ctypes.POINTER(type('VkPhysicalDevice', (ctypes.Structure,), dict()))
VkDevice = ctypes.POINTER(type('VkDevice', (ctypes.Structure,), dict()))
VkQueue = ctypes.POINTER(type('VkQueue', (ctypes.Structure,), dict()))
VkCommandBuffer = ctypes.POINTER(type('VkCommandBuffer', (ctypes.Structure,), dict()))
VkDeviceMemory = ctypes.POINTER(type('VkDeviceMemory', (ctypes.Structure,), dict()))
VkCommandPool = ctypes.POINTER(type('VkCommandPool', (ctypes.Structure,), dict()))
VkBuffer = ctypes.POINTER(type('VkBuffer', (ctypes.Structure,), dict()))
VkBufferView = ctypes.POINTER(type('VkBufferView', (ctypes.Structure,), dict()))
VkImage = ctypes.POINTER(type('VkImage', (ctypes.Structure,), dict()))
VkImageView = ctypes.POINTER(type('VkImageView', (ctypes.Structure,), dict()))
VkShaderModule = ctypes.POINTER(type('VkShaderModule', (ctypes.Structure,), dict()))
VkPipeline = ctypes.POINTER(type('VkPipeline', (ctypes.Structure,), dict()))
VkPipelineLayout = ctypes.POINTER(type('VkPipelineLayout', (ctypes.Structure,), dict()))
VkSampler = ctypes.POINTER(type('VkSampler', (ctypes.Structure,), dict()))
VkDescriptorSet = ctypes.POINTER(type('VkDescriptorSet', (ctypes.Structure,), dict()))
VkDescriptorSetLayout = ctypes.POINTER(type('VkDescriptorSetLayout', (ctypes.Structure,), dict()))
VkDescriptorPool = ctypes.POINTER(type('VkDescriptorPool', (ctypes.Structure,), dict()))
VkFence = ctypes.POINTER(type('VkFence', (ctypes.Structure,), dict()))
VkSemaphore = ctypes.POINTER(type('VkSemaphore', (ctypes.Structure,), dict()))
VkEvent = ctypes.POINTER(type('VkEvent', (ctypes.Structure,), dict()))
VkQueryPool = ctypes.POINTER(type('VkQueryPool', (ctypes.Structure,), dict()))
VkFramebuffer = ctypes.POINTER(type('VkFramebuffer', (ctypes.Structure,), dict()))
VkRenderPass = ctypes.POINTER(type('VkRenderPass', (ctypes.Structure,), dict()))
VkPipelineCache = ctypes.POINTER(type('VkPipelineCache', (ctypes.Structure,), dict()))
VkIndirectCommandsLayoutNV = ctypes.POINTER(type('VkIndirectCommandsLayoutNV', (ctypes.Structure,), dict()))
VkDescriptorUpdateTemplate = ctypes.POINTER(type('VkDescriptorUpdateTemplate', (ctypes.Structure,), dict()))
VkDescriptorUpdateTemplateKHR = VkDescriptorUpdateTemplate
VkSamplerYcbcrConversion = ctypes.POINTER(type('VkSamplerYcbcrConversion', (ctypes.Structure,), dict()))
VkSamplerYcbcrConversionKHR = VkSamplerYcbcrConversion
VkValidationCacheEXT = ctypes.POINTER(type('VkValidationCacheEXT', (ctypes.Structure,), dict()))
VkAccelerationStructureKHR = ctypes.POINTER(type('VkAccelerationStructureKHR', (ctypes.Structure,), dict()))
VkAccelerationStructureNV = ctypes.POINTER(type('VkAccelerationStructureNV', (ctypes.Structure,), dict()))
VkPerformanceConfigurationINTEL = ctypes.POINTER(type('VkPerformanceConfigurationINTEL', (ctypes.Structure,), dict()))
VkDeferredOperationKHR = ctypes.POINTER(type('VkDeferredOperationKHR', (ctypes.Structure,), dict()))
VkPrivateDataSlotEXT = ctypes.POINTER(type('VkPrivateDataSlotEXT', (ctypes.Structure,), dict()))
VkDisplayKHR = ctypes.POINTER(type('VkDisplayKHR', (ctypes.Structure,), dict()))
VkDisplayModeKHR = ctypes.POINTER(type('VkDisplayModeKHR', (ctypes.Structure,), dict()))
VkSurfaceKHR = ctypes.POINTER(type('VkSurfaceKHR', (ctypes.Structure,), dict()))
VkSwapchainKHR = ctypes.POINTER(type('VkSwapchainKHR', (ctypes.Structure,), dict()))
VkDebugReportCallbackEXT = ctypes.POINTER(type('VkDebugReportCallbackEXT', (ctypes.Structure,), dict()))
VkDebugUtilsMessengerEXT = ctypes.POINTER(type('VkDebugUtilsMessengerEXT', (ctypes.Structure,), dict()))

# API Constants
VK_MAX_PHYSICAL_DEVICE_NAME_SIZE = 256
VK_UUID_SIZE = 16
VK_LUID_SIZE = 8
VK_LUID_SIZE_KHR = VK_LUID_SIZE
VK_MAX_EXTENSION_NAME_SIZE = 256
VK_MAX_DESCRIPTION_SIZE = 256
VK_MAX_MEMORY_TYPES = 32
VK_MAX_MEMORY_HEAPS = 16
VK_LOD_CLAMP_NONE = 1000.0
VK_REMAINING_MIP_LEVELS = 0xFFFFFFFF
VK_REMAINING_ARRAY_LAYERS = 0xFFFFFFFF
VK_WHOLE_SIZE = 0xFFFFFFFFFFFFFFFF
VK_ATTACHMENT_UNUSED = 0xFFFFFFFF
VK_TRUE = 1
VK_FALSE = 0
VK_QUEUE_FAMILY_IGNORED = 0xFFFFFFFF
VK_QUEUE_FAMILY_EXTERNAL = 0xFFFFFFFF - 1
VK_QUEUE_FAMILY_EXTERNAL_KHR = VK_QUEUE_FAMILY_EXTERNAL
VK_QUEUE_FAMILY_FOREIGN_EXT = 0xFFFFFFFF - 2
VK_SUBPASS_EXTERNAL = 0xFFFFFFFF
VK_MAX_DEVICE_GROUP_SIZE = 32
VK_MAX_DEVICE_GROUP_SIZE_KHR = VK_MAX_DEVICE_GROUP_SIZE
VK_MAX_DRIVER_NAME_SIZE = 256
VK_MAX_DRIVER_NAME_SIZE_KHR = VK_MAX_DRIVER_NAME_SIZE
VK_MAX_DRIVER_INFO_SIZE = 256
VK_MAX_DRIVER_INFO_SIZE_KHR = VK_MAX_DRIVER_INFO_SIZE
VK_SHADER_UNUSED_KHR = 0xFFFFFFFF
VK_SHADER_UNUSED_NV = VK_SHADER_UNUSED_KHR

VkAttachmentLoadOp = type('VkAttachmentLoadOp', (c_enum,), dict(names=dict()))
VkAttachmentLoadOp.names = {
    0 : 'VK_ATTACHMENT_LOAD_OP_LOAD',
    1 : 'VK_ATTACHMENT_LOAD_OP_CLEAR',
    2 : 'VK_ATTACHMENT_LOAD_OP_DONT_CARE',
}
VK_ATTACHMENT_LOAD_OP_LOAD = VkAttachmentLoadOp(0)
VK_ATTACHMENT_LOAD_OP_CLEAR = VkAttachmentLoadOp(1)
VK_ATTACHMENT_LOAD_OP_DONT_CARE = VkAttachmentLoadOp(2)

VkAttachmentStoreOp = type('VkAttachmentStoreOp', (c_enum,), dict(names=dict()))
VkAttachmentStoreOp.names = {
    0 : 'VK_ATTACHMENT_STORE_OP_STORE',
    1 : 'VK_ATTACHMENT_STORE_OP_DONT_CARE',
    1000301000 : 'VK_ATTACHMENT_STORE_OP_NONE_QCOM',
}
VK_ATTACHMENT_STORE_OP_STORE = VkAttachmentStoreOp(0)
VK_ATTACHMENT_STORE_OP_DONT_CARE = VkAttachmentStoreOp(1)
VK_ATTACHMENT_STORE_OP_NONE_QCOM = VkAttachmentStoreOp(1000301000)

VkBlendFactor = type('VkBlendFactor', (c_enum,), dict(names=dict()))
VkBlendFactor.names = {
    0 : 'VK_BLEND_FACTOR_ZERO',
    1 : 'VK_BLEND_FACTOR_ONE',
    2 : 'VK_BLEND_FACTOR_SRC_COLOR',
    3 : 'VK_BLEND_FACTOR_ONE_MINUS_SRC_COLOR',
    4 : 'VK_BLEND_FACTOR_DST_COLOR',
    5 : 'VK_BLEND_FACTOR_ONE_MINUS_DST_COLOR',
    6 : 'VK_BLEND_FACTOR_SRC_ALPHA',
    7 : 'VK_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA',
    8 : 'VK_BLEND_FACTOR_DST_ALPHA',
    9 : 'VK_BLEND_FACTOR_ONE_MINUS_DST_ALPHA',
    10 : 'VK_BLEND_FACTOR_CONSTANT_COLOR',
    11 : 'VK_BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR',
    12 : 'VK_BLEND_FACTOR_CONSTANT_ALPHA',
    13 : 'VK_BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA',
    14 : 'VK_BLEND_FACTOR_SRC_ALPHA_SATURATE',
    15 : 'VK_BLEND_FACTOR_SRC1_COLOR',
    16 : 'VK_BLEND_FACTOR_ONE_MINUS_SRC1_COLOR',
    17 : 'VK_BLEND_FACTOR_SRC1_ALPHA',
    18 : 'VK_BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA',
}
VK_BLEND_FACTOR_ZERO = VkBlendFactor(0)
VK_BLEND_FACTOR_ONE = VkBlendFactor(1)
VK_BLEND_FACTOR_SRC_COLOR = VkBlendFactor(2)
VK_BLEND_FACTOR_ONE_MINUS_SRC_COLOR = VkBlendFactor(3)
VK_BLEND_FACTOR_DST_COLOR = VkBlendFactor(4)
VK_BLEND_FACTOR_ONE_MINUS_DST_COLOR = VkBlendFactor(5)
VK_BLEND_FACTOR_SRC_ALPHA = VkBlendFactor(6)
VK_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA = VkBlendFactor(7)
VK_BLEND_FACTOR_DST_ALPHA = VkBlendFactor(8)
VK_BLEND_FACTOR_ONE_MINUS_DST_ALPHA = VkBlendFactor(9)
VK_BLEND_FACTOR_CONSTANT_COLOR = VkBlendFactor(10)
VK_BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR = VkBlendFactor(11)
VK_BLEND_FACTOR_CONSTANT_ALPHA = VkBlendFactor(12)
VK_BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA = VkBlendFactor(13)
VK_BLEND_FACTOR_SRC_ALPHA_SATURATE = VkBlendFactor(14)
VK_BLEND_FACTOR_SRC1_COLOR = VkBlendFactor(15)
VK_BLEND_FACTOR_ONE_MINUS_SRC1_COLOR = VkBlendFactor(16)
VK_BLEND_FACTOR_SRC1_ALPHA = VkBlendFactor(17)
VK_BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA = VkBlendFactor(18)

VkBlendOp = type('VkBlendOp', (c_enum,), dict(names=dict()))
VkBlendOp.names = {
    0 : 'VK_BLEND_OP_ADD',
    1 : 'VK_BLEND_OP_SUBTRACT',
    2 : 'VK_BLEND_OP_REVERSE_SUBTRACT',
    3 : 'VK_BLEND_OP_MIN',
    4 : 'VK_BLEND_OP_MAX',
    1000148000 : 'VK_BLEND_OP_ZERO_EXT',
    1000148001 : 'VK_BLEND_OP_SRC_EXT',
    1000148002 : 'VK_BLEND_OP_DST_EXT',
    1000148003 : 'VK_BLEND_OP_SRC_OVER_EXT',
    1000148004 : 'VK_BLEND_OP_DST_OVER_EXT',
    1000148005 : 'VK_BLEND_OP_SRC_IN_EXT',
    1000148006 : 'VK_BLEND_OP_DST_IN_EXT',
    1000148007 : 'VK_BLEND_OP_SRC_OUT_EXT',
    1000148008 : 'VK_BLEND_OP_DST_OUT_EXT',
    1000148009 : 'VK_BLEND_OP_SRC_ATOP_EXT',
    1000148010 : 'VK_BLEND_OP_DST_ATOP_EXT',
    1000148011 : 'VK_BLEND_OP_XOR_EXT',
    1000148012 : 'VK_BLEND_OP_MULTIPLY_EXT',
    1000148013 : 'VK_BLEND_OP_SCREEN_EXT',
    1000148014 : 'VK_BLEND_OP_OVERLAY_EXT',
    1000148015 : 'VK_BLEND_OP_DARKEN_EXT',
    1000148016 : 'VK_BLEND_OP_LIGHTEN_EXT',
    1000148017 : 'VK_BLEND_OP_COLORDODGE_EXT',
    1000148018 : 'VK_BLEND_OP_COLORBURN_EXT',
    1000148019 : 'VK_BLEND_OP_HARDLIGHT_EXT',
    1000148020 : 'VK_BLEND_OP_SOFTLIGHT_EXT',
    1000148021 : 'VK_BLEND_OP_DIFFERENCE_EXT',
    1000148022 : 'VK_BLEND_OP_EXCLUSION_EXT',
    1000148023 : 'VK_BLEND_OP_INVERT_EXT',
    1000148024 : 'VK_BLEND_OP_INVERT_RGB_EXT',
    1000148025 : 'VK_BLEND_OP_LINEARDODGE_EXT',
    1000148026 : 'VK_BLEND_OP_LINEARBURN_EXT',
    1000148027 : 'VK_BLEND_OP_VIVIDLIGHT_EXT',
    1000148028 : 'VK_BLEND_OP_LINEARLIGHT_EXT',
    1000148029 : 'VK_BLEND_OP_PINLIGHT_EXT',
    1000148030 : 'VK_BLEND_OP_HARDMIX_EXT',
    1000148031 : 'VK_BLEND_OP_HSL_HUE_EXT',
    1000148032 : 'VK_BLEND_OP_HSL_SATURATION_EXT',
    1000148033 : 'VK_BLEND_OP_HSL_COLOR_EXT',
    1000148034 : 'VK_BLEND_OP_HSL_LUMINOSITY_EXT',
    1000148035 : 'VK_BLEND_OP_PLUS_EXT',
    1000148036 : 'VK_BLEND_OP_PLUS_CLAMPED_EXT',
    1000148037 : 'VK_BLEND_OP_PLUS_CLAMPED_ALPHA_EXT',
    1000148038 : 'VK_BLEND_OP_PLUS_DARKER_EXT',
    1000148039 : 'VK_BLEND_OP_MINUS_EXT',
    1000148040 : 'VK_BLEND_OP_MINUS_CLAMPED_EXT',
    1000148041 : 'VK_BLEND_OP_CONTRAST_EXT',
    1000148042 : 'VK_BLEND_OP_INVERT_OVG_EXT',
    1000148043 : 'VK_BLEND_OP_RED_EXT',
    1000148044 : 'VK_BLEND_OP_GREEN_EXT',
    1000148045 : 'VK_BLEND_OP_BLUE_EXT',
}
VK_BLEND_OP_ADD = VkBlendOp(0)
VK_BLEND_OP_SUBTRACT = VkBlendOp(1)
VK_BLEND_OP_REVERSE_SUBTRACT = VkBlendOp(2)
VK_BLEND_OP_MIN = VkBlendOp(3)
VK_BLEND_OP_MAX = VkBlendOp(4)
VK_BLEND_OP_ZERO_EXT = VkBlendOp(1000148000)
VK_BLEND_OP_SRC_EXT = VkBlendOp(1000148001)
VK_BLEND_OP_DST_EXT = VkBlendOp(1000148002)
VK_BLEND_OP_SRC_OVER_EXT = VkBlendOp(1000148003)
VK_BLEND_OP_DST_OVER_EXT = VkBlendOp(1000148004)
VK_BLEND_OP_SRC_IN_EXT = VkBlendOp(1000148005)
VK_BLEND_OP_DST_IN_EXT = VkBlendOp(1000148006)
VK_BLEND_OP_SRC_OUT_EXT = VkBlendOp(1000148007)
VK_BLEND_OP_DST_OUT_EXT = VkBlendOp(1000148008)
VK_BLEND_OP_SRC_ATOP_EXT = VkBlendOp(1000148009)
VK_BLEND_OP_DST_ATOP_EXT = VkBlendOp(1000148010)
VK_BLEND_OP_XOR_EXT = VkBlendOp(1000148011)
VK_BLEND_OP_MULTIPLY_EXT = VkBlendOp(1000148012)
VK_BLEND_OP_SCREEN_EXT = VkBlendOp(1000148013)
VK_BLEND_OP_OVERLAY_EXT = VkBlendOp(1000148014)
VK_BLEND_OP_DARKEN_EXT = VkBlendOp(1000148015)
VK_BLEND_OP_LIGHTEN_EXT = VkBlendOp(1000148016)
VK_BLEND_OP_COLORDODGE_EXT = VkBlendOp(1000148017)
VK_BLEND_OP_COLORBURN_EXT = VkBlendOp(1000148018)
VK_BLEND_OP_HARDLIGHT_EXT = VkBlendOp(1000148019)
VK_BLEND_OP_SOFTLIGHT_EXT = VkBlendOp(1000148020)
VK_BLEND_OP_DIFFERENCE_EXT = VkBlendOp(1000148021)
VK_BLEND_OP_EXCLUSION_EXT = VkBlendOp(1000148022)
VK_BLEND_OP_INVERT_EXT = VkBlendOp(1000148023)
VK_BLEND_OP_INVERT_RGB_EXT = VkBlendOp(1000148024)
VK_BLEND_OP_LINEARDODGE_EXT = VkBlendOp(1000148025)
VK_BLEND_OP_LINEARBURN_EXT = VkBlendOp(1000148026)
VK_BLEND_OP_VIVIDLIGHT_EXT = VkBlendOp(1000148027)
VK_BLEND_OP_LINEARLIGHT_EXT = VkBlendOp(1000148028)
VK_BLEND_OP_PINLIGHT_EXT = VkBlendOp(1000148029)
VK_BLEND_OP_HARDMIX_EXT = VkBlendOp(1000148030)
VK_BLEND_OP_HSL_HUE_EXT = VkBlendOp(1000148031)
VK_BLEND_OP_HSL_SATURATION_EXT = VkBlendOp(1000148032)
VK_BLEND_OP_HSL_COLOR_EXT = VkBlendOp(1000148033)
VK_BLEND_OP_HSL_LUMINOSITY_EXT = VkBlendOp(1000148034)
VK_BLEND_OP_PLUS_EXT = VkBlendOp(1000148035)
VK_BLEND_OP_PLUS_CLAMPED_EXT = VkBlendOp(1000148036)
VK_BLEND_OP_PLUS_CLAMPED_ALPHA_EXT = VkBlendOp(1000148037)
VK_BLEND_OP_PLUS_DARKER_EXT = VkBlendOp(1000148038)
VK_BLEND_OP_MINUS_EXT = VkBlendOp(1000148039)
VK_BLEND_OP_MINUS_CLAMPED_EXT = VkBlendOp(1000148040)
VK_BLEND_OP_CONTRAST_EXT = VkBlendOp(1000148041)
VK_BLEND_OP_INVERT_OVG_EXT = VkBlendOp(1000148042)
VK_BLEND_OP_RED_EXT = VkBlendOp(1000148043)
VK_BLEND_OP_GREEN_EXT = VkBlendOp(1000148044)
VK_BLEND_OP_BLUE_EXT = VkBlendOp(1000148045)

VkBorderColor = type('VkBorderColor', (c_enum,), dict(names=dict()))
VkBorderColor.names = {
    0 : 'VK_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK',
    1 : 'VK_BORDER_COLOR_INT_TRANSPARENT_BLACK',
    2 : 'VK_BORDER_COLOR_FLOAT_OPAQUE_BLACK',
    3 : 'VK_BORDER_COLOR_INT_OPAQUE_BLACK',
    4 : 'VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE',
    5 : 'VK_BORDER_COLOR_INT_OPAQUE_WHITE',
    1000287003 : 'VK_BORDER_COLOR_FLOAT_CUSTOM_EXT',
    1000287004 : 'VK_BORDER_COLOR_INT_CUSTOM_EXT',
}
VK_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK = VkBorderColor(0)
VK_BORDER_COLOR_INT_TRANSPARENT_BLACK = VkBorderColor(1)
VK_BORDER_COLOR_FLOAT_OPAQUE_BLACK = VkBorderColor(2)
VK_BORDER_COLOR_INT_OPAQUE_BLACK = VkBorderColor(3)
VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE = VkBorderColor(4)
VK_BORDER_COLOR_INT_OPAQUE_WHITE = VkBorderColor(5)
VK_BORDER_COLOR_FLOAT_CUSTOM_EXT = VkBorderColor(1000287003)
VK_BORDER_COLOR_INT_CUSTOM_EXT = VkBorderColor(1000287004)

VkFramebufferCreateFlagBits = type('VkFramebufferCreateFlagBits', (c_enum,), dict(names=dict()))
VkFramebufferCreateFlagBits.names = {
    1 : 'VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT',
}
VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT = VkFramebufferCreateFlagBits(1)
VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT_KHR = VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT

VkQueryPoolCreateFlagBits = type('VkQueryPoolCreateFlagBits', (c_enum,), dict(names=dict()))
VkQueryPoolCreateFlagBits.names = {
}

VkRenderPassCreateFlagBits = type('VkRenderPassCreateFlagBits', (c_enum,), dict(names=dict()))
VkRenderPassCreateFlagBits.names = {
    2 : 'VK_RENDER_PASS_CREATE_TRANSFORM_BIT_QCOM',
}
VK_RENDER_PASS_CREATE_TRANSFORM_BIT_QCOM = VkRenderPassCreateFlagBits(2)

VkSamplerCreateFlagBits = type('VkSamplerCreateFlagBits', (c_enum,), dict(names=dict()))
VkSamplerCreateFlagBits.names = {
    1 : 'VK_SAMPLER_CREATE_SUBSAMPLED_BIT_EXT',
    2 : 'VK_SAMPLER_CREATE_SUBSAMPLED_COARSE_RECONSTRUCTION_BIT_EXT',
}
VK_SAMPLER_CREATE_SUBSAMPLED_BIT_EXT = VkSamplerCreateFlagBits(1)
VK_SAMPLER_CREATE_SUBSAMPLED_COARSE_RECONSTRUCTION_BIT_EXT = VkSamplerCreateFlagBits(2)

VkPipelineCacheHeaderVersion = type('VkPipelineCacheHeaderVersion', (c_enum,), dict(names=dict()))
VkPipelineCacheHeaderVersion.names = {
    1 : 'VK_PIPELINE_CACHE_HEADER_VERSION_ONE',
}
VK_PIPELINE_CACHE_HEADER_VERSION_ONE = VkPipelineCacheHeaderVersion(1)

VkPipelineCacheCreateFlagBits = type('VkPipelineCacheCreateFlagBits', (c_enum,), dict(names=dict()))
VkPipelineCacheCreateFlagBits.names = {
    1 : 'VK_PIPELINE_CACHE_CREATE_EXTERNALLY_SYNCHRONIZED_BIT_EXT',
}
VK_PIPELINE_CACHE_CREATE_EXTERNALLY_SYNCHRONIZED_BIT_EXT = VkPipelineCacheCreateFlagBits(1)

VkPipelineShaderStageCreateFlagBits = type('VkPipelineShaderStageCreateFlagBits', (c_enum,), dict(names=dict()))
VkPipelineShaderStageCreateFlagBits.names = {
    1 : 'VK_PIPELINE_SHADER_STAGE_CREATE_ALLOW_VARYING_SUBGROUP_SIZE_BIT_EXT',
    2 : 'VK_PIPELINE_SHADER_STAGE_CREATE_REQUIRE_FULL_SUBGROUPS_BIT_EXT',
}
VK_PIPELINE_SHADER_STAGE_CREATE_ALLOW_VARYING_SUBGROUP_SIZE_BIT_EXT = VkPipelineShaderStageCreateFlagBits(1)
VK_PIPELINE_SHADER_STAGE_CREATE_REQUIRE_FULL_SUBGROUPS_BIT_EXT = VkPipelineShaderStageCreateFlagBits(2)

VkDescriptorSetLayoutCreateFlagBits = type('VkDescriptorSetLayoutCreateFlagBits', (c_enum,), dict(names=dict()))
VkDescriptorSetLayoutCreateFlagBits.names = {
    2 : 'VK_DESCRIPTOR_SET_LAYOUT_CREATE_UPDATE_AFTER_BIND_POOL_BIT',
    1 : 'VK_DESCRIPTOR_SET_LAYOUT_CREATE_PUSH_DESCRIPTOR_BIT_KHR',
}
VK_DESCRIPTOR_SET_LAYOUT_CREATE_UPDATE_AFTER_BIND_POOL_BIT = VkDescriptorSetLayoutCreateFlagBits(2)
VK_DESCRIPTOR_SET_LAYOUT_CREATE_PUSH_DESCRIPTOR_BIT_KHR = VkDescriptorSetLayoutCreateFlagBits(1)
VK_DESCRIPTOR_SET_LAYOUT_CREATE_UPDATE_AFTER_BIND_POOL_BIT_EXT = VK_DESCRIPTOR_SET_LAYOUT_CREATE_UPDATE_AFTER_BIND_POOL_BIT

VkInstanceCreateFlagBits = type('VkInstanceCreateFlagBits', (c_enum,), dict(names=dict()))
VkInstanceCreateFlagBits.names = {
}

VkDeviceQueueCreateFlagBits = type('VkDeviceQueueCreateFlagBits', (c_enum,), dict(names=dict()))
VkDeviceQueueCreateFlagBits.names = {
    1 : 'VK_DEVICE_QUEUE_CREATE_PROTECTED_BIT',
}
VK_DEVICE_QUEUE_CREATE_PROTECTED_BIT = VkDeviceQueueCreateFlagBits(1)

VkBufferCreateFlagBits = type('VkBufferCreateFlagBits', (c_enum,), dict(names=dict()))
VkBufferCreateFlagBits.names = {
    1 : 'VK_BUFFER_CREATE_SPARSE_BINDING_BIT',
    2 : 'VK_BUFFER_CREATE_SPARSE_RESIDENCY_BIT',
    4 : 'VK_BUFFER_CREATE_SPARSE_ALIASED_BIT',
    8 : 'VK_BUFFER_CREATE_PROTECTED_BIT',
    16 : 'VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT',
}
VK_BUFFER_CREATE_SPARSE_BINDING_BIT = VkBufferCreateFlagBits(1)
VK_BUFFER_CREATE_SPARSE_RESIDENCY_BIT = VkBufferCreateFlagBits(2)
VK_BUFFER_CREATE_SPARSE_ALIASED_BIT = VkBufferCreateFlagBits(4)
VK_BUFFER_CREATE_PROTECTED_BIT = VkBufferCreateFlagBits(8)
VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT = VkBufferCreateFlagBits(16)
VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_EXT = VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT
VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT

VkBufferUsageFlagBits = type('VkBufferUsageFlagBits', (c_enum,), dict(names=dict()))
VkBufferUsageFlagBits.names = {
    1 : 'VK_BUFFER_USAGE_TRANSFER_SRC_BIT',
    2 : 'VK_BUFFER_USAGE_TRANSFER_DST_BIT',
    4 : 'VK_BUFFER_USAGE_UNIFORM_TEXEL_BUFFER_BIT',
    8 : 'VK_BUFFER_USAGE_STORAGE_TEXEL_BUFFER_BIT',
    16 : 'VK_BUFFER_USAGE_UNIFORM_BUFFER_BIT',
    32 : 'VK_BUFFER_USAGE_STORAGE_BUFFER_BIT',
    64 : 'VK_BUFFER_USAGE_INDEX_BUFFER_BIT',
    128 : 'VK_BUFFER_USAGE_VERTEX_BUFFER_BIT',
    256 : 'VK_BUFFER_USAGE_INDIRECT_BUFFER_BIT',
    131072 : 'VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT',
    2048 : 'VK_BUFFER_USAGE_TRANSFORM_FEEDBACK_BUFFER_BIT_EXT',
    4096 : 'VK_BUFFER_USAGE_TRANSFORM_FEEDBACK_COUNTER_BUFFER_BIT_EXT',
    512 : 'VK_BUFFER_USAGE_CONDITIONAL_RENDERING_BIT_EXT',
    524288 : 'VK_BUFFER_USAGE_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT_KHR',
    1048576 : 'VK_BUFFER_USAGE_ACCELERATION_STRUCTURE_STORAGE_BIT_KHR',
    1024 : 'VK_BUFFER_USAGE_SHADER_BINDING_TABLE_BIT_KHR',
}
VK_BUFFER_USAGE_TRANSFER_SRC_BIT = VkBufferUsageFlagBits(1)
VK_BUFFER_USAGE_TRANSFER_DST_BIT = VkBufferUsageFlagBits(2)
VK_BUFFER_USAGE_UNIFORM_TEXEL_BUFFER_BIT = VkBufferUsageFlagBits(4)
VK_BUFFER_USAGE_STORAGE_TEXEL_BUFFER_BIT = VkBufferUsageFlagBits(8)
VK_BUFFER_USAGE_UNIFORM_BUFFER_BIT = VkBufferUsageFlagBits(16)
VK_BUFFER_USAGE_STORAGE_BUFFER_BIT = VkBufferUsageFlagBits(32)
VK_BUFFER_USAGE_INDEX_BUFFER_BIT = VkBufferUsageFlagBits(64)
VK_BUFFER_USAGE_VERTEX_BUFFER_BIT = VkBufferUsageFlagBits(128)
VK_BUFFER_USAGE_INDIRECT_BUFFER_BIT = VkBufferUsageFlagBits(256)
VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT = VkBufferUsageFlagBits(131072)
VK_BUFFER_USAGE_TRANSFORM_FEEDBACK_BUFFER_BIT_EXT = VkBufferUsageFlagBits(2048)
VK_BUFFER_USAGE_TRANSFORM_FEEDBACK_COUNTER_BUFFER_BIT_EXT = VkBufferUsageFlagBits(4096)
VK_BUFFER_USAGE_CONDITIONAL_RENDERING_BIT_EXT = VkBufferUsageFlagBits(512)
VK_BUFFER_USAGE_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT_KHR = VkBufferUsageFlagBits(524288)
VK_BUFFER_USAGE_ACCELERATION_STRUCTURE_STORAGE_BIT_KHR = VkBufferUsageFlagBits(1048576)
VK_BUFFER_USAGE_SHADER_BINDING_TABLE_BIT_KHR = VkBufferUsageFlagBits(1024)
VK_BUFFER_USAGE_RAY_TRACING_BIT_NV = VK_BUFFER_USAGE_SHADER_BINDING_TABLE_BIT_KHR
VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT_EXT = VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT
VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT_KHR = VK_BUFFER_USAGE_SHADER_DEVICE_ADDRESS_BIT

VkColorComponentFlagBits = type('VkColorComponentFlagBits', (c_enum,), dict(names=dict()))
VkColorComponentFlagBits.names = {
    1 : 'VK_COLOR_COMPONENT_R_BIT',
    2 : 'VK_COLOR_COMPONENT_G_BIT',
    4 : 'VK_COLOR_COMPONENT_B_BIT',
    8 : 'VK_COLOR_COMPONENT_A_BIT',
}
VK_COLOR_COMPONENT_R_BIT = VkColorComponentFlagBits(1)
VK_COLOR_COMPONENT_G_BIT = VkColorComponentFlagBits(2)
VK_COLOR_COMPONENT_B_BIT = VkColorComponentFlagBits(4)
VK_COLOR_COMPONENT_A_BIT = VkColorComponentFlagBits(8)

VkComponentSwizzle = type('VkComponentSwizzle', (c_enum,), dict(names=dict()))
VkComponentSwizzle.names = {
    0 : 'VK_COMPONENT_SWIZZLE_IDENTITY',
    1 : 'VK_COMPONENT_SWIZZLE_ZERO',
    2 : 'VK_COMPONENT_SWIZZLE_ONE',
    3 : 'VK_COMPONENT_SWIZZLE_R',
    4 : 'VK_COMPONENT_SWIZZLE_G',
    5 : 'VK_COMPONENT_SWIZZLE_B',
    6 : 'VK_COMPONENT_SWIZZLE_A',
}
VK_COMPONENT_SWIZZLE_IDENTITY = VkComponentSwizzle(0)
VK_COMPONENT_SWIZZLE_ZERO = VkComponentSwizzle(1)
VK_COMPONENT_SWIZZLE_ONE = VkComponentSwizzle(2)
VK_COMPONENT_SWIZZLE_R = VkComponentSwizzle(3)
VK_COMPONENT_SWIZZLE_G = VkComponentSwizzle(4)
VK_COMPONENT_SWIZZLE_B = VkComponentSwizzle(5)
VK_COMPONENT_SWIZZLE_A = VkComponentSwizzle(6)

VkCommandPoolCreateFlagBits = type('VkCommandPoolCreateFlagBits', (c_enum,), dict(names=dict()))
VkCommandPoolCreateFlagBits.names = {
    1 : 'VK_COMMAND_POOL_CREATE_TRANSIENT_BIT',
    2 : 'VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT',
    4 : 'VK_COMMAND_POOL_CREATE_PROTECTED_BIT',
}
VK_COMMAND_POOL_CREATE_TRANSIENT_BIT = VkCommandPoolCreateFlagBits(1)
VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT = VkCommandPoolCreateFlagBits(2)
VK_COMMAND_POOL_CREATE_PROTECTED_BIT = VkCommandPoolCreateFlagBits(4)

VkCommandPoolResetFlagBits = type('VkCommandPoolResetFlagBits', (c_enum,), dict(names=dict()))
VkCommandPoolResetFlagBits.names = {
    1 : 'VK_COMMAND_POOL_RESET_RELEASE_RESOURCES_BIT',
}
VK_COMMAND_POOL_RESET_RELEASE_RESOURCES_BIT = VkCommandPoolResetFlagBits(1)

VkCommandBufferResetFlagBits = type('VkCommandBufferResetFlagBits', (c_enum,), dict(names=dict()))
VkCommandBufferResetFlagBits.names = {
    1 : 'VK_COMMAND_BUFFER_RESET_RELEASE_RESOURCES_BIT',
}
VK_COMMAND_BUFFER_RESET_RELEASE_RESOURCES_BIT = VkCommandBufferResetFlagBits(1)

VkCommandBufferLevel = type('VkCommandBufferLevel', (c_enum,), dict(names=dict()))
VkCommandBufferLevel.names = {
    0 : 'VK_COMMAND_BUFFER_LEVEL_PRIMARY',
    1 : 'VK_COMMAND_BUFFER_LEVEL_SECONDARY',
}
VK_COMMAND_BUFFER_LEVEL_PRIMARY = VkCommandBufferLevel(0)
VK_COMMAND_BUFFER_LEVEL_SECONDARY = VkCommandBufferLevel(1)

VkCommandBufferUsageFlagBits = type('VkCommandBufferUsageFlagBits', (c_enum,), dict(names=dict()))
VkCommandBufferUsageFlagBits.names = {
    1 : 'VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT',
    2 : 'VK_COMMAND_BUFFER_USAGE_RENDER_PASS_CONTINUE_BIT',
    4 : 'VK_COMMAND_BUFFER_USAGE_SIMULTANEOUS_USE_BIT',
}
VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT = VkCommandBufferUsageFlagBits(1)
VK_COMMAND_BUFFER_USAGE_RENDER_PASS_CONTINUE_BIT = VkCommandBufferUsageFlagBits(2)
VK_COMMAND_BUFFER_USAGE_SIMULTANEOUS_USE_BIT = VkCommandBufferUsageFlagBits(4)

VkCompareOp = type('VkCompareOp', (c_enum,), dict(names=dict()))
VkCompareOp.names = {
    0 : 'VK_COMPARE_OP_NEVER',
    1 : 'VK_COMPARE_OP_LESS',
    2 : 'VK_COMPARE_OP_EQUAL',
    3 : 'VK_COMPARE_OP_LESS_OR_EQUAL',
    4 : 'VK_COMPARE_OP_GREATER',
    5 : 'VK_COMPARE_OP_NOT_EQUAL',
    6 : 'VK_COMPARE_OP_GREATER_OR_EQUAL',
    7 : 'VK_COMPARE_OP_ALWAYS',
}
VK_COMPARE_OP_NEVER = VkCompareOp(0)
VK_COMPARE_OP_LESS = VkCompareOp(1)
VK_COMPARE_OP_EQUAL = VkCompareOp(2)
VK_COMPARE_OP_LESS_OR_EQUAL = VkCompareOp(3)
VK_COMPARE_OP_GREATER = VkCompareOp(4)
VK_COMPARE_OP_NOT_EQUAL = VkCompareOp(5)
VK_COMPARE_OP_GREATER_OR_EQUAL = VkCompareOp(6)
VK_COMPARE_OP_ALWAYS = VkCompareOp(7)

VkCullModeFlagBits = type('VkCullModeFlagBits', (c_enum,), dict(names=dict()))
VkCullModeFlagBits.names = {
    0 : 'VK_CULL_MODE_NONE',
    1 : 'VK_CULL_MODE_FRONT_BIT',
    2 : 'VK_CULL_MODE_BACK_BIT',
    0x00000003 : 'VK_CULL_MODE_FRONT_AND_BACK',
}
VK_CULL_MODE_NONE = VkCullModeFlagBits(0)
VK_CULL_MODE_FRONT_BIT = VkCullModeFlagBits(1)
VK_CULL_MODE_BACK_BIT = VkCullModeFlagBits(2)
VK_CULL_MODE_FRONT_AND_BACK = VkCullModeFlagBits(0x00000003)

VkDescriptorType = type('VkDescriptorType', (c_enum,), dict(names=dict()))
VkDescriptorType.names = {
    0 : 'VK_DESCRIPTOR_TYPE_SAMPLER',
    1 : 'VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER',
    2 : 'VK_DESCRIPTOR_TYPE_SAMPLED_IMAGE',
    3 : 'VK_DESCRIPTOR_TYPE_STORAGE_IMAGE',
    4 : 'VK_DESCRIPTOR_TYPE_UNIFORM_TEXEL_BUFFER',
    5 : 'VK_DESCRIPTOR_TYPE_STORAGE_TEXEL_BUFFER',
    6 : 'VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER',
    7 : 'VK_DESCRIPTOR_TYPE_STORAGE_BUFFER',
    8 : 'VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER_DYNAMIC',
    9 : 'VK_DESCRIPTOR_TYPE_STORAGE_BUFFER_DYNAMIC',
    10 : 'VK_DESCRIPTOR_TYPE_INPUT_ATTACHMENT',
    1000138000 : 'VK_DESCRIPTOR_TYPE_INLINE_UNIFORM_BLOCK_EXT',
    1000150000 : 'VK_DESCRIPTOR_TYPE_ACCELERATION_STRUCTURE_KHR',
    1000165000 : 'VK_DESCRIPTOR_TYPE_ACCELERATION_STRUCTURE_NV',
}
VK_DESCRIPTOR_TYPE_SAMPLER = VkDescriptorType(0)
VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER = VkDescriptorType(1)
VK_DESCRIPTOR_TYPE_SAMPLED_IMAGE = VkDescriptorType(2)
VK_DESCRIPTOR_TYPE_STORAGE_IMAGE = VkDescriptorType(3)
VK_DESCRIPTOR_TYPE_UNIFORM_TEXEL_BUFFER = VkDescriptorType(4)
VK_DESCRIPTOR_TYPE_STORAGE_TEXEL_BUFFER = VkDescriptorType(5)
VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER = VkDescriptorType(6)
VK_DESCRIPTOR_TYPE_STORAGE_BUFFER = VkDescriptorType(7)
VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER_DYNAMIC = VkDescriptorType(8)
VK_DESCRIPTOR_TYPE_STORAGE_BUFFER_DYNAMIC = VkDescriptorType(9)
VK_DESCRIPTOR_TYPE_INPUT_ATTACHMENT = VkDescriptorType(10)
VK_DESCRIPTOR_TYPE_INLINE_UNIFORM_BLOCK_EXT = VkDescriptorType(1000138000)
VK_DESCRIPTOR_TYPE_ACCELERATION_STRUCTURE_KHR = VkDescriptorType(1000150000)
VK_DESCRIPTOR_TYPE_ACCELERATION_STRUCTURE_NV = VkDescriptorType(1000165000)

VkDeviceCreateFlagBits = type('VkDeviceCreateFlagBits', (c_enum,), dict(names=dict()))
VkDeviceCreateFlagBits.names = {
}

VkDynamicState = type('VkDynamicState', (c_enum,), dict(names=dict()))
VkDynamicState.names = {
    0 : 'VK_DYNAMIC_STATE_VIEWPORT',
    1 : 'VK_DYNAMIC_STATE_SCISSOR',
    2 : 'VK_DYNAMIC_STATE_LINE_WIDTH',
    3 : 'VK_DYNAMIC_STATE_DEPTH_BIAS',
    4 : 'VK_DYNAMIC_STATE_BLEND_CONSTANTS',
    5 : 'VK_DYNAMIC_STATE_DEPTH_BOUNDS',
    6 : 'VK_DYNAMIC_STATE_STENCIL_COMPARE_MASK',
    7 : 'VK_DYNAMIC_STATE_STENCIL_WRITE_MASK',
    8 : 'VK_DYNAMIC_STATE_STENCIL_REFERENCE',
    1000087000 : 'VK_DYNAMIC_STATE_VIEWPORT_W_SCALING_NV',
    1000099000 : 'VK_DYNAMIC_STATE_DISCARD_RECTANGLE_EXT',
    1000143000 : 'VK_DYNAMIC_STATE_SAMPLE_LOCATIONS_EXT',
    1000347000 : 'VK_DYNAMIC_STATE_RAY_TRACING_PIPELINE_STACK_SIZE_KHR',
    1000164004 : 'VK_DYNAMIC_STATE_VIEWPORT_SHADING_RATE_PALETTE_NV',
    1000164006 : 'VK_DYNAMIC_STATE_VIEWPORT_COARSE_SAMPLE_ORDER_NV',
    1000205001 : 'VK_DYNAMIC_STATE_EXCLUSIVE_SCISSOR_NV',
    1000226000 : 'VK_DYNAMIC_STATE_FRAGMENT_SHADING_RATE_KHR',
    1000259000 : 'VK_DYNAMIC_STATE_LINE_STIPPLE_EXT',
    1000267000 : 'VK_DYNAMIC_STATE_CULL_MODE_EXT',
    1000267001 : 'VK_DYNAMIC_STATE_FRONT_FACE_EXT',
    1000267002 : 'VK_DYNAMIC_STATE_PRIMITIVE_TOPOLOGY_EXT',
    1000267003 : 'VK_DYNAMIC_STATE_VIEWPORT_WITH_COUNT_EXT',
    1000267004 : 'VK_DYNAMIC_STATE_SCISSOR_WITH_COUNT_EXT',
    1000267005 : 'VK_DYNAMIC_STATE_VERTEX_INPUT_BINDING_STRIDE_EXT',
    1000267006 : 'VK_DYNAMIC_STATE_DEPTH_TEST_ENABLE_EXT',
    1000267007 : 'VK_DYNAMIC_STATE_DEPTH_WRITE_ENABLE_EXT',
    1000267008 : 'VK_DYNAMIC_STATE_DEPTH_COMPARE_OP_EXT',
    1000267009 : 'VK_DYNAMIC_STATE_DEPTH_BOUNDS_TEST_ENABLE_EXT',
    1000267010 : 'VK_DYNAMIC_STATE_STENCIL_TEST_ENABLE_EXT',
    1000267011 : 'VK_DYNAMIC_STATE_STENCIL_OP_EXT',
}
VK_DYNAMIC_STATE_VIEWPORT = VkDynamicState(0)
VK_DYNAMIC_STATE_SCISSOR = VkDynamicState(1)
VK_DYNAMIC_STATE_LINE_WIDTH = VkDynamicState(2)
VK_DYNAMIC_STATE_DEPTH_BIAS = VkDynamicState(3)
VK_DYNAMIC_STATE_BLEND_CONSTANTS = VkDynamicState(4)
VK_DYNAMIC_STATE_DEPTH_BOUNDS = VkDynamicState(5)
VK_DYNAMIC_STATE_STENCIL_COMPARE_MASK = VkDynamicState(6)
VK_DYNAMIC_STATE_STENCIL_WRITE_MASK = VkDynamicState(7)
VK_DYNAMIC_STATE_STENCIL_REFERENCE = VkDynamicState(8)
VK_DYNAMIC_STATE_VIEWPORT_W_SCALING_NV = VkDynamicState(1000087000)
VK_DYNAMIC_STATE_DISCARD_RECTANGLE_EXT = VkDynamicState(1000099000)
VK_DYNAMIC_STATE_SAMPLE_LOCATIONS_EXT = VkDynamicState(1000143000)
VK_DYNAMIC_STATE_RAY_TRACING_PIPELINE_STACK_SIZE_KHR = VkDynamicState(1000347000)
VK_DYNAMIC_STATE_VIEWPORT_SHADING_RATE_PALETTE_NV = VkDynamicState(1000164004)
VK_DYNAMIC_STATE_VIEWPORT_COARSE_SAMPLE_ORDER_NV = VkDynamicState(1000164006)
VK_DYNAMIC_STATE_EXCLUSIVE_SCISSOR_NV = VkDynamicState(1000205001)
VK_DYNAMIC_STATE_FRAGMENT_SHADING_RATE_KHR = VkDynamicState(1000226000)
VK_DYNAMIC_STATE_LINE_STIPPLE_EXT = VkDynamicState(1000259000)
VK_DYNAMIC_STATE_CULL_MODE_EXT = VkDynamicState(1000267000)
VK_DYNAMIC_STATE_FRONT_FACE_EXT = VkDynamicState(1000267001)
VK_DYNAMIC_STATE_PRIMITIVE_TOPOLOGY_EXT = VkDynamicState(1000267002)
VK_DYNAMIC_STATE_VIEWPORT_WITH_COUNT_EXT = VkDynamicState(1000267003)
VK_DYNAMIC_STATE_SCISSOR_WITH_COUNT_EXT = VkDynamicState(1000267004)
VK_DYNAMIC_STATE_VERTEX_INPUT_BINDING_STRIDE_EXT = VkDynamicState(1000267005)
VK_DYNAMIC_STATE_DEPTH_TEST_ENABLE_EXT = VkDynamicState(1000267006)
VK_DYNAMIC_STATE_DEPTH_WRITE_ENABLE_EXT = VkDynamicState(1000267007)
VK_DYNAMIC_STATE_DEPTH_COMPARE_OP_EXT = VkDynamicState(1000267008)
VK_DYNAMIC_STATE_DEPTH_BOUNDS_TEST_ENABLE_EXT = VkDynamicState(1000267009)
VK_DYNAMIC_STATE_STENCIL_TEST_ENABLE_EXT = VkDynamicState(1000267010)
VK_DYNAMIC_STATE_STENCIL_OP_EXT = VkDynamicState(1000267011)

VkFenceCreateFlagBits = type('VkFenceCreateFlagBits', (c_enum,), dict(names=dict()))
VkFenceCreateFlagBits.names = {
    1 : 'VK_FENCE_CREATE_SIGNALED_BIT',
}
VK_FENCE_CREATE_SIGNALED_BIT = VkFenceCreateFlagBits(1)

VkPolygonMode = type('VkPolygonMode', (c_enum,), dict(names=dict()))
VkPolygonMode.names = {
    0 : 'VK_POLYGON_MODE_FILL',
    1 : 'VK_POLYGON_MODE_LINE',
    2 : 'VK_POLYGON_MODE_POINT',
    1000153000 : 'VK_POLYGON_MODE_FILL_RECTANGLE_NV',
}
VK_POLYGON_MODE_FILL = VkPolygonMode(0)
VK_POLYGON_MODE_LINE = VkPolygonMode(1)
VK_POLYGON_MODE_POINT = VkPolygonMode(2)
VK_POLYGON_MODE_FILL_RECTANGLE_NV = VkPolygonMode(1000153000)

VkFormat = type('VkFormat', (c_enum,), dict(names=dict()))
VkFormat.names = {
    0 : 'VK_FORMAT_UNDEFINED',
    1 : 'VK_FORMAT_R4G4_UNORM_PACK8',
    2 : 'VK_FORMAT_R4G4B4A4_UNORM_PACK16',
    3 : 'VK_FORMAT_B4G4R4A4_UNORM_PACK16',
    4 : 'VK_FORMAT_R5G6B5_UNORM_PACK16',
    5 : 'VK_FORMAT_B5G6R5_UNORM_PACK16',
    6 : 'VK_FORMAT_R5G5B5A1_UNORM_PACK16',
    7 : 'VK_FORMAT_B5G5R5A1_UNORM_PACK16',
    8 : 'VK_FORMAT_A1R5G5B5_UNORM_PACK16',
    9 : 'VK_FORMAT_R8_UNORM',
    10 : 'VK_FORMAT_R8_SNORM',
    11 : 'VK_FORMAT_R8_USCALED',
    12 : 'VK_FORMAT_R8_SSCALED',
    13 : 'VK_FORMAT_R8_UINT',
    14 : 'VK_FORMAT_R8_SINT',
    15 : 'VK_FORMAT_R8_SRGB',
    16 : 'VK_FORMAT_R8G8_UNORM',
    17 : 'VK_FORMAT_R8G8_SNORM',
    18 : 'VK_FORMAT_R8G8_USCALED',
    19 : 'VK_FORMAT_R8G8_SSCALED',
    20 : 'VK_FORMAT_R8G8_UINT',
    21 : 'VK_FORMAT_R8G8_SINT',
    22 : 'VK_FORMAT_R8G8_SRGB',
    23 : 'VK_FORMAT_R8G8B8_UNORM',
    24 : 'VK_FORMAT_R8G8B8_SNORM',
    25 : 'VK_FORMAT_R8G8B8_USCALED',
    26 : 'VK_FORMAT_R8G8B8_SSCALED',
    27 : 'VK_FORMAT_R8G8B8_UINT',
    28 : 'VK_FORMAT_R8G8B8_SINT',
    29 : 'VK_FORMAT_R8G8B8_SRGB',
    30 : 'VK_FORMAT_B8G8R8_UNORM',
    31 : 'VK_FORMAT_B8G8R8_SNORM',
    32 : 'VK_FORMAT_B8G8R8_USCALED',
    33 : 'VK_FORMAT_B8G8R8_SSCALED',
    34 : 'VK_FORMAT_B8G8R8_UINT',
    35 : 'VK_FORMAT_B8G8R8_SINT',
    36 : 'VK_FORMAT_B8G8R8_SRGB',
    37 : 'VK_FORMAT_R8G8B8A8_UNORM',
    38 : 'VK_FORMAT_R8G8B8A8_SNORM',
    39 : 'VK_FORMAT_R8G8B8A8_USCALED',
    40 : 'VK_FORMAT_R8G8B8A8_SSCALED',
    41 : 'VK_FORMAT_R8G8B8A8_UINT',
    42 : 'VK_FORMAT_R8G8B8A8_SINT',
    43 : 'VK_FORMAT_R8G8B8A8_SRGB',
    44 : 'VK_FORMAT_B8G8R8A8_UNORM',
    45 : 'VK_FORMAT_B8G8R8A8_SNORM',
    46 : 'VK_FORMAT_B8G8R8A8_USCALED',
    47 : 'VK_FORMAT_B8G8R8A8_SSCALED',
    48 : 'VK_FORMAT_B8G8R8A8_UINT',
    49 : 'VK_FORMAT_B8G8R8A8_SINT',
    50 : 'VK_FORMAT_B8G8R8A8_SRGB',
    51 : 'VK_FORMAT_A8B8G8R8_UNORM_PACK32',
    52 : 'VK_FORMAT_A8B8G8R8_SNORM_PACK32',
    53 : 'VK_FORMAT_A8B8G8R8_USCALED_PACK32',
    54 : 'VK_FORMAT_A8B8G8R8_SSCALED_PACK32',
    55 : 'VK_FORMAT_A8B8G8R8_UINT_PACK32',
    56 : 'VK_FORMAT_A8B8G8R8_SINT_PACK32',
    57 : 'VK_FORMAT_A8B8G8R8_SRGB_PACK32',
    58 : 'VK_FORMAT_A2R10G10B10_UNORM_PACK32',
    59 : 'VK_FORMAT_A2R10G10B10_SNORM_PACK32',
    60 : 'VK_FORMAT_A2R10G10B10_USCALED_PACK32',
    61 : 'VK_FORMAT_A2R10G10B10_SSCALED_PACK32',
    62 : 'VK_FORMAT_A2R10G10B10_UINT_PACK32',
    63 : 'VK_FORMAT_A2R10G10B10_SINT_PACK32',
    64 : 'VK_FORMAT_A2B10G10R10_UNORM_PACK32',
    65 : 'VK_FORMAT_A2B10G10R10_SNORM_PACK32',
    66 : 'VK_FORMAT_A2B10G10R10_USCALED_PACK32',
    67 : 'VK_FORMAT_A2B10G10R10_SSCALED_PACK32',
    68 : 'VK_FORMAT_A2B10G10R10_UINT_PACK32',
    69 : 'VK_FORMAT_A2B10G10R10_SINT_PACK32',
    70 : 'VK_FORMAT_R16_UNORM',
    71 : 'VK_FORMAT_R16_SNORM',
    72 : 'VK_FORMAT_R16_USCALED',
    73 : 'VK_FORMAT_R16_SSCALED',
    74 : 'VK_FORMAT_R16_UINT',
    75 : 'VK_FORMAT_R16_SINT',
    76 : 'VK_FORMAT_R16_SFLOAT',
    77 : 'VK_FORMAT_R16G16_UNORM',
    78 : 'VK_FORMAT_R16G16_SNORM',
    79 : 'VK_FORMAT_R16G16_USCALED',
    80 : 'VK_FORMAT_R16G16_SSCALED',
    81 : 'VK_FORMAT_R16G16_UINT',
    82 : 'VK_FORMAT_R16G16_SINT',
    83 : 'VK_FORMAT_R16G16_SFLOAT',
    84 : 'VK_FORMAT_R16G16B16_UNORM',
    85 : 'VK_FORMAT_R16G16B16_SNORM',
    86 : 'VK_FORMAT_R16G16B16_USCALED',
    87 : 'VK_FORMAT_R16G16B16_SSCALED',
    88 : 'VK_FORMAT_R16G16B16_UINT',
    89 : 'VK_FORMAT_R16G16B16_SINT',
    90 : 'VK_FORMAT_R16G16B16_SFLOAT',
    91 : 'VK_FORMAT_R16G16B16A16_UNORM',
    92 : 'VK_FORMAT_R16G16B16A16_SNORM',
    93 : 'VK_FORMAT_R16G16B16A16_USCALED',
    94 : 'VK_FORMAT_R16G16B16A16_SSCALED',
    95 : 'VK_FORMAT_R16G16B16A16_UINT',
    96 : 'VK_FORMAT_R16G16B16A16_SINT',
    97 : 'VK_FORMAT_R16G16B16A16_SFLOAT',
    98 : 'VK_FORMAT_R32_UINT',
    99 : 'VK_FORMAT_R32_SINT',
    100 : 'VK_FORMAT_R32_SFLOAT',
    101 : 'VK_FORMAT_R32G32_UINT',
    102 : 'VK_FORMAT_R32G32_SINT',
    103 : 'VK_FORMAT_R32G32_SFLOAT',
    104 : 'VK_FORMAT_R32G32B32_UINT',
    105 : 'VK_FORMAT_R32G32B32_SINT',
    106 : 'VK_FORMAT_R32G32B32_SFLOAT',
    107 : 'VK_FORMAT_R32G32B32A32_UINT',
    108 : 'VK_FORMAT_R32G32B32A32_SINT',
    109 : 'VK_FORMAT_R32G32B32A32_SFLOAT',
    110 : 'VK_FORMAT_R64_UINT',
    111 : 'VK_FORMAT_R64_SINT',
    112 : 'VK_FORMAT_R64_SFLOAT',
    113 : 'VK_FORMAT_R64G64_UINT',
    114 : 'VK_FORMAT_R64G64_SINT',
    115 : 'VK_FORMAT_R64G64_SFLOAT',
    116 : 'VK_FORMAT_R64G64B64_UINT',
    117 : 'VK_FORMAT_R64G64B64_SINT',
    118 : 'VK_FORMAT_R64G64B64_SFLOAT',
    119 : 'VK_FORMAT_R64G64B64A64_UINT',
    120 : 'VK_FORMAT_R64G64B64A64_SINT',
    121 : 'VK_FORMAT_R64G64B64A64_SFLOAT',
    122 : 'VK_FORMAT_B10G11R11_UFLOAT_PACK32',
    123 : 'VK_FORMAT_E5B9G9R9_UFLOAT_PACK32',
    124 : 'VK_FORMAT_D16_UNORM',
    125 : 'VK_FORMAT_X8_D24_UNORM_PACK32',
    126 : 'VK_FORMAT_D32_SFLOAT',
    127 : 'VK_FORMAT_S8_UINT',
    128 : 'VK_FORMAT_D16_UNORM_S8_UINT',
    129 : 'VK_FORMAT_D24_UNORM_S8_UINT',
    130 : 'VK_FORMAT_D32_SFLOAT_S8_UINT',
    131 : 'VK_FORMAT_BC1_RGB_UNORM_BLOCK',
    132 : 'VK_FORMAT_BC1_RGB_SRGB_BLOCK',
    133 : 'VK_FORMAT_BC1_RGBA_UNORM_BLOCK',
    134 : 'VK_FORMAT_BC1_RGBA_SRGB_BLOCK',
    135 : 'VK_FORMAT_BC2_UNORM_BLOCK',
    136 : 'VK_FORMAT_BC2_SRGB_BLOCK',
    137 : 'VK_FORMAT_BC3_UNORM_BLOCK',
    138 : 'VK_FORMAT_BC3_SRGB_BLOCK',
    139 : 'VK_FORMAT_BC4_UNORM_BLOCK',
    140 : 'VK_FORMAT_BC4_SNORM_BLOCK',
    141 : 'VK_FORMAT_BC5_UNORM_BLOCK',
    142 : 'VK_FORMAT_BC5_SNORM_BLOCK',
    143 : 'VK_FORMAT_BC6H_UFLOAT_BLOCK',
    144 : 'VK_FORMAT_BC6H_SFLOAT_BLOCK',
    145 : 'VK_FORMAT_BC7_UNORM_BLOCK',
    146 : 'VK_FORMAT_BC7_SRGB_BLOCK',
    147 : 'VK_FORMAT_ETC2_R8G8B8_UNORM_BLOCK',
    148 : 'VK_FORMAT_ETC2_R8G8B8_SRGB_BLOCK',
    149 : 'VK_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK',
    150 : 'VK_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK',
    151 : 'VK_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK',
    152 : 'VK_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK',
    153 : 'VK_FORMAT_EAC_R11_UNORM_BLOCK',
    154 : 'VK_FORMAT_EAC_R11_SNORM_BLOCK',
    155 : 'VK_FORMAT_EAC_R11G11_UNORM_BLOCK',
    156 : 'VK_FORMAT_EAC_R11G11_SNORM_BLOCK',
    157 : 'VK_FORMAT_ASTC_4x4_UNORM_BLOCK',
    158 : 'VK_FORMAT_ASTC_4x4_SRGB_BLOCK',
    159 : 'VK_FORMAT_ASTC_5x4_UNORM_BLOCK',
    160 : 'VK_FORMAT_ASTC_5x4_SRGB_BLOCK',
    161 : 'VK_FORMAT_ASTC_5x5_UNORM_BLOCK',
    162 : 'VK_FORMAT_ASTC_5x5_SRGB_BLOCK',
    163 : 'VK_FORMAT_ASTC_6x5_UNORM_BLOCK',
    164 : 'VK_FORMAT_ASTC_6x5_SRGB_BLOCK',
    165 : 'VK_FORMAT_ASTC_6x6_UNORM_BLOCK',
    166 : 'VK_FORMAT_ASTC_6x6_SRGB_BLOCK',
    167 : 'VK_FORMAT_ASTC_8x5_UNORM_BLOCK',
    168 : 'VK_FORMAT_ASTC_8x5_SRGB_BLOCK',
    169 : 'VK_FORMAT_ASTC_8x6_UNORM_BLOCK',
    170 : 'VK_FORMAT_ASTC_8x6_SRGB_BLOCK',
    171 : 'VK_FORMAT_ASTC_8x8_UNORM_BLOCK',
    172 : 'VK_FORMAT_ASTC_8x8_SRGB_BLOCK',
    173 : 'VK_FORMAT_ASTC_10x5_UNORM_BLOCK',
    174 : 'VK_FORMAT_ASTC_10x5_SRGB_BLOCK',
    175 : 'VK_FORMAT_ASTC_10x6_UNORM_BLOCK',
    176 : 'VK_FORMAT_ASTC_10x6_SRGB_BLOCK',
    177 : 'VK_FORMAT_ASTC_10x8_UNORM_BLOCK',
    178 : 'VK_FORMAT_ASTC_10x8_SRGB_BLOCK',
    179 : 'VK_FORMAT_ASTC_10x10_UNORM_BLOCK',
    180 : 'VK_FORMAT_ASTC_10x10_SRGB_BLOCK',
    181 : 'VK_FORMAT_ASTC_12x10_UNORM_BLOCK',
    182 : 'VK_FORMAT_ASTC_12x10_SRGB_BLOCK',
    183 : 'VK_FORMAT_ASTC_12x12_UNORM_BLOCK',
    184 : 'VK_FORMAT_ASTC_12x12_SRGB_BLOCK',
    1000156000 : 'VK_FORMAT_G8B8G8R8_422_UNORM',
    1000156001 : 'VK_FORMAT_B8G8R8G8_422_UNORM',
    1000156002 : 'VK_FORMAT_G8_B8_R8_3PLANE_420_UNORM',
    1000156003 : 'VK_FORMAT_G8_B8R8_2PLANE_420_UNORM',
    1000156004 : 'VK_FORMAT_G8_B8_R8_3PLANE_422_UNORM',
    1000156005 : 'VK_FORMAT_G8_B8R8_2PLANE_422_UNORM',
    1000156006 : 'VK_FORMAT_G8_B8_R8_3PLANE_444_UNORM',
    1000156007 : 'VK_FORMAT_R10X6_UNORM_PACK16',
    1000156008 : 'VK_FORMAT_R10X6G10X6_UNORM_2PACK16',
    1000156009 : 'VK_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16',
    1000156010 : 'VK_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16',
    1000156011 : 'VK_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16',
    1000156012 : 'VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16',
    1000156013 : 'VK_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16',
    1000156014 : 'VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16',
    1000156015 : 'VK_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16',
    1000156016 : 'VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16',
    1000156017 : 'VK_FORMAT_R12X4_UNORM_PACK16',
    1000156018 : 'VK_FORMAT_R12X4G12X4_UNORM_2PACK16',
    1000156019 : 'VK_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16',
    1000156020 : 'VK_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16',
    1000156021 : 'VK_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16',
    1000156022 : 'VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16',
    1000156023 : 'VK_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16',
    1000156024 : 'VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16',
    1000156025 : 'VK_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16',
    1000156026 : 'VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16',
    1000156027 : 'VK_FORMAT_G16B16G16R16_422_UNORM',
    1000156028 : 'VK_FORMAT_B16G16R16G16_422_UNORM',
    1000156029 : 'VK_FORMAT_G16_B16_R16_3PLANE_420_UNORM',
    1000156030 : 'VK_FORMAT_G16_B16R16_2PLANE_420_UNORM',
    1000156031 : 'VK_FORMAT_G16_B16_R16_3PLANE_422_UNORM',
    1000156032 : 'VK_FORMAT_G16_B16R16_2PLANE_422_UNORM',
    1000156033 : 'VK_FORMAT_G16_B16_R16_3PLANE_444_UNORM',
    1000054000 : 'VK_FORMAT_PVRTC1_2BPP_UNORM_BLOCK_IMG',
    1000054001 : 'VK_FORMAT_PVRTC1_4BPP_UNORM_BLOCK_IMG',
    1000054002 : 'VK_FORMAT_PVRTC2_2BPP_UNORM_BLOCK_IMG',
    1000054003 : 'VK_FORMAT_PVRTC2_4BPP_UNORM_BLOCK_IMG',
    1000054004 : 'VK_FORMAT_PVRTC1_2BPP_SRGB_BLOCK_IMG',
    1000054005 : 'VK_FORMAT_PVRTC1_4BPP_SRGB_BLOCK_IMG',
    1000054006 : 'VK_FORMAT_PVRTC2_2BPP_SRGB_BLOCK_IMG',
    1000054007 : 'VK_FORMAT_PVRTC2_4BPP_SRGB_BLOCK_IMG',
    1000066000 : 'VK_FORMAT_ASTC_4x4_SFLOAT_BLOCK_EXT',
    1000066001 : 'VK_FORMAT_ASTC_5x4_SFLOAT_BLOCK_EXT',
    1000066002 : 'VK_FORMAT_ASTC_5x5_SFLOAT_BLOCK_EXT',
    1000066003 : 'VK_FORMAT_ASTC_6x5_SFLOAT_BLOCK_EXT',
    1000066004 : 'VK_FORMAT_ASTC_6x6_SFLOAT_BLOCK_EXT',
    1000066005 : 'VK_FORMAT_ASTC_8x5_SFLOAT_BLOCK_EXT',
    1000066006 : 'VK_FORMAT_ASTC_8x6_SFLOAT_BLOCK_EXT',
    1000066007 : 'VK_FORMAT_ASTC_8x8_SFLOAT_BLOCK_EXT',
    1000066008 : 'VK_FORMAT_ASTC_10x5_SFLOAT_BLOCK_EXT',
    1000066009 : 'VK_FORMAT_ASTC_10x6_SFLOAT_BLOCK_EXT',
    1000066010 : 'VK_FORMAT_ASTC_10x8_SFLOAT_BLOCK_EXT',
    1000066011 : 'VK_FORMAT_ASTC_10x10_SFLOAT_BLOCK_EXT',
    1000066012 : 'VK_FORMAT_ASTC_12x10_SFLOAT_BLOCK_EXT',
    1000066013 : 'VK_FORMAT_ASTC_12x12_SFLOAT_BLOCK_EXT',
    1000340000 : 'VK_FORMAT_A4R4G4B4_UNORM_PACK16_EXT',
    1000340001 : 'VK_FORMAT_A4B4G4R4_UNORM_PACK16_EXT',
}
VK_FORMAT_UNDEFINED = VkFormat(0)
VK_FORMAT_R4G4_UNORM_PACK8 = VkFormat(1)
VK_FORMAT_R4G4B4A4_UNORM_PACK16 = VkFormat(2)
VK_FORMAT_B4G4R4A4_UNORM_PACK16 = VkFormat(3)
VK_FORMAT_R5G6B5_UNORM_PACK16 = VkFormat(4)
VK_FORMAT_B5G6R5_UNORM_PACK16 = VkFormat(5)
VK_FORMAT_R5G5B5A1_UNORM_PACK16 = VkFormat(6)
VK_FORMAT_B5G5R5A1_UNORM_PACK16 = VkFormat(7)
VK_FORMAT_A1R5G5B5_UNORM_PACK16 = VkFormat(8)
VK_FORMAT_R8_UNORM = VkFormat(9)
VK_FORMAT_R8_SNORM = VkFormat(10)
VK_FORMAT_R8_USCALED = VkFormat(11)
VK_FORMAT_R8_SSCALED = VkFormat(12)
VK_FORMAT_R8_UINT = VkFormat(13)
VK_FORMAT_R8_SINT = VkFormat(14)
VK_FORMAT_R8_SRGB = VkFormat(15)
VK_FORMAT_R8G8_UNORM = VkFormat(16)
VK_FORMAT_R8G8_SNORM = VkFormat(17)
VK_FORMAT_R8G8_USCALED = VkFormat(18)
VK_FORMAT_R8G8_SSCALED = VkFormat(19)
VK_FORMAT_R8G8_UINT = VkFormat(20)
VK_FORMAT_R8G8_SINT = VkFormat(21)
VK_FORMAT_R8G8_SRGB = VkFormat(22)
VK_FORMAT_R8G8B8_UNORM = VkFormat(23)
VK_FORMAT_R8G8B8_SNORM = VkFormat(24)
VK_FORMAT_R8G8B8_USCALED = VkFormat(25)
VK_FORMAT_R8G8B8_SSCALED = VkFormat(26)
VK_FORMAT_R8G8B8_UINT = VkFormat(27)
VK_FORMAT_R8G8B8_SINT = VkFormat(28)
VK_FORMAT_R8G8B8_SRGB = VkFormat(29)
VK_FORMAT_B8G8R8_UNORM = VkFormat(30)
VK_FORMAT_B8G8R8_SNORM = VkFormat(31)
VK_FORMAT_B8G8R8_USCALED = VkFormat(32)
VK_FORMAT_B8G8R8_SSCALED = VkFormat(33)
VK_FORMAT_B8G8R8_UINT = VkFormat(34)
VK_FORMAT_B8G8R8_SINT = VkFormat(35)
VK_FORMAT_B8G8R8_SRGB = VkFormat(36)
VK_FORMAT_R8G8B8A8_UNORM = VkFormat(37)
VK_FORMAT_R8G8B8A8_SNORM = VkFormat(38)
VK_FORMAT_R8G8B8A8_USCALED = VkFormat(39)
VK_FORMAT_R8G8B8A8_SSCALED = VkFormat(40)
VK_FORMAT_R8G8B8A8_UINT = VkFormat(41)
VK_FORMAT_R8G8B8A8_SINT = VkFormat(42)
VK_FORMAT_R8G8B8A8_SRGB = VkFormat(43)
VK_FORMAT_B8G8R8A8_UNORM = VkFormat(44)
VK_FORMAT_B8G8R8A8_SNORM = VkFormat(45)
VK_FORMAT_B8G8R8A8_USCALED = VkFormat(46)
VK_FORMAT_B8G8R8A8_SSCALED = VkFormat(47)
VK_FORMAT_B8G8R8A8_UINT = VkFormat(48)
VK_FORMAT_B8G8R8A8_SINT = VkFormat(49)
VK_FORMAT_B8G8R8A8_SRGB = VkFormat(50)
VK_FORMAT_A8B8G8R8_UNORM_PACK32 = VkFormat(51)
VK_FORMAT_A8B8G8R8_SNORM_PACK32 = VkFormat(52)
VK_FORMAT_A8B8G8R8_USCALED_PACK32 = VkFormat(53)
VK_FORMAT_A8B8G8R8_SSCALED_PACK32 = VkFormat(54)
VK_FORMAT_A8B8G8R8_UINT_PACK32 = VkFormat(55)
VK_FORMAT_A8B8G8R8_SINT_PACK32 = VkFormat(56)
VK_FORMAT_A8B8G8R8_SRGB_PACK32 = VkFormat(57)
VK_FORMAT_A2R10G10B10_UNORM_PACK32 = VkFormat(58)
VK_FORMAT_A2R10G10B10_SNORM_PACK32 = VkFormat(59)
VK_FORMAT_A2R10G10B10_USCALED_PACK32 = VkFormat(60)
VK_FORMAT_A2R10G10B10_SSCALED_PACK32 = VkFormat(61)
VK_FORMAT_A2R10G10B10_UINT_PACK32 = VkFormat(62)
VK_FORMAT_A2R10G10B10_SINT_PACK32 = VkFormat(63)
VK_FORMAT_A2B10G10R10_UNORM_PACK32 = VkFormat(64)
VK_FORMAT_A2B10G10R10_SNORM_PACK32 = VkFormat(65)
VK_FORMAT_A2B10G10R10_USCALED_PACK32 = VkFormat(66)
VK_FORMAT_A2B10G10R10_SSCALED_PACK32 = VkFormat(67)
VK_FORMAT_A2B10G10R10_UINT_PACK32 = VkFormat(68)
VK_FORMAT_A2B10G10R10_SINT_PACK32 = VkFormat(69)
VK_FORMAT_R16_UNORM = VkFormat(70)
VK_FORMAT_R16_SNORM = VkFormat(71)
VK_FORMAT_R16_USCALED = VkFormat(72)
VK_FORMAT_R16_SSCALED = VkFormat(73)
VK_FORMAT_R16_UINT = VkFormat(74)
VK_FORMAT_R16_SINT = VkFormat(75)
VK_FORMAT_R16_SFLOAT = VkFormat(76)
VK_FORMAT_R16G16_UNORM = VkFormat(77)
VK_FORMAT_R16G16_SNORM = VkFormat(78)
VK_FORMAT_R16G16_USCALED = VkFormat(79)
VK_FORMAT_R16G16_SSCALED = VkFormat(80)
VK_FORMAT_R16G16_UINT = VkFormat(81)
VK_FORMAT_R16G16_SINT = VkFormat(82)
VK_FORMAT_R16G16_SFLOAT = VkFormat(83)
VK_FORMAT_R16G16B16_UNORM = VkFormat(84)
VK_FORMAT_R16G16B16_SNORM = VkFormat(85)
VK_FORMAT_R16G16B16_USCALED = VkFormat(86)
VK_FORMAT_R16G16B16_SSCALED = VkFormat(87)
VK_FORMAT_R16G16B16_UINT = VkFormat(88)
VK_FORMAT_R16G16B16_SINT = VkFormat(89)
VK_FORMAT_R16G16B16_SFLOAT = VkFormat(90)
VK_FORMAT_R16G16B16A16_UNORM = VkFormat(91)
VK_FORMAT_R16G16B16A16_SNORM = VkFormat(92)
VK_FORMAT_R16G16B16A16_USCALED = VkFormat(93)
VK_FORMAT_R16G16B16A16_SSCALED = VkFormat(94)
VK_FORMAT_R16G16B16A16_UINT = VkFormat(95)
VK_FORMAT_R16G16B16A16_SINT = VkFormat(96)
VK_FORMAT_R16G16B16A16_SFLOAT = VkFormat(97)
VK_FORMAT_R32_UINT = VkFormat(98)
VK_FORMAT_R32_SINT = VkFormat(99)
VK_FORMAT_R32_SFLOAT = VkFormat(100)
VK_FORMAT_R32G32_UINT = VkFormat(101)
VK_FORMAT_R32G32_SINT = VkFormat(102)
VK_FORMAT_R32G32_SFLOAT = VkFormat(103)
VK_FORMAT_R32G32B32_UINT = VkFormat(104)
VK_FORMAT_R32G32B32_SINT = VkFormat(105)
VK_FORMAT_R32G32B32_SFLOAT = VkFormat(106)
VK_FORMAT_R32G32B32A32_UINT = VkFormat(107)
VK_FORMAT_R32G32B32A32_SINT = VkFormat(108)
VK_FORMAT_R32G32B32A32_SFLOAT = VkFormat(109)
VK_FORMAT_R64_UINT = VkFormat(110)
VK_FORMAT_R64_SINT = VkFormat(111)
VK_FORMAT_R64_SFLOAT = VkFormat(112)
VK_FORMAT_R64G64_UINT = VkFormat(113)
VK_FORMAT_R64G64_SINT = VkFormat(114)
VK_FORMAT_R64G64_SFLOAT = VkFormat(115)
VK_FORMAT_R64G64B64_UINT = VkFormat(116)
VK_FORMAT_R64G64B64_SINT = VkFormat(117)
VK_FORMAT_R64G64B64_SFLOAT = VkFormat(118)
VK_FORMAT_R64G64B64A64_UINT = VkFormat(119)
VK_FORMAT_R64G64B64A64_SINT = VkFormat(120)
VK_FORMAT_R64G64B64A64_SFLOAT = VkFormat(121)
VK_FORMAT_B10G11R11_UFLOAT_PACK32 = VkFormat(122)
VK_FORMAT_E5B9G9R9_UFLOAT_PACK32 = VkFormat(123)
VK_FORMAT_D16_UNORM = VkFormat(124)
VK_FORMAT_X8_D24_UNORM_PACK32 = VkFormat(125)
VK_FORMAT_D32_SFLOAT = VkFormat(126)
VK_FORMAT_S8_UINT = VkFormat(127)
VK_FORMAT_D16_UNORM_S8_UINT = VkFormat(128)
VK_FORMAT_D24_UNORM_S8_UINT = VkFormat(129)
VK_FORMAT_D32_SFLOAT_S8_UINT = VkFormat(130)
VK_FORMAT_BC1_RGB_UNORM_BLOCK = VkFormat(131)
VK_FORMAT_BC1_RGB_SRGB_BLOCK = VkFormat(132)
VK_FORMAT_BC1_RGBA_UNORM_BLOCK = VkFormat(133)
VK_FORMAT_BC1_RGBA_SRGB_BLOCK = VkFormat(134)
VK_FORMAT_BC2_UNORM_BLOCK = VkFormat(135)
VK_FORMAT_BC2_SRGB_BLOCK = VkFormat(136)
VK_FORMAT_BC3_UNORM_BLOCK = VkFormat(137)
VK_FORMAT_BC3_SRGB_BLOCK = VkFormat(138)
VK_FORMAT_BC4_UNORM_BLOCK = VkFormat(139)
VK_FORMAT_BC4_SNORM_BLOCK = VkFormat(140)
VK_FORMAT_BC5_UNORM_BLOCK = VkFormat(141)
VK_FORMAT_BC5_SNORM_BLOCK = VkFormat(142)
VK_FORMAT_BC6H_UFLOAT_BLOCK = VkFormat(143)
VK_FORMAT_BC6H_SFLOAT_BLOCK = VkFormat(144)
VK_FORMAT_BC7_UNORM_BLOCK = VkFormat(145)
VK_FORMAT_BC7_SRGB_BLOCK = VkFormat(146)
VK_FORMAT_ETC2_R8G8B8_UNORM_BLOCK = VkFormat(147)
VK_FORMAT_ETC2_R8G8B8_SRGB_BLOCK = VkFormat(148)
VK_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK = VkFormat(149)
VK_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK = VkFormat(150)
VK_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK = VkFormat(151)
VK_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK = VkFormat(152)
VK_FORMAT_EAC_R11_UNORM_BLOCK = VkFormat(153)
VK_FORMAT_EAC_R11_SNORM_BLOCK = VkFormat(154)
VK_FORMAT_EAC_R11G11_UNORM_BLOCK = VkFormat(155)
VK_FORMAT_EAC_R11G11_SNORM_BLOCK = VkFormat(156)
VK_FORMAT_ASTC_4x4_UNORM_BLOCK = VkFormat(157)
VK_FORMAT_ASTC_4x4_SRGB_BLOCK = VkFormat(158)
VK_FORMAT_ASTC_5x4_UNORM_BLOCK = VkFormat(159)
VK_FORMAT_ASTC_5x4_SRGB_BLOCK = VkFormat(160)
VK_FORMAT_ASTC_5x5_UNORM_BLOCK = VkFormat(161)
VK_FORMAT_ASTC_5x5_SRGB_BLOCK = VkFormat(162)
VK_FORMAT_ASTC_6x5_UNORM_BLOCK = VkFormat(163)
VK_FORMAT_ASTC_6x5_SRGB_BLOCK = VkFormat(164)
VK_FORMAT_ASTC_6x6_UNORM_BLOCK = VkFormat(165)
VK_FORMAT_ASTC_6x6_SRGB_BLOCK = VkFormat(166)
VK_FORMAT_ASTC_8x5_UNORM_BLOCK = VkFormat(167)
VK_FORMAT_ASTC_8x5_SRGB_BLOCK = VkFormat(168)
VK_FORMAT_ASTC_8x6_UNORM_BLOCK = VkFormat(169)
VK_FORMAT_ASTC_8x6_SRGB_BLOCK = VkFormat(170)
VK_FORMAT_ASTC_8x8_UNORM_BLOCK = VkFormat(171)
VK_FORMAT_ASTC_8x8_SRGB_BLOCK = VkFormat(172)
VK_FORMAT_ASTC_10x5_UNORM_BLOCK = VkFormat(173)
VK_FORMAT_ASTC_10x5_SRGB_BLOCK = VkFormat(174)
VK_FORMAT_ASTC_10x6_UNORM_BLOCK = VkFormat(175)
VK_FORMAT_ASTC_10x6_SRGB_BLOCK = VkFormat(176)
VK_FORMAT_ASTC_10x8_UNORM_BLOCK = VkFormat(177)
VK_FORMAT_ASTC_10x8_SRGB_BLOCK = VkFormat(178)
VK_FORMAT_ASTC_10x10_UNORM_BLOCK = VkFormat(179)
VK_FORMAT_ASTC_10x10_SRGB_BLOCK = VkFormat(180)
VK_FORMAT_ASTC_12x10_UNORM_BLOCK = VkFormat(181)
VK_FORMAT_ASTC_12x10_SRGB_BLOCK = VkFormat(182)
VK_FORMAT_ASTC_12x12_UNORM_BLOCK = VkFormat(183)
VK_FORMAT_ASTC_12x12_SRGB_BLOCK = VkFormat(184)
VK_FORMAT_G8B8G8R8_422_UNORM = VkFormat(1000156000)
VK_FORMAT_B8G8R8G8_422_UNORM = VkFormat(1000156001)
VK_FORMAT_G8_B8_R8_3PLANE_420_UNORM = VkFormat(1000156002)
VK_FORMAT_G8_B8R8_2PLANE_420_UNORM = VkFormat(1000156003)
VK_FORMAT_G8_B8_R8_3PLANE_422_UNORM = VkFormat(1000156004)
VK_FORMAT_G8_B8R8_2PLANE_422_UNORM = VkFormat(1000156005)
VK_FORMAT_G8_B8_R8_3PLANE_444_UNORM = VkFormat(1000156006)
VK_FORMAT_R10X6_UNORM_PACK16 = VkFormat(1000156007)
VK_FORMAT_R10X6G10X6_UNORM_2PACK16 = VkFormat(1000156008)
VK_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16 = VkFormat(1000156009)
VK_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16 = VkFormat(1000156010)
VK_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16 = VkFormat(1000156011)
VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16 = VkFormat(1000156012)
VK_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16 = VkFormat(1000156013)
VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16 = VkFormat(1000156014)
VK_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16 = VkFormat(1000156015)
VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16 = VkFormat(1000156016)
VK_FORMAT_R12X4_UNORM_PACK16 = VkFormat(1000156017)
VK_FORMAT_R12X4G12X4_UNORM_2PACK16 = VkFormat(1000156018)
VK_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16 = VkFormat(1000156019)
VK_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16 = VkFormat(1000156020)
VK_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16 = VkFormat(1000156021)
VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16 = VkFormat(1000156022)
VK_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16 = VkFormat(1000156023)
VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16 = VkFormat(1000156024)
VK_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16 = VkFormat(1000156025)
VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16 = VkFormat(1000156026)
VK_FORMAT_G16B16G16R16_422_UNORM = VkFormat(1000156027)
VK_FORMAT_B16G16R16G16_422_UNORM = VkFormat(1000156028)
VK_FORMAT_G16_B16_R16_3PLANE_420_UNORM = VkFormat(1000156029)
VK_FORMAT_G16_B16R16_2PLANE_420_UNORM = VkFormat(1000156030)
VK_FORMAT_G16_B16_R16_3PLANE_422_UNORM = VkFormat(1000156031)
VK_FORMAT_G16_B16R16_2PLANE_422_UNORM = VkFormat(1000156032)
VK_FORMAT_G16_B16_R16_3PLANE_444_UNORM = VkFormat(1000156033)
VK_FORMAT_PVRTC1_2BPP_UNORM_BLOCK_IMG = VkFormat(1000054000)
VK_FORMAT_PVRTC1_4BPP_UNORM_BLOCK_IMG = VkFormat(1000054001)
VK_FORMAT_PVRTC2_2BPP_UNORM_BLOCK_IMG = VkFormat(1000054002)
VK_FORMAT_PVRTC2_4BPP_UNORM_BLOCK_IMG = VkFormat(1000054003)
VK_FORMAT_PVRTC1_2BPP_SRGB_BLOCK_IMG = VkFormat(1000054004)
VK_FORMAT_PVRTC1_4BPP_SRGB_BLOCK_IMG = VkFormat(1000054005)
VK_FORMAT_PVRTC2_2BPP_SRGB_BLOCK_IMG = VkFormat(1000054006)
VK_FORMAT_PVRTC2_4BPP_SRGB_BLOCK_IMG = VkFormat(1000054007)
VK_FORMAT_ASTC_4x4_SFLOAT_BLOCK_EXT = VkFormat(1000066000)
VK_FORMAT_ASTC_5x4_SFLOAT_BLOCK_EXT = VkFormat(1000066001)
VK_FORMAT_ASTC_5x5_SFLOAT_BLOCK_EXT = VkFormat(1000066002)
VK_FORMAT_ASTC_6x5_SFLOAT_BLOCK_EXT = VkFormat(1000066003)
VK_FORMAT_ASTC_6x6_SFLOAT_BLOCK_EXT = VkFormat(1000066004)
VK_FORMAT_ASTC_8x5_SFLOAT_BLOCK_EXT = VkFormat(1000066005)
VK_FORMAT_ASTC_8x6_SFLOAT_BLOCK_EXT = VkFormat(1000066006)
VK_FORMAT_ASTC_8x8_SFLOAT_BLOCK_EXT = VkFormat(1000066007)
VK_FORMAT_ASTC_10x5_SFLOAT_BLOCK_EXT = VkFormat(1000066008)
VK_FORMAT_ASTC_10x6_SFLOAT_BLOCK_EXT = VkFormat(1000066009)
VK_FORMAT_ASTC_10x8_SFLOAT_BLOCK_EXT = VkFormat(1000066010)
VK_FORMAT_ASTC_10x10_SFLOAT_BLOCK_EXT = VkFormat(1000066011)
VK_FORMAT_ASTC_12x10_SFLOAT_BLOCK_EXT = VkFormat(1000066012)
VK_FORMAT_ASTC_12x12_SFLOAT_BLOCK_EXT = VkFormat(1000066013)
VK_FORMAT_G8B8G8R8_422_UNORM_KHR = VK_FORMAT_G8B8G8R8_422_UNORM
VK_FORMAT_B8G8R8G8_422_UNORM_KHR = VK_FORMAT_B8G8R8G8_422_UNORM
VK_FORMAT_G8_B8_R8_3PLANE_420_UNORM_KHR = VK_FORMAT_G8_B8_R8_3PLANE_420_UNORM
VK_FORMAT_G8_B8R8_2PLANE_420_UNORM_KHR = VK_FORMAT_G8_B8R8_2PLANE_420_UNORM
VK_FORMAT_G8_B8_R8_3PLANE_422_UNORM_KHR = VK_FORMAT_G8_B8_R8_3PLANE_422_UNORM
VK_FORMAT_G8_B8R8_2PLANE_422_UNORM_KHR = VK_FORMAT_G8_B8R8_2PLANE_422_UNORM
VK_FORMAT_G8_B8_R8_3PLANE_444_UNORM_KHR = VK_FORMAT_G8_B8_R8_3PLANE_444_UNORM
VK_FORMAT_R10X6_UNORM_PACK16_KHR = VK_FORMAT_R10X6_UNORM_PACK16
VK_FORMAT_R10X6G10X6_UNORM_2PACK16_KHR = VK_FORMAT_R10X6G10X6_UNORM_2PACK16
VK_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16_KHR = VK_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16
VK_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16_KHR = VK_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16
VK_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16_KHR = VK_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16
VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16_KHR = VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16
VK_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16_KHR = VK_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16
VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16_KHR = VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16
VK_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16_KHR = VK_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16
VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16_KHR = VK_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16
VK_FORMAT_R12X4_UNORM_PACK16_KHR = VK_FORMAT_R12X4_UNORM_PACK16
VK_FORMAT_R12X4G12X4_UNORM_2PACK16_KHR = VK_FORMAT_R12X4G12X4_UNORM_2PACK16
VK_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16_KHR = VK_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16
VK_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16_KHR = VK_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16
VK_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16_KHR = VK_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16
VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16_KHR = VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16
VK_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16_KHR = VK_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16
VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16_KHR = VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16
VK_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16_KHR = VK_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16
VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16_KHR = VK_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16
VK_FORMAT_G16B16G16R16_422_UNORM_KHR = VK_FORMAT_G16B16G16R16_422_UNORM
VK_FORMAT_B16G16R16G16_422_UNORM_KHR = VK_FORMAT_B16G16R16G16_422_UNORM
VK_FORMAT_G16_B16_R16_3PLANE_420_UNORM_KHR = VK_FORMAT_G16_B16_R16_3PLANE_420_UNORM
VK_FORMAT_G16_B16R16_2PLANE_420_UNORM_KHR = VK_FORMAT_G16_B16R16_2PLANE_420_UNORM
VK_FORMAT_G16_B16_R16_3PLANE_422_UNORM_KHR = VK_FORMAT_G16_B16_R16_3PLANE_422_UNORM
VK_FORMAT_G16_B16R16_2PLANE_422_UNORM_KHR = VK_FORMAT_G16_B16R16_2PLANE_422_UNORM
VK_FORMAT_G16_B16_R16_3PLANE_444_UNORM_KHR = VK_FORMAT_G16_B16_R16_3PLANE_444_UNORM
VK_FORMAT_A4R4G4B4_UNORM_PACK16_EXT = VkFormat(1000340000)
VK_FORMAT_A4B4G4R4_UNORM_PACK16_EXT = VkFormat(1000340001)

VkFormatFeatureFlagBits = type('VkFormatFeatureFlagBits', (c_enum,), dict(names=dict()))
VkFormatFeatureFlagBits.names = {
    1 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_BIT',
    2 : 'VK_FORMAT_FEATURE_STORAGE_IMAGE_BIT',
    4 : 'VK_FORMAT_FEATURE_STORAGE_IMAGE_ATOMIC_BIT',
    8 : 'VK_FORMAT_FEATURE_UNIFORM_TEXEL_BUFFER_BIT',
    16 : 'VK_FORMAT_FEATURE_STORAGE_TEXEL_BUFFER_BIT',
    32 : 'VK_FORMAT_FEATURE_STORAGE_TEXEL_BUFFER_ATOMIC_BIT',
    64 : 'VK_FORMAT_FEATURE_VERTEX_BUFFER_BIT',
    128 : 'VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BIT',
    256 : 'VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BLEND_BIT',
    512 : 'VK_FORMAT_FEATURE_DEPTH_STENCIL_ATTACHMENT_BIT',
    1024 : 'VK_FORMAT_FEATURE_BLIT_SRC_BIT',
    2048 : 'VK_FORMAT_FEATURE_BLIT_DST_BIT',
    4096 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_LINEAR_BIT',
    16384 : 'VK_FORMAT_FEATURE_TRANSFER_SRC_BIT',
    32768 : 'VK_FORMAT_FEATURE_TRANSFER_DST_BIT',
    131072 : 'VK_FORMAT_FEATURE_MIDPOINT_CHROMA_SAMPLES_BIT',
    262144 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_LINEAR_FILTER_BIT',
    524288 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_SEPARATE_RECONSTRUCTION_FILTER_BIT',
    1048576 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_BIT',
    2097152 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_FORCEABLE_BIT',
    4194304 : 'VK_FORMAT_FEATURE_DISJOINT_BIT',
    8388608 : 'VK_FORMAT_FEATURE_COSITED_CHROMA_SAMPLES_BIT',
    65536 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_MINMAX_BIT',
    8192 : 'VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_CUBIC_BIT_IMG',
    536870912 : 'VK_FORMAT_FEATURE_ACCELERATION_STRUCTURE_VERTEX_BUFFER_BIT_KHR',
    16777216 : 'VK_FORMAT_FEATURE_FRAGMENT_DENSITY_MAP_BIT_EXT',
    1073741824 : 'VK_FORMAT_FEATURE_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR',
}
VK_FORMAT_FEATURE_SAMPLED_IMAGE_BIT = VkFormatFeatureFlagBits(1)
VK_FORMAT_FEATURE_STORAGE_IMAGE_BIT = VkFormatFeatureFlagBits(2)
VK_FORMAT_FEATURE_STORAGE_IMAGE_ATOMIC_BIT = VkFormatFeatureFlagBits(4)
VK_FORMAT_FEATURE_UNIFORM_TEXEL_BUFFER_BIT = VkFormatFeatureFlagBits(8)
VK_FORMAT_FEATURE_STORAGE_TEXEL_BUFFER_BIT = VkFormatFeatureFlagBits(16)
VK_FORMAT_FEATURE_STORAGE_TEXEL_BUFFER_ATOMIC_BIT = VkFormatFeatureFlagBits(32)
VK_FORMAT_FEATURE_VERTEX_BUFFER_BIT = VkFormatFeatureFlagBits(64)
VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BIT = VkFormatFeatureFlagBits(128)
VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BLEND_BIT = VkFormatFeatureFlagBits(256)
VK_FORMAT_FEATURE_DEPTH_STENCIL_ATTACHMENT_BIT = VkFormatFeatureFlagBits(512)
VK_FORMAT_FEATURE_BLIT_SRC_BIT = VkFormatFeatureFlagBits(1024)
VK_FORMAT_FEATURE_BLIT_DST_BIT = VkFormatFeatureFlagBits(2048)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_LINEAR_BIT = VkFormatFeatureFlagBits(4096)
VK_FORMAT_FEATURE_TRANSFER_SRC_BIT = VkFormatFeatureFlagBits(16384)
VK_FORMAT_FEATURE_TRANSFER_DST_BIT = VkFormatFeatureFlagBits(32768)
VK_FORMAT_FEATURE_MIDPOINT_CHROMA_SAMPLES_BIT = VkFormatFeatureFlagBits(131072)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_LINEAR_FILTER_BIT = VkFormatFeatureFlagBits(262144)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_SEPARATE_RECONSTRUCTION_FILTER_BIT = VkFormatFeatureFlagBits(524288)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_BIT = VkFormatFeatureFlagBits(1048576)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_FORCEABLE_BIT = VkFormatFeatureFlagBits(2097152)
VK_FORMAT_FEATURE_DISJOINT_BIT = VkFormatFeatureFlagBits(4194304)
VK_FORMAT_FEATURE_COSITED_CHROMA_SAMPLES_BIT = VkFormatFeatureFlagBits(8388608)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_MINMAX_BIT = VkFormatFeatureFlagBits(65536)
VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_CUBIC_BIT_IMG = VkFormatFeatureFlagBits(8192)
VK_FORMAT_FEATURE_TRANSFER_SRC_BIT_KHR = VK_FORMAT_FEATURE_TRANSFER_SRC_BIT
VK_FORMAT_FEATURE_TRANSFER_DST_BIT_KHR = VK_FORMAT_FEATURE_TRANSFER_DST_BIT
VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_MINMAX_BIT_EXT = VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_MINMAX_BIT
VK_FORMAT_FEATURE_ACCELERATION_STRUCTURE_VERTEX_BUFFER_BIT_KHR = VkFormatFeatureFlagBits(536870912)
VK_FORMAT_FEATURE_MIDPOINT_CHROMA_SAMPLES_BIT_KHR = VK_FORMAT_FEATURE_MIDPOINT_CHROMA_SAMPLES_BIT
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_LINEAR_FILTER_BIT_KHR = VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_LINEAR_FILTER_BIT
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_SEPARATE_RECONSTRUCTION_FILTER_BIT_KHR = VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_SEPARATE_RECONSTRUCTION_FILTER_BIT
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_BIT_KHR = VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_BIT
VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_FORCEABLE_BIT_KHR = VK_FORMAT_FEATURE_SAMPLED_IMAGE_YCBCR_CONVERSION_CHROMA_RECONSTRUCTION_EXPLICIT_FORCEABLE_BIT
VK_FORMAT_FEATURE_DISJOINT_BIT_KHR = VK_FORMAT_FEATURE_DISJOINT_BIT
VK_FORMAT_FEATURE_COSITED_CHROMA_SAMPLES_BIT_KHR = VK_FORMAT_FEATURE_COSITED_CHROMA_SAMPLES_BIT
VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_CUBIC_BIT_EXT = VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_CUBIC_BIT_IMG
VK_FORMAT_FEATURE_FRAGMENT_DENSITY_MAP_BIT_EXT = VkFormatFeatureFlagBits(16777216)
VK_FORMAT_FEATURE_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR = VkFormatFeatureFlagBits(1073741824)

VkFrontFace = type('VkFrontFace', (c_enum,), dict(names=dict()))
VkFrontFace.names = {
    0 : 'VK_FRONT_FACE_COUNTER_CLOCKWISE',
    1 : 'VK_FRONT_FACE_CLOCKWISE',
}
VK_FRONT_FACE_COUNTER_CLOCKWISE = VkFrontFace(0)
VK_FRONT_FACE_CLOCKWISE = VkFrontFace(1)

VkImageAspectFlagBits = type('VkImageAspectFlagBits', (c_enum,), dict(names=dict()))
VkImageAspectFlagBits.names = {
    1 : 'VK_IMAGE_ASPECT_COLOR_BIT',
    2 : 'VK_IMAGE_ASPECT_DEPTH_BIT',
    4 : 'VK_IMAGE_ASPECT_STENCIL_BIT',
    8 : 'VK_IMAGE_ASPECT_METADATA_BIT',
    16 : 'VK_IMAGE_ASPECT_PLANE_0_BIT',
    32 : 'VK_IMAGE_ASPECT_PLANE_1_BIT',
    64 : 'VK_IMAGE_ASPECT_PLANE_2_BIT',
    128 : 'VK_IMAGE_ASPECT_MEMORY_PLANE_0_BIT_EXT',
    256 : 'VK_IMAGE_ASPECT_MEMORY_PLANE_1_BIT_EXT',
    512 : 'VK_IMAGE_ASPECT_MEMORY_PLANE_2_BIT_EXT',
    1024 : 'VK_IMAGE_ASPECT_MEMORY_PLANE_3_BIT_EXT',
}
VK_IMAGE_ASPECT_COLOR_BIT = VkImageAspectFlagBits(1)
VK_IMAGE_ASPECT_DEPTH_BIT = VkImageAspectFlagBits(2)
VK_IMAGE_ASPECT_STENCIL_BIT = VkImageAspectFlagBits(4)
VK_IMAGE_ASPECT_METADATA_BIT = VkImageAspectFlagBits(8)
VK_IMAGE_ASPECT_PLANE_0_BIT = VkImageAspectFlagBits(16)
VK_IMAGE_ASPECT_PLANE_1_BIT = VkImageAspectFlagBits(32)
VK_IMAGE_ASPECT_PLANE_2_BIT = VkImageAspectFlagBits(64)
VK_IMAGE_ASPECT_PLANE_0_BIT_KHR = VK_IMAGE_ASPECT_PLANE_0_BIT
VK_IMAGE_ASPECT_PLANE_1_BIT_KHR = VK_IMAGE_ASPECT_PLANE_1_BIT
VK_IMAGE_ASPECT_PLANE_2_BIT_KHR = VK_IMAGE_ASPECT_PLANE_2_BIT
VK_IMAGE_ASPECT_MEMORY_PLANE_0_BIT_EXT = VkImageAspectFlagBits(128)
VK_IMAGE_ASPECT_MEMORY_PLANE_1_BIT_EXT = VkImageAspectFlagBits(256)
VK_IMAGE_ASPECT_MEMORY_PLANE_2_BIT_EXT = VkImageAspectFlagBits(512)
VK_IMAGE_ASPECT_MEMORY_PLANE_3_BIT_EXT = VkImageAspectFlagBits(1024)

VkImageCreateFlagBits = type('VkImageCreateFlagBits', (c_enum,), dict(names=dict()))
VkImageCreateFlagBits.names = {
    1 : 'VK_IMAGE_CREATE_SPARSE_BINDING_BIT',
    2 : 'VK_IMAGE_CREATE_SPARSE_RESIDENCY_BIT',
    4 : 'VK_IMAGE_CREATE_SPARSE_ALIASED_BIT',
    8 : 'VK_IMAGE_CREATE_MUTABLE_FORMAT_BIT',
    16 : 'VK_IMAGE_CREATE_CUBE_COMPATIBLE_BIT',
    1024 : 'VK_IMAGE_CREATE_ALIAS_BIT',
    64 : 'VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT',
    32 : 'VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT',
    128 : 'VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT',
    256 : 'VK_IMAGE_CREATE_EXTENDED_USAGE_BIT',
    2048 : 'VK_IMAGE_CREATE_PROTECTED_BIT',
    512 : 'VK_IMAGE_CREATE_DISJOINT_BIT',
    8192 : 'VK_IMAGE_CREATE_CORNER_SAMPLED_BIT_NV',
    4096 : 'VK_IMAGE_CREATE_SAMPLE_LOCATIONS_COMPATIBLE_DEPTH_BIT_EXT',
    16384 : 'VK_IMAGE_CREATE_SUBSAMPLED_BIT_EXT',
}
VK_IMAGE_CREATE_SPARSE_BINDING_BIT = VkImageCreateFlagBits(1)
VK_IMAGE_CREATE_SPARSE_RESIDENCY_BIT = VkImageCreateFlagBits(2)
VK_IMAGE_CREATE_SPARSE_ALIASED_BIT = VkImageCreateFlagBits(4)
VK_IMAGE_CREATE_MUTABLE_FORMAT_BIT = VkImageCreateFlagBits(8)
VK_IMAGE_CREATE_CUBE_COMPATIBLE_BIT = VkImageCreateFlagBits(16)
VK_IMAGE_CREATE_ALIAS_BIT = VkImageCreateFlagBits(1024)
VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT = VkImageCreateFlagBits(64)
VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT = VkImageCreateFlagBits(32)
VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT = VkImageCreateFlagBits(128)
VK_IMAGE_CREATE_EXTENDED_USAGE_BIT = VkImageCreateFlagBits(256)
VK_IMAGE_CREATE_PROTECTED_BIT = VkImageCreateFlagBits(2048)
VK_IMAGE_CREATE_DISJOINT_BIT = VkImageCreateFlagBits(512)
VK_IMAGE_CREATE_CORNER_SAMPLED_BIT_NV = VkImageCreateFlagBits(8192)
VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR = VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT
VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT_KHR = VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT
VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT_KHR = VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT
VK_IMAGE_CREATE_EXTENDED_USAGE_BIT_KHR = VK_IMAGE_CREATE_EXTENDED_USAGE_BIT
VK_IMAGE_CREATE_SAMPLE_LOCATIONS_COMPATIBLE_DEPTH_BIT_EXT = VkImageCreateFlagBits(4096)
VK_IMAGE_CREATE_DISJOINT_BIT_KHR = VK_IMAGE_CREATE_DISJOINT_BIT
VK_IMAGE_CREATE_ALIAS_BIT_KHR = VK_IMAGE_CREATE_ALIAS_BIT
VK_IMAGE_CREATE_SUBSAMPLED_BIT_EXT = VkImageCreateFlagBits(16384)

VkImageLayout = type('VkImageLayout', (c_enum,), dict(names=dict()))
VkImageLayout.names = {
    0 : 'VK_IMAGE_LAYOUT_UNDEFINED',
    1 : 'VK_IMAGE_LAYOUT_GENERAL',
    2 : 'VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL',
    3 : 'VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL',
    4 : 'VK_IMAGE_LAYOUT_DEPTH_STENCIL_READ_ONLY_OPTIMAL',
    5 : 'VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL',
    6 : 'VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL',
    7 : 'VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL',
    8 : 'VK_IMAGE_LAYOUT_PREINITIALIZED',
    1000117000 : 'VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL',
    1000117001 : 'VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL',
    1000241000 : 'VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL',
    1000241001 : 'VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL',
    1000241002 : 'VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL',
    1000241003 : 'VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL',
    1000001002 : 'VK_IMAGE_LAYOUT_PRESENT_SRC_KHR',
    1000111000 : 'VK_IMAGE_LAYOUT_SHARED_PRESENT_KHR',
    1000164003 : 'VK_IMAGE_LAYOUT_SHADING_RATE_OPTIMAL_NV',
    1000218000 : 'VK_IMAGE_LAYOUT_FRAGMENT_DENSITY_MAP_OPTIMAL_EXT',
}
VK_IMAGE_LAYOUT_UNDEFINED = VkImageLayout(0)
VK_IMAGE_LAYOUT_GENERAL = VkImageLayout(1)
VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL = VkImageLayout(2)
VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL = VkImageLayout(3)
VK_IMAGE_LAYOUT_DEPTH_STENCIL_READ_ONLY_OPTIMAL = VkImageLayout(4)
VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL = VkImageLayout(5)
VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL = VkImageLayout(6)
VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL = VkImageLayout(7)
VK_IMAGE_LAYOUT_PREINITIALIZED = VkImageLayout(8)
VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL = VkImageLayout(1000117000)
VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL = VkImageLayout(1000117001)
VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL = VkImageLayout(1000241000)
VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL = VkImageLayout(1000241001)
VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL = VkImageLayout(1000241002)
VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL = VkImageLayout(1000241003)
VK_IMAGE_LAYOUT_PRESENT_SRC_KHR = VkImageLayout(1000001002)
VK_IMAGE_LAYOUT_SHARED_PRESENT_KHR = VkImageLayout(1000111000)
VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL_KHR = VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL
VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL_KHR = VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL
VK_IMAGE_LAYOUT_SHADING_RATE_OPTIMAL_NV = VkImageLayout(1000164003)
VK_IMAGE_LAYOUT_FRAGMENT_DENSITY_MAP_OPTIMAL_EXT = VkImageLayout(1000218000)
VK_IMAGE_LAYOUT_FRAGMENT_SHADING_RATE_ATTACHMENT_OPTIMAL_KHR = VK_IMAGE_LAYOUT_SHADING_RATE_OPTIMAL_NV
VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL_KHR = VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL
VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL_KHR = VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL
VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL_KHR = VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL
VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL_KHR = VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL

VkImageTiling = type('VkImageTiling', (c_enum,), dict(names=dict()))
VkImageTiling.names = {
    0 : 'VK_IMAGE_TILING_OPTIMAL',
    1 : 'VK_IMAGE_TILING_LINEAR',
    1000158000 : 'VK_IMAGE_TILING_DRM_FORMAT_MODIFIER_EXT',
}
VK_IMAGE_TILING_OPTIMAL = VkImageTiling(0)
VK_IMAGE_TILING_LINEAR = VkImageTiling(1)
VK_IMAGE_TILING_DRM_FORMAT_MODIFIER_EXT = VkImageTiling(1000158000)

VkImageType = type('VkImageType', (c_enum,), dict(names=dict()))
VkImageType.names = {
    0 : 'VK_IMAGE_TYPE_1D',
    1 : 'VK_IMAGE_TYPE_2D',
    2 : 'VK_IMAGE_TYPE_3D',
}
VK_IMAGE_TYPE_1D = VkImageType(0)
VK_IMAGE_TYPE_2D = VkImageType(1)
VK_IMAGE_TYPE_3D = VkImageType(2)

VkImageUsageFlagBits = type('VkImageUsageFlagBits', (c_enum,), dict(names=dict()))
VkImageUsageFlagBits.names = {
    1 : 'VK_IMAGE_USAGE_TRANSFER_SRC_BIT',
    2 : 'VK_IMAGE_USAGE_TRANSFER_DST_BIT',
    4 : 'VK_IMAGE_USAGE_SAMPLED_BIT',
    8 : 'VK_IMAGE_USAGE_STORAGE_BIT',
    16 : 'VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT',
    32 : 'VK_IMAGE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT',
    64 : 'VK_IMAGE_USAGE_TRANSIENT_ATTACHMENT_BIT',
    128 : 'VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT',
    256 : 'VK_IMAGE_USAGE_SHADING_RATE_IMAGE_BIT_NV',
    512 : 'VK_IMAGE_USAGE_FRAGMENT_DENSITY_MAP_BIT_EXT',
}
VK_IMAGE_USAGE_TRANSFER_SRC_BIT = VkImageUsageFlagBits(1)
VK_IMAGE_USAGE_TRANSFER_DST_BIT = VkImageUsageFlagBits(2)
VK_IMAGE_USAGE_SAMPLED_BIT = VkImageUsageFlagBits(4)
VK_IMAGE_USAGE_STORAGE_BIT = VkImageUsageFlagBits(8)
VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT = VkImageUsageFlagBits(16)
VK_IMAGE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT = VkImageUsageFlagBits(32)
VK_IMAGE_USAGE_TRANSIENT_ATTACHMENT_BIT = VkImageUsageFlagBits(64)
VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT = VkImageUsageFlagBits(128)
VK_IMAGE_USAGE_SHADING_RATE_IMAGE_BIT_NV = VkImageUsageFlagBits(256)
VK_IMAGE_USAGE_FRAGMENT_DENSITY_MAP_BIT_EXT = VkImageUsageFlagBits(512)
VK_IMAGE_USAGE_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR = VK_IMAGE_USAGE_SHADING_RATE_IMAGE_BIT_NV

VkImageViewCreateFlagBits = type('VkImageViewCreateFlagBits', (c_enum,), dict(names=dict()))
VkImageViewCreateFlagBits.names = {
    1 : 'VK_IMAGE_VIEW_CREATE_FRAGMENT_DENSITY_MAP_DYNAMIC_BIT_EXT',
    2 : 'VK_IMAGE_VIEW_CREATE_FRAGMENT_DENSITY_MAP_DEFERRED_BIT_EXT',
}
VK_IMAGE_VIEW_CREATE_FRAGMENT_DENSITY_MAP_DYNAMIC_BIT_EXT = VkImageViewCreateFlagBits(1)
VK_IMAGE_VIEW_CREATE_FRAGMENT_DENSITY_MAP_DEFERRED_BIT_EXT = VkImageViewCreateFlagBits(2)

VkImageViewType = type('VkImageViewType', (c_enum,), dict(names=dict()))
VkImageViewType.names = {
    0 : 'VK_IMAGE_VIEW_TYPE_1D',
    1 : 'VK_IMAGE_VIEW_TYPE_2D',
    2 : 'VK_IMAGE_VIEW_TYPE_3D',
    3 : 'VK_IMAGE_VIEW_TYPE_CUBE',
    4 : 'VK_IMAGE_VIEW_TYPE_1D_ARRAY',
    5 : 'VK_IMAGE_VIEW_TYPE_2D_ARRAY',
    6 : 'VK_IMAGE_VIEW_TYPE_CUBE_ARRAY',
}
VK_IMAGE_VIEW_TYPE_1D = VkImageViewType(0)
VK_IMAGE_VIEW_TYPE_2D = VkImageViewType(1)
VK_IMAGE_VIEW_TYPE_3D = VkImageViewType(2)
VK_IMAGE_VIEW_TYPE_CUBE = VkImageViewType(3)
VK_IMAGE_VIEW_TYPE_1D_ARRAY = VkImageViewType(4)
VK_IMAGE_VIEW_TYPE_2D_ARRAY = VkImageViewType(5)
VK_IMAGE_VIEW_TYPE_CUBE_ARRAY = VkImageViewType(6)

VkSharingMode = type('VkSharingMode', (c_enum,), dict(names=dict()))
VkSharingMode.names = {
    0 : 'VK_SHARING_MODE_EXCLUSIVE',
    1 : 'VK_SHARING_MODE_CONCURRENT',
}
VK_SHARING_MODE_EXCLUSIVE = VkSharingMode(0)
VK_SHARING_MODE_CONCURRENT = VkSharingMode(1)

VkIndexType = type('VkIndexType', (c_enum,), dict(names=dict()))
VkIndexType.names = {
    0 : 'VK_INDEX_TYPE_UINT16',
    1 : 'VK_INDEX_TYPE_UINT32',
    1000165000 : 'VK_INDEX_TYPE_NONE_KHR',
    1000265000 : 'VK_INDEX_TYPE_UINT8_EXT',
}
VK_INDEX_TYPE_UINT16 = VkIndexType(0)
VK_INDEX_TYPE_UINT32 = VkIndexType(1)
VK_INDEX_TYPE_NONE_KHR = VkIndexType(1000165000)
VK_INDEX_TYPE_NONE_NV = VK_INDEX_TYPE_NONE_KHR
VK_INDEX_TYPE_UINT8_EXT = VkIndexType(1000265000)

VkLogicOp = type('VkLogicOp', (c_enum,), dict(names=dict()))
VkLogicOp.names = {
    0 : 'VK_LOGIC_OP_CLEAR',
    1 : 'VK_LOGIC_OP_AND',
    2 : 'VK_LOGIC_OP_AND_REVERSE',
    3 : 'VK_LOGIC_OP_COPY',
    4 : 'VK_LOGIC_OP_AND_INVERTED',
    5 : 'VK_LOGIC_OP_NO_OP',
    6 : 'VK_LOGIC_OP_XOR',
    7 : 'VK_LOGIC_OP_OR',
    8 : 'VK_LOGIC_OP_NOR',
    9 : 'VK_LOGIC_OP_EQUIVALENT',
    10 : 'VK_LOGIC_OP_INVERT',
    11 : 'VK_LOGIC_OP_OR_REVERSE',
    12 : 'VK_LOGIC_OP_COPY_INVERTED',
    13 : 'VK_LOGIC_OP_OR_INVERTED',
    14 : 'VK_LOGIC_OP_NAND',
    15 : 'VK_LOGIC_OP_SET',
}
VK_LOGIC_OP_CLEAR = VkLogicOp(0)
VK_LOGIC_OP_AND = VkLogicOp(1)
VK_LOGIC_OP_AND_REVERSE = VkLogicOp(2)
VK_LOGIC_OP_COPY = VkLogicOp(3)
VK_LOGIC_OP_AND_INVERTED = VkLogicOp(4)
VK_LOGIC_OP_NO_OP = VkLogicOp(5)
VK_LOGIC_OP_XOR = VkLogicOp(6)
VK_LOGIC_OP_OR = VkLogicOp(7)
VK_LOGIC_OP_NOR = VkLogicOp(8)
VK_LOGIC_OP_EQUIVALENT = VkLogicOp(9)
VK_LOGIC_OP_INVERT = VkLogicOp(10)
VK_LOGIC_OP_OR_REVERSE = VkLogicOp(11)
VK_LOGIC_OP_COPY_INVERTED = VkLogicOp(12)
VK_LOGIC_OP_OR_INVERTED = VkLogicOp(13)
VK_LOGIC_OP_NAND = VkLogicOp(14)
VK_LOGIC_OP_SET = VkLogicOp(15)

VkMemoryHeapFlagBits = type('VkMemoryHeapFlagBits', (c_enum,), dict(names=dict()))
VkMemoryHeapFlagBits.names = {
    1 : 'VK_MEMORY_HEAP_DEVICE_LOCAL_BIT',
    2 : 'VK_MEMORY_HEAP_MULTI_INSTANCE_BIT',
}
VK_MEMORY_HEAP_DEVICE_LOCAL_BIT = VkMemoryHeapFlagBits(1)
VK_MEMORY_HEAP_MULTI_INSTANCE_BIT = VkMemoryHeapFlagBits(2)
VK_MEMORY_HEAP_MULTI_INSTANCE_BIT_KHR = VK_MEMORY_HEAP_MULTI_INSTANCE_BIT

VkAccessFlagBits = type('VkAccessFlagBits', (c_enum,), dict(names=dict()))
VkAccessFlagBits.names = {
    1 : 'VK_ACCESS_INDIRECT_COMMAND_READ_BIT',
    2 : 'VK_ACCESS_INDEX_READ_BIT',
    4 : 'VK_ACCESS_VERTEX_ATTRIBUTE_READ_BIT',
    8 : 'VK_ACCESS_UNIFORM_READ_BIT',
    16 : 'VK_ACCESS_INPUT_ATTACHMENT_READ_BIT',
    32 : 'VK_ACCESS_SHADER_READ_BIT',
    64 : 'VK_ACCESS_SHADER_WRITE_BIT',
    128 : 'VK_ACCESS_COLOR_ATTACHMENT_READ_BIT',
    256 : 'VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT',
    512 : 'VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_READ_BIT',
    1024 : 'VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT',
    2048 : 'VK_ACCESS_TRANSFER_READ_BIT',
    4096 : 'VK_ACCESS_TRANSFER_WRITE_BIT',
    8192 : 'VK_ACCESS_HOST_READ_BIT',
    16384 : 'VK_ACCESS_HOST_WRITE_BIT',
    32768 : 'VK_ACCESS_MEMORY_READ_BIT',
    65536 : 'VK_ACCESS_MEMORY_WRITE_BIT',
    33554432 : 'VK_ACCESS_TRANSFORM_FEEDBACK_WRITE_BIT_EXT',
    67108864 : 'VK_ACCESS_TRANSFORM_FEEDBACK_COUNTER_READ_BIT_EXT',
    134217728 : 'VK_ACCESS_TRANSFORM_FEEDBACK_COUNTER_WRITE_BIT_EXT',
    1048576 : 'VK_ACCESS_CONDITIONAL_RENDERING_READ_BIT_EXT',
    524288 : 'VK_ACCESS_COLOR_ATTACHMENT_READ_NONCOHERENT_BIT_EXT',
    2097152 : 'VK_ACCESS_ACCELERATION_STRUCTURE_READ_BIT_KHR',
    4194304 : 'VK_ACCESS_ACCELERATION_STRUCTURE_WRITE_BIT_KHR',
    8388608 : 'VK_ACCESS_SHADING_RATE_IMAGE_READ_BIT_NV',
    16777216 : 'VK_ACCESS_FRAGMENT_DENSITY_MAP_READ_BIT_EXT',
    131072 : 'VK_ACCESS_COMMAND_PREPROCESS_READ_BIT_NV',
    262144 : 'VK_ACCESS_COMMAND_PREPROCESS_WRITE_BIT_NV',
}
VK_ACCESS_INDIRECT_COMMAND_READ_BIT = VkAccessFlagBits(1)
VK_ACCESS_INDEX_READ_BIT = VkAccessFlagBits(2)
VK_ACCESS_VERTEX_ATTRIBUTE_READ_BIT = VkAccessFlagBits(4)
VK_ACCESS_UNIFORM_READ_BIT = VkAccessFlagBits(8)
VK_ACCESS_INPUT_ATTACHMENT_READ_BIT = VkAccessFlagBits(16)
VK_ACCESS_SHADER_READ_BIT = VkAccessFlagBits(32)
VK_ACCESS_SHADER_WRITE_BIT = VkAccessFlagBits(64)
VK_ACCESS_COLOR_ATTACHMENT_READ_BIT = VkAccessFlagBits(128)
VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT = VkAccessFlagBits(256)
VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_READ_BIT = VkAccessFlagBits(512)
VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT = VkAccessFlagBits(1024)
VK_ACCESS_TRANSFER_READ_BIT = VkAccessFlagBits(2048)
VK_ACCESS_TRANSFER_WRITE_BIT = VkAccessFlagBits(4096)
VK_ACCESS_HOST_READ_BIT = VkAccessFlagBits(8192)
VK_ACCESS_HOST_WRITE_BIT = VkAccessFlagBits(16384)
VK_ACCESS_MEMORY_READ_BIT = VkAccessFlagBits(32768)
VK_ACCESS_MEMORY_WRITE_BIT = VkAccessFlagBits(65536)
VK_ACCESS_TRANSFORM_FEEDBACK_WRITE_BIT_EXT = VkAccessFlagBits(33554432)
VK_ACCESS_TRANSFORM_FEEDBACK_COUNTER_READ_BIT_EXT = VkAccessFlagBits(67108864)
VK_ACCESS_TRANSFORM_FEEDBACK_COUNTER_WRITE_BIT_EXT = VkAccessFlagBits(134217728)
VK_ACCESS_CONDITIONAL_RENDERING_READ_BIT_EXT = VkAccessFlagBits(1048576)
VK_ACCESS_COLOR_ATTACHMENT_READ_NONCOHERENT_BIT_EXT = VkAccessFlagBits(524288)
VK_ACCESS_ACCELERATION_STRUCTURE_READ_BIT_KHR = VkAccessFlagBits(2097152)
VK_ACCESS_ACCELERATION_STRUCTURE_WRITE_BIT_KHR = VkAccessFlagBits(4194304)
VK_ACCESS_SHADING_RATE_IMAGE_READ_BIT_NV = VkAccessFlagBits(8388608)
VK_ACCESS_ACCELERATION_STRUCTURE_READ_BIT_NV = VK_ACCESS_ACCELERATION_STRUCTURE_READ_BIT_KHR
VK_ACCESS_ACCELERATION_STRUCTURE_WRITE_BIT_NV = VK_ACCESS_ACCELERATION_STRUCTURE_WRITE_BIT_KHR
VK_ACCESS_FRAGMENT_DENSITY_MAP_READ_BIT_EXT = VkAccessFlagBits(16777216)
VK_ACCESS_FRAGMENT_SHADING_RATE_ATTACHMENT_READ_BIT_KHR = VK_ACCESS_SHADING_RATE_IMAGE_READ_BIT_NV
VK_ACCESS_COMMAND_PREPROCESS_READ_BIT_NV = VkAccessFlagBits(131072)
VK_ACCESS_COMMAND_PREPROCESS_WRITE_BIT_NV = VkAccessFlagBits(262144)

VkMemoryPropertyFlagBits = type('VkMemoryPropertyFlagBits', (c_enum,), dict(names=dict()))
VkMemoryPropertyFlagBits.names = {
    1 : 'VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT',
    2 : 'VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT',
    4 : 'VK_MEMORY_PROPERTY_HOST_COHERENT_BIT',
    8 : 'VK_MEMORY_PROPERTY_HOST_CACHED_BIT',
    16 : 'VK_MEMORY_PROPERTY_LAZILY_ALLOCATED_BIT',
    32 : 'VK_MEMORY_PROPERTY_PROTECTED_BIT',
    64 : 'VK_MEMORY_PROPERTY_DEVICE_COHERENT_BIT_AMD',
    128 : 'VK_MEMORY_PROPERTY_DEVICE_UNCACHED_BIT_AMD',
}
VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT = VkMemoryPropertyFlagBits(1)
VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT = VkMemoryPropertyFlagBits(2)
VK_MEMORY_PROPERTY_HOST_COHERENT_BIT = VkMemoryPropertyFlagBits(4)
VK_MEMORY_PROPERTY_HOST_CACHED_BIT = VkMemoryPropertyFlagBits(8)
VK_MEMORY_PROPERTY_LAZILY_ALLOCATED_BIT = VkMemoryPropertyFlagBits(16)
VK_MEMORY_PROPERTY_PROTECTED_BIT = VkMemoryPropertyFlagBits(32)
VK_MEMORY_PROPERTY_DEVICE_COHERENT_BIT_AMD = VkMemoryPropertyFlagBits(64)
VK_MEMORY_PROPERTY_DEVICE_UNCACHED_BIT_AMD = VkMemoryPropertyFlagBits(128)

VkPhysicalDeviceType = type('VkPhysicalDeviceType', (c_enum,), dict(names=dict()))
VkPhysicalDeviceType.names = {
    0 : 'VK_PHYSICAL_DEVICE_TYPE_OTHER',
    1 : 'VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU',
    2 : 'VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU',
    3 : 'VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU',
    4 : 'VK_PHYSICAL_DEVICE_TYPE_CPU',
}
VK_PHYSICAL_DEVICE_TYPE_OTHER = VkPhysicalDeviceType(0)
VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU = VkPhysicalDeviceType(1)
VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU = VkPhysicalDeviceType(2)
VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU = VkPhysicalDeviceType(3)
VK_PHYSICAL_DEVICE_TYPE_CPU = VkPhysicalDeviceType(4)

VkPipelineBindPoint = type('VkPipelineBindPoint', (c_enum,), dict(names=dict()))
VkPipelineBindPoint.names = {
    0 : 'VK_PIPELINE_BIND_POINT_GRAPHICS',
    1 : 'VK_PIPELINE_BIND_POINT_COMPUTE',
    1000165000 : 'VK_PIPELINE_BIND_POINT_RAY_TRACING_KHR',
}
VK_PIPELINE_BIND_POINT_GRAPHICS = VkPipelineBindPoint(0)
VK_PIPELINE_BIND_POINT_COMPUTE = VkPipelineBindPoint(1)
VK_PIPELINE_BIND_POINT_RAY_TRACING_KHR = VkPipelineBindPoint(1000165000)
VK_PIPELINE_BIND_POINT_RAY_TRACING_NV = VK_PIPELINE_BIND_POINT_RAY_TRACING_KHR

VkPipelineCreateFlagBits = type('VkPipelineCreateFlagBits', (c_enum,), dict(names=dict()))
VkPipelineCreateFlagBits.names = {
    1 : 'VK_PIPELINE_CREATE_DISABLE_OPTIMIZATION_BIT',
    2 : 'VK_PIPELINE_CREATE_ALLOW_DERIVATIVES_BIT',
    4 : 'VK_PIPELINE_CREATE_DERIVATIVE_BIT',
    8 : 'VK_PIPELINE_CREATE_VIEW_INDEX_FROM_DEVICE_INDEX_BIT',
    16 : 'VK_PIPELINE_CREATE_DISPATCH_BASE_BIT',
    16384 : 'VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_ANY_HIT_SHADERS_BIT_KHR',
    32768 : 'VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_CLOSEST_HIT_SHADERS_BIT_KHR',
    65536 : 'VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_MISS_SHADERS_BIT_KHR',
    131072 : 'VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_INTERSECTION_SHADERS_BIT_KHR',
    4096 : 'VK_PIPELINE_CREATE_RAY_TRACING_SKIP_TRIANGLES_BIT_KHR',
    8192 : 'VK_PIPELINE_CREATE_RAY_TRACING_SKIP_AABBS_BIT_KHR',
    524288 : 'VK_PIPELINE_CREATE_RAY_TRACING_SHADER_GROUP_HANDLE_CAPTURE_REPLAY_BIT_KHR',
    32 : 'VK_PIPELINE_CREATE_DEFER_COMPILE_BIT_NV',
    64 : 'VK_PIPELINE_CREATE_CAPTURE_STATISTICS_BIT_KHR',
    128 : 'VK_PIPELINE_CREATE_CAPTURE_INTERNAL_REPRESENTATIONS_BIT_KHR',
    262144 : 'VK_PIPELINE_CREATE_INDIRECT_BINDABLE_BIT_NV',
    2048 : 'VK_PIPELINE_CREATE_LIBRARY_BIT_KHR',
    256 : 'VK_PIPELINE_CREATE_FAIL_ON_PIPELINE_COMPILE_REQUIRED_BIT_EXT',
    512 : 'VK_PIPELINE_CREATE_EARLY_RETURN_ON_FAILURE_BIT_EXT',
}
VK_PIPELINE_CREATE_DISABLE_OPTIMIZATION_BIT = VkPipelineCreateFlagBits(1)
VK_PIPELINE_CREATE_ALLOW_DERIVATIVES_BIT = VkPipelineCreateFlagBits(2)
VK_PIPELINE_CREATE_DERIVATIVE_BIT = VkPipelineCreateFlagBits(4)
VK_PIPELINE_CREATE_VIEW_INDEX_FROM_DEVICE_INDEX_BIT = VkPipelineCreateFlagBits(8)
VK_PIPELINE_CREATE_DISPATCH_BASE_BIT = VkPipelineCreateFlagBits(16)
VK_PIPELINE_CREATE_DISPATCH_BASE = VK_PIPELINE_CREATE_DISPATCH_BASE_BIT
VK_PIPELINE_CREATE_VIEW_INDEX_FROM_DEVICE_INDEX_BIT_KHR = VK_PIPELINE_CREATE_VIEW_INDEX_FROM_DEVICE_INDEX_BIT
VK_PIPELINE_CREATE_DISPATCH_BASE_KHR = VK_PIPELINE_CREATE_DISPATCH_BASE
VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_ANY_HIT_SHADERS_BIT_KHR = VkPipelineCreateFlagBits(16384)
VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_CLOSEST_HIT_SHADERS_BIT_KHR = VkPipelineCreateFlagBits(32768)
VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_MISS_SHADERS_BIT_KHR = VkPipelineCreateFlagBits(65536)
VK_PIPELINE_CREATE_RAY_TRACING_NO_NULL_INTERSECTION_SHADERS_BIT_KHR = VkPipelineCreateFlagBits(131072)
VK_PIPELINE_CREATE_RAY_TRACING_SKIP_TRIANGLES_BIT_KHR = VkPipelineCreateFlagBits(4096)
VK_PIPELINE_CREATE_RAY_TRACING_SKIP_AABBS_BIT_KHR = VkPipelineCreateFlagBits(8192)
VK_PIPELINE_CREATE_RAY_TRACING_SHADER_GROUP_HANDLE_CAPTURE_REPLAY_BIT_KHR = VkPipelineCreateFlagBits(524288)
VK_PIPELINE_CREATE_DEFER_COMPILE_BIT_NV = VkPipelineCreateFlagBits(32)
VK_PIPELINE_CREATE_CAPTURE_STATISTICS_BIT_KHR = VkPipelineCreateFlagBits(64)
VK_PIPELINE_CREATE_CAPTURE_INTERNAL_REPRESENTATIONS_BIT_KHR = VkPipelineCreateFlagBits(128)
VK_PIPELINE_CREATE_INDIRECT_BINDABLE_BIT_NV = VkPipelineCreateFlagBits(262144)
VK_PIPELINE_CREATE_LIBRARY_BIT_KHR = VkPipelineCreateFlagBits(2048)
VK_PIPELINE_CREATE_FAIL_ON_PIPELINE_COMPILE_REQUIRED_BIT_EXT = VkPipelineCreateFlagBits(256)
VK_PIPELINE_CREATE_EARLY_RETURN_ON_FAILURE_BIT_EXT = VkPipelineCreateFlagBits(512)

VkPrimitiveTopology = type('VkPrimitiveTopology', (c_enum,), dict(names=dict()))
VkPrimitiveTopology.names = {
    0 : 'VK_PRIMITIVE_TOPOLOGY_POINT_LIST',
    1 : 'VK_PRIMITIVE_TOPOLOGY_LINE_LIST',
    2 : 'VK_PRIMITIVE_TOPOLOGY_LINE_STRIP',
    3 : 'VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST',
    4 : 'VK_PRIMITIVE_TOPOLOGY_TRIANGLE_STRIP',
    5 : 'VK_PRIMITIVE_TOPOLOGY_TRIANGLE_FAN',
    6 : 'VK_PRIMITIVE_TOPOLOGY_LINE_LIST_WITH_ADJACENCY',
    7 : 'VK_PRIMITIVE_TOPOLOGY_LINE_STRIP_WITH_ADJACENCY',
    8 : 'VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST_WITH_ADJACENCY',
    9 : 'VK_PRIMITIVE_TOPOLOGY_TRIANGLE_STRIP_WITH_ADJACENCY',
    10 : 'VK_PRIMITIVE_TOPOLOGY_PATCH_LIST',
}
VK_PRIMITIVE_TOPOLOGY_POINT_LIST = VkPrimitiveTopology(0)
VK_PRIMITIVE_TOPOLOGY_LINE_LIST = VkPrimitiveTopology(1)
VK_PRIMITIVE_TOPOLOGY_LINE_STRIP = VkPrimitiveTopology(2)
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST = VkPrimitiveTopology(3)
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_STRIP = VkPrimitiveTopology(4)
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_FAN = VkPrimitiveTopology(5)
VK_PRIMITIVE_TOPOLOGY_LINE_LIST_WITH_ADJACENCY = VkPrimitiveTopology(6)
VK_PRIMITIVE_TOPOLOGY_LINE_STRIP_WITH_ADJACENCY = VkPrimitiveTopology(7)
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST_WITH_ADJACENCY = VkPrimitiveTopology(8)
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_STRIP_WITH_ADJACENCY = VkPrimitiveTopology(9)
VK_PRIMITIVE_TOPOLOGY_PATCH_LIST = VkPrimitiveTopology(10)

VkQueryControlFlagBits = type('VkQueryControlFlagBits', (c_enum,), dict(names=dict()))
VkQueryControlFlagBits.names = {
    1 : 'VK_QUERY_CONTROL_PRECISE_BIT',
}
VK_QUERY_CONTROL_PRECISE_BIT = VkQueryControlFlagBits(1)

VkQueryPipelineStatisticFlagBits = type('VkQueryPipelineStatisticFlagBits', (c_enum,), dict(names=dict()))
VkQueryPipelineStatisticFlagBits.names = {
    1 : 'VK_QUERY_PIPELINE_STATISTIC_INPUT_ASSEMBLY_VERTICES_BIT',
    2 : 'VK_QUERY_PIPELINE_STATISTIC_INPUT_ASSEMBLY_PRIMITIVES_BIT',
    4 : 'VK_QUERY_PIPELINE_STATISTIC_VERTEX_SHADER_INVOCATIONS_BIT',
    8 : 'VK_QUERY_PIPELINE_STATISTIC_GEOMETRY_SHADER_INVOCATIONS_BIT',
    16 : 'VK_QUERY_PIPELINE_STATISTIC_GEOMETRY_SHADER_PRIMITIVES_BIT',
    32 : 'VK_QUERY_PIPELINE_STATISTIC_CLIPPING_INVOCATIONS_BIT',
    64 : 'VK_QUERY_PIPELINE_STATISTIC_CLIPPING_PRIMITIVES_BIT',
    128 : 'VK_QUERY_PIPELINE_STATISTIC_FRAGMENT_SHADER_INVOCATIONS_BIT',
    256 : 'VK_QUERY_PIPELINE_STATISTIC_TESSELLATION_CONTROL_SHADER_PATCHES_BIT',
    512 : 'VK_QUERY_PIPELINE_STATISTIC_TESSELLATION_EVALUATION_SHADER_INVOCATIONS_BIT',
    1024 : 'VK_QUERY_PIPELINE_STATISTIC_COMPUTE_SHADER_INVOCATIONS_BIT',
}
VK_QUERY_PIPELINE_STATISTIC_INPUT_ASSEMBLY_VERTICES_BIT = VkQueryPipelineStatisticFlagBits(1)
VK_QUERY_PIPELINE_STATISTIC_INPUT_ASSEMBLY_PRIMITIVES_BIT = VkQueryPipelineStatisticFlagBits(2)
VK_QUERY_PIPELINE_STATISTIC_VERTEX_SHADER_INVOCATIONS_BIT = VkQueryPipelineStatisticFlagBits(4)
VK_QUERY_PIPELINE_STATISTIC_GEOMETRY_SHADER_INVOCATIONS_BIT = VkQueryPipelineStatisticFlagBits(8)
VK_QUERY_PIPELINE_STATISTIC_GEOMETRY_SHADER_PRIMITIVES_BIT = VkQueryPipelineStatisticFlagBits(16)
VK_QUERY_PIPELINE_STATISTIC_CLIPPING_INVOCATIONS_BIT = VkQueryPipelineStatisticFlagBits(32)
VK_QUERY_PIPELINE_STATISTIC_CLIPPING_PRIMITIVES_BIT = VkQueryPipelineStatisticFlagBits(64)
VK_QUERY_PIPELINE_STATISTIC_FRAGMENT_SHADER_INVOCATIONS_BIT = VkQueryPipelineStatisticFlagBits(128)
VK_QUERY_PIPELINE_STATISTIC_TESSELLATION_CONTROL_SHADER_PATCHES_BIT = VkQueryPipelineStatisticFlagBits(256)
VK_QUERY_PIPELINE_STATISTIC_TESSELLATION_EVALUATION_SHADER_INVOCATIONS_BIT = VkQueryPipelineStatisticFlagBits(512)
VK_QUERY_PIPELINE_STATISTIC_COMPUTE_SHADER_INVOCATIONS_BIT = VkQueryPipelineStatisticFlagBits(1024)

VkQueryResultFlagBits = type('VkQueryResultFlagBits', (c_enum,), dict(names=dict()))
VkQueryResultFlagBits.names = {
    1 : 'VK_QUERY_RESULT_64_BIT',
    2 : 'VK_QUERY_RESULT_WAIT_BIT',
    4 : 'VK_QUERY_RESULT_WITH_AVAILABILITY_BIT',
    8 : 'VK_QUERY_RESULT_PARTIAL_BIT',
}
VK_QUERY_RESULT_64_BIT = VkQueryResultFlagBits(1)
VK_QUERY_RESULT_WAIT_BIT = VkQueryResultFlagBits(2)
VK_QUERY_RESULT_WITH_AVAILABILITY_BIT = VkQueryResultFlagBits(4)
VK_QUERY_RESULT_PARTIAL_BIT = VkQueryResultFlagBits(8)

VkQueryType = type('VkQueryType', (c_enum,), dict(names=dict()))
VkQueryType.names = {
    0 : 'VK_QUERY_TYPE_OCCLUSION',
    1 : 'VK_QUERY_TYPE_PIPELINE_STATISTICS',
    2 : 'VK_QUERY_TYPE_TIMESTAMP',
    1000028004 : 'VK_QUERY_TYPE_TRANSFORM_FEEDBACK_STREAM_EXT',
    1000116000 : 'VK_QUERY_TYPE_PERFORMANCE_QUERY_KHR',
    1000150000 : 'VK_QUERY_TYPE_ACCELERATION_STRUCTURE_COMPACTED_SIZE_KHR',
    1000150001 : 'VK_QUERY_TYPE_ACCELERATION_STRUCTURE_SERIALIZATION_SIZE_KHR',
    1000165000 : 'VK_QUERY_TYPE_ACCELERATION_STRUCTURE_COMPACTED_SIZE_NV',
    1000210000 : 'VK_QUERY_TYPE_PERFORMANCE_QUERY_INTEL',
}
VK_QUERY_TYPE_OCCLUSION = VkQueryType(0)
VK_QUERY_TYPE_PIPELINE_STATISTICS = VkQueryType(1)
VK_QUERY_TYPE_TIMESTAMP = VkQueryType(2)
VK_QUERY_TYPE_TRANSFORM_FEEDBACK_STREAM_EXT = VkQueryType(1000028004)
VK_QUERY_TYPE_PERFORMANCE_QUERY_KHR = VkQueryType(1000116000)
VK_QUERY_TYPE_ACCELERATION_STRUCTURE_COMPACTED_SIZE_KHR = VkQueryType(1000150000)
VK_QUERY_TYPE_ACCELERATION_STRUCTURE_SERIALIZATION_SIZE_KHR = VkQueryType(1000150001)
VK_QUERY_TYPE_ACCELERATION_STRUCTURE_COMPACTED_SIZE_NV = VkQueryType(1000165000)
VK_QUERY_TYPE_PERFORMANCE_QUERY_INTEL = VkQueryType(1000210000)

VkQueueFlagBits = type('VkQueueFlagBits', (c_enum,), dict(names=dict()))
VkQueueFlagBits.names = {
    1 : 'VK_QUEUE_GRAPHICS_BIT',
    2 : 'VK_QUEUE_COMPUTE_BIT',
    4 : 'VK_QUEUE_TRANSFER_BIT',
    8 : 'VK_QUEUE_SPARSE_BINDING_BIT',
    16 : 'VK_QUEUE_PROTECTED_BIT',
}
VK_QUEUE_GRAPHICS_BIT = VkQueueFlagBits(1)
VK_QUEUE_COMPUTE_BIT = VkQueueFlagBits(2)
VK_QUEUE_TRANSFER_BIT = VkQueueFlagBits(4)
VK_QUEUE_SPARSE_BINDING_BIT = VkQueueFlagBits(8)
VK_QUEUE_PROTECTED_BIT = VkQueueFlagBits(16)

VkSubpassContents = type('VkSubpassContents', (c_enum,), dict(names=dict()))
VkSubpassContents.names = {
    0 : 'VK_SUBPASS_CONTENTS_INLINE',
    1 : 'VK_SUBPASS_CONTENTS_SECONDARY_COMMAND_BUFFERS',
}
VK_SUBPASS_CONTENTS_INLINE = VkSubpassContents(0)
VK_SUBPASS_CONTENTS_SECONDARY_COMMAND_BUFFERS = VkSubpassContents(1)

VkResult = type('VkResult', (c_enum,), dict(names=dict()))
VkResult.names = {
    0 : 'VK_SUCCESS',
    1 : 'VK_NOT_READY',
    2 : 'VK_TIMEOUT',
    3 : 'VK_EVENT_SET',
    4 : 'VK_EVENT_RESET',
    5 : 'VK_INCOMPLETE',
    -1 : 'VK_ERROR_OUT_OF_HOST_MEMORY',
    -2 : 'VK_ERROR_OUT_OF_DEVICE_MEMORY',
    -3 : 'VK_ERROR_INITIALIZATION_FAILED',
    -4 : 'VK_ERROR_DEVICE_LOST',
    -5 : 'VK_ERROR_MEMORY_MAP_FAILED',
    -6 : 'VK_ERROR_LAYER_NOT_PRESENT',
    -7 : 'VK_ERROR_EXTENSION_NOT_PRESENT',
    -8 : 'VK_ERROR_FEATURE_NOT_PRESENT',
    -9 : 'VK_ERROR_INCOMPATIBLE_DRIVER',
    -10 : 'VK_ERROR_TOO_MANY_OBJECTS',
    -11 : 'VK_ERROR_FORMAT_NOT_SUPPORTED',
    -12 : 'VK_ERROR_FRAGMENTED_POOL',
    -13 : 'VK_ERROR_UNKNOWN',
    1000069000 : 'VK_ERROR_OUT_OF_POOL_MEMORY',
    1000072003 : 'VK_ERROR_INVALID_EXTERNAL_HANDLE',
    1000161000 : 'VK_ERROR_FRAGMENTATION',
    1000257000 : 'VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS',
    1000000000 : 'VK_ERROR_SURFACE_LOST_KHR',
    1000000001 : 'VK_ERROR_NATIVE_WINDOW_IN_USE_KHR',
    1000001003 : 'VK_SUBOPTIMAL_KHR',
    1000001004 : 'VK_ERROR_OUT_OF_DATE_KHR',
    1000003001 : 'VK_ERROR_INCOMPATIBLE_DISPLAY_KHR',
    1000011001 : 'VK_ERROR_VALIDATION_FAILED_EXT',
    1000012000 : 'VK_ERROR_INVALID_SHADER_NV',
    1000158000 : 'VK_ERROR_INVALID_DRM_FORMAT_MODIFIER_PLANE_LAYOUT_EXT',
    1000174001 : 'VK_ERROR_NOT_PERMITTED_EXT',
    1000255000 : 'VK_ERROR_FULL_SCREEN_EXCLUSIVE_MODE_LOST_EXT',
    1000268000 : 'VK_THREAD_IDLE_KHR',
    1000268001 : 'VK_THREAD_DONE_KHR',
    1000268002 : 'VK_OPERATION_DEFERRED_KHR',
    1000268003 : 'VK_OPERATION_NOT_DEFERRED_KHR',
    1000297000 : 'VK_PIPELINE_COMPILE_REQUIRED_EXT',
}
VK_SUCCESS = VkResult(0)
VK_NOT_READY = VkResult(1)
VK_TIMEOUT = VkResult(2)
VK_EVENT_SET = VkResult(3)
VK_EVENT_RESET = VkResult(4)
VK_INCOMPLETE = VkResult(5)
VK_ERROR_OUT_OF_HOST_MEMORY = VkResult(-1)
VK_ERROR_OUT_OF_DEVICE_MEMORY = VkResult(-2)
VK_ERROR_INITIALIZATION_FAILED = VkResult(-3)
VK_ERROR_DEVICE_LOST = VkResult(-4)
VK_ERROR_MEMORY_MAP_FAILED = VkResult(-5)
VK_ERROR_LAYER_NOT_PRESENT = VkResult(-6)
VK_ERROR_EXTENSION_NOT_PRESENT = VkResult(-7)
VK_ERROR_FEATURE_NOT_PRESENT = VkResult(-8)
VK_ERROR_INCOMPATIBLE_DRIVER = VkResult(-9)
VK_ERROR_TOO_MANY_OBJECTS = VkResult(-10)
VK_ERROR_FORMAT_NOT_SUPPORTED = VkResult(-11)
VK_ERROR_FRAGMENTED_POOL = VkResult(-12)
VK_ERROR_UNKNOWN = VkResult(-13)
VK_ERROR_OUT_OF_POOL_MEMORY = VkResult(-1000069000)
VK_ERROR_INVALID_EXTERNAL_HANDLE = VkResult(-1000072003)
VK_ERROR_FRAGMENTATION = VkResult(-1000161000)
VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS = VkResult(-1000257000)
VK_ERROR_SURFACE_LOST_KHR = VkResult(-1000000000)
VK_ERROR_NATIVE_WINDOW_IN_USE_KHR = VkResult(-1000000001)
VK_SUBOPTIMAL_KHR = VkResult(1000001003)
VK_ERROR_OUT_OF_DATE_KHR = VkResult(-1000001004)
VK_ERROR_INCOMPATIBLE_DISPLAY_KHR = VkResult(-1000003001)
VK_ERROR_VALIDATION_FAILED_EXT = VkResult(-1000011001)
VK_ERROR_INVALID_SHADER_NV = VkResult(-1000012000)
VK_ERROR_OUT_OF_POOL_MEMORY_KHR = VK_ERROR_OUT_OF_POOL_MEMORY
VK_ERROR_INVALID_EXTERNAL_HANDLE_KHR = VK_ERROR_INVALID_EXTERNAL_HANDLE
VK_ERROR_INVALID_DRM_FORMAT_MODIFIER_PLANE_LAYOUT_EXT = VkResult(-1000158000)
VK_ERROR_FRAGMENTATION_EXT = VK_ERROR_FRAGMENTATION
VK_ERROR_NOT_PERMITTED_EXT = VkResult(-1000174001)
VK_ERROR_INVALID_DEVICE_ADDRESS_EXT = VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS
VK_ERROR_FULL_SCREEN_EXCLUSIVE_MODE_LOST_EXT = VkResult(-1000255000)
VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS_KHR = VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS
VK_THREAD_IDLE_KHR = VkResult(1000268000)
VK_THREAD_DONE_KHR = VkResult(1000268001)
VK_OPERATION_DEFERRED_KHR = VkResult(1000268002)
VK_OPERATION_NOT_DEFERRED_KHR = VkResult(1000268003)
VK_PIPELINE_COMPILE_REQUIRED_EXT = VkResult(1000297000)
VK_ERROR_PIPELINE_COMPILE_REQUIRED_EXT = VK_PIPELINE_COMPILE_REQUIRED_EXT

VkShaderStageFlagBits = type('VkShaderStageFlagBits', (c_enum,), dict(names=dict()))
VkShaderStageFlagBits.names = {
    1 : 'VK_SHADER_STAGE_VERTEX_BIT',
    2 : 'VK_SHADER_STAGE_TESSELLATION_CONTROL_BIT',
    4 : 'VK_SHADER_STAGE_TESSELLATION_EVALUATION_BIT',
    8 : 'VK_SHADER_STAGE_GEOMETRY_BIT',
    16 : 'VK_SHADER_STAGE_FRAGMENT_BIT',
    32 : 'VK_SHADER_STAGE_COMPUTE_BIT',
    0x0000001F : 'VK_SHADER_STAGE_ALL_GRAPHICS',
    0x7FFFFFFF : 'VK_SHADER_STAGE_ALL',
    256 : 'VK_SHADER_STAGE_RAYGEN_BIT_KHR',
    512 : 'VK_SHADER_STAGE_ANY_HIT_BIT_KHR',
    1024 : 'VK_SHADER_STAGE_CLOSEST_HIT_BIT_KHR',
    2048 : 'VK_SHADER_STAGE_MISS_BIT_KHR',
    4096 : 'VK_SHADER_STAGE_INTERSECTION_BIT_KHR',
    8192 : 'VK_SHADER_STAGE_CALLABLE_BIT_KHR',
    64 : 'VK_SHADER_STAGE_TASK_BIT_NV',
    128 : 'VK_SHADER_STAGE_MESH_BIT_NV',
}
VK_SHADER_STAGE_VERTEX_BIT = VkShaderStageFlagBits(1)
VK_SHADER_STAGE_TESSELLATION_CONTROL_BIT = VkShaderStageFlagBits(2)
VK_SHADER_STAGE_TESSELLATION_EVALUATION_BIT = VkShaderStageFlagBits(4)
VK_SHADER_STAGE_GEOMETRY_BIT = VkShaderStageFlagBits(8)
VK_SHADER_STAGE_FRAGMENT_BIT = VkShaderStageFlagBits(16)
VK_SHADER_STAGE_COMPUTE_BIT = VkShaderStageFlagBits(32)
VK_SHADER_STAGE_ALL_GRAPHICS = VkShaderStageFlagBits(0x0000001F)
VK_SHADER_STAGE_ALL = VkShaderStageFlagBits(0x7FFFFFFF)
VK_SHADER_STAGE_RAYGEN_BIT_KHR = VkShaderStageFlagBits(256)
VK_SHADER_STAGE_ANY_HIT_BIT_KHR = VkShaderStageFlagBits(512)
VK_SHADER_STAGE_CLOSEST_HIT_BIT_KHR = VkShaderStageFlagBits(1024)
VK_SHADER_STAGE_MISS_BIT_KHR = VkShaderStageFlagBits(2048)
VK_SHADER_STAGE_INTERSECTION_BIT_KHR = VkShaderStageFlagBits(4096)
VK_SHADER_STAGE_CALLABLE_BIT_KHR = VkShaderStageFlagBits(8192)
VK_SHADER_STAGE_RAYGEN_BIT_NV = VK_SHADER_STAGE_RAYGEN_BIT_KHR
VK_SHADER_STAGE_ANY_HIT_BIT_NV = VK_SHADER_STAGE_ANY_HIT_BIT_KHR
VK_SHADER_STAGE_CLOSEST_HIT_BIT_NV = VK_SHADER_STAGE_CLOSEST_HIT_BIT_KHR
VK_SHADER_STAGE_MISS_BIT_NV = VK_SHADER_STAGE_MISS_BIT_KHR
VK_SHADER_STAGE_INTERSECTION_BIT_NV = VK_SHADER_STAGE_INTERSECTION_BIT_KHR
VK_SHADER_STAGE_CALLABLE_BIT_NV = VK_SHADER_STAGE_CALLABLE_BIT_KHR
VK_SHADER_STAGE_TASK_BIT_NV = VkShaderStageFlagBits(64)
VK_SHADER_STAGE_MESH_BIT_NV = VkShaderStageFlagBits(128)

VkSparseMemoryBindFlagBits = type('VkSparseMemoryBindFlagBits', (c_enum,), dict(names=dict()))
VkSparseMemoryBindFlagBits.names = {
    1 : 'VK_SPARSE_MEMORY_BIND_METADATA_BIT',
}
VK_SPARSE_MEMORY_BIND_METADATA_BIT = VkSparseMemoryBindFlagBits(1)

VkStencilFaceFlagBits = type('VkStencilFaceFlagBits', (c_enum,), dict(names=dict()))
VkStencilFaceFlagBits.names = {
    1 : 'VK_STENCIL_FACE_FRONT_BIT',
    2 : 'VK_STENCIL_FACE_BACK_BIT',
    0x00000003 : 'VK_STENCIL_FACE_FRONT_AND_BACK',
}
VK_STENCIL_FACE_FRONT_BIT = VkStencilFaceFlagBits(1)
VK_STENCIL_FACE_BACK_BIT = VkStencilFaceFlagBits(2)
VK_STENCIL_FACE_FRONT_AND_BACK = VkStencilFaceFlagBits(0x00000003)
VK_STENCIL_FRONT_AND_BACK = VK_STENCIL_FACE_FRONT_AND_BACK

VkStencilOp = type('VkStencilOp', (c_enum,), dict(names=dict()))
VkStencilOp.names = {
    0 : 'VK_STENCIL_OP_KEEP',
    1 : 'VK_STENCIL_OP_ZERO',
    2 : 'VK_STENCIL_OP_REPLACE',
    3 : 'VK_STENCIL_OP_INCREMENT_AND_CLAMP',
    4 : 'VK_STENCIL_OP_DECREMENT_AND_CLAMP',
    5 : 'VK_STENCIL_OP_INVERT',
    6 : 'VK_STENCIL_OP_INCREMENT_AND_WRAP',
    7 : 'VK_STENCIL_OP_DECREMENT_AND_WRAP',
}
VK_STENCIL_OP_KEEP = VkStencilOp(0)
VK_STENCIL_OP_ZERO = VkStencilOp(1)
VK_STENCIL_OP_REPLACE = VkStencilOp(2)
VK_STENCIL_OP_INCREMENT_AND_CLAMP = VkStencilOp(3)
VK_STENCIL_OP_DECREMENT_AND_CLAMP = VkStencilOp(4)
VK_STENCIL_OP_INVERT = VkStencilOp(5)
VK_STENCIL_OP_INCREMENT_AND_WRAP = VkStencilOp(6)
VK_STENCIL_OP_DECREMENT_AND_WRAP = VkStencilOp(7)

VkStructureType = type('VkStructureType', (c_enum,), dict(names=dict()))
VkStructureType.names = {
    0 : 'VK_STRUCTURE_TYPE_APPLICATION_INFO',
    1 : 'VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO',
    2 : 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO',
    3 : 'VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO',
    4 : 'VK_STRUCTURE_TYPE_SUBMIT_INFO',
    5 : 'VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO',
    6 : 'VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE',
    7 : 'VK_STRUCTURE_TYPE_BIND_SPARSE_INFO',
    8 : 'VK_STRUCTURE_TYPE_FENCE_CREATE_INFO',
    9 : 'VK_STRUCTURE_TYPE_SEMAPHORE_CREATE_INFO',
    10 : 'VK_STRUCTURE_TYPE_EVENT_CREATE_INFO',
    11 : 'VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO',
    12 : 'VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO',
    13 : 'VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO',
    14 : 'VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO',
    15 : 'VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO',
    16 : 'VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO',
    17 : 'VK_STRUCTURE_TYPE_PIPELINE_CACHE_CREATE_INFO',
    18 : 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO',
    19 : 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO',
    20 : 'VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO',
    21 : 'VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_STATE_CREATE_INFO',
    22 : 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO',
    23 : 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO',
    24 : 'VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO',
    25 : 'VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO',
    26 : 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO',
    27 : 'VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO',
    28 : 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO',
    29 : 'VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO',
    30 : 'VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO',
    31 : 'VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO',
    32 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO',
    33 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO',
    34 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO',
    35 : 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET',
    36 : 'VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET',
    37 : 'VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO',
    38 : 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO',
    39 : 'VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO',
    40 : 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO',
    41 : 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO',
    42 : 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO',
    43 : 'VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO',
    44 : 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER',
    45 : 'VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER',
    46 : 'VK_STRUCTURE_TYPE_MEMORY_BARRIER',
    47 : 'VK_STRUCTURE_TYPE_LOADER_INSTANCE_CREATE_INFO',
    48 : 'VK_STRUCTURE_TYPE_LOADER_DEVICE_CREATE_INFO',
    1000094000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_PROPERTIES',
    1000157000 : 'VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO',
    1000157001 : 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO',
    1000083000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES',
    1000127000 : 'VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS',
    1000127001 : 'VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO',
    1000060000 : 'VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_FLAGS_INFO',
    1000060003 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO',
    1000060004 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_COMMAND_BUFFER_BEGIN_INFO',
    1000060005 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO',
    1000060006 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO',
    1000060013 : 'VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO',
    1000060014 : 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO',
    1000070000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES',
    1000070001 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO',
    1000146000 : 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_REQUIREMENTS_INFO_2',
    1000146001 : 'VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2',
    1000146002 : 'VK_STRUCTURE_TYPE_IMAGE_SPARSE_MEMORY_REQUIREMENTS_INFO_2',
    1000146003 : 'VK_STRUCTURE_TYPE_MEMORY_REQUIREMENTS_2',
    1000146004 : 'VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2',
    1000059000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2',
    1000059001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2',
    1000059002 : 'VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2',
    1000059003 : 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2',
    1000059004 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2',
    1000059005 : 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2',
    1000059006 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2',
    1000059007 : 'VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2',
    1000059008 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2',
    1000117000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_POINT_CLIPPING_PROPERTIES',
    1000117001 : 'VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO',
    1000117002 : 'VK_STRUCTURE_TYPE_IMAGE_VIEW_USAGE_CREATE_INFO',
    1000117003 : 'VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_DOMAIN_ORIGIN_STATE_CREATE_INFO',
    1000053000 : 'VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO',
    1000053001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_FEATURES',
    1000053002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PROPERTIES',
    1000120000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES',
    1000145000 : 'VK_STRUCTURE_TYPE_PROTECTED_SUBMIT_INFO',
    1000145001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROTECTED_MEMORY_FEATURES',
    1000145002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROTECTED_MEMORY_PROPERTIES',
    1000145003 : 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_INFO_2',
    1000156000 : 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO',
    1000156001 : 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO',
    1000156002 : 'VK_STRUCTURE_TYPE_BIND_IMAGE_PLANE_MEMORY_INFO',
    1000156003 : 'VK_STRUCTURE_TYPE_IMAGE_PLANE_MEMORY_REQUIREMENTS_INFO',
    1000156004 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_YCBCR_CONVERSION_FEATURES',
    1000156005 : 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_IMAGE_FORMAT_PROPERTIES',
    1000085000 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO',
    1000071000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_IMAGE_FORMAT_INFO',
    1000071001 : 'VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES',
    1000071002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO',
    1000071003 : 'VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES',
    1000071004 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES',
    1000072000 : 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO',
    1000072001 : 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO',
    1000072002 : 'VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO',
    1000112000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FENCE_INFO',
    1000112001 : 'VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES',
    1000113000 : 'VK_STRUCTURE_TYPE_EXPORT_FENCE_CREATE_INFO',
    1000077000 : 'VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_CREATE_INFO',
    1000076000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO',
    1000076001 : 'VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES',
    1000168000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_3_PROPERTIES',
    1000168001 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT',
    1000063000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DRAW_PARAMETERS_FEATURES',
    49 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_FEATURES',
    50 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES',
    51 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_FEATURES',
    52 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_PROPERTIES',
    1000147000 : 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO',
    1000109000 : 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2',
    1000109001 : 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2',
    1000109002 : 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2',
    1000109003 : 'VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2',
    1000109004 : 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2',
    1000109005 : 'VK_STRUCTURE_TYPE_SUBPASS_BEGIN_INFO',
    1000109006 : 'VK_STRUCTURE_TYPE_SUBPASS_END_INFO',
    1000177000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_8BIT_STORAGE_FEATURES',
    1000196000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES',
    1000180000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_INT64_FEATURES',
    1000082000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT16_INT8_FEATURES',
    1000197000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES',
    1000161000 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO',
    1000161001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES',
    1000161002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES',
    1000161003 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO',
    1000161004 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT',
    1000199000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES',
    1000199001 : 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE',
    1000221000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCALAR_BLOCK_LAYOUT_FEATURES',
    1000246000 : 'VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO',
    1000130000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_FILTER_MINMAX_PROPERTIES',
    1000130001 : 'VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO',
    1000211000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES',
    1000108000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGELESS_FRAMEBUFFER_FEATURES',
    1000108001 : 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO',
    1000108002 : 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO',
    1000108003 : 'VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO',
    1000253000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_UNIFORM_BUFFER_STANDARD_LAYOUT_FEATURES',
    1000175000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_EXTENDED_TYPES_FEATURES',
    1000241000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SEPARATE_DEPTH_STENCIL_LAYOUTS_FEATURES',
    1000241001 : 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT',
    1000241002 : 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT',
    1000261000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_QUERY_RESET_FEATURES',
    1000207000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_FEATURES',
    1000207001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_PROPERTIES',
    1000207002 : 'VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO',
    1000207003 : 'VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO',
    1000207004 : 'VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO',
    1000207005 : 'VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO',
    1000257000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES',
    1000244001 : 'VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO',
    1000257002 : 'VK_STRUCTURE_TYPE_BUFFER_OPAQUE_CAPTURE_ADDRESS_CREATE_INFO',
    1000257003 : 'VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO',
    1000257004 : 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_OPAQUE_CAPTURE_ADDRESS_INFO',
    1000001000 : 'VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR',
    1000001001 : 'VK_STRUCTURE_TYPE_PRESENT_INFO_KHR',
    1000060007 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR',
    1000060008 : 'VK_STRUCTURE_TYPE_IMAGE_SWAPCHAIN_CREATE_INFO_KHR',
    1000060009 : 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_SWAPCHAIN_INFO_KHR',
    1000060010 : 'VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR',
    1000060011 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_INFO_KHR',
    1000060012 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR',
    1000002000 : 'VK_STRUCTURE_TYPE_DISPLAY_MODE_CREATE_INFO_KHR',
    1000002001 : 'VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR',
    1000003000 : 'VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR',
    1000004000 : 'VK_STRUCTURE_TYPE_XLIB_SURFACE_CREATE_INFO_KHR',
    1000005000 : 'VK_STRUCTURE_TYPE_XCB_SURFACE_CREATE_INFO_KHR',
    1000006000 : 'VK_STRUCTURE_TYPE_WAYLAND_SURFACE_CREATE_INFO_KHR',
    1000008000 : 'VK_STRUCTURE_TYPE_ANDROID_SURFACE_CREATE_INFO_KHR',
    1000009000 : 'VK_STRUCTURE_TYPE_WIN32_SURFACE_CREATE_INFO_KHR',
    1000011000 : 'VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT',
    1000018000 : 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_RASTERIZATION_ORDER_AMD',
    1000022000 : 'VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_NAME_INFO_EXT',
    1000022001 : 'VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_TAG_INFO_EXT',
    1000022002 : 'VK_STRUCTURE_TYPE_DEBUG_MARKER_MARKER_INFO_EXT',
    1000026000 : 'VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_IMAGE_CREATE_INFO_NV',
    1000026001 : 'VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_BUFFER_CREATE_INFO_NV',
    1000026002 : 'VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_MEMORY_ALLOCATE_INFO_NV',
    1000028000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_FEATURES_EXT',
    1000028001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT',
    1000028002 : 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_STREAM_CREATE_INFO_EXT',
    1000030000 : 'VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX',
    1000030001 : 'VK_STRUCTURE_TYPE_IMAGE_VIEW_ADDRESS_PROPERTIES_NVX',
    1000041000 : 'VK_STRUCTURE_TYPE_TEXTURE_LOD_GATHER_FORMAT_PROPERTIES_AMD',
    1000049000 : 'VK_STRUCTURE_TYPE_STREAM_DESCRIPTOR_SURFACE_CREATE_INFO_GGP',
    1000050000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CORNER_SAMPLED_IMAGE_FEATURES_NV',
    1000056000 : 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO_NV',
    1000056001 : 'VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO_NV',
    1000057000 : 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_NV',
    1000057001 : 'VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_NV',
    1000058000 : 'VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_NV',
    1000060007 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR',
    1000060008 : 'VK_STRUCTURE_TYPE_IMAGE_SWAPCHAIN_CREATE_INFO_KHR',
    1000060009 : 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_SWAPCHAIN_INFO_KHR',
    1000060010 : 'VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR',
    1000060011 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_INFO_KHR',
    1000060012 : 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR',
    1000061000 : 'VK_STRUCTURE_TYPE_VALIDATION_FLAGS_EXT',
    1000062000 : 'VK_STRUCTURE_TYPE_VI_SURFACE_CREATE_INFO_NN',
    1000066000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXTURE_COMPRESSION_ASTC_HDR_FEATURES_EXT',
    1000067000 : 'VK_STRUCTURE_TYPE_IMAGE_VIEW_ASTC_DECODE_MODE_EXT',
    1000067001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ASTC_DECODE_FEATURES_EXT',
    1000073000 : 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_KHR',
    1000073001 : 'VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_KHR',
    1000073002 : 'VK_STRUCTURE_TYPE_MEMORY_WIN32_HANDLE_PROPERTIES_KHR',
    1000073003 : 'VK_STRUCTURE_TYPE_MEMORY_GET_WIN32_HANDLE_INFO_KHR',
    1000074000 : 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_FD_INFO_KHR',
    1000074001 : 'VK_STRUCTURE_TYPE_MEMORY_FD_PROPERTIES_KHR',
    1000074002 : 'VK_STRUCTURE_TYPE_MEMORY_GET_FD_INFO_KHR',
    1000075000 : 'VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_KHR',
    1000078000 : 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR',
    1000078001 : 'VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR',
    1000078002 : 'VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR',
    1000078003 : 'VK_STRUCTURE_TYPE_SEMAPHORE_GET_WIN32_HANDLE_INFO_KHR',
    1000079000 : 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_FD_INFO_KHR',
    1000079001 : 'VK_STRUCTURE_TYPE_SEMAPHORE_GET_FD_INFO_KHR',
    1000080000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PUSH_DESCRIPTOR_PROPERTIES_KHR',
    1000081000 : 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_CONDITIONAL_RENDERING_INFO_EXT',
    1000081001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONDITIONAL_RENDERING_FEATURES_EXT',
    1000081002 : 'VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT',
    1000084000 : 'VK_STRUCTURE_TYPE_PRESENT_REGIONS_KHR',
    1000087000 : 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV',
    1000090000 : 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT',
    1000091000 : 'VK_STRUCTURE_TYPE_DISPLAY_POWER_INFO_EXT',
    1000091001 : 'VK_STRUCTURE_TYPE_DEVICE_EVENT_INFO_EXT',
    1000091002 : 'VK_STRUCTURE_TYPE_DISPLAY_EVENT_INFO_EXT',
    1000091003 : 'VK_STRUCTURE_TYPE_SWAPCHAIN_COUNTER_CREATE_INFO_EXT',
    1000092000 : 'VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE',
    1000097000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PER_VIEW_ATTRIBUTES_PROPERTIES_NVX',
    1000098000 : 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV',
    1000099000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DISCARD_RECTANGLE_PROPERTIES_EXT',
    1000099001 : 'VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT',
    1000101000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT',
    1000101001 : 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_CONSERVATIVE_STATE_CREATE_INFO_EXT',
    1000102000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_CLIP_ENABLE_FEATURES_EXT',
    1000102001 : 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_DEPTH_CLIP_STATE_CREATE_INFO_EXT',
    1000105000 : 'VK_STRUCTURE_TYPE_HDR_METADATA_EXT',
    1000111000 : 'VK_STRUCTURE_TYPE_SHARED_PRESENT_SURFACE_CAPABILITIES_KHR',
    1000114000 : 'VK_STRUCTURE_TYPE_IMPORT_FENCE_WIN32_HANDLE_INFO_KHR',
    1000114001 : 'VK_STRUCTURE_TYPE_EXPORT_FENCE_WIN32_HANDLE_INFO_KHR',
    1000114002 : 'VK_STRUCTURE_TYPE_FENCE_GET_WIN32_HANDLE_INFO_KHR',
    1000115000 : 'VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR',
    1000115001 : 'VK_STRUCTURE_TYPE_FENCE_GET_FD_INFO_KHR',
    1000116000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_FEATURES_KHR',
    1000116001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_PROPERTIES_KHR',
    1000116002 : 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR',
    1000116003 : 'VK_STRUCTURE_TYPE_PERFORMANCE_QUERY_SUBMIT_INFO_KHR',
    1000116004 : 'VK_STRUCTURE_TYPE_ACQUIRE_PROFILING_LOCK_INFO_KHR',
    1000116005 : 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR',
    1000116006 : 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR',
    1000119000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR',
    1000119001 : 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR',
    1000119002 : 'VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR',
    1000121000 : 'VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR',
    1000121001 : 'VK_STRUCTURE_TYPE_DISPLAY_PLANE_PROPERTIES_2_KHR',
    1000121002 : 'VK_STRUCTURE_TYPE_DISPLAY_MODE_PROPERTIES_2_KHR',
    1000121003 : 'VK_STRUCTURE_TYPE_DISPLAY_PLANE_INFO_2_KHR',
    1000121004 : 'VK_STRUCTURE_TYPE_DISPLAY_PLANE_CAPABILITIES_2_KHR',
    1000122000 : 'VK_STRUCTURE_TYPE_IOS_SURFACE_CREATE_INFO_MVK',
    1000123000 : 'VK_STRUCTURE_TYPE_MACOS_SURFACE_CREATE_INFO_MVK',
    1000128000 : 'VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT',
    1000128001 : 'VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_TAG_INFO_EXT',
    1000128002 : 'VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT',
    1000128003 : 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT',
    1000128004 : 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT',
    1000129000 : 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID',
    1000129001 : 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID',
    1000129002 : 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_ANDROID',
    1000129003 : 'VK_STRUCTURE_TYPE_IMPORT_ANDROID_HARDWARE_BUFFER_INFO_ANDROID',
    1000129004 : 'VK_STRUCTURE_TYPE_MEMORY_GET_ANDROID_HARDWARE_BUFFER_INFO_ANDROID',
    1000129005 : 'VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_ANDROID',
    1000138000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_FEATURES_EXT',
    1000138001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES_EXT',
    1000138002 : 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_INLINE_UNIFORM_BLOCK_EXT',
    1000138003 : 'VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_INLINE_UNIFORM_BLOCK_CREATE_INFO_EXT',
    1000143000 : 'VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT',
    1000143001 : 'VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT',
    1000143002 : 'VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT',
    1000143003 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT',
    1000143004 : 'VK_STRUCTURE_TYPE_MULTISAMPLE_PROPERTIES_EXT',
    1000148000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_FEATURES_EXT',
    1000148001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_PROPERTIES_EXT',
    1000148002 : 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT',
    1000149000 : 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_TO_COLOR_STATE_CREATE_INFO_NV',
    1000150007 : 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_KHR',
    1000150000 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR',
    1000150002 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_DEVICE_ADDRESS_INFO_KHR',
    1000150003 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_AABBS_DATA_KHR',
    1000150004 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR',
    1000150005 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR',
    1000150006 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_KHR',
    1000150009 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_VERSION_INFO_KHR',
    1000150010 : 'VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_INFO_KHR',
    1000150011 : 'VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_TO_MEMORY_INFO_KHR',
    1000150012 : 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_ACCELERATION_STRUCTURE_INFO_KHR',
    1000150013 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR',
    1000150014 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR',
    1000150017 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_KHR',
    1000150020 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_SIZES_INFO_KHR',
    1000347000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR',
    1000347001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR',
    1000150015 : 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR',
    1000150016 : 'VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_KHR',
    1000150018 : 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR',
    1000348013 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_QUERY_FEATURES_KHR',
    1000152000 : 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_MODULATION_STATE_CREATE_INFO_NV',
    1000154000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SM_BUILTINS_FEATURES_NV',
    1000154001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SM_BUILTINS_PROPERTIES_NV',
    1000158000 : 'VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_EXT',
    1000158002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT',
    1000158003 : 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_LIST_CREATE_INFO_EXT',
    1000158004 : 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT',
    1000158005 : 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_PROPERTIES_EXT',
    1000160000 : 'VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT',
    1000160001 : 'VK_STRUCTURE_TYPE_SHADER_MODULE_VALIDATION_CACHE_CREATE_INFO_EXT',
    1000163000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR',
    1000163001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_PROPERTIES_KHR',
    1000164000 : 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV',
    1000164001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_FEATURES_NV',
    1000164002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV',
    1000164005 : 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV',
    1000165000 : 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV',
    1000165001 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV',
    1000165003 : 'VK_STRUCTURE_TYPE_GEOMETRY_NV',
    1000165004 : 'VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV',
    1000165005 : 'VK_STRUCTURE_TYPE_GEOMETRY_AABB_NV',
    1000165006 : 'VK_STRUCTURE_TYPE_BIND_ACCELERATION_STRUCTURE_MEMORY_INFO_NV',
    1000165007 : 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_NV',
    1000165008 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_INFO_NV',
    1000165009 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV',
    1000165011 : 'VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_NV',
    1000165012 : 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV',
    1000166000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_REPRESENTATIVE_FRAGMENT_TEST_FEATURES_NV',
    1000166001 : 'VK_STRUCTURE_TYPE_PIPELINE_REPRESENTATIVE_FRAGMENT_TEST_STATE_CREATE_INFO_NV',
    1000170000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_IMAGE_FORMAT_INFO_EXT',
    1000170001 : 'VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT',
    1000174000 : 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_GLOBAL_PRIORITY_CREATE_INFO_EXT',
    1000178000 : 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_HOST_POINTER_INFO_EXT',
    1000178001 : 'VK_STRUCTURE_TYPE_MEMORY_HOST_POINTER_PROPERTIES_EXT',
    1000178002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_HOST_PROPERTIES_EXT',
    1000181000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CLOCK_FEATURES_KHR',
    1000183000 : 'VK_STRUCTURE_TYPE_PIPELINE_COMPILER_CONTROL_CREATE_INFO_AMD',
    1000184000 : 'VK_STRUCTURE_TYPE_CALIBRATED_TIMESTAMP_INFO_EXT',
    1000185000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD',
    1000189000 : 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD',
    1000190000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_PROPERTIES_EXT',
    1000190001 : 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO_EXT',
    1000190002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_FEATURES_EXT',
    1000191000 : 'VK_STRUCTURE_TYPE_PRESENT_FRAME_TOKEN_GGP',
    1000192000 : 'VK_STRUCTURE_TYPE_PIPELINE_CREATION_FEEDBACK_CREATE_INFO_EXT',
    1000201000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMPUTE_SHADER_DERIVATIVES_FEATURES_NV',
    1000202000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_FEATURES_NV',
    1000202001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV',
    1000203000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_BARYCENTRIC_FEATURES_NV',
    1000204000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_IMAGE_FOOTPRINT_FEATURES_NV',
    1000205000 : 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV',
    1000205002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXCLUSIVE_SCISSOR_FEATURES_NV',
    1000206000 : 'VK_STRUCTURE_TYPE_CHECKPOINT_DATA_NV',
    1000206001 : 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_NV',
    1000209000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_FUNCTIONS_2_FEATURES_INTEL',
    1000210000 : 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL',
    1000210001 : 'VK_STRUCTURE_TYPE_INITIALIZE_PERFORMANCE_API_INFO_INTEL',
    1000210002 : 'VK_STRUCTURE_TYPE_PERFORMANCE_MARKER_INFO_INTEL',
    1000210003 : 'VK_STRUCTURE_TYPE_PERFORMANCE_STREAM_MARKER_INFO_INTEL',
    1000210004 : 'VK_STRUCTURE_TYPE_PERFORMANCE_OVERRIDE_INFO_INTEL',
    1000210005 : 'VK_STRUCTURE_TYPE_PERFORMANCE_CONFIGURATION_ACQUIRE_INFO_INTEL',
    1000212000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PCI_BUS_INFO_PROPERTIES_EXT',
    1000213000 : 'VK_STRUCTURE_TYPE_DISPLAY_NATIVE_HDR_SURFACE_CAPABILITIES_AMD',
    1000213001 : 'VK_STRUCTURE_TYPE_SWAPCHAIN_DISPLAY_NATIVE_HDR_CREATE_INFO_AMD',
    1000214000 : 'VK_STRUCTURE_TYPE_IMAGEPIPE_SURFACE_CREATE_INFO_FUCHSIA',
    1000215000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TERMINATE_INVOCATION_FEATURES_KHR',
    1000217000 : 'VK_STRUCTURE_TYPE_METAL_SURFACE_CREATE_INFO_EXT',
    1000218000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_FEATURES_EXT',
    1000218001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_PROPERTIES_EXT',
    1000218002 : 'VK_STRUCTURE_TYPE_RENDER_PASS_FRAGMENT_DENSITY_MAP_CREATE_INFO_EXT',
    1000225000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_PROPERTIES_EXT',
    1000225001 : 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_REQUIRED_SUBGROUP_SIZE_CREATE_INFO_EXT',
    1000225002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_FEATURES_EXT',
    1000226000 : 'VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR',
    1000226001 : 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_STATE_CREATE_INFO_KHR',
    1000226002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR',
    1000226003 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_FEATURES_KHR',
    1000226004 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR',
    1000227000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_2_AMD',
    1000229000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COHERENT_MEMORY_FEATURES_AMD',
    1000234000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_IMAGE_ATOMIC_INT64_FEATURES_EXT',
    1000237000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_BUDGET_PROPERTIES_EXT',
    1000238000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PRIORITY_FEATURES_EXT',
    1000238001 : 'VK_STRUCTURE_TYPE_MEMORY_PRIORITY_ALLOCATE_INFO_EXT',
    1000239000 : 'VK_STRUCTURE_TYPE_SURFACE_PROTECTED_CAPABILITIES_KHR',
    1000240000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEDICATED_ALLOCATION_IMAGE_ALIASING_FEATURES_NV',
    1000244000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES_EXT',
    1000244002 : 'VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_CREATE_INFO_EXT',
    1000245000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES_EXT',
    1000247000 : 'VK_STRUCTURE_TYPE_VALIDATION_FEATURES_EXT',
    1000249000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_FEATURES_NV',
    1000249001 : 'VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_NV',
    1000249002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_PROPERTIES_NV',
    1000250000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COVERAGE_REDUCTION_MODE_FEATURES_NV',
    1000250001 : 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV',
    1000250002 : 'VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV',
    1000251000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_INTERLOCK_FEATURES_EXT',
    1000252000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_YCBCR_IMAGE_ARRAYS_FEATURES_EXT',
    1000255000 : 'VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_INFO_EXT',
    1000255002 : 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_FULL_SCREEN_EXCLUSIVE_EXT',
    1000255001 : 'VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_WIN32_INFO_EXT',
    1000256000 : 'VK_STRUCTURE_TYPE_HEADLESS_SURFACE_CREATE_INFO_EXT',
    1000259000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES_EXT',
    1000259001 : 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO_EXT',
    1000259002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_PROPERTIES_EXT',
    1000260000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT',
    1000265000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INDEX_TYPE_UINT8_FEATURES_EXT',
    1000267000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_FEATURES_EXT',
    1000269000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_EXECUTABLE_PROPERTIES_FEATURES_KHR',
    1000269001 : 'VK_STRUCTURE_TYPE_PIPELINE_INFO_KHR',
    1000269002 : 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR',
    1000269003 : 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INFO_KHR',
    1000269004 : 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR',
    1000269005 : 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR',
    1000276000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DEMOTE_TO_HELPER_INVOCATION_FEATURES_EXT',
    1000277000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV',
    1000277001 : 'VK_STRUCTURE_TYPE_GRAPHICS_SHADER_GROUP_CREATE_INFO_NV',
    1000277002 : 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV',
    1000277003 : 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV',
    1000277004 : 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV',
    1000277005 : 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV',
    1000277006 : 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV',
    1000277007 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_FEATURES_NV',
    1000281000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_FEATURES_EXT',
    1000281001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_PROPERTIES_EXT',
    1000282000 : 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDER_PASS_TRANSFORM_INFO_QCOM',
    1000282001 : 'VK_STRUCTURE_TYPE_RENDER_PASS_TRANSFORM_BEGIN_INFO_QCOM',
    1000284000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_MEMORY_REPORT_FEATURES_EXT',
    1000284001 : 'VK_STRUCTURE_TYPE_DEVICE_DEVICE_MEMORY_REPORT_CREATE_INFO_EXT',
    1000284002 : 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT',
    1000286000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_FEATURES_EXT',
    1000286001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_PROPERTIES_EXT',
    1000287000 : 'VK_STRUCTURE_TYPE_SAMPLER_CUSTOM_BORDER_COLOR_CREATE_INFO_EXT',
    1000287001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_PROPERTIES_EXT',
    1000287002 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_FEATURES_EXT',
    1000290000 : 'VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR',
    1000295000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIVATE_DATA_FEATURES_EXT',
    1000295001 : 'VK_STRUCTURE_TYPE_DEVICE_PRIVATE_DATA_CREATE_INFO_EXT',
    1000295002 : 'VK_STRUCTURE_TYPE_PRIVATE_DATA_SLOT_CREATE_INFO_EXT',
    1000297000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_CREATION_CACHE_CONTROL_FEATURES_EXT',
    1000300000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DIAGNOSTICS_CONFIG_FEATURES_NV',
    1000300001 : 'VK_STRUCTURE_TYPE_DEVICE_DIAGNOSTICS_CONFIG_CREATE_INFO_NV',
    1000326000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_PROPERTIES_NV',
    1000326001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV',
    1000326002 : 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV',
    1000332000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_FEATURES_EXT',
    1000332001 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT',
    1000333000 : 'VK_STRUCTURE_TYPE_COPY_COMMAND_TRANSFORM_INFO_QCOM',
    1000335000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ROBUSTNESS_FEATURES_EXT',
    1000337000 : 'VK_STRUCTURE_TYPE_COPY_BUFFER_INFO_2_KHR',
    1000337001 : 'VK_STRUCTURE_TYPE_COPY_IMAGE_INFO_2_KHR',
    1000337002 : 'VK_STRUCTURE_TYPE_COPY_BUFFER_TO_IMAGE_INFO_2_KHR',
    1000337003 : 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_BUFFER_INFO_2_KHR',
    1000337004 : 'VK_STRUCTURE_TYPE_BLIT_IMAGE_INFO_2_KHR',
    1000337005 : 'VK_STRUCTURE_TYPE_RESOLVE_IMAGE_INFO_2_KHR',
    1000337006 : 'VK_STRUCTURE_TYPE_BUFFER_COPY_2_KHR',
    1000337007 : 'VK_STRUCTURE_TYPE_IMAGE_COPY_2_KHR',
    1000337008 : 'VK_STRUCTURE_TYPE_IMAGE_BLIT_2_KHR',
    1000337009 : 'VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2_KHR',
    1000337010 : 'VK_STRUCTURE_TYPE_IMAGE_RESOLVE_2_KHR',
    1000340000 : 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_4444_FORMATS_FEATURES_EXT',
    1000346000 : 'VK_STRUCTURE_TYPE_DIRECTFB_SURFACE_CREATE_INFO_EXT',
}
VK_STRUCTURE_TYPE_APPLICATION_INFO = VkStructureType(0)
VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO = VkStructureType(1)
VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO = VkStructureType(2)
VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO = VkStructureType(3)
VK_STRUCTURE_TYPE_SUBMIT_INFO = VkStructureType(4)
VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO = VkStructureType(5)
VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE = VkStructureType(6)
VK_STRUCTURE_TYPE_BIND_SPARSE_INFO = VkStructureType(7)
VK_STRUCTURE_TYPE_FENCE_CREATE_INFO = VkStructureType(8)
VK_STRUCTURE_TYPE_SEMAPHORE_CREATE_INFO = VkStructureType(9)
VK_STRUCTURE_TYPE_EVENT_CREATE_INFO = VkStructureType(10)
VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO = VkStructureType(11)
VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO = VkStructureType(12)
VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO = VkStructureType(13)
VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO = VkStructureType(14)
VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO = VkStructureType(15)
VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO = VkStructureType(16)
VK_STRUCTURE_TYPE_PIPELINE_CACHE_CREATE_INFO = VkStructureType(17)
VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO = VkStructureType(18)
VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO = VkStructureType(19)
VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO = VkStructureType(20)
VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_STATE_CREATE_INFO = VkStructureType(21)
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO = VkStructureType(22)
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO = VkStructureType(23)
VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO = VkStructureType(24)
VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO = VkStructureType(25)
VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO = VkStructureType(26)
VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO = VkStructureType(27)
VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO = VkStructureType(28)
VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO = VkStructureType(29)
VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO = VkStructureType(30)
VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO = VkStructureType(31)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO = VkStructureType(32)
VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO = VkStructureType(33)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO = VkStructureType(34)
VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET = VkStructureType(35)
VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET = VkStructureType(36)
VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO = VkStructureType(37)
VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO = VkStructureType(38)
VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO = VkStructureType(39)
VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO = VkStructureType(40)
VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO = VkStructureType(41)
VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO = VkStructureType(42)
VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO = VkStructureType(43)
VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER = VkStructureType(44)
VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER = VkStructureType(45)
VK_STRUCTURE_TYPE_MEMORY_BARRIER = VkStructureType(46)
VK_STRUCTURE_TYPE_LOADER_INSTANCE_CREATE_INFO = VkStructureType(47)
VK_STRUCTURE_TYPE_LOADER_DEVICE_CREATE_INFO = VkStructureType(48)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_PROPERTIES = VkStructureType(1000094000)
VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO = VkStructureType(1000157000)
VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO = VkStructureType(1000157001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES = VkStructureType(1000083000)
VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS = VkStructureType(1000127000)
VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO = VkStructureType(1000127001)
VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_FLAGS_INFO = VkStructureType(1000060000)
VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO = VkStructureType(1000060003)
VK_STRUCTURE_TYPE_DEVICE_GROUP_COMMAND_BUFFER_BEGIN_INFO = VkStructureType(1000060004)
VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO = VkStructureType(1000060005)
VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO = VkStructureType(1000060006)
VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO = VkStructureType(1000060013)
VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO = VkStructureType(1000060014)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES = VkStructureType(1000070000)
VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO = VkStructureType(1000070001)
VK_STRUCTURE_TYPE_BUFFER_MEMORY_REQUIREMENTS_INFO_2 = VkStructureType(1000146000)
VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2 = VkStructureType(1000146001)
VK_STRUCTURE_TYPE_IMAGE_SPARSE_MEMORY_REQUIREMENTS_INFO_2 = VkStructureType(1000146002)
VK_STRUCTURE_TYPE_MEMORY_REQUIREMENTS_2 = VkStructureType(1000146003)
VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2 = VkStructureType(1000146004)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2 = VkStructureType(1000059000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2 = VkStructureType(1000059001)
VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2 = VkStructureType(1000059002)
VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2 = VkStructureType(1000059003)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2 = VkStructureType(1000059004)
VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2 = VkStructureType(1000059005)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2 = VkStructureType(1000059006)
VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2 = VkStructureType(1000059007)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2 = VkStructureType(1000059008)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_POINT_CLIPPING_PROPERTIES = VkStructureType(1000117000)
VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO = VkStructureType(1000117001)
VK_STRUCTURE_TYPE_IMAGE_VIEW_USAGE_CREATE_INFO = VkStructureType(1000117002)
VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_DOMAIN_ORIGIN_STATE_CREATE_INFO = VkStructureType(1000117003)
VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO = VkStructureType(1000053000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_FEATURES = VkStructureType(1000053001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PROPERTIES = VkStructureType(1000053002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES = VkStructureType(1000120000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTER_FEATURES = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES
VK_STRUCTURE_TYPE_PROTECTED_SUBMIT_INFO = VkStructureType(1000145000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROTECTED_MEMORY_FEATURES = VkStructureType(1000145001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROTECTED_MEMORY_PROPERTIES = VkStructureType(1000145002)
VK_STRUCTURE_TYPE_DEVICE_QUEUE_INFO_2 = VkStructureType(1000145003)
VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO = VkStructureType(1000156000)
VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO = VkStructureType(1000156001)
VK_STRUCTURE_TYPE_BIND_IMAGE_PLANE_MEMORY_INFO = VkStructureType(1000156002)
VK_STRUCTURE_TYPE_IMAGE_PLANE_MEMORY_REQUIREMENTS_INFO = VkStructureType(1000156003)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_YCBCR_CONVERSION_FEATURES = VkStructureType(1000156004)
VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_IMAGE_FORMAT_PROPERTIES = VkStructureType(1000156005)
VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO = VkStructureType(1000085000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_IMAGE_FORMAT_INFO = VkStructureType(1000071000)
VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES = VkStructureType(1000071001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO = VkStructureType(1000071002)
VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES = VkStructureType(1000071003)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES = VkStructureType(1000071004)
VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO = VkStructureType(1000072000)
VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO = VkStructureType(1000072001)
VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO = VkStructureType(1000072002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FENCE_INFO = VkStructureType(1000112000)
VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES = VkStructureType(1000112001)
VK_STRUCTURE_TYPE_EXPORT_FENCE_CREATE_INFO = VkStructureType(1000113000)
VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_CREATE_INFO = VkStructureType(1000077000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO = VkStructureType(1000076000)
VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES = VkStructureType(1000076001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_3_PROPERTIES = VkStructureType(1000168000)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT = VkStructureType(1000168001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DRAW_PARAMETERS_FEATURES = VkStructureType(1000063000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DRAW_PARAMETER_FEATURES = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DRAW_PARAMETERS_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_FEATURES = VkStructureType(49)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES = VkStructureType(50)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_FEATURES = VkStructureType(51)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_PROPERTIES = VkStructureType(52)
VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO = VkStructureType(1000147000)
VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2 = VkStructureType(1000109000)
VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2 = VkStructureType(1000109001)
VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2 = VkStructureType(1000109002)
VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2 = VkStructureType(1000109003)
VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2 = VkStructureType(1000109004)
VK_STRUCTURE_TYPE_SUBPASS_BEGIN_INFO = VkStructureType(1000109005)
VK_STRUCTURE_TYPE_SUBPASS_END_INFO = VkStructureType(1000109006)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_8BIT_STORAGE_FEATURES = VkStructureType(1000177000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES = VkStructureType(1000196000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_INT64_FEATURES = VkStructureType(1000180000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT16_INT8_FEATURES = VkStructureType(1000082000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES = VkStructureType(1000197000)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO = VkStructureType(1000161000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES = VkStructureType(1000161001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES = VkStructureType(1000161002)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO = VkStructureType(1000161003)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT = VkStructureType(1000161004)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES = VkStructureType(1000199000)
VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE = VkStructureType(1000199001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCALAR_BLOCK_LAYOUT_FEATURES = VkStructureType(1000221000)
VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO = VkStructureType(1000246000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_FILTER_MINMAX_PROPERTIES = VkStructureType(1000130000)
VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO = VkStructureType(1000130001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES = VkStructureType(1000211000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGELESS_FRAMEBUFFER_FEATURES = VkStructureType(1000108000)
VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO = VkStructureType(1000108001)
VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO = VkStructureType(1000108002)
VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO = VkStructureType(1000108003)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_UNIFORM_BUFFER_STANDARD_LAYOUT_FEATURES = VkStructureType(1000253000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_EXTENDED_TYPES_FEATURES = VkStructureType(1000175000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SEPARATE_DEPTH_STENCIL_LAYOUTS_FEATURES = VkStructureType(1000241000)
VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT = VkStructureType(1000241001)
VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT = VkStructureType(1000241002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_QUERY_RESET_FEATURES = VkStructureType(1000261000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_FEATURES = VkStructureType(1000207000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_PROPERTIES = VkStructureType(1000207001)
VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO = VkStructureType(1000207002)
VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO = VkStructureType(1000207003)
VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO = VkStructureType(1000207004)
VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO = VkStructureType(1000207005)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES = VkStructureType(1000257000)
VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO = VkStructureType(1000244001)
VK_STRUCTURE_TYPE_BUFFER_OPAQUE_CAPTURE_ADDRESS_CREATE_INFO = VkStructureType(1000257002)
VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO = VkStructureType(1000257003)
VK_STRUCTURE_TYPE_DEVICE_MEMORY_OPAQUE_CAPTURE_ADDRESS_INFO = VkStructureType(1000257004)
VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR = VkStructureType(1000001000)
VK_STRUCTURE_TYPE_PRESENT_INFO_KHR = VkStructureType(1000001001)
VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR = VkStructureType(1000060007)
VK_STRUCTURE_TYPE_IMAGE_SWAPCHAIN_CREATE_INFO_KHR = VkStructureType(1000060008)
VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_SWAPCHAIN_INFO_KHR = VkStructureType(1000060009)
VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR = VkStructureType(1000060010)
VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_INFO_KHR = VkStructureType(1000060011)
VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR = VkStructureType(1000060012)
VK_STRUCTURE_TYPE_DISPLAY_MODE_CREATE_INFO_KHR = VkStructureType(1000002000)
VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR = VkStructureType(1000002001)
VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR = VkStructureType(1000003000)
VK_STRUCTURE_TYPE_XLIB_SURFACE_CREATE_INFO_KHR = VkStructureType(1000004000)
VK_STRUCTURE_TYPE_XCB_SURFACE_CREATE_INFO_KHR = VkStructureType(1000005000)
VK_STRUCTURE_TYPE_WAYLAND_SURFACE_CREATE_INFO_KHR = VkStructureType(1000006000)
VK_STRUCTURE_TYPE_ANDROID_SURFACE_CREATE_INFO_KHR = VkStructureType(1000008000)
VK_STRUCTURE_TYPE_WIN32_SURFACE_CREATE_INFO_KHR = VkStructureType(1000009000)
VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT = VkStructureType(1000011000)
VK_STRUCTURE_TYPE_DEBUG_REPORT_CREATE_INFO_EXT = VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_RASTERIZATION_ORDER_AMD = VkStructureType(1000018000)
VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_NAME_INFO_EXT = VkStructureType(1000022000)
VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_TAG_INFO_EXT = VkStructureType(1000022001)
VK_STRUCTURE_TYPE_DEBUG_MARKER_MARKER_INFO_EXT = VkStructureType(1000022002)
VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_IMAGE_CREATE_INFO_NV = VkStructureType(1000026000)
VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_BUFFER_CREATE_INFO_NV = VkStructureType(1000026001)
VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_MEMORY_ALLOCATE_INFO_NV = VkStructureType(1000026002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_FEATURES_EXT = VkStructureType(1000028000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT = VkStructureType(1000028001)
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_STREAM_CREATE_INFO_EXT = VkStructureType(1000028002)
VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX = VkStructureType(1000030000)
VK_STRUCTURE_TYPE_IMAGE_VIEW_ADDRESS_PROPERTIES_NVX = VkStructureType(1000030001)
VK_STRUCTURE_TYPE_TEXTURE_LOD_GATHER_FORMAT_PROPERTIES_AMD = VkStructureType(1000041000)
VK_STRUCTURE_TYPE_STREAM_DESCRIPTOR_SURFACE_CREATE_INFO_GGP = VkStructureType(1000049000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CORNER_SAMPLED_IMAGE_FEATURES_NV = VkStructureType(1000050000)
VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PROPERTIES
VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO_NV = VkStructureType(1000056000)
VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO_NV = VkStructureType(1000056001)
VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_NV = VkStructureType(1000057000)
VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_NV = VkStructureType(1000057001)
VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_NV = VkStructureType(1000058000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2
VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2_KHR = VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2
VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2_KHR = VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2
VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2_KHR = VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2
VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2_KHR = VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2
VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_FLAGS_INFO_KHR = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_FLAGS_INFO
VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO_KHR = VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO
VK_STRUCTURE_TYPE_DEVICE_GROUP_COMMAND_BUFFER_BEGIN_INFO_KHR = VK_STRUCTURE_TYPE_DEVICE_GROUP_COMMAND_BUFFER_BEGIN_INFO
VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO_KHR = VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO
VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO_KHR = VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO
VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO_KHR = VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO
VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO_KHR = VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO
VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR = VkStructureType(1000060007)
VK_STRUCTURE_TYPE_IMAGE_SWAPCHAIN_CREATE_INFO_KHR = VkStructureType(1000060008)
VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_SWAPCHAIN_INFO_KHR = VkStructureType(1000060009)
VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR = VkStructureType(1000060010)
VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_INFO_KHR = VkStructureType(1000060011)
VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR = VkStructureType(1000060012)
VK_STRUCTURE_TYPE_VALIDATION_FLAGS_EXT = VkStructureType(1000061000)
VK_STRUCTURE_TYPE_VI_SURFACE_CREATE_INFO_NN = VkStructureType(1000062000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXTURE_COMPRESSION_ASTC_HDR_FEATURES_EXT = VkStructureType(1000066000)
VK_STRUCTURE_TYPE_IMAGE_VIEW_ASTC_DECODE_MODE_EXT = VkStructureType(1000067000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ASTC_DECODE_FEATURES_EXT = VkStructureType(1000067001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES
VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_IMAGE_FORMAT_INFO_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_IMAGE_FORMAT_INFO
VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES_KHR = VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO
VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES_KHR = VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES
VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO
VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO
VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO_KHR = VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO
VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_KHR = VkStructureType(1000073000)
VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_KHR = VkStructureType(1000073001)
VK_STRUCTURE_TYPE_MEMORY_WIN32_HANDLE_PROPERTIES_KHR = VkStructureType(1000073002)
VK_STRUCTURE_TYPE_MEMORY_GET_WIN32_HANDLE_INFO_KHR = VkStructureType(1000073003)
VK_STRUCTURE_TYPE_IMPORT_MEMORY_FD_INFO_KHR = VkStructureType(1000074000)
VK_STRUCTURE_TYPE_MEMORY_FD_PROPERTIES_KHR = VkStructureType(1000074001)
VK_STRUCTURE_TYPE_MEMORY_GET_FD_INFO_KHR = VkStructureType(1000074002)
VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_KHR = VkStructureType(1000075000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO
VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES_KHR = VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES
VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_CREATE_INFO
VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR = VkStructureType(1000078000)
VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR = VkStructureType(1000078001)
VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR = VkStructureType(1000078002)
VK_STRUCTURE_TYPE_SEMAPHORE_GET_WIN32_HANDLE_INFO_KHR = VkStructureType(1000078003)
VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_FD_INFO_KHR = VkStructureType(1000079000)
VK_STRUCTURE_TYPE_SEMAPHORE_GET_FD_INFO_KHR = VkStructureType(1000079001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PUSH_DESCRIPTOR_PROPERTIES_KHR = VkStructureType(1000080000)
VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_CONDITIONAL_RENDERING_INFO_EXT = VkStructureType(1000081000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONDITIONAL_RENDERING_FEATURES_EXT = VkStructureType(1000081001)
VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT = VkStructureType(1000081002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT16_INT8_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT16_INT8_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT16_INT8_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT16_INT8_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES
VK_STRUCTURE_TYPE_PRESENT_REGIONS_KHR = VkStructureType(1000084000)
VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV = VkStructureType(1000087000)
VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT = VkStructureType(1000090000)
VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES2_EXT = VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT
VK_STRUCTURE_TYPE_DISPLAY_POWER_INFO_EXT = VkStructureType(1000091000)
VK_STRUCTURE_TYPE_DEVICE_EVENT_INFO_EXT = VkStructureType(1000091001)
VK_STRUCTURE_TYPE_DISPLAY_EVENT_INFO_EXT = VkStructureType(1000091002)
VK_STRUCTURE_TYPE_SWAPCHAIN_COUNTER_CREATE_INFO_EXT = VkStructureType(1000091003)
VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE = VkStructureType(1000092000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PER_VIEW_ATTRIBUTES_PROPERTIES_NVX = VkStructureType(1000097000)
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV = VkStructureType(1000098000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DISCARD_RECTANGLE_PROPERTIES_EXT = VkStructureType(1000099000)
VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT = VkStructureType(1000099001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT = VkStructureType(1000101000)
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_CONSERVATIVE_STATE_CREATE_INFO_EXT = VkStructureType(1000101001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_CLIP_ENABLE_FEATURES_EXT = VkStructureType(1000102000)
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_DEPTH_CLIP_STATE_CREATE_INFO_EXT = VkStructureType(1000102001)
VK_STRUCTURE_TYPE_HDR_METADATA_EXT = VkStructureType(1000105000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGELESS_FRAMEBUFFER_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGELESS_FRAMEBUFFER_FEATURES
VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO
VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO_KHR = VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO
VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO_KHR = VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO
VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2_KHR = VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2
VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2_KHR = VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2
VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2_KHR = VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2
VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2_KHR = VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2
VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2_KHR = VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2
VK_STRUCTURE_TYPE_SUBPASS_BEGIN_INFO_KHR = VK_STRUCTURE_TYPE_SUBPASS_BEGIN_INFO
VK_STRUCTURE_TYPE_SUBPASS_END_INFO_KHR = VK_STRUCTURE_TYPE_SUBPASS_END_INFO
VK_STRUCTURE_TYPE_SHARED_PRESENT_SURFACE_CAPABILITIES_KHR = VkStructureType(1000111000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FENCE_INFO_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FENCE_INFO
VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES_KHR = VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES
VK_STRUCTURE_TYPE_EXPORT_FENCE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_EXPORT_FENCE_CREATE_INFO
VK_STRUCTURE_TYPE_IMPORT_FENCE_WIN32_HANDLE_INFO_KHR = VkStructureType(1000114000)
VK_STRUCTURE_TYPE_EXPORT_FENCE_WIN32_HANDLE_INFO_KHR = VkStructureType(1000114001)
VK_STRUCTURE_TYPE_FENCE_GET_WIN32_HANDLE_INFO_KHR = VkStructureType(1000114002)
VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR = VkStructureType(1000115000)
VK_STRUCTURE_TYPE_FENCE_GET_FD_INFO_KHR = VkStructureType(1000115001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_FEATURES_KHR = VkStructureType(1000116000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_PROPERTIES_KHR = VkStructureType(1000116001)
VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR = VkStructureType(1000116002)
VK_STRUCTURE_TYPE_PERFORMANCE_QUERY_SUBMIT_INFO_KHR = VkStructureType(1000116003)
VK_STRUCTURE_TYPE_ACQUIRE_PROFILING_LOCK_INFO_KHR = VkStructureType(1000116004)
VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR = VkStructureType(1000116005)
VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR = VkStructureType(1000116006)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_POINT_CLIPPING_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_POINT_CLIPPING_PROPERTIES
VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO
VK_STRUCTURE_TYPE_IMAGE_VIEW_USAGE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_IMAGE_VIEW_USAGE_CREATE_INFO
VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_DOMAIN_ORIGIN_STATE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_DOMAIN_ORIGIN_STATE_CREATE_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR = VkStructureType(1000119000)
VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR = VkStructureType(1000119001)
VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR = VkStructureType(1000119002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTER_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES_KHR
VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR = VkStructureType(1000121000)
VK_STRUCTURE_TYPE_DISPLAY_PLANE_PROPERTIES_2_KHR = VkStructureType(1000121001)
VK_STRUCTURE_TYPE_DISPLAY_MODE_PROPERTIES_2_KHR = VkStructureType(1000121002)
VK_STRUCTURE_TYPE_DISPLAY_PLANE_INFO_2_KHR = VkStructureType(1000121003)
VK_STRUCTURE_TYPE_DISPLAY_PLANE_CAPABILITIES_2_KHR = VkStructureType(1000121004)
VK_STRUCTURE_TYPE_IOS_SURFACE_CREATE_INFO_MVK = VkStructureType(1000122000)
VK_STRUCTURE_TYPE_MACOS_SURFACE_CREATE_INFO_MVK = VkStructureType(1000123000)
VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS_KHR = VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS
VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO_KHR = VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO
VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT = VkStructureType(1000128000)
VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_TAG_INFO_EXT = VkStructureType(1000128001)
VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT = VkStructureType(1000128002)
VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT = VkStructureType(1000128003)
VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT = VkStructureType(1000128004)
VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID = VkStructureType(1000129000)
VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID = VkStructureType(1000129001)
VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_ANDROID = VkStructureType(1000129002)
VK_STRUCTURE_TYPE_IMPORT_ANDROID_HARDWARE_BUFFER_INFO_ANDROID = VkStructureType(1000129003)
VK_STRUCTURE_TYPE_MEMORY_GET_ANDROID_HARDWARE_BUFFER_INFO_ANDROID = VkStructureType(1000129004)
VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_ANDROID = VkStructureType(1000129005)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_FILTER_MINMAX_PROPERTIES_EXT = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_FILTER_MINMAX_PROPERTIES
VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO_EXT = VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_FEATURES_EXT = VkStructureType(1000138000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES_EXT = VkStructureType(1000138001)
VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_INLINE_UNIFORM_BLOCK_EXT = VkStructureType(1000138002)
VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_INLINE_UNIFORM_BLOCK_CREATE_INFO_EXT = VkStructureType(1000138003)
VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT = VkStructureType(1000143000)
VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT = VkStructureType(1000143001)
VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT = VkStructureType(1000143002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT = VkStructureType(1000143003)
VK_STRUCTURE_TYPE_MULTISAMPLE_PROPERTIES_EXT = VkStructureType(1000143004)
VK_STRUCTURE_TYPE_BUFFER_MEMORY_REQUIREMENTS_INFO_2_KHR = VK_STRUCTURE_TYPE_BUFFER_MEMORY_REQUIREMENTS_INFO_2
VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2_KHR = VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2
VK_STRUCTURE_TYPE_IMAGE_SPARSE_MEMORY_REQUIREMENTS_INFO_2_KHR = VK_STRUCTURE_TYPE_IMAGE_SPARSE_MEMORY_REQUIREMENTS_INFO_2
VK_STRUCTURE_TYPE_MEMORY_REQUIREMENTS_2_KHR = VK_STRUCTURE_TYPE_MEMORY_REQUIREMENTS_2
VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2_KHR = VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2
VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_FEATURES_EXT = VkStructureType(1000148000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_PROPERTIES_EXT = VkStructureType(1000148001)
VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT = VkStructureType(1000148002)
VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_TO_COLOR_STATE_CREATE_INFO_NV = VkStructureType(1000149000)
VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_KHR = VkStructureType(1000150007)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR = VkStructureType(1000150000)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_DEVICE_ADDRESS_INFO_KHR = VkStructureType(1000150002)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_AABBS_DATA_KHR = VkStructureType(1000150003)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR = VkStructureType(1000150004)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR = VkStructureType(1000150005)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_KHR = VkStructureType(1000150006)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_VERSION_INFO_KHR = VkStructureType(1000150009)
VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_INFO_KHR = VkStructureType(1000150010)
VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_TO_MEMORY_INFO_KHR = VkStructureType(1000150011)
VK_STRUCTURE_TYPE_COPY_MEMORY_TO_ACCELERATION_STRUCTURE_INFO_KHR = VkStructureType(1000150012)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR = VkStructureType(1000150013)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR = VkStructureType(1000150014)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_KHR = VkStructureType(1000150017)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_SIZES_INFO_KHR = VkStructureType(1000150020)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR = VkStructureType(1000347000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR = VkStructureType(1000347001)
VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR = VkStructureType(1000150015)
VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_KHR = VkStructureType(1000150016)
VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR = VkStructureType(1000150018)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_QUERY_FEATURES_KHR = VkStructureType(1000348013)
VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_MODULATION_STATE_CREATE_INFO_NV = VkStructureType(1000152000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SM_BUILTINS_FEATURES_NV = VkStructureType(1000154000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SM_BUILTINS_PROPERTIES_NV = VkStructureType(1000154001)
VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO
VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO_KHR = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO
VK_STRUCTURE_TYPE_BIND_IMAGE_PLANE_MEMORY_INFO_KHR = VK_STRUCTURE_TYPE_BIND_IMAGE_PLANE_MEMORY_INFO
VK_STRUCTURE_TYPE_IMAGE_PLANE_MEMORY_REQUIREMENTS_INFO_KHR = VK_STRUCTURE_TYPE_IMAGE_PLANE_MEMORY_REQUIREMENTS_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_YCBCR_CONVERSION_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_YCBCR_CONVERSION_FEATURES
VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_IMAGE_FORMAT_PROPERTIES_KHR = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_IMAGE_FORMAT_PROPERTIES
VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO_KHR = VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO
VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO_KHR = VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO
VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_EXT = VkStructureType(1000158000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT = VkStructureType(1000158002)
VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_LIST_CREATE_INFO_EXT = VkStructureType(1000158003)
VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT = VkStructureType(1000158004)
VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_PROPERTIES_EXT = VkStructureType(1000158005)
VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT = VkStructureType(1000160000)
VK_STRUCTURE_TYPE_SHADER_MODULE_VALIDATION_CACHE_CREATE_INFO_EXT = VkStructureType(1000160001)
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO_EXT = VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES_EXT = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES_EXT = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO_EXT = VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT_EXT = VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR = VkStructureType(1000163000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_PROPERTIES_KHR = VkStructureType(1000163001)
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV = VkStructureType(1000164000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_FEATURES_NV = VkStructureType(1000164001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV = VkStructureType(1000164002)
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV = VkStructureType(1000164005)
VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV = VkStructureType(1000165000)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV = VkStructureType(1000165001)
VK_STRUCTURE_TYPE_GEOMETRY_NV = VkStructureType(1000165003)
VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV = VkStructureType(1000165004)
VK_STRUCTURE_TYPE_GEOMETRY_AABB_NV = VkStructureType(1000165005)
VK_STRUCTURE_TYPE_BIND_ACCELERATION_STRUCTURE_MEMORY_INFO_NV = VkStructureType(1000165006)
VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_NV = VkStructureType(1000165007)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_INFO_NV = VkStructureType(1000165008)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV = VkStructureType(1000165009)
VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_NV = VkStructureType(1000165011)
VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV = VkStructureType(1000165012)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_REPRESENTATIVE_FRAGMENT_TEST_FEATURES_NV = VkStructureType(1000166000)
VK_STRUCTURE_TYPE_PIPELINE_REPRESENTATIVE_FRAGMENT_TEST_STATE_CREATE_INFO_NV = VkStructureType(1000166001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_3_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_3_PROPERTIES
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT_KHR = VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_IMAGE_FORMAT_INFO_EXT = VkStructureType(1000170000)
VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT = VkStructureType(1000170001)
VK_STRUCTURE_TYPE_DEVICE_QUEUE_GLOBAL_PRIORITY_CREATE_INFO_EXT = VkStructureType(1000174000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_EXTENDED_TYPES_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_EXTENDED_TYPES_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_8BIT_STORAGE_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_8BIT_STORAGE_FEATURES
VK_STRUCTURE_TYPE_IMPORT_MEMORY_HOST_POINTER_INFO_EXT = VkStructureType(1000178000)
VK_STRUCTURE_TYPE_MEMORY_HOST_POINTER_PROPERTIES_EXT = VkStructureType(1000178001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_HOST_PROPERTIES_EXT = VkStructureType(1000178002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_INT64_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_INT64_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CLOCK_FEATURES_KHR = VkStructureType(1000181000)
VK_STRUCTURE_TYPE_PIPELINE_COMPILER_CONTROL_CREATE_INFO_AMD = VkStructureType(1000183000)
VK_STRUCTURE_TYPE_CALIBRATED_TIMESTAMP_INFO_EXT = VkStructureType(1000184000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD = VkStructureType(1000185000)
VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD = VkStructureType(1000189000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_PROPERTIES_EXT = VkStructureType(1000190000)
VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO_EXT = VkStructureType(1000190001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_FEATURES_EXT = VkStructureType(1000190002)
VK_STRUCTURE_TYPE_PRESENT_FRAME_TOKEN_GGP = VkStructureType(1000191000)
VK_STRUCTURE_TYPE_PIPELINE_CREATION_FEEDBACK_CREATE_INFO_EXT = VkStructureType(1000192000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES
VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE_KHR = VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMPUTE_SHADER_DERIVATIVES_FEATURES_NV = VkStructureType(1000201000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_FEATURES_NV = VkStructureType(1000202000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV = VkStructureType(1000202001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_BARYCENTRIC_FEATURES_NV = VkStructureType(1000203000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_IMAGE_FOOTPRINT_FEATURES_NV = VkStructureType(1000204000)
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV = VkStructureType(1000205000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXCLUSIVE_SCISSOR_FEATURES_NV = VkStructureType(1000205002)
VK_STRUCTURE_TYPE_CHECKPOINT_DATA_NV = VkStructureType(1000206000)
VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_NV = VkStructureType(1000206001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_PROPERTIES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_PROPERTIES
VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO
VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO_KHR = VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO
VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO_KHR = VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO
VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO_KHR = VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_FUNCTIONS_2_FEATURES_INTEL = VkStructureType(1000209000)
VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL = VkStructureType(1000210000)
VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO_INTEL = VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL
VK_STRUCTURE_TYPE_INITIALIZE_PERFORMANCE_API_INFO_INTEL = VkStructureType(1000210001)
VK_STRUCTURE_TYPE_PERFORMANCE_MARKER_INFO_INTEL = VkStructureType(1000210002)
VK_STRUCTURE_TYPE_PERFORMANCE_STREAM_MARKER_INFO_INTEL = VkStructureType(1000210003)
VK_STRUCTURE_TYPE_PERFORMANCE_OVERRIDE_INFO_INTEL = VkStructureType(1000210004)
VK_STRUCTURE_TYPE_PERFORMANCE_CONFIGURATION_ACQUIRE_INFO_INTEL = VkStructureType(1000210005)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PCI_BUS_INFO_PROPERTIES_EXT = VkStructureType(1000212000)
VK_STRUCTURE_TYPE_DISPLAY_NATIVE_HDR_SURFACE_CAPABILITIES_AMD = VkStructureType(1000213000)
VK_STRUCTURE_TYPE_SWAPCHAIN_DISPLAY_NATIVE_HDR_CREATE_INFO_AMD = VkStructureType(1000213001)
VK_STRUCTURE_TYPE_IMAGEPIPE_SURFACE_CREATE_INFO_FUCHSIA = VkStructureType(1000214000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TERMINATE_INVOCATION_FEATURES_KHR = VkStructureType(1000215000)
VK_STRUCTURE_TYPE_METAL_SURFACE_CREATE_INFO_EXT = VkStructureType(1000217000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_FEATURES_EXT = VkStructureType(1000218000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_PROPERTIES_EXT = VkStructureType(1000218001)
VK_STRUCTURE_TYPE_RENDER_PASS_FRAGMENT_DENSITY_MAP_CREATE_INFO_EXT = VkStructureType(1000218002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCALAR_BLOCK_LAYOUT_FEATURES_EXT = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCALAR_BLOCK_LAYOUT_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_PROPERTIES_EXT = VkStructureType(1000225000)
VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_REQUIRED_SUBGROUP_SIZE_CREATE_INFO_EXT = VkStructureType(1000225001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_FEATURES_EXT = VkStructureType(1000225002)
VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR = VkStructureType(1000226000)
VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_STATE_CREATE_INFO_KHR = VkStructureType(1000226001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR = VkStructureType(1000226002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_FEATURES_KHR = VkStructureType(1000226003)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR = VkStructureType(1000226004)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_2_AMD = VkStructureType(1000227000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COHERENT_MEMORY_FEATURES_AMD = VkStructureType(1000229000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_IMAGE_ATOMIC_INT64_FEATURES_EXT = VkStructureType(1000234000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_BUDGET_PROPERTIES_EXT = VkStructureType(1000237000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PRIORITY_FEATURES_EXT = VkStructureType(1000238000)
VK_STRUCTURE_TYPE_MEMORY_PRIORITY_ALLOCATE_INFO_EXT = VkStructureType(1000238001)
VK_STRUCTURE_TYPE_SURFACE_PROTECTED_CAPABILITIES_KHR = VkStructureType(1000239000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEDICATED_ALLOCATION_IMAGE_ALIASING_FEATURES_NV = VkStructureType(1000240000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SEPARATE_DEPTH_STENCIL_LAYOUTS_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SEPARATE_DEPTH_STENCIL_LAYOUTS_FEATURES
VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT_KHR = VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT
VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT_KHR = VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES_EXT = VkStructureType(1000244000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_ADDRESS_FEATURES_EXT = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES_EXT
VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO_EXT = VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO
VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_CREATE_INFO_EXT = VkStructureType(1000244002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES_EXT = VkStructureType(1000245000)
VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO_EXT = VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO
VK_STRUCTURE_TYPE_VALIDATION_FEATURES_EXT = VkStructureType(1000247000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_FEATURES_NV = VkStructureType(1000249000)
VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_NV = VkStructureType(1000249001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_PROPERTIES_NV = VkStructureType(1000249002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COVERAGE_REDUCTION_MODE_FEATURES_NV = VkStructureType(1000250000)
VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV = VkStructureType(1000250001)
VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV = VkStructureType(1000250002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_INTERLOCK_FEATURES_EXT = VkStructureType(1000251000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_YCBCR_IMAGE_ARRAYS_FEATURES_EXT = VkStructureType(1000252000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_UNIFORM_BUFFER_STANDARD_LAYOUT_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_UNIFORM_BUFFER_STANDARD_LAYOUT_FEATURES
VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_INFO_EXT = VkStructureType(1000255000)
VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_FULL_SCREEN_EXCLUSIVE_EXT = VkStructureType(1000255002)
VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_WIN32_INFO_EXT = VkStructureType(1000255001)
VK_STRUCTURE_TYPE_HEADLESS_SURFACE_CREATE_INFO_EXT = VkStructureType(1000256000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES_KHR = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES
VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO_KHR = VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO
VK_STRUCTURE_TYPE_BUFFER_OPAQUE_CAPTURE_ADDRESS_CREATE_INFO_KHR = VK_STRUCTURE_TYPE_BUFFER_OPAQUE_CAPTURE_ADDRESS_CREATE_INFO
VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO_KHR = VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO
VK_STRUCTURE_TYPE_DEVICE_MEMORY_OPAQUE_CAPTURE_ADDRESS_INFO_KHR = VK_STRUCTURE_TYPE_DEVICE_MEMORY_OPAQUE_CAPTURE_ADDRESS_INFO
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES_EXT = VkStructureType(1000259000)
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO_EXT = VkStructureType(1000259001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_PROPERTIES_EXT = VkStructureType(1000259002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT = VkStructureType(1000260000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_QUERY_RESET_FEATURES_EXT = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_QUERY_RESET_FEATURES
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INDEX_TYPE_UINT8_FEATURES_EXT = VkStructureType(1000265000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_FEATURES_EXT = VkStructureType(1000267000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_EXECUTABLE_PROPERTIES_FEATURES_KHR = VkStructureType(1000269000)
VK_STRUCTURE_TYPE_PIPELINE_INFO_KHR = VkStructureType(1000269001)
VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR = VkStructureType(1000269002)
VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INFO_KHR = VkStructureType(1000269003)
VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR = VkStructureType(1000269004)
VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR = VkStructureType(1000269005)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DEMOTE_TO_HELPER_INVOCATION_FEATURES_EXT = VkStructureType(1000276000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV = VkStructureType(1000277000)
VK_STRUCTURE_TYPE_GRAPHICS_SHADER_GROUP_CREATE_INFO_NV = VkStructureType(1000277001)
VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV = VkStructureType(1000277002)
VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV = VkStructureType(1000277003)
VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV = VkStructureType(1000277004)
VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV = VkStructureType(1000277005)
VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV = VkStructureType(1000277006)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_FEATURES_NV = VkStructureType(1000277007)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_FEATURES_EXT = VkStructureType(1000281000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_PROPERTIES_EXT = VkStructureType(1000281001)
VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDER_PASS_TRANSFORM_INFO_QCOM = VkStructureType(1000282000)
VK_STRUCTURE_TYPE_RENDER_PASS_TRANSFORM_BEGIN_INFO_QCOM = VkStructureType(1000282001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_MEMORY_REPORT_FEATURES_EXT = VkStructureType(1000284000)
VK_STRUCTURE_TYPE_DEVICE_DEVICE_MEMORY_REPORT_CREATE_INFO_EXT = VkStructureType(1000284001)
VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT = VkStructureType(1000284002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_FEATURES_EXT = VkStructureType(1000286000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_PROPERTIES_EXT = VkStructureType(1000286001)
VK_STRUCTURE_TYPE_SAMPLER_CUSTOM_BORDER_COLOR_CREATE_INFO_EXT = VkStructureType(1000287000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_PROPERTIES_EXT = VkStructureType(1000287001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_FEATURES_EXT = VkStructureType(1000287002)
VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR = VkStructureType(1000290000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIVATE_DATA_FEATURES_EXT = VkStructureType(1000295000)
VK_STRUCTURE_TYPE_DEVICE_PRIVATE_DATA_CREATE_INFO_EXT = VkStructureType(1000295001)
VK_STRUCTURE_TYPE_PRIVATE_DATA_SLOT_CREATE_INFO_EXT = VkStructureType(1000295002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_CREATION_CACHE_CONTROL_FEATURES_EXT = VkStructureType(1000297000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DIAGNOSTICS_CONFIG_FEATURES_NV = VkStructureType(1000300000)
VK_STRUCTURE_TYPE_DEVICE_DIAGNOSTICS_CONFIG_CREATE_INFO_NV = VkStructureType(1000300001)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_PROPERTIES_NV = VkStructureType(1000326000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV = VkStructureType(1000326001)
VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV = VkStructureType(1000326002)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_FEATURES_EXT = VkStructureType(1000332000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT = VkStructureType(1000332001)
VK_STRUCTURE_TYPE_COPY_COMMAND_TRANSFORM_INFO_QCOM = VkStructureType(1000333000)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ROBUSTNESS_FEATURES_EXT = VkStructureType(1000335000)
VK_STRUCTURE_TYPE_COPY_BUFFER_INFO_2_KHR = VkStructureType(1000337000)
VK_STRUCTURE_TYPE_COPY_IMAGE_INFO_2_KHR = VkStructureType(1000337001)
VK_STRUCTURE_TYPE_COPY_BUFFER_TO_IMAGE_INFO_2_KHR = VkStructureType(1000337002)
VK_STRUCTURE_TYPE_COPY_IMAGE_TO_BUFFER_INFO_2_KHR = VkStructureType(1000337003)
VK_STRUCTURE_TYPE_BLIT_IMAGE_INFO_2_KHR = VkStructureType(1000337004)
VK_STRUCTURE_TYPE_RESOLVE_IMAGE_INFO_2_KHR = VkStructureType(1000337005)
VK_STRUCTURE_TYPE_BUFFER_COPY_2_KHR = VkStructureType(1000337006)
VK_STRUCTURE_TYPE_IMAGE_COPY_2_KHR = VkStructureType(1000337007)
VK_STRUCTURE_TYPE_IMAGE_BLIT_2_KHR = VkStructureType(1000337008)
VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2_KHR = VkStructureType(1000337009)
VK_STRUCTURE_TYPE_IMAGE_RESOLVE_2_KHR = VkStructureType(1000337010)
VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_4444_FORMATS_FEATURES_EXT = VkStructureType(1000340000)
VK_STRUCTURE_TYPE_DIRECTFB_SURFACE_CREATE_INFO_EXT = VkStructureType(1000346000)

VkSystemAllocationScope = type('VkSystemAllocationScope', (c_enum,), dict(names=dict()))
VkSystemAllocationScope.names = {
    0 : 'VK_SYSTEM_ALLOCATION_SCOPE_COMMAND',
    1 : 'VK_SYSTEM_ALLOCATION_SCOPE_OBJECT',
    2 : 'VK_SYSTEM_ALLOCATION_SCOPE_CACHE',
    3 : 'VK_SYSTEM_ALLOCATION_SCOPE_DEVICE',
    4 : 'VK_SYSTEM_ALLOCATION_SCOPE_INSTANCE',
}
VK_SYSTEM_ALLOCATION_SCOPE_COMMAND = VkSystemAllocationScope(0)
VK_SYSTEM_ALLOCATION_SCOPE_OBJECT = VkSystemAllocationScope(1)
VK_SYSTEM_ALLOCATION_SCOPE_CACHE = VkSystemAllocationScope(2)
VK_SYSTEM_ALLOCATION_SCOPE_DEVICE = VkSystemAllocationScope(3)
VK_SYSTEM_ALLOCATION_SCOPE_INSTANCE = VkSystemAllocationScope(4)

VkInternalAllocationType = type('VkInternalAllocationType', (c_enum,), dict(names=dict()))
VkInternalAllocationType.names = {
    0 : 'VK_INTERNAL_ALLOCATION_TYPE_EXECUTABLE',
}
VK_INTERNAL_ALLOCATION_TYPE_EXECUTABLE = VkInternalAllocationType(0)

VkSamplerAddressMode = type('VkSamplerAddressMode', (c_enum,), dict(names=dict()))
VkSamplerAddressMode.names = {
    0 : 'VK_SAMPLER_ADDRESS_MODE_REPEAT',
    1 : 'VK_SAMPLER_ADDRESS_MODE_MIRRORED_REPEAT',
    2 : 'VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE',
    3 : 'VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_BORDER',
    4 : 'VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE',
    4 : 'VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE',
}
VK_SAMPLER_ADDRESS_MODE_REPEAT = VkSamplerAddressMode(0)
VK_SAMPLER_ADDRESS_MODE_MIRRORED_REPEAT = VkSamplerAddressMode(1)
VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE = VkSamplerAddressMode(2)
VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_BORDER = VkSamplerAddressMode(3)
VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE = VkSamplerAddressMode(4)
VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE = VkSamplerAddressMode(4)
VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE_KHR = VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE

VkFilter = type('VkFilter', (c_enum,), dict(names=dict()))
VkFilter.names = {
    0 : 'VK_FILTER_NEAREST',
    1 : 'VK_FILTER_LINEAR',
    1000015000 : 'VK_FILTER_CUBIC_IMG',
}
VK_FILTER_NEAREST = VkFilter(0)
VK_FILTER_LINEAR = VkFilter(1)
VK_FILTER_CUBIC_IMG = VkFilter(1000015000)
VK_FILTER_CUBIC_EXT = VK_FILTER_CUBIC_IMG

VkSamplerMipmapMode = type('VkSamplerMipmapMode', (c_enum,), dict(names=dict()))
VkSamplerMipmapMode.names = {
    0 : 'VK_SAMPLER_MIPMAP_MODE_NEAREST',
    1 : 'VK_SAMPLER_MIPMAP_MODE_LINEAR',
}
VK_SAMPLER_MIPMAP_MODE_NEAREST = VkSamplerMipmapMode(0)
VK_SAMPLER_MIPMAP_MODE_LINEAR = VkSamplerMipmapMode(1)

VkVertexInputRate = type('VkVertexInputRate', (c_enum,), dict(names=dict()))
VkVertexInputRate.names = {
    0 : 'VK_VERTEX_INPUT_RATE_VERTEX',
    1 : 'VK_VERTEX_INPUT_RATE_INSTANCE',
}
VK_VERTEX_INPUT_RATE_VERTEX = VkVertexInputRate(0)
VK_VERTEX_INPUT_RATE_INSTANCE = VkVertexInputRate(1)

VkPipelineStageFlagBits = type('VkPipelineStageFlagBits', (c_enum,), dict(names=dict()))
VkPipelineStageFlagBits.names = {
    1 : 'VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT',
    2 : 'VK_PIPELINE_STAGE_DRAW_INDIRECT_BIT',
    4 : 'VK_PIPELINE_STAGE_VERTEX_INPUT_BIT',
    8 : 'VK_PIPELINE_STAGE_VERTEX_SHADER_BIT',
    16 : 'VK_PIPELINE_STAGE_TESSELLATION_CONTROL_SHADER_BIT',
    32 : 'VK_PIPELINE_STAGE_TESSELLATION_EVALUATION_SHADER_BIT',
    64 : 'VK_PIPELINE_STAGE_GEOMETRY_SHADER_BIT',
    128 : 'VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT',
    256 : 'VK_PIPELINE_STAGE_EARLY_FRAGMENT_TESTS_BIT',
    512 : 'VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT',
    1024 : 'VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT',
    2048 : 'VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT',
    4096 : 'VK_PIPELINE_STAGE_TRANSFER_BIT',
    8192 : 'VK_PIPELINE_STAGE_BOTTOM_OF_PIPE_BIT',
    16384 : 'VK_PIPELINE_STAGE_HOST_BIT',
    32768 : 'VK_PIPELINE_STAGE_ALL_GRAPHICS_BIT',
    65536 : 'VK_PIPELINE_STAGE_ALL_COMMANDS_BIT',
    16777216 : 'VK_PIPELINE_STAGE_TRANSFORM_FEEDBACK_BIT_EXT',
    262144 : 'VK_PIPELINE_STAGE_CONDITIONAL_RENDERING_BIT_EXT',
    33554432 : 'VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_KHR',
    2097152 : 'VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_KHR',
    4194304 : 'VK_PIPELINE_STAGE_SHADING_RATE_IMAGE_BIT_NV',
    524288 : 'VK_PIPELINE_STAGE_TASK_SHADER_BIT_NV',
    1048576 : 'VK_PIPELINE_STAGE_MESH_SHADER_BIT_NV',
    8388608 : 'VK_PIPELINE_STAGE_FRAGMENT_DENSITY_PROCESS_BIT_EXT',
    131072 : 'VK_PIPELINE_STAGE_COMMAND_PREPROCESS_BIT_NV',
}
VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT = VkPipelineStageFlagBits(1)
VK_PIPELINE_STAGE_DRAW_INDIRECT_BIT = VkPipelineStageFlagBits(2)
VK_PIPELINE_STAGE_VERTEX_INPUT_BIT = VkPipelineStageFlagBits(4)
VK_PIPELINE_STAGE_VERTEX_SHADER_BIT = VkPipelineStageFlagBits(8)
VK_PIPELINE_STAGE_TESSELLATION_CONTROL_SHADER_BIT = VkPipelineStageFlagBits(16)
VK_PIPELINE_STAGE_TESSELLATION_EVALUATION_SHADER_BIT = VkPipelineStageFlagBits(32)
VK_PIPELINE_STAGE_GEOMETRY_SHADER_BIT = VkPipelineStageFlagBits(64)
VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT = VkPipelineStageFlagBits(128)
VK_PIPELINE_STAGE_EARLY_FRAGMENT_TESTS_BIT = VkPipelineStageFlagBits(256)
VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT = VkPipelineStageFlagBits(512)
VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT = VkPipelineStageFlagBits(1024)
VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT = VkPipelineStageFlagBits(2048)
VK_PIPELINE_STAGE_TRANSFER_BIT = VkPipelineStageFlagBits(4096)
VK_PIPELINE_STAGE_BOTTOM_OF_PIPE_BIT = VkPipelineStageFlagBits(8192)
VK_PIPELINE_STAGE_HOST_BIT = VkPipelineStageFlagBits(16384)
VK_PIPELINE_STAGE_ALL_GRAPHICS_BIT = VkPipelineStageFlagBits(32768)
VK_PIPELINE_STAGE_ALL_COMMANDS_BIT = VkPipelineStageFlagBits(65536)
VK_PIPELINE_STAGE_TRANSFORM_FEEDBACK_BIT_EXT = VkPipelineStageFlagBits(16777216)
VK_PIPELINE_STAGE_CONDITIONAL_RENDERING_BIT_EXT = VkPipelineStageFlagBits(262144)
VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_KHR = VkPipelineStageFlagBits(33554432)
VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_KHR = VkPipelineStageFlagBits(2097152)
VK_PIPELINE_STAGE_SHADING_RATE_IMAGE_BIT_NV = VkPipelineStageFlagBits(4194304)
VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_NV = VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_KHR
VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_NV = VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_KHR
VK_PIPELINE_STAGE_TASK_SHADER_BIT_NV = VkPipelineStageFlagBits(524288)
VK_PIPELINE_STAGE_MESH_SHADER_BIT_NV = VkPipelineStageFlagBits(1048576)
VK_PIPELINE_STAGE_FRAGMENT_DENSITY_PROCESS_BIT_EXT = VkPipelineStageFlagBits(8388608)
VK_PIPELINE_STAGE_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR = VK_PIPELINE_STAGE_SHADING_RATE_IMAGE_BIT_NV
VK_PIPELINE_STAGE_COMMAND_PREPROCESS_BIT_NV = VkPipelineStageFlagBits(131072)

VkSparseImageFormatFlagBits = type('VkSparseImageFormatFlagBits', (c_enum,), dict(names=dict()))
VkSparseImageFormatFlagBits.names = {
    1 : 'VK_SPARSE_IMAGE_FORMAT_SINGLE_MIPTAIL_BIT',
    2 : 'VK_SPARSE_IMAGE_FORMAT_ALIGNED_MIP_SIZE_BIT',
    4 : 'VK_SPARSE_IMAGE_FORMAT_NONSTANDARD_BLOCK_SIZE_BIT',
}
VK_SPARSE_IMAGE_FORMAT_SINGLE_MIPTAIL_BIT = VkSparseImageFormatFlagBits(1)
VK_SPARSE_IMAGE_FORMAT_ALIGNED_MIP_SIZE_BIT = VkSparseImageFormatFlagBits(2)
VK_SPARSE_IMAGE_FORMAT_NONSTANDARD_BLOCK_SIZE_BIT = VkSparseImageFormatFlagBits(4)

VkSampleCountFlagBits = type('VkSampleCountFlagBits', (c_enum,), dict(names=dict()))
VkSampleCountFlagBits.names = {
    1 : 'VK_SAMPLE_COUNT_1_BIT',
    2 : 'VK_SAMPLE_COUNT_2_BIT',
    4 : 'VK_SAMPLE_COUNT_4_BIT',
    8 : 'VK_SAMPLE_COUNT_8_BIT',
    16 : 'VK_SAMPLE_COUNT_16_BIT',
    32 : 'VK_SAMPLE_COUNT_32_BIT',
    64 : 'VK_SAMPLE_COUNT_64_BIT',
}
VK_SAMPLE_COUNT_1_BIT = VkSampleCountFlagBits(1)
VK_SAMPLE_COUNT_2_BIT = VkSampleCountFlagBits(2)
VK_SAMPLE_COUNT_4_BIT = VkSampleCountFlagBits(4)
VK_SAMPLE_COUNT_8_BIT = VkSampleCountFlagBits(8)
VK_SAMPLE_COUNT_16_BIT = VkSampleCountFlagBits(16)
VK_SAMPLE_COUNT_32_BIT = VkSampleCountFlagBits(32)
VK_SAMPLE_COUNT_64_BIT = VkSampleCountFlagBits(64)

VkAttachmentDescriptionFlagBits = type('VkAttachmentDescriptionFlagBits', (c_enum,), dict(names=dict()))
VkAttachmentDescriptionFlagBits.names = {
    1 : 'VK_ATTACHMENT_DESCRIPTION_MAY_ALIAS_BIT',
}
VK_ATTACHMENT_DESCRIPTION_MAY_ALIAS_BIT = VkAttachmentDescriptionFlagBits(1)

VkDescriptorPoolCreateFlagBits = type('VkDescriptorPoolCreateFlagBits', (c_enum,), dict(names=dict()))
VkDescriptorPoolCreateFlagBits.names = {
    1 : 'VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT',
    2 : 'VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT',
}
VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT = VkDescriptorPoolCreateFlagBits(1)
VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT = VkDescriptorPoolCreateFlagBits(2)
VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT_EXT = VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT

VkDependencyFlagBits = type('VkDependencyFlagBits', (c_enum,), dict(names=dict()))
VkDependencyFlagBits.names = {
    1 : 'VK_DEPENDENCY_BY_REGION_BIT',
    4 : 'VK_DEPENDENCY_DEVICE_GROUP_BIT',
    2 : 'VK_DEPENDENCY_VIEW_LOCAL_BIT',
}
VK_DEPENDENCY_BY_REGION_BIT = VkDependencyFlagBits(1)
VK_DEPENDENCY_DEVICE_GROUP_BIT = VkDependencyFlagBits(4)
VK_DEPENDENCY_VIEW_LOCAL_BIT = VkDependencyFlagBits(2)
VK_DEPENDENCY_VIEW_LOCAL_BIT_KHR = VK_DEPENDENCY_VIEW_LOCAL_BIT
VK_DEPENDENCY_DEVICE_GROUP_BIT_KHR = VK_DEPENDENCY_DEVICE_GROUP_BIT

VkObjectType = type('VkObjectType', (c_enum,), dict(names=dict()))
VkObjectType.names = {
    0 : 'VK_OBJECT_TYPE_UNKNOWN',
    1 : 'VK_OBJECT_TYPE_INSTANCE',
    2 : 'VK_OBJECT_TYPE_PHYSICAL_DEVICE',
    3 : 'VK_OBJECT_TYPE_DEVICE',
    4 : 'VK_OBJECT_TYPE_QUEUE',
    5 : 'VK_OBJECT_TYPE_SEMAPHORE',
    6 : 'VK_OBJECT_TYPE_COMMAND_BUFFER',
    7 : 'VK_OBJECT_TYPE_FENCE',
    8 : 'VK_OBJECT_TYPE_DEVICE_MEMORY',
    9 : 'VK_OBJECT_TYPE_BUFFER',
    10 : 'VK_OBJECT_TYPE_IMAGE',
    11 : 'VK_OBJECT_TYPE_EVENT',
    12 : 'VK_OBJECT_TYPE_QUERY_POOL',
    13 : 'VK_OBJECT_TYPE_BUFFER_VIEW',
    14 : 'VK_OBJECT_TYPE_IMAGE_VIEW',
    15 : 'VK_OBJECT_TYPE_SHADER_MODULE',
    16 : 'VK_OBJECT_TYPE_PIPELINE_CACHE',
    17 : 'VK_OBJECT_TYPE_PIPELINE_LAYOUT',
    18 : 'VK_OBJECT_TYPE_RENDER_PASS',
    19 : 'VK_OBJECT_TYPE_PIPELINE',
    20 : 'VK_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT',
    21 : 'VK_OBJECT_TYPE_SAMPLER',
    22 : 'VK_OBJECT_TYPE_DESCRIPTOR_POOL',
    23 : 'VK_OBJECT_TYPE_DESCRIPTOR_SET',
    24 : 'VK_OBJECT_TYPE_FRAMEBUFFER',
    25 : 'VK_OBJECT_TYPE_COMMAND_POOL',
    1000156000 : 'VK_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION',
    1000085000 : 'VK_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE',
    1000000000 : 'VK_OBJECT_TYPE_SURFACE_KHR',
    1000001000 : 'VK_OBJECT_TYPE_SWAPCHAIN_KHR',
    1000002000 : 'VK_OBJECT_TYPE_DISPLAY_KHR',
    1000002001 : 'VK_OBJECT_TYPE_DISPLAY_MODE_KHR',
    1000011000 : 'VK_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT',
    1000128000 : 'VK_OBJECT_TYPE_DEBUG_UTILS_MESSENGER_EXT',
    1000150000 : 'VK_OBJECT_TYPE_ACCELERATION_STRUCTURE_KHR',
    1000160000 : 'VK_OBJECT_TYPE_VALIDATION_CACHE_EXT',
    1000165000 : 'VK_OBJECT_TYPE_ACCELERATION_STRUCTURE_NV',
    1000210000 : 'VK_OBJECT_TYPE_PERFORMANCE_CONFIGURATION_INTEL',
    1000268000 : 'VK_OBJECT_TYPE_DEFERRED_OPERATION_KHR',
    1000277000 : 'VK_OBJECT_TYPE_INDIRECT_COMMANDS_LAYOUT_NV',
    1000295000 : 'VK_OBJECT_TYPE_PRIVATE_DATA_SLOT_EXT',
}
VK_OBJECT_TYPE_UNKNOWN = VkObjectType(0)
VK_OBJECT_TYPE_INSTANCE = VkObjectType(1)
VK_OBJECT_TYPE_PHYSICAL_DEVICE = VkObjectType(2)
VK_OBJECT_TYPE_DEVICE = VkObjectType(3)
VK_OBJECT_TYPE_QUEUE = VkObjectType(4)
VK_OBJECT_TYPE_SEMAPHORE = VkObjectType(5)
VK_OBJECT_TYPE_COMMAND_BUFFER = VkObjectType(6)
VK_OBJECT_TYPE_FENCE = VkObjectType(7)
VK_OBJECT_TYPE_DEVICE_MEMORY = VkObjectType(8)
VK_OBJECT_TYPE_BUFFER = VkObjectType(9)
VK_OBJECT_TYPE_IMAGE = VkObjectType(10)
VK_OBJECT_TYPE_EVENT = VkObjectType(11)
VK_OBJECT_TYPE_QUERY_POOL = VkObjectType(12)
VK_OBJECT_TYPE_BUFFER_VIEW = VkObjectType(13)
VK_OBJECT_TYPE_IMAGE_VIEW = VkObjectType(14)
VK_OBJECT_TYPE_SHADER_MODULE = VkObjectType(15)
VK_OBJECT_TYPE_PIPELINE_CACHE = VkObjectType(16)
VK_OBJECT_TYPE_PIPELINE_LAYOUT = VkObjectType(17)
VK_OBJECT_TYPE_RENDER_PASS = VkObjectType(18)
VK_OBJECT_TYPE_PIPELINE = VkObjectType(19)
VK_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT = VkObjectType(20)
VK_OBJECT_TYPE_SAMPLER = VkObjectType(21)
VK_OBJECT_TYPE_DESCRIPTOR_POOL = VkObjectType(22)
VK_OBJECT_TYPE_DESCRIPTOR_SET = VkObjectType(23)
VK_OBJECT_TYPE_FRAMEBUFFER = VkObjectType(24)
VK_OBJECT_TYPE_COMMAND_POOL = VkObjectType(25)
VK_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION = VkObjectType(1000156000)
VK_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE = VkObjectType(1000085000)
VK_OBJECT_TYPE_SURFACE_KHR = VkObjectType(1000000000)
VK_OBJECT_TYPE_SWAPCHAIN_KHR = VkObjectType(1000001000)
VK_OBJECT_TYPE_DISPLAY_KHR = VkObjectType(1000002000)
VK_OBJECT_TYPE_DISPLAY_MODE_KHR = VkObjectType(1000002001)
VK_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT = VkObjectType(1000011000)
VK_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_KHR = VK_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE
VK_OBJECT_TYPE_DEBUG_UTILS_MESSENGER_EXT = VkObjectType(1000128000)
VK_OBJECT_TYPE_ACCELERATION_STRUCTURE_KHR = VkObjectType(1000150000)
VK_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_KHR = VK_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION
VK_OBJECT_TYPE_VALIDATION_CACHE_EXT = VkObjectType(1000160000)
VK_OBJECT_TYPE_ACCELERATION_STRUCTURE_NV = VkObjectType(1000165000)
VK_OBJECT_TYPE_PERFORMANCE_CONFIGURATION_INTEL = VkObjectType(1000210000)
VK_OBJECT_TYPE_DEFERRED_OPERATION_KHR = VkObjectType(1000268000)
VK_OBJECT_TYPE_INDIRECT_COMMANDS_LAYOUT_NV = VkObjectType(1000277000)
VK_OBJECT_TYPE_PRIVATE_DATA_SLOT_EXT = VkObjectType(1000295000)

VkIndirectCommandsLayoutUsageFlagBitsNV = type('VkIndirectCommandsLayoutUsageFlagBitsNV', (c_enum,), dict(names=dict()))
VkIndirectCommandsLayoutUsageFlagBitsNV.names = {
    1 : 'VK_INDIRECT_COMMANDS_LAYOUT_USAGE_EXPLICIT_PREPROCESS_BIT_NV',
    2 : 'VK_INDIRECT_COMMANDS_LAYOUT_USAGE_INDEXED_SEQUENCES_BIT_NV',
    4 : 'VK_INDIRECT_COMMANDS_LAYOUT_USAGE_UNORDERED_SEQUENCES_BIT_NV',
}
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_EXPLICIT_PREPROCESS_BIT_NV = VkIndirectCommandsLayoutUsageFlagBitsNV(1)
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_INDEXED_SEQUENCES_BIT_NV = VkIndirectCommandsLayoutUsageFlagBitsNV(2)
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_UNORDERED_SEQUENCES_BIT_NV = VkIndirectCommandsLayoutUsageFlagBitsNV(4)

VkIndirectCommandsTokenTypeNV = type('VkIndirectCommandsTokenTypeNV', (c_enum,), dict(names=dict()))
VkIndirectCommandsTokenTypeNV.names = {
    0 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_SHADER_GROUP_NV',
    1 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_STATE_FLAGS_NV',
    2 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_INDEX_BUFFER_NV',
    3 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_VERTEX_BUFFER_NV',
    4 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_PUSH_CONSTANT_NV',
    5 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_INDEXED_NV',
    6 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_NV',
    7 : 'VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_TASKS_NV',
}
VK_INDIRECT_COMMANDS_TOKEN_TYPE_SHADER_GROUP_NV = VkIndirectCommandsTokenTypeNV(0)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_STATE_FLAGS_NV = VkIndirectCommandsTokenTypeNV(1)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_INDEX_BUFFER_NV = VkIndirectCommandsTokenTypeNV(2)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_VERTEX_BUFFER_NV = VkIndirectCommandsTokenTypeNV(3)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_PUSH_CONSTANT_NV = VkIndirectCommandsTokenTypeNV(4)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_INDEXED_NV = VkIndirectCommandsTokenTypeNV(5)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_NV = VkIndirectCommandsTokenTypeNV(6)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_TASKS_NV = VkIndirectCommandsTokenTypeNV(7)

VkIndirectStateFlagBitsNV = type('VkIndirectStateFlagBitsNV', (c_enum,), dict(names=dict()))
VkIndirectStateFlagBitsNV.names = {
    1 : 'VK_INDIRECT_STATE_FLAG_FRONTFACE_BIT_NV',
}
VK_INDIRECT_STATE_FLAG_FRONTFACE_BIT_NV = VkIndirectStateFlagBitsNV(1)

VkPrivateDataSlotCreateFlagBitsEXT = type('VkPrivateDataSlotCreateFlagBitsEXT', (c_enum,), dict(names=dict()))
VkPrivateDataSlotCreateFlagBitsEXT.names = {
}

VkDescriptorUpdateTemplateType = type('VkDescriptorUpdateTemplateType', (c_enum,), dict(names=dict()))
VkDescriptorUpdateTemplateType.names = {
    0 : 'VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET',
    1 : 'VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR',
    1 : 'VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR',
    1 : 'VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR',
}
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET = VkDescriptorUpdateTemplateType(0)
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR = VkDescriptorUpdateTemplateType(1)
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR = VkDescriptorUpdateTemplateType(1)
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET_KHR = VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR = VkDescriptorUpdateTemplateType(1)

VkDescriptorUpdateTemplateTypeKHR = VkDescriptorUpdateTemplateType

VkViewportCoordinateSwizzleNV = type('VkViewportCoordinateSwizzleNV', (c_enum,), dict(names=dict()))
VkViewportCoordinateSwizzleNV.names = {
    0 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_X_NV',
    1 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_X_NV',
    2 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Y_NV',
    3 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Y_NV',
    4 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Z_NV',
    5 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Z_NV',
    6 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_W_NV',
    7 : 'VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_W_NV',
}
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_X_NV = VkViewportCoordinateSwizzleNV(0)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_X_NV = VkViewportCoordinateSwizzleNV(1)
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Y_NV = VkViewportCoordinateSwizzleNV(2)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Y_NV = VkViewportCoordinateSwizzleNV(3)
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Z_NV = VkViewportCoordinateSwizzleNV(4)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Z_NV = VkViewportCoordinateSwizzleNV(5)
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_W_NV = VkViewportCoordinateSwizzleNV(6)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_W_NV = VkViewportCoordinateSwizzleNV(7)

VkDiscardRectangleModeEXT = type('VkDiscardRectangleModeEXT', (c_enum,), dict(names=dict()))
VkDiscardRectangleModeEXT.names = {
    0 : 'VK_DISCARD_RECTANGLE_MODE_INCLUSIVE_EXT',
    1 : 'VK_DISCARD_RECTANGLE_MODE_EXCLUSIVE_EXT',
}
VK_DISCARD_RECTANGLE_MODE_INCLUSIVE_EXT = VkDiscardRectangleModeEXT(0)
VK_DISCARD_RECTANGLE_MODE_EXCLUSIVE_EXT = VkDiscardRectangleModeEXT(1)

VkSubpassDescriptionFlagBits = type('VkSubpassDescriptionFlagBits', (c_enum,), dict(names=dict()))
VkSubpassDescriptionFlagBits.names = {
    1 : 'VK_SUBPASS_DESCRIPTION_PER_VIEW_ATTRIBUTES_BIT_NVX',
    2 : 'VK_SUBPASS_DESCRIPTION_PER_VIEW_POSITION_X_ONLY_BIT_NVX',
    4 : 'VK_SUBPASS_DESCRIPTION_FRAGMENT_REGION_BIT_QCOM',
    8 : 'VK_SUBPASS_DESCRIPTION_SHADER_RESOLVE_BIT_QCOM',
}
VK_SUBPASS_DESCRIPTION_PER_VIEW_ATTRIBUTES_BIT_NVX = VkSubpassDescriptionFlagBits(1)
VK_SUBPASS_DESCRIPTION_PER_VIEW_POSITION_X_ONLY_BIT_NVX = VkSubpassDescriptionFlagBits(2)
VK_SUBPASS_DESCRIPTION_FRAGMENT_REGION_BIT_QCOM = VkSubpassDescriptionFlagBits(4)
VK_SUBPASS_DESCRIPTION_SHADER_RESOLVE_BIT_QCOM = VkSubpassDescriptionFlagBits(8)

VkPointClippingBehavior = type('VkPointClippingBehavior', (c_enum,), dict(names=dict()))
VkPointClippingBehavior.names = {
    0 : 'VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES',
    1 : 'VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY',
}
VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES = VkPointClippingBehavior(0)
VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY = VkPointClippingBehavior(1)
VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES_KHR = VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES
VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY_KHR = VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY

VkPointClippingBehaviorKHR = VkPointClippingBehavior

VkCoverageModulationModeNV = type('VkCoverageModulationModeNV', (c_enum,), dict(names=dict()))
VkCoverageModulationModeNV.names = {
    0 : 'VK_COVERAGE_MODULATION_MODE_NONE_NV',
    1 : 'VK_COVERAGE_MODULATION_MODE_RGB_NV',
    2 : 'VK_COVERAGE_MODULATION_MODE_ALPHA_NV',
    3 : 'VK_COVERAGE_MODULATION_MODE_RGBA_NV',
}
VK_COVERAGE_MODULATION_MODE_NONE_NV = VkCoverageModulationModeNV(0)
VK_COVERAGE_MODULATION_MODE_RGB_NV = VkCoverageModulationModeNV(1)
VK_COVERAGE_MODULATION_MODE_ALPHA_NV = VkCoverageModulationModeNV(2)
VK_COVERAGE_MODULATION_MODE_RGBA_NV = VkCoverageModulationModeNV(3)

VkCoverageReductionModeNV = type('VkCoverageReductionModeNV', (c_enum,), dict(names=dict()))
VkCoverageReductionModeNV.names = {
    0 : 'VK_COVERAGE_REDUCTION_MODE_MERGE_NV',
    1 : 'VK_COVERAGE_REDUCTION_MODE_TRUNCATE_NV',
}
VK_COVERAGE_REDUCTION_MODE_MERGE_NV = VkCoverageReductionModeNV(0)
VK_COVERAGE_REDUCTION_MODE_TRUNCATE_NV = VkCoverageReductionModeNV(1)

VkValidationCacheHeaderVersionEXT = type('VkValidationCacheHeaderVersionEXT', (c_enum,), dict(names=dict()))
VkValidationCacheHeaderVersionEXT.names = {
    1 : 'VK_VALIDATION_CACHE_HEADER_VERSION_ONE_EXT',
}
VK_VALIDATION_CACHE_HEADER_VERSION_ONE_EXT = VkValidationCacheHeaderVersionEXT(1)

VkShaderInfoTypeAMD = type('VkShaderInfoTypeAMD', (c_enum,), dict(names=dict()))
VkShaderInfoTypeAMD.names = {
    0 : 'VK_SHADER_INFO_TYPE_STATISTICS_AMD',
    1 : 'VK_SHADER_INFO_TYPE_BINARY_AMD',
    2 : 'VK_SHADER_INFO_TYPE_DISASSEMBLY_AMD',
}
VK_SHADER_INFO_TYPE_STATISTICS_AMD = VkShaderInfoTypeAMD(0)
VK_SHADER_INFO_TYPE_BINARY_AMD = VkShaderInfoTypeAMD(1)
VK_SHADER_INFO_TYPE_DISASSEMBLY_AMD = VkShaderInfoTypeAMD(2)

VkQueueGlobalPriorityEXT = type('VkQueueGlobalPriorityEXT', (c_enum,), dict(names=dict()))
VkQueueGlobalPriorityEXT.names = {
    128 : 'VK_QUEUE_GLOBAL_PRIORITY_LOW_EXT',
    256 : 'VK_QUEUE_GLOBAL_PRIORITY_MEDIUM_EXT',
    512 : 'VK_QUEUE_GLOBAL_PRIORITY_HIGH_EXT',
    1024 : 'VK_QUEUE_GLOBAL_PRIORITY_REALTIME_EXT',
}
VK_QUEUE_GLOBAL_PRIORITY_LOW_EXT = VkQueueGlobalPriorityEXT(128)
VK_QUEUE_GLOBAL_PRIORITY_MEDIUM_EXT = VkQueueGlobalPriorityEXT(256)
VK_QUEUE_GLOBAL_PRIORITY_HIGH_EXT = VkQueueGlobalPriorityEXT(512)
VK_QUEUE_GLOBAL_PRIORITY_REALTIME_EXT = VkQueueGlobalPriorityEXT(1024)

VkTimeDomainEXT = type('VkTimeDomainEXT', (c_enum,), dict(names=dict()))
VkTimeDomainEXT.names = {
    0 : 'VK_TIME_DOMAIN_DEVICE_EXT',
    1 : 'VK_TIME_DOMAIN_CLOCK_MONOTONIC_EXT',
    2 : 'VK_TIME_DOMAIN_CLOCK_MONOTONIC_RAW_EXT',
    3 : 'VK_TIME_DOMAIN_QUERY_PERFORMANCE_COUNTER_EXT',
}
VK_TIME_DOMAIN_DEVICE_EXT = VkTimeDomainEXT(0)
VK_TIME_DOMAIN_CLOCK_MONOTONIC_EXT = VkTimeDomainEXT(1)
VK_TIME_DOMAIN_CLOCK_MONOTONIC_RAW_EXT = VkTimeDomainEXT(2)
VK_TIME_DOMAIN_QUERY_PERFORMANCE_COUNTER_EXT = VkTimeDomainEXT(3)

VkConservativeRasterizationModeEXT = type('VkConservativeRasterizationModeEXT', (c_enum,), dict(names=dict()))
VkConservativeRasterizationModeEXT.names = {
    0 : 'VK_CONSERVATIVE_RASTERIZATION_MODE_DISABLED_EXT',
    1 : 'VK_CONSERVATIVE_RASTERIZATION_MODE_OVERESTIMATE_EXT',
    2 : 'VK_CONSERVATIVE_RASTERIZATION_MODE_UNDERESTIMATE_EXT',
}
VK_CONSERVATIVE_RASTERIZATION_MODE_DISABLED_EXT = VkConservativeRasterizationModeEXT(0)
VK_CONSERVATIVE_RASTERIZATION_MODE_OVERESTIMATE_EXT = VkConservativeRasterizationModeEXT(1)
VK_CONSERVATIVE_RASTERIZATION_MODE_UNDERESTIMATE_EXT = VkConservativeRasterizationModeEXT(2)

VkResolveModeFlagBits = type('VkResolveModeFlagBits', (c_enum,), dict(names=dict()))
VkResolveModeFlagBits.names = {
    0 : 'VK_RESOLVE_MODE_NONE',
    1 : 'VK_RESOLVE_MODE_SAMPLE_ZERO_BIT',
    2 : 'VK_RESOLVE_MODE_AVERAGE_BIT',
    4 : 'VK_RESOLVE_MODE_MIN_BIT',
    8 : 'VK_RESOLVE_MODE_MAX_BIT',
}
VK_RESOLVE_MODE_NONE = VkResolveModeFlagBits(0)
VK_RESOLVE_MODE_SAMPLE_ZERO_BIT = VkResolveModeFlagBits(1)
VK_RESOLVE_MODE_AVERAGE_BIT = VkResolveModeFlagBits(2)
VK_RESOLVE_MODE_MIN_BIT = VkResolveModeFlagBits(4)
VK_RESOLVE_MODE_MAX_BIT = VkResolveModeFlagBits(8)
VK_RESOLVE_MODE_NONE_KHR = VK_RESOLVE_MODE_NONE
VK_RESOLVE_MODE_SAMPLE_ZERO_BIT_KHR = VK_RESOLVE_MODE_SAMPLE_ZERO_BIT
VK_RESOLVE_MODE_AVERAGE_BIT_KHR = VK_RESOLVE_MODE_AVERAGE_BIT
VK_RESOLVE_MODE_MIN_BIT_KHR = VK_RESOLVE_MODE_MIN_BIT
VK_RESOLVE_MODE_MAX_BIT_KHR = VK_RESOLVE_MODE_MAX_BIT

VkResolveModeFlagBitsKHR = VkResolveModeFlagBits

VkDescriptorBindingFlagBits = type('VkDescriptorBindingFlagBits', (c_enum,), dict(names=dict()))
VkDescriptorBindingFlagBits.names = {
    1 : 'VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT',
    2 : 'VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT',
    4 : 'VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT',
    8 : 'VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT',
}
VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT = VkDescriptorBindingFlagBits(1)
VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT = VkDescriptorBindingFlagBits(2)
VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT = VkDescriptorBindingFlagBits(4)
VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT = VkDescriptorBindingFlagBits(8)
VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT_EXT = VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT
VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT_EXT = VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT
VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT_EXT = VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT
VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT_EXT = VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT

VkDescriptorBindingFlagBitsEXT = VkDescriptorBindingFlagBits

VkConditionalRenderingFlagBitsEXT = type('VkConditionalRenderingFlagBitsEXT', (c_enum,), dict(names=dict()))
VkConditionalRenderingFlagBitsEXT.names = {
    1 : 'VK_CONDITIONAL_RENDERING_INVERTED_BIT_EXT',
}
VK_CONDITIONAL_RENDERING_INVERTED_BIT_EXT = VkConditionalRenderingFlagBitsEXT(1)

VkSemaphoreType = type('VkSemaphoreType', (c_enum,), dict(names=dict()))
VkSemaphoreType.names = {
    0 : 'VK_SEMAPHORE_TYPE_BINARY',
    1 : 'VK_SEMAPHORE_TYPE_TIMELINE',
}
VK_SEMAPHORE_TYPE_BINARY = VkSemaphoreType(0)
VK_SEMAPHORE_TYPE_TIMELINE = VkSemaphoreType(1)
VK_SEMAPHORE_TYPE_BINARY_KHR = VK_SEMAPHORE_TYPE_BINARY
VK_SEMAPHORE_TYPE_TIMELINE_KHR = VK_SEMAPHORE_TYPE_TIMELINE

VkSemaphoreTypeKHR = VkSemaphoreType

VkGeometryFlagBitsKHR = type('VkGeometryFlagBitsKHR', (c_enum,), dict(names=dict()))
VkGeometryFlagBitsKHR.names = {
    1 : 'VK_GEOMETRY_OPAQUE_BIT_KHR',
    2 : 'VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR',
}
VK_GEOMETRY_OPAQUE_BIT_KHR = VkGeometryFlagBitsKHR(1)
VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR = VkGeometryFlagBitsKHR(2)
VK_GEOMETRY_OPAQUE_BIT_NV = VK_GEOMETRY_OPAQUE_BIT_KHR
VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_NV = VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR

VkGeometryFlagBitsNV = VkGeometryFlagBitsKHR

VkGeometryInstanceFlagBitsKHR = type('VkGeometryInstanceFlagBitsKHR', (c_enum,), dict(names=dict()))
VkGeometryInstanceFlagBitsKHR.names = {
    1 : 'VK_GEOMETRY_INSTANCE_TRIANGLE_FACING_CULL_DISABLE_BIT_KHR',
    2 : 'VK_GEOMETRY_INSTANCE_TRIANGLE_FRONT_COUNTERCLOCKWISE_BIT_KHR',
    4 : 'VK_GEOMETRY_INSTANCE_FORCE_OPAQUE_BIT_KHR',
    8 : 'VK_GEOMETRY_INSTANCE_FORCE_NO_OPAQUE_BIT_KHR',
}
VK_GEOMETRY_INSTANCE_TRIANGLE_FACING_CULL_DISABLE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(1)
VK_GEOMETRY_INSTANCE_TRIANGLE_FRONT_COUNTERCLOCKWISE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(2)
VK_GEOMETRY_INSTANCE_FORCE_OPAQUE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(4)
VK_GEOMETRY_INSTANCE_FORCE_NO_OPAQUE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(8)
VK_GEOMETRY_INSTANCE_TRIANGLE_CULL_DISABLE_BIT_NV = VK_GEOMETRY_INSTANCE_TRIANGLE_FACING_CULL_DISABLE_BIT_KHR
VK_GEOMETRY_INSTANCE_TRIANGLE_FRONT_COUNTERCLOCKWISE_BIT_NV = VK_GEOMETRY_INSTANCE_TRIANGLE_FRONT_COUNTERCLOCKWISE_BIT_KHR
VK_GEOMETRY_INSTANCE_FORCE_OPAQUE_BIT_NV = VK_GEOMETRY_INSTANCE_FORCE_OPAQUE_BIT_KHR
VK_GEOMETRY_INSTANCE_FORCE_NO_OPAQUE_BIT_NV = VK_GEOMETRY_INSTANCE_FORCE_NO_OPAQUE_BIT_KHR

VkGeometryInstanceFlagBitsNV = VkGeometryInstanceFlagBitsKHR

VkBuildAccelerationStructureFlagBitsKHR = type('VkBuildAccelerationStructureFlagBitsKHR', (c_enum,), dict(names=dict()))
VkBuildAccelerationStructureFlagBitsKHR.names = {
    1 : 'VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT_KHR',
    2 : 'VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT_KHR',
    4 : 'VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT_KHR',
    8 : 'VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT_KHR',
    16 : 'VK_BUILD_ACCELERATION_STRUCTURE_LOW_MEMORY_BIT_KHR',
}
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(1)
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(2)
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(4)
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(8)
VK_BUILD_ACCELERATION_STRUCTURE_LOW_MEMORY_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(16)
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT_NV = VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT_KHR
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT_NV = VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT_KHR
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT_NV = VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT_KHR
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT_NV = VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT_KHR
VK_BUILD_ACCELERATION_STRUCTURE_LOW_MEMORY_BIT_NV = VK_BUILD_ACCELERATION_STRUCTURE_LOW_MEMORY_BIT_KHR

VkBuildAccelerationStructureFlagBitsNV = VkBuildAccelerationStructureFlagBitsKHR

VkAccelerationStructureCreateFlagBitsKHR = type('VkAccelerationStructureCreateFlagBitsKHR', (c_enum,), dict(names=dict()))
VkAccelerationStructureCreateFlagBitsKHR.names = {
    1 : 'VK_ACCELERATION_STRUCTURE_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR',
}
VK_ACCELERATION_STRUCTURE_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = VkAccelerationStructureCreateFlagBitsKHR(1)

VkBuildAccelerationStructureModeKHR = type('VkBuildAccelerationStructureModeKHR', (c_enum,), dict(names=dict()))
VkBuildAccelerationStructureModeKHR.names = {
    0 : 'VK_BUILD_ACCELERATION_STRUCTURE_MODE_BUILD_KHR',
    1 : 'VK_BUILD_ACCELERATION_STRUCTURE_MODE_UPDATE_KHR',
}
VK_BUILD_ACCELERATION_STRUCTURE_MODE_BUILD_KHR = VkBuildAccelerationStructureModeKHR(0)
VK_BUILD_ACCELERATION_STRUCTURE_MODE_UPDATE_KHR = VkBuildAccelerationStructureModeKHR(1)

VkCopyAccelerationStructureModeKHR = type('VkCopyAccelerationStructureModeKHR', (c_enum,), dict(names=dict()))
VkCopyAccelerationStructureModeKHR.names = {
    0 : 'VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_KHR',
    1 : 'VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_KHR',
    2 : 'VK_COPY_ACCELERATION_STRUCTURE_MODE_SERIALIZE_KHR',
    3 : 'VK_COPY_ACCELERATION_STRUCTURE_MODE_DESERIALIZE_KHR',
}
VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_KHR = VkCopyAccelerationStructureModeKHR(0)
VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_KHR = VkCopyAccelerationStructureModeKHR(1)
VK_COPY_ACCELERATION_STRUCTURE_MODE_SERIALIZE_KHR = VkCopyAccelerationStructureModeKHR(2)
VK_COPY_ACCELERATION_STRUCTURE_MODE_DESERIALIZE_KHR = VkCopyAccelerationStructureModeKHR(3)
VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_NV = VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_KHR
VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_NV = VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_KHR

VkCopyAccelerationStructureModeNV = VkCopyAccelerationStructureModeKHR

VkAccelerationStructureTypeKHR = type('VkAccelerationStructureTypeKHR', (c_enum,), dict(names=dict()))
VkAccelerationStructureTypeKHR.names = {
    0 : 'VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR',
    1 : 'VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR',
    2 : 'VK_ACCELERATION_STRUCTURE_TYPE_GENERIC_KHR',
}
VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR = VkAccelerationStructureTypeKHR(0)
VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR = VkAccelerationStructureTypeKHR(1)
VK_ACCELERATION_STRUCTURE_TYPE_GENERIC_KHR = VkAccelerationStructureTypeKHR(2)
VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_NV = VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR
VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_NV = VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR

VkAccelerationStructureTypeNV = VkAccelerationStructureTypeKHR

VkGeometryTypeKHR = type('VkGeometryTypeKHR', (c_enum,), dict(names=dict()))
VkGeometryTypeKHR.names = {
    0 : 'VK_GEOMETRY_TYPE_TRIANGLES_KHR',
    1 : 'VK_GEOMETRY_TYPE_AABBS_KHR',
    2 : 'VK_GEOMETRY_TYPE_INSTANCES_KHR',
}
VK_GEOMETRY_TYPE_TRIANGLES_KHR = VkGeometryTypeKHR(0)
VK_GEOMETRY_TYPE_AABBS_KHR = VkGeometryTypeKHR(1)
VK_GEOMETRY_TYPE_INSTANCES_KHR = VkGeometryTypeKHR(2)
VK_GEOMETRY_TYPE_TRIANGLES_NV = VK_GEOMETRY_TYPE_TRIANGLES_KHR
VK_GEOMETRY_TYPE_AABBS_NV = VK_GEOMETRY_TYPE_AABBS_KHR

VkGeometryTypeNV = VkGeometryTypeKHR

VkRayTracingShaderGroupTypeKHR = type('VkRayTracingShaderGroupTypeKHR', (c_enum,), dict(names=dict()))
VkRayTracingShaderGroupTypeKHR.names = {
    0 : 'VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_KHR',
    1 : 'VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_KHR',
    2 : 'VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_KHR',
}
VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_KHR = VkRayTracingShaderGroupTypeKHR(0)
VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_KHR = VkRayTracingShaderGroupTypeKHR(1)
VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_KHR = VkRayTracingShaderGroupTypeKHR(2)
VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_NV = VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_KHR
VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_NV = VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_KHR
VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_NV = VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_KHR

VkRayTracingShaderGroupTypeNV = VkRayTracingShaderGroupTypeKHR

VkAccelerationStructureMemoryRequirementsTypeNV = type('VkAccelerationStructureMemoryRequirementsTypeNV', (c_enum,), dict(names=dict()))
VkAccelerationStructureMemoryRequirementsTypeNV.names = {
    0 : 'VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_OBJECT_NV',
    1 : 'VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_BUILD_SCRATCH_NV',
    2 : 'VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_UPDATE_SCRATCH_NV',
}
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_OBJECT_NV = VkAccelerationStructureMemoryRequirementsTypeNV(0)
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_BUILD_SCRATCH_NV = VkAccelerationStructureMemoryRequirementsTypeNV(1)
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_UPDATE_SCRATCH_NV = VkAccelerationStructureMemoryRequirementsTypeNV(2)

VkAccelerationStructureBuildTypeKHR = type('VkAccelerationStructureBuildTypeKHR', (c_enum,), dict(names=dict()))
VkAccelerationStructureBuildTypeKHR.names = {
    0 : 'VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_KHR',
    1 : 'VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR',
    2 : 'VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_OR_DEVICE_KHR',
}
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_KHR = VkAccelerationStructureBuildTypeKHR(0)
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR = VkAccelerationStructureBuildTypeKHR(1)
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_OR_DEVICE_KHR = VkAccelerationStructureBuildTypeKHR(2)

VkAccelerationStructureCompatibilityKHR = type('VkAccelerationStructureCompatibilityKHR', (c_enum,), dict(names=dict()))
VkAccelerationStructureCompatibilityKHR.names = {
    0 : 'VK_ACCELERATION_STRUCTURE_COMPATIBILITY_COMPATIBLE_KHR',
    1 : 'VK_ACCELERATION_STRUCTURE_COMPATIBILITY_INCOMPATIBLE_KHR',
}
VK_ACCELERATION_STRUCTURE_COMPATIBILITY_COMPATIBLE_KHR = VkAccelerationStructureCompatibilityKHR(0)
VK_ACCELERATION_STRUCTURE_COMPATIBILITY_INCOMPATIBLE_KHR = VkAccelerationStructureCompatibilityKHR(1)

VkShaderGroupShaderKHR = type('VkShaderGroupShaderKHR', (c_enum,), dict(names=dict()))
VkShaderGroupShaderKHR.names = {
    0 : 'VK_SHADER_GROUP_SHADER_GENERAL_KHR',
    1 : 'VK_SHADER_GROUP_SHADER_CLOSEST_HIT_KHR',
    2 : 'VK_SHADER_GROUP_SHADER_ANY_HIT_KHR',
    3 : 'VK_SHADER_GROUP_SHADER_INTERSECTION_KHR',
}
VK_SHADER_GROUP_SHADER_GENERAL_KHR = VkShaderGroupShaderKHR(0)
VK_SHADER_GROUP_SHADER_CLOSEST_HIT_KHR = VkShaderGroupShaderKHR(1)
VK_SHADER_GROUP_SHADER_ANY_HIT_KHR = VkShaderGroupShaderKHR(2)
VK_SHADER_GROUP_SHADER_INTERSECTION_KHR = VkShaderGroupShaderKHR(3)

VkMemoryOverallocationBehaviorAMD = type('VkMemoryOverallocationBehaviorAMD', (c_enum,), dict(names=dict()))
VkMemoryOverallocationBehaviorAMD.names = {
    0 : 'VK_MEMORY_OVERALLOCATION_BEHAVIOR_DEFAULT_AMD',
    1 : 'VK_MEMORY_OVERALLOCATION_BEHAVIOR_ALLOWED_AMD',
    2 : 'VK_MEMORY_OVERALLOCATION_BEHAVIOR_DISALLOWED_AMD',
}
VK_MEMORY_OVERALLOCATION_BEHAVIOR_DEFAULT_AMD = VkMemoryOverallocationBehaviorAMD(0)
VK_MEMORY_OVERALLOCATION_BEHAVIOR_ALLOWED_AMD = VkMemoryOverallocationBehaviorAMD(1)
VK_MEMORY_OVERALLOCATION_BEHAVIOR_DISALLOWED_AMD = VkMemoryOverallocationBehaviorAMD(2)

VkScopeNV = type('VkScopeNV', (c_enum,), dict(names=dict()))
VkScopeNV.names = {
    1 : 'VK_SCOPE_DEVICE_NV',
    2 : 'VK_SCOPE_WORKGROUP_NV',
    3 : 'VK_SCOPE_SUBGROUP_NV',
    5 : 'VK_SCOPE_QUEUE_FAMILY_NV',
}
VK_SCOPE_DEVICE_NV = VkScopeNV(1)
VK_SCOPE_WORKGROUP_NV = VkScopeNV(2)
VK_SCOPE_SUBGROUP_NV = VkScopeNV(3)
VK_SCOPE_QUEUE_FAMILY_NV = VkScopeNV(5)

VkComponentTypeNV = type('VkComponentTypeNV', (c_enum,), dict(names=dict()))
VkComponentTypeNV.names = {
    0 : 'VK_COMPONENT_TYPE_FLOAT16_NV',
    1 : 'VK_COMPONENT_TYPE_FLOAT32_NV',
    2 : 'VK_COMPONENT_TYPE_FLOAT64_NV',
    3 : 'VK_COMPONENT_TYPE_SINT8_NV',
    4 : 'VK_COMPONENT_TYPE_SINT16_NV',
    5 : 'VK_COMPONENT_TYPE_SINT32_NV',
    6 : 'VK_COMPONENT_TYPE_SINT64_NV',
    7 : 'VK_COMPONENT_TYPE_UINT8_NV',
    8 : 'VK_COMPONENT_TYPE_UINT16_NV',
    9 : 'VK_COMPONENT_TYPE_UINT32_NV',
    10 : 'VK_COMPONENT_TYPE_UINT64_NV',
}
VK_COMPONENT_TYPE_FLOAT16_NV = VkComponentTypeNV(0)
VK_COMPONENT_TYPE_FLOAT32_NV = VkComponentTypeNV(1)
VK_COMPONENT_TYPE_FLOAT64_NV = VkComponentTypeNV(2)
VK_COMPONENT_TYPE_SINT8_NV = VkComponentTypeNV(3)
VK_COMPONENT_TYPE_SINT16_NV = VkComponentTypeNV(4)
VK_COMPONENT_TYPE_SINT32_NV = VkComponentTypeNV(5)
VK_COMPONENT_TYPE_SINT64_NV = VkComponentTypeNV(6)
VK_COMPONENT_TYPE_UINT8_NV = VkComponentTypeNV(7)
VK_COMPONENT_TYPE_UINT16_NV = VkComponentTypeNV(8)
VK_COMPONENT_TYPE_UINT32_NV = VkComponentTypeNV(9)
VK_COMPONENT_TYPE_UINT64_NV = VkComponentTypeNV(10)

VkDeviceDiagnosticsConfigFlagBitsNV = type('VkDeviceDiagnosticsConfigFlagBitsNV', (c_enum,), dict(names=dict()))
VkDeviceDiagnosticsConfigFlagBitsNV.names = {
    1 : 'VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_SHADER_DEBUG_INFO_BIT_NV',
    2 : 'VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_RESOURCE_TRACKING_BIT_NV',
    4 : 'VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_AUTOMATIC_CHECKPOINTS_BIT_NV',
}
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_SHADER_DEBUG_INFO_BIT_NV = VkDeviceDiagnosticsConfigFlagBitsNV(1)
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_RESOURCE_TRACKING_BIT_NV = VkDeviceDiagnosticsConfigFlagBitsNV(2)
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_AUTOMATIC_CHECKPOINTS_BIT_NV = VkDeviceDiagnosticsConfigFlagBitsNV(4)

VkPipelineCreationFeedbackFlagBitsEXT = type('VkPipelineCreationFeedbackFlagBitsEXT', (c_enum,), dict(names=dict()))
VkPipelineCreationFeedbackFlagBitsEXT.names = {
    1 : 'VK_PIPELINE_CREATION_FEEDBACK_VALID_BIT_EXT',
    2 : 'VK_PIPELINE_CREATION_FEEDBACK_APPLICATION_PIPELINE_CACHE_HIT_BIT_EXT',
    4 : 'VK_PIPELINE_CREATION_FEEDBACK_BASE_PIPELINE_ACCELERATION_BIT_EXT',
}
VK_PIPELINE_CREATION_FEEDBACK_VALID_BIT_EXT = VkPipelineCreationFeedbackFlagBitsEXT(1)
VK_PIPELINE_CREATION_FEEDBACK_APPLICATION_PIPELINE_CACHE_HIT_BIT_EXT = VkPipelineCreationFeedbackFlagBitsEXT(2)
VK_PIPELINE_CREATION_FEEDBACK_BASE_PIPELINE_ACCELERATION_BIT_EXT = VkPipelineCreationFeedbackFlagBitsEXT(4)

VkPerformanceCounterScopeKHR = type('VkPerformanceCounterScopeKHR', (c_enum,), dict(names=dict()))
VkPerformanceCounterScopeKHR.names = {
    0 : 'VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR',
    1 : 'VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR',
    2 : 'VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR',
}
VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR = VkPerformanceCounterScopeKHR(0)
VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR = VkPerformanceCounterScopeKHR(1)
VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR = VkPerformanceCounterScopeKHR(2)
VK_QUERY_SCOPE_COMMAND_BUFFER_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR
VK_QUERY_SCOPE_RENDER_PASS_KHR = VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR
VK_QUERY_SCOPE_COMMAND_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR

VkPerformanceCounterUnitKHR = type('VkPerformanceCounterUnitKHR', (c_enum,), dict(names=dict()))
VkPerformanceCounterUnitKHR.names = {
    0 : 'VK_PERFORMANCE_COUNTER_UNIT_GENERIC_KHR',
    1 : 'VK_PERFORMANCE_COUNTER_UNIT_PERCENTAGE_KHR',
    2 : 'VK_PERFORMANCE_COUNTER_UNIT_NANOSECONDS_KHR',
    3 : 'VK_PERFORMANCE_COUNTER_UNIT_BYTES_KHR',
    4 : 'VK_PERFORMANCE_COUNTER_UNIT_BYTES_PER_SECOND_KHR',
    5 : 'VK_PERFORMANCE_COUNTER_UNIT_KELVIN_KHR',
    6 : 'VK_PERFORMANCE_COUNTER_UNIT_WATTS_KHR',
    7 : 'VK_PERFORMANCE_COUNTER_UNIT_VOLTS_KHR',
    8 : 'VK_PERFORMANCE_COUNTER_UNIT_AMPS_KHR',
    9 : 'VK_PERFORMANCE_COUNTER_UNIT_HERTZ_KHR',
    10 : 'VK_PERFORMANCE_COUNTER_UNIT_CYCLES_KHR',
}
VK_PERFORMANCE_COUNTER_UNIT_GENERIC_KHR = VkPerformanceCounterUnitKHR(0)
VK_PERFORMANCE_COUNTER_UNIT_PERCENTAGE_KHR = VkPerformanceCounterUnitKHR(1)
VK_PERFORMANCE_COUNTER_UNIT_NANOSECONDS_KHR = VkPerformanceCounterUnitKHR(2)
VK_PERFORMANCE_COUNTER_UNIT_BYTES_KHR = VkPerformanceCounterUnitKHR(3)
VK_PERFORMANCE_COUNTER_UNIT_BYTES_PER_SECOND_KHR = VkPerformanceCounterUnitKHR(4)
VK_PERFORMANCE_COUNTER_UNIT_KELVIN_KHR = VkPerformanceCounterUnitKHR(5)
VK_PERFORMANCE_COUNTER_UNIT_WATTS_KHR = VkPerformanceCounterUnitKHR(6)
VK_PERFORMANCE_COUNTER_UNIT_VOLTS_KHR = VkPerformanceCounterUnitKHR(7)
VK_PERFORMANCE_COUNTER_UNIT_AMPS_KHR = VkPerformanceCounterUnitKHR(8)
VK_PERFORMANCE_COUNTER_UNIT_HERTZ_KHR = VkPerformanceCounterUnitKHR(9)
VK_PERFORMANCE_COUNTER_UNIT_CYCLES_KHR = VkPerformanceCounterUnitKHR(10)

VkPerformanceCounterStorageKHR = type('VkPerformanceCounterStorageKHR', (c_enum,), dict(names=dict()))
VkPerformanceCounterStorageKHR.names = {
    0 : 'VK_PERFORMANCE_COUNTER_STORAGE_INT32_KHR',
    1 : 'VK_PERFORMANCE_COUNTER_STORAGE_INT64_KHR',
    2 : 'VK_PERFORMANCE_COUNTER_STORAGE_UINT32_KHR',
    3 : 'VK_PERFORMANCE_COUNTER_STORAGE_UINT64_KHR',
    4 : 'VK_PERFORMANCE_COUNTER_STORAGE_FLOAT32_KHR',
    5 : 'VK_PERFORMANCE_COUNTER_STORAGE_FLOAT64_KHR',
}
VK_PERFORMANCE_COUNTER_STORAGE_INT32_KHR = VkPerformanceCounterStorageKHR(0)
VK_PERFORMANCE_COUNTER_STORAGE_INT64_KHR = VkPerformanceCounterStorageKHR(1)
VK_PERFORMANCE_COUNTER_STORAGE_UINT32_KHR = VkPerformanceCounterStorageKHR(2)
VK_PERFORMANCE_COUNTER_STORAGE_UINT64_KHR = VkPerformanceCounterStorageKHR(3)
VK_PERFORMANCE_COUNTER_STORAGE_FLOAT32_KHR = VkPerformanceCounterStorageKHR(4)
VK_PERFORMANCE_COUNTER_STORAGE_FLOAT64_KHR = VkPerformanceCounterStorageKHR(5)

VkPerformanceCounterDescriptionFlagBitsKHR = type('VkPerformanceCounterDescriptionFlagBitsKHR', (c_enum,), dict(names=dict()))
VkPerformanceCounterDescriptionFlagBitsKHR.names = {
    1 : 'VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR',
    2 : 'VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR',
}
VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR = VkPerformanceCounterDescriptionFlagBitsKHR(1)
VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_KHR = VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR
VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR = VkPerformanceCounterDescriptionFlagBitsKHR(2)
VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_KHR = VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR

VkAcquireProfilingLockFlagBitsKHR = type('VkAcquireProfilingLockFlagBitsKHR', (c_enum,), dict(names=dict()))
VkAcquireProfilingLockFlagBitsKHR.names = {
}

VkSemaphoreWaitFlagBits = type('VkSemaphoreWaitFlagBits', (c_enum,), dict(names=dict()))
VkSemaphoreWaitFlagBits.names = {
    1 : 'VK_SEMAPHORE_WAIT_ANY_BIT',
}
VK_SEMAPHORE_WAIT_ANY_BIT = VkSemaphoreWaitFlagBits(1)
VK_SEMAPHORE_WAIT_ANY_BIT_KHR = VK_SEMAPHORE_WAIT_ANY_BIT

VkSemaphoreWaitFlagBitsKHR = VkSemaphoreWaitFlagBits

VkPerformanceConfigurationTypeINTEL = type('VkPerformanceConfigurationTypeINTEL', (c_enum,), dict(names=dict()))
VkPerformanceConfigurationTypeINTEL.names = {
    0 : 'VK_PERFORMANCE_CONFIGURATION_TYPE_COMMAND_QUEUE_METRICS_DISCOVERY_ACTIVATED_INTEL',
}
VK_PERFORMANCE_CONFIGURATION_TYPE_COMMAND_QUEUE_METRICS_DISCOVERY_ACTIVATED_INTEL = VkPerformanceConfigurationTypeINTEL(0)

VkQueryPoolSamplingModeINTEL = type('VkQueryPoolSamplingModeINTEL', (c_enum,), dict(names=dict()))
VkQueryPoolSamplingModeINTEL.names = {
    0 : 'VK_QUERY_POOL_SAMPLING_MODE_MANUAL_INTEL',
}
VK_QUERY_POOL_SAMPLING_MODE_MANUAL_INTEL = VkQueryPoolSamplingModeINTEL(0)

VkPerformanceOverrideTypeINTEL = type('VkPerformanceOverrideTypeINTEL', (c_enum,), dict(names=dict()))
VkPerformanceOverrideTypeINTEL.names = {
    0 : 'VK_PERFORMANCE_OVERRIDE_TYPE_NULL_HARDWARE_INTEL',
    1 : 'VK_PERFORMANCE_OVERRIDE_TYPE_FLUSH_GPU_CACHES_INTEL',
}
VK_PERFORMANCE_OVERRIDE_TYPE_NULL_HARDWARE_INTEL = VkPerformanceOverrideTypeINTEL(0)
VK_PERFORMANCE_OVERRIDE_TYPE_FLUSH_GPU_CACHES_INTEL = VkPerformanceOverrideTypeINTEL(1)

VkPerformanceParameterTypeINTEL = type('VkPerformanceParameterTypeINTEL', (c_enum,), dict(names=dict()))
VkPerformanceParameterTypeINTEL.names = {
    0 : 'VK_PERFORMANCE_PARAMETER_TYPE_HW_COUNTERS_SUPPORTED_INTEL',
    1 : 'VK_PERFORMANCE_PARAMETER_TYPE_STREAM_MARKER_VALID_BITS_INTEL',
}
VK_PERFORMANCE_PARAMETER_TYPE_HW_COUNTERS_SUPPORTED_INTEL = VkPerformanceParameterTypeINTEL(0)
VK_PERFORMANCE_PARAMETER_TYPE_STREAM_MARKER_VALID_BITS_INTEL = VkPerformanceParameterTypeINTEL(1)

VkPerformanceValueTypeINTEL = type('VkPerformanceValueTypeINTEL', (c_enum,), dict(names=dict()))
VkPerformanceValueTypeINTEL.names = {
    0 : 'VK_PERFORMANCE_VALUE_TYPE_UINT32_INTEL',
    1 : 'VK_PERFORMANCE_VALUE_TYPE_UINT64_INTEL',
    2 : 'VK_PERFORMANCE_VALUE_TYPE_FLOAT_INTEL',
    3 : 'VK_PERFORMANCE_VALUE_TYPE_BOOL_INTEL',
    4 : 'VK_PERFORMANCE_VALUE_TYPE_STRING_INTEL',
}
VK_PERFORMANCE_VALUE_TYPE_UINT32_INTEL = VkPerformanceValueTypeINTEL(0)
VK_PERFORMANCE_VALUE_TYPE_UINT64_INTEL = VkPerformanceValueTypeINTEL(1)
VK_PERFORMANCE_VALUE_TYPE_FLOAT_INTEL = VkPerformanceValueTypeINTEL(2)
VK_PERFORMANCE_VALUE_TYPE_BOOL_INTEL = VkPerformanceValueTypeINTEL(3)
VK_PERFORMANCE_VALUE_TYPE_STRING_INTEL = VkPerformanceValueTypeINTEL(4)

VkLineRasterizationModeEXT = type('VkLineRasterizationModeEXT', (c_enum,), dict(names=dict()))
VkLineRasterizationModeEXT.names = {
    0 : 'VK_LINE_RASTERIZATION_MODE_DEFAULT_EXT',
    1 : 'VK_LINE_RASTERIZATION_MODE_RECTANGULAR_EXT',
    2 : 'VK_LINE_RASTERIZATION_MODE_BRESENHAM_EXT',
    3 : 'VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_EXT',
}
VK_LINE_RASTERIZATION_MODE_DEFAULT_EXT = VkLineRasterizationModeEXT(0)
VK_LINE_RASTERIZATION_MODE_RECTANGULAR_EXT = VkLineRasterizationModeEXT(1)
VK_LINE_RASTERIZATION_MODE_BRESENHAM_EXT = VkLineRasterizationModeEXT(2)
VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_EXT = VkLineRasterizationModeEXT(3)

VkShaderModuleCreateFlagBits = type('VkShaderModuleCreateFlagBits', (c_enum,), dict(names=dict()))
VkShaderModuleCreateFlagBits.names = {
}

VkPipelineCompilerControlFlagBitsAMD = type('VkPipelineCompilerControlFlagBitsAMD', (c_enum,), dict(names=dict()))
VkPipelineCompilerControlFlagBitsAMD.names = {
}

VkShaderCorePropertiesFlagBitsAMD = type('VkShaderCorePropertiesFlagBitsAMD', (c_enum,), dict(names=dict()))
VkShaderCorePropertiesFlagBitsAMD.names = {
}

VkToolPurposeFlagBitsEXT = type('VkToolPurposeFlagBitsEXT', (c_enum,), dict(names=dict()))
VkToolPurposeFlagBitsEXT.names = {
    1 : 'VK_TOOL_PURPOSE_VALIDATION_BIT_EXT',
    2 : 'VK_TOOL_PURPOSE_PROFILING_BIT_EXT',
    4 : 'VK_TOOL_PURPOSE_TRACING_BIT_EXT',
    8 : 'VK_TOOL_PURPOSE_ADDITIONAL_FEATURES_BIT_EXT',
    16 : 'VK_TOOL_PURPOSE_MODIFYING_FEATURES_BIT_EXT',
    32 : 'VK_TOOL_PURPOSE_DEBUG_REPORTING_BIT_EXT',
    64 : 'VK_TOOL_PURPOSE_DEBUG_MARKERS_BIT_EXT',
    32 : 'VK_TOOL_PURPOSE_DEBUG_REPORTING_BIT_EXT',
    64 : 'VK_TOOL_PURPOSE_DEBUG_MARKERS_BIT_EXT',
}
VK_TOOL_PURPOSE_VALIDATION_BIT_EXT = VkToolPurposeFlagBitsEXT(1)
VK_TOOL_PURPOSE_PROFILING_BIT_EXT = VkToolPurposeFlagBitsEXT(2)
VK_TOOL_PURPOSE_TRACING_BIT_EXT = VkToolPurposeFlagBitsEXT(4)
VK_TOOL_PURPOSE_ADDITIONAL_FEATURES_BIT_EXT = VkToolPurposeFlagBitsEXT(8)
VK_TOOL_PURPOSE_MODIFYING_FEATURES_BIT_EXT = VkToolPurposeFlagBitsEXT(16)
VK_TOOL_PURPOSE_DEBUG_REPORTING_BIT_EXT = VkToolPurposeFlagBitsEXT(32)
VK_TOOL_PURPOSE_DEBUG_MARKERS_BIT_EXT = VkToolPurposeFlagBitsEXT(64)
VK_TOOL_PURPOSE_DEBUG_REPORTING_BIT_EXT = VkToolPurposeFlagBitsEXT(32)
VK_TOOL_PURPOSE_DEBUG_MARKERS_BIT_EXT = VkToolPurposeFlagBitsEXT(64)

VkFragmentShadingRateNV = type('VkFragmentShadingRateNV', (c_enum,), dict(names=dict()))
VkFragmentShadingRateNV.names = {
    0 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV',
    1 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV',
    4 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV',
    5 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV',
    6 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV',
    9 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV',
    10 : 'VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV',
    11 : 'VK_FRAGMENT_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV',
    12 : 'VK_FRAGMENT_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV',
    13 : 'VK_FRAGMENT_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV',
    14 : 'VK_FRAGMENT_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV',
    15 : 'VK_FRAGMENT_SHADING_RATE_NO_INVOCATIONS_NV',
}
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV = VkFragmentShadingRateNV(0)
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV = VkFragmentShadingRateNV(1)
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV = VkFragmentShadingRateNV(4)
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV = VkFragmentShadingRateNV(5)
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV = VkFragmentShadingRateNV(6)
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV = VkFragmentShadingRateNV(9)
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV = VkFragmentShadingRateNV(10)
VK_FRAGMENT_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV = VkFragmentShadingRateNV(11)
VK_FRAGMENT_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV = VkFragmentShadingRateNV(12)
VK_FRAGMENT_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV = VkFragmentShadingRateNV(13)
VK_FRAGMENT_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV = VkFragmentShadingRateNV(14)
VK_FRAGMENT_SHADING_RATE_NO_INVOCATIONS_NV = VkFragmentShadingRateNV(15)

VkFragmentShadingRateTypeNV = type('VkFragmentShadingRateTypeNV', (c_enum,), dict(names=dict()))
VkFragmentShadingRateTypeNV.names = {
    0 : 'VK_FRAGMENT_SHADING_RATE_TYPE_FRAGMENT_SIZE_NV',
    1 : 'VK_FRAGMENT_SHADING_RATE_TYPE_ENUMS_NV',
}
VK_FRAGMENT_SHADING_RATE_TYPE_FRAGMENT_SIZE_NV = VkFragmentShadingRateTypeNV(0)
VK_FRAGMENT_SHADING_RATE_TYPE_ENUMS_NV = VkFragmentShadingRateTypeNV(1)

VkColorSpaceKHR = type('VkColorSpaceKHR', (c_enum,), dict(names=dict()))
VkColorSpaceKHR.names = {
    0 : 'VK_COLOR_SPACE_SRGB_NONLINEAR_KHR',
    1000104001 : 'VK_COLOR_SPACE_DISPLAY_P3_NONLINEAR_EXT',
    1000104002 : 'VK_COLOR_SPACE_EXTENDED_SRGB_LINEAR_EXT',
    1000104003 : 'VK_COLOR_SPACE_DISPLAY_P3_LINEAR_EXT',
    1000104004 : 'VK_COLOR_SPACE_DCI_P3_NONLINEAR_EXT',
    1000104005 : 'VK_COLOR_SPACE_BT709_LINEAR_EXT',
    1000104006 : 'VK_COLOR_SPACE_BT709_NONLINEAR_EXT',
    1000104007 : 'VK_COLOR_SPACE_BT2020_LINEAR_EXT',
    1000104008 : 'VK_COLOR_SPACE_HDR10_ST2084_EXT',
    1000104009 : 'VK_COLOR_SPACE_DOLBYVISION_EXT',
    1000104010 : 'VK_COLOR_SPACE_HDR10_HLG_EXT',
    1000104011 : 'VK_COLOR_SPACE_ADOBERGB_LINEAR_EXT',
    1000104012 : 'VK_COLOR_SPACE_ADOBERGB_NONLINEAR_EXT',
    1000104013 : 'VK_COLOR_SPACE_PASS_THROUGH_EXT',
    1000104014 : 'VK_COLOR_SPACE_EXTENDED_SRGB_NONLINEAR_EXT',
    1000213000 : 'VK_COLOR_SPACE_DISPLAY_NATIVE_AMD',
}
VK_COLOR_SPACE_SRGB_NONLINEAR_KHR = VkColorSpaceKHR(0)
VK_COLORSPACE_SRGB_NONLINEAR_KHR = VK_COLOR_SPACE_SRGB_NONLINEAR_KHR
VK_COLOR_SPACE_DISPLAY_P3_NONLINEAR_EXT = VkColorSpaceKHR(1000104001)
VK_COLOR_SPACE_EXTENDED_SRGB_LINEAR_EXT = VkColorSpaceKHR(1000104002)
VK_COLOR_SPACE_DISPLAY_P3_LINEAR_EXT = VkColorSpaceKHR(1000104003)
VK_COLOR_SPACE_DCI_P3_NONLINEAR_EXT = VkColorSpaceKHR(1000104004)
VK_COLOR_SPACE_BT709_LINEAR_EXT = VkColorSpaceKHR(1000104005)
VK_COLOR_SPACE_BT709_NONLINEAR_EXT = VkColorSpaceKHR(1000104006)
VK_COLOR_SPACE_BT2020_LINEAR_EXT = VkColorSpaceKHR(1000104007)
VK_COLOR_SPACE_HDR10_ST2084_EXT = VkColorSpaceKHR(1000104008)
VK_COLOR_SPACE_DOLBYVISION_EXT = VkColorSpaceKHR(1000104009)
VK_COLOR_SPACE_HDR10_HLG_EXT = VkColorSpaceKHR(1000104010)
VK_COLOR_SPACE_ADOBERGB_LINEAR_EXT = VkColorSpaceKHR(1000104011)
VK_COLOR_SPACE_ADOBERGB_NONLINEAR_EXT = VkColorSpaceKHR(1000104012)
VK_COLOR_SPACE_PASS_THROUGH_EXT = VkColorSpaceKHR(1000104013)
VK_COLOR_SPACE_EXTENDED_SRGB_NONLINEAR_EXT = VkColorSpaceKHR(1000104014)
VK_COLOR_SPACE_DCI_P3_LINEAR_EXT = VK_COLOR_SPACE_DISPLAY_P3_LINEAR_EXT
VK_COLOR_SPACE_DISPLAY_NATIVE_AMD = VkColorSpaceKHR(1000213000)

VkCompositeAlphaFlagBitsKHR = type('VkCompositeAlphaFlagBitsKHR', (c_enum,), dict(names=dict()))
VkCompositeAlphaFlagBitsKHR.names = {
    1 : 'VK_COMPOSITE_ALPHA_OPAQUE_BIT_KHR',
    2 : 'VK_COMPOSITE_ALPHA_PRE_MULTIPLIED_BIT_KHR',
    4 : 'VK_COMPOSITE_ALPHA_POST_MULTIPLIED_BIT_KHR',
    8 : 'VK_COMPOSITE_ALPHA_INHERIT_BIT_KHR',
}
VK_COMPOSITE_ALPHA_OPAQUE_BIT_KHR = VkCompositeAlphaFlagBitsKHR(1)
VK_COMPOSITE_ALPHA_PRE_MULTIPLIED_BIT_KHR = VkCompositeAlphaFlagBitsKHR(2)
VK_COMPOSITE_ALPHA_POST_MULTIPLIED_BIT_KHR = VkCompositeAlphaFlagBitsKHR(4)
VK_COMPOSITE_ALPHA_INHERIT_BIT_KHR = VkCompositeAlphaFlagBitsKHR(8)

VkDisplayPlaneAlphaFlagBitsKHR = type('VkDisplayPlaneAlphaFlagBitsKHR', (c_enum,), dict(names=dict()))
VkDisplayPlaneAlphaFlagBitsKHR.names = {
    1 : 'VK_DISPLAY_PLANE_ALPHA_OPAQUE_BIT_KHR',
    2 : 'VK_DISPLAY_PLANE_ALPHA_GLOBAL_BIT_KHR',
    4 : 'VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_BIT_KHR',
    8 : 'VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_PREMULTIPLIED_BIT_KHR',
}
VK_DISPLAY_PLANE_ALPHA_OPAQUE_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(1)
VK_DISPLAY_PLANE_ALPHA_GLOBAL_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(2)
VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(4)
VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_PREMULTIPLIED_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(8)

VkPresentModeKHR = type('VkPresentModeKHR', (c_enum,), dict(names=dict()))
VkPresentModeKHR.names = {
    0 : 'VK_PRESENT_MODE_IMMEDIATE_KHR',
    1 : 'VK_PRESENT_MODE_MAILBOX_KHR',
    2 : 'VK_PRESENT_MODE_FIFO_KHR',
    3 : 'VK_PRESENT_MODE_FIFO_RELAXED_KHR',
    1000111000 : 'VK_PRESENT_MODE_SHARED_DEMAND_REFRESH_KHR',
    1000111001 : 'VK_PRESENT_MODE_SHARED_CONTINUOUS_REFRESH_KHR',
}
VK_PRESENT_MODE_IMMEDIATE_KHR = VkPresentModeKHR(0)
VK_PRESENT_MODE_MAILBOX_KHR = VkPresentModeKHR(1)
VK_PRESENT_MODE_FIFO_KHR = VkPresentModeKHR(2)
VK_PRESENT_MODE_FIFO_RELAXED_KHR = VkPresentModeKHR(3)
VK_PRESENT_MODE_SHARED_DEMAND_REFRESH_KHR = VkPresentModeKHR(1000111000)
VK_PRESENT_MODE_SHARED_CONTINUOUS_REFRESH_KHR = VkPresentModeKHR(1000111001)

VkSurfaceTransformFlagBitsKHR = type('VkSurfaceTransformFlagBitsKHR', (c_enum,), dict(names=dict()))
VkSurfaceTransformFlagBitsKHR.names = {
    1 : 'VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR',
    2 : 'VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR',
    4 : 'VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR',
    8 : 'VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR',
    16 : 'VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_BIT_KHR',
    32 : 'VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_90_BIT_KHR',
    64 : 'VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_180_BIT_KHR',
    128 : 'VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_270_BIT_KHR',
    256 : 'VK_SURFACE_TRANSFORM_INHERIT_BIT_KHR',
}
VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR = VkSurfaceTransformFlagBitsKHR(1)
VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR = VkSurfaceTransformFlagBitsKHR(2)
VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR = VkSurfaceTransformFlagBitsKHR(4)
VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR = VkSurfaceTransformFlagBitsKHR(8)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_BIT_KHR = VkSurfaceTransformFlagBitsKHR(16)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_90_BIT_KHR = VkSurfaceTransformFlagBitsKHR(32)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_180_BIT_KHR = VkSurfaceTransformFlagBitsKHR(64)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_270_BIT_KHR = VkSurfaceTransformFlagBitsKHR(128)
VK_SURFACE_TRANSFORM_INHERIT_BIT_KHR = VkSurfaceTransformFlagBitsKHR(256)

VkDebugReportFlagBitsEXT = type('VkDebugReportFlagBitsEXT', (c_enum,), dict(names=dict()))
VkDebugReportFlagBitsEXT.names = {
    1 : 'VK_DEBUG_REPORT_INFORMATION_BIT_EXT',
    2 : 'VK_DEBUG_REPORT_WARNING_BIT_EXT',
    4 : 'VK_DEBUG_REPORT_PERFORMANCE_WARNING_BIT_EXT',
    8 : 'VK_DEBUG_REPORT_ERROR_BIT_EXT',
    16 : 'VK_DEBUG_REPORT_DEBUG_BIT_EXT',
}
VK_DEBUG_REPORT_INFORMATION_BIT_EXT = VkDebugReportFlagBitsEXT(1)
VK_DEBUG_REPORT_WARNING_BIT_EXT = VkDebugReportFlagBitsEXT(2)
VK_DEBUG_REPORT_PERFORMANCE_WARNING_BIT_EXT = VkDebugReportFlagBitsEXT(4)
VK_DEBUG_REPORT_ERROR_BIT_EXT = VkDebugReportFlagBitsEXT(8)
VK_DEBUG_REPORT_DEBUG_BIT_EXT = VkDebugReportFlagBitsEXT(16)

VkDebugReportObjectTypeEXT = type('VkDebugReportObjectTypeEXT', (c_enum,), dict(names=dict()))
VkDebugReportObjectTypeEXT.names = {
    0 : 'VK_DEBUG_REPORT_OBJECT_TYPE_UNKNOWN_EXT',
    1 : 'VK_DEBUG_REPORT_OBJECT_TYPE_INSTANCE_EXT',
    2 : 'VK_DEBUG_REPORT_OBJECT_TYPE_PHYSICAL_DEVICE_EXT',
    3 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_EXT',
    4 : 'VK_DEBUG_REPORT_OBJECT_TYPE_QUEUE_EXT',
    5 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SEMAPHORE_EXT',
    6 : 'VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_BUFFER_EXT',
    7 : 'VK_DEBUG_REPORT_OBJECT_TYPE_FENCE_EXT',
    8 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_MEMORY_EXT',
    9 : 'VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_EXT',
    10 : 'VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_EXT',
    11 : 'VK_DEBUG_REPORT_OBJECT_TYPE_EVENT_EXT',
    12 : 'VK_DEBUG_REPORT_OBJECT_TYPE_QUERY_POOL_EXT',
    13 : 'VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_VIEW_EXT',
    14 : 'VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_VIEW_EXT',
    15 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SHADER_MODULE_EXT',
    16 : 'VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_CACHE_EXT',
    17 : 'VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_LAYOUT_EXT',
    18 : 'VK_DEBUG_REPORT_OBJECT_TYPE_RENDER_PASS_EXT',
    19 : 'VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_EXT',
    20 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT_EXT',
    21 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_EXT',
    22 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_POOL_EXT',
    23 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_EXT',
    24 : 'VK_DEBUG_REPORT_OBJECT_TYPE_FRAMEBUFFER_EXT',
    25 : 'VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_POOL_EXT',
    26 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SURFACE_KHR_EXT',
    27 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SWAPCHAIN_KHR_EXT',
    28 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT',
    29 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_KHR_EXT',
    30 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_MODE_KHR_EXT',
    33 : 'VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT',
    1000156000 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT',
    1000085000 : 'VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_EXT',
    1000150000 : 'VK_DEBUG_REPORT_OBJECT_TYPE_ACCELERATION_STRUCTURE_KHR_EXT',
    1000156000 : 'VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT',
    1000165000 : 'VK_DEBUG_REPORT_OBJECT_TYPE_ACCELERATION_STRUCTURE_NV_EXT',
}
VK_DEBUG_REPORT_OBJECT_TYPE_UNKNOWN_EXT = VkDebugReportObjectTypeEXT(0)
VK_DEBUG_REPORT_OBJECT_TYPE_INSTANCE_EXT = VkDebugReportObjectTypeEXT(1)
VK_DEBUG_REPORT_OBJECT_TYPE_PHYSICAL_DEVICE_EXT = VkDebugReportObjectTypeEXT(2)
VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_EXT = VkDebugReportObjectTypeEXT(3)
VK_DEBUG_REPORT_OBJECT_TYPE_QUEUE_EXT = VkDebugReportObjectTypeEXT(4)
VK_DEBUG_REPORT_OBJECT_TYPE_SEMAPHORE_EXT = VkDebugReportObjectTypeEXT(5)
VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_BUFFER_EXT = VkDebugReportObjectTypeEXT(6)
VK_DEBUG_REPORT_OBJECT_TYPE_FENCE_EXT = VkDebugReportObjectTypeEXT(7)
VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_MEMORY_EXT = VkDebugReportObjectTypeEXT(8)
VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_EXT = VkDebugReportObjectTypeEXT(9)
VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_EXT = VkDebugReportObjectTypeEXT(10)
VK_DEBUG_REPORT_OBJECT_TYPE_EVENT_EXT = VkDebugReportObjectTypeEXT(11)
VK_DEBUG_REPORT_OBJECT_TYPE_QUERY_POOL_EXT = VkDebugReportObjectTypeEXT(12)
VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_VIEW_EXT = VkDebugReportObjectTypeEXT(13)
VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_VIEW_EXT = VkDebugReportObjectTypeEXT(14)
VK_DEBUG_REPORT_OBJECT_TYPE_SHADER_MODULE_EXT = VkDebugReportObjectTypeEXT(15)
VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_CACHE_EXT = VkDebugReportObjectTypeEXT(16)
VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_LAYOUT_EXT = VkDebugReportObjectTypeEXT(17)
VK_DEBUG_REPORT_OBJECT_TYPE_RENDER_PASS_EXT = VkDebugReportObjectTypeEXT(18)
VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_EXT = VkDebugReportObjectTypeEXT(19)
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT_EXT = VkDebugReportObjectTypeEXT(20)
VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_EXT = VkDebugReportObjectTypeEXT(21)
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_POOL_EXT = VkDebugReportObjectTypeEXT(22)
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_EXT = VkDebugReportObjectTypeEXT(23)
VK_DEBUG_REPORT_OBJECT_TYPE_FRAMEBUFFER_EXT = VkDebugReportObjectTypeEXT(24)
VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_POOL_EXT = VkDebugReportObjectTypeEXT(25)
VK_DEBUG_REPORT_OBJECT_TYPE_SURFACE_KHR_EXT = VkDebugReportObjectTypeEXT(26)
VK_DEBUG_REPORT_OBJECT_TYPE_SWAPCHAIN_KHR_EXT = VkDebugReportObjectTypeEXT(27)
VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT = VkDebugReportObjectTypeEXT(28)
VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT
VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_KHR_EXT = VkDebugReportObjectTypeEXT(29)
VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_MODE_KHR_EXT = VkDebugReportObjectTypeEXT(30)
VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT = VkDebugReportObjectTypeEXT(33)
VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT
VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT = VkDebugReportObjectTypeEXT(1000156000)
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_EXT = VkDebugReportObjectTypeEXT(1000085000)
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_KHR_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_EXT
VK_DEBUG_REPORT_OBJECT_TYPE_ACCELERATION_STRUCTURE_KHR_EXT = VkDebugReportObjectTypeEXT(1000150000)
VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_KHR_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT
VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT = VkDebugReportObjectTypeEXT(1000156000)
VK_DEBUG_REPORT_OBJECT_TYPE_ACCELERATION_STRUCTURE_NV_EXT = VkDebugReportObjectTypeEXT(1000165000)

VkDeviceMemoryReportEventTypeEXT = type('VkDeviceMemoryReportEventTypeEXT', (c_enum,), dict(names=dict()))
VkDeviceMemoryReportEventTypeEXT.names = {
    0 : 'VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATE_EXT',
    1 : 'VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_FREE_EXT',
    2 : 'VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_IMPORT_EXT',
    3 : 'VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_UNIMPORT_EXT',
    4 : 'VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATION_FAILED_EXT',
}
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATE_EXT = VkDeviceMemoryReportEventTypeEXT(0)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_FREE_EXT = VkDeviceMemoryReportEventTypeEXT(1)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_IMPORT_EXT = VkDeviceMemoryReportEventTypeEXT(2)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_UNIMPORT_EXT = VkDeviceMemoryReportEventTypeEXT(3)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATION_FAILED_EXT = VkDeviceMemoryReportEventTypeEXT(4)

VkRasterizationOrderAMD = type('VkRasterizationOrderAMD', (c_enum,), dict(names=dict()))
VkRasterizationOrderAMD.names = {
    0 : 'VK_RASTERIZATION_ORDER_STRICT_AMD',
    1 : 'VK_RASTERIZATION_ORDER_RELAXED_AMD',
}
VK_RASTERIZATION_ORDER_STRICT_AMD = VkRasterizationOrderAMD(0)
VK_RASTERIZATION_ORDER_RELAXED_AMD = VkRasterizationOrderAMD(1)

VkExternalMemoryHandleTypeFlagBitsNV = type('VkExternalMemoryHandleTypeFlagBitsNV', (c_enum,), dict(names=dict()))
VkExternalMemoryHandleTypeFlagBitsNV.names = {
    1 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT_NV',
    2 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_NV',
    4 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_BIT_NV',
    8 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_KMT_BIT_NV',
}
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(1)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(2)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(4)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_KMT_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(8)

VkExternalMemoryFeatureFlagBitsNV = type('VkExternalMemoryFeatureFlagBitsNV', (c_enum,), dict(names=dict()))
VkExternalMemoryFeatureFlagBitsNV.names = {
    1 : 'VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_NV',
    2 : 'VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_NV',
    4 : 'VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_NV',
}
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_NV = VkExternalMemoryFeatureFlagBitsNV(1)
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_NV = VkExternalMemoryFeatureFlagBitsNV(2)
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_NV = VkExternalMemoryFeatureFlagBitsNV(4)

VkValidationCheckEXT = type('VkValidationCheckEXT', (c_enum,), dict(names=dict()))
VkValidationCheckEXT.names = {
    0 : 'VK_VALIDATION_CHECK_ALL_EXT',
    1 : 'VK_VALIDATION_CHECK_SHADERS_EXT',
}
VK_VALIDATION_CHECK_ALL_EXT = VkValidationCheckEXT(0)
VK_VALIDATION_CHECK_SHADERS_EXT = VkValidationCheckEXT(1)

VkValidationFeatureEnableEXT = type('VkValidationFeatureEnableEXT', (c_enum,), dict(names=dict()))
VkValidationFeatureEnableEXT.names = {
    0 : 'VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_EXT',
    1 : 'VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_RESERVE_BINDING_SLOT_EXT',
    2 : 'VK_VALIDATION_FEATURE_ENABLE_BEST_PRACTICES_EXT',
    3 : 'VK_VALIDATION_FEATURE_ENABLE_DEBUG_PRINTF_EXT',
    4 : 'VK_VALIDATION_FEATURE_ENABLE_SYNCHRONIZATION_VALIDATION_EXT',
}
VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_EXT = VkValidationFeatureEnableEXT(0)
VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_RESERVE_BINDING_SLOT_EXT = VkValidationFeatureEnableEXT(1)
VK_VALIDATION_FEATURE_ENABLE_BEST_PRACTICES_EXT = VkValidationFeatureEnableEXT(2)
VK_VALIDATION_FEATURE_ENABLE_DEBUG_PRINTF_EXT = VkValidationFeatureEnableEXT(3)
VK_VALIDATION_FEATURE_ENABLE_SYNCHRONIZATION_VALIDATION_EXT = VkValidationFeatureEnableEXT(4)

VkValidationFeatureDisableEXT = type('VkValidationFeatureDisableEXT', (c_enum,), dict(names=dict()))
VkValidationFeatureDisableEXT.names = {
    0 : 'VK_VALIDATION_FEATURE_DISABLE_ALL_EXT',
    1 : 'VK_VALIDATION_FEATURE_DISABLE_SHADERS_EXT',
    2 : 'VK_VALIDATION_FEATURE_DISABLE_THREAD_SAFETY_EXT',
    3 : 'VK_VALIDATION_FEATURE_DISABLE_API_PARAMETERS_EXT',
    4 : 'VK_VALIDATION_FEATURE_DISABLE_OBJECT_LIFETIMES_EXT',
    5 : 'VK_VALIDATION_FEATURE_DISABLE_CORE_CHECKS_EXT',
    6 : 'VK_VALIDATION_FEATURE_DISABLE_UNIQUE_HANDLES_EXT',
}
VK_VALIDATION_FEATURE_DISABLE_ALL_EXT = VkValidationFeatureDisableEXT(0)
VK_VALIDATION_FEATURE_DISABLE_SHADERS_EXT = VkValidationFeatureDisableEXT(1)
VK_VALIDATION_FEATURE_DISABLE_THREAD_SAFETY_EXT = VkValidationFeatureDisableEXT(2)
VK_VALIDATION_FEATURE_DISABLE_API_PARAMETERS_EXT = VkValidationFeatureDisableEXT(3)
VK_VALIDATION_FEATURE_DISABLE_OBJECT_LIFETIMES_EXT = VkValidationFeatureDisableEXT(4)
VK_VALIDATION_FEATURE_DISABLE_CORE_CHECKS_EXT = VkValidationFeatureDisableEXT(5)
VK_VALIDATION_FEATURE_DISABLE_UNIQUE_HANDLES_EXT = VkValidationFeatureDisableEXT(6)

VkExternalMemoryHandleTypeFlagBits = type('VkExternalMemoryHandleTypeFlagBits', (c_enum,), dict(names=dict()))
VkExternalMemoryHandleTypeFlagBits.names = {
    1 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT',
    2 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT',
    4 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT',
    8 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_BIT',
    16 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_KMT_BIT',
    32 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP_BIT',
    64 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE_BIT',
    512 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_DMA_BUF_BIT_EXT',
    1024 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_ANDROID_HARDWARE_BUFFER_BIT_ANDROID',
    128 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_HOST_ALLOCATION_BIT_EXT',
    256 : 'VK_EXTERNAL_MEMORY_HANDLE_TYPE_HOST_MAPPED_FOREIGN_MEMORY_BIT_EXT',
}
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT = VkExternalMemoryHandleTypeFlagBits(1)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT = VkExternalMemoryHandleTypeFlagBits(2)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = VkExternalMemoryHandleTypeFlagBits(4)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_BIT = VkExternalMemoryHandleTypeFlagBits(8)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_KMT_BIT = VkExternalMemoryHandleTypeFlagBits(16)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP_BIT = VkExternalMemoryHandleTypeFlagBits(32)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE_BIT = VkExternalMemoryHandleTypeFlagBits(64)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_KMT_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_KMT_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE_BIT_KHR = VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE_BIT
VK_EXTERNAL_MEMORY_HANDLE_TYPE_DMA_BUF_BIT_EXT = VkExternalMemoryHandleTypeFlagBits(512)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_ANDROID_HARDWARE_BUFFER_BIT_ANDROID = VkExternalMemoryHandleTypeFlagBits(1024)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_HOST_ALLOCATION_BIT_EXT = VkExternalMemoryHandleTypeFlagBits(128)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_HOST_MAPPED_FOREIGN_MEMORY_BIT_EXT = VkExternalMemoryHandleTypeFlagBits(256)

VkExternalMemoryHandleTypeFlagBitsKHR = VkExternalMemoryHandleTypeFlagBits

VkExternalMemoryFeatureFlagBits = type('VkExternalMemoryFeatureFlagBits', (c_enum,), dict(names=dict()))
VkExternalMemoryFeatureFlagBits.names = {
    1 : 'VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT',
    2 : 'VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT',
    4 : 'VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT',
}
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT = VkExternalMemoryFeatureFlagBits(1)
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT = VkExternalMemoryFeatureFlagBits(2)
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT = VkExternalMemoryFeatureFlagBits(4)
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_KHR = VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_KHR = VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_KHR = VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT

VkExternalMemoryFeatureFlagBitsKHR = VkExternalMemoryFeatureFlagBits

VkExternalSemaphoreHandleTypeFlagBits = type('VkExternalSemaphoreHandleTypeFlagBits', (c_enum,), dict(names=dict()))
VkExternalSemaphoreHandleTypeFlagBits.names = {
    1 : 'VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT',
    2 : 'VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT',
    4 : 'VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT',
    8 : 'VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT',
    16 : 'VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_SYNC_FD_BIT',
}
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT = VkExternalSemaphoreHandleTypeFlagBits(1)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT = VkExternalSemaphoreHandleTypeFlagBits(2)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = VkExternalSemaphoreHandleTypeFlagBits(4)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT = VkExternalSemaphoreHandleTypeFlagBits(8)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_FENCE_BIT = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_SYNC_FD_BIT = VkExternalSemaphoreHandleTypeFlagBits(16)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT_KHR = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT_KHR = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_KHR = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT_KHR = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_SYNC_FD_BIT_KHR = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_SYNC_FD_BIT

VkExternalSemaphoreHandleTypeFlagBitsKHR = VkExternalSemaphoreHandleTypeFlagBits

VkExternalSemaphoreFeatureFlagBits = type('VkExternalSemaphoreFeatureFlagBits', (c_enum,), dict(names=dict()))
VkExternalSemaphoreFeatureFlagBits.names = {
    1 : 'VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT',
    2 : 'VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT',
}
VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT = VkExternalSemaphoreFeatureFlagBits(1)
VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT = VkExternalSemaphoreFeatureFlagBits(2)
VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT_KHR = VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT
VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT_KHR = VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT

VkExternalSemaphoreFeatureFlagBitsKHR = VkExternalSemaphoreFeatureFlagBits

VkSemaphoreImportFlagBits = type('VkSemaphoreImportFlagBits', (c_enum,), dict(names=dict()))
VkSemaphoreImportFlagBits.names = {
    1 : 'VK_SEMAPHORE_IMPORT_TEMPORARY_BIT',
}
VK_SEMAPHORE_IMPORT_TEMPORARY_BIT = VkSemaphoreImportFlagBits(1)
VK_SEMAPHORE_IMPORT_TEMPORARY_BIT_KHR = VK_SEMAPHORE_IMPORT_TEMPORARY_BIT

VkSemaphoreImportFlagBitsKHR = VkSemaphoreImportFlagBits

VkExternalFenceHandleTypeFlagBits = type('VkExternalFenceHandleTypeFlagBits', (c_enum,), dict(names=dict()))
VkExternalFenceHandleTypeFlagBits.names = {
    1 : 'VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT',
    2 : 'VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT',
    4 : 'VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT',
    8 : 'VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT',
}
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT = VkExternalFenceHandleTypeFlagBits(1)
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT = VkExternalFenceHandleTypeFlagBits(2)
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = VkExternalFenceHandleTypeFlagBits(4)
VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT = VkExternalFenceHandleTypeFlagBits(8)
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT_KHR = VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT_KHR = VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_KHR = VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT
VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT_KHR = VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT

VkExternalFenceHandleTypeFlagBitsKHR = VkExternalFenceHandleTypeFlagBits

VkExternalFenceFeatureFlagBits = type('VkExternalFenceFeatureFlagBits', (c_enum,), dict(names=dict()))
VkExternalFenceFeatureFlagBits.names = {
    1 : 'VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT',
    2 : 'VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT',
}
VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT = VkExternalFenceFeatureFlagBits(1)
VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT = VkExternalFenceFeatureFlagBits(2)
VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT_KHR = VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT
VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT_KHR = VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT

VkExternalFenceFeatureFlagBitsKHR = VkExternalFenceFeatureFlagBits

VkFenceImportFlagBits = type('VkFenceImportFlagBits', (c_enum,), dict(names=dict()))
VkFenceImportFlagBits.names = {
    1 : 'VK_FENCE_IMPORT_TEMPORARY_BIT',
}
VK_FENCE_IMPORT_TEMPORARY_BIT = VkFenceImportFlagBits(1)
VK_FENCE_IMPORT_TEMPORARY_BIT_KHR = VK_FENCE_IMPORT_TEMPORARY_BIT

VkFenceImportFlagBitsKHR = VkFenceImportFlagBits

VkSurfaceCounterFlagBitsEXT = type('VkSurfaceCounterFlagBitsEXT', (c_enum,), dict(names=dict()))
VkSurfaceCounterFlagBitsEXT.names = {
    1 : 'VK_SURFACE_COUNTER_VBLANK_BIT_EXT',
}
VK_SURFACE_COUNTER_VBLANK_BIT_EXT = VkSurfaceCounterFlagBitsEXT(1)
VK_SURFACE_COUNTER_VBLANK_EXT = VK_SURFACE_COUNTER_VBLANK_BIT_EXT

VkDisplayPowerStateEXT = type('VkDisplayPowerStateEXT', (c_enum,), dict(names=dict()))
VkDisplayPowerStateEXT.names = {
    0 : 'VK_DISPLAY_POWER_STATE_OFF_EXT',
    1 : 'VK_DISPLAY_POWER_STATE_SUSPEND_EXT',
    2 : 'VK_DISPLAY_POWER_STATE_ON_EXT',
}
VK_DISPLAY_POWER_STATE_OFF_EXT = VkDisplayPowerStateEXT(0)
VK_DISPLAY_POWER_STATE_SUSPEND_EXT = VkDisplayPowerStateEXT(1)
VK_DISPLAY_POWER_STATE_ON_EXT = VkDisplayPowerStateEXT(2)

VkDeviceEventTypeEXT = type('VkDeviceEventTypeEXT', (c_enum,), dict(names=dict()))
VkDeviceEventTypeEXT.names = {
    0 : 'VK_DEVICE_EVENT_TYPE_DISPLAY_HOTPLUG_EXT',
}
VK_DEVICE_EVENT_TYPE_DISPLAY_HOTPLUG_EXT = VkDeviceEventTypeEXT(0)

VkDisplayEventTypeEXT = type('VkDisplayEventTypeEXT', (c_enum,), dict(names=dict()))
VkDisplayEventTypeEXT.names = {
    0 : 'VK_DISPLAY_EVENT_TYPE_FIRST_PIXEL_OUT_EXT',
}
VK_DISPLAY_EVENT_TYPE_FIRST_PIXEL_OUT_EXT = VkDisplayEventTypeEXT(0)

VkPeerMemoryFeatureFlagBits = type('VkPeerMemoryFeatureFlagBits', (c_enum,), dict(names=dict()))
VkPeerMemoryFeatureFlagBits.names = {
    1 : 'VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT',
    2 : 'VK_PEER_MEMORY_FEATURE_COPY_DST_BIT',
    4 : 'VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT',
    8 : 'VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT',
}
VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT = VkPeerMemoryFeatureFlagBits(1)
VK_PEER_MEMORY_FEATURE_COPY_DST_BIT = VkPeerMemoryFeatureFlagBits(2)
VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT = VkPeerMemoryFeatureFlagBits(4)
VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT = VkPeerMemoryFeatureFlagBits(8)
VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT_KHR = VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT
VK_PEER_MEMORY_FEATURE_COPY_DST_BIT_KHR = VK_PEER_MEMORY_FEATURE_COPY_DST_BIT
VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT_KHR = VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT
VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT_KHR = VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT

VkPeerMemoryFeatureFlagBitsKHR = VkPeerMemoryFeatureFlagBits

VkMemoryAllocateFlagBits = type('VkMemoryAllocateFlagBits', (c_enum,), dict(names=dict()))
VkMemoryAllocateFlagBits.names = {
    1 : 'VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT',
    2 : 'VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_BIT',
    4 : 'VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT',
}
VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT = VkMemoryAllocateFlagBits(1)
VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_BIT = VkMemoryAllocateFlagBits(2)
VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT = VkMemoryAllocateFlagBits(4)
VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT_KHR = VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT
VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_BIT_KHR = VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_BIT
VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT

VkMemoryAllocateFlagBitsKHR = VkMemoryAllocateFlagBits

VkDeviceGroupPresentModeFlagBitsKHR = type('VkDeviceGroupPresentModeFlagBitsKHR', (c_enum,), dict(names=dict()))
VkDeviceGroupPresentModeFlagBitsKHR.names = {
    1 : 'VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_BIT_KHR',
    2 : 'VK_DEVICE_GROUP_PRESENT_MODE_REMOTE_BIT_KHR',
    4 : 'VK_DEVICE_GROUP_PRESENT_MODE_SUM_BIT_KHR',
    8 : 'VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_MULTI_DEVICE_BIT_KHR',
}
VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(1)
VK_DEVICE_GROUP_PRESENT_MODE_REMOTE_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(2)
VK_DEVICE_GROUP_PRESENT_MODE_SUM_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(4)
VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_MULTI_DEVICE_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(8)

VkSwapchainCreateFlagBitsKHR = type('VkSwapchainCreateFlagBitsKHR', (c_enum,), dict(names=dict()))
VkSwapchainCreateFlagBitsKHR.names = {
    1 : 'VK_SWAPCHAIN_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR',
    2 : 'VK_SWAPCHAIN_CREATE_PROTECTED_BIT_KHR',
    1 : 'VK_SWAPCHAIN_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR',
    4 : 'VK_SWAPCHAIN_CREATE_MUTABLE_FORMAT_BIT_KHR',
}
VK_SWAPCHAIN_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR = VkSwapchainCreateFlagBitsKHR(1)
VK_SWAPCHAIN_CREATE_PROTECTED_BIT_KHR = VkSwapchainCreateFlagBitsKHR(2)
VK_SWAPCHAIN_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR = VkSwapchainCreateFlagBitsKHR(1)
VK_SWAPCHAIN_CREATE_MUTABLE_FORMAT_BIT_KHR = VkSwapchainCreateFlagBitsKHR(4)

VkSubgroupFeatureFlagBits = type('VkSubgroupFeatureFlagBits', (c_enum,), dict(names=dict()))
VkSubgroupFeatureFlagBits.names = {
    1 : 'VK_SUBGROUP_FEATURE_BASIC_BIT',
    2 : 'VK_SUBGROUP_FEATURE_VOTE_BIT',
    4 : 'VK_SUBGROUP_FEATURE_ARITHMETIC_BIT',
    8 : 'VK_SUBGROUP_FEATURE_BALLOT_BIT',
    16 : 'VK_SUBGROUP_FEATURE_SHUFFLE_BIT',
    32 : 'VK_SUBGROUP_FEATURE_SHUFFLE_RELATIVE_BIT',
    64 : 'VK_SUBGROUP_FEATURE_CLUSTERED_BIT',
    128 : 'VK_SUBGROUP_FEATURE_QUAD_BIT',
    256 : 'VK_SUBGROUP_FEATURE_PARTITIONED_BIT_NV',
}
VK_SUBGROUP_FEATURE_BASIC_BIT = VkSubgroupFeatureFlagBits(1)
VK_SUBGROUP_FEATURE_VOTE_BIT = VkSubgroupFeatureFlagBits(2)
VK_SUBGROUP_FEATURE_ARITHMETIC_BIT = VkSubgroupFeatureFlagBits(4)
VK_SUBGROUP_FEATURE_BALLOT_BIT = VkSubgroupFeatureFlagBits(8)
VK_SUBGROUP_FEATURE_SHUFFLE_BIT = VkSubgroupFeatureFlagBits(16)
VK_SUBGROUP_FEATURE_SHUFFLE_RELATIVE_BIT = VkSubgroupFeatureFlagBits(32)
VK_SUBGROUP_FEATURE_CLUSTERED_BIT = VkSubgroupFeatureFlagBits(64)
VK_SUBGROUP_FEATURE_QUAD_BIT = VkSubgroupFeatureFlagBits(128)
VK_SUBGROUP_FEATURE_PARTITIONED_BIT_NV = VkSubgroupFeatureFlagBits(256)

VkTessellationDomainOrigin = type('VkTessellationDomainOrigin', (c_enum,), dict(names=dict()))
VkTessellationDomainOrigin.names = {
    0 : 'VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT',
    1 : 'VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT',
}
VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT = VkTessellationDomainOrigin(0)
VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT = VkTessellationDomainOrigin(1)
VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT_KHR = VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT
VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT_KHR = VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT

VkTessellationDomainOriginKHR = VkTessellationDomainOrigin

VkSamplerYcbcrModelConversion = type('VkSamplerYcbcrModelConversion', (c_enum,), dict(names=dict()))
VkSamplerYcbcrModelConversion.names = {
    0 : 'VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY',
    1 : 'VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY',
    2 : 'VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709',
    3 : 'VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601',
    4 : 'VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020',
}
VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY = VkSamplerYcbcrModelConversion(0)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY = VkSamplerYcbcrModelConversion(1)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709 = VkSamplerYcbcrModelConversion(2)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601 = VkSamplerYcbcrModelConversion(3)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020 = VkSamplerYcbcrModelConversion(4)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY_KHR = VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY_KHR = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709_KHR = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601_KHR = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020_KHR = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020

VkSamplerYcbcrModelConversionKHR = VkSamplerYcbcrModelConversion

VkSamplerYcbcrRange = type('VkSamplerYcbcrRange', (c_enum,), dict(names=dict()))
VkSamplerYcbcrRange.names = {
    0 : 'VK_SAMPLER_YCBCR_RANGE_ITU_FULL',
    1 : 'VK_SAMPLER_YCBCR_RANGE_ITU_NARROW',
}
VK_SAMPLER_YCBCR_RANGE_ITU_FULL = VkSamplerYcbcrRange(0)
VK_SAMPLER_YCBCR_RANGE_ITU_NARROW = VkSamplerYcbcrRange(1)
VK_SAMPLER_YCBCR_RANGE_ITU_FULL_KHR = VK_SAMPLER_YCBCR_RANGE_ITU_FULL
VK_SAMPLER_YCBCR_RANGE_ITU_NARROW_KHR = VK_SAMPLER_YCBCR_RANGE_ITU_NARROW

VkSamplerYcbcrRangeKHR = VkSamplerYcbcrRange

VkChromaLocation = type('VkChromaLocation', (c_enum,), dict(names=dict()))
VkChromaLocation.names = {
    0 : 'VK_CHROMA_LOCATION_COSITED_EVEN',
    1 : 'VK_CHROMA_LOCATION_MIDPOINT',
}
VK_CHROMA_LOCATION_COSITED_EVEN = VkChromaLocation(0)
VK_CHROMA_LOCATION_MIDPOINT = VkChromaLocation(1)
VK_CHROMA_LOCATION_COSITED_EVEN_KHR = VK_CHROMA_LOCATION_COSITED_EVEN
VK_CHROMA_LOCATION_MIDPOINT_KHR = VK_CHROMA_LOCATION_MIDPOINT

VkChromaLocationKHR = VkChromaLocation

VkSamplerReductionMode = type('VkSamplerReductionMode', (c_enum,), dict(names=dict()))
VkSamplerReductionMode.names = {
    0 : 'VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE',
    1 : 'VK_SAMPLER_REDUCTION_MODE_MIN',
    2 : 'VK_SAMPLER_REDUCTION_MODE_MAX',
}
VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE = VkSamplerReductionMode(0)
VK_SAMPLER_REDUCTION_MODE_MIN = VkSamplerReductionMode(1)
VK_SAMPLER_REDUCTION_MODE_MAX = VkSamplerReductionMode(2)
VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE_EXT = VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE
VK_SAMPLER_REDUCTION_MODE_MIN_EXT = VK_SAMPLER_REDUCTION_MODE_MIN
VK_SAMPLER_REDUCTION_MODE_MAX_EXT = VK_SAMPLER_REDUCTION_MODE_MAX

VkSamplerReductionModeEXT = VkSamplerReductionMode

VkBlendOverlapEXT = type('VkBlendOverlapEXT', (c_enum,), dict(names=dict()))
VkBlendOverlapEXT.names = {
    0 : 'VK_BLEND_OVERLAP_UNCORRELATED_EXT',
    1 : 'VK_BLEND_OVERLAP_DISJOINT_EXT',
    2 : 'VK_BLEND_OVERLAP_CONJOINT_EXT',
}
VK_BLEND_OVERLAP_UNCORRELATED_EXT = VkBlendOverlapEXT(0)
VK_BLEND_OVERLAP_DISJOINT_EXT = VkBlendOverlapEXT(1)
VK_BLEND_OVERLAP_CONJOINT_EXT = VkBlendOverlapEXT(2)

VkDebugUtilsMessageSeverityFlagBitsEXT = type('VkDebugUtilsMessageSeverityFlagBitsEXT', (c_enum,), dict(names=dict()))
VkDebugUtilsMessageSeverityFlagBitsEXT.names = {
    1 : 'VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT',
    16 : 'VK_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT',
    256 : 'VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT',
    4096 : 'VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT',
}
VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(1)
VK_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(16)
VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(256)
VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(4096)

VkDebugUtilsMessageTypeFlagBitsEXT = type('VkDebugUtilsMessageTypeFlagBitsEXT', (c_enum,), dict(names=dict()))
VkDebugUtilsMessageTypeFlagBitsEXT.names = {
    1 : 'VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT',
    2 : 'VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT',
    4 : 'VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT',
}
VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT = VkDebugUtilsMessageTypeFlagBitsEXT(1)
VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT = VkDebugUtilsMessageTypeFlagBitsEXT(2)
VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT = VkDebugUtilsMessageTypeFlagBitsEXT(4)

VkFullScreenExclusiveEXT = type('VkFullScreenExclusiveEXT', (c_enum,), dict(names=dict()))
VkFullScreenExclusiveEXT.names = {
    0 : 'VK_FULL_SCREEN_EXCLUSIVE_DEFAULT_EXT',
    1 : 'VK_FULL_SCREEN_EXCLUSIVE_ALLOWED_EXT',
    2 : 'VK_FULL_SCREEN_EXCLUSIVE_DISALLOWED_EXT',
    3 : 'VK_FULL_SCREEN_EXCLUSIVE_APPLICATION_CONTROLLED_EXT',
}
VK_FULL_SCREEN_EXCLUSIVE_DEFAULT_EXT = VkFullScreenExclusiveEXT(0)
VK_FULL_SCREEN_EXCLUSIVE_ALLOWED_EXT = VkFullScreenExclusiveEXT(1)
VK_FULL_SCREEN_EXCLUSIVE_DISALLOWED_EXT = VkFullScreenExclusiveEXT(2)
VK_FULL_SCREEN_EXCLUSIVE_APPLICATION_CONTROLLED_EXT = VkFullScreenExclusiveEXT(3)

VkShaderFloatControlsIndependence = type('VkShaderFloatControlsIndependence', (c_enum,), dict(names=dict()))
VkShaderFloatControlsIndependence.names = {
    0 : 'VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY',
    1 : 'VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL',
    2 : 'VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE',
}
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY = VkShaderFloatControlsIndependence(0)
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL = VkShaderFloatControlsIndependence(1)
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE = VkShaderFloatControlsIndependence(2)
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY_KHR = VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL_KHR = VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE_KHR = VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE

VkShaderFloatControlsIndependenceKHR = VkShaderFloatControlsIndependence

VkSwapchainImageUsageFlagBitsANDROID = type('VkSwapchainImageUsageFlagBitsANDROID', (c_enum,), dict(names=dict()))
VkSwapchainImageUsageFlagBitsANDROID.names = {
    1 : 'VK_SWAPCHAIN_IMAGE_USAGE_SHARED_BIT_ANDROID',
}
VK_SWAPCHAIN_IMAGE_USAGE_SHARED_BIT_ANDROID = VkSwapchainImageUsageFlagBitsANDROID(1)

VkFragmentShadingRateCombinerOpKHR = type('VkFragmentShadingRateCombinerOpKHR', (c_enum,), dict(names=dict()))
VkFragmentShadingRateCombinerOpKHR.names = {
    0 : 'VK_FRAGMENT_SHADING_RATE_COMBINER_OP_KEEP_KHR',
    1 : 'VK_FRAGMENT_SHADING_RATE_COMBINER_OP_REPLACE_KHR',
    2 : 'VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MIN_KHR',
    3 : 'VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR',
    4 : 'VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MUL_KHR',
}
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_KEEP_KHR = VkFragmentShadingRateCombinerOpKHR(0)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_REPLACE_KHR = VkFragmentShadingRateCombinerOpKHR(1)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MIN_KHR = VkFragmentShadingRateCombinerOpKHR(2)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR = VkFragmentShadingRateCombinerOpKHR(3)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MUL_KHR = VkFragmentShadingRateCombinerOpKHR(4)

VkVendorId = type('VkVendorId', (c_enum,), dict(names=dict()))
VkVendorId.names = {
    0x10001 : 'VK_VENDOR_ID_VIV',
    0x10002 : 'VK_VENDOR_ID_VSI',
    0x10003 : 'VK_VENDOR_ID_KAZAN',
    0x10004 : 'VK_VENDOR_ID_CODEPLAY',
    0x10005 : 'VK_VENDOR_ID_MESA',
}
VK_VENDOR_ID_VIV = VkVendorId(0x10001)
VK_VENDOR_ID_VSI = VkVendorId(0x10002)
VK_VENDOR_ID_KAZAN = VkVendorId(0x10003)
VK_VENDOR_ID_CODEPLAY = VkVendorId(0x10004)
VK_VENDOR_ID_MESA = VkVendorId(0x10005)

VkDriverId = type('VkDriverId', (c_enum,), dict(names=dict()))
VkDriverId.names = {
    1 : 'VK_DRIVER_ID_AMD_PROPRIETARY',
    2 : 'VK_DRIVER_ID_AMD_OPEN_SOURCE',
    3 : 'VK_DRIVER_ID_MESA_RADV',
    4 : 'VK_DRIVER_ID_NVIDIA_PROPRIETARY',
    5 : 'VK_DRIVER_ID_INTEL_PROPRIETARY_WINDOWS',
    6 : 'VK_DRIVER_ID_INTEL_OPEN_SOURCE_MESA',
    7 : 'VK_DRIVER_ID_IMAGINATION_PROPRIETARY',
    8 : 'VK_DRIVER_ID_QUALCOMM_PROPRIETARY',
    9 : 'VK_DRIVER_ID_ARM_PROPRIETARY',
    10 : 'VK_DRIVER_ID_GOOGLE_SWIFTSHADER',
    11 : 'VK_DRIVER_ID_GGP_PROPRIETARY',
    12 : 'VK_DRIVER_ID_BROADCOM_PROPRIETARY',
    13 : 'VK_DRIVER_ID_MESA_LLVMPIPE',
    14 : 'VK_DRIVER_ID_MOLTENVK',
}
VK_DRIVER_ID_AMD_PROPRIETARY = VkDriverId(1)
VK_DRIVER_ID_AMD_OPEN_SOURCE = VkDriverId(2)
VK_DRIVER_ID_MESA_RADV = VkDriverId(3)
VK_DRIVER_ID_NVIDIA_PROPRIETARY = VkDriverId(4)
VK_DRIVER_ID_INTEL_PROPRIETARY_WINDOWS = VkDriverId(5)
VK_DRIVER_ID_INTEL_OPEN_SOURCE_MESA = VkDriverId(6)
VK_DRIVER_ID_IMAGINATION_PROPRIETARY = VkDriverId(7)
VK_DRIVER_ID_QUALCOMM_PROPRIETARY = VkDriverId(8)
VK_DRIVER_ID_ARM_PROPRIETARY = VkDriverId(9)
VK_DRIVER_ID_GOOGLE_SWIFTSHADER = VkDriverId(10)
VK_DRIVER_ID_GGP_PROPRIETARY = VkDriverId(11)
VK_DRIVER_ID_BROADCOM_PROPRIETARY = VkDriverId(12)
VK_DRIVER_ID_MESA_LLVMPIPE = VkDriverId(13)
VK_DRIVER_ID_MOLTENVK = VkDriverId(14)
VK_DRIVER_ID_AMD_PROPRIETARY_KHR = VK_DRIVER_ID_AMD_PROPRIETARY
VK_DRIVER_ID_AMD_OPEN_SOURCE_KHR = VK_DRIVER_ID_AMD_OPEN_SOURCE
VK_DRIVER_ID_MESA_RADV_KHR = VK_DRIVER_ID_MESA_RADV
VK_DRIVER_ID_NVIDIA_PROPRIETARY_KHR = VK_DRIVER_ID_NVIDIA_PROPRIETARY
VK_DRIVER_ID_INTEL_PROPRIETARY_WINDOWS_KHR = VK_DRIVER_ID_INTEL_PROPRIETARY_WINDOWS
VK_DRIVER_ID_INTEL_OPEN_SOURCE_MESA_KHR = VK_DRIVER_ID_INTEL_OPEN_SOURCE_MESA
VK_DRIVER_ID_IMAGINATION_PROPRIETARY_KHR = VK_DRIVER_ID_IMAGINATION_PROPRIETARY
VK_DRIVER_ID_QUALCOMM_PROPRIETARY_KHR = VK_DRIVER_ID_QUALCOMM_PROPRIETARY
VK_DRIVER_ID_ARM_PROPRIETARY_KHR = VK_DRIVER_ID_ARM_PROPRIETARY
VK_DRIVER_ID_GOOGLE_SWIFTSHADER_KHR = VK_DRIVER_ID_GOOGLE_SWIFTSHADER
VK_DRIVER_ID_GGP_PROPRIETARY_KHR = VK_DRIVER_ID_GGP_PROPRIETARY
VK_DRIVER_ID_BROADCOM_PROPRIETARY_KHR = VK_DRIVER_ID_BROADCOM_PROPRIETARY

VkDriverIdKHR = VkDriverId

VkShadingRatePaletteEntryNV = type('VkShadingRatePaletteEntryNV', (c_enum,), dict(names=dict()))
VkShadingRatePaletteEntryNV.names = {
    0 : 'VK_SHADING_RATE_PALETTE_ENTRY_NO_INVOCATIONS_NV',
    1 : 'VK_SHADING_RATE_PALETTE_ENTRY_16_INVOCATIONS_PER_PIXEL_NV',
    2 : 'VK_SHADING_RATE_PALETTE_ENTRY_8_INVOCATIONS_PER_PIXEL_NV',
    3 : 'VK_SHADING_RATE_PALETTE_ENTRY_4_INVOCATIONS_PER_PIXEL_NV',
    4 : 'VK_SHADING_RATE_PALETTE_ENTRY_2_INVOCATIONS_PER_PIXEL_NV',
    5 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_PIXEL_NV',
    6 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X1_PIXELS_NV',
    7 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_1X2_PIXELS_NV',
    8 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X2_PIXELS_NV',
    9 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_4X2_PIXELS_NV',
    10 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X4_PIXELS_NV',
    11 : 'VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_4X4_PIXELS_NV',
}
VK_SHADING_RATE_PALETTE_ENTRY_NO_INVOCATIONS_NV = VkShadingRatePaletteEntryNV(0)
VK_SHADING_RATE_PALETTE_ENTRY_16_INVOCATIONS_PER_PIXEL_NV = VkShadingRatePaletteEntryNV(1)
VK_SHADING_RATE_PALETTE_ENTRY_8_INVOCATIONS_PER_PIXEL_NV = VkShadingRatePaletteEntryNV(2)
VK_SHADING_RATE_PALETTE_ENTRY_4_INVOCATIONS_PER_PIXEL_NV = VkShadingRatePaletteEntryNV(3)
VK_SHADING_RATE_PALETTE_ENTRY_2_INVOCATIONS_PER_PIXEL_NV = VkShadingRatePaletteEntryNV(4)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_PIXEL_NV = VkShadingRatePaletteEntryNV(5)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X1_PIXELS_NV = VkShadingRatePaletteEntryNV(6)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_1X2_PIXELS_NV = VkShadingRatePaletteEntryNV(7)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X2_PIXELS_NV = VkShadingRatePaletteEntryNV(8)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_4X2_PIXELS_NV = VkShadingRatePaletteEntryNV(9)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X4_PIXELS_NV = VkShadingRatePaletteEntryNV(10)
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_4X4_PIXELS_NV = VkShadingRatePaletteEntryNV(11)

VkCoarseSampleOrderTypeNV = type('VkCoarseSampleOrderTypeNV', (c_enum,), dict(names=dict()))
VkCoarseSampleOrderTypeNV.names = {
    0 : 'VK_COARSE_SAMPLE_ORDER_TYPE_DEFAULT_NV',
    1 : 'VK_COARSE_SAMPLE_ORDER_TYPE_CUSTOM_NV',
    2 : 'VK_COARSE_SAMPLE_ORDER_TYPE_PIXEL_MAJOR_NV',
    3 : 'VK_COARSE_SAMPLE_ORDER_TYPE_SAMPLE_MAJOR_NV',
}
VK_COARSE_SAMPLE_ORDER_TYPE_DEFAULT_NV = VkCoarseSampleOrderTypeNV(0)
VK_COARSE_SAMPLE_ORDER_TYPE_CUSTOM_NV = VkCoarseSampleOrderTypeNV(1)
VK_COARSE_SAMPLE_ORDER_TYPE_PIXEL_MAJOR_NV = VkCoarseSampleOrderTypeNV(2)
VK_COARSE_SAMPLE_ORDER_TYPE_SAMPLE_MAJOR_NV = VkCoarseSampleOrderTypeNV(3)

VkPipelineExecutableStatisticFormatKHR = type('VkPipelineExecutableStatisticFormatKHR', (c_enum,), dict(names=dict()))
VkPipelineExecutableStatisticFormatKHR.names = {
    0 : 'VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_BOOL32_KHR',
    1 : 'VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_INT64_KHR',
    2 : 'VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_UINT64_KHR',
    3 : 'VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_FLOAT64_KHR',
}
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_BOOL32_KHR = VkPipelineExecutableStatisticFormatKHR(0)
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_INT64_KHR = VkPipelineExecutableStatisticFormatKHR(1)
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_UINT64_KHR = VkPipelineExecutableStatisticFormatKHR(2)
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_FLOAT64_KHR = VkPipelineExecutableStatisticFormatKHR(3)

VkBaseOutStructure = type('VkBaseOutStructure', (ctypes.Structure,), dict())
VkBaseInStructure = type('VkBaseInStructure', (ctypes.Structure,), dict())
VkOffset2D = type('VkOffset2D', (ctypes.Structure,), dict())
VkOffset3D = type('VkOffset3D', (ctypes.Structure,), dict())
VkExtent2D = type('VkExtent2D', (ctypes.Structure,), dict())
VkExtent3D = type('VkExtent3D', (ctypes.Structure,), dict())
VkViewport = type('VkViewport', (ctypes.Structure,), dict())
VkRect2D = type('VkRect2D', (ctypes.Structure,), dict())
VkClearRect = type('VkClearRect', (ctypes.Structure,), dict())
VkComponentMapping = type('VkComponentMapping', (ctypes.Structure,), dict())
VkPhysicalDeviceLimits = type('VkPhysicalDeviceLimits', (ctypes.Structure,), dict())
VkPhysicalDeviceSparseProperties = type('VkPhysicalDeviceSparseProperties', (ctypes.Structure,), dict())
VkPhysicalDeviceProperties = type('VkPhysicalDeviceProperties', (ctypes.Structure,), dict())
VkExtensionProperties = type('VkExtensionProperties', (ctypes.Structure,), dict())
VkLayerProperties = type('VkLayerProperties', (ctypes.Structure,), dict())
VkApplicationInfo = type('VkApplicationInfo', (ctypes.Structure,), dict())
VkAllocationCallbacks = type('VkAllocationCallbacks', (ctypes.Structure,), dict())
VkDeviceQueueCreateInfo = type('VkDeviceQueueCreateInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceFeatures = type('VkPhysicalDeviceFeatures', (ctypes.Structure,), dict())
VkDeviceCreateInfo = type('VkDeviceCreateInfo', (ctypes.Structure,), dict())
VkInstanceCreateInfo = type('VkInstanceCreateInfo', (ctypes.Structure,), dict())
VkQueueFamilyProperties = type('VkQueueFamilyProperties', (ctypes.Structure,), dict())
VkMemoryType = type('VkMemoryType', (ctypes.Structure,), dict())
VkMemoryHeap = type('VkMemoryHeap', (ctypes.Structure,), dict())
VkPhysicalDeviceMemoryProperties = type('VkPhysicalDeviceMemoryProperties', (ctypes.Structure,), dict())
VkMemoryAllocateInfo = type('VkMemoryAllocateInfo', (ctypes.Structure,), dict())
VkMemoryRequirements = type('VkMemoryRequirements', (ctypes.Structure,), dict())
VkSparseImageFormatProperties = type('VkSparseImageFormatProperties', (ctypes.Structure,), dict())
VkSparseImageMemoryRequirements = type('VkSparseImageMemoryRequirements', (ctypes.Structure,), dict())
VkMappedMemoryRange = type('VkMappedMemoryRange', (ctypes.Structure,), dict())
VkFormatProperties = type('VkFormatProperties', (ctypes.Structure,), dict())
VkImageFormatProperties = type('VkImageFormatProperties', (ctypes.Structure,), dict())
VkDescriptorBufferInfo = type('VkDescriptorBufferInfo', (ctypes.Structure,), dict())
VkDescriptorImageInfo = type('VkDescriptorImageInfo', (ctypes.Structure,), dict())
VkWriteDescriptorSet = type('VkWriteDescriptorSet', (ctypes.Structure,), dict())
VkCopyDescriptorSet = type('VkCopyDescriptorSet', (ctypes.Structure,), dict())
VkBufferCreateInfo = type('VkBufferCreateInfo', (ctypes.Structure,), dict())
VkBufferViewCreateInfo = type('VkBufferViewCreateInfo', (ctypes.Structure,), dict())
VkImageSubresource = type('VkImageSubresource', (ctypes.Structure,), dict())
VkImageSubresourceLayers = type('VkImageSubresourceLayers', (ctypes.Structure,), dict())
VkImageSubresourceRange = type('VkImageSubresourceRange', (ctypes.Structure,), dict())
VkMemoryBarrier = type('VkMemoryBarrier', (ctypes.Structure,), dict())
VkBufferMemoryBarrier = type('VkBufferMemoryBarrier', (ctypes.Structure,), dict())
VkImageMemoryBarrier = type('VkImageMemoryBarrier', (ctypes.Structure,), dict())
VkImageCreateInfo = type('VkImageCreateInfo', (ctypes.Structure,), dict())
VkSubresourceLayout = type('VkSubresourceLayout', (ctypes.Structure,), dict())
VkImageViewCreateInfo = type('VkImageViewCreateInfo', (ctypes.Structure,), dict())
VkBufferCopy = type('VkBufferCopy', (ctypes.Structure,), dict())
VkSparseMemoryBind = type('VkSparseMemoryBind', (ctypes.Structure,), dict())
VkSparseImageMemoryBind = type('VkSparseImageMemoryBind', (ctypes.Structure,), dict())
VkSparseBufferMemoryBindInfo = type('VkSparseBufferMemoryBindInfo', (ctypes.Structure,), dict())
VkSparseImageOpaqueMemoryBindInfo = type('VkSparseImageOpaqueMemoryBindInfo', (ctypes.Structure,), dict())
VkSparseImageMemoryBindInfo = type('VkSparseImageMemoryBindInfo', (ctypes.Structure,), dict())
VkBindSparseInfo = type('VkBindSparseInfo', (ctypes.Structure,), dict())
VkImageCopy = type('VkImageCopy', (ctypes.Structure,), dict())
VkImageBlit = type('VkImageBlit', (ctypes.Structure,), dict())
VkBufferImageCopy = type('VkBufferImageCopy', (ctypes.Structure,), dict())
VkImageResolve = type('VkImageResolve', (ctypes.Structure,), dict())
VkShaderModuleCreateInfo = type('VkShaderModuleCreateInfo', (ctypes.Structure,), dict())
VkDescriptorSetLayoutBinding = type('VkDescriptorSetLayoutBinding', (ctypes.Structure,), dict())
VkDescriptorSetLayoutCreateInfo = type('VkDescriptorSetLayoutCreateInfo', (ctypes.Structure,), dict())
VkDescriptorPoolSize = type('VkDescriptorPoolSize', (ctypes.Structure,), dict())
VkDescriptorPoolCreateInfo = type('VkDescriptorPoolCreateInfo', (ctypes.Structure,), dict())
VkDescriptorSetAllocateInfo = type('VkDescriptorSetAllocateInfo', (ctypes.Structure,), dict())
VkSpecializationMapEntry = type('VkSpecializationMapEntry', (ctypes.Structure,), dict())
VkSpecializationInfo = type('VkSpecializationInfo', (ctypes.Structure,), dict())
VkPipelineShaderStageCreateInfo = type('VkPipelineShaderStageCreateInfo', (ctypes.Structure,), dict())
VkComputePipelineCreateInfo = type('VkComputePipelineCreateInfo', (ctypes.Structure,), dict())
VkVertexInputBindingDescription = type('VkVertexInputBindingDescription', (ctypes.Structure,), dict())
VkVertexInputAttributeDescription = type('VkVertexInputAttributeDescription', (ctypes.Structure,), dict())
VkPipelineVertexInputStateCreateInfo = type('VkPipelineVertexInputStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineInputAssemblyStateCreateInfo = type('VkPipelineInputAssemblyStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineTessellationStateCreateInfo = type('VkPipelineTessellationStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineViewportStateCreateInfo = type('VkPipelineViewportStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineRasterizationStateCreateInfo = type('VkPipelineRasterizationStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineMultisampleStateCreateInfo = type('VkPipelineMultisampleStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineColorBlendAttachmentState = type('VkPipelineColorBlendAttachmentState', (ctypes.Structure,), dict())
VkPipelineColorBlendStateCreateInfo = type('VkPipelineColorBlendStateCreateInfo', (ctypes.Structure,), dict())
VkPipelineDynamicStateCreateInfo = type('VkPipelineDynamicStateCreateInfo', (ctypes.Structure,), dict())
VkStencilOpState = type('VkStencilOpState', (ctypes.Structure,), dict())
VkPipelineDepthStencilStateCreateInfo = type('VkPipelineDepthStencilStateCreateInfo', (ctypes.Structure,), dict())
VkGraphicsPipelineCreateInfo = type('VkGraphicsPipelineCreateInfo', (ctypes.Structure,), dict())
VkPipelineCacheCreateInfo = type('VkPipelineCacheCreateInfo', (ctypes.Structure,), dict())
VkPushConstantRange = type('VkPushConstantRange', (ctypes.Structure,), dict())
VkPipelineLayoutCreateInfo = type('VkPipelineLayoutCreateInfo', (ctypes.Structure,), dict())
VkSamplerCreateInfo = type('VkSamplerCreateInfo', (ctypes.Structure,), dict())
VkCommandPoolCreateInfo = type('VkCommandPoolCreateInfo', (ctypes.Structure,), dict())
VkCommandBufferAllocateInfo = type('VkCommandBufferAllocateInfo', (ctypes.Structure,), dict())
VkCommandBufferInheritanceInfo = type('VkCommandBufferInheritanceInfo', (ctypes.Structure,), dict())
VkCommandBufferBeginInfo = type('VkCommandBufferBeginInfo', (ctypes.Structure,), dict())
VkClearColorValue = type('VkClearColorValue', (ctypes.Union,), dict())
VkClearDepthStencilValue = type('VkClearDepthStencilValue', (ctypes.Structure,), dict())
VkClearValue = type('VkClearValue', (ctypes.Union,), dict())
VkRenderPassBeginInfo = type('VkRenderPassBeginInfo', (ctypes.Structure,), dict())
VkClearAttachment = type('VkClearAttachment', (ctypes.Structure,), dict())
VkAttachmentDescription = type('VkAttachmentDescription', (ctypes.Structure,), dict())
VkAttachmentReference = type('VkAttachmentReference', (ctypes.Structure,), dict())
VkSubpassDescription = type('VkSubpassDescription', (ctypes.Structure,), dict())
VkSubpassDependency = type('VkSubpassDependency', (ctypes.Structure,), dict())
VkRenderPassCreateInfo = type('VkRenderPassCreateInfo', (ctypes.Structure,), dict())
VkEventCreateInfo = type('VkEventCreateInfo', (ctypes.Structure,), dict())
VkFenceCreateInfo = type('VkFenceCreateInfo', (ctypes.Structure,), dict())
VkSemaphoreCreateInfo = type('VkSemaphoreCreateInfo', (ctypes.Structure,), dict())
VkQueryPoolCreateInfo = type('VkQueryPoolCreateInfo', (ctypes.Structure,), dict())
VkFramebufferCreateInfo = type('VkFramebufferCreateInfo', (ctypes.Structure,), dict())
VkDrawIndirectCommand = type('VkDrawIndirectCommand', (ctypes.Structure,), dict())
VkDrawIndexedIndirectCommand = type('VkDrawIndexedIndirectCommand', (ctypes.Structure,), dict())
VkDispatchIndirectCommand = type('VkDispatchIndirectCommand', (ctypes.Structure,), dict())
VkSubmitInfo = type('VkSubmitInfo', (ctypes.Structure,), dict())
VkDisplayPropertiesKHR = type('VkDisplayPropertiesKHR', (ctypes.Structure,), dict())
VkDisplayPlanePropertiesKHR = type('VkDisplayPlanePropertiesKHR', (ctypes.Structure,), dict())
VkDisplayModeParametersKHR = type('VkDisplayModeParametersKHR', (ctypes.Structure,), dict())
VkDisplayModePropertiesKHR = type('VkDisplayModePropertiesKHR', (ctypes.Structure,), dict())
VkDisplayModeCreateInfoKHR = type('VkDisplayModeCreateInfoKHR', (ctypes.Structure,), dict())
VkDisplayPlaneCapabilitiesKHR = type('VkDisplayPlaneCapabilitiesKHR', (ctypes.Structure,), dict())
VkDisplaySurfaceCreateInfoKHR = type('VkDisplaySurfaceCreateInfoKHR', (ctypes.Structure,), dict())
VkDisplayPresentInfoKHR = type('VkDisplayPresentInfoKHR', (ctypes.Structure,), dict())
VkSurfaceCapabilitiesKHR = type('VkSurfaceCapabilitiesKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidSurfaceCreateInfoKHR = type('VkAndroidSurfaceCreateInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_VI_NN:
    VkViSurfaceCreateInfoNN = type('VkViSurfaceCreateInfoNN', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WAYLAND_KHR:
    VkWaylandSurfaceCreateInfoKHR = type('VkWaylandSurfaceCreateInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkWin32SurfaceCreateInfoKHR = type('VkWin32SurfaceCreateInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_XLIB_KHR:
    VkXlibSurfaceCreateInfoKHR = type('VkXlibSurfaceCreateInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_XCB_KHR:
    VkXcbSurfaceCreateInfoKHR = type('VkXcbSurfaceCreateInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_DIRECTFB_EXT:
    VkDirectFBSurfaceCreateInfoEXT = type('VkDirectFBSurfaceCreateInfoEXT', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_FUCHSIA:
    VkImagePipeSurfaceCreateInfoFUCHSIA = type('VkImagePipeSurfaceCreateInfoFUCHSIA', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_GGP:
    VkStreamDescriptorSurfaceCreateInfoGGP = type('VkStreamDescriptorSurfaceCreateInfoGGP', (ctypes.Structure,), dict())
VkSurfaceFormatKHR = type('VkSurfaceFormatKHR', (ctypes.Structure,), dict())
VkSwapchainCreateInfoKHR = type('VkSwapchainCreateInfoKHR', (ctypes.Structure,), dict())
VkPresentInfoKHR = type('VkPresentInfoKHR', (ctypes.Structure,), dict())
VkDebugReportCallbackCreateInfoEXT = type('VkDebugReportCallbackCreateInfoEXT', (ctypes.Structure,), dict())
VkValidationFlagsEXT = type('VkValidationFlagsEXT', (ctypes.Structure,), dict())
VkValidationFeaturesEXT = type('VkValidationFeaturesEXT', (ctypes.Structure,), dict())
VkPipelineRasterizationStateRasterizationOrderAMD = type('VkPipelineRasterizationStateRasterizationOrderAMD', (ctypes.Structure,), dict())
VkDebugMarkerObjectNameInfoEXT = type('VkDebugMarkerObjectNameInfoEXT', (ctypes.Structure,), dict())
VkDebugMarkerObjectTagInfoEXT = type('VkDebugMarkerObjectTagInfoEXT', (ctypes.Structure,), dict())
VkDebugMarkerMarkerInfoEXT = type('VkDebugMarkerMarkerInfoEXT', (ctypes.Structure,), dict())
VkDedicatedAllocationImageCreateInfoNV = type('VkDedicatedAllocationImageCreateInfoNV', (ctypes.Structure,), dict())
VkDedicatedAllocationBufferCreateInfoNV = type('VkDedicatedAllocationBufferCreateInfoNV', (ctypes.Structure,), dict())
VkDedicatedAllocationMemoryAllocateInfoNV = type('VkDedicatedAllocationMemoryAllocateInfoNV', (ctypes.Structure,), dict())
VkExternalImageFormatPropertiesNV = type('VkExternalImageFormatPropertiesNV', (ctypes.Structure,), dict())
VkExternalMemoryImageCreateInfoNV = type('VkExternalMemoryImageCreateInfoNV', (ctypes.Structure,), dict())
VkExportMemoryAllocateInfoNV = type('VkExportMemoryAllocateInfoNV', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportMemoryWin32HandleInfoNV = type('VkImportMemoryWin32HandleInfoNV', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportMemoryWin32HandleInfoNV = type('VkExportMemoryWin32HandleInfoNV', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkWin32KeyedMutexAcquireReleaseInfoNV = type('VkWin32KeyedMutexAcquireReleaseInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV = type('VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV', (ctypes.Structure,), dict())
VkDevicePrivateDataCreateInfoEXT = type('VkDevicePrivateDataCreateInfoEXT', (ctypes.Structure,), dict())
VkPrivateDataSlotCreateInfoEXT = type('VkPrivateDataSlotCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDevicePrivateDataFeaturesEXT = type('VkPhysicalDevicePrivateDataFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV = type('VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV', (ctypes.Structure,), dict())
VkGraphicsShaderGroupCreateInfoNV = type('VkGraphicsShaderGroupCreateInfoNV', (ctypes.Structure,), dict())
VkGraphicsPipelineShaderGroupsCreateInfoNV = type('VkGraphicsPipelineShaderGroupsCreateInfoNV', (ctypes.Structure,), dict())
VkBindShaderGroupIndirectCommandNV = type('VkBindShaderGroupIndirectCommandNV', (ctypes.Structure,), dict())
VkBindIndexBufferIndirectCommandNV = type('VkBindIndexBufferIndirectCommandNV', (ctypes.Structure,), dict())
VkBindVertexBufferIndirectCommandNV = type('VkBindVertexBufferIndirectCommandNV', (ctypes.Structure,), dict())
VkSetStateFlagsIndirectCommandNV = type('VkSetStateFlagsIndirectCommandNV', (ctypes.Structure,), dict())
VkIndirectCommandsStreamNV = type('VkIndirectCommandsStreamNV', (ctypes.Structure,), dict())
VkIndirectCommandsLayoutTokenNV = type('VkIndirectCommandsLayoutTokenNV', (ctypes.Structure,), dict())
VkIndirectCommandsLayoutCreateInfoNV = type('VkIndirectCommandsLayoutCreateInfoNV', (ctypes.Structure,), dict())
VkGeneratedCommandsInfoNV = type('VkGeneratedCommandsInfoNV', (ctypes.Structure,), dict())
VkGeneratedCommandsMemoryRequirementsInfoNV = type('VkGeneratedCommandsMemoryRequirementsInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceFeatures2 = type('VkPhysicalDeviceFeatures2', (ctypes.Structure,), dict())
VkPhysicalDeviceProperties2 = type('VkPhysicalDeviceProperties2', (ctypes.Structure,), dict())
VkFormatProperties2 = type('VkFormatProperties2', (ctypes.Structure,), dict())
VkImageFormatProperties2 = type('VkImageFormatProperties2', (ctypes.Structure,), dict())
VkPhysicalDeviceImageFormatInfo2 = type('VkPhysicalDeviceImageFormatInfo2', (ctypes.Structure,), dict())
VkQueueFamilyProperties2 = type('VkQueueFamilyProperties2', (ctypes.Structure,), dict())
VkPhysicalDeviceMemoryProperties2 = type('VkPhysicalDeviceMemoryProperties2', (ctypes.Structure,), dict())
VkSparseImageFormatProperties2 = type('VkSparseImageFormatProperties2', (ctypes.Structure,), dict())
VkPhysicalDeviceSparseImageFormatInfo2 = type('VkPhysicalDeviceSparseImageFormatInfo2', (ctypes.Structure,), dict())
VkPhysicalDevicePushDescriptorPropertiesKHR = type('VkPhysicalDevicePushDescriptorPropertiesKHR', (ctypes.Structure,), dict())
VkConformanceVersion = type('VkConformanceVersion', (ctypes.Structure,), dict())
VkPhysicalDeviceDriverProperties = type('VkPhysicalDeviceDriverProperties', (ctypes.Structure,), dict())
VkRectLayerKHR = type('VkRectLayerKHR', (ctypes.Structure,), dict())
VkPresentRegionKHR = type('VkPresentRegionKHR', (ctypes.Structure,), dict())
VkPresentRegionsKHR = type('VkPresentRegionsKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceVariablePointersFeatures = type('VkPhysicalDeviceVariablePointersFeatures', (ctypes.Structure,), dict())
VkExternalMemoryProperties = type('VkExternalMemoryProperties', (ctypes.Structure,), dict())
VkPhysicalDeviceExternalImageFormatInfo = type('VkPhysicalDeviceExternalImageFormatInfo', (ctypes.Structure,), dict())
VkExternalImageFormatProperties = type('VkExternalImageFormatProperties', (ctypes.Structure,), dict())
VkPhysicalDeviceExternalBufferInfo = type('VkPhysicalDeviceExternalBufferInfo', (ctypes.Structure,), dict())
VkExternalBufferProperties = type('VkExternalBufferProperties', (ctypes.Structure,), dict())
VkPhysicalDeviceIDProperties = type('VkPhysicalDeviceIDProperties', (ctypes.Structure,), dict())
VkExternalMemoryImageCreateInfo = type('VkExternalMemoryImageCreateInfo', (ctypes.Structure,), dict())
VkExternalMemoryBufferCreateInfo = type('VkExternalMemoryBufferCreateInfo', (ctypes.Structure,), dict())
VkExportMemoryAllocateInfo = type('VkExportMemoryAllocateInfo', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportMemoryWin32HandleInfoKHR = type('VkImportMemoryWin32HandleInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportMemoryWin32HandleInfoKHR = type('VkExportMemoryWin32HandleInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkMemoryWin32HandlePropertiesKHR = type('VkMemoryWin32HandlePropertiesKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkMemoryGetWin32HandleInfoKHR = type('VkMemoryGetWin32HandleInfoKHR', (ctypes.Structure,), dict())
VkImportMemoryFdInfoKHR = type('VkImportMemoryFdInfoKHR', (ctypes.Structure,), dict())
VkMemoryFdPropertiesKHR = type('VkMemoryFdPropertiesKHR', (ctypes.Structure,), dict())
VkMemoryGetFdInfoKHR = type('VkMemoryGetFdInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkWin32KeyedMutexAcquireReleaseInfoKHR = type('VkWin32KeyedMutexAcquireReleaseInfoKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceExternalSemaphoreInfo = type('VkPhysicalDeviceExternalSemaphoreInfo', (ctypes.Structure,), dict())
VkExternalSemaphoreProperties = type('VkExternalSemaphoreProperties', (ctypes.Structure,), dict())
VkExportSemaphoreCreateInfo = type('VkExportSemaphoreCreateInfo', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportSemaphoreWin32HandleInfoKHR = type('VkImportSemaphoreWin32HandleInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportSemaphoreWin32HandleInfoKHR = type('VkExportSemaphoreWin32HandleInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkD3D12FenceSubmitInfoKHR = type('VkD3D12FenceSubmitInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkSemaphoreGetWin32HandleInfoKHR = type('VkSemaphoreGetWin32HandleInfoKHR', (ctypes.Structure,), dict())
VkImportSemaphoreFdInfoKHR = type('VkImportSemaphoreFdInfoKHR', (ctypes.Structure,), dict())
VkSemaphoreGetFdInfoKHR = type('VkSemaphoreGetFdInfoKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceExternalFenceInfo = type('VkPhysicalDeviceExternalFenceInfo', (ctypes.Structure,), dict())
VkExternalFenceProperties = type('VkExternalFenceProperties', (ctypes.Structure,), dict())
VkExportFenceCreateInfo = type('VkExportFenceCreateInfo', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportFenceWin32HandleInfoKHR = type('VkImportFenceWin32HandleInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportFenceWin32HandleInfoKHR = type('VkExportFenceWin32HandleInfoKHR', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkFenceGetWin32HandleInfoKHR = type('VkFenceGetWin32HandleInfoKHR', (ctypes.Structure,), dict())
VkImportFenceFdInfoKHR = type('VkImportFenceFdInfoKHR', (ctypes.Structure,), dict())
VkFenceGetFdInfoKHR = type('VkFenceGetFdInfoKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceMultiviewFeatures = type('VkPhysicalDeviceMultiviewFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceMultiviewProperties = type('VkPhysicalDeviceMultiviewProperties', (ctypes.Structure,), dict())
VkRenderPassMultiviewCreateInfo = type('VkRenderPassMultiviewCreateInfo', (ctypes.Structure,), dict())
VkSurfaceCapabilities2EXT = type('VkSurfaceCapabilities2EXT', (ctypes.Structure,), dict())
VkDisplayPowerInfoEXT = type('VkDisplayPowerInfoEXT', (ctypes.Structure,), dict())
VkDeviceEventInfoEXT = type('VkDeviceEventInfoEXT', (ctypes.Structure,), dict())
VkDisplayEventInfoEXT = type('VkDisplayEventInfoEXT', (ctypes.Structure,), dict())
VkSwapchainCounterCreateInfoEXT = type('VkSwapchainCounterCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceGroupProperties = type('VkPhysicalDeviceGroupProperties', (ctypes.Structure,), dict())
VkMemoryAllocateFlagsInfo = type('VkMemoryAllocateFlagsInfo', (ctypes.Structure,), dict())
VkBindBufferMemoryInfo = type('VkBindBufferMemoryInfo', (ctypes.Structure,), dict())
VkBindBufferMemoryDeviceGroupInfo = type('VkBindBufferMemoryDeviceGroupInfo', (ctypes.Structure,), dict())
VkBindImageMemoryInfo = type('VkBindImageMemoryInfo', (ctypes.Structure,), dict())
VkBindImageMemoryDeviceGroupInfo = type('VkBindImageMemoryDeviceGroupInfo', (ctypes.Structure,), dict())
VkDeviceGroupRenderPassBeginInfo = type('VkDeviceGroupRenderPassBeginInfo', (ctypes.Structure,), dict())
VkDeviceGroupCommandBufferBeginInfo = type('VkDeviceGroupCommandBufferBeginInfo', (ctypes.Structure,), dict())
VkDeviceGroupSubmitInfo = type('VkDeviceGroupSubmitInfo', (ctypes.Structure,), dict())
VkDeviceGroupBindSparseInfo = type('VkDeviceGroupBindSparseInfo', (ctypes.Structure,), dict())
VkDeviceGroupPresentCapabilitiesKHR = type('VkDeviceGroupPresentCapabilitiesKHR', (ctypes.Structure,), dict())
VkImageSwapchainCreateInfoKHR = type('VkImageSwapchainCreateInfoKHR', (ctypes.Structure,), dict())
VkBindImageMemorySwapchainInfoKHR = type('VkBindImageMemorySwapchainInfoKHR', (ctypes.Structure,), dict())
VkAcquireNextImageInfoKHR = type('VkAcquireNextImageInfoKHR', (ctypes.Structure,), dict())
VkDeviceGroupPresentInfoKHR = type('VkDeviceGroupPresentInfoKHR', (ctypes.Structure,), dict())
VkDeviceGroupDeviceCreateInfo = type('VkDeviceGroupDeviceCreateInfo', (ctypes.Structure,), dict())
VkDeviceGroupSwapchainCreateInfoKHR = type('VkDeviceGroupSwapchainCreateInfoKHR', (ctypes.Structure,), dict())
VkDescriptorUpdateTemplateEntry = type('VkDescriptorUpdateTemplateEntry', (ctypes.Structure,), dict())
VkDescriptorUpdateTemplateCreateInfo = type('VkDescriptorUpdateTemplateCreateInfo', (ctypes.Structure,), dict())
VkXYColorEXT = type('VkXYColorEXT', (ctypes.Structure,), dict())
VkHdrMetadataEXT = type('VkHdrMetadataEXT', (ctypes.Structure,), dict())
VkDisplayNativeHdrSurfaceCapabilitiesAMD = type('VkDisplayNativeHdrSurfaceCapabilitiesAMD', (ctypes.Structure,), dict())
VkSwapchainDisplayNativeHdrCreateInfoAMD = type('VkSwapchainDisplayNativeHdrCreateInfoAMD', (ctypes.Structure,), dict())
VkRefreshCycleDurationGOOGLE = type('VkRefreshCycleDurationGOOGLE', (ctypes.Structure,), dict())
VkPastPresentationTimingGOOGLE = type('VkPastPresentationTimingGOOGLE', (ctypes.Structure,), dict())
VkPresentTimeGOOGLE = type('VkPresentTimeGOOGLE', (ctypes.Structure,), dict())
VkPresentTimesInfoGOOGLE = type('VkPresentTimesInfoGOOGLE', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_IOS_MVK:
    VkIOSSurfaceCreateInfoMVK = type('VkIOSSurfaceCreateInfoMVK', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_MACOS_MVK:
    VkMacOSSurfaceCreateInfoMVK = type('VkMacOSSurfaceCreateInfoMVK', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_METAL_EXT:
    VkMetalSurfaceCreateInfoEXT = type('VkMetalSurfaceCreateInfoEXT', (ctypes.Structure,), dict())
VkViewportWScalingNV = type('VkViewportWScalingNV', (ctypes.Structure,), dict())
VkPipelineViewportWScalingStateCreateInfoNV = type('VkPipelineViewportWScalingStateCreateInfoNV', (ctypes.Structure,), dict())
VkViewportSwizzleNV = type('VkViewportSwizzleNV', (ctypes.Structure,), dict())
VkPipelineViewportSwizzleStateCreateInfoNV = type('VkPipelineViewportSwizzleStateCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceDiscardRectanglePropertiesEXT = type('VkPhysicalDeviceDiscardRectanglePropertiesEXT', (ctypes.Structure,), dict())
VkPipelineDiscardRectangleStateCreateInfoEXT = type('VkPipelineDiscardRectangleStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX = type('VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX', (ctypes.Structure,), dict())
VkInputAttachmentAspectReference = type('VkInputAttachmentAspectReference', (ctypes.Structure,), dict())
VkRenderPassInputAttachmentAspectCreateInfo = type('VkRenderPassInputAttachmentAspectCreateInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceSurfaceInfo2KHR = type('VkPhysicalDeviceSurfaceInfo2KHR', (ctypes.Structure,), dict())
VkSurfaceCapabilities2KHR = type('VkSurfaceCapabilities2KHR', (ctypes.Structure,), dict())
VkSurfaceFormat2KHR = type('VkSurfaceFormat2KHR', (ctypes.Structure,), dict())
VkDisplayProperties2KHR = type('VkDisplayProperties2KHR', (ctypes.Structure,), dict())
VkDisplayPlaneProperties2KHR = type('VkDisplayPlaneProperties2KHR', (ctypes.Structure,), dict())
VkDisplayModeProperties2KHR = type('VkDisplayModeProperties2KHR', (ctypes.Structure,), dict())
VkDisplayPlaneInfo2KHR = type('VkDisplayPlaneInfo2KHR', (ctypes.Structure,), dict())
VkDisplayPlaneCapabilities2KHR = type('VkDisplayPlaneCapabilities2KHR', (ctypes.Structure,), dict())
VkSharedPresentSurfaceCapabilitiesKHR = type('VkSharedPresentSurfaceCapabilitiesKHR', (ctypes.Structure,), dict())
VkPhysicalDevice16BitStorageFeatures = type('VkPhysicalDevice16BitStorageFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceSubgroupProperties = type('VkPhysicalDeviceSubgroupProperties', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures = type('VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures', (ctypes.Structure,), dict())
VkBufferMemoryRequirementsInfo2 = type('VkBufferMemoryRequirementsInfo2', (ctypes.Structure,), dict())
VkImageMemoryRequirementsInfo2 = type('VkImageMemoryRequirementsInfo2', (ctypes.Structure,), dict())
VkImageSparseMemoryRequirementsInfo2 = type('VkImageSparseMemoryRequirementsInfo2', (ctypes.Structure,), dict())
VkMemoryRequirements2 = type('VkMemoryRequirements2', (ctypes.Structure,), dict())
VkSparseImageMemoryRequirements2 = type('VkSparseImageMemoryRequirements2', (ctypes.Structure,), dict())
VkPhysicalDevicePointClippingProperties = type('VkPhysicalDevicePointClippingProperties', (ctypes.Structure,), dict())
VkMemoryDedicatedRequirements = type('VkMemoryDedicatedRequirements', (ctypes.Structure,), dict())
VkMemoryDedicatedAllocateInfo = type('VkMemoryDedicatedAllocateInfo', (ctypes.Structure,), dict())
VkImageViewUsageCreateInfo = type('VkImageViewUsageCreateInfo', (ctypes.Structure,), dict())
VkPipelineTessellationDomainOriginStateCreateInfo = type('VkPipelineTessellationDomainOriginStateCreateInfo', (ctypes.Structure,), dict())
VkSamplerYcbcrConversionInfo = type('VkSamplerYcbcrConversionInfo', (ctypes.Structure,), dict())
VkSamplerYcbcrConversionCreateInfo = type('VkSamplerYcbcrConversionCreateInfo', (ctypes.Structure,), dict())
VkBindImagePlaneMemoryInfo = type('VkBindImagePlaneMemoryInfo', (ctypes.Structure,), dict())
VkImagePlaneMemoryRequirementsInfo = type('VkImagePlaneMemoryRequirementsInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceSamplerYcbcrConversionFeatures = type('VkPhysicalDeviceSamplerYcbcrConversionFeatures', (ctypes.Structure,), dict())
VkSamplerYcbcrConversionImageFormatProperties = type('VkSamplerYcbcrConversionImageFormatProperties', (ctypes.Structure,), dict())
VkTextureLODGatherFormatPropertiesAMD = type('VkTextureLODGatherFormatPropertiesAMD', (ctypes.Structure,), dict())
VkConditionalRenderingBeginInfoEXT = type('VkConditionalRenderingBeginInfoEXT', (ctypes.Structure,), dict())
VkProtectedSubmitInfo = type('VkProtectedSubmitInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceProtectedMemoryFeatures = type('VkPhysicalDeviceProtectedMemoryFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceProtectedMemoryProperties = type('VkPhysicalDeviceProtectedMemoryProperties', (ctypes.Structure,), dict())
VkDeviceQueueInfo2 = type('VkDeviceQueueInfo2', (ctypes.Structure,), dict())
VkPipelineCoverageToColorStateCreateInfoNV = type('VkPipelineCoverageToColorStateCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceSamplerFilterMinmaxProperties = type('VkPhysicalDeviceSamplerFilterMinmaxProperties', (ctypes.Structure,), dict())
VkSampleLocationEXT = type('VkSampleLocationEXT', (ctypes.Structure,), dict())
VkSampleLocationsInfoEXT = type('VkSampleLocationsInfoEXT', (ctypes.Structure,), dict())
VkAttachmentSampleLocationsEXT = type('VkAttachmentSampleLocationsEXT', (ctypes.Structure,), dict())
VkSubpassSampleLocationsEXT = type('VkSubpassSampleLocationsEXT', (ctypes.Structure,), dict())
VkRenderPassSampleLocationsBeginInfoEXT = type('VkRenderPassSampleLocationsBeginInfoEXT', (ctypes.Structure,), dict())
VkPipelineSampleLocationsStateCreateInfoEXT = type('VkPipelineSampleLocationsStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceSampleLocationsPropertiesEXT = type('VkPhysicalDeviceSampleLocationsPropertiesEXT', (ctypes.Structure,), dict())
VkMultisamplePropertiesEXT = type('VkMultisamplePropertiesEXT', (ctypes.Structure,), dict())
VkSamplerReductionModeCreateInfo = type('VkSamplerReductionModeCreateInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT = type('VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT = type('VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT', (ctypes.Structure,), dict())
VkPipelineColorBlendAdvancedStateCreateInfoEXT = type('VkPipelineColorBlendAdvancedStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceInlineUniformBlockFeaturesEXT = type('VkPhysicalDeviceInlineUniformBlockFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceInlineUniformBlockPropertiesEXT = type('VkPhysicalDeviceInlineUniformBlockPropertiesEXT', (ctypes.Structure,), dict())
VkWriteDescriptorSetInlineUniformBlockEXT = type('VkWriteDescriptorSetInlineUniformBlockEXT', (ctypes.Structure,), dict())
VkDescriptorPoolInlineUniformBlockCreateInfoEXT = type('VkDescriptorPoolInlineUniformBlockCreateInfoEXT', (ctypes.Structure,), dict())
VkPipelineCoverageModulationStateCreateInfoNV = type('VkPipelineCoverageModulationStateCreateInfoNV', (ctypes.Structure,), dict())
VkImageFormatListCreateInfo = type('VkImageFormatListCreateInfo', (ctypes.Structure,), dict())
VkValidationCacheCreateInfoEXT = type('VkValidationCacheCreateInfoEXT', (ctypes.Structure,), dict())
VkShaderModuleValidationCacheCreateInfoEXT = type('VkShaderModuleValidationCacheCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceMaintenance3Properties = type('VkPhysicalDeviceMaintenance3Properties', (ctypes.Structure,), dict())
VkDescriptorSetLayoutSupport = type('VkDescriptorSetLayoutSupport', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderDrawParametersFeatures = type('VkPhysicalDeviceShaderDrawParametersFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderFloat16Int8Features = type('VkPhysicalDeviceShaderFloat16Int8Features', (ctypes.Structure,), dict())
VkPhysicalDeviceFloatControlsProperties = type('VkPhysicalDeviceFloatControlsProperties', (ctypes.Structure,), dict())
VkPhysicalDeviceHostQueryResetFeatures = type('VkPhysicalDeviceHostQueryResetFeatures', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkNativeBufferUsage2ANDROID = type('VkNativeBufferUsage2ANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkNativeBufferANDROID = type('VkNativeBufferANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkSwapchainImageCreateInfoANDROID = type('VkSwapchainImageCreateInfoANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkPhysicalDevicePresentationPropertiesANDROID = type('VkPhysicalDevicePresentationPropertiesANDROID', (ctypes.Structure,), dict())
VkShaderResourceUsageAMD = type('VkShaderResourceUsageAMD', (ctypes.Structure,), dict())
VkShaderStatisticsInfoAMD = type('VkShaderStatisticsInfoAMD', (ctypes.Structure,), dict())
VkDeviceQueueGlobalPriorityCreateInfoEXT = type('VkDeviceQueueGlobalPriorityCreateInfoEXT', (ctypes.Structure,), dict())
VkDebugUtilsObjectNameInfoEXT = type('VkDebugUtilsObjectNameInfoEXT', (ctypes.Structure,), dict())
VkDebugUtilsObjectTagInfoEXT = type('VkDebugUtilsObjectTagInfoEXT', (ctypes.Structure,), dict())
VkDebugUtilsLabelEXT = type('VkDebugUtilsLabelEXT', (ctypes.Structure,), dict())
VkDebugUtilsMessengerCreateInfoEXT = type('VkDebugUtilsMessengerCreateInfoEXT', (ctypes.Structure,), dict())
VkDebugUtilsMessengerCallbackDataEXT = type('VkDebugUtilsMessengerCallbackDataEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceDeviceMemoryReportFeaturesEXT = type('VkPhysicalDeviceDeviceMemoryReportFeaturesEXT', (ctypes.Structure,), dict())
VkDeviceDeviceMemoryReportCreateInfoEXT = type('VkDeviceDeviceMemoryReportCreateInfoEXT', (ctypes.Structure,), dict())
VkDeviceMemoryReportCallbackDataEXT = type('VkDeviceMemoryReportCallbackDataEXT', (ctypes.Structure,), dict())
VkImportMemoryHostPointerInfoEXT = type('VkImportMemoryHostPointerInfoEXT', (ctypes.Structure,), dict())
VkMemoryHostPointerPropertiesEXT = type('VkMemoryHostPointerPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceExternalMemoryHostPropertiesEXT = type('VkPhysicalDeviceExternalMemoryHostPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceConservativeRasterizationPropertiesEXT = type('VkPhysicalDeviceConservativeRasterizationPropertiesEXT', (ctypes.Structure,), dict())
VkCalibratedTimestampInfoEXT = type('VkCalibratedTimestampInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderCorePropertiesAMD = type('VkPhysicalDeviceShaderCorePropertiesAMD', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderCoreProperties2AMD = type('VkPhysicalDeviceShaderCoreProperties2AMD', (ctypes.Structure,), dict())
VkPipelineRasterizationConservativeStateCreateInfoEXT = type('VkPipelineRasterizationConservativeStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceDescriptorIndexingFeatures = type('VkPhysicalDeviceDescriptorIndexingFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceDescriptorIndexingProperties = type('VkPhysicalDeviceDescriptorIndexingProperties', (ctypes.Structure,), dict())
VkDescriptorSetLayoutBindingFlagsCreateInfo = type('VkDescriptorSetLayoutBindingFlagsCreateInfo', (ctypes.Structure,), dict())
VkDescriptorSetVariableDescriptorCountAllocateInfo = type('VkDescriptorSetVariableDescriptorCountAllocateInfo', (ctypes.Structure,), dict())
VkDescriptorSetVariableDescriptorCountLayoutSupport = type('VkDescriptorSetVariableDescriptorCountLayoutSupport', (ctypes.Structure,), dict())
VkAttachmentDescription2 = type('VkAttachmentDescription2', (ctypes.Structure,), dict())
VkAttachmentReference2 = type('VkAttachmentReference2', (ctypes.Structure,), dict())
VkSubpassDescription2 = type('VkSubpassDescription2', (ctypes.Structure,), dict())
VkSubpassDependency2 = type('VkSubpassDependency2', (ctypes.Structure,), dict())
VkRenderPassCreateInfo2 = type('VkRenderPassCreateInfo2', (ctypes.Structure,), dict())
VkSubpassBeginInfo = type('VkSubpassBeginInfo', (ctypes.Structure,), dict())
VkSubpassEndInfo = type('VkSubpassEndInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceTimelineSemaphoreFeatures = type('VkPhysicalDeviceTimelineSemaphoreFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceTimelineSemaphoreProperties = type('VkPhysicalDeviceTimelineSemaphoreProperties', (ctypes.Structure,), dict())
VkSemaphoreTypeCreateInfo = type('VkSemaphoreTypeCreateInfo', (ctypes.Structure,), dict())
VkTimelineSemaphoreSubmitInfo = type('VkTimelineSemaphoreSubmitInfo', (ctypes.Structure,), dict())
VkSemaphoreWaitInfo = type('VkSemaphoreWaitInfo', (ctypes.Structure,), dict())
VkSemaphoreSignalInfo = type('VkSemaphoreSignalInfo', (ctypes.Structure,), dict())
VkVertexInputBindingDivisorDescriptionEXT = type('VkVertexInputBindingDivisorDescriptionEXT', (ctypes.Structure,), dict())
VkPipelineVertexInputDivisorStateCreateInfoEXT = type('VkPipelineVertexInputDivisorStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT = type('VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDevicePCIBusInfoPropertiesEXT = type('VkPhysicalDevicePCIBusInfoPropertiesEXT', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkImportAndroidHardwareBufferInfoANDROID = type('VkImportAndroidHardwareBufferInfoANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidHardwareBufferUsageANDROID = type('VkAndroidHardwareBufferUsageANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidHardwareBufferPropertiesANDROID = type('VkAndroidHardwareBufferPropertiesANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkMemoryGetAndroidHardwareBufferInfoANDROID = type('VkMemoryGetAndroidHardwareBufferInfoANDROID', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidHardwareBufferFormatPropertiesANDROID = type('VkAndroidHardwareBufferFormatPropertiesANDROID', (ctypes.Structure,), dict())
VkCommandBufferInheritanceConditionalRenderingInfoEXT = type('VkCommandBufferInheritanceConditionalRenderingInfoEXT', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkExternalFormatANDROID = type('VkExternalFormatANDROID', (ctypes.Structure,), dict())
VkPhysicalDevice8BitStorageFeatures = type('VkPhysicalDevice8BitStorageFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceConditionalRenderingFeaturesEXT = type('VkPhysicalDeviceConditionalRenderingFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceVulkanMemoryModelFeatures = type('VkPhysicalDeviceVulkanMemoryModelFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderAtomicInt64Features = type('VkPhysicalDeviceShaderAtomicInt64Features', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderAtomicFloatFeaturesEXT = type('VkPhysicalDeviceShaderAtomicFloatFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceVertexAttributeDivisorFeaturesEXT = type('VkPhysicalDeviceVertexAttributeDivisorFeaturesEXT', (ctypes.Structure,), dict())
VkQueueFamilyCheckpointPropertiesNV = type('VkQueueFamilyCheckpointPropertiesNV', (ctypes.Structure,), dict())
VkCheckpointDataNV = type('VkCheckpointDataNV', (ctypes.Structure,), dict())
VkPhysicalDeviceDepthStencilResolveProperties = type('VkPhysicalDeviceDepthStencilResolveProperties', (ctypes.Structure,), dict())
VkSubpassDescriptionDepthStencilResolve = type('VkSubpassDescriptionDepthStencilResolve', (ctypes.Structure,), dict())
VkImageViewASTCDecodeModeEXT = type('VkImageViewASTCDecodeModeEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceASTCDecodeFeaturesEXT = type('VkPhysicalDeviceASTCDecodeFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceTransformFeedbackFeaturesEXT = type('VkPhysicalDeviceTransformFeedbackFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceTransformFeedbackPropertiesEXT = type('VkPhysicalDeviceTransformFeedbackPropertiesEXT', (ctypes.Structure,), dict())
VkPipelineRasterizationStateStreamCreateInfoEXT = type('VkPipelineRasterizationStateStreamCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV = type('VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV', (ctypes.Structure,), dict())
VkPipelineRepresentativeFragmentTestStateCreateInfoNV = type('VkPipelineRepresentativeFragmentTestStateCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceExclusiveScissorFeaturesNV = type('VkPhysicalDeviceExclusiveScissorFeaturesNV', (ctypes.Structure,), dict())
VkPipelineViewportExclusiveScissorStateCreateInfoNV = type('VkPipelineViewportExclusiveScissorStateCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceCornerSampledImageFeaturesNV = type('VkPhysicalDeviceCornerSampledImageFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceComputeShaderDerivativesFeaturesNV = type('VkPhysicalDeviceComputeShaderDerivativesFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShaderBarycentricFeaturesNV = type('VkPhysicalDeviceFragmentShaderBarycentricFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderImageFootprintFeaturesNV = type('VkPhysicalDeviceShaderImageFootprintFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV = type('VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV', (ctypes.Structure,), dict())
VkShadingRatePaletteNV = type('VkShadingRatePaletteNV', (ctypes.Structure,), dict())
VkPipelineViewportShadingRateImageStateCreateInfoNV = type('VkPipelineViewportShadingRateImageStateCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceShadingRateImageFeaturesNV = type('VkPhysicalDeviceShadingRateImageFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceShadingRateImagePropertiesNV = type('VkPhysicalDeviceShadingRateImagePropertiesNV', (ctypes.Structure,), dict())
VkCoarseSampleLocationNV = type('VkCoarseSampleLocationNV', (ctypes.Structure,), dict())
VkCoarseSampleOrderCustomNV = type('VkCoarseSampleOrderCustomNV', (ctypes.Structure,), dict())
VkPipelineViewportCoarseSampleOrderStateCreateInfoNV = type('VkPipelineViewportCoarseSampleOrderStateCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceMeshShaderFeaturesNV = type('VkPhysicalDeviceMeshShaderFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceMeshShaderPropertiesNV = type('VkPhysicalDeviceMeshShaderPropertiesNV', (ctypes.Structure,), dict())
VkDrawMeshTasksIndirectCommandNV = type('VkDrawMeshTasksIndirectCommandNV', (ctypes.Structure,), dict())
VkRayTracingShaderGroupCreateInfoNV = type('VkRayTracingShaderGroupCreateInfoNV', (ctypes.Structure,), dict())
VkRayTracingShaderGroupCreateInfoKHR = type('VkRayTracingShaderGroupCreateInfoKHR', (ctypes.Structure,), dict())
VkRayTracingPipelineCreateInfoNV = type('VkRayTracingPipelineCreateInfoNV', (ctypes.Structure,), dict())
VkPipelineLibraryCreateInfoKHR = type('VkPipelineLibraryCreateInfoKHR', (ctypes.Structure,), dict())
VkRayTracingPipelineInterfaceCreateInfoKHR = type('VkRayTracingPipelineInterfaceCreateInfoKHR', (ctypes.Structure,), dict())
VkRayTracingPipelineCreateInfoKHR = type('VkRayTracingPipelineCreateInfoKHR', (ctypes.Structure,), dict())
VkGeometryTrianglesNV = type('VkGeometryTrianglesNV', (ctypes.Structure,), dict())
VkGeometryAABBNV = type('VkGeometryAABBNV', (ctypes.Structure,), dict())
VkGeometryDataNV = type('VkGeometryDataNV', (ctypes.Structure,), dict())
VkGeometryNV = type('VkGeometryNV', (ctypes.Structure,), dict())
VkAccelerationStructureInfoNV = type('VkAccelerationStructureInfoNV', (ctypes.Structure,), dict())
VkAccelerationStructureCreateInfoNV = type('VkAccelerationStructureCreateInfoNV', (ctypes.Structure,), dict())
VkBindAccelerationStructureMemoryInfoNV = type('VkBindAccelerationStructureMemoryInfoNV', (ctypes.Structure,), dict())
VkWriteDescriptorSetAccelerationStructureKHR = type('VkWriteDescriptorSetAccelerationStructureKHR', (ctypes.Structure,), dict())
VkWriteDescriptorSetAccelerationStructureNV = type('VkWriteDescriptorSetAccelerationStructureNV', (ctypes.Structure,), dict())
VkAccelerationStructureMemoryRequirementsInfoNV = type('VkAccelerationStructureMemoryRequirementsInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceAccelerationStructureFeaturesKHR = type('VkPhysicalDeviceAccelerationStructureFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceRayTracingPipelineFeaturesKHR = type('VkPhysicalDeviceRayTracingPipelineFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceRayQueryFeaturesKHR = type('VkPhysicalDeviceRayQueryFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceAccelerationStructurePropertiesKHR = type('VkPhysicalDeviceAccelerationStructurePropertiesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceRayTracingPipelinePropertiesKHR = type('VkPhysicalDeviceRayTracingPipelinePropertiesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceRayTracingPropertiesNV = type('VkPhysicalDeviceRayTracingPropertiesNV', (ctypes.Structure,), dict())
VkStridedDeviceAddressRegionKHR = type('VkStridedDeviceAddressRegionKHR', (ctypes.Structure,), dict())
VkTraceRaysIndirectCommandKHR = type('VkTraceRaysIndirectCommandKHR', (ctypes.Structure,), dict())
VkDrmFormatModifierPropertiesEXT = type('VkDrmFormatModifierPropertiesEXT', (ctypes.Structure,), dict())
VkDrmFormatModifierPropertiesListEXT = type('VkDrmFormatModifierPropertiesListEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceImageDrmFormatModifierInfoEXT = type('VkPhysicalDeviceImageDrmFormatModifierInfoEXT', (ctypes.Structure,), dict())
VkImageDrmFormatModifierListCreateInfoEXT = type('VkImageDrmFormatModifierListCreateInfoEXT', (ctypes.Structure,), dict())
VkImageDrmFormatModifierExplicitCreateInfoEXT = type('VkImageDrmFormatModifierExplicitCreateInfoEXT', (ctypes.Structure,), dict())
VkImageDrmFormatModifierPropertiesEXT = type('VkImageDrmFormatModifierPropertiesEXT', (ctypes.Structure,), dict())
VkImageStencilUsageCreateInfo = type('VkImageStencilUsageCreateInfo', (ctypes.Structure,), dict())
VkDeviceMemoryOverallocationCreateInfoAMD = type('VkDeviceMemoryOverallocationCreateInfoAMD', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentDensityMapFeaturesEXT = type('VkPhysicalDeviceFragmentDensityMapFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentDensityMap2FeaturesEXT = type('VkPhysicalDeviceFragmentDensityMap2FeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentDensityMapPropertiesEXT = type('VkPhysicalDeviceFragmentDensityMapPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentDensityMap2PropertiesEXT = type('VkPhysicalDeviceFragmentDensityMap2PropertiesEXT', (ctypes.Structure,), dict())
VkRenderPassFragmentDensityMapCreateInfoEXT = type('VkRenderPassFragmentDensityMapCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceScalarBlockLayoutFeatures = type('VkPhysicalDeviceScalarBlockLayoutFeatures', (ctypes.Structure,), dict())
VkSurfaceProtectedCapabilitiesKHR = type('VkSurfaceProtectedCapabilitiesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceUniformBufferStandardLayoutFeatures = type('VkPhysicalDeviceUniformBufferStandardLayoutFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceDepthClipEnableFeaturesEXT = type('VkPhysicalDeviceDepthClipEnableFeaturesEXT', (ctypes.Structure,), dict())
VkPipelineRasterizationDepthClipStateCreateInfoEXT = type('VkPipelineRasterizationDepthClipStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceMemoryBudgetPropertiesEXT = type('VkPhysicalDeviceMemoryBudgetPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceMemoryPriorityFeaturesEXT = type('VkPhysicalDeviceMemoryPriorityFeaturesEXT', (ctypes.Structure,), dict())
VkMemoryPriorityAllocateInfoEXT = type('VkMemoryPriorityAllocateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceBufferDeviceAddressFeatures = type('VkPhysicalDeviceBufferDeviceAddressFeatures', (ctypes.Structure,), dict())
VkPhysicalDeviceBufferDeviceAddressFeaturesEXT = type('VkPhysicalDeviceBufferDeviceAddressFeaturesEXT', (ctypes.Structure,), dict())
VkBufferDeviceAddressInfo = type('VkBufferDeviceAddressInfo', (ctypes.Structure,), dict())
VkBufferOpaqueCaptureAddressCreateInfo = type('VkBufferOpaqueCaptureAddressCreateInfo', (ctypes.Structure,), dict())
VkBufferDeviceAddressCreateInfoEXT = type('VkBufferDeviceAddressCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceImageViewImageFormatInfoEXT = type('VkPhysicalDeviceImageViewImageFormatInfoEXT', (ctypes.Structure,), dict())
VkFilterCubicImageViewImageFormatPropertiesEXT = type('VkFilterCubicImageViewImageFormatPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceImagelessFramebufferFeatures = type('VkPhysicalDeviceImagelessFramebufferFeatures', (ctypes.Structure,), dict())
VkFramebufferAttachmentImageInfo = type('VkFramebufferAttachmentImageInfo', (ctypes.Structure,), dict())
VkFramebufferAttachmentsCreateInfo = type('VkFramebufferAttachmentsCreateInfo', (ctypes.Structure,), dict())
VkRenderPassAttachmentBeginInfo = type('VkRenderPassAttachmentBeginInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceTextureCompressionASTCHDRFeaturesEXT = type('VkPhysicalDeviceTextureCompressionASTCHDRFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceCooperativeMatrixFeaturesNV = type('VkPhysicalDeviceCooperativeMatrixFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceCooperativeMatrixPropertiesNV = type('VkPhysicalDeviceCooperativeMatrixPropertiesNV', (ctypes.Structure,), dict())
VkCooperativeMatrixPropertiesNV = type('VkCooperativeMatrixPropertiesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceYcbcrImageArraysFeaturesEXT = type('VkPhysicalDeviceYcbcrImageArraysFeaturesEXT', (ctypes.Structure,), dict())
VkImageViewHandleInfoNVX = type('VkImageViewHandleInfoNVX', (ctypes.Structure,), dict())
VkImageViewAddressPropertiesNVX = type('VkImageViewAddressPropertiesNVX', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_GGP:
    VkPresentFrameTokenGGP = type('VkPresentFrameTokenGGP', (ctypes.Structure,), dict())
VkPipelineCreationFeedbackEXT = type('VkPipelineCreationFeedbackEXT', (ctypes.Structure,), dict())
VkPipelineCreationFeedbackCreateInfoEXT = type('VkPipelineCreationFeedbackCreateInfoEXT', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkSurfaceFullScreenExclusiveInfoEXT = type('VkSurfaceFullScreenExclusiveInfoEXT', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkSurfaceFullScreenExclusiveWin32InfoEXT = type('VkSurfaceFullScreenExclusiveWin32InfoEXT', (ctypes.Structure,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkSurfaceCapabilitiesFullScreenExclusiveEXT = type('VkSurfaceCapabilitiesFullScreenExclusiveEXT', (ctypes.Structure,), dict())
VkPhysicalDevicePerformanceQueryFeaturesKHR = type('VkPhysicalDevicePerformanceQueryFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDevicePerformanceQueryPropertiesKHR = type('VkPhysicalDevicePerformanceQueryPropertiesKHR', (ctypes.Structure,), dict())
VkPerformanceCounterKHR = type('VkPerformanceCounterKHR', (ctypes.Structure,), dict())
VkPerformanceCounterDescriptionKHR = type('VkPerformanceCounterDescriptionKHR', (ctypes.Structure,), dict())
VkQueryPoolPerformanceCreateInfoKHR = type('VkQueryPoolPerformanceCreateInfoKHR', (ctypes.Structure,), dict())
VkPerformanceCounterResultKHR = type('VkPerformanceCounterResultKHR', (ctypes.Union,), dict())
VkAcquireProfilingLockInfoKHR = type('VkAcquireProfilingLockInfoKHR', (ctypes.Structure,), dict())
VkPerformanceQuerySubmitInfoKHR = type('VkPerformanceQuerySubmitInfoKHR', (ctypes.Structure,), dict())
VkHeadlessSurfaceCreateInfoEXT = type('VkHeadlessSurfaceCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceCoverageReductionModeFeaturesNV = type('VkPhysicalDeviceCoverageReductionModeFeaturesNV', (ctypes.Structure,), dict())
VkPipelineCoverageReductionStateCreateInfoNV = type('VkPipelineCoverageReductionStateCreateInfoNV', (ctypes.Structure,), dict())
VkFramebufferMixedSamplesCombinationNV = type('VkFramebufferMixedSamplesCombinationNV', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL = type('VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL', (ctypes.Structure,), dict())
VkPerformanceValueDataINTEL = type('VkPerformanceValueDataINTEL', (ctypes.Union,), dict())
VkPerformanceValueINTEL = type('VkPerformanceValueINTEL', (ctypes.Structure,), dict())
VkInitializePerformanceApiInfoINTEL = type('VkInitializePerformanceApiInfoINTEL', (ctypes.Structure,), dict())
VkQueryPoolPerformanceQueryCreateInfoINTEL = type('VkQueryPoolPerformanceQueryCreateInfoINTEL', (ctypes.Structure,), dict())
VkPerformanceMarkerInfoINTEL = type('VkPerformanceMarkerInfoINTEL', (ctypes.Structure,), dict())
VkPerformanceStreamMarkerInfoINTEL = type('VkPerformanceStreamMarkerInfoINTEL', (ctypes.Structure,), dict())
VkPerformanceOverrideInfoINTEL = type('VkPerformanceOverrideInfoINTEL', (ctypes.Structure,), dict())
VkPerformanceConfigurationAcquireInfoINTEL = type('VkPerformanceConfigurationAcquireInfoINTEL', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderClockFeaturesKHR = type('VkPhysicalDeviceShaderClockFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceIndexTypeUint8FeaturesEXT = type('VkPhysicalDeviceIndexTypeUint8FeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderSMBuiltinsPropertiesNV = type('VkPhysicalDeviceShaderSMBuiltinsPropertiesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderSMBuiltinsFeaturesNV = type('VkPhysicalDeviceShaderSMBuiltinsFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT = type('VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures = type('VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures', (ctypes.Structure,), dict())
VkAttachmentReferenceStencilLayout = type('VkAttachmentReferenceStencilLayout', (ctypes.Structure,), dict())
VkAttachmentDescriptionStencilLayout = type('VkAttachmentDescriptionStencilLayout', (ctypes.Structure,), dict())
VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR = type('VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR', (ctypes.Structure,), dict())
VkPipelineInfoKHR = type('VkPipelineInfoKHR', (ctypes.Structure,), dict())
VkPipelineExecutablePropertiesKHR = type('VkPipelineExecutablePropertiesKHR', (ctypes.Structure,), dict())
VkPipelineExecutableInfoKHR = type('VkPipelineExecutableInfoKHR', (ctypes.Structure,), dict())
VkPipelineExecutableStatisticValueKHR = type('VkPipelineExecutableStatisticValueKHR', (ctypes.Union,), dict())
VkPipelineExecutableStatisticKHR = type('VkPipelineExecutableStatisticKHR', (ctypes.Structure,), dict())
VkPipelineExecutableInternalRepresentationKHR = type('VkPipelineExecutableInternalRepresentationKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderDemoteToHelperInvocationFeaturesEXT = type('VkPhysicalDeviceShaderDemoteToHelperInvocationFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT = type('VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceTexelBufferAlignmentPropertiesEXT = type('VkPhysicalDeviceTexelBufferAlignmentPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceSubgroupSizeControlFeaturesEXT = type('VkPhysicalDeviceSubgroupSizeControlFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceSubgroupSizeControlPropertiesEXT = type('VkPhysicalDeviceSubgroupSizeControlPropertiesEXT', (ctypes.Structure,), dict())
VkPipelineShaderStageRequiredSubgroupSizeCreateInfoEXT = type('VkPipelineShaderStageRequiredSubgroupSizeCreateInfoEXT', (ctypes.Structure,), dict())
VkMemoryOpaqueCaptureAddressAllocateInfo = type('VkMemoryOpaqueCaptureAddressAllocateInfo', (ctypes.Structure,), dict())
VkDeviceMemoryOpaqueCaptureAddressInfo = type('VkDeviceMemoryOpaqueCaptureAddressInfo', (ctypes.Structure,), dict())
VkPhysicalDeviceLineRasterizationFeaturesEXT = type('VkPhysicalDeviceLineRasterizationFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceLineRasterizationPropertiesEXT = type('VkPhysicalDeviceLineRasterizationPropertiesEXT', (ctypes.Structure,), dict())
VkPipelineRasterizationLineStateCreateInfoEXT = type('VkPipelineRasterizationLineStateCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDevicePipelineCreationCacheControlFeaturesEXT = type('VkPhysicalDevicePipelineCreationCacheControlFeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceVulkan11Features = type('VkPhysicalDeviceVulkan11Features', (ctypes.Structure,), dict())
VkPhysicalDeviceVulkan11Properties = type('VkPhysicalDeviceVulkan11Properties', (ctypes.Structure,), dict())
VkPhysicalDeviceVulkan12Features = type('VkPhysicalDeviceVulkan12Features', (ctypes.Structure,), dict())
VkPhysicalDeviceVulkan12Properties = type('VkPhysicalDeviceVulkan12Properties', (ctypes.Structure,), dict())
VkPipelineCompilerControlCreateInfoAMD = type('VkPipelineCompilerControlCreateInfoAMD', (ctypes.Structure,), dict())
VkPhysicalDeviceCoherentMemoryFeaturesAMD = type('VkPhysicalDeviceCoherentMemoryFeaturesAMD', (ctypes.Structure,), dict())
VkPhysicalDeviceToolPropertiesEXT = type('VkPhysicalDeviceToolPropertiesEXT', (ctypes.Structure,), dict())
VkSamplerCustomBorderColorCreateInfoEXT = type('VkSamplerCustomBorderColorCreateInfoEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceCustomBorderColorPropertiesEXT = type('VkPhysicalDeviceCustomBorderColorPropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceCustomBorderColorFeaturesEXT = type('VkPhysicalDeviceCustomBorderColorFeaturesEXT', (ctypes.Structure,), dict())
VkDeviceOrHostAddressKHR = type('VkDeviceOrHostAddressKHR', (ctypes.Union,), dict())
VkDeviceOrHostAddressConstKHR = type('VkDeviceOrHostAddressConstKHR', (ctypes.Union,), dict())
VkAccelerationStructureGeometryTrianglesDataKHR = type('VkAccelerationStructureGeometryTrianglesDataKHR', (ctypes.Structure,), dict())
VkAccelerationStructureGeometryAabbsDataKHR = type('VkAccelerationStructureGeometryAabbsDataKHR', (ctypes.Structure,), dict())
VkAccelerationStructureGeometryInstancesDataKHR = type('VkAccelerationStructureGeometryInstancesDataKHR', (ctypes.Structure,), dict())
VkAccelerationStructureGeometryDataKHR = type('VkAccelerationStructureGeometryDataKHR', (ctypes.Union,), dict())
VkAccelerationStructureGeometryKHR = type('VkAccelerationStructureGeometryKHR', (ctypes.Structure,), dict())
VkAccelerationStructureBuildGeometryInfoKHR = type('VkAccelerationStructureBuildGeometryInfoKHR', (ctypes.Structure,), dict())
VkAccelerationStructureBuildRangeInfoKHR = type('VkAccelerationStructureBuildRangeInfoKHR', (ctypes.Structure,), dict())
VkAccelerationStructureCreateInfoKHR = type('VkAccelerationStructureCreateInfoKHR', (ctypes.Structure,), dict())
VkAabbPositionsKHR = type('VkAabbPositionsKHR', (ctypes.Structure,), dict())
VkTransformMatrixKHR = type('VkTransformMatrixKHR', (ctypes.Structure,), dict())
VkAccelerationStructureInstanceKHR = type('VkAccelerationStructureInstanceKHR', (ctypes.Structure,), dict())
VkAccelerationStructureDeviceAddressInfoKHR = type('VkAccelerationStructureDeviceAddressInfoKHR', (ctypes.Structure,), dict())
VkAccelerationStructureVersionInfoKHR = type('VkAccelerationStructureVersionInfoKHR', (ctypes.Structure,), dict())
VkCopyAccelerationStructureInfoKHR = type('VkCopyAccelerationStructureInfoKHR', (ctypes.Structure,), dict())
VkCopyAccelerationStructureToMemoryInfoKHR = type('VkCopyAccelerationStructureToMemoryInfoKHR', (ctypes.Structure,), dict())
VkCopyMemoryToAccelerationStructureInfoKHR = type('VkCopyMemoryToAccelerationStructureInfoKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceExtendedDynamicStateFeaturesEXT = type('VkPhysicalDeviceExtendedDynamicStateFeaturesEXT', (ctypes.Structure,), dict())
VkRenderPassTransformBeginInfoQCOM = type('VkRenderPassTransformBeginInfoQCOM', (ctypes.Structure,), dict())
VkCopyCommandTransformInfoQCOM = type('VkCopyCommandTransformInfoQCOM', (ctypes.Structure,), dict())
VkCommandBufferInheritanceRenderPassTransformInfoQCOM = type('VkCommandBufferInheritanceRenderPassTransformInfoQCOM', (ctypes.Structure,), dict())
VkPhysicalDeviceDiagnosticsConfigFeaturesNV = type('VkPhysicalDeviceDiagnosticsConfigFeaturesNV', (ctypes.Structure,), dict())
VkDeviceDiagnosticsConfigCreateInfoNV = type('VkDeviceDiagnosticsConfigCreateInfoNV', (ctypes.Structure,), dict())
VkPhysicalDeviceRobustness2FeaturesEXT = type('VkPhysicalDeviceRobustness2FeaturesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceRobustness2PropertiesEXT = type('VkPhysicalDeviceRobustness2PropertiesEXT', (ctypes.Structure,), dict())
VkPhysicalDeviceImageRobustnessFeaturesEXT = type('VkPhysicalDeviceImageRobustnessFeaturesEXT', (ctypes.Structure,), dict())
if VK_ENABLE_BETA_EXTENSIONS:
    VkPhysicalDevicePortabilitySubsetFeaturesKHR = type('VkPhysicalDevicePortabilitySubsetFeaturesKHR', (ctypes.Structure,), dict())
if VK_ENABLE_BETA_EXTENSIONS:
    VkPhysicalDevicePortabilitySubsetPropertiesKHR = type('VkPhysicalDevicePortabilitySubsetPropertiesKHR', (ctypes.Structure,), dict())
VkPhysicalDevice4444FormatsFeaturesEXT = type('VkPhysicalDevice4444FormatsFeaturesEXT', (ctypes.Structure,), dict())
VkBufferCopy2KHR = type('VkBufferCopy2KHR', (ctypes.Structure,), dict())
VkImageCopy2KHR = type('VkImageCopy2KHR', (ctypes.Structure,), dict())
VkImageBlit2KHR = type('VkImageBlit2KHR', (ctypes.Structure,), dict())
VkBufferImageCopy2KHR = type('VkBufferImageCopy2KHR', (ctypes.Structure,), dict())
VkImageResolve2KHR = type('VkImageResolve2KHR', (ctypes.Structure,), dict())
VkCopyBufferInfo2KHR = type('VkCopyBufferInfo2KHR', (ctypes.Structure,), dict())
VkCopyImageInfo2KHR = type('VkCopyImageInfo2KHR', (ctypes.Structure,), dict())
VkBlitImageInfo2KHR = type('VkBlitImageInfo2KHR', (ctypes.Structure,), dict())
VkCopyBufferToImageInfo2KHR = type('VkCopyBufferToImageInfo2KHR', (ctypes.Structure,), dict())
VkCopyImageToBufferInfo2KHR = type('VkCopyImageToBufferInfo2KHR', (ctypes.Structure,), dict())
VkResolveImageInfo2KHR = type('VkResolveImageInfo2KHR', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderImageAtomicInt64FeaturesEXT = type('VkPhysicalDeviceShaderImageAtomicInt64FeaturesEXT', (ctypes.Structure,), dict())
VkFragmentShadingRateAttachmentInfoKHR = type('VkFragmentShadingRateAttachmentInfoKHR', (ctypes.Structure,), dict())
VkPipelineFragmentShadingRateStateCreateInfoKHR = type('VkPipelineFragmentShadingRateStateCreateInfoKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShadingRateFeaturesKHR = type('VkPhysicalDeviceFragmentShadingRateFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShadingRatePropertiesKHR = type('VkPhysicalDeviceFragmentShadingRatePropertiesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShadingRateKHR = type('VkPhysicalDeviceFragmentShadingRateKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceShaderTerminateInvocationFeaturesKHR = type('VkPhysicalDeviceShaderTerminateInvocationFeaturesKHR', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV = type('VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV', (ctypes.Structure,), dict())
VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV = type('VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV', (ctypes.Structure,), dict())
VkPipelineFragmentShadingRateEnumStateCreateInfoNV = type('VkPipelineFragmentShadingRateEnumStateCreateInfoNV', (ctypes.Structure,), dict())
VkAccelerationStructureBuildSizesInfoKHR = type('VkAccelerationStructureBuildSizesInfoKHR', (ctypes.Structure,), dict())

PFN_vkInternalAllocationNotification = VK_FUNCTYPE(None, ctypes.c_void_p, ctypes.c_size_t, VkInternalAllocationType, VkSystemAllocationScope)
PFN_vkInternalFreeNotification = VK_FUNCTYPE(None, ctypes.c_void_p, ctypes.c_size_t, VkInternalAllocationType, VkSystemAllocationScope)
PFN_vkReallocationFunction = VK_FUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, VkSystemAllocationScope)
PFN_vkAllocationFunction = VK_FUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, VkSystemAllocationScope)
PFN_vkFreeFunction = VK_FUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
PFN_vkVoidFunction = VK_FUNCTYPE(None)
PFN_vkDebugReportCallbackEXT = VK_FUNCTYPE(VkBool32, VkDebugReportFlagsEXT, VkDebugReportObjectTypeEXT, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)
PFN_vkDebugUtilsMessengerCallbackEXT = VK_FUNCTYPE(VkBool32, VkDebugUtilsMessageSeverityFlagBitsEXT, VkDebugUtilsMessageTypeFlagsEXT, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT), ctypes.c_void_p)
PFN_vkDeviceMemoryReportCallbackEXT = VK_FUNCTYPE(None, ctypes.POINTER(VkDeviceMemoryReportCallbackDataEXT), ctypes.c_void_p)

VkBaseOutStructure._fields_ = [('sType', VkStructureType), ('pNext', ctypes.POINTER(VkBaseOutStructure))]
VkBaseInStructure._fields_ = [('sType', VkStructureType), ('pNext', ctypes.POINTER(VkBaseInStructure))]
VkOffset2D._fields_ = [('x', ctypes.c_int32), ('y', ctypes.c_int32)]
VkOffset3D._fields_ = [('x', ctypes.c_int32), ('y', ctypes.c_int32), ('z', ctypes.c_int32)]
VkExtent2D._fields_ = [('width', ctypes.c_uint32), ('height', ctypes.c_uint32)]
VkExtent3D._fields_ = [('width', ctypes.c_uint32), ('height', ctypes.c_uint32), ('depth', ctypes.c_uint32)]
VkViewport._fields_ = [('x', ctypes.c_float), ('y', ctypes.c_float), ('width', ctypes.c_float), ('height', ctypes.c_float), ('minDepth', ctypes.c_float), ('maxDepth', ctypes.c_float)]
VkRect2D._fields_ = [('offset', VkOffset2D), ('extent', VkExtent2D)]
VkClearRect._fields_ = [('rect', VkRect2D), ('baseArrayLayer', ctypes.c_uint32), ('layerCount', ctypes.c_uint32)]
VkComponentMapping._fields_ = [('r', VkComponentSwizzle), ('g', VkComponentSwizzle), ('b', VkComponentSwizzle), ('a', VkComponentSwizzle)]
VkPhysicalDeviceLimits._fields_ = [('maxImageDimension1D', ctypes.c_uint32), ('maxImageDimension2D', ctypes.c_uint32), ('maxImageDimension3D', ctypes.c_uint32), ('maxImageDimensionCube', ctypes.c_uint32), ('maxImageArrayLayers', ctypes.c_uint32), ('maxTexelBufferElements', ctypes.c_uint32), ('maxUniformBufferRange', ctypes.c_uint32), ('maxStorageBufferRange', ctypes.c_uint32), ('maxPushConstantsSize', ctypes.c_uint32), ('maxMemoryAllocationCount', ctypes.c_uint32), ('maxSamplerAllocationCount', ctypes.c_uint32), ('bufferImageGranularity', VkDeviceSize), ('sparseAddressSpaceSize', VkDeviceSize), ('maxBoundDescriptorSets', ctypes.c_uint32), ('maxPerStageDescriptorSamplers', ctypes.c_uint32), ('maxPerStageDescriptorUniformBuffers', ctypes.c_uint32), ('maxPerStageDescriptorStorageBuffers', ctypes.c_uint32), ('maxPerStageDescriptorSampledImages', ctypes.c_uint32), ('maxPerStageDescriptorStorageImages', ctypes.c_uint32), ('maxPerStageDescriptorInputAttachments', ctypes.c_uint32), ('maxPerStageResources', ctypes.c_uint32), ('maxDescriptorSetSamplers', ctypes.c_uint32), ('maxDescriptorSetUniformBuffers', ctypes.c_uint32), ('maxDescriptorSetUniformBuffersDynamic', ctypes.c_uint32), ('maxDescriptorSetStorageBuffers', ctypes.c_uint32), ('maxDescriptorSetStorageBuffersDynamic', ctypes.c_uint32), ('maxDescriptorSetSampledImages', ctypes.c_uint32), ('maxDescriptorSetStorageImages', ctypes.c_uint32), ('maxDescriptorSetInputAttachments', ctypes.c_uint32), ('maxVertexInputAttributes', ctypes.c_uint32), ('maxVertexInputBindings', ctypes.c_uint32), ('maxVertexInputAttributeOffset', ctypes.c_uint32), ('maxVertexInputBindingStride', ctypes.c_uint32), ('maxVertexOutputComponents', ctypes.c_uint32), ('maxTessellationGenerationLevel', ctypes.c_uint32), ('maxTessellationPatchSize', ctypes.c_uint32), ('maxTessellationControlPerVertexInputComponents', ctypes.c_uint32), ('maxTessellationControlPerVertexOutputComponents', ctypes.c_uint32), ('maxTessellationControlPerPatchOutputComponents', ctypes.c_uint32), ('maxTessellationControlTotalOutputComponents', ctypes.c_uint32), ('maxTessellationEvaluationInputComponents', ctypes.c_uint32), ('maxTessellationEvaluationOutputComponents', ctypes.c_uint32), ('maxGeometryShaderInvocations', ctypes.c_uint32), ('maxGeometryInputComponents', ctypes.c_uint32), ('maxGeometryOutputComponents', ctypes.c_uint32), ('maxGeometryOutputVertices', ctypes.c_uint32), ('maxGeometryTotalOutputComponents', ctypes.c_uint32), ('maxFragmentInputComponents', ctypes.c_uint32), ('maxFragmentOutputAttachments', ctypes.c_uint32), ('maxFragmentDualSrcAttachments', ctypes.c_uint32), ('maxFragmentCombinedOutputResources', ctypes.c_uint32), ('maxComputeSharedMemorySize', ctypes.c_uint32), ('maxComputeWorkGroupCount', (ctypes.c_uint32 * (3))), ('maxComputeWorkGroupInvocations', ctypes.c_uint32), ('maxComputeWorkGroupSize', (ctypes.c_uint32 * (3))), ('subPixelPrecisionBits', ctypes.c_uint32), ('subTexelPrecisionBits', ctypes.c_uint32), ('mipmapPrecisionBits', ctypes.c_uint32), ('maxDrawIndexedIndexValue', ctypes.c_uint32), ('maxDrawIndirectCount', ctypes.c_uint32), ('maxSamplerLodBias', ctypes.c_float), ('maxSamplerAnisotropy', ctypes.c_float), ('maxViewports', ctypes.c_uint32), ('maxViewportDimensions', (ctypes.c_uint32 * (2))), ('viewportBoundsRange', (ctypes.c_float * (2))), ('viewportSubPixelBits', ctypes.c_uint32), ('minMemoryMapAlignment', ctypes.c_size_t), ('minTexelBufferOffsetAlignment', VkDeviceSize), ('minUniformBufferOffsetAlignment', VkDeviceSize), ('minStorageBufferOffsetAlignment', VkDeviceSize), ('minTexelOffset', ctypes.c_int32), ('maxTexelOffset', ctypes.c_uint32), ('minTexelGatherOffset', ctypes.c_int32), ('maxTexelGatherOffset', ctypes.c_uint32), ('minInterpolationOffset', ctypes.c_float), ('maxInterpolationOffset', ctypes.c_float), ('subPixelInterpolationOffsetBits', ctypes.c_uint32), ('maxFramebufferWidth', ctypes.c_uint32), ('maxFramebufferHeight', ctypes.c_uint32), ('maxFramebufferLayers', ctypes.c_uint32), ('framebufferColorSampleCounts', VkSampleCountFlags), ('framebufferDepthSampleCounts', VkSampleCountFlags), ('framebufferStencilSampleCounts', VkSampleCountFlags), ('framebufferNoAttachmentsSampleCounts', VkSampleCountFlags), ('maxColorAttachments', ctypes.c_uint32), ('sampledImageColorSampleCounts', VkSampleCountFlags), ('sampledImageIntegerSampleCounts', VkSampleCountFlags), ('sampledImageDepthSampleCounts', VkSampleCountFlags), ('sampledImageStencilSampleCounts', VkSampleCountFlags), ('storageImageSampleCounts', VkSampleCountFlags), ('maxSampleMaskWords', ctypes.c_uint32), ('timestampComputeAndGraphics', VkBool32), ('timestampPeriod', ctypes.c_float), ('maxClipDistances', ctypes.c_uint32), ('maxCullDistances', ctypes.c_uint32), ('maxCombinedClipAndCullDistances', ctypes.c_uint32), ('discreteQueuePriorities', ctypes.c_uint32), ('pointSizeRange', (ctypes.c_float * (2))), ('lineWidthRange', (ctypes.c_float * (2))), ('pointSizeGranularity', ctypes.c_float), ('lineWidthGranularity', ctypes.c_float), ('strictLines', VkBool32), ('standardSampleLocations', VkBool32), ('optimalBufferCopyOffsetAlignment', VkDeviceSize), ('optimalBufferCopyRowPitchAlignment', VkDeviceSize), ('nonCoherentAtomSize', VkDeviceSize)]
VkPhysicalDeviceSparseProperties._fields_ = [('residencyStandard2DBlockShape', VkBool32), ('residencyStandard2DMultisampleBlockShape', VkBool32), ('residencyStandard3DBlockShape', VkBool32), ('residencyAlignedMipSize', VkBool32), ('residencyNonResidentStrict', VkBool32)]
VkPhysicalDeviceProperties._fields_ = [('apiVersion', ctypes.c_uint32), ('driverVersion', ctypes.c_uint32), ('vendorID', ctypes.c_uint32), ('deviceID', ctypes.c_uint32), ('deviceType', VkPhysicalDeviceType), ('deviceName', (ctypes.c_char * (VK_MAX_PHYSICAL_DEVICE_NAME_SIZE))), ('pipelineCacheUUID', (ctypes.c_uint8 * (VK_UUID_SIZE))), ('limits', VkPhysicalDeviceLimits), ('sparseProperties', VkPhysicalDeviceSparseProperties)]
VkExtensionProperties._fields_ = [('extensionName', (ctypes.c_char * (VK_MAX_EXTENSION_NAME_SIZE))), ('specVersion', ctypes.c_uint32)]
VkLayerProperties._fields_ = [('layerName', (ctypes.c_char * (VK_MAX_EXTENSION_NAME_SIZE))), ('specVersion', ctypes.c_uint32), ('implementationVersion', ctypes.c_uint32), ('description', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE)))]
VkApplicationInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pApplicationName', ctypes.c_char_p), ('applicationVersion', ctypes.c_uint32), ('pEngineName', ctypes.c_char_p), ('engineVersion', ctypes.c_uint32), ('apiVersion', ctypes.c_uint32)]
VkAllocationCallbacks._fields_ = [('pUserData', ctypes.c_void_p), ('pfnAllocation', PFN_vkAllocationFunction), ('pfnReallocation', PFN_vkReallocationFunction), ('pfnFree', PFN_vkFreeFunction), ('pfnInternalAllocation', PFN_vkInternalAllocationNotification), ('pfnInternalFree', PFN_vkInternalFreeNotification)]
VkDeviceQueueCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDeviceQueueCreateFlags), ('queueFamilyIndex', ctypes.c_uint32), ('queueCount', ctypes.c_uint32), ('pQueuePriorities', ctypes.POINTER(ctypes.c_float))]
VkPhysicalDeviceFeatures._fields_ = [('robustBufferAccess', VkBool32), ('fullDrawIndexUint32', VkBool32), ('imageCubeArray', VkBool32), ('independentBlend', VkBool32), ('geometryShader', VkBool32), ('tessellationShader', VkBool32), ('sampleRateShading', VkBool32), ('dualSrcBlend', VkBool32), ('logicOp', VkBool32), ('multiDrawIndirect', VkBool32), ('drawIndirectFirstInstance', VkBool32), ('depthClamp', VkBool32), ('depthBiasClamp', VkBool32), ('fillModeNonSolid', VkBool32), ('depthBounds', VkBool32), ('wideLines', VkBool32), ('largePoints', VkBool32), ('alphaToOne', VkBool32), ('multiViewport', VkBool32), ('samplerAnisotropy', VkBool32), ('textureCompressionETC2', VkBool32), ('textureCompressionASTC_LDR', VkBool32), ('textureCompressionBC', VkBool32), ('occlusionQueryPrecise', VkBool32), ('pipelineStatisticsQuery', VkBool32), ('vertexPipelineStoresAndAtomics', VkBool32), ('fragmentStoresAndAtomics', VkBool32), ('shaderTessellationAndGeometryPointSize', VkBool32), ('shaderImageGatherExtended', VkBool32), ('shaderStorageImageExtendedFormats', VkBool32), ('shaderStorageImageMultisample', VkBool32), ('shaderStorageImageReadWithoutFormat', VkBool32), ('shaderStorageImageWriteWithoutFormat', VkBool32), ('shaderUniformBufferArrayDynamicIndexing', VkBool32), ('shaderSampledImageArrayDynamicIndexing', VkBool32), ('shaderStorageBufferArrayDynamicIndexing', VkBool32), ('shaderStorageImageArrayDynamicIndexing', VkBool32), ('shaderClipDistance', VkBool32), ('shaderCullDistance', VkBool32), ('shaderFloat64', VkBool32), ('shaderInt64', VkBool32), ('shaderInt16', VkBool32), ('shaderResourceResidency', VkBool32), ('shaderResourceMinLod', VkBool32), ('sparseBinding', VkBool32), ('sparseResidencyBuffer', VkBool32), ('sparseResidencyImage2D', VkBool32), ('sparseResidencyImage3D', VkBool32), ('sparseResidency2Samples', VkBool32), ('sparseResidency4Samples', VkBool32), ('sparseResidency8Samples', VkBool32), ('sparseResidency16Samples', VkBool32), ('sparseResidencyAliased', VkBool32), ('variableMultisampleRate', VkBool32), ('inheritedQueries', VkBool32)]
VkDeviceCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDeviceCreateFlags), ('queueCreateInfoCount', ctypes.c_uint32), ('pQueueCreateInfos', ctypes.POINTER(VkDeviceQueueCreateInfo)), ('enabledLayerCount', ctypes.c_uint32), ('ppEnabledLayerNames', ctypes.POINTER(ctypes.c_char_p)), ('enabledExtensionCount', ctypes.c_uint32), ('ppEnabledExtensionNames', ctypes.POINTER(ctypes.c_char_p)), ('pEnabledFeatures', ctypes.POINTER(VkPhysicalDeviceFeatures))]
VkInstanceCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkInstanceCreateFlags), ('pApplicationInfo', ctypes.POINTER(VkApplicationInfo)), ('enabledLayerCount', ctypes.c_uint32), ('ppEnabledLayerNames', ctypes.POINTER(ctypes.c_char_p)), ('enabledExtensionCount', ctypes.c_uint32), ('ppEnabledExtensionNames', ctypes.POINTER(ctypes.c_char_p))]
VkQueueFamilyProperties._fields_ = [('queueFlags', VkQueueFlags), ('queueCount', ctypes.c_uint32), ('timestampValidBits', ctypes.c_uint32), ('minImageTransferGranularity', VkExtent3D)]
VkMemoryType._fields_ = [('propertyFlags', VkMemoryPropertyFlags), ('heapIndex', ctypes.c_uint32)]
VkMemoryHeap._fields_ = [('size', VkDeviceSize), ('flags', VkMemoryHeapFlags)]
VkPhysicalDeviceMemoryProperties._fields_ = [('memoryTypeCount', ctypes.c_uint32), ('memoryTypes', (VkMemoryType * (VK_MAX_MEMORY_TYPES))), ('memoryHeapCount', ctypes.c_uint32), ('memoryHeaps', (VkMemoryHeap * (VK_MAX_MEMORY_HEAPS)))]
VkMemoryAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('allocationSize', VkDeviceSize), ('memoryTypeIndex', ctypes.c_uint32)]
VkMemoryRequirements._fields_ = [('size', VkDeviceSize), ('alignment', VkDeviceSize), ('memoryTypeBits', ctypes.c_uint32)]
VkSparseImageFormatProperties._fields_ = [('aspectMask', VkImageAspectFlags), ('imageGranularity', VkExtent3D), ('flags', VkSparseImageFormatFlags)]
VkSparseImageMemoryRequirements._fields_ = [('formatProperties', VkSparseImageFormatProperties), ('imageMipTailFirstLod', ctypes.c_uint32), ('imageMipTailSize', VkDeviceSize), ('imageMipTailOffset', VkDeviceSize), ('imageMipTailStride', VkDeviceSize)]
VkMappedMemoryRange._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memory', VkDeviceMemory), ('offset', VkDeviceSize), ('size', VkDeviceSize)]
VkFormatProperties._fields_ = [('linearTilingFeatures', VkFormatFeatureFlags), ('optimalTilingFeatures', VkFormatFeatureFlags), ('bufferFeatures', VkFormatFeatureFlags)]
VkImageFormatProperties._fields_ = [('maxExtent', VkExtent3D), ('maxMipLevels', ctypes.c_uint32), ('maxArrayLayers', ctypes.c_uint32), ('sampleCounts', VkSampleCountFlags), ('maxResourceSize', VkDeviceSize)]
VkDescriptorBufferInfo._fields_ = [('buffer', VkBuffer), ('offset', VkDeviceSize), ('range', VkDeviceSize)]
VkDescriptorImageInfo._fields_ = [('sampler', VkSampler), ('imageView', VkImageView), ('imageLayout', VkImageLayout)]
VkWriteDescriptorSet._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('dstSet', VkDescriptorSet), ('dstBinding', ctypes.c_uint32), ('dstArrayElement', ctypes.c_uint32), ('descriptorCount', ctypes.c_uint32), ('descriptorType', VkDescriptorType), ('pImageInfo', ctypes.POINTER(VkDescriptorImageInfo)), ('pBufferInfo', ctypes.POINTER(VkDescriptorBufferInfo)), ('pTexelBufferView', ctypes.POINTER(VkBufferView))]
VkCopyDescriptorSet._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcSet', VkDescriptorSet), ('srcBinding', ctypes.c_uint32), ('srcArrayElement', ctypes.c_uint32), ('dstSet', VkDescriptorSet), ('dstBinding', ctypes.c_uint32), ('dstArrayElement', ctypes.c_uint32), ('descriptorCount', ctypes.c_uint32)]
VkBufferCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkBufferCreateFlags), ('size', VkDeviceSize), ('usage', VkBufferUsageFlags), ('sharingMode', VkSharingMode), ('queueFamilyIndexCount', ctypes.c_uint32), ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32))]
VkBufferViewCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkBufferViewCreateFlags), ('buffer', VkBuffer), ('format', VkFormat), ('offset', VkDeviceSize), ('range', VkDeviceSize)]
VkImageSubresource._fields_ = [('aspectMask', VkImageAspectFlags), ('mipLevel', ctypes.c_uint32), ('arrayLayer', ctypes.c_uint32)]
VkImageSubresourceLayers._fields_ = [('aspectMask', VkImageAspectFlags), ('mipLevel', ctypes.c_uint32), ('baseArrayLayer', ctypes.c_uint32), ('layerCount', ctypes.c_uint32)]
VkImageSubresourceRange._fields_ = [('aspectMask', VkImageAspectFlags), ('baseMipLevel', ctypes.c_uint32), ('levelCount', ctypes.c_uint32), ('baseArrayLayer', ctypes.c_uint32), ('layerCount', ctypes.c_uint32)]
VkMemoryBarrier._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcAccessMask', VkAccessFlags), ('dstAccessMask', VkAccessFlags)]
VkBufferMemoryBarrier._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcAccessMask', VkAccessFlags), ('dstAccessMask', VkAccessFlags), ('srcQueueFamilyIndex', ctypes.c_uint32), ('dstQueueFamilyIndex', ctypes.c_uint32), ('buffer', VkBuffer), ('offset', VkDeviceSize), ('size', VkDeviceSize)]
VkImageMemoryBarrier._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcAccessMask', VkAccessFlags), ('dstAccessMask', VkAccessFlags), ('oldLayout', VkImageLayout), ('newLayout', VkImageLayout), ('srcQueueFamilyIndex', ctypes.c_uint32), ('dstQueueFamilyIndex', ctypes.c_uint32), ('image', VkImage), ('subresourceRange', VkImageSubresourceRange)]
VkImageCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkImageCreateFlags), ('imageType', VkImageType), ('format', VkFormat), ('extent', VkExtent3D), ('mipLevels', ctypes.c_uint32), ('arrayLayers', ctypes.c_uint32), ('samples', VkSampleCountFlagBits), ('tiling', VkImageTiling), ('usage', VkImageUsageFlags), ('sharingMode', VkSharingMode), ('queueFamilyIndexCount', ctypes.c_uint32), ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)), ('initialLayout', VkImageLayout)]
VkSubresourceLayout._fields_ = [('offset', VkDeviceSize), ('size', VkDeviceSize), ('rowPitch', VkDeviceSize), ('arrayPitch', VkDeviceSize), ('depthPitch', VkDeviceSize)]
VkImageViewCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkImageViewCreateFlags), ('image', VkImage), ('viewType', VkImageViewType), ('format', VkFormat), ('components', VkComponentMapping), ('subresourceRange', VkImageSubresourceRange)]
VkBufferCopy._fields_ = [('srcOffset', VkDeviceSize), ('dstOffset', VkDeviceSize), ('size', VkDeviceSize)]
VkSparseMemoryBind._fields_ = [('resourceOffset', VkDeviceSize), ('size', VkDeviceSize), ('memory', VkDeviceMemory), ('memoryOffset', VkDeviceSize), ('flags', VkSparseMemoryBindFlags)]
VkSparseImageMemoryBind._fields_ = [('subresource', VkImageSubresource), ('offset', VkOffset3D), ('extent', VkExtent3D), ('memory', VkDeviceMemory), ('memoryOffset', VkDeviceSize), ('flags', VkSparseMemoryBindFlags)]
VkSparseBufferMemoryBindInfo._fields_ = [('buffer', VkBuffer), ('bindCount', ctypes.c_uint32), ('pBinds', ctypes.POINTER(VkSparseMemoryBind))]
VkSparseImageOpaqueMemoryBindInfo._fields_ = [('image', VkImage), ('bindCount', ctypes.c_uint32), ('pBinds', ctypes.POINTER(VkSparseMemoryBind))]
VkSparseImageMemoryBindInfo._fields_ = [('image', VkImage), ('bindCount', ctypes.c_uint32), ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind))]
VkBindSparseInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('waitSemaphoreCount', ctypes.c_uint32), ('pWaitSemaphores', ctypes.POINTER(VkSemaphore)), ('bufferBindCount', ctypes.c_uint32), ('pBufferBinds', ctypes.POINTER(VkSparseBufferMemoryBindInfo)), ('imageOpaqueBindCount', ctypes.c_uint32), ('pImageOpaqueBinds', ctypes.POINTER(VkSparseImageOpaqueMemoryBindInfo)), ('imageBindCount', ctypes.c_uint32), ('pImageBinds', ctypes.POINTER(VkSparseImageMemoryBindInfo)), ('signalSemaphoreCount', ctypes.c_uint32), ('pSignalSemaphores', ctypes.POINTER(VkSemaphore))]
VkImageCopy._fields_ = [('srcSubresource', VkImageSubresourceLayers), ('srcOffset', VkOffset3D), ('dstSubresource', VkImageSubresourceLayers), ('dstOffset', VkOffset3D), ('extent', VkExtent3D)]
VkImageBlit._fields_ = [('srcSubresource', VkImageSubresourceLayers), ('srcOffsets', (VkOffset3D * (2))), ('dstSubresource', VkImageSubresourceLayers), ('dstOffsets', (VkOffset3D * (2)))]
VkBufferImageCopy._fields_ = [('bufferOffset', VkDeviceSize), ('bufferRowLength', ctypes.c_uint32), ('bufferImageHeight', ctypes.c_uint32), ('imageSubresource', VkImageSubresourceLayers), ('imageOffset', VkOffset3D), ('imageExtent', VkExtent3D)]
VkImageResolve._fields_ = [('srcSubresource', VkImageSubresourceLayers), ('srcOffset', VkOffset3D), ('dstSubresource', VkImageSubresourceLayers), ('dstOffset', VkOffset3D), ('extent', VkExtent3D)]
VkShaderModuleCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkShaderModuleCreateFlags), ('codeSize', ctypes.c_size_t), ('pCode', ctypes.POINTER(ctypes.c_uint32))]
VkDescriptorSetLayoutBinding._fields_ = [('binding', ctypes.c_uint32), ('descriptorType', VkDescriptorType), ('descriptorCount', ctypes.c_uint32), ('stageFlags', VkShaderStageFlags), ('pImmutableSamplers', ctypes.POINTER(VkSampler))]
VkDescriptorSetLayoutCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDescriptorSetLayoutCreateFlags), ('bindingCount', ctypes.c_uint32), ('pBindings', ctypes.POINTER(VkDescriptorSetLayoutBinding))]
VkDescriptorPoolSize._fields_ = [('type', VkDescriptorType), ('descriptorCount', ctypes.c_uint32)]
VkDescriptorPoolCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDescriptorPoolCreateFlags), ('maxSets', ctypes.c_uint32), ('poolSizeCount', ctypes.c_uint32), ('pPoolSizes', ctypes.POINTER(VkDescriptorPoolSize))]
VkDescriptorSetAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('descriptorPool', VkDescriptorPool), ('descriptorSetCount', ctypes.c_uint32), ('pSetLayouts', ctypes.POINTER(VkDescriptorSetLayout))]
VkSpecializationMapEntry._fields_ = [('constantID', ctypes.c_uint32), ('offset', ctypes.c_uint32), ('size', ctypes.c_size_t)]
VkSpecializationInfo._fields_ = [('mapEntryCount', ctypes.c_uint32), ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)), ('dataSize', ctypes.c_size_t), ('pData', ctypes.c_void_p)]
VkPipelineShaderStageCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineShaderStageCreateFlags), ('stage', VkShaderStageFlagBits), ('module', VkShaderModule), ('pName', ctypes.c_char_p), ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo))]
VkComputePipelineCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCreateFlags), ('stage', VkPipelineShaderStageCreateInfo), ('layout', VkPipelineLayout), ('basePipelineHandle', VkPipeline), ('basePipelineIndex', ctypes.c_int32)]
VkVertexInputBindingDescription._fields_ = [('binding', ctypes.c_uint32), ('stride', ctypes.c_uint32), ('inputRate', VkVertexInputRate)]
VkVertexInputAttributeDescription._fields_ = [('location', ctypes.c_uint32), ('binding', ctypes.c_uint32), ('format', VkFormat), ('offset', ctypes.c_uint32)]
VkPipelineVertexInputStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineVertexInputStateCreateFlags), ('vertexBindingDescriptionCount', ctypes.c_uint32), ('pVertexBindingDescriptions', ctypes.POINTER(VkVertexInputBindingDescription)), ('vertexAttributeDescriptionCount', ctypes.c_uint32), ('pVertexAttributeDescriptions', ctypes.POINTER(VkVertexInputAttributeDescription))]
VkPipelineInputAssemblyStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineInputAssemblyStateCreateFlags), ('topology', VkPrimitiveTopology), ('primitiveRestartEnable', VkBool32)]
VkPipelineTessellationStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineTessellationStateCreateFlags), ('patchControlPoints', ctypes.c_uint32)]
VkPipelineViewportStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineViewportStateCreateFlags), ('viewportCount', ctypes.c_uint32), ('pViewports', ctypes.POINTER(VkViewport)), ('scissorCount', ctypes.c_uint32), ('pScissors', ctypes.POINTER(VkRect2D))]
VkPipelineRasterizationStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineRasterizationStateCreateFlags), ('depthClampEnable', VkBool32), ('rasterizerDiscardEnable', VkBool32), ('polygonMode', VkPolygonMode), ('cullMode', VkCullModeFlags), ('frontFace', VkFrontFace), ('depthBiasEnable', VkBool32), ('depthBiasConstantFactor', ctypes.c_float), ('depthBiasClamp', ctypes.c_float), ('depthBiasSlopeFactor', ctypes.c_float), ('lineWidth', ctypes.c_float)]
VkPipelineMultisampleStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineMultisampleStateCreateFlags), ('rasterizationSamples', VkSampleCountFlagBits), ('sampleShadingEnable', VkBool32), ('minSampleShading', ctypes.c_float), ('pSampleMask', ctypes.POINTER(VkSampleMask)), ('alphaToCoverageEnable', VkBool32), ('alphaToOneEnable', VkBool32)]
VkPipelineColorBlendAttachmentState._fields_ = [('blendEnable', VkBool32), ('srcColorBlendFactor', VkBlendFactor), ('dstColorBlendFactor', VkBlendFactor), ('colorBlendOp', VkBlendOp), ('srcAlphaBlendFactor', VkBlendFactor), ('dstAlphaBlendFactor', VkBlendFactor), ('alphaBlendOp', VkBlendOp), ('colorWriteMask', VkColorComponentFlags)]
VkPipelineColorBlendStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineColorBlendStateCreateFlags), ('logicOpEnable', VkBool32), ('logicOp', VkLogicOp), ('attachmentCount', ctypes.c_uint32), ('pAttachments', ctypes.POINTER(VkPipelineColorBlendAttachmentState)), ('blendConstants', (ctypes.c_float * (4)))]
VkPipelineDynamicStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineDynamicStateCreateFlags), ('dynamicStateCount', ctypes.c_uint32), ('pDynamicStates', ctypes.POINTER(VkDynamicState))]
VkStencilOpState._fields_ = [('failOp', VkStencilOp), ('passOp', VkStencilOp), ('depthFailOp', VkStencilOp), ('compareOp', VkCompareOp), ('compareMask', ctypes.c_uint32), ('writeMask', ctypes.c_uint32), ('reference', ctypes.c_uint32)]
VkPipelineDepthStencilStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineDepthStencilStateCreateFlags), ('depthTestEnable', VkBool32), ('depthWriteEnable', VkBool32), ('depthCompareOp', VkCompareOp), ('depthBoundsTestEnable', VkBool32), ('stencilTestEnable', VkBool32), ('front', VkStencilOpState), ('back', VkStencilOpState), ('minDepthBounds', ctypes.c_float), ('maxDepthBounds', ctypes.c_float)]
VkGraphicsPipelineCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCreateFlags), ('stageCount', ctypes.c_uint32), ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)), ('pVertexInputState', ctypes.POINTER(VkPipelineVertexInputStateCreateInfo)), ('pInputAssemblyState', ctypes.POINTER(VkPipelineInputAssemblyStateCreateInfo)), ('pTessellationState', ctypes.POINTER(VkPipelineTessellationStateCreateInfo)), ('pViewportState', ctypes.POINTER(VkPipelineViewportStateCreateInfo)), ('pRasterizationState', ctypes.POINTER(VkPipelineRasterizationStateCreateInfo)), ('pMultisampleState', ctypes.POINTER(VkPipelineMultisampleStateCreateInfo)), ('pDepthStencilState', ctypes.POINTER(VkPipelineDepthStencilStateCreateInfo)), ('pColorBlendState', ctypes.POINTER(VkPipelineColorBlendStateCreateInfo)), ('pDynamicState', ctypes.POINTER(VkPipelineDynamicStateCreateInfo)), ('layout', VkPipelineLayout), ('renderPass', VkRenderPass), ('subpass', ctypes.c_uint32), ('basePipelineHandle', VkPipeline), ('basePipelineIndex', ctypes.c_int32)]
VkPipelineCacheCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCacheCreateFlags), ('initialDataSize', ctypes.c_size_t), ('pInitialData', ctypes.c_void_p)]
VkPushConstantRange._fields_ = [('stageFlags', VkShaderStageFlags), ('offset', ctypes.c_uint32), ('size', ctypes.c_uint32)]
VkPipelineLayoutCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineLayoutCreateFlags), ('setLayoutCount', ctypes.c_uint32), ('pSetLayouts', ctypes.POINTER(VkDescriptorSetLayout)), ('pushConstantRangeCount', ctypes.c_uint32), ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange))]
VkSamplerCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkSamplerCreateFlags), ('magFilter', VkFilter), ('minFilter', VkFilter), ('mipmapMode', VkSamplerMipmapMode), ('addressModeU', VkSamplerAddressMode), ('addressModeV', VkSamplerAddressMode), ('addressModeW', VkSamplerAddressMode), ('mipLodBias', ctypes.c_float), ('anisotropyEnable', VkBool32), ('maxAnisotropy', ctypes.c_float), ('compareEnable', VkBool32), ('compareOp', VkCompareOp), ('minLod', ctypes.c_float), ('maxLod', ctypes.c_float), ('borderColor', VkBorderColor), ('unnormalizedCoordinates', VkBool32)]
VkCommandPoolCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkCommandPoolCreateFlags), ('queueFamilyIndex', ctypes.c_uint32)]
VkCommandBufferAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('commandPool', VkCommandPool), ('level', VkCommandBufferLevel), ('commandBufferCount', ctypes.c_uint32)]
VkCommandBufferInheritanceInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('renderPass', VkRenderPass), ('subpass', ctypes.c_uint32), ('framebuffer', VkFramebuffer), ('occlusionQueryEnable', VkBool32), ('queryFlags', VkQueryControlFlags), ('pipelineStatistics', VkQueryPipelineStatisticFlags)]
VkCommandBufferBeginInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkCommandBufferUsageFlags), ('pInheritanceInfo', ctypes.POINTER(VkCommandBufferInheritanceInfo))]
VkClearColorValue._fields_ = [('float32', (ctypes.c_float * (4))), ('int32', (ctypes.c_int32 * (4))), ('uint32', (ctypes.c_uint32 * (4)))]
VkClearDepthStencilValue._fields_ = [('depth', ctypes.c_float), ('stencil', ctypes.c_uint32)]
VkClearValue._fields_ = [('color', VkClearColorValue), ('depthStencil', VkClearDepthStencilValue)]
VkRenderPassBeginInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('renderPass', VkRenderPass), ('framebuffer', VkFramebuffer), ('renderArea', VkRect2D), ('clearValueCount', ctypes.c_uint32), ('pClearValues', ctypes.POINTER(VkClearValue))]
VkClearAttachment._fields_ = [('aspectMask', VkImageAspectFlags), ('colorAttachment', ctypes.c_uint32), ('clearValue', VkClearValue)]
VkAttachmentDescription._fields_ = [('flags', VkAttachmentDescriptionFlags), ('format', VkFormat), ('samples', VkSampleCountFlagBits), ('loadOp', VkAttachmentLoadOp), ('storeOp', VkAttachmentStoreOp), ('stencilLoadOp', VkAttachmentLoadOp), ('stencilStoreOp', VkAttachmentStoreOp), ('initialLayout', VkImageLayout), ('finalLayout', VkImageLayout)]
VkAttachmentReference._fields_ = [('attachment', ctypes.c_uint32), ('layout', VkImageLayout)]
VkSubpassDescription._fields_ = [('flags', VkSubpassDescriptionFlags), ('pipelineBindPoint', VkPipelineBindPoint), ('inputAttachmentCount', ctypes.c_uint32), ('pInputAttachments', ctypes.POINTER(VkAttachmentReference)), ('colorAttachmentCount', ctypes.c_uint32), ('pColorAttachments', ctypes.POINTER(VkAttachmentReference)), ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference)), ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference)), ('preserveAttachmentCount', ctypes.c_uint32), ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32))]
VkSubpassDependency._fields_ = [('srcSubpass', ctypes.c_uint32), ('dstSubpass', ctypes.c_uint32), ('srcStageMask', VkPipelineStageFlags), ('dstStageMask', VkPipelineStageFlags), ('srcAccessMask', VkAccessFlags), ('dstAccessMask', VkAccessFlags), ('dependencyFlags', VkDependencyFlags)]
VkRenderPassCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkRenderPassCreateFlags), ('attachmentCount', ctypes.c_uint32), ('pAttachments', ctypes.POINTER(VkAttachmentDescription)), ('subpassCount', ctypes.c_uint32), ('pSubpasses', ctypes.POINTER(VkSubpassDescription)), ('dependencyCount', ctypes.c_uint32), ('pDependencies', ctypes.POINTER(VkSubpassDependency))]
VkEventCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkEventCreateFlags)]
VkFenceCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkFenceCreateFlags)]
VkSemaphoreCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkSemaphoreCreateFlags)]
VkQueryPoolCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkQueryPoolCreateFlags), ('queryType', VkQueryType), ('queryCount', ctypes.c_uint32), ('pipelineStatistics', VkQueryPipelineStatisticFlags)]
VkFramebufferCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkFramebufferCreateFlags), ('renderPass', VkRenderPass), ('attachmentCount', ctypes.c_uint32), ('pAttachments', ctypes.POINTER(VkImageView)), ('width', ctypes.c_uint32), ('height', ctypes.c_uint32), ('layers', ctypes.c_uint32)]
VkDrawIndirectCommand._fields_ = [('vertexCount', ctypes.c_uint32), ('instanceCount', ctypes.c_uint32), ('firstVertex', ctypes.c_uint32), ('firstInstance', ctypes.c_uint32)]
VkDrawIndexedIndirectCommand._fields_ = [('indexCount', ctypes.c_uint32), ('instanceCount', ctypes.c_uint32), ('firstIndex', ctypes.c_uint32), ('vertexOffset', ctypes.c_int32), ('firstInstance', ctypes.c_uint32)]
VkDispatchIndirectCommand._fields_ = [('x', ctypes.c_uint32), ('y', ctypes.c_uint32), ('z', ctypes.c_uint32)]
VkSubmitInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('waitSemaphoreCount', ctypes.c_uint32), ('pWaitSemaphores', ctypes.POINTER(VkSemaphore)), ('pWaitDstStageMask', ctypes.POINTER(VkPipelineStageFlags)), ('commandBufferCount', ctypes.c_uint32), ('pCommandBuffers', ctypes.POINTER(VkCommandBuffer)), ('signalSemaphoreCount', ctypes.c_uint32), ('pSignalSemaphores', ctypes.POINTER(VkSemaphore))]
VkDisplayPropertiesKHR._fields_ = [('display', VkDisplayKHR), ('displayName', ctypes.c_char_p), ('physicalDimensions', VkExtent2D), ('physicalResolution', VkExtent2D), ('supportedTransforms', VkSurfaceTransformFlagsKHR), ('planeReorderPossible', VkBool32), ('persistentContent', VkBool32)]
VkDisplayPlanePropertiesKHR._fields_ = [('currentDisplay', VkDisplayKHR), ('currentStackIndex', ctypes.c_uint32)]
VkDisplayModeParametersKHR._fields_ = [('visibleRegion', VkExtent2D), ('refreshRate', ctypes.c_uint32)]
VkDisplayModePropertiesKHR._fields_ = [('displayMode', VkDisplayModeKHR), ('parameters', VkDisplayModeParametersKHR)]
VkDisplayModeCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDisplayModeCreateFlagsKHR), ('parameters', VkDisplayModeParametersKHR)]
VkDisplayPlaneCapabilitiesKHR._fields_ = [('supportedAlpha', VkDisplayPlaneAlphaFlagsKHR), ('minSrcPosition', VkOffset2D), ('maxSrcPosition', VkOffset2D), ('minSrcExtent', VkExtent2D), ('maxSrcExtent', VkExtent2D), ('minDstPosition', VkOffset2D), ('maxDstPosition', VkOffset2D), ('minDstExtent', VkExtent2D), ('maxDstExtent', VkExtent2D)]
VkDisplaySurfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDisplaySurfaceCreateFlagsKHR), ('displayMode', VkDisplayModeKHR), ('planeIndex', ctypes.c_uint32), ('planeStackIndex', ctypes.c_uint32), ('transform', VkSurfaceTransformFlagBitsKHR), ('globalAlpha', ctypes.c_float), ('alphaMode', VkDisplayPlaneAlphaFlagBitsKHR), ('imageExtent', VkExtent2D)]
VkDisplayPresentInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcRect', VkRect2D), ('dstRect', VkRect2D), ('persistent', VkBool32)]
VkSurfaceCapabilitiesKHR._fields_ = [('minImageCount', ctypes.c_uint32), ('maxImageCount', ctypes.c_uint32), ('currentExtent', VkExtent2D), ('minImageExtent', VkExtent2D), ('maxImageExtent', VkExtent2D), ('maxImageArrayLayers', ctypes.c_uint32), ('supportedTransforms', VkSurfaceTransformFlagsKHR), ('currentTransform', VkSurfaceTransformFlagBitsKHR), ('supportedCompositeAlpha', VkCompositeAlphaFlagsKHR), ('supportedUsageFlags', VkImageUsageFlags)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidSurfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkAndroidSurfaceCreateFlagsKHR), ('window', ctypes.POINTER(ANativeWindow))]
if VK_USE_PLATFORM_VI_NN:
    VkViSurfaceCreateInfoNN._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkViSurfaceCreateFlagsNN), ('window', ctypes.c_void_p)]
if VK_USE_PLATFORM_WAYLAND_KHR:
    VkWaylandSurfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkWaylandSurfaceCreateFlagsKHR), ('display', ctypes.POINTER(wl_display)), ('surface', ctypes.POINTER(wl_surface))]
if VK_USE_PLATFORM_WIN32_KHR:
    VkWin32SurfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkWin32SurfaceCreateFlagsKHR), ('hinstance', ctypes.wintypes.HINSTANCE), ('hwnd', ctypes.wintypes.HWND)]
if VK_USE_PLATFORM_XLIB_KHR:
    VkXlibSurfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkXlibSurfaceCreateFlagsKHR), ('dpy', ctypes.POINTER(Display)), ('window', Window)]
if VK_USE_PLATFORM_XCB_KHR:
    VkXcbSurfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkXcbSurfaceCreateFlagsKHR), ('connection', ctypes.POINTER(xcb_connection_t)), ('window', xcb_window_t)]
if VK_USE_PLATFORM_DIRECTFB_EXT:
    VkDirectFBSurfaceCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDirectFBSurfaceCreateFlagsEXT), ('dfb', ctypes.POINTER(IDirectFB)), ('surface', ctypes.POINTER(IDirectFBSurface))]
if VK_USE_PLATFORM_FUCHSIA:
    VkImagePipeSurfaceCreateInfoFUCHSIA._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkImagePipeSurfaceCreateFlagsFUCHSIA), ('imagePipeHandle', zx_handle_t)]
if VK_USE_PLATFORM_GGP:
    VkStreamDescriptorSurfaceCreateInfoGGP._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkStreamDescriptorSurfaceCreateFlagsGGP), ('streamDescriptor', GgpStreamDescriptor)]
VkSurfaceFormatKHR._fields_ = [('format', VkFormat), ('colorSpace', VkColorSpaceKHR)]
VkSwapchainCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkSwapchainCreateFlagsKHR), ('surface', VkSurfaceKHR), ('minImageCount', ctypes.c_uint32), ('imageFormat', VkFormat), ('imageColorSpace', VkColorSpaceKHR), ('imageExtent', VkExtent2D), ('imageArrayLayers', ctypes.c_uint32), ('imageUsage', VkImageUsageFlags), ('imageSharingMode', VkSharingMode), ('queueFamilyIndexCount', ctypes.c_uint32), ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)), ('preTransform', VkSurfaceTransformFlagBitsKHR), ('compositeAlpha', VkCompositeAlphaFlagBitsKHR), ('presentMode', VkPresentModeKHR), ('clipped', VkBool32), ('oldSwapchain', VkSwapchainKHR)]
VkPresentInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('waitSemaphoreCount', ctypes.c_uint32), ('pWaitSemaphores', ctypes.POINTER(VkSemaphore)), ('swapchainCount', ctypes.c_uint32), ('pSwapchains', ctypes.POINTER(VkSwapchainKHR)), ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)), ('pResults', ctypes.POINTER(VkResult))]
VkDebugReportCallbackCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDebugReportFlagsEXT), ('pfnCallback', PFN_vkDebugReportCallbackEXT), ('pUserData', ctypes.c_void_p)]
VkValidationFlagsEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('disabledValidationCheckCount', ctypes.c_uint32), ('pDisabledValidationChecks', ctypes.POINTER(VkValidationCheckEXT))]
VkValidationFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('enabledValidationFeatureCount', ctypes.c_uint32), ('pEnabledValidationFeatures', ctypes.POINTER(VkValidationFeatureEnableEXT)), ('disabledValidationFeatureCount', ctypes.c_uint32), ('pDisabledValidationFeatures', ctypes.POINTER(VkValidationFeatureDisableEXT))]
VkPipelineRasterizationStateRasterizationOrderAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('rasterizationOrder', VkRasterizationOrderAMD)]
VkDebugMarkerObjectNameInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('objectType', VkDebugReportObjectTypeEXT), ('object', ctypes.c_uint64), ('pObjectName', ctypes.c_char_p)]
VkDebugMarkerObjectTagInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('objectType', VkDebugReportObjectTypeEXT), ('object', ctypes.c_uint64), ('tagName', ctypes.c_uint64), ('tagSize', ctypes.c_size_t), ('pTag', ctypes.c_void_p)]
VkDebugMarkerMarkerInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pMarkerName', ctypes.c_char_p), ('color', (ctypes.c_float * (4)))]
VkDedicatedAllocationImageCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('dedicatedAllocation', VkBool32)]
VkDedicatedAllocationBufferCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('dedicatedAllocation', VkBool32)]
VkDedicatedAllocationMemoryAllocateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('image', VkImage), ('buffer', VkBuffer)]
VkExternalImageFormatPropertiesNV._fields_ = [('imageFormatProperties', VkImageFormatProperties), ('externalMemoryFeatures', VkExternalMemoryFeatureFlagsNV), ('exportFromImportedHandleTypes', VkExternalMemoryHandleTypeFlagsNV), ('compatibleHandleTypes', VkExternalMemoryHandleTypeFlagsNV)]
VkExternalMemoryImageCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalMemoryHandleTypeFlagsNV)]
VkExportMemoryAllocateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalMemoryHandleTypeFlagsNV)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportMemoryWin32HandleInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalMemoryHandleTypeFlagsNV), ('handle', ctypes.wintypes.HANDLE)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportMemoryWin32HandleInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pAttributes', ctypes.POINTER(SECURITY_ATTRIBUTES)), ('dwAccess', ctypes.wintypes.DWORD)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkWin32KeyedMutexAcquireReleaseInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('acquireCount', ctypes.c_uint32), ('pAcquireSyncs', ctypes.POINTER(VkDeviceMemory)), ('pAcquireKeys', ctypes.POINTER(ctypes.c_uint64)), ('pAcquireTimeoutMilliseconds', ctypes.POINTER(ctypes.c_uint32)), ('releaseCount', ctypes.c_uint32), ('pReleaseSyncs', ctypes.POINTER(VkDeviceMemory)), ('pReleaseKeys', ctypes.POINTER(ctypes.c_uint64))]
VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceGeneratedCommands', VkBool32)]
VkDevicePrivateDataCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('privateDataSlotRequestCount', ctypes.c_uint32)]
VkPrivateDataSlotCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPrivateDataSlotCreateFlagsEXT)]
VkPhysicalDevicePrivateDataFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('privateData', VkBool32)]
VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxGraphicsShaderGroupCount', ctypes.c_uint32), ('maxIndirectSequenceCount', ctypes.c_uint32), ('maxIndirectCommandsTokenCount', ctypes.c_uint32), ('maxIndirectCommandsStreamCount', ctypes.c_uint32), ('maxIndirectCommandsTokenOffset', ctypes.c_uint32), ('maxIndirectCommandsStreamStride', ctypes.c_uint32), ('minSequencesCountBufferOffsetAlignment', ctypes.c_uint32), ('minSequencesIndexBufferOffsetAlignment', ctypes.c_uint32), ('minIndirectCommandsBufferOffsetAlignment', ctypes.c_uint32)]
VkGraphicsShaderGroupCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('stageCount', ctypes.c_uint32), ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)), ('pVertexInputState', ctypes.POINTER(VkPipelineVertexInputStateCreateInfo)), ('pTessellationState', ctypes.POINTER(VkPipelineTessellationStateCreateInfo))]
VkGraphicsPipelineShaderGroupsCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('groupCount', ctypes.c_uint32), ('pGroups', ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV)), ('pipelineCount', ctypes.c_uint32), ('pPipelines', ctypes.POINTER(VkPipeline))]
VkBindShaderGroupIndirectCommandNV._fields_ = [('groupIndex', ctypes.c_uint32)]
VkBindIndexBufferIndirectCommandNV._fields_ = [('bufferAddress', VkDeviceAddress), ('size', ctypes.c_uint32), ('indexType', VkIndexType)]
VkBindVertexBufferIndirectCommandNV._fields_ = [('bufferAddress', VkDeviceAddress), ('size', ctypes.c_uint32), ('stride', ctypes.c_uint32)]
VkSetStateFlagsIndirectCommandNV._fields_ = [('data', ctypes.c_uint32)]
VkIndirectCommandsStreamNV._fields_ = [('buffer', VkBuffer), ('offset', VkDeviceSize)]
VkIndirectCommandsLayoutTokenNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('tokenType', VkIndirectCommandsTokenTypeNV), ('stream', ctypes.c_uint32), ('offset', ctypes.c_uint32), ('vertexBindingUnit', ctypes.c_uint32), ('vertexDynamicStride', VkBool32), ('pushconstantPipelineLayout', VkPipelineLayout), ('pushconstantShaderStageFlags', VkShaderStageFlags), ('pushconstantOffset', ctypes.c_uint32), ('pushconstantSize', ctypes.c_uint32), ('indirectStateFlags', VkIndirectStateFlagsNV), ('indexTypeCount', ctypes.c_uint32), ('pIndexTypes', ctypes.POINTER(VkIndexType)), ('pIndexTypeValues', ctypes.POINTER(ctypes.c_uint32))]
VkIndirectCommandsLayoutCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkIndirectCommandsLayoutUsageFlagsNV), ('pipelineBindPoint', VkPipelineBindPoint), ('tokenCount', ctypes.c_uint32), ('pTokens', ctypes.POINTER(VkIndirectCommandsLayoutTokenNV)), ('streamCount', ctypes.c_uint32), ('pStreamStrides', ctypes.POINTER(ctypes.c_uint32))]
VkGeneratedCommandsInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipelineBindPoint', VkPipelineBindPoint), ('pipeline', VkPipeline), ('indirectCommandsLayout', VkIndirectCommandsLayoutNV), ('streamCount', ctypes.c_uint32), ('pStreams', ctypes.POINTER(VkIndirectCommandsStreamNV)), ('sequencesCount', ctypes.c_uint32), ('preprocessBuffer', VkBuffer), ('preprocessOffset', VkDeviceSize), ('preprocessSize', VkDeviceSize), ('sequencesCountBuffer', VkBuffer), ('sequencesCountOffset', VkDeviceSize), ('sequencesIndexBuffer', VkBuffer), ('sequencesIndexOffset', VkDeviceSize)]
VkGeneratedCommandsMemoryRequirementsInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipelineBindPoint', VkPipelineBindPoint), ('pipeline', VkPipeline), ('indirectCommandsLayout', VkIndirectCommandsLayoutNV), ('maxSequencesCount', ctypes.c_uint32)]
VkPhysicalDeviceFeatures2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('features', VkPhysicalDeviceFeatures)]
VkPhysicalDeviceFeatures2KHR = type('VkPhysicalDeviceFeatures2KHR', (VkPhysicalDeviceFeatures2,), dict())
VkPhysicalDeviceProperties2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('properties', VkPhysicalDeviceProperties)]
VkPhysicalDeviceProperties2KHR = type('VkPhysicalDeviceProperties2KHR', (VkPhysicalDeviceProperties2,), dict())
VkFormatProperties2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('formatProperties', VkFormatProperties)]
VkFormatProperties2KHR = type('VkFormatProperties2KHR', (VkFormatProperties2,), dict())
VkImageFormatProperties2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('imageFormatProperties', VkImageFormatProperties)]
VkImageFormatProperties2KHR = type('VkImageFormatProperties2KHR', (VkImageFormatProperties2,), dict())
VkPhysicalDeviceImageFormatInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('format', VkFormat), ('type', VkImageType), ('tiling', VkImageTiling), ('usage', VkImageUsageFlags), ('flags', VkImageCreateFlags)]
VkPhysicalDeviceImageFormatInfo2KHR = type('VkPhysicalDeviceImageFormatInfo2KHR', (VkPhysicalDeviceImageFormatInfo2,), dict())
VkQueueFamilyProperties2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('queueFamilyProperties', VkQueueFamilyProperties)]
VkQueueFamilyProperties2KHR = type('VkQueueFamilyProperties2KHR', (VkQueueFamilyProperties2,), dict())
VkPhysicalDeviceMemoryProperties2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryProperties', VkPhysicalDeviceMemoryProperties)]
VkPhysicalDeviceMemoryProperties2KHR = type('VkPhysicalDeviceMemoryProperties2KHR', (VkPhysicalDeviceMemoryProperties2,), dict())
VkSparseImageFormatProperties2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('properties', VkSparseImageFormatProperties)]
VkSparseImageFormatProperties2KHR = type('VkSparseImageFormatProperties2KHR', (VkSparseImageFormatProperties2,), dict())
VkPhysicalDeviceSparseImageFormatInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('format', VkFormat), ('type', VkImageType), ('samples', VkSampleCountFlagBits), ('usage', VkImageUsageFlags), ('tiling', VkImageTiling)]
VkPhysicalDeviceSparseImageFormatInfo2KHR = type('VkPhysicalDeviceSparseImageFormatInfo2KHR', (VkPhysicalDeviceSparseImageFormatInfo2,), dict())
VkPhysicalDevicePushDescriptorPropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxPushDescriptors', ctypes.c_uint32)]
VkConformanceVersion._fields_ = [('major', ctypes.c_uint8), ('minor', ctypes.c_uint8), ('subminor', ctypes.c_uint8), ('patch', ctypes.c_uint8)]
VkConformanceVersionKHR = type('VkConformanceVersionKHR', (VkConformanceVersion,), dict())
VkPhysicalDeviceDriverProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('driverID', VkDriverId), ('driverName', (ctypes.c_char * (VK_MAX_DRIVER_NAME_SIZE))), ('driverInfo', (ctypes.c_char * (VK_MAX_DRIVER_INFO_SIZE))), ('conformanceVersion', VkConformanceVersion)]
VkPhysicalDeviceDriverPropertiesKHR = type('VkPhysicalDeviceDriverPropertiesKHR', (VkPhysicalDeviceDriverProperties,), dict())
VkRectLayerKHR._fields_ = [('offset', VkOffset2D), ('extent', VkExtent2D), ('layer', ctypes.c_uint32)]
VkPresentRegionKHR._fields_ = [('rectangleCount', ctypes.c_uint32), ('pRectangles', ctypes.POINTER(VkRectLayerKHR))]
VkPresentRegionsKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('swapchainCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkPresentRegionKHR))]
VkPhysicalDeviceVariablePointersFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('variablePointersStorageBuffer', VkBool32), ('variablePointers', VkBool32)]
VkPhysicalDeviceVariablePointersFeaturesKHR = type('VkPhysicalDeviceVariablePointersFeaturesKHR', (VkPhysicalDeviceVariablePointersFeatures,), dict())
VkPhysicalDeviceVariablePointerFeaturesKHR = type('VkPhysicalDeviceVariablePointerFeaturesKHR', (VkPhysicalDeviceVariablePointersFeatures,), dict())
VkPhysicalDeviceVariablePointerFeatures = type('VkPhysicalDeviceVariablePointerFeatures', (VkPhysicalDeviceVariablePointersFeatures,), dict())
VkExternalMemoryProperties._fields_ = [('externalMemoryFeatures', VkExternalMemoryFeatureFlags), ('exportFromImportedHandleTypes', VkExternalMemoryHandleTypeFlags), ('compatibleHandleTypes', VkExternalMemoryHandleTypeFlags)]
VkExternalMemoryPropertiesKHR = type('VkExternalMemoryPropertiesKHR', (VkExternalMemoryProperties,), dict())
VkPhysicalDeviceExternalImageFormatInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalMemoryHandleTypeFlagBits)]
VkPhysicalDeviceExternalImageFormatInfoKHR = type('VkPhysicalDeviceExternalImageFormatInfoKHR', (VkPhysicalDeviceExternalImageFormatInfo,), dict())
VkExternalImageFormatProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('externalMemoryProperties', VkExternalMemoryProperties)]
VkExternalImageFormatPropertiesKHR = type('VkExternalImageFormatPropertiesKHR', (VkExternalImageFormatProperties,), dict())
VkPhysicalDeviceExternalBufferInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkBufferCreateFlags), ('usage', VkBufferUsageFlags), ('handleType', VkExternalMemoryHandleTypeFlagBits)]
VkPhysicalDeviceExternalBufferInfoKHR = type('VkPhysicalDeviceExternalBufferInfoKHR', (VkPhysicalDeviceExternalBufferInfo,), dict())
VkExternalBufferProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('externalMemoryProperties', VkExternalMemoryProperties)]
VkExternalBufferPropertiesKHR = type('VkExternalBufferPropertiesKHR', (VkExternalBufferProperties,), dict())
VkPhysicalDeviceIDProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceUUID', (ctypes.c_uint8 * (VK_UUID_SIZE))), ('driverUUID', (ctypes.c_uint8 * (VK_UUID_SIZE))), ('deviceLUID', (ctypes.c_uint8 * (VK_LUID_SIZE))), ('deviceNodeMask', ctypes.c_uint32), ('deviceLUIDValid', VkBool32)]
VkPhysicalDeviceIDPropertiesKHR = type('VkPhysicalDeviceIDPropertiesKHR', (VkPhysicalDeviceIDProperties,), dict())
VkExternalMemoryImageCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalMemoryHandleTypeFlags)]
VkExternalMemoryImageCreateInfoKHR = type('VkExternalMemoryImageCreateInfoKHR', (VkExternalMemoryImageCreateInfo,), dict())
VkExternalMemoryBufferCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalMemoryHandleTypeFlags)]
VkExternalMemoryBufferCreateInfoKHR = type('VkExternalMemoryBufferCreateInfoKHR', (VkExternalMemoryBufferCreateInfo,), dict())
VkExportMemoryAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalMemoryHandleTypeFlags)]
VkExportMemoryAllocateInfoKHR = type('VkExportMemoryAllocateInfoKHR', (VkExportMemoryAllocateInfo,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportMemoryWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalMemoryHandleTypeFlagBits), ('handle', ctypes.wintypes.HANDLE), ('name', ctypes.wintypes.LPCWSTR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportMemoryWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pAttributes', ctypes.POINTER(SECURITY_ATTRIBUTES)), ('dwAccess', ctypes.wintypes.DWORD), ('name', ctypes.wintypes.LPCWSTR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkMemoryWin32HandlePropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryTypeBits', ctypes.c_uint32)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkMemoryGetWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memory', VkDeviceMemory), ('handleType', VkExternalMemoryHandleTypeFlagBits)]
VkImportMemoryFdInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalMemoryHandleTypeFlagBits), ('fd', ctypes.c_int)]
VkMemoryFdPropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryTypeBits', ctypes.c_uint32)]
VkMemoryGetFdInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memory', VkDeviceMemory), ('handleType', VkExternalMemoryHandleTypeFlagBits)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkWin32KeyedMutexAcquireReleaseInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('acquireCount', ctypes.c_uint32), ('pAcquireSyncs', ctypes.POINTER(VkDeviceMemory)), ('pAcquireKeys', ctypes.POINTER(ctypes.c_uint64)), ('pAcquireTimeouts', ctypes.POINTER(ctypes.c_uint32)), ('releaseCount', ctypes.c_uint32), ('pReleaseSyncs', ctypes.POINTER(VkDeviceMemory)), ('pReleaseKeys', ctypes.POINTER(ctypes.c_uint64))]
VkPhysicalDeviceExternalSemaphoreInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalSemaphoreHandleTypeFlagBits)]
VkPhysicalDeviceExternalSemaphoreInfoKHR = type('VkPhysicalDeviceExternalSemaphoreInfoKHR', (VkPhysicalDeviceExternalSemaphoreInfo,), dict())
VkExternalSemaphoreProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('exportFromImportedHandleTypes', VkExternalSemaphoreHandleTypeFlags), ('compatibleHandleTypes', VkExternalSemaphoreHandleTypeFlags), ('externalSemaphoreFeatures', VkExternalSemaphoreFeatureFlags)]
VkExternalSemaphorePropertiesKHR = type('VkExternalSemaphorePropertiesKHR', (VkExternalSemaphoreProperties,), dict())
VkExportSemaphoreCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalSemaphoreHandleTypeFlags)]
VkExportSemaphoreCreateInfoKHR = type('VkExportSemaphoreCreateInfoKHR', (VkExportSemaphoreCreateInfo,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportSemaphoreWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('semaphore', VkSemaphore), ('flags', VkSemaphoreImportFlags), ('handleType', VkExternalSemaphoreHandleTypeFlagBits), ('handle', ctypes.wintypes.HANDLE), ('name', ctypes.wintypes.LPCWSTR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportSemaphoreWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pAttributes', ctypes.POINTER(SECURITY_ATTRIBUTES)), ('dwAccess', ctypes.wintypes.DWORD), ('name', ctypes.wintypes.LPCWSTR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkD3D12FenceSubmitInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('waitSemaphoreValuesCount', ctypes.c_uint32), ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)), ('signalSemaphoreValuesCount', ctypes.c_uint32), ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64))]
if VK_USE_PLATFORM_WIN32_KHR:
    VkSemaphoreGetWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('semaphore', VkSemaphore), ('handleType', VkExternalSemaphoreHandleTypeFlagBits)]
VkImportSemaphoreFdInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('semaphore', VkSemaphore), ('flags', VkSemaphoreImportFlags), ('handleType', VkExternalSemaphoreHandleTypeFlagBits), ('fd', ctypes.c_int)]
VkSemaphoreGetFdInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('semaphore', VkSemaphore), ('handleType', VkExternalSemaphoreHandleTypeFlagBits)]
VkPhysicalDeviceExternalFenceInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalFenceHandleTypeFlagBits)]
VkPhysicalDeviceExternalFenceInfoKHR = type('VkPhysicalDeviceExternalFenceInfoKHR', (VkPhysicalDeviceExternalFenceInfo,), dict())
VkExternalFenceProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('exportFromImportedHandleTypes', VkExternalFenceHandleTypeFlags), ('compatibleHandleTypes', VkExternalFenceHandleTypeFlags), ('externalFenceFeatures', VkExternalFenceFeatureFlags)]
VkExternalFencePropertiesKHR = type('VkExternalFencePropertiesKHR', (VkExternalFenceProperties,), dict())
VkExportFenceCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleTypes', VkExternalFenceHandleTypeFlags)]
VkExportFenceCreateInfoKHR = type('VkExportFenceCreateInfoKHR', (VkExportFenceCreateInfo,), dict())
if VK_USE_PLATFORM_WIN32_KHR:
    VkImportFenceWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fence', VkFence), ('flags', VkFenceImportFlags), ('handleType', VkExternalFenceHandleTypeFlagBits), ('handle', ctypes.wintypes.HANDLE), ('name', ctypes.wintypes.LPCWSTR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkExportFenceWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pAttributes', ctypes.POINTER(SECURITY_ATTRIBUTES)), ('dwAccess', ctypes.wintypes.DWORD), ('name', ctypes.wintypes.LPCWSTR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkFenceGetWin32HandleInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fence', VkFence), ('handleType', VkExternalFenceHandleTypeFlagBits)]
VkImportFenceFdInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fence', VkFence), ('flags', VkFenceImportFlags), ('handleType', VkExternalFenceHandleTypeFlagBits), ('fd', ctypes.c_int)]
VkFenceGetFdInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fence', VkFence), ('handleType', VkExternalFenceHandleTypeFlagBits)]
VkPhysicalDeviceMultiviewFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('multiview', VkBool32), ('multiviewGeometryShader', VkBool32), ('multiviewTessellationShader', VkBool32)]
VkPhysicalDeviceMultiviewFeaturesKHR = type('VkPhysicalDeviceMultiviewFeaturesKHR', (VkPhysicalDeviceMultiviewFeatures,), dict())
VkPhysicalDeviceMultiviewProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxMultiviewViewCount', ctypes.c_uint32), ('maxMultiviewInstanceIndex', ctypes.c_uint32)]
VkPhysicalDeviceMultiviewPropertiesKHR = type('VkPhysicalDeviceMultiviewPropertiesKHR', (VkPhysicalDeviceMultiviewProperties,), dict())
VkRenderPassMultiviewCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('subpassCount', ctypes.c_uint32), ('pViewMasks', ctypes.POINTER(ctypes.c_uint32)), ('dependencyCount', ctypes.c_uint32), ('pViewOffsets', ctypes.POINTER(ctypes.c_int32)), ('correlationMaskCount', ctypes.c_uint32), ('pCorrelationMasks', ctypes.POINTER(ctypes.c_uint32))]
VkRenderPassMultiviewCreateInfoKHR = type('VkRenderPassMultiviewCreateInfoKHR', (VkRenderPassMultiviewCreateInfo,), dict())
VkSurfaceCapabilities2EXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('minImageCount', ctypes.c_uint32), ('maxImageCount', ctypes.c_uint32), ('currentExtent', VkExtent2D), ('minImageExtent', VkExtent2D), ('maxImageExtent', VkExtent2D), ('maxImageArrayLayers', ctypes.c_uint32), ('supportedTransforms', VkSurfaceTransformFlagsKHR), ('currentTransform', VkSurfaceTransformFlagBitsKHR), ('supportedCompositeAlpha', VkCompositeAlphaFlagsKHR), ('supportedUsageFlags', VkImageUsageFlags), ('supportedSurfaceCounters', VkSurfaceCounterFlagsEXT)]
VkDisplayPowerInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('powerState', VkDisplayPowerStateEXT)]
VkDeviceEventInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceEvent', VkDeviceEventTypeEXT)]
VkDisplayEventInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('displayEvent', VkDisplayEventTypeEXT)]
VkSwapchainCounterCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('surfaceCounters', VkSurfaceCounterFlagsEXT)]
VkPhysicalDeviceGroupProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('physicalDeviceCount', ctypes.c_uint32), ('physicalDevices', (VkPhysicalDevice * (VK_MAX_DEVICE_GROUP_SIZE))), ('subsetAllocation', VkBool32)]
VkPhysicalDeviceGroupPropertiesKHR = type('VkPhysicalDeviceGroupPropertiesKHR', (VkPhysicalDeviceGroupProperties,), dict())
VkMemoryAllocateFlagsInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkMemoryAllocateFlags), ('deviceMask', ctypes.c_uint32)]
VkMemoryAllocateFlagsInfoKHR = type('VkMemoryAllocateFlagsInfoKHR', (VkMemoryAllocateFlagsInfo,), dict())
VkBindBufferMemoryInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('buffer', VkBuffer), ('memory', VkDeviceMemory), ('memoryOffset', VkDeviceSize)]
VkBindBufferMemoryInfoKHR = type('VkBindBufferMemoryInfoKHR', (VkBindBufferMemoryInfo,), dict())
VkBindBufferMemoryDeviceGroupInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceIndexCount', ctypes.c_uint32), ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32))]
VkBindBufferMemoryDeviceGroupInfoKHR = type('VkBindBufferMemoryDeviceGroupInfoKHR', (VkBindBufferMemoryDeviceGroupInfo,), dict())
VkBindImageMemoryInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('image', VkImage), ('memory', VkDeviceMemory), ('memoryOffset', VkDeviceSize)]
VkBindImageMemoryInfoKHR = type('VkBindImageMemoryInfoKHR', (VkBindImageMemoryInfo,), dict())
VkBindImageMemoryDeviceGroupInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceIndexCount', ctypes.c_uint32), ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)), ('splitInstanceBindRegionCount', ctypes.c_uint32), ('pSplitInstanceBindRegions', ctypes.POINTER(VkRect2D))]
VkBindImageMemoryDeviceGroupInfoKHR = type('VkBindImageMemoryDeviceGroupInfoKHR', (VkBindImageMemoryDeviceGroupInfo,), dict())
VkDeviceGroupRenderPassBeginInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceMask', ctypes.c_uint32), ('deviceRenderAreaCount', ctypes.c_uint32), ('pDeviceRenderAreas', ctypes.POINTER(VkRect2D))]
VkDeviceGroupRenderPassBeginInfoKHR = type('VkDeviceGroupRenderPassBeginInfoKHR', (VkDeviceGroupRenderPassBeginInfo,), dict())
VkDeviceGroupCommandBufferBeginInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceMask', ctypes.c_uint32)]
VkDeviceGroupCommandBufferBeginInfoKHR = type('VkDeviceGroupCommandBufferBeginInfoKHR', (VkDeviceGroupCommandBufferBeginInfo,), dict())
VkDeviceGroupSubmitInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('waitSemaphoreCount', ctypes.c_uint32), ('pWaitSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)), ('commandBufferCount', ctypes.c_uint32), ('pCommandBufferDeviceMasks', ctypes.POINTER(ctypes.c_uint32)), ('signalSemaphoreCount', ctypes.c_uint32), ('pSignalSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32))]
VkDeviceGroupSubmitInfoKHR = type('VkDeviceGroupSubmitInfoKHR', (VkDeviceGroupSubmitInfo,), dict())
VkDeviceGroupBindSparseInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('resourceDeviceIndex', ctypes.c_uint32), ('memoryDeviceIndex', ctypes.c_uint32)]
VkDeviceGroupBindSparseInfoKHR = type('VkDeviceGroupBindSparseInfoKHR', (VkDeviceGroupBindSparseInfo,), dict())
VkDeviceGroupPresentCapabilitiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('presentMask', (ctypes.c_uint32 * (VK_MAX_DEVICE_GROUP_SIZE))), ('modes', VkDeviceGroupPresentModeFlagsKHR)]
VkImageSwapchainCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('swapchain', VkSwapchainKHR)]
VkBindImageMemorySwapchainInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('swapchain', VkSwapchainKHR), ('imageIndex', ctypes.c_uint32)]
VkAcquireNextImageInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('swapchain', VkSwapchainKHR), ('timeout', ctypes.c_uint64), ('semaphore', VkSemaphore), ('fence', VkFence), ('deviceMask', ctypes.c_uint32)]
VkDeviceGroupPresentInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('swapchainCount', ctypes.c_uint32), ('pDeviceMasks', ctypes.POINTER(ctypes.c_uint32)), ('mode', VkDeviceGroupPresentModeFlagBitsKHR)]
VkDeviceGroupDeviceCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('physicalDeviceCount', ctypes.c_uint32), ('pPhysicalDevices', ctypes.POINTER(VkPhysicalDevice))]
VkDeviceGroupDeviceCreateInfoKHR = type('VkDeviceGroupDeviceCreateInfoKHR', (VkDeviceGroupDeviceCreateInfo,), dict())
VkDeviceGroupSwapchainCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('modes', VkDeviceGroupPresentModeFlagsKHR)]
VkDescriptorUpdateTemplateEntry._fields_ = [('dstBinding', ctypes.c_uint32), ('dstArrayElement', ctypes.c_uint32), ('descriptorCount', ctypes.c_uint32), ('descriptorType', VkDescriptorType), ('offset', ctypes.c_size_t), ('stride', ctypes.c_size_t)]
VkDescriptorUpdateTemplateEntryKHR = type('VkDescriptorUpdateTemplateEntryKHR', (VkDescriptorUpdateTemplateEntry,), dict())
VkDescriptorUpdateTemplateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDescriptorUpdateTemplateCreateFlags), ('descriptorUpdateEntryCount', ctypes.c_uint32), ('pDescriptorUpdateEntries', ctypes.POINTER(VkDescriptorUpdateTemplateEntry)), ('templateType', VkDescriptorUpdateTemplateType), ('descriptorSetLayout', VkDescriptorSetLayout), ('pipelineBindPoint', VkPipelineBindPoint), ('pipelineLayout', VkPipelineLayout), ('set', ctypes.c_uint32)]
VkDescriptorUpdateTemplateCreateInfoKHR = type('VkDescriptorUpdateTemplateCreateInfoKHR', (VkDescriptorUpdateTemplateCreateInfo,), dict())
VkXYColorEXT._fields_ = [('x', ctypes.c_float), ('y', ctypes.c_float)]
VkHdrMetadataEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('displayPrimaryRed', VkXYColorEXT), ('displayPrimaryGreen', VkXYColorEXT), ('displayPrimaryBlue', VkXYColorEXT), ('whitePoint', VkXYColorEXT), ('maxLuminance', ctypes.c_float), ('minLuminance', ctypes.c_float), ('maxContentLightLevel', ctypes.c_float), ('maxFrameAverageLightLevel', ctypes.c_float)]
VkDisplayNativeHdrSurfaceCapabilitiesAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('localDimmingSupport', VkBool32)]
VkSwapchainDisplayNativeHdrCreateInfoAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('localDimmingEnable', VkBool32)]
VkRefreshCycleDurationGOOGLE._fields_ = [('refreshDuration', ctypes.c_uint64)]
VkPastPresentationTimingGOOGLE._fields_ = [('presentID', ctypes.c_uint32), ('desiredPresentTime', ctypes.c_uint64), ('actualPresentTime', ctypes.c_uint64), ('earliestPresentTime', ctypes.c_uint64), ('presentMargin', ctypes.c_uint64)]
VkPresentTimeGOOGLE._fields_ = [('presentID', ctypes.c_uint32), ('desiredPresentTime', ctypes.c_uint64)]
VkPresentTimesInfoGOOGLE._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('swapchainCount', ctypes.c_uint32), ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE))]
if VK_USE_PLATFORM_IOS_MVK:
    VkIOSSurfaceCreateInfoMVK._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkIOSSurfaceCreateFlagsMVK), ('pView', ctypes.c_void_p)]
if VK_USE_PLATFORM_MACOS_MVK:
    VkMacOSSurfaceCreateInfoMVK._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkMacOSSurfaceCreateFlagsMVK), ('pView', ctypes.c_void_p)]
if VK_USE_PLATFORM_METAL_EXT:
    VkMetalSurfaceCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkMetalSurfaceCreateFlagsEXT), ('pLayer', ctypes.POINTER(CAMetalLayer))]
VkViewportWScalingNV._fields_ = [('xcoeff', ctypes.c_float), ('ycoeff', ctypes.c_float)]
VkPipelineViewportWScalingStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('viewportWScalingEnable', VkBool32), ('viewportCount', ctypes.c_uint32), ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV))]
VkViewportSwizzleNV._fields_ = [('x', VkViewportCoordinateSwizzleNV), ('y', VkViewportCoordinateSwizzleNV), ('z', VkViewportCoordinateSwizzleNV), ('w', VkViewportCoordinateSwizzleNV)]
VkPipelineViewportSwizzleStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineViewportSwizzleStateCreateFlagsNV), ('viewportCount', ctypes.c_uint32), ('pViewportSwizzles', ctypes.POINTER(VkViewportSwizzleNV))]
VkPhysicalDeviceDiscardRectanglePropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxDiscardRectangles', ctypes.c_uint32)]
VkPipelineDiscardRectangleStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineDiscardRectangleStateCreateFlagsEXT), ('discardRectangleMode', VkDiscardRectangleModeEXT), ('discardRectangleCount', ctypes.c_uint32), ('pDiscardRectangles', ctypes.POINTER(VkRect2D))]
VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('perViewPositionAllComponents', VkBool32)]
VkInputAttachmentAspectReference._fields_ = [('subpass', ctypes.c_uint32), ('inputAttachmentIndex', ctypes.c_uint32), ('aspectMask', VkImageAspectFlags)]
VkInputAttachmentAspectReferenceKHR = type('VkInputAttachmentAspectReferenceKHR', (VkInputAttachmentAspectReference,), dict())
VkRenderPassInputAttachmentAspectCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('aspectReferenceCount', ctypes.c_uint32), ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference))]
VkRenderPassInputAttachmentAspectCreateInfoKHR = type('VkRenderPassInputAttachmentAspectCreateInfoKHR', (VkRenderPassInputAttachmentAspectCreateInfo,), dict())
VkPhysicalDeviceSurfaceInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('surface', VkSurfaceKHR)]
VkSurfaceCapabilities2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('surfaceCapabilities', VkSurfaceCapabilitiesKHR)]
VkSurfaceFormat2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('surfaceFormat', VkSurfaceFormatKHR)]
VkDisplayProperties2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('displayProperties', VkDisplayPropertiesKHR)]
VkDisplayPlaneProperties2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('displayPlaneProperties', VkDisplayPlanePropertiesKHR)]
VkDisplayModeProperties2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('displayModeProperties', VkDisplayModePropertiesKHR)]
VkDisplayPlaneInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('mode', VkDisplayModeKHR), ('planeIndex', ctypes.c_uint32)]
VkDisplayPlaneCapabilities2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('capabilities', VkDisplayPlaneCapabilitiesKHR)]
VkSharedPresentSurfaceCapabilitiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sharedPresentSupportedUsageFlags', VkImageUsageFlags)]
VkPhysicalDevice16BitStorageFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('storageBuffer16BitAccess', VkBool32), ('uniformAndStorageBuffer16BitAccess', VkBool32), ('storagePushConstant16', VkBool32), ('storageInputOutput16', VkBool32)]
VkPhysicalDevice16BitStorageFeaturesKHR = type('VkPhysicalDevice16BitStorageFeaturesKHR', (VkPhysicalDevice16BitStorageFeatures,), dict())
VkPhysicalDeviceSubgroupProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('subgroupSize', ctypes.c_uint32), ('supportedStages', VkShaderStageFlags), ('supportedOperations', VkSubgroupFeatureFlags), ('quadOperationsInAllStages', VkBool32)]
VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderSubgroupExtendedTypes', VkBool32)]
VkPhysicalDeviceShaderSubgroupExtendedTypesFeaturesKHR = type('VkPhysicalDeviceShaderSubgroupExtendedTypesFeaturesKHR', (VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures,), dict())
VkBufferMemoryRequirementsInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('buffer', VkBuffer)]
VkBufferMemoryRequirementsInfo2KHR = type('VkBufferMemoryRequirementsInfo2KHR', (VkBufferMemoryRequirementsInfo2,), dict())
VkImageMemoryRequirementsInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('image', VkImage)]
VkImageMemoryRequirementsInfo2KHR = type('VkImageMemoryRequirementsInfo2KHR', (VkImageMemoryRequirementsInfo2,), dict())
VkImageSparseMemoryRequirementsInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('image', VkImage)]
VkImageSparseMemoryRequirementsInfo2KHR = type('VkImageSparseMemoryRequirementsInfo2KHR', (VkImageSparseMemoryRequirementsInfo2,), dict())
VkMemoryRequirements2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryRequirements', VkMemoryRequirements)]
VkMemoryRequirements2KHR = type('VkMemoryRequirements2KHR', (VkMemoryRequirements2,), dict())
VkSparseImageMemoryRequirements2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryRequirements', VkSparseImageMemoryRequirements)]
VkSparseImageMemoryRequirements2KHR = type('VkSparseImageMemoryRequirements2KHR', (VkSparseImageMemoryRequirements2,), dict())
VkPhysicalDevicePointClippingProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pointClippingBehavior', VkPointClippingBehavior)]
VkPhysicalDevicePointClippingPropertiesKHR = type('VkPhysicalDevicePointClippingPropertiesKHR', (VkPhysicalDevicePointClippingProperties,), dict())
VkMemoryDedicatedRequirements._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('prefersDedicatedAllocation', VkBool32), ('requiresDedicatedAllocation', VkBool32)]
VkMemoryDedicatedRequirementsKHR = type('VkMemoryDedicatedRequirementsKHR', (VkMemoryDedicatedRequirements,), dict())
VkMemoryDedicatedAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('image', VkImage), ('buffer', VkBuffer)]
VkMemoryDedicatedAllocateInfoKHR = type('VkMemoryDedicatedAllocateInfoKHR', (VkMemoryDedicatedAllocateInfo,), dict())
VkImageViewUsageCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('usage', VkImageUsageFlags)]
VkImageViewUsageCreateInfoKHR = type('VkImageViewUsageCreateInfoKHR', (VkImageViewUsageCreateInfo,), dict())
VkPipelineTessellationDomainOriginStateCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('domainOrigin', VkTessellationDomainOrigin)]
VkPipelineTessellationDomainOriginStateCreateInfoKHR = type('VkPipelineTessellationDomainOriginStateCreateInfoKHR', (VkPipelineTessellationDomainOriginStateCreateInfo,), dict())
VkSamplerYcbcrConversionInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('conversion', VkSamplerYcbcrConversion)]
VkSamplerYcbcrConversionInfoKHR = type('VkSamplerYcbcrConversionInfoKHR', (VkSamplerYcbcrConversionInfo,), dict())
VkSamplerYcbcrConversionCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('format', VkFormat), ('ycbcrModel', VkSamplerYcbcrModelConversion), ('ycbcrRange', VkSamplerYcbcrRange), ('components', VkComponentMapping), ('xChromaOffset', VkChromaLocation), ('yChromaOffset', VkChromaLocation), ('chromaFilter', VkFilter), ('forceExplicitReconstruction', VkBool32)]
VkSamplerYcbcrConversionCreateInfoKHR = type('VkSamplerYcbcrConversionCreateInfoKHR', (VkSamplerYcbcrConversionCreateInfo,), dict())
VkBindImagePlaneMemoryInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('planeAspect', VkImageAspectFlagBits)]
VkBindImagePlaneMemoryInfoKHR = type('VkBindImagePlaneMemoryInfoKHR', (VkBindImagePlaneMemoryInfo,), dict())
VkImagePlaneMemoryRequirementsInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('planeAspect', VkImageAspectFlagBits)]
VkImagePlaneMemoryRequirementsInfoKHR = type('VkImagePlaneMemoryRequirementsInfoKHR', (VkImagePlaneMemoryRequirementsInfo,), dict())
VkPhysicalDeviceSamplerYcbcrConversionFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('samplerYcbcrConversion', VkBool32)]
VkPhysicalDeviceSamplerYcbcrConversionFeaturesKHR = type('VkPhysicalDeviceSamplerYcbcrConversionFeaturesKHR', (VkPhysicalDeviceSamplerYcbcrConversionFeatures,), dict())
VkSamplerYcbcrConversionImageFormatProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('combinedImageSamplerDescriptorCount', ctypes.c_uint32)]
VkSamplerYcbcrConversionImageFormatPropertiesKHR = type('VkSamplerYcbcrConversionImageFormatPropertiesKHR', (VkSamplerYcbcrConversionImageFormatProperties,), dict())
VkTextureLODGatherFormatPropertiesAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('supportsTextureGatherLODBiasAMD', VkBool32)]
VkConditionalRenderingBeginInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('buffer', VkBuffer), ('offset', VkDeviceSize), ('flags', VkConditionalRenderingFlagsEXT)]
VkProtectedSubmitInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('protectedSubmit', VkBool32)]
VkPhysicalDeviceProtectedMemoryFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('protectedMemory', VkBool32)]
VkPhysicalDeviceProtectedMemoryProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('protectedNoFault', VkBool32)]
VkDeviceQueueInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDeviceQueueCreateFlags), ('queueFamilyIndex', ctypes.c_uint32), ('queueIndex', ctypes.c_uint32)]
VkPipelineCoverageToColorStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCoverageToColorStateCreateFlagsNV), ('coverageToColorEnable', VkBool32), ('coverageToColorLocation', ctypes.c_uint32)]
VkPhysicalDeviceSamplerFilterMinmaxProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('filterMinmaxSingleComponentFormats', VkBool32), ('filterMinmaxImageComponentMapping', VkBool32)]
VkPhysicalDeviceSamplerFilterMinmaxPropertiesEXT = type('VkPhysicalDeviceSamplerFilterMinmaxPropertiesEXT', (VkPhysicalDeviceSamplerFilterMinmaxProperties,), dict())
VkSampleLocationEXT._fields_ = [('x', ctypes.c_float), ('y', ctypes.c_float)]
VkSampleLocationsInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sampleLocationsPerPixel', VkSampleCountFlagBits), ('sampleLocationGridSize', VkExtent2D), ('sampleLocationsCount', ctypes.c_uint32), ('pSampleLocations', ctypes.POINTER(VkSampleLocationEXT))]
VkAttachmentSampleLocationsEXT._fields_ = [('attachmentIndex', ctypes.c_uint32), ('sampleLocationsInfo', VkSampleLocationsInfoEXT)]
VkSubpassSampleLocationsEXT._fields_ = [('subpassIndex', ctypes.c_uint32), ('sampleLocationsInfo', VkSampleLocationsInfoEXT)]
VkRenderPassSampleLocationsBeginInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('attachmentInitialSampleLocationsCount', ctypes.c_uint32), ('pAttachmentInitialSampleLocations', ctypes.POINTER(VkAttachmentSampleLocationsEXT)), ('postSubpassSampleLocationsCount', ctypes.c_uint32), ('pPostSubpassSampleLocations', ctypes.POINTER(VkSubpassSampleLocationsEXT))]
VkPipelineSampleLocationsStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sampleLocationsEnable', VkBool32), ('sampleLocationsInfo', VkSampleLocationsInfoEXT)]
VkPhysicalDeviceSampleLocationsPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sampleLocationSampleCounts', VkSampleCountFlags), ('maxSampleLocationGridSize', VkExtent2D), ('sampleLocationCoordinateRange', (ctypes.c_float * (2))), ('sampleLocationSubPixelBits', ctypes.c_uint32), ('variableSampleLocations', VkBool32)]
VkMultisamplePropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxSampleLocationGridSize', VkExtent2D)]
VkSamplerReductionModeCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('reductionMode', VkSamplerReductionMode)]
VkSamplerReductionModeCreateInfoEXT = type('VkSamplerReductionModeCreateInfoEXT', (VkSamplerReductionModeCreateInfo,), dict())
VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('advancedBlendCoherentOperations', VkBool32)]
VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('advancedBlendMaxColorAttachments', ctypes.c_uint32), ('advancedBlendIndependentBlend', VkBool32), ('advancedBlendNonPremultipliedSrcColor', VkBool32), ('advancedBlendNonPremultipliedDstColor', VkBool32), ('advancedBlendCorrelatedOverlap', VkBool32), ('advancedBlendAllOperations', VkBool32)]
VkPipelineColorBlendAdvancedStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcPremultiplied', VkBool32), ('dstPremultiplied', VkBool32), ('blendOverlap', VkBlendOverlapEXT)]
VkPhysicalDeviceInlineUniformBlockFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('inlineUniformBlock', VkBool32), ('descriptorBindingInlineUniformBlockUpdateAfterBind', VkBool32)]
VkPhysicalDeviceInlineUniformBlockPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxInlineUniformBlockSize', ctypes.c_uint32), ('maxPerStageDescriptorInlineUniformBlocks', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32), ('maxDescriptorSetInlineUniformBlocks', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32)]
VkWriteDescriptorSetInlineUniformBlockEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('dataSize', ctypes.c_uint32), ('pData', ctypes.c_void_p)]
VkDescriptorPoolInlineUniformBlockCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxInlineUniformBlockBindings', ctypes.c_uint32)]
VkPipelineCoverageModulationStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCoverageModulationStateCreateFlagsNV), ('coverageModulationMode', VkCoverageModulationModeNV), ('coverageModulationTableEnable', VkBool32), ('coverageModulationTableCount', ctypes.c_uint32), ('pCoverageModulationTable', ctypes.POINTER(ctypes.c_float))]
VkImageFormatListCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('viewFormatCount', ctypes.c_uint32), ('pViewFormats', ctypes.POINTER(VkFormat))]
VkImageFormatListCreateInfoKHR = type('VkImageFormatListCreateInfoKHR', (VkImageFormatListCreateInfo,), dict())
VkValidationCacheCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkValidationCacheCreateFlagsEXT), ('initialDataSize', ctypes.c_size_t), ('pInitialData', ctypes.c_void_p)]
VkShaderModuleValidationCacheCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('validationCache', VkValidationCacheEXT)]
VkPhysicalDeviceMaintenance3Properties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxPerSetDescriptors', ctypes.c_uint32), ('maxMemoryAllocationSize', VkDeviceSize)]
VkPhysicalDeviceMaintenance3PropertiesKHR = type('VkPhysicalDeviceMaintenance3PropertiesKHR', (VkPhysicalDeviceMaintenance3Properties,), dict())
VkDescriptorSetLayoutSupport._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('supported', VkBool32)]
VkDescriptorSetLayoutSupportKHR = type('VkDescriptorSetLayoutSupportKHR', (VkDescriptorSetLayoutSupport,), dict())
VkPhysicalDeviceShaderDrawParametersFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderDrawParameters', VkBool32)]
VkPhysicalDeviceShaderDrawParameterFeatures = type('VkPhysicalDeviceShaderDrawParameterFeatures', (VkPhysicalDeviceShaderDrawParametersFeatures,), dict())
VkPhysicalDeviceShaderFloat16Int8Features._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderFloat16', VkBool32), ('shaderInt8', VkBool32)]
VkPhysicalDeviceShaderFloat16Int8FeaturesKHR = type('VkPhysicalDeviceShaderFloat16Int8FeaturesKHR', (VkPhysicalDeviceShaderFloat16Int8Features,), dict())
VkPhysicalDeviceFloat16Int8FeaturesKHR = type('VkPhysicalDeviceFloat16Int8FeaturesKHR', (VkPhysicalDeviceShaderFloat16Int8Features,), dict())
VkPhysicalDeviceFloatControlsProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('denormBehaviorIndependence', VkShaderFloatControlsIndependence), ('roundingModeIndependence', VkShaderFloatControlsIndependence), ('shaderSignedZeroInfNanPreserveFloat16', VkBool32), ('shaderSignedZeroInfNanPreserveFloat32', VkBool32), ('shaderSignedZeroInfNanPreserveFloat64', VkBool32), ('shaderDenormPreserveFloat16', VkBool32), ('shaderDenormPreserveFloat32', VkBool32), ('shaderDenormPreserveFloat64', VkBool32), ('shaderDenormFlushToZeroFloat16', VkBool32), ('shaderDenormFlushToZeroFloat32', VkBool32), ('shaderDenormFlushToZeroFloat64', VkBool32), ('shaderRoundingModeRTEFloat16', VkBool32), ('shaderRoundingModeRTEFloat32', VkBool32), ('shaderRoundingModeRTEFloat64', VkBool32), ('shaderRoundingModeRTZFloat16', VkBool32), ('shaderRoundingModeRTZFloat32', VkBool32), ('shaderRoundingModeRTZFloat64', VkBool32)]
VkPhysicalDeviceFloatControlsPropertiesKHR = type('VkPhysicalDeviceFloatControlsPropertiesKHR', (VkPhysicalDeviceFloatControlsProperties,), dict())
VkPhysicalDeviceHostQueryResetFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('hostQueryReset', VkBool32)]
VkPhysicalDeviceHostQueryResetFeaturesEXT = type('VkPhysicalDeviceHostQueryResetFeaturesEXT', (VkPhysicalDeviceHostQueryResetFeatures,), dict())
if VK_USE_PLATFORM_ANDROID_KHR:
    VkNativeBufferUsage2ANDROID._fields_ = [('consumer', ctypes.c_uint64), ('producer', ctypes.c_uint64)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkNativeBufferANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handle', ctypes.c_void_p), ('stride', ctypes.c_int), ('format', ctypes.c_int), ('usage', ctypes.c_int), ('usage2', VkNativeBufferUsage2ANDROID)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkSwapchainImageCreateInfoANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('usage', VkSwapchainImageUsageFlagsANDROID)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkPhysicalDevicePresentationPropertiesANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sharedImage', VkBool32)]
VkShaderResourceUsageAMD._fields_ = [('numUsedVgprs', ctypes.c_uint32), ('numUsedSgprs', ctypes.c_uint32), ('ldsSizePerLocalWorkGroup', ctypes.c_uint32), ('ldsUsageSizeInBytes', ctypes.c_size_t), ('scratchMemUsageInBytes', ctypes.c_size_t)]
VkShaderStatisticsInfoAMD._fields_ = [('shaderStageMask', VkShaderStageFlags), ('resourceUsage', VkShaderResourceUsageAMD), ('numPhysicalVgprs', ctypes.c_uint32), ('numPhysicalSgprs', ctypes.c_uint32), ('numAvailableVgprs', ctypes.c_uint32), ('numAvailableSgprs', ctypes.c_uint32), ('computeWorkGroupSize', (ctypes.c_uint32 * (3)))]
VkDeviceQueueGlobalPriorityCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('globalPriority', VkQueueGlobalPriorityEXT)]
VkDebugUtilsObjectNameInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('objectType', VkObjectType), ('objectHandle', ctypes.c_uint64), ('pObjectName', ctypes.c_char_p)]
VkDebugUtilsObjectTagInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('objectType', VkObjectType), ('objectHandle', ctypes.c_uint64), ('tagName', ctypes.c_uint64), ('tagSize', ctypes.c_size_t), ('pTag', ctypes.c_void_p)]
VkDebugUtilsLabelEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pLabelName', ctypes.c_char_p), ('color', (ctypes.c_float * (4)))]
VkDebugUtilsMessengerCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDebugUtilsMessengerCreateFlagsEXT), ('messageSeverity', VkDebugUtilsMessageSeverityFlagsEXT), ('messageType', VkDebugUtilsMessageTypeFlagsEXT), ('pfnUserCallback', PFN_vkDebugUtilsMessengerCallbackEXT), ('pUserData', ctypes.c_void_p)]
VkDebugUtilsMessengerCallbackDataEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDebugUtilsMessengerCallbackDataFlagsEXT), ('pMessageIdName', ctypes.c_char_p), ('messageIdNumber', ctypes.c_int32), ('pMessage', ctypes.c_char_p), ('queueLabelCount', ctypes.c_uint32), ('pQueueLabels', ctypes.POINTER(VkDebugUtilsLabelEXT)), ('cmdBufLabelCount', ctypes.c_uint32), ('pCmdBufLabels', ctypes.POINTER(VkDebugUtilsLabelEXT)), ('objectCount', ctypes.c_uint32), ('pObjects', ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT))]
VkPhysicalDeviceDeviceMemoryReportFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceMemoryReport', VkBool32)]
VkDeviceDeviceMemoryReportCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDeviceMemoryReportFlagsEXT), ('pfnUserCallback', PFN_vkDeviceMemoryReportCallbackEXT), ('pUserData', ctypes.c_void_p)]
VkDeviceMemoryReportCallbackDataEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDeviceMemoryReportFlagsEXT), ('type', VkDeviceMemoryReportEventTypeEXT), ('memoryObjectId', ctypes.c_uint64), ('size', VkDeviceSize), ('objectType', VkObjectType), ('objectHandle', ctypes.c_uint64), ('heapIndex', ctypes.c_uint32)]
VkImportMemoryHostPointerInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('handleType', VkExternalMemoryHandleTypeFlagBits), ('pHostPointer', ctypes.c_void_p)]
VkMemoryHostPointerPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryTypeBits', ctypes.c_uint32)]
VkPhysicalDeviceExternalMemoryHostPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('minImportedHostPointerAlignment', VkDeviceSize)]
VkPhysicalDeviceConservativeRasterizationPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('primitiveOverestimationSize', ctypes.c_float), ('maxExtraPrimitiveOverestimationSize', ctypes.c_float), ('extraPrimitiveOverestimationSizeGranularity', ctypes.c_float), ('primitiveUnderestimation', VkBool32), ('conservativePointAndLineRasterization', VkBool32), ('degenerateTrianglesRasterized', VkBool32), ('degenerateLinesRasterized', VkBool32), ('fullyCoveredFragmentShaderInputVariable', VkBool32), ('conservativeRasterizationPostDepthCoverage', VkBool32)]
VkCalibratedTimestampInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('timeDomain', VkTimeDomainEXT)]
VkPhysicalDeviceShaderCorePropertiesAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderEngineCount', ctypes.c_uint32), ('shaderArraysPerEngineCount', ctypes.c_uint32), ('computeUnitsPerShaderArray', ctypes.c_uint32), ('simdPerComputeUnit', ctypes.c_uint32), ('wavefrontsPerSimd', ctypes.c_uint32), ('wavefrontSize', ctypes.c_uint32), ('sgprsPerSimd', ctypes.c_uint32), ('minSgprAllocation', ctypes.c_uint32), ('maxSgprAllocation', ctypes.c_uint32), ('sgprAllocationGranularity', ctypes.c_uint32), ('vgprsPerSimd', ctypes.c_uint32), ('minVgprAllocation', ctypes.c_uint32), ('maxVgprAllocation', ctypes.c_uint32), ('vgprAllocationGranularity', ctypes.c_uint32)]
VkPhysicalDeviceShaderCoreProperties2AMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderCoreFeatures', VkShaderCorePropertiesFlagsAMD), ('activeComputeUnitCount', ctypes.c_uint32)]
VkPipelineRasterizationConservativeStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineRasterizationConservativeStateCreateFlagsEXT), ('conservativeRasterizationMode', VkConservativeRasterizationModeEXT), ('extraPrimitiveOverestimationSize', ctypes.c_float)]
VkPhysicalDeviceDescriptorIndexingFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderInputAttachmentArrayDynamicIndexing', VkBool32), ('shaderUniformTexelBufferArrayDynamicIndexing', VkBool32), ('shaderStorageTexelBufferArrayDynamicIndexing', VkBool32), ('shaderUniformBufferArrayNonUniformIndexing', VkBool32), ('shaderSampledImageArrayNonUniformIndexing', VkBool32), ('shaderStorageBufferArrayNonUniformIndexing', VkBool32), ('shaderStorageImageArrayNonUniformIndexing', VkBool32), ('shaderInputAttachmentArrayNonUniformIndexing', VkBool32), ('shaderUniformTexelBufferArrayNonUniformIndexing', VkBool32), ('shaderStorageTexelBufferArrayNonUniformIndexing', VkBool32), ('descriptorBindingUniformBufferUpdateAfterBind', VkBool32), ('descriptorBindingSampledImageUpdateAfterBind', VkBool32), ('descriptorBindingStorageImageUpdateAfterBind', VkBool32), ('descriptorBindingStorageBufferUpdateAfterBind', VkBool32), ('descriptorBindingUniformTexelBufferUpdateAfterBind', VkBool32), ('descriptorBindingStorageTexelBufferUpdateAfterBind', VkBool32), ('descriptorBindingUpdateUnusedWhilePending', VkBool32), ('descriptorBindingPartiallyBound', VkBool32), ('descriptorBindingVariableDescriptorCount', VkBool32), ('runtimeDescriptorArray', VkBool32)]
VkPhysicalDeviceDescriptorIndexingFeaturesEXT = type('VkPhysicalDeviceDescriptorIndexingFeaturesEXT', (VkPhysicalDeviceDescriptorIndexingFeatures,), dict())
VkPhysicalDeviceDescriptorIndexingProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxUpdateAfterBindDescriptorsInAllPools', ctypes.c_uint32), ('shaderUniformBufferArrayNonUniformIndexingNative', VkBool32), ('shaderSampledImageArrayNonUniformIndexingNative', VkBool32), ('shaderStorageBufferArrayNonUniformIndexingNative', VkBool32), ('shaderStorageImageArrayNonUniformIndexingNative', VkBool32), ('shaderInputAttachmentArrayNonUniformIndexingNative', VkBool32), ('robustBufferAccessUpdateAfterBind', VkBool32), ('quadDivergentImplicitLod', VkBool32), ('maxPerStageDescriptorUpdateAfterBindSamplers', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindUniformBuffers', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindStorageBuffers', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindSampledImages', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindStorageImages', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindInputAttachments', ctypes.c_uint32), ('maxPerStageUpdateAfterBindResources', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindSamplers', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindUniformBuffers', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindUniformBuffersDynamic', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindStorageBuffers', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindStorageBuffersDynamic', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindSampledImages', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindStorageImages', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindInputAttachments', ctypes.c_uint32)]
VkPhysicalDeviceDescriptorIndexingPropertiesEXT = type('VkPhysicalDeviceDescriptorIndexingPropertiesEXT', (VkPhysicalDeviceDescriptorIndexingProperties,), dict())
VkDescriptorSetLayoutBindingFlagsCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('bindingCount', ctypes.c_uint32), ('pBindingFlags', ctypes.POINTER(VkDescriptorBindingFlags))]
VkDescriptorSetLayoutBindingFlagsCreateInfoEXT = type('VkDescriptorSetLayoutBindingFlagsCreateInfoEXT', (VkDescriptorSetLayoutBindingFlagsCreateInfo,), dict())
VkDescriptorSetVariableDescriptorCountAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('descriptorSetCount', ctypes.c_uint32), ('pDescriptorCounts', ctypes.POINTER(ctypes.c_uint32))]
VkDescriptorSetVariableDescriptorCountAllocateInfoEXT = type('VkDescriptorSetVariableDescriptorCountAllocateInfoEXT', (VkDescriptorSetVariableDescriptorCountAllocateInfo,), dict())
VkDescriptorSetVariableDescriptorCountLayoutSupport._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxVariableDescriptorCount', ctypes.c_uint32)]
VkDescriptorSetVariableDescriptorCountLayoutSupportEXT = type('VkDescriptorSetVariableDescriptorCountLayoutSupportEXT', (VkDescriptorSetVariableDescriptorCountLayoutSupport,), dict())
VkAttachmentDescription2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkAttachmentDescriptionFlags), ('format', VkFormat), ('samples', VkSampleCountFlagBits), ('loadOp', VkAttachmentLoadOp), ('storeOp', VkAttachmentStoreOp), ('stencilLoadOp', VkAttachmentLoadOp), ('stencilStoreOp', VkAttachmentStoreOp), ('initialLayout', VkImageLayout), ('finalLayout', VkImageLayout)]
VkAttachmentDescription2KHR = type('VkAttachmentDescription2KHR', (VkAttachmentDescription2,), dict())
VkAttachmentReference2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('attachment', ctypes.c_uint32), ('layout', VkImageLayout), ('aspectMask', VkImageAspectFlags)]
VkAttachmentReference2KHR = type('VkAttachmentReference2KHR', (VkAttachmentReference2,), dict())
VkSubpassDescription2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkSubpassDescriptionFlags), ('pipelineBindPoint', VkPipelineBindPoint), ('viewMask', ctypes.c_uint32), ('inputAttachmentCount', ctypes.c_uint32), ('pInputAttachments', ctypes.POINTER(VkAttachmentReference2)), ('colorAttachmentCount', ctypes.c_uint32), ('pColorAttachments', ctypes.POINTER(VkAttachmentReference2)), ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference2)), ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference2)), ('preserveAttachmentCount', ctypes.c_uint32), ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32))]
VkSubpassDescription2KHR = type('VkSubpassDescription2KHR', (VkSubpassDescription2,), dict())
VkSubpassDependency2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcSubpass', ctypes.c_uint32), ('dstSubpass', ctypes.c_uint32), ('srcStageMask', VkPipelineStageFlags), ('dstStageMask', VkPipelineStageFlags), ('srcAccessMask', VkAccessFlags), ('dstAccessMask', VkAccessFlags), ('dependencyFlags', VkDependencyFlags), ('viewOffset', ctypes.c_int32)]
VkSubpassDependency2KHR = type('VkSubpassDependency2KHR', (VkSubpassDependency2,), dict())
VkRenderPassCreateInfo2._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkRenderPassCreateFlags), ('attachmentCount', ctypes.c_uint32), ('pAttachments', ctypes.POINTER(VkAttachmentDescription2)), ('subpassCount', ctypes.c_uint32), ('pSubpasses', ctypes.POINTER(VkSubpassDescription2)), ('dependencyCount', ctypes.c_uint32), ('pDependencies', ctypes.POINTER(VkSubpassDependency2)), ('correlatedViewMaskCount', ctypes.c_uint32), ('pCorrelatedViewMasks', ctypes.POINTER(ctypes.c_uint32))]
VkRenderPassCreateInfo2KHR = type('VkRenderPassCreateInfo2KHR', (VkRenderPassCreateInfo2,), dict())
VkSubpassBeginInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('contents', VkSubpassContents)]
VkSubpassBeginInfoKHR = type('VkSubpassBeginInfoKHR', (VkSubpassBeginInfo,), dict())
VkSubpassEndInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p)]
VkSubpassEndInfoKHR = type('VkSubpassEndInfoKHR', (VkSubpassEndInfo,), dict())
VkPhysicalDeviceTimelineSemaphoreFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('timelineSemaphore', VkBool32)]
VkPhysicalDeviceTimelineSemaphoreFeaturesKHR = type('VkPhysicalDeviceTimelineSemaphoreFeaturesKHR', (VkPhysicalDeviceTimelineSemaphoreFeatures,), dict())
VkPhysicalDeviceTimelineSemaphoreProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxTimelineSemaphoreValueDifference', ctypes.c_uint64)]
VkPhysicalDeviceTimelineSemaphorePropertiesKHR = type('VkPhysicalDeviceTimelineSemaphorePropertiesKHR', (VkPhysicalDeviceTimelineSemaphoreProperties,), dict())
VkSemaphoreTypeCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('semaphoreType', VkSemaphoreType), ('initialValue', ctypes.c_uint64)]
VkSemaphoreTypeCreateInfoKHR = type('VkSemaphoreTypeCreateInfoKHR', (VkSemaphoreTypeCreateInfo,), dict())
VkTimelineSemaphoreSubmitInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('waitSemaphoreValueCount', ctypes.c_uint32), ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)), ('signalSemaphoreValueCount', ctypes.c_uint32), ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64))]
VkTimelineSemaphoreSubmitInfoKHR = type('VkTimelineSemaphoreSubmitInfoKHR', (VkTimelineSemaphoreSubmitInfo,), dict())
VkSemaphoreWaitInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkSemaphoreWaitFlags), ('semaphoreCount', ctypes.c_uint32), ('pSemaphores', ctypes.POINTER(VkSemaphore)), ('pValues', ctypes.POINTER(ctypes.c_uint64))]
VkSemaphoreWaitInfoKHR = type('VkSemaphoreWaitInfoKHR', (VkSemaphoreWaitInfo,), dict())
VkSemaphoreSignalInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('semaphore', VkSemaphore), ('value', ctypes.c_uint64)]
VkSemaphoreSignalInfoKHR = type('VkSemaphoreSignalInfoKHR', (VkSemaphoreSignalInfo,), dict())
VkVertexInputBindingDivisorDescriptionEXT._fields_ = [('binding', ctypes.c_uint32), ('divisor', ctypes.c_uint32)]
VkPipelineVertexInputDivisorStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('vertexBindingDivisorCount', ctypes.c_uint32), ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionEXT))]
VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxVertexAttribDivisor', ctypes.c_uint32)]
VkPhysicalDevicePCIBusInfoPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pciDomain', ctypes.c_uint32), ('pciBus', ctypes.c_uint32), ('pciDevice', ctypes.c_uint32), ('pciFunction', ctypes.c_uint32)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkImportAndroidHardwareBufferInfoANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('buffer', ctypes.POINTER(AHardwareBuffer))]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidHardwareBufferUsageANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('androidHardwareBufferUsage', ctypes.c_uint64)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidHardwareBufferPropertiesANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('allocationSize', VkDeviceSize), ('memoryTypeBits', ctypes.c_uint32)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkMemoryGetAndroidHardwareBufferInfoANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memory', VkDeviceMemory)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkAndroidHardwareBufferFormatPropertiesANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('format', VkFormat), ('externalFormat', ctypes.c_uint64), ('formatFeatures', VkFormatFeatureFlags), ('samplerYcbcrConversionComponents', VkComponentMapping), ('suggestedYcbcrModel', VkSamplerYcbcrModelConversion), ('suggestedYcbcrRange', VkSamplerYcbcrRange), ('suggestedXChromaOffset', VkChromaLocation), ('suggestedYChromaOffset', VkChromaLocation)]
VkCommandBufferInheritanceConditionalRenderingInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('conditionalRenderingEnable', VkBool32)]
if VK_USE_PLATFORM_ANDROID_KHR:
    VkExternalFormatANDROID._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('externalFormat', ctypes.c_uint64)]
VkPhysicalDevice8BitStorageFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('storageBuffer8BitAccess', VkBool32), ('uniformAndStorageBuffer8BitAccess', VkBool32), ('storagePushConstant8', VkBool32)]
VkPhysicalDevice8BitStorageFeaturesKHR = type('VkPhysicalDevice8BitStorageFeaturesKHR', (VkPhysicalDevice8BitStorageFeatures,), dict())
VkPhysicalDeviceConditionalRenderingFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('conditionalRendering', VkBool32), ('inheritedConditionalRendering', VkBool32)]
VkPhysicalDeviceVulkanMemoryModelFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('vulkanMemoryModel', VkBool32), ('vulkanMemoryModelDeviceScope', VkBool32), ('vulkanMemoryModelAvailabilityVisibilityChains', VkBool32)]
VkPhysicalDeviceVulkanMemoryModelFeaturesKHR = type('VkPhysicalDeviceVulkanMemoryModelFeaturesKHR', (VkPhysicalDeviceVulkanMemoryModelFeatures,), dict())
VkPhysicalDeviceShaderAtomicInt64Features._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderBufferInt64Atomics', VkBool32), ('shaderSharedInt64Atomics', VkBool32)]
VkPhysicalDeviceShaderAtomicInt64FeaturesKHR = type('VkPhysicalDeviceShaderAtomicInt64FeaturesKHR', (VkPhysicalDeviceShaderAtomicInt64Features,), dict())
VkPhysicalDeviceShaderAtomicFloatFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderBufferFloat32Atomics', VkBool32), ('shaderBufferFloat32AtomicAdd', VkBool32), ('shaderBufferFloat64Atomics', VkBool32), ('shaderBufferFloat64AtomicAdd', VkBool32), ('shaderSharedFloat32Atomics', VkBool32), ('shaderSharedFloat32AtomicAdd', VkBool32), ('shaderSharedFloat64Atomics', VkBool32), ('shaderSharedFloat64AtomicAdd', VkBool32), ('shaderImageFloat32Atomics', VkBool32), ('shaderImageFloat32AtomicAdd', VkBool32), ('sparseImageFloat32Atomics', VkBool32), ('sparseImageFloat32AtomicAdd', VkBool32)]
VkPhysicalDeviceVertexAttributeDivisorFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('vertexAttributeInstanceRateDivisor', VkBool32), ('vertexAttributeInstanceRateZeroDivisor', VkBool32)]
VkQueueFamilyCheckpointPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('checkpointExecutionStageMask', VkPipelineStageFlags)]
VkCheckpointDataNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('stage', VkPipelineStageFlagBits), ('pCheckpointMarker', ctypes.c_void_p)]
VkPhysicalDeviceDepthStencilResolveProperties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('supportedDepthResolveModes', VkResolveModeFlags), ('supportedStencilResolveModes', VkResolveModeFlags), ('independentResolveNone', VkBool32), ('independentResolve', VkBool32)]
VkPhysicalDeviceDepthStencilResolvePropertiesKHR = type('VkPhysicalDeviceDepthStencilResolvePropertiesKHR', (VkPhysicalDeviceDepthStencilResolveProperties,), dict())
VkSubpassDescriptionDepthStencilResolve._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('depthResolveMode', VkResolveModeFlagBits), ('stencilResolveMode', VkResolveModeFlagBits), ('pDepthStencilResolveAttachment', ctypes.POINTER(VkAttachmentReference2))]
VkSubpassDescriptionDepthStencilResolveKHR = type('VkSubpassDescriptionDepthStencilResolveKHR', (VkSubpassDescriptionDepthStencilResolve,), dict())
VkImageViewASTCDecodeModeEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('decodeMode', VkFormat)]
VkPhysicalDeviceASTCDecodeFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('decodeModeSharedExponent', VkBool32)]
VkPhysicalDeviceTransformFeedbackFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('transformFeedback', VkBool32), ('geometryStreams', VkBool32)]
VkPhysicalDeviceTransformFeedbackPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxTransformFeedbackStreams', ctypes.c_uint32), ('maxTransformFeedbackBuffers', ctypes.c_uint32), ('maxTransformFeedbackBufferSize', VkDeviceSize), ('maxTransformFeedbackStreamDataSize', ctypes.c_uint32), ('maxTransformFeedbackBufferDataSize', ctypes.c_uint32), ('maxTransformFeedbackBufferDataStride', ctypes.c_uint32), ('transformFeedbackQueries', VkBool32), ('transformFeedbackStreamsLinesTriangles', VkBool32), ('transformFeedbackRasterizationStreamSelect', VkBool32), ('transformFeedbackDraw', VkBool32)]
VkPipelineRasterizationStateStreamCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineRasterizationStateStreamCreateFlagsEXT), ('rasterizationStream', ctypes.c_uint32)]
VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('representativeFragmentTest', VkBool32)]
VkPipelineRepresentativeFragmentTestStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('representativeFragmentTestEnable', VkBool32)]
VkPhysicalDeviceExclusiveScissorFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('exclusiveScissor', VkBool32)]
VkPipelineViewportExclusiveScissorStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('exclusiveScissorCount', ctypes.c_uint32), ('pExclusiveScissors', ctypes.POINTER(VkRect2D))]
VkPhysicalDeviceCornerSampledImageFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('cornerSampledImage', VkBool32)]
VkPhysicalDeviceComputeShaderDerivativesFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('computeDerivativeGroupQuads', VkBool32), ('computeDerivativeGroupLinear', VkBool32)]
VkPhysicalDeviceFragmentShaderBarycentricFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentShaderBarycentric', VkBool32)]
VkPhysicalDeviceShaderImageFootprintFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('imageFootprint', VkBool32)]
VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('dedicatedAllocationImageAliasing', VkBool32)]
VkShadingRatePaletteNV._fields_ = [('shadingRatePaletteEntryCount', ctypes.c_uint32), ('pShadingRatePaletteEntries', ctypes.POINTER(VkShadingRatePaletteEntryNV))]
VkPipelineViewportShadingRateImageStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shadingRateImageEnable', VkBool32), ('viewportCount', ctypes.c_uint32), ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV))]
VkPhysicalDeviceShadingRateImageFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shadingRateImage', VkBool32), ('shadingRateCoarseSampleOrder', VkBool32)]
VkPhysicalDeviceShadingRateImagePropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shadingRateTexelSize', VkExtent2D), ('shadingRatePaletteSize', ctypes.c_uint32), ('shadingRateMaxCoarseSamples', ctypes.c_uint32)]
VkCoarseSampleLocationNV._fields_ = [('pixelX', ctypes.c_uint32), ('pixelY', ctypes.c_uint32), ('sample', ctypes.c_uint32)]
VkCoarseSampleOrderCustomNV._fields_ = [('shadingRate', VkShadingRatePaletteEntryNV), ('sampleCount', ctypes.c_uint32), ('sampleLocationCount', ctypes.c_uint32), ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV))]
VkPipelineViewportCoarseSampleOrderStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sampleOrderType', VkCoarseSampleOrderTypeNV), ('customSampleOrderCount', ctypes.c_uint32), ('pCustomSampleOrders', ctypes.POINTER(VkCoarseSampleOrderCustomNV))]
VkPhysicalDeviceMeshShaderFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('taskShader', VkBool32), ('meshShader', VkBool32)]
VkPhysicalDeviceMeshShaderPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxDrawMeshTasksCount', ctypes.c_uint32), ('maxTaskWorkGroupInvocations', ctypes.c_uint32), ('maxTaskWorkGroupSize', (ctypes.c_uint32 * (3))), ('maxTaskTotalMemorySize', ctypes.c_uint32), ('maxTaskOutputCount', ctypes.c_uint32), ('maxMeshWorkGroupInvocations', ctypes.c_uint32), ('maxMeshWorkGroupSize', (ctypes.c_uint32 * (3))), ('maxMeshTotalMemorySize', ctypes.c_uint32), ('maxMeshOutputVertices', ctypes.c_uint32), ('maxMeshOutputPrimitives', ctypes.c_uint32), ('maxMeshMultiviewViewCount', ctypes.c_uint32), ('meshOutputPerVertexGranularity', ctypes.c_uint32), ('meshOutputPerPrimitiveGranularity', ctypes.c_uint32)]
VkDrawMeshTasksIndirectCommandNV._fields_ = [('taskCount', ctypes.c_uint32), ('firstTask', ctypes.c_uint32)]
VkRayTracingShaderGroupCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkRayTracingShaderGroupTypeKHR), ('generalShader', ctypes.c_uint32), ('closestHitShader', ctypes.c_uint32), ('anyHitShader', ctypes.c_uint32), ('intersectionShader', ctypes.c_uint32)]
VkRayTracingShaderGroupCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkRayTracingShaderGroupTypeKHR), ('generalShader', ctypes.c_uint32), ('closestHitShader', ctypes.c_uint32), ('anyHitShader', ctypes.c_uint32), ('intersectionShader', ctypes.c_uint32), ('pShaderGroupCaptureReplayHandle', ctypes.c_void_p)]
VkRayTracingPipelineCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCreateFlags), ('stageCount', ctypes.c_uint32), ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)), ('groupCount', ctypes.c_uint32), ('pGroups', ctypes.POINTER(VkRayTracingShaderGroupCreateInfoNV)), ('maxRecursionDepth', ctypes.c_uint32), ('layout', VkPipelineLayout), ('basePipelineHandle', VkPipeline), ('basePipelineIndex', ctypes.c_int32)]
VkPipelineLibraryCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('libraryCount', ctypes.c_uint32), ('pLibraries', ctypes.POINTER(VkPipeline))]
VkRayTracingPipelineInterfaceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxPipelineRayPayloadSize', ctypes.c_uint32), ('maxPipelineRayHitAttributeSize', ctypes.c_uint32)]
VkRayTracingPipelineCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCreateFlags), ('stageCount', ctypes.c_uint32), ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)), ('groupCount', ctypes.c_uint32), ('pGroups', ctypes.POINTER(VkRayTracingShaderGroupCreateInfoKHR)), ('maxPipelineRayRecursionDepth', ctypes.c_uint32), ('pLibraryInfo', ctypes.POINTER(VkPipelineLibraryCreateInfoKHR)), ('pLibraryInterface', ctypes.POINTER(VkRayTracingPipelineInterfaceCreateInfoKHR)), ('pDynamicState', ctypes.POINTER(VkPipelineDynamicStateCreateInfo)), ('layout', VkPipelineLayout), ('basePipelineHandle', VkPipeline), ('basePipelineIndex', ctypes.c_int32)]
VkGeometryTrianglesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('vertexData', VkBuffer), ('vertexOffset', VkDeviceSize), ('vertexCount', ctypes.c_uint32), ('vertexStride', VkDeviceSize), ('vertexFormat', VkFormat), ('indexData', VkBuffer), ('indexOffset', VkDeviceSize), ('indexCount', ctypes.c_uint32), ('indexType', VkIndexType), ('transformData', VkBuffer), ('transformOffset', VkDeviceSize)]
VkGeometryAABBNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('aabbData', VkBuffer), ('numAABBs', ctypes.c_uint32), ('stride', ctypes.c_uint32), ('offset', VkDeviceSize)]
VkGeometryDataNV._fields_ = [('triangles', VkGeometryTrianglesNV), ('aabbs', VkGeometryAABBNV)]
VkGeometryNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('geometryType', VkGeometryTypeKHR), ('geometry', VkGeometryDataNV), ('flags', VkGeometryFlagsKHR)]
VkAccelerationStructureInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkAccelerationStructureTypeNV), ('flags', VkBuildAccelerationStructureFlagsNV), ('instanceCount', ctypes.c_uint32), ('geometryCount', ctypes.c_uint32), ('pGeometries', ctypes.POINTER(VkGeometryNV))]
VkAccelerationStructureCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('compactedSize', VkDeviceSize), ('info', VkAccelerationStructureInfoNV)]
VkBindAccelerationStructureMemoryInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('accelerationStructure', VkAccelerationStructureNV), ('memory', VkDeviceMemory), ('memoryOffset', VkDeviceSize), ('deviceIndexCount', ctypes.c_uint32), ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32))]
VkWriteDescriptorSetAccelerationStructureKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('accelerationStructureCount', ctypes.c_uint32), ('pAccelerationStructures', ctypes.POINTER(VkAccelerationStructureKHR))]
VkWriteDescriptorSetAccelerationStructureNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('accelerationStructureCount', ctypes.c_uint32), ('pAccelerationStructures', ctypes.POINTER(VkAccelerationStructureNV))]
VkAccelerationStructureMemoryRequirementsInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkAccelerationStructureMemoryRequirementsTypeNV), ('accelerationStructure', VkAccelerationStructureNV)]
VkPhysicalDeviceAccelerationStructureFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('accelerationStructure', VkBool32), ('accelerationStructureCaptureReplay', VkBool32), ('accelerationStructureIndirectBuild', VkBool32), ('accelerationStructureHostCommands', VkBool32), ('descriptorBindingAccelerationStructureUpdateAfterBind', VkBool32)]
VkPhysicalDeviceRayTracingPipelineFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('rayTracingPipeline', VkBool32), ('rayTracingPipelineShaderGroupHandleCaptureReplay', VkBool32), ('rayTracingPipelineShaderGroupHandleCaptureReplayMixed', VkBool32), ('rayTracingPipelineTraceRaysIndirect', VkBool32), ('rayTraversalPrimitiveCulling', VkBool32)]
VkPhysicalDeviceRayQueryFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('rayQuery', VkBool32)]
VkPhysicalDeviceAccelerationStructurePropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxGeometryCount', ctypes.c_uint64), ('maxInstanceCount', ctypes.c_uint64), ('maxPrimitiveCount', ctypes.c_uint64), ('maxPerStageDescriptorAccelerationStructures', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindAccelerationStructures', ctypes.c_uint32), ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindAccelerationStructures', ctypes.c_uint32), ('minAccelerationStructureScratchOffsetAlignment', ctypes.c_uint32)]
VkPhysicalDeviceRayTracingPipelinePropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderGroupHandleSize', ctypes.c_uint32), ('maxRayRecursionDepth', ctypes.c_uint32), ('maxShaderGroupStride', ctypes.c_uint32), ('shaderGroupBaseAlignment', ctypes.c_uint32), ('shaderGroupHandleCaptureReplaySize', ctypes.c_uint32), ('maxRayDispatchInvocationCount', ctypes.c_uint32), ('shaderGroupHandleAlignment', ctypes.c_uint32), ('maxRayHitAttributeSize', ctypes.c_uint32)]
VkPhysicalDeviceRayTracingPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderGroupHandleSize', ctypes.c_uint32), ('maxRecursionDepth', ctypes.c_uint32), ('maxShaderGroupStride', ctypes.c_uint32), ('shaderGroupBaseAlignment', ctypes.c_uint32), ('maxGeometryCount', ctypes.c_uint64), ('maxInstanceCount', ctypes.c_uint64), ('maxTriangleCount', ctypes.c_uint64), ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32)]
VkStridedDeviceAddressRegionKHR._fields_ = [('deviceAddress', VkDeviceAddress), ('stride', VkDeviceSize), ('size', VkDeviceSize)]
VkTraceRaysIndirectCommandKHR._fields_ = [('width', ctypes.c_uint32), ('height', ctypes.c_uint32), ('depth', ctypes.c_uint32)]
VkDrmFormatModifierPropertiesEXT._fields_ = [('drmFormatModifier', ctypes.c_uint64), ('drmFormatModifierPlaneCount', ctypes.c_uint32), ('drmFormatModifierTilingFeatures', VkFormatFeatureFlags)]
VkDrmFormatModifierPropertiesListEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('drmFormatModifierCount', ctypes.c_uint32), ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierPropertiesEXT))]
VkPhysicalDeviceImageDrmFormatModifierInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('drmFormatModifier', ctypes.c_uint64), ('sharingMode', VkSharingMode), ('queueFamilyIndexCount', ctypes.c_uint32), ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32))]
VkImageDrmFormatModifierListCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('drmFormatModifierCount', ctypes.c_uint32), ('pDrmFormatModifiers', ctypes.POINTER(ctypes.c_uint64))]
VkImageDrmFormatModifierExplicitCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('drmFormatModifier', ctypes.c_uint64), ('drmFormatModifierPlaneCount', ctypes.c_uint32), ('pPlaneLayouts', ctypes.POINTER(VkSubresourceLayout))]
VkImageDrmFormatModifierPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('drmFormatModifier', ctypes.c_uint64)]
VkImageStencilUsageCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('stencilUsage', VkImageUsageFlags)]
VkImageStencilUsageCreateInfoEXT = type('VkImageStencilUsageCreateInfoEXT', (VkImageStencilUsageCreateInfo,), dict())
VkDeviceMemoryOverallocationCreateInfoAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('overallocationBehavior', VkMemoryOverallocationBehaviorAMD)]
VkPhysicalDeviceFragmentDensityMapFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentDensityMap', VkBool32), ('fragmentDensityMapDynamic', VkBool32), ('fragmentDensityMapNonSubsampledImages', VkBool32)]
VkPhysicalDeviceFragmentDensityMap2FeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentDensityMapDeferred', VkBool32)]
VkPhysicalDeviceFragmentDensityMapPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('minFragmentDensityTexelSize', VkExtent2D), ('maxFragmentDensityTexelSize', VkExtent2D), ('fragmentDensityInvocations', VkBool32)]
VkPhysicalDeviceFragmentDensityMap2PropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('subsampledLoads', VkBool32), ('subsampledCoarseReconstructionEarlyAccess', VkBool32), ('maxSubsampledArrayLayers', ctypes.c_uint32), ('maxDescriptorSetSubsampledSamplers', ctypes.c_uint32)]
VkRenderPassFragmentDensityMapCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentDensityMapAttachment', VkAttachmentReference)]
VkPhysicalDeviceScalarBlockLayoutFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('scalarBlockLayout', VkBool32)]
VkPhysicalDeviceScalarBlockLayoutFeaturesEXT = type('VkPhysicalDeviceScalarBlockLayoutFeaturesEXT', (VkPhysicalDeviceScalarBlockLayoutFeatures,), dict())
VkSurfaceProtectedCapabilitiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('supportsProtected', VkBool32)]
VkPhysicalDeviceUniformBufferStandardLayoutFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('uniformBufferStandardLayout', VkBool32)]
VkPhysicalDeviceUniformBufferStandardLayoutFeaturesKHR = type('VkPhysicalDeviceUniformBufferStandardLayoutFeaturesKHR', (VkPhysicalDeviceUniformBufferStandardLayoutFeatures,), dict())
VkPhysicalDeviceDepthClipEnableFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('depthClipEnable', VkBool32)]
VkPipelineRasterizationDepthClipStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineRasterizationDepthClipStateCreateFlagsEXT), ('depthClipEnable', VkBool32)]
VkPhysicalDeviceMemoryBudgetPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('heapBudget', (VkDeviceSize * (VK_MAX_MEMORY_HEAPS))), ('heapUsage', (VkDeviceSize * (VK_MAX_MEMORY_HEAPS)))]
VkPhysicalDeviceMemoryPriorityFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memoryPriority', VkBool32)]
VkMemoryPriorityAllocateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('priority', ctypes.c_float)]
VkPhysicalDeviceBufferDeviceAddressFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('bufferDeviceAddress', VkBool32), ('bufferDeviceAddressCaptureReplay', VkBool32), ('bufferDeviceAddressMultiDevice', VkBool32)]
VkPhysicalDeviceBufferDeviceAddressFeaturesKHR = type('VkPhysicalDeviceBufferDeviceAddressFeaturesKHR', (VkPhysicalDeviceBufferDeviceAddressFeatures,), dict())
VkPhysicalDeviceBufferDeviceAddressFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('bufferDeviceAddress', VkBool32), ('bufferDeviceAddressCaptureReplay', VkBool32), ('bufferDeviceAddressMultiDevice', VkBool32)]
VkPhysicalDeviceBufferAddressFeaturesEXT = type('VkPhysicalDeviceBufferAddressFeaturesEXT', (VkPhysicalDeviceBufferDeviceAddressFeaturesEXT,), dict())
VkBufferDeviceAddressInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('buffer', VkBuffer)]
VkBufferDeviceAddressInfoKHR = type('VkBufferDeviceAddressInfoKHR', (VkBufferDeviceAddressInfo,), dict())
VkBufferDeviceAddressInfoEXT = type('VkBufferDeviceAddressInfoEXT', (VkBufferDeviceAddressInfo,), dict())
VkBufferOpaqueCaptureAddressCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('opaqueCaptureAddress', ctypes.c_uint64)]
VkBufferOpaqueCaptureAddressCreateInfoKHR = type('VkBufferOpaqueCaptureAddressCreateInfoKHR', (VkBufferOpaqueCaptureAddressCreateInfo,), dict())
VkBufferDeviceAddressCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceAddress', VkDeviceAddress)]
VkPhysicalDeviceImageViewImageFormatInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('imageViewType', VkImageViewType)]
VkFilterCubicImageViewImageFormatPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('filterCubic', VkBool32), ('filterCubicMinmax', VkBool32)]
VkPhysicalDeviceImagelessFramebufferFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('imagelessFramebuffer', VkBool32)]
VkPhysicalDeviceImagelessFramebufferFeaturesKHR = type('VkPhysicalDeviceImagelessFramebufferFeaturesKHR', (VkPhysicalDeviceImagelessFramebufferFeatures,), dict())
VkFramebufferAttachmentImageInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkImageCreateFlags), ('usage', VkImageUsageFlags), ('width', ctypes.c_uint32), ('height', ctypes.c_uint32), ('layerCount', ctypes.c_uint32), ('viewFormatCount', ctypes.c_uint32), ('pViewFormats', ctypes.POINTER(VkFormat))]
VkFramebufferAttachmentsCreateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('attachmentImageInfoCount', ctypes.c_uint32), ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo))]
VkFramebufferAttachmentsCreateInfoKHR = type('VkFramebufferAttachmentsCreateInfoKHR', (VkFramebufferAttachmentsCreateInfo,), dict())
VkFramebufferAttachmentImageInfoKHR = type('VkFramebufferAttachmentImageInfoKHR', (VkFramebufferAttachmentImageInfo,), dict())
VkRenderPassAttachmentBeginInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('attachmentCount', ctypes.c_uint32), ('pAttachments', ctypes.POINTER(VkImageView))]
VkRenderPassAttachmentBeginInfoKHR = type('VkRenderPassAttachmentBeginInfoKHR', (VkRenderPassAttachmentBeginInfo,), dict())
VkPhysicalDeviceTextureCompressionASTCHDRFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('textureCompressionASTC_HDR', VkBool32)]
VkPhysicalDeviceCooperativeMatrixFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('cooperativeMatrix', VkBool32), ('cooperativeMatrixRobustBufferAccess', VkBool32)]
VkPhysicalDeviceCooperativeMatrixPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('cooperativeMatrixSupportedStages', VkShaderStageFlags)]
VkCooperativeMatrixPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('MSize', ctypes.c_uint32), ('NSize', ctypes.c_uint32), ('KSize', ctypes.c_uint32), ('AType', VkComponentTypeNV), ('BType', VkComponentTypeNV), ('CType', VkComponentTypeNV), ('DType', VkComponentTypeNV), ('scope', VkScopeNV)]
VkPhysicalDeviceYcbcrImageArraysFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('ycbcrImageArrays', VkBool32)]
VkImageViewHandleInfoNVX._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('imageView', VkImageView), ('descriptorType', VkDescriptorType), ('sampler', VkSampler)]
VkImageViewAddressPropertiesNVX._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceAddress', VkDeviceAddress), ('size', VkDeviceSize)]
if VK_USE_PLATFORM_GGP:
    VkPresentFrameTokenGGP._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('frameToken', GgpFrameToken)]
VkPipelineCreationFeedbackEXT._fields_ = [('flags', VkPipelineCreationFeedbackFlagsEXT), ('duration', ctypes.c_uint64)]
VkPipelineCreationFeedbackCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pPipelineCreationFeedback', ctypes.POINTER(VkPipelineCreationFeedbackEXT)), ('pipelineStageCreationFeedbackCount', ctypes.c_uint32), ('pPipelineStageCreationFeedbacks', ctypes.POINTER(VkPipelineCreationFeedbackEXT))]
if VK_USE_PLATFORM_WIN32_KHR:
    VkSurfaceFullScreenExclusiveInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fullScreenExclusive', VkFullScreenExclusiveEXT)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkSurfaceFullScreenExclusiveWin32InfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('hmonitor', ctypes.wintypes.HMONITOR)]
if VK_USE_PLATFORM_WIN32_KHR:
    VkSurfaceCapabilitiesFullScreenExclusiveEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fullScreenExclusiveSupported', VkBool32)]
VkPhysicalDevicePerformanceQueryFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('performanceCounterQueryPools', VkBool32), ('performanceCounterMultipleQueryPools', VkBool32)]
VkPhysicalDevicePerformanceQueryPropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('allowCommandBufferQueryCopies', VkBool32)]
VkPerformanceCounterKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('unit', VkPerformanceCounterUnitKHR), ('scope', VkPerformanceCounterScopeKHR), ('storage', VkPerformanceCounterStorageKHR), ('uuid', (ctypes.c_uint8 * (VK_UUID_SIZE)))]
VkPerformanceCounterDescriptionKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPerformanceCounterDescriptionFlagsKHR), ('name', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('category', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('description', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE)))]
VkQueryPoolPerformanceCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('queueFamilyIndex', ctypes.c_uint32), ('counterIndexCount', ctypes.c_uint32), ('pCounterIndices', ctypes.POINTER(ctypes.c_uint32))]
VkPerformanceCounterResultKHR._fields_ = [('int32', ctypes.c_int32), ('int64', ctypes.c_int64), ('uint32', ctypes.c_uint32), ('uint64', ctypes.c_uint64), ('float32', ctypes.c_float), ('float64', ctypes.c_double)]
VkAcquireProfilingLockInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkAcquireProfilingLockFlagsKHR), ('timeout', ctypes.c_uint64)]
VkPerformanceQuerySubmitInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('counterPassIndex', ctypes.c_uint32)]
VkHeadlessSurfaceCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkHeadlessSurfaceCreateFlagsEXT)]
VkPhysicalDeviceCoverageReductionModeFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('coverageReductionMode', VkBool32)]
VkPipelineCoverageReductionStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkPipelineCoverageReductionStateCreateFlagsNV), ('coverageReductionMode', VkCoverageReductionModeNV)]
VkFramebufferMixedSamplesCombinationNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('coverageReductionMode', VkCoverageReductionModeNV), ('rasterizationSamples', VkSampleCountFlagBits), ('depthStencilSamples', VkSampleCountFlags), ('colorSamples', VkSampleCountFlags)]
VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderIntegerFunctions2', VkBool32)]
VkPerformanceValueDataINTEL._fields_ = [('value32', ctypes.c_uint32), ('value64', ctypes.c_uint64), ('valueFloat', ctypes.c_float), ('valueBool', VkBool32), ('valueString', ctypes.c_char_p)]
VkPerformanceValueINTEL._fields_ = [('type', VkPerformanceValueTypeINTEL), ('data', VkPerformanceValueDataINTEL)]
VkInitializePerformanceApiInfoINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pUserData', ctypes.c_void_p)]
VkQueryPoolPerformanceQueryCreateInfoINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('performanceCountersSampling', VkQueryPoolSamplingModeINTEL)]
VkQueryPoolCreateInfoINTEL = type('VkQueryPoolCreateInfoINTEL', (VkQueryPoolPerformanceQueryCreateInfoINTEL,), dict())
VkPerformanceMarkerInfoINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('marker', ctypes.c_uint64)]
VkPerformanceStreamMarkerInfoINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('marker', ctypes.c_uint32)]
VkPerformanceOverrideInfoINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkPerformanceOverrideTypeINTEL), ('enable', VkBool32), ('parameter', ctypes.c_uint64)]
VkPerformanceConfigurationAcquireInfoINTEL._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkPerformanceConfigurationTypeINTEL)]
VkPhysicalDeviceShaderClockFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderSubgroupClock', VkBool32), ('shaderDeviceClock', VkBool32)]
VkPhysicalDeviceIndexTypeUint8FeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('indexTypeUint8', VkBool32)]
VkPhysicalDeviceShaderSMBuiltinsPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderSMCount', ctypes.c_uint32), ('shaderWarpsPerSM', ctypes.c_uint32)]
VkPhysicalDeviceShaderSMBuiltinsFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderSMBuiltins', VkBool32)]
VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentShaderSampleInterlock', VkBool32), ('fragmentShaderPixelInterlock', VkBool32), ('fragmentShaderShadingRateInterlock', VkBool32)]
VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('separateDepthStencilLayouts', VkBool32)]
VkPhysicalDeviceSeparateDepthStencilLayoutsFeaturesKHR = type('VkPhysicalDeviceSeparateDepthStencilLayoutsFeaturesKHR', (VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures,), dict())
VkAttachmentReferenceStencilLayout._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('stencilLayout', VkImageLayout)]
VkAttachmentReferenceStencilLayoutKHR = type('VkAttachmentReferenceStencilLayoutKHR', (VkAttachmentReferenceStencilLayout,), dict())
VkAttachmentDescriptionStencilLayout._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('stencilInitialLayout', VkImageLayout), ('stencilFinalLayout', VkImageLayout)]
VkAttachmentDescriptionStencilLayoutKHR = type('VkAttachmentDescriptionStencilLayoutKHR', (VkAttachmentDescriptionStencilLayout,), dict())
VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipelineExecutableInfo', VkBool32)]
VkPipelineInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipeline', VkPipeline)]
VkPipelineExecutablePropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('stages', VkShaderStageFlags), ('name', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('description', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('subgroupSize', ctypes.c_uint32)]
VkPipelineExecutableInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipeline', VkPipeline), ('executableIndex', ctypes.c_uint32)]
VkPipelineExecutableStatisticValueKHR._fields_ = [('b32', VkBool32), ('i64', ctypes.c_int64), ('u64', ctypes.c_uint64), ('f64', ctypes.c_double)]
VkPipelineExecutableStatisticKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('name', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('description', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('format', VkPipelineExecutableStatisticFormatKHR), ('value', VkPipelineExecutableStatisticValueKHR)]
VkPipelineExecutableInternalRepresentationKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('name', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('description', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('isText', VkBool32), ('dataSize', ctypes.c_size_t), ('pData', ctypes.c_void_p)]
VkPhysicalDeviceShaderDemoteToHelperInvocationFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderDemoteToHelperInvocation', VkBool32)]
VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('texelBufferAlignment', VkBool32)]
VkPhysicalDeviceTexelBufferAlignmentPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('storageTexelBufferOffsetAlignmentBytes', VkDeviceSize), ('storageTexelBufferOffsetSingleTexelAlignment', VkBool32), ('uniformTexelBufferOffsetAlignmentBytes', VkDeviceSize), ('uniformTexelBufferOffsetSingleTexelAlignment', VkBool32)]
VkPhysicalDeviceSubgroupSizeControlFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('subgroupSizeControl', VkBool32), ('computeFullSubgroups', VkBool32)]
VkPhysicalDeviceSubgroupSizeControlPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('minSubgroupSize', ctypes.c_uint32), ('maxSubgroupSize', ctypes.c_uint32), ('maxComputeWorkgroupSubgroups', ctypes.c_uint32), ('requiredSubgroupSizeStages', VkShaderStageFlags)]
VkPipelineShaderStageRequiredSubgroupSizeCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('requiredSubgroupSize', ctypes.c_uint32)]
VkMemoryOpaqueCaptureAddressAllocateInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('opaqueCaptureAddress', ctypes.c_uint64)]
VkMemoryOpaqueCaptureAddressAllocateInfoKHR = type('VkMemoryOpaqueCaptureAddressAllocateInfoKHR', (VkMemoryOpaqueCaptureAddressAllocateInfo,), dict())
VkDeviceMemoryOpaqueCaptureAddressInfo._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('memory', VkDeviceMemory)]
VkDeviceMemoryOpaqueCaptureAddressInfoKHR = type('VkDeviceMemoryOpaqueCaptureAddressInfoKHR', (VkDeviceMemoryOpaqueCaptureAddressInfo,), dict())
VkPhysicalDeviceLineRasterizationFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('rectangularLines', VkBool32), ('bresenhamLines', VkBool32), ('smoothLines', VkBool32), ('stippledRectangularLines', VkBool32), ('stippledBresenhamLines', VkBool32), ('stippledSmoothLines', VkBool32)]
VkPhysicalDeviceLineRasterizationPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('lineSubPixelPrecisionBits', ctypes.c_uint32)]
VkPipelineRasterizationLineStateCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('lineRasterizationMode', VkLineRasterizationModeEXT), ('stippledLineEnable', VkBool32), ('lineStippleFactor', ctypes.c_uint32), ('lineStipplePattern', ctypes.c_uint16)]
VkPhysicalDevicePipelineCreationCacheControlFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipelineCreationCacheControl', VkBool32)]
VkPhysicalDeviceVulkan11Features._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('storageBuffer16BitAccess', VkBool32), ('uniformAndStorageBuffer16BitAccess', VkBool32), ('storagePushConstant16', VkBool32), ('storageInputOutput16', VkBool32), ('multiview', VkBool32), ('multiviewGeometryShader', VkBool32), ('multiviewTessellationShader', VkBool32), ('variablePointersStorageBuffer', VkBool32), ('variablePointers', VkBool32), ('protectedMemory', VkBool32), ('samplerYcbcrConversion', VkBool32), ('shaderDrawParameters', VkBool32)]
VkPhysicalDeviceVulkan11Properties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceUUID', (ctypes.c_uint8 * (VK_UUID_SIZE))), ('driverUUID', (ctypes.c_uint8 * (VK_UUID_SIZE))), ('deviceLUID', (ctypes.c_uint8 * (VK_LUID_SIZE))), ('deviceNodeMask', ctypes.c_uint32), ('deviceLUIDValid', VkBool32), ('subgroupSize', ctypes.c_uint32), ('subgroupSupportedStages', VkShaderStageFlags), ('subgroupSupportedOperations', VkSubgroupFeatureFlags), ('subgroupQuadOperationsInAllStages', VkBool32), ('pointClippingBehavior', VkPointClippingBehavior), ('maxMultiviewViewCount', ctypes.c_uint32), ('maxMultiviewInstanceIndex', ctypes.c_uint32), ('protectedNoFault', VkBool32), ('maxPerSetDescriptors', ctypes.c_uint32), ('maxMemoryAllocationSize', VkDeviceSize)]
VkPhysicalDeviceVulkan12Features._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('samplerMirrorClampToEdge', VkBool32), ('drawIndirectCount', VkBool32), ('storageBuffer8BitAccess', VkBool32), ('uniformAndStorageBuffer8BitAccess', VkBool32), ('storagePushConstant8', VkBool32), ('shaderBufferInt64Atomics', VkBool32), ('shaderSharedInt64Atomics', VkBool32), ('shaderFloat16', VkBool32), ('shaderInt8', VkBool32), ('descriptorIndexing', VkBool32), ('shaderInputAttachmentArrayDynamicIndexing', VkBool32), ('shaderUniformTexelBufferArrayDynamicIndexing', VkBool32), ('shaderStorageTexelBufferArrayDynamicIndexing', VkBool32), ('shaderUniformBufferArrayNonUniformIndexing', VkBool32), ('shaderSampledImageArrayNonUniformIndexing', VkBool32), ('shaderStorageBufferArrayNonUniformIndexing', VkBool32), ('shaderStorageImageArrayNonUniformIndexing', VkBool32), ('shaderInputAttachmentArrayNonUniformIndexing', VkBool32), ('shaderUniformTexelBufferArrayNonUniformIndexing', VkBool32), ('shaderStorageTexelBufferArrayNonUniformIndexing', VkBool32), ('descriptorBindingUniformBufferUpdateAfterBind', VkBool32), ('descriptorBindingSampledImageUpdateAfterBind', VkBool32), ('descriptorBindingStorageImageUpdateAfterBind', VkBool32), ('descriptorBindingStorageBufferUpdateAfterBind', VkBool32), ('descriptorBindingUniformTexelBufferUpdateAfterBind', VkBool32), ('descriptorBindingStorageTexelBufferUpdateAfterBind', VkBool32), ('descriptorBindingUpdateUnusedWhilePending', VkBool32), ('descriptorBindingPartiallyBound', VkBool32), ('descriptorBindingVariableDescriptorCount', VkBool32), ('runtimeDescriptorArray', VkBool32), ('samplerFilterMinmax', VkBool32), ('scalarBlockLayout', VkBool32), ('imagelessFramebuffer', VkBool32), ('uniformBufferStandardLayout', VkBool32), ('shaderSubgroupExtendedTypes', VkBool32), ('separateDepthStencilLayouts', VkBool32), ('hostQueryReset', VkBool32), ('timelineSemaphore', VkBool32), ('bufferDeviceAddress', VkBool32), ('bufferDeviceAddressCaptureReplay', VkBool32), ('bufferDeviceAddressMultiDevice', VkBool32), ('vulkanMemoryModel', VkBool32), ('vulkanMemoryModelDeviceScope', VkBool32), ('vulkanMemoryModelAvailabilityVisibilityChains', VkBool32), ('shaderOutputViewportIndex', VkBool32), ('shaderOutputLayer', VkBool32), ('subgroupBroadcastDynamicId', VkBool32)]
VkPhysicalDeviceVulkan12Properties._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('driverID', VkDriverId), ('driverName', (ctypes.c_char * (VK_MAX_DRIVER_NAME_SIZE))), ('driverInfo', (ctypes.c_char * (VK_MAX_DRIVER_INFO_SIZE))), ('conformanceVersion', VkConformanceVersion), ('denormBehaviorIndependence', VkShaderFloatControlsIndependence), ('roundingModeIndependence', VkShaderFloatControlsIndependence), ('shaderSignedZeroInfNanPreserveFloat16', VkBool32), ('shaderSignedZeroInfNanPreserveFloat32', VkBool32), ('shaderSignedZeroInfNanPreserveFloat64', VkBool32), ('shaderDenormPreserveFloat16', VkBool32), ('shaderDenormPreserveFloat32', VkBool32), ('shaderDenormPreserveFloat64', VkBool32), ('shaderDenormFlushToZeroFloat16', VkBool32), ('shaderDenormFlushToZeroFloat32', VkBool32), ('shaderDenormFlushToZeroFloat64', VkBool32), ('shaderRoundingModeRTEFloat16', VkBool32), ('shaderRoundingModeRTEFloat32', VkBool32), ('shaderRoundingModeRTEFloat64', VkBool32), ('shaderRoundingModeRTZFloat16', VkBool32), ('shaderRoundingModeRTZFloat32', VkBool32), ('shaderRoundingModeRTZFloat64', VkBool32), ('maxUpdateAfterBindDescriptorsInAllPools', ctypes.c_uint32), ('shaderUniformBufferArrayNonUniformIndexingNative', VkBool32), ('shaderSampledImageArrayNonUniformIndexingNative', VkBool32), ('shaderStorageBufferArrayNonUniformIndexingNative', VkBool32), ('shaderStorageImageArrayNonUniformIndexingNative', VkBool32), ('shaderInputAttachmentArrayNonUniformIndexingNative', VkBool32), ('robustBufferAccessUpdateAfterBind', VkBool32), ('quadDivergentImplicitLod', VkBool32), ('maxPerStageDescriptorUpdateAfterBindSamplers', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindUniformBuffers', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindStorageBuffers', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindSampledImages', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindStorageImages', ctypes.c_uint32), ('maxPerStageDescriptorUpdateAfterBindInputAttachments', ctypes.c_uint32), ('maxPerStageUpdateAfterBindResources', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindSamplers', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindUniformBuffers', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindUniformBuffersDynamic', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindStorageBuffers', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindStorageBuffersDynamic', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindSampledImages', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindStorageImages', ctypes.c_uint32), ('maxDescriptorSetUpdateAfterBindInputAttachments', ctypes.c_uint32), ('supportedDepthResolveModes', VkResolveModeFlags), ('supportedStencilResolveModes', VkResolveModeFlags), ('independentResolveNone', VkBool32), ('independentResolve', VkBool32), ('filterMinmaxSingleComponentFormats', VkBool32), ('filterMinmaxImageComponentMapping', VkBool32), ('maxTimelineSemaphoreValueDifference', ctypes.c_uint64), ('framebufferIntegerColorSampleCounts', VkSampleCountFlags)]
VkPipelineCompilerControlCreateInfoAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('compilerControlFlags', VkPipelineCompilerControlFlagsAMD)]
VkPhysicalDeviceCoherentMemoryFeaturesAMD._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('deviceCoherentMemory', VkBool32)]
VkPhysicalDeviceToolPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('name', (ctypes.c_char * (VK_MAX_EXTENSION_NAME_SIZE))), ('version', (ctypes.c_char * (VK_MAX_EXTENSION_NAME_SIZE))), ('purposes', VkToolPurposeFlagsEXT), ('description', (ctypes.c_char * (VK_MAX_DESCRIPTION_SIZE))), ('layer', (ctypes.c_char * (VK_MAX_EXTENSION_NAME_SIZE)))]
VkSamplerCustomBorderColorCreateInfoEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('customBorderColor', VkClearColorValue), ('format', VkFormat)]
VkPhysicalDeviceCustomBorderColorPropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxCustomBorderColorSamplers', ctypes.c_uint32)]
VkPhysicalDeviceCustomBorderColorFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('customBorderColors', VkBool32), ('customBorderColorWithoutFormat', VkBool32)]
VkDeviceOrHostAddressKHR._fields_ = [('deviceAddress', VkDeviceAddress), ('hostAddress', ctypes.c_void_p)]
VkDeviceOrHostAddressConstKHR._fields_ = [('deviceAddress', VkDeviceAddress), ('hostAddress', ctypes.c_void_p)]
VkAccelerationStructureGeometryTrianglesDataKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('vertexFormat', VkFormat), ('vertexData', VkDeviceOrHostAddressConstKHR), ('vertexStride', VkDeviceSize), ('maxVertex', ctypes.c_uint32), ('indexType', VkIndexType), ('indexData', VkDeviceOrHostAddressConstKHR), ('transformData', VkDeviceOrHostAddressConstKHR)]
VkAccelerationStructureGeometryAabbsDataKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('data', VkDeviceOrHostAddressConstKHR), ('stride', VkDeviceSize)]
VkAccelerationStructureGeometryInstancesDataKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('arrayOfPointers', VkBool32), ('data', VkDeviceOrHostAddressConstKHR)]
VkAccelerationStructureGeometryDataKHR._fields_ = [('triangles', VkAccelerationStructureGeometryTrianglesDataKHR), ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR), ('instances', VkAccelerationStructureGeometryInstancesDataKHR)]
VkAccelerationStructureGeometryKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('geometryType', VkGeometryTypeKHR), ('geometry', VkAccelerationStructureGeometryDataKHR), ('flags', VkGeometryFlagsKHR)]
VkAccelerationStructureBuildGeometryInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('type', VkAccelerationStructureTypeKHR), ('flags', VkBuildAccelerationStructureFlagsKHR), ('mode', VkBuildAccelerationStructureModeKHR), ('srcAccelerationStructure', VkAccelerationStructureKHR), ('dstAccelerationStructure', VkAccelerationStructureKHR), ('geometryCount', ctypes.c_uint32), ('pGeometries', ctypes.POINTER(VkAccelerationStructureGeometryKHR)), ('ppGeometries', ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureGeometryKHR))), ('scratchData', VkDeviceOrHostAddressKHR)]
VkAccelerationStructureBuildRangeInfoKHR._fields_ = [('primitiveCount', ctypes.c_uint32), ('primitiveOffset', ctypes.c_uint32), ('firstVertex', ctypes.c_uint32), ('transformOffset', ctypes.c_uint32)]
VkAccelerationStructureCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('createFlags', VkAccelerationStructureCreateFlagsKHR), ('buffer', VkBuffer), ('offset', VkDeviceSize), ('size', VkDeviceSize), ('type', VkAccelerationStructureTypeKHR), ('deviceAddress', VkDeviceAddress)]
VkAabbPositionsKHR._fields_ = [('minX', ctypes.c_float), ('minY', ctypes.c_float), ('minZ', ctypes.c_float), ('maxX', ctypes.c_float), ('maxY', ctypes.c_float), ('maxZ', ctypes.c_float)]
VkAabbPositionsNV = type('VkAabbPositionsNV', (VkAabbPositionsKHR,), dict())
VkTransformMatrixKHR._fields_ = [('matrix', (ctypes.c_float * (3 * 4)))]
VkTransformMatrixNV = type('VkTransformMatrixNV', (VkTransformMatrixKHR,), dict())
VkAccelerationStructureInstanceKHR._fields_ = [('transform', VkTransformMatrixKHR), ('instanceCustomIndex', ctypes.c_uint32, 24), ('mask', ctypes.c_uint32, 8), ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24), ('flags', VkGeometryInstanceFlagsKHR, 8), ('accelerationStructureReference', ctypes.c_uint64)]
VkAccelerationStructureInstanceNV = type('VkAccelerationStructureInstanceNV', (VkAccelerationStructureInstanceKHR,), dict())
VkAccelerationStructureDeviceAddressInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('accelerationStructure', VkAccelerationStructureKHR)]
VkAccelerationStructureVersionInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pVersionData', ctypes.POINTER(ctypes.c_uint8))]
VkCopyAccelerationStructureInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('src', VkAccelerationStructureKHR), ('dst', VkAccelerationStructureKHR), ('mode', VkCopyAccelerationStructureModeKHR)]
VkCopyAccelerationStructureToMemoryInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('src', VkAccelerationStructureKHR), ('dst', VkDeviceOrHostAddressKHR), ('mode', VkCopyAccelerationStructureModeKHR)]
VkCopyMemoryToAccelerationStructureInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('src', VkDeviceOrHostAddressConstKHR), ('dst', VkAccelerationStructureKHR), ('mode', VkCopyAccelerationStructureModeKHR)]
VkPhysicalDeviceExtendedDynamicStateFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('extendedDynamicState', VkBool32)]
VkRenderPassTransformBeginInfoQCOM._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('transform', VkSurfaceTransformFlagBitsKHR)]
VkCopyCommandTransformInfoQCOM._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('transform', VkSurfaceTransformFlagBitsKHR)]
VkCommandBufferInheritanceRenderPassTransformInfoQCOM._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('transform', VkSurfaceTransformFlagBitsKHR), ('renderArea', VkRect2D)]
VkPhysicalDeviceDiagnosticsConfigFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('diagnosticsConfig', VkBool32)]
VkDeviceDiagnosticsConfigCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('flags', VkDeviceDiagnosticsConfigFlagsNV)]
VkPhysicalDeviceRobustness2FeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('robustBufferAccess2', VkBool32), ('robustImageAccess2', VkBool32), ('nullDescriptor', VkBool32)]
VkPhysicalDeviceRobustness2PropertiesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('robustStorageBufferAccessSizeAlignment', VkDeviceSize), ('robustUniformBufferAccessSizeAlignment', VkDeviceSize)]
VkPhysicalDeviceImageRobustnessFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('robustImageAccess', VkBool32)]
if VK_ENABLE_BETA_EXTENSIONS:
    VkPhysicalDevicePortabilitySubsetFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('constantAlphaColorBlendFactors', VkBool32), ('events', VkBool32), ('imageViewFormatReinterpretation', VkBool32), ('imageViewFormatSwizzle', VkBool32), ('imageView2DOn3DImage', VkBool32), ('multisampleArrayImage', VkBool32), ('mutableComparisonSamplers', VkBool32), ('pointPolygons', VkBool32), ('samplerMipLodBias', VkBool32), ('separateStencilMaskRef', VkBool32), ('shaderSampleRateInterpolationFunctions', VkBool32), ('tessellationIsolines', VkBool32), ('tessellationPointMode', VkBool32), ('triangleFans', VkBool32), ('vertexAttributeAccessBeyondStride', VkBool32)]
if VK_ENABLE_BETA_EXTENSIONS:
    VkPhysicalDevicePortabilitySubsetPropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('minVertexInputBindingStrideAlignment', ctypes.c_uint32)]
VkPhysicalDevice4444FormatsFeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('formatA4R4G4B4', VkBool32), ('formatA4B4G4R4', VkBool32)]
VkBufferCopy2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcOffset', VkDeviceSize), ('dstOffset', VkDeviceSize), ('size', VkDeviceSize)]
VkImageCopy2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcSubresource', VkImageSubresourceLayers), ('srcOffset', VkOffset3D), ('dstSubresource', VkImageSubresourceLayers), ('dstOffset', VkOffset3D), ('extent', VkExtent3D)]
VkImageBlit2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcSubresource', VkImageSubresourceLayers), ('srcOffsets', (VkOffset3D * (2))), ('dstSubresource', VkImageSubresourceLayers), ('dstOffsets', (VkOffset3D * (2)))]
VkBufferImageCopy2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('bufferOffset', VkDeviceSize), ('bufferRowLength', ctypes.c_uint32), ('bufferImageHeight', ctypes.c_uint32), ('imageSubresource', VkImageSubresourceLayers), ('imageOffset', VkOffset3D), ('imageExtent', VkExtent3D)]
VkImageResolve2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcSubresource', VkImageSubresourceLayers), ('srcOffset', VkOffset3D), ('dstSubresource', VkImageSubresourceLayers), ('dstOffset', VkOffset3D), ('extent', VkExtent3D)]
VkCopyBufferInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcBuffer', VkBuffer), ('dstBuffer', VkBuffer), ('regionCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkBufferCopy2KHR))]
VkCopyImageInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcImage', VkImage), ('srcImageLayout', VkImageLayout), ('dstImage', VkImage), ('dstImageLayout', VkImageLayout), ('regionCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkImageCopy2KHR))]
VkBlitImageInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcImage', VkImage), ('srcImageLayout', VkImageLayout), ('dstImage', VkImage), ('dstImageLayout', VkImageLayout), ('regionCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkImageBlit2KHR)), ('filter', VkFilter)]
VkCopyBufferToImageInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcBuffer', VkBuffer), ('dstImage', VkImage), ('dstImageLayout', VkImageLayout), ('regionCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkBufferImageCopy2KHR))]
VkCopyImageToBufferInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcImage', VkImage), ('srcImageLayout', VkImageLayout), ('dstBuffer', VkBuffer), ('regionCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkBufferImageCopy2KHR))]
VkResolveImageInfo2KHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('srcImage', VkImage), ('srcImageLayout', VkImageLayout), ('dstImage', VkImage), ('dstImageLayout', VkImageLayout), ('regionCount', ctypes.c_uint32), ('pRegions', ctypes.POINTER(VkImageResolve2KHR))]
VkPhysicalDeviceShaderImageAtomicInt64FeaturesEXT._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderImageInt64Atomics', VkBool32), ('sparseImageInt64Atomics', VkBool32)]
VkFragmentShadingRateAttachmentInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pFragmentShadingRateAttachment', ctypes.POINTER(VkAttachmentReference2)), ('shadingRateAttachmentTexelSize', VkExtent2D)]
VkPipelineFragmentShadingRateStateCreateInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentSize', VkExtent2D), ('combinerOps', (VkFragmentShadingRateCombinerOpKHR * (2)))]
VkPhysicalDeviceFragmentShadingRateFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('pipelineFragmentShadingRate', VkBool32), ('primitiveFragmentShadingRate', VkBool32), ('attachmentFragmentShadingRate', VkBool32)]
VkPhysicalDeviceFragmentShadingRatePropertiesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('minFragmentShadingRateAttachmentTexelSize', VkExtent2D), ('maxFragmentShadingRateAttachmentTexelSize', VkExtent2D), ('maxFragmentShadingRateAttachmentTexelSizeAspectRatio', ctypes.c_uint32), ('primitiveFragmentShadingRateWithMultipleViewports', VkBool32), ('layeredShadingRateAttachments', VkBool32), ('fragmentShadingRateNonTrivialCombinerOps', VkBool32), ('maxFragmentSize', VkExtent2D), ('maxFragmentSizeAspectRatio', ctypes.c_uint32), ('maxFragmentShadingRateCoverageSamples', ctypes.c_uint32), ('maxFragmentShadingRateRasterizationSamples', VkSampleCountFlagBits), ('fragmentShadingRateWithShaderDepthStencilWrites', VkBool32), ('fragmentShadingRateWithSampleMask', VkBool32), ('fragmentShadingRateWithShaderSampleMask', VkBool32), ('fragmentShadingRateWithConservativeRasterization', VkBool32), ('fragmentShadingRateWithFragmentShaderInterlock', VkBool32), ('fragmentShadingRateWithCustomSampleLocations', VkBool32), ('fragmentShadingRateStrictMultiplyCombiner', VkBool32)]
VkPhysicalDeviceFragmentShadingRateKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('sampleCounts', VkSampleCountFlags), ('fragmentSize', VkExtent2D)]
VkPhysicalDeviceShaderTerminateInvocationFeaturesKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shaderTerminateInvocation', VkBool32)]
VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('fragmentShadingRateEnums', VkBool32), ('supersampleFragmentShadingRates', VkBool32), ('noInvocationFragmentShadingRates', VkBool32)]
VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('maxFragmentShadingRateInvocationCount', VkSampleCountFlagBits)]
VkPipelineFragmentShadingRateEnumStateCreateInfoNV._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('shadingRateType', VkFragmentShadingRateTypeNV), ('shadingRate', VkFragmentShadingRateNV), ('combinerOps', (VkFragmentShadingRateCombinerOpKHR * (2)))]
VkAccelerationStructureBuildSizesInfoKHR._fields_ = [('sType', VkStructureType), ('pNext', ctypes.c_void_p), ('accelerationStructureSize', VkDeviceSize), ('updateScratchSize', VkDeviceSize), ('buildScratchSize', VkDeviceSize)]

PFN_vkCreateInstance = VK_FUNCTYPE(VkResult, ctypes.POINTER(VkInstanceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkInstance))
vkCreateInstance = VK_DLL.vkCreateInstance
vkCreateInstance.restype = VkResult
vkCreateInstance.argtypes = [ctypes.POINTER(VkInstanceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkInstance)]
PFN_vkDestroyInstance = VK_FUNCTYPE(None, VkInstance, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyInstance = VK_DLL.vkDestroyInstance
vkDestroyInstance.restype = None
vkDestroyInstance.argtypes = [VkInstance, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkEnumeratePhysicalDevices = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDevice))
vkEnumeratePhysicalDevices = VK_DLL.vkEnumeratePhysicalDevices
vkEnumeratePhysicalDevices.restype = VkResult
vkEnumeratePhysicalDevices.argtypes = [VkInstance, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDevice)]
PFN_vkGetDeviceProcAddr = VK_FUNCTYPE(PFN_vkVoidFunction, VkDevice, ctypes.c_char_p)
vkGetDeviceProcAddr = VK_DLL.vkGetDeviceProcAddr
vkGetDeviceProcAddr.restype = PFN_vkVoidFunction
vkGetDeviceProcAddr.argtypes = [VkDevice, ctypes.c_char_p]
PFN_vkGetInstanceProcAddr = VK_FUNCTYPE(PFN_vkVoidFunction, VkInstance, ctypes.c_char_p)
vkGetInstanceProcAddr = VK_DLL.vkGetInstanceProcAddr
vkGetInstanceProcAddr.restype = PFN_vkVoidFunction
vkGetInstanceProcAddr.argtypes = [VkInstance, ctypes.c_char_p]
PFN_vkGetPhysicalDeviceProperties = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceProperties))
vkGetPhysicalDeviceProperties = VK_DLL.vkGetPhysicalDeviceProperties
vkGetPhysicalDeviceProperties.restype = None
vkGetPhysicalDeviceProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceProperties)]
PFN_vkGetPhysicalDeviceQueueFamilyProperties = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties))
vkGetPhysicalDeviceQueueFamilyProperties = VK_DLL.vkGetPhysicalDeviceQueueFamilyProperties
vkGetPhysicalDeviceQueueFamilyProperties.restype = None
vkGetPhysicalDeviceQueueFamilyProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties)]
PFN_vkGetPhysicalDeviceMemoryProperties = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceMemoryProperties))
vkGetPhysicalDeviceMemoryProperties = VK_DLL.vkGetPhysicalDeviceMemoryProperties
vkGetPhysicalDeviceMemoryProperties.restype = None
vkGetPhysicalDeviceMemoryProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceMemoryProperties)]
PFN_vkGetPhysicalDeviceFeatures = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceFeatures))
vkGetPhysicalDeviceFeatures = VK_DLL.vkGetPhysicalDeviceFeatures
vkGetPhysicalDeviceFeatures.restype = None
vkGetPhysicalDeviceFeatures.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceFeatures)]
PFN_vkGetPhysicalDeviceFormatProperties = VK_FUNCTYPE(None, VkPhysicalDevice, VkFormat, ctypes.POINTER(VkFormatProperties))
vkGetPhysicalDeviceFormatProperties = VK_DLL.vkGetPhysicalDeviceFormatProperties
vkGetPhysicalDeviceFormatProperties.restype = None
vkGetPhysicalDeviceFormatProperties.argtypes = [VkPhysicalDevice, VkFormat, ctypes.POINTER(VkFormatProperties)]
PFN_vkGetPhysicalDeviceImageFormatProperties = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkFormat, VkImageType, VkImageTiling, VkImageUsageFlags, VkImageCreateFlags, ctypes.POINTER(VkImageFormatProperties))
vkGetPhysicalDeviceImageFormatProperties = VK_DLL.vkGetPhysicalDeviceImageFormatProperties
vkGetPhysicalDeviceImageFormatProperties.restype = VkResult
vkGetPhysicalDeviceImageFormatProperties.argtypes = [VkPhysicalDevice, VkFormat, VkImageType, VkImageTiling, VkImageUsageFlags, VkImageCreateFlags, ctypes.POINTER(VkImageFormatProperties)]
PFN_vkCreateDevice = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(VkDeviceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDevice))
vkCreateDevice = VK_DLL.vkCreateDevice
vkCreateDevice.restype = VkResult
vkCreateDevice.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkDeviceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDevice)]
PFN_vkDestroyDevice = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDevice = VK_DLL.vkDestroyDevice
vkDestroyDevice.restype = None
vkDestroyDevice.argtypes = [VkDevice, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkEnumerateInstanceVersion = VK_FUNCTYPE(VkResult, ctypes.POINTER(ctypes.c_uint32))
vkEnumerateInstanceVersion = VK_DLL.vkEnumerateInstanceVersion
vkEnumerateInstanceVersion.restype = VkResult
vkEnumerateInstanceVersion.argtypes = [ctypes.POINTER(ctypes.c_uint32)]
PFN_vkEnumerateInstanceLayerProperties = VK_FUNCTYPE(VkResult, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
vkEnumerateInstanceLayerProperties = VK_DLL.vkEnumerateInstanceLayerProperties
vkEnumerateInstanceLayerProperties.restype = VkResult
vkEnumerateInstanceLayerProperties.argtypes = [ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties)]
PFN_vkEnumerateInstanceExtensionProperties = VK_FUNCTYPE(VkResult, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
vkEnumerateInstanceExtensionProperties = VK_DLL.vkEnumerateInstanceExtensionProperties
vkEnumerateInstanceExtensionProperties.restype = VkResult
vkEnumerateInstanceExtensionProperties.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties)]
PFN_vkEnumerateDeviceLayerProperties = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
vkEnumerateDeviceLayerProperties = VK_DLL.vkEnumerateDeviceLayerProperties
vkEnumerateDeviceLayerProperties.restype = VkResult
vkEnumerateDeviceLayerProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties)]
PFN_vkEnumerateDeviceExtensionProperties = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
vkEnumerateDeviceExtensionProperties = VK_DLL.vkEnumerateDeviceExtensionProperties
vkEnumerateDeviceExtensionProperties.restype = VkResult
vkEnumerateDeviceExtensionProperties.argtypes = [VkPhysicalDevice, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties)]
PFN_vkGetDeviceQueue = VK_FUNCTYPE(None, VkDevice, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkQueue))
vkGetDeviceQueue = VK_DLL.vkGetDeviceQueue
vkGetDeviceQueue.restype = None
vkGetDeviceQueue.argtypes = [VkDevice, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkQueue)]
PFN_vkQueueSubmit = VK_FUNCTYPE(VkResult, VkQueue, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo), VkFence)
vkQueueSubmit = VK_DLL.vkQueueSubmit
vkQueueSubmit.restype = VkResult
vkQueueSubmit.argtypes = [VkQueue, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo), VkFence]
PFN_vkQueueWaitIdle = VK_FUNCTYPE(VkResult, VkQueue)
vkQueueWaitIdle = VK_DLL.vkQueueWaitIdle
vkQueueWaitIdle.restype = VkResult
vkQueueWaitIdle.argtypes = [VkQueue]
PFN_vkDeviceWaitIdle = VK_FUNCTYPE(VkResult, VkDevice)
vkDeviceWaitIdle = VK_DLL.vkDeviceWaitIdle
vkDeviceWaitIdle.restype = VkResult
vkDeviceWaitIdle.argtypes = [VkDevice]
PFN_vkAllocateMemory = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkMemoryAllocateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDeviceMemory))
vkAllocateMemory = VK_DLL.vkAllocateMemory
vkAllocateMemory.restype = VkResult
vkAllocateMemory.argtypes = [VkDevice, ctypes.POINTER(VkMemoryAllocateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDeviceMemory)]
PFN_vkFreeMemory = VK_FUNCTYPE(None, VkDevice, VkDeviceMemory, ctypes.POINTER(VkAllocationCallbacks))
vkFreeMemory = VK_DLL.vkFreeMemory
vkFreeMemory.restype = None
vkFreeMemory.argtypes = [VkDevice, VkDeviceMemory, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkMapMemory = VK_FUNCTYPE(VkResult, VkDevice, VkDeviceMemory, VkDeviceSize, VkDeviceSize, VkMemoryMapFlags, ctypes.POINTER(ctypes.c_void_p))
vkMapMemory = VK_DLL.vkMapMemory
vkMapMemory.restype = VkResult
vkMapMemory.argtypes = [VkDevice, VkDeviceMemory, VkDeviceSize, VkDeviceSize, VkMemoryMapFlags, ctypes.POINTER(ctypes.c_void_p)]
PFN_vkUnmapMemory = VK_FUNCTYPE(None, VkDevice, VkDeviceMemory)
vkUnmapMemory = VK_DLL.vkUnmapMemory
vkUnmapMemory.restype = None
vkUnmapMemory.argtypes = [VkDevice, VkDeviceMemory]
PFN_vkFlushMappedMemoryRanges = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange))
vkFlushMappedMemoryRanges = VK_DLL.vkFlushMappedMemoryRanges
vkFlushMappedMemoryRanges.restype = VkResult
vkFlushMappedMemoryRanges.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange)]
PFN_vkInvalidateMappedMemoryRanges = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange))
vkInvalidateMappedMemoryRanges = VK_DLL.vkInvalidateMappedMemoryRanges
vkInvalidateMappedMemoryRanges.restype = VkResult
vkInvalidateMappedMemoryRanges.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange)]
PFN_vkGetDeviceMemoryCommitment = VK_FUNCTYPE(None, VkDevice, VkDeviceMemory, ctypes.POINTER(VkDeviceSize))
vkGetDeviceMemoryCommitment = VK_DLL.vkGetDeviceMemoryCommitment
vkGetDeviceMemoryCommitment.restype = None
vkGetDeviceMemoryCommitment.argtypes = [VkDevice, VkDeviceMemory, ctypes.POINTER(VkDeviceSize)]
PFN_vkGetBufferMemoryRequirements = VK_FUNCTYPE(None, VkDevice, VkBuffer, ctypes.POINTER(VkMemoryRequirements))
vkGetBufferMemoryRequirements = VK_DLL.vkGetBufferMemoryRequirements
vkGetBufferMemoryRequirements.restype = None
vkGetBufferMemoryRequirements.argtypes = [VkDevice, VkBuffer, ctypes.POINTER(VkMemoryRequirements)]
PFN_vkBindBufferMemory = VK_FUNCTYPE(VkResult, VkDevice, VkBuffer, VkDeviceMemory, VkDeviceSize)
vkBindBufferMemory = VK_DLL.vkBindBufferMemory
vkBindBufferMemory.restype = VkResult
vkBindBufferMemory.argtypes = [VkDevice, VkBuffer, VkDeviceMemory, VkDeviceSize]
PFN_vkGetImageMemoryRequirements = VK_FUNCTYPE(None, VkDevice, VkImage, ctypes.POINTER(VkMemoryRequirements))
vkGetImageMemoryRequirements = VK_DLL.vkGetImageMemoryRequirements
vkGetImageMemoryRequirements.restype = None
vkGetImageMemoryRequirements.argtypes = [VkDevice, VkImage, ctypes.POINTER(VkMemoryRequirements)]
PFN_vkBindImageMemory = VK_FUNCTYPE(VkResult, VkDevice, VkImage, VkDeviceMemory, VkDeviceSize)
vkBindImageMemory = VK_DLL.vkBindImageMemory
vkBindImageMemory.restype = VkResult
vkBindImageMemory.argtypes = [VkDevice, VkImage, VkDeviceMemory, VkDeviceSize]
PFN_vkGetImageSparseMemoryRequirements = VK_FUNCTYPE(None, VkDevice, VkImage, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements))
vkGetImageSparseMemoryRequirements = VK_DLL.vkGetImageSparseMemoryRequirements
vkGetImageSparseMemoryRequirements.restype = None
vkGetImageSparseMemoryRequirements.argtypes = [VkDevice, VkImage, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements)]
PFN_vkGetPhysicalDeviceSparseImageFormatProperties = VK_FUNCTYPE(None, VkPhysicalDevice, VkFormat, VkImageType, VkSampleCountFlagBits, VkImageUsageFlags, VkImageTiling, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties))
vkGetPhysicalDeviceSparseImageFormatProperties = VK_DLL.vkGetPhysicalDeviceSparseImageFormatProperties
vkGetPhysicalDeviceSparseImageFormatProperties.restype = None
vkGetPhysicalDeviceSparseImageFormatProperties.argtypes = [VkPhysicalDevice, VkFormat, VkImageType, VkSampleCountFlagBits, VkImageUsageFlags, VkImageTiling, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties)]
PFN_vkQueueBindSparse = VK_FUNCTYPE(VkResult, VkQueue, ctypes.c_uint32, ctypes.POINTER(VkBindSparseInfo), VkFence)
vkQueueBindSparse = VK_DLL.vkQueueBindSparse
vkQueueBindSparse.restype = VkResult
vkQueueBindSparse.argtypes = [VkQueue, ctypes.c_uint32, ctypes.POINTER(VkBindSparseInfo), VkFence]
PFN_vkCreateFence = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkFenceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkFence))
vkCreateFence = VK_DLL.vkCreateFence
vkCreateFence.restype = VkResult
vkCreateFence.argtypes = [VkDevice, ctypes.POINTER(VkFenceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkFence)]
PFN_vkDestroyFence = VK_FUNCTYPE(None, VkDevice, VkFence, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyFence = VK_DLL.vkDestroyFence
vkDestroyFence.restype = None
vkDestroyFence.argtypes = [VkDevice, VkFence, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkResetFences = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkFence))
vkResetFences = VK_DLL.vkResetFences
vkResetFences.restype = VkResult
vkResetFences.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkFence)]
PFN_vkGetFenceStatus = VK_FUNCTYPE(VkResult, VkDevice, VkFence)
vkGetFenceStatus = VK_DLL.vkGetFenceStatus
vkGetFenceStatus.restype = VkResult
vkGetFenceStatus.argtypes = [VkDevice, VkFence]
PFN_vkWaitForFences = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkFence), VkBool32, ctypes.c_uint64)
vkWaitForFences = VK_DLL.vkWaitForFences
vkWaitForFences.restype = VkResult
vkWaitForFences.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkFence), VkBool32, ctypes.c_uint64]
PFN_vkCreateSemaphore = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSemaphoreCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSemaphore))
vkCreateSemaphore = VK_DLL.vkCreateSemaphore
vkCreateSemaphore.restype = VkResult
vkCreateSemaphore.argtypes = [VkDevice, ctypes.POINTER(VkSemaphoreCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSemaphore)]
PFN_vkDestroySemaphore = VK_FUNCTYPE(None, VkDevice, VkSemaphore, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySemaphore = VK_DLL.vkDestroySemaphore
vkDestroySemaphore.restype = None
vkDestroySemaphore.argtypes = [VkDevice, VkSemaphore, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateEvent = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkEventCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkEvent))
vkCreateEvent = VK_DLL.vkCreateEvent
vkCreateEvent.restype = VkResult
vkCreateEvent.argtypes = [VkDevice, ctypes.POINTER(VkEventCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkEvent)]
PFN_vkDestroyEvent = VK_FUNCTYPE(None, VkDevice, VkEvent, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyEvent = VK_DLL.vkDestroyEvent
vkDestroyEvent.restype = None
vkDestroyEvent.argtypes = [VkDevice, VkEvent, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkGetEventStatus = VK_FUNCTYPE(VkResult, VkDevice, VkEvent)
vkGetEventStatus = VK_DLL.vkGetEventStatus
vkGetEventStatus.restype = VkResult
vkGetEventStatus.argtypes = [VkDevice, VkEvent]
PFN_vkSetEvent = VK_FUNCTYPE(VkResult, VkDevice, VkEvent)
vkSetEvent = VK_DLL.vkSetEvent
vkSetEvent.restype = VkResult
vkSetEvent.argtypes = [VkDevice, VkEvent]
PFN_vkResetEvent = VK_FUNCTYPE(VkResult, VkDevice, VkEvent)
vkResetEvent = VK_DLL.vkResetEvent
vkResetEvent.restype = VkResult
vkResetEvent.argtypes = [VkDevice, VkEvent]
PFN_vkCreateQueryPool = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkQueryPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkQueryPool))
vkCreateQueryPool = VK_DLL.vkCreateQueryPool
vkCreateQueryPool.restype = VkResult
vkCreateQueryPool.argtypes = [VkDevice, ctypes.POINTER(VkQueryPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkQueryPool)]
PFN_vkDestroyQueryPool = VK_FUNCTYPE(None, VkDevice, VkQueryPool, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyQueryPool = VK_DLL.vkDestroyQueryPool
vkDestroyQueryPool.restype = None
vkDestroyQueryPool.argtypes = [VkDevice, VkQueryPool, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkGetQueryPoolResults = VK_FUNCTYPE(VkResult, VkDevice, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p, VkDeviceSize, VkQueryResultFlags)
vkGetQueryPoolResults = VK_DLL.vkGetQueryPoolResults
vkGetQueryPoolResults.restype = VkResult
vkGetQueryPoolResults.argtypes = [VkDevice, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p, VkDeviceSize, VkQueryResultFlags]
PFN_vkResetQueryPool = VK_FUNCTYPE(None, VkDevice, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32)
vkResetQueryPool = VK_DLL.vkResetQueryPool
vkResetQueryPool.restype = None
vkResetQueryPool.argtypes = [VkDevice, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkResetQueryPoolEXT = PFN_vkResetQueryPool
vkResetQueryPoolEXT = vkResetQueryPool
PFN_vkCreateBuffer = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkBufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkBuffer))
vkCreateBuffer = VK_DLL.vkCreateBuffer
vkCreateBuffer.restype = VkResult
vkCreateBuffer.argtypes = [VkDevice, ctypes.POINTER(VkBufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkBuffer)]
PFN_vkDestroyBuffer = VK_FUNCTYPE(None, VkDevice, VkBuffer, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyBuffer = VK_DLL.vkDestroyBuffer
vkDestroyBuffer.restype = None
vkDestroyBuffer.argtypes = [VkDevice, VkBuffer, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateBufferView = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkBufferViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkBufferView))
vkCreateBufferView = VK_DLL.vkCreateBufferView
vkCreateBufferView.restype = VkResult
vkCreateBufferView.argtypes = [VkDevice, ctypes.POINTER(VkBufferViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkBufferView)]
PFN_vkDestroyBufferView = VK_FUNCTYPE(None, VkDevice, VkBufferView, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyBufferView = VK_DLL.vkDestroyBufferView
vkDestroyBufferView.restype = None
vkDestroyBufferView.argtypes = [VkDevice, VkBufferView, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateImage = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkImageCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkImage))
vkCreateImage = VK_DLL.vkCreateImage
vkCreateImage.restype = VkResult
vkCreateImage.argtypes = [VkDevice, ctypes.POINTER(VkImageCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkImage)]
PFN_vkDestroyImage = VK_FUNCTYPE(None, VkDevice, VkImage, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyImage = VK_DLL.vkDestroyImage
vkDestroyImage.restype = None
vkDestroyImage.argtypes = [VkDevice, VkImage, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkGetImageSubresourceLayout = VK_FUNCTYPE(None, VkDevice, VkImage, ctypes.POINTER(VkImageSubresource), ctypes.POINTER(VkSubresourceLayout))
vkGetImageSubresourceLayout = VK_DLL.vkGetImageSubresourceLayout
vkGetImageSubresourceLayout.restype = None
vkGetImageSubresourceLayout.argtypes = [VkDevice, VkImage, ctypes.POINTER(VkImageSubresource), ctypes.POINTER(VkSubresourceLayout)]
PFN_vkCreateImageView = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkImageViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkImageView))
vkCreateImageView = VK_DLL.vkCreateImageView
vkCreateImageView.restype = VkResult
vkCreateImageView.argtypes = [VkDevice, ctypes.POINTER(VkImageViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkImageView)]
PFN_vkDestroyImageView = VK_FUNCTYPE(None, VkDevice, VkImageView, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyImageView = VK_DLL.vkDestroyImageView
vkDestroyImageView.restype = None
vkDestroyImageView.argtypes = [VkDevice, VkImageView, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateShaderModule = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkShaderModule))
vkCreateShaderModule = VK_DLL.vkCreateShaderModule
vkCreateShaderModule.restype = VkResult
vkCreateShaderModule.argtypes = [VkDevice, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkShaderModule)]
PFN_vkDestroyShaderModule = VK_FUNCTYPE(None, VkDevice, VkShaderModule, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyShaderModule = VK_DLL.vkDestroyShaderModule
vkDestroyShaderModule.restype = None
vkDestroyShaderModule.argtypes = [VkDevice, VkShaderModule, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreatePipelineCache = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPipelineCacheCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipelineCache))
vkCreatePipelineCache = VK_DLL.vkCreatePipelineCache
vkCreatePipelineCache.restype = VkResult
vkCreatePipelineCache.argtypes = [VkDevice, ctypes.POINTER(VkPipelineCacheCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipelineCache)]
PFN_vkDestroyPipelineCache = VK_FUNCTYPE(None, VkDevice, VkPipelineCache, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPipelineCache = VK_DLL.vkDestroyPipelineCache
vkDestroyPipelineCache.restype = None
vkDestroyPipelineCache.argtypes = [VkDevice, VkPipelineCache, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkGetPipelineCacheData = VK_FUNCTYPE(VkResult, VkDevice, VkPipelineCache, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetPipelineCacheData = VK_DLL.vkGetPipelineCacheData
vkGetPipelineCacheData.restype = VkResult
vkGetPipelineCacheData.argtypes = [VkDevice, VkPipelineCache, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p]
PFN_vkMergePipelineCaches = VK_FUNCTYPE(VkResult, VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkPipelineCache))
vkMergePipelineCaches = VK_DLL.vkMergePipelineCaches
vkMergePipelineCaches.restype = VkResult
vkMergePipelineCaches.argtypes = [VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkPipelineCache)]
PFN_vkCreateGraphicsPipelines = VK_FUNCTYPE(VkResult, VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkGraphicsPipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipeline))
vkCreateGraphicsPipelines = VK_DLL.vkCreateGraphicsPipelines
vkCreateGraphicsPipelines.restype = VkResult
vkCreateGraphicsPipelines.argtypes = [VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkGraphicsPipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipeline)]
PFN_vkCreateComputePipelines = VK_FUNCTYPE(VkResult, VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipeline))
vkCreateComputePipelines = VK_DLL.vkCreateComputePipelines
vkCreateComputePipelines.restype = VkResult
vkCreateComputePipelines.argtypes = [VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipeline)]
PFN_vkDestroyPipeline = VK_FUNCTYPE(None, VkDevice, VkPipeline, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPipeline = VK_DLL.vkDestroyPipeline
vkDestroyPipeline.restype = None
vkDestroyPipeline.argtypes = [VkDevice, VkPipeline, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreatePipelineLayout = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPipelineLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipelineLayout))
vkCreatePipelineLayout = VK_DLL.vkCreatePipelineLayout
vkCreatePipelineLayout.restype = VkResult
vkCreatePipelineLayout.argtypes = [VkDevice, ctypes.POINTER(VkPipelineLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipelineLayout)]
PFN_vkDestroyPipelineLayout = VK_FUNCTYPE(None, VkDevice, VkPipelineLayout, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPipelineLayout = VK_DLL.vkDestroyPipelineLayout
vkDestroyPipelineLayout.restype = None
vkDestroyPipelineLayout.argtypes = [VkDevice, VkPipelineLayout, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateSampler = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSamplerCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSampler))
vkCreateSampler = VK_DLL.vkCreateSampler
vkCreateSampler.restype = VkResult
vkCreateSampler.argtypes = [VkDevice, ctypes.POINTER(VkSamplerCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSampler)]
PFN_vkDestroySampler = VK_FUNCTYPE(None, VkDevice, VkSampler, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySampler = VK_DLL.vkDestroySampler
vkDestroySampler.restype = None
vkDestroySampler.argtypes = [VkDevice, VkSampler, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateDescriptorSetLayout = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDescriptorSetLayout))
vkCreateDescriptorSetLayout = VK_DLL.vkCreateDescriptorSetLayout
vkCreateDescriptorSetLayout.restype = VkResult
vkCreateDescriptorSetLayout.argtypes = [VkDevice, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDescriptorSetLayout)]
PFN_vkDestroyDescriptorSetLayout = VK_FUNCTYPE(None, VkDevice, VkDescriptorSetLayout, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDescriptorSetLayout = VK_DLL.vkDestroyDescriptorSetLayout
vkDestroyDescriptorSetLayout.restype = None
vkDestroyDescriptorSetLayout.argtypes = [VkDevice, VkDescriptorSetLayout, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateDescriptorPool = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDescriptorPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDescriptorPool))
vkCreateDescriptorPool = VK_DLL.vkCreateDescriptorPool
vkCreateDescriptorPool.restype = VkResult
vkCreateDescriptorPool.argtypes = [VkDevice, ctypes.POINTER(VkDescriptorPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDescriptorPool)]
PFN_vkDestroyDescriptorPool = VK_FUNCTYPE(None, VkDevice, VkDescriptorPool, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDescriptorPool = VK_DLL.vkDestroyDescriptorPool
vkDestroyDescriptorPool.restype = None
vkDestroyDescriptorPool.argtypes = [VkDevice, VkDescriptorPool, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkResetDescriptorPool = VK_FUNCTYPE(VkResult, VkDevice, VkDescriptorPool, VkDescriptorPoolResetFlags)
vkResetDescriptorPool = VK_DLL.vkResetDescriptorPool
vkResetDescriptorPool.restype = VkResult
vkResetDescriptorPool.argtypes = [VkDevice, VkDescriptorPool, VkDescriptorPoolResetFlags]
PFN_vkAllocateDescriptorSets = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDescriptorSetAllocateInfo), ctypes.POINTER(VkDescriptorSet))
vkAllocateDescriptorSets = VK_DLL.vkAllocateDescriptorSets
vkAllocateDescriptorSets.restype = VkResult
vkAllocateDescriptorSets.argtypes = [VkDevice, ctypes.POINTER(VkDescriptorSetAllocateInfo), ctypes.POINTER(VkDescriptorSet)]
PFN_vkFreeDescriptorSets = VK_FUNCTYPE(VkResult, VkDevice, VkDescriptorPool, ctypes.c_uint32, ctypes.POINTER(VkDescriptorSet))
vkFreeDescriptorSets = VK_DLL.vkFreeDescriptorSets
vkFreeDescriptorSets.restype = VkResult
vkFreeDescriptorSets.argtypes = [VkDevice, VkDescriptorPool, ctypes.c_uint32, ctypes.POINTER(VkDescriptorSet)]
PFN_vkUpdateDescriptorSets = VK_FUNCTYPE(None, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet), ctypes.c_uint32, ctypes.POINTER(VkCopyDescriptorSet))
vkUpdateDescriptorSets = VK_DLL.vkUpdateDescriptorSets
vkUpdateDescriptorSets.restype = None
vkUpdateDescriptorSets.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet), ctypes.c_uint32, ctypes.POINTER(VkCopyDescriptorSet)]
PFN_vkCreateFramebuffer = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkFramebufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkFramebuffer))
vkCreateFramebuffer = VK_DLL.vkCreateFramebuffer
vkCreateFramebuffer.restype = VkResult
vkCreateFramebuffer.argtypes = [VkDevice, ctypes.POINTER(VkFramebufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkFramebuffer)]
PFN_vkDestroyFramebuffer = VK_FUNCTYPE(None, VkDevice, VkFramebuffer, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyFramebuffer = VK_DLL.vkDestroyFramebuffer
vkDestroyFramebuffer.restype = None
vkDestroyFramebuffer.argtypes = [VkDevice, VkFramebuffer, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkCreateRenderPass = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkRenderPassCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkRenderPass))
vkCreateRenderPass = VK_DLL.vkCreateRenderPass
vkCreateRenderPass.restype = VkResult
vkCreateRenderPass.argtypes = [VkDevice, ctypes.POINTER(VkRenderPassCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkRenderPass)]
PFN_vkDestroyRenderPass = VK_FUNCTYPE(None, VkDevice, VkRenderPass, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyRenderPass = VK_DLL.vkDestroyRenderPass
vkDestroyRenderPass.restype = None
vkDestroyRenderPass.argtypes = [VkDevice, VkRenderPass, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkGetRenderAreaGranularity = VK_FUNCTYPE(None, VkDevice, VkRenderPass, ctypes.POINTER(VkExtent2D))
vkGetRenderAreaGranularity = VK_DLL.vkGetRenderAreaGranularity
vkGetRenderAreaGranularity.restype = None
vkGetRenderAreaGranularity.argtypes = [VkDevice, VkRenderPass, ctypes.POINTER(VkExtent2D)]
PFN_vkCreateCommandPool = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkCommandPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkCommandPool))
vkCreateCommandPool = VK_DLL.vkCreateCommandPool
vkCreateCommandPool.restype = VkResult
vkCreateCommandPool.argtypes = [VkDevice, ctypes.POINTER(VkCommandPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkCommandPool)]
PFN_vkDestroyCommandPool = VK_FUNCTYPE(None, VkDevice, VkCommandPool, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCommandPool = VK_DLL.vkDestroyCommandPool
vkDestroyCommandPool.restype = None
vkDestroyCommandPool.argtypes = [VkDevice, VkCommandPool, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkResetCommandPool = VK_FUNCTYPE(VkResult, VkDevice, VkCommandPool, VkCommandPoolResetFlags)
vkResetCommandPool = VK_DLL.vkResetCommandPool
vkResetCommandPool.restype = VkResult
vkResetCommandPool.argtypes = [VkDevice, VkCommandPool, VkCommandPoolResetFlags]
PFN_vkAllocateCommandBuffers = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkCommandBufferAllocateInfo), ctypes.POINTER(VkCommandBuffer))
vkAllocateCommandBuffers = VK_DLL.vkAllocateCommandBuffers
vkAllocateCommandBuffers.restype = VkResult
vkAllocateCommandBuffers.argtypes = [VkDevice, ctypes.POINTER(VkCommandBufferAllocateInfo), ctypes.POINTER(VkCommandBuffer)]
PFN_vkFreeCommandBuffers = VK_FUNCTYPE(None, VkDevice, VkCommandPool, ctypes.c_uint32, ctypes.POINTER(VkCommandBuffer))
vkFreeCommandBuffers = VK_DLL.vkFreeCommandBuffers
vkFreeCommandBuffers.restype = None
vkFreeCommandBuffers.argtypes = [VkDevice, VkCommandPool, ctypes.c_uint32, ctypes.POINTER(VkCommandBuffer)]
PFN_vkBeginCommandBuffer = VK_FUNCTYPE(VkResult, VkCommandBuffer, ctypes.POINTER(VkCommandBufferBeginInfo))
vkBeginCommandBuffer = VK_DLL.vkBeginCommandBuffer
vkBeginCommandBuffer.restype = VkResult
vkBeginCommandBuffer.argtypes = [VkCommandBuffer, ctypes.POINTER(VkCommandBufferBeginInfo)]
PFN_vkEndCommandBuffer = VK_FUNCTYPE(VkResult, VkCommandBuffer)
vkEndCommandBuffer = VK_DLL.vkEndCommandBuffer
vkEndCommandBuffer.restype = VkResult
vkEndCommandBuffer.argtypes = [VkCommandBuffer]
PFN_vkResetCommandBuffer = VK_FUNCTYPE(VkResult, VkCommandBuffer, VkCommandBufferResetFlags)
vkResetCommandBuffer = VK_DLL.vkResetCommandBuffer
vkResetCommandBuffer.restype = VkResult
vkResetCommandBuffer.argtypes = [VkCommandBuffer, VkCommandBufferResetFlags]
PFN_vkCmdBindPipeline = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineBindPoint, VkPipeline)
vkCmdBindPipeline = VK_DLL.vkCmdBindPipeline
vkCmdBindPipeline.restype = None
vkCmdBindPipeline.argtypes = [VkCommandBuffer, VkPipelineBindPoint, VkPipeline]
PFN_vkCmdSetViewport = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewport))
vkCmdSetViewport = VK_DLL.vkCmdSetViewport
vkCmdSetViewport.restype = None
vkCmdSetViewport.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewport)]
PFN_vkCmdSetScissor = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetScissor = VK_DLL.vkCmdSetScissor
vkCmdSetScissor.restype = None
vkCmdSetScissor.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D)]
PFN_vkCmdSetLineWidth = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_float)
vkCmdSetLineWidth = VK_DLL.vkCmdSetLineWidth
vkCmdSetLineWidth.restype = None
vkCmdSetLineWidth.argtypes = [VkCommandBuffer, ctypes.c_float]
PFN_vkCmdSetDepthBias = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_float, ctypes.c_float, ctypes.c_float)
vkCmdSetDepthBias = VK_DLL.vkCmdSetDepthBias
vkCmdSetDepthBias.restype = None
vkCmdSetDepthBias.argtypes = [VkCommandBuffer, ctypes.c_float, ctypes.c_float, ctypes.c_float]
PFN_vkCmdSetBlendConstants = VK_FUNCTYPE(None, VkCommandBuffer, (ctypes.c_float * (4)))
vkCmdSetBlendConstants = VK_DLL.vkCmdSetBlendConstants
vkCmdSetBlendConstants.restype = None
vkCmdSetBlendConstants.argtypes = [VkCommandBuffer, (ctypes.c_float * (4))]
PFN_vkCmdSetDepthBounds = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_float, ctypes.c_float)
vkCmdSetDepthBounds = VK_DLL.vkCmdSetDepthBounds
vkCmdSetDepthBounds.restype = None
vkCmdSetDepthBounds.argtypes = [VkCommandBuffer, ctypes.c_float, ctypes.c_float]
PFN_vkCmdSetStencilCompareMask = VK_FUNCTYPE(None, VkCommandBuffer, VkStencilFaceFlags, ctypes.c_uint32)
vkCmdSetStencilCompareMask = VK_DLL.vkCmdSetStencilCompareMask
vkCmdSetStencilCompareMask.restype = None
vkCmdSetStencilCompareMask.argtypes = [VkCommandBuffer, VkStencilFaceFlags, ctypes.c_uint32]
PFN_vkCmdSetStencilWriteMask = VK_FUNCTYPE(None, VkCommandBuffer, VkStencilFaceFlags, ctypes.c_uint32)
vkCmdSetStencilWriteMask = VK_DLL.vkCmdSetStencilWriteMask
vkCmdSetStencilWriteMask.restype = None
vkCmdSetStencilWriteMask.argtypes = [VkCommandBuffer, VkStencilFaceFlags, ctypes.c_uint32]
PFN_vkCmdSetStencilReference = VK_FUNCTYPE(None, VkCommandBuffer, VkStencilFaceFlags, ctypes.c_uint32)
vkCmdSetStencilReference = VK_DLL.vkCmdSetStencilReference
vkCmdSetStencilReference.restype = None
vkCmdSetStencilReference.argtypes = [VkCommandBuffer, VkStencilFaceFlags, ctypes.c_uint32]
PFN_vkCmdBindDescriptorSets = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineBindPoint, VkPipelineLayout, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDescriptorSet), ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdBindDescriptorSets = VK_DLL.vkCmdBindDescriptorSets
vkCmdBindDescriptorSets.restype = None
vkCmdBindDescriptorSets.argtypes = [VkCommandBuffer, VkPipelineBindPoint, VkPipelineLayout, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDescriptorSet), ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
PFN_vkCmdBindIndexBuffer = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkIndexType)
vkCmdBindIndexBuffer = VK_DLL.vkCmdBindIndexBuffer
vkCmdBindIndexBuffer.restype = None
vkCmdBindIndexBuffer.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, VkIndexType]
PFN_vkCmdBindVertexBuffers = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkBuffer), ctypes.POINTER(VkDeviceSize))
vkCmdBindVertexBuffers = VK_DLL.vkCmdBindVertexBuffers
vkCmdBindVertexBuffers.restype = None
vkCmdBindVertexBuffers.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkBuffer), ctypes.POINTER(VkDeviceSize)]
PFN_vkCmdDraw = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDraw = VK_DLL.vkCmdDraw
vkCmdDraw.restype = None
vkCmdDraw.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDrawIndexed = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32)
vkCmdDrawIndexed = VK_DLL.vkCmdDrawIndexed
vkCmdDrawIndexed.restype = None
vkCmdDrawIndexed.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32]
PFN_vkCmdDrawIndirect = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirect = VK_DLL.vkCmdDrawIndirect
vkCmdDrawIndirect.restype = None
vkCmdDrawIndirect.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDrawIndexedIndirect = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndexedIndirect = VK_DLL.vkCmdDrawIndexedIndirect
vkCmdDrawIndexedIndirect.restype = None
vkCmdDrawIndexedIndirect.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDispatch = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDispatch = VK_DLL.vkCmdDispatch
vkCmdDispatch.restype = None
vkCmdDispatch.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDispatchIndirect = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize)
vkCmdDispatchIndirect = VK_DLL.vkCmdDispatchIndirect
vkCmdDispatchIndirect.restype = None
vkCmdDispatchIndirect.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize]
PFN_vkCmdCopyBuffer = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkBuffer, ctypes.c_uint32, ctypes.POINTER(VkBufferCopy))
vkCmdCopyBuffer = VK_DLL.vkCmdCopyBuffer
vkCmdCopyBuffer.restype = None
vkCmdCopyBuffer.argtypes = [VkCommandBuffer, VkBuffer, VkBuffer, ctypes.c_uint32, ctypes.POINTER(VkBufferCopy)]
PFN_vkCmdCopyImage = VK_FUNCTYPE(None, VkCommandBuffer, VkImage, VkImageLayout, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkImageCopy))
vkCmdCopyImage = VK_DLL.vkCmdCopyImage
vkCmdCopyImage.restype = None
vkCmdCopyImage.argtypes = [VkCommandBuffer, VkImage, VkImageLayout, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkImageCopy)]
PFN_vkCmdBlitImage = VK_FUNCTYPE(None, VkCommandBuffer, VkImage, VkImageLayout, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkImageBlit), VkFilter)
vkCmdBlitImage = VK_DLL.vkCmdBlitImage
vkCmdBlitImage.restype = None
vkCmdBlitImage.argtypes = [VkCommandBuffer, VkImage, VkImageLayout, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkImageBlit), VkFilter]
PFN_vkCmdCopyBufferToImage = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
vkCmdCopyBufferToImage = VK_DLL.vkCmdCopyBufferToImage
vkCmdCopyBufferToImage.restype = None
vkCmdCopyBufferToImage.argtypes = [VkCommandBuffer, VkBuffer, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy)]
PFN_vkCmdCopyImageToBuffer = VK_FUNCTYPE(None, VkCommandBuffer, VkImage, VkImageLayout, VkBuffer, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
vkCmdCopyImageToBuffer = VK_DLL.vkCmdCopyImageToBuffer
vkCmdCopyImageToBuffer.restype = None
vkCmdCopyImageToBuffer.argtypes = [VkCommandBuffer, VkImage, VkImageLayout, VkBuffer, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy)]
PFN_vkCmdUpdateBuffer = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkDeviceSize, ctypes.c_void_p)
vkCmdUpdateBuffer = VK_DLL.vkCmdUpdateBuffer
vkCmdUpdateBuffer.restype = None
vkCmdUpdateBuffer.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, VkDeviceSize, ctypes.c_void_p]
PFN_vkCmdFillBuffer = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkDeviceSize, ctypes.c_uint32)
vkCmdFillBuffer = VK_DLL.vkCmdFillBuffer
vkCmdFillBuffer.restype = None
vkCmdFillBuffer.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, VkDeviceSize, ctypes.c_uint32]
PFN_vkCmdClearColorImage = VK_FUNCTYPE(None, VkCommandBuffer, VkImage, VkImageLayout, ctypes.POINTER(VkClearColorValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
vkCmdClearColorImage = VK_DLL.vkCmdClearColorImage
vkCmdClearColorImage.restype = None
vkCmdClearColorImage.argtypes = [VkCommandBuffer, VkImage, VkImageLayout, ctypes.POINTER(VkClearColorValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange)]
PFN_vkCmdClearDepthStencilImage = VK_FUNCTYPE(None, VkCommandBuffer, VkImage, VkImageLayout, ctypes.POINTER(VkClearDepthStencilValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
vkCmdClearDepthStencilImage = VK_DLL.vkCmdClearDepthStencilImage
vkCmdClearDepthStencilImage.restype = None
vkCmdClearDepthStencilImage.argtypes = [VkCommandBuffer, VkImage, VkImageLayout, ctypes.POINTER(VkClearDepthStencilValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange)]
PFN_vkCmdClearAttachments = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkClearAttachment), ctypes.c_uint32, ctypes.POINTER(VkClearRect))
vkCmdClearAttachments = VK_DLL.vkCmdClearAttachments
vkCmdClearAttachments.restype = None
vkCmdClearAttachments.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkClearAttachment), ctypes.c_uint32, ctypes.POINTER(VkClearRect)]
PFN_vkCmdResolveImage = VK_FUNCTYPE(None, VkCommandBuffer, VkImage, VkImageLayout, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkImageResolve))
vkCmdResolveImage = VK_DLL.vkCmdResolveImage
vkCmdResolveImage.restype = None
vkCmdResolveImage.argtypes = [VkCommandBuffer, VkImage, VkImageLayout, VkImage, VkImageLayout, ctypes.c_uint32, ctypes.POINTER(VkImageResolve)]
PFN_vkCmdSetEvent = VK_FUNCTYPE(None, VkCommandBuffer, VkEvent, VkPipelineStageFlags)
vkCmdSetEvent = VK_DLL.vkCmdSetEvent
vkCmdSetEvent.restype = None
vkCmdSetEvent.argtypes = [VkCommandBuffer, VkEvent, VkPipelineStageFlags]
PFN_vkCmdResetEvent = VK_FUNCTYPE(None, VkCommandBuffer, VkEvent, VkPipelineStageFlags)
vkCmdResetEvent = VK_DLL.vkCmdResetEvent
vkCmdResetEvent.restype = None
vkCmdResetEvent.argtypes = [VkCommandBuffer, VkEvent, VkPipelineStageFlags]
PFN_vkCmdWaitEvents = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkEvent), VkPipelineStageFlags, VkPipelineStageFlags, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
vkCmdWaitEvents = VK_DLL.vkCmdWaitEvents
vkCmdWaitEvents.restype = None
vkCmdWaitEvents.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkEvent), VkPipelineStageFlags, VkPipelineStageFlags, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier)]
PFN_vkCmdPipelineBarrier = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineStageFlags, VkPipelineStageFlags, VkDependencyFlags, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
vkCmdPipelineBarrier = VK_DLL.vkCmdPipelineBarrier
vkCmdPipelineBarrier.restype = None
vkCmdPipelineBarrier.argtypes = [VkCommandBuffer, VkPipelineStageFlags, VkPipelineStageFlags, VkDependencyFlags, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier)]
PFN_vkCmdBeginQuery = VK_FUNCTYPE(None, VkCommandBuffer, VkQueryPool, ctypes.c_uint32, VkQueryControlFlags)
vkCmdBeginQuery = VK_DLL.vkCmdBeginQuery
vkCmdBeginQuery.restype = None
vkCmdBeginQuery.argtypes = [VkCommandBuffer, VkQueryPool, ctypes.c_uint32, VkQueryControlFlags]
PFN_vkCmdEndQuery = VK_FUNCTYPE(None, VkCommandBuffer, VkQueryPool, ctypes.c_uint32)
vkCmdEndQuery = VK_DLL.vkCmdEndQuery
vkCmdEndQuery.restype = None
vkCmdEndQuery.argtypes = [VkCommandBuffer, VkQueryPool, ctypes.c_uint32]
PFN_vkCmdBeginConditionalRenderingEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkConditionalRenderingBeginInfoEXT))
vkCmdBeginConditionalRenderingEXT = vk_device_fn(b'vkCmdBeginConditionalRenderingEXT', PFN_vkCmdBeginConditionalRenderingEXT)
PFN_vkCmdEndConditionalRenderingEXT = VK_FUNCTYPE(None, VkCommandBuffer)
vkCmdEndConditionalRenderingEXT = vk_device_fn(b'vkCmdEndConditionalRenderingEXT', PFN_vkCmdEndConditionalRenderingEXT)
PFN_vkCmdResetQueryPool = VK_FUNCTYPE(None, VkCommandBuffer, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32)
vkCmdResetQueryPool = VK_DLL.vkCmdResetQueryPool
vkCmdResetQueryPool.restype = None
vkCmdResetQueryPool.argtypes = [VkCommandBuffer, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdWriteTimestamp = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineStageFlagBits, VkQueryPool, ctypes.c_uint32)
vkCmdWriteTimestamp = VK_DLL.vkCmdWriteTimestamp
vkCmdWriteTimestamp.restype = None
vkCmdWriteTimestamp.argtypes = [VkCommandBuffer, VkPipelineStageFlagBits, VkQueryPool, ctypes.c_uint32]
PFN_vkCmdCopyQueryPoolResults = VK_FUNCTYPE(None, VkCommandBuffer, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32, VkBuffer, VkDeviceSize, VkDeviceSize, VkQueryResultFlags)
vkCmdCopyQueryPoolResults = VK_DLL.vkCmdCopyQueryPoolResults
vkCmdCopyQueryPoolResults.restype = None
vkCmdCopyQueryPoolResults.argtypes = [VkCommandBuffer, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32, VkBuffer, VkDeviceSize, VkDeviceSize, VkQueryResultFlags]
PFN_vkCmdPushConstants = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineLayout, VkShaderStageFlags, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)
vkCmdPushConstants = VK_DLL.vkCmdPushConstants
vkCmdPushConstants.restype = None
vkCmdPushConstants.argtypes = [VkCommandBuffer, VkPipelineLayout, VkShaderStageFlags, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p]
PFN_vkCmdBeginRenderPass = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkRenderPassBeginInfo), VkSubpassContents)
vkCmdBeginRenderPass = VK_DLL.vkCmdBeginRenderPass
vkCmdBeginRenderPass.restype = None
vkCmdBeginRenderPass.argtypes = [VkCommandBuffer, ctypes.POINTER(VkRenderPassBeginInfo), VkSubpassContents]
PFN_vkCmdNextSubpass = VK_FUNCTYPE(None, VkCommandBuffer, VkSubpassContents)
vkCmdNextSubpass = VK_DLL.vkCmdNextSubpass
vkCmdNextSubpass.restype = None
vkCmdNextSubpass.argtypes = [VkCommandBuffer, VkSubpassContents]
PFN_vkCmdEndRenderPass = VK_FUNCTYPE(None, VkCommandBuffer)
vkCmdEndRenderPass = VK_DLL.vkCmdEndRenderPass
vkCmdEndRenderPass.restype = None
vkCmdEndRenderPass.argtypes = [VkCommandBuffer]
PFN_vkCmdExecuteCommands = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkCommandBuffer))
vkCmdExecuteCommands = VK_DLL.vkCmdExecuteCommands
vkCmdExecuteCommands.restype = None
vkCmdExecuteCommands.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkCommandBuffer)]
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkCreateAndroidSurfaceKHR = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkAndroidSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateAndroidSurfaceKHR = vk_instance_fn(b'vkCreateAndroidSurfaceKHR', PFN_vkCreateAndroidSurfaceKHR)
PFN_vkGetPhysicalDeviceDisplayPropertiesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPropertiesKHR))
vkGetPhysicalDeviceDisplayPropertiesKHR = vk_instance_fn(b'vkGetPhysicalDeviceDisplayPropertiesKHR', PFN_vkGetPhysicalDeviceDisplayPropertiesKHR)
PFN_vkGetPhysicalDeviceDisplayPlanePropertiesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlanePropertiesKHR))
vkGetPhysicalDeviceDisplayPlanePropertiesKHR = vk_instance_fn(b'vkGetPhysicalDeviceDisplayPlanePropertiesKHR', PFN_vkGetPhysicalDeviceDisplayPlanePropertiesKHR)
PFN_vkGetDisplayPlaneSupportedDisplaysKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayKHR))
vkGetDisplayPlaneSupportedDisplaysKHR = vk_instance_fn(b'vkGetDisplayPlaneSupportedDisplaysKHR', PFN_vkGetDisplayPlaneSupportedDisplaysKHR)
PFN_vkGetDisplayModePropertiesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkDisplayKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModePropertiesKHR))
vkGetDisplayModePropertiesKHR = vk_instance_fn(b'vkGetDisplayModePropertiesKHR', PFN_vkGetDisplayModePropertiesKHR)
PFN_vkCreateDisplayModeKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkDisplayKHR, ctypes.POINTER(VkDisplayModeCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDisplayModeKHR))
vkCreateDisplayModeKHR = vk_instance_fn(b'vkCreateDisplayModeKHR', PFN_vkCreateDisplayModeKHR)
PFN_vkGetDisplayPlaneCapabilitiesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkDisplayModeKHR, ctypes.c_uint32, ctypes.POINTER(VkDisplayPlaneCapabilitiesKHR))
vkGetDisplayPlaneCapabilitiesKHR = vk_instance_fn(b'vkGetDisplayPlaneCapabilitiesKHR', PFN_vkGetDisplayPlaneCapabilitiesKHR)
PFN_vkCreateDisplayPlaneSurfaceKHR = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkDisplaySurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
vkCreateDisplayPlaneSurfaceKHR = vk_instance_fn(b'vkCreateDisplayPlaneSurfaceKHR', PFN_vkCreateDisplayPlaneSurfaceKHR)
PFN_vkCreateSharedSwapchainsKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSwapchainKHR))
vkCreateSharedSwapchainsKHR = vk_device_fn(b'vkCreateSharedSwapchainsKHR', PFN_vkCreateSharedSwapchainsKHR)
PFN_vkDestroySurfaceKHR = VK_FUNCTYPE(None, VkInstance, VkSurfaceKHR, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySurfaceKHR = vk_instance_fn(b'vkDestroySurfaceKHR', PFN_vkDestroySurfaceKHR)
PFN_vkGetPhysicalDeviceSurfaceSupportKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.c_uint32, VkSurfaceKHR, ctypes.POINTER(VkBool32))
vkGetPhysicalDeviceSurfaceSupportKHR = vk_instance_fn(b'vkGetPhysicalDeviceSurfaceSupportKHR', PFN_vkGetPhysicalDeviceSurfaceSupportKHR)
PFN_vkGetPhysicalDeviceSurfaceCapabilitiesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkSurfaceKHR, ctypes.POINTER(VkSurfaceCapabilitiesKHR))
vkGetPhysicalDeviceSurfaceCapabilitiesKHR = vk_instance_fn(b'vkGetPhysicalDeviceSurfaceCapabilitiesKHR', PFN_vkGetPhysicalDeviceSurfaceCapabilitiesKHR)
PFN_vkGetPhysicalDeviceSurfaceFormatsKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkSurfaceKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormatKHR))
vkGetPhysicalDeviceSurfaceFormatsKHR = vk_instance_fn(b'vkGetPhysicalDeviceSurfaceFormatsKHR', PFN_vkGetPhysicalDeviceSurfaceFormatsKHR)
PFN_vkGetPhysicalDeviceSurfacePresentModesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkSurfaceKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPresentModeKHR))
vkGetPhysicalDeviceSurfacePresentModesKHR = vk_instance_fn(b'vkGetPhysicalDeviceSurfacePresentModesKHR', PFN_vkGetPhysicalDeviceSurfacePresentModesKHR)
PFN_vkCreateSwapchainKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSwapchainKHR))
vkCreateSwapchainKHR = vk_device_fn(b'vkCreateSwapchainKHR', PFN_vkCreateSwapchainKHR)
PFN_vkDestroySwapchainKHR = VK_FUNCTYPE(None, VkDevice, VkSwapchainKHR, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySwapchainKHR = vk_device_fn(b'vkDestroySwapchainKHR', PFN_vkDestroySwapchainKHR)
PFN_vkGetSwapchainImagesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkImage))
vkGetSwapchainImagesKHR = vk_device_fn(b'vkGetSwapchainImagesKHR', PFN_vkGetSwapchainImagesKHR)
PFN_vkAcquireNextImageKHR = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR, ctypes.c_uint64, VkSemaphore, VkFence, ctypes.POINTER(ctypes.c_uint32))
vkAcquireNextImageKHR = vk_device_fn(b'vkAcquireNextImageKHR', PFN_vkAcquireNextImageKHR)
PFN_vkQueuePresentKHR = VK_FUNCTYPE(VkResult, VkQueue, ctypes.POINTER(VkPresentInfoKHR))
vkQueuePresentKHR = vk_device_fn(b'vkQueuePresentKHR', PFN_vkQueuePresentKHR)
if VK_USE_PLATFORM_VI_NN:
    PFN_vkCreateViSurfaceNN = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkViSurfaceCreateInfoNN), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateViSurfaceNN = vk_instance_fn(b'vkCreateViSurfaceNN', PFN_vkCreateViSurfaceNN)
if VK_USE_PLATFORM_WAYLAND_KHR:
    PFN_vkCreateWaylandSurfaceKHR = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkWaylandSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateWaylandSurfaceKHR = vk_instance_fn(b'vkCreateWaylandSurfaceKHR', PFN_vkCreateWaylandSurfaceKHR)
if VK_USE_PLATFORM_WAYLAND_KHR:
    PFN_vkGetPhysicalDeviceWaylandPresentationSupportKHR = VK_FUNCTYPE(VkBool32, VkPhysicalDevice, ctypes.c_uint32, ctypes.POINTER(wl_display))
    vkGetPhysicalDeviceWaylandPresentationSupportKHR = vk_instance_fn(b'vkGetPhysicalDeviceWaylandPresentationSupportKHR', PFN_vkGetPhysicalDeviceWaylandPresentationSupportKHR)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkCreateWin32SurfaceKHR = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkWin32SurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateWin32SurfaceKHR = vk_instance_fn(b'vkCreateWin32SurfaceKHR', PFN_vkCreateWin32SurfaceKHR)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetPhysicalDeviceWin32PresentationSupportKHR = VK_FUNCTYPE(VkBool32, VkPhysicalDevice, ctypes.c_uint32)
    vkGetPhysicalDeviceWin32PresentationSupportKHR = vk_instance_fn(b'vkGetPhysicalDeviceWin32PresentationSupportKHR', PFN_vkGetPhysicalDeviceWin32PresentationSupportKHR)
if VK_USE_PLATFORM_XLIB_KHR:
    PFN_vkCreateXlibSurfaceKHR = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkXlibSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateXlibSurfaceKHR = vk_instance_fn(b'vkCreateXlibSurfaceKHR', PFN_vkCreateXlibSurfaceKHR)
if VK_USE_PLATFORM_XLIB_KHR:
    PFN_vkGetPhysicalDeviceXlibPresentationSupportKHR = VK_FUNCTYPE(VkBool32, VkPhysicalDevice, ctypes.c_uint32, ctypes.POINTER(Display), VisualID)
    vkGetPhysicalDeviceXlibPresentationSupportKHR = vk_instance_fn(b'vkGetPhysicalDeviceXlibPresentationSupportKHR', PFN_vkGetPhysicalDeviceXlibPresentationSupportKHR)
if VK_USE_PLATFORM_XCB_KHR:
    PFN_vkCreateXcbSurfaceKHR = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkXcbSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateXcbSurfaceKHR = vk_instance_fn(b'vkCreateXcbSurfaceKHR', PFN_vkCreateXcbSurfaceKHR)
if VK_USE_PLATFORM_XCB_KHR:
    PFN_vkGetPhysicalDeviceXcbPresentationSupportKHR = VK_FUNCTYPE(VkBool32, VkPhysicalDevice, ctypes.c_uint32, ctypes.POINTER(xcb_connection_t), xcb_visualid_t)
    vkGetPhysicalDeviceXcbPresentationSupportKHR = vk_instance_fn(b'vkGetPhysicalDeviceXcbPresentationSupportKHR', PFN_vkGetPhysicalDeviceXcbPresentationSupportKHR)
if VK_USE_PLATFORM_DIRECTFB_EXT:
    PFN_vkCreateDirectFBSurfaceEXT = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkDirectFBSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateDirectFBSurfaceEXT = vk_instance_fn(b'vkCreateDirectFBSurfaceEXT', PFN_vkCreateDirectFBSurfaceEXT)
if VK_USE_PLATFORM_DIRECTFB_EXT:
    PFN_vkGetPhysicalDeviceDirectFBPresentationSupportEXT = VK_FUNCTYPE(VkBool32, VkPhysicalDevice, ctypes.c_uint32, ctypes.POINTER(IDirectFB))
    vkGetPhysicalDeviceDirectFBPresentationSupportEXT = vk_instance_fn(b'vkGetPhysicalDeviceDirectFBPresentationSupportEXT', PFN_vkGetPhysicalDeviceDirectFBPresentationSupportEXT)
if VK_USE_PLATFORM_FUCHSIA:
    PFN_vkCreateImagePipeSurfaceFUCHSIA = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkImagePipeSurfaceCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateImagePipeSurfaceFUCHSIA = vk_instance_fn(b'vkCreateImagePipeSurfaceFUCHSIA', PFN_vkCreateImagePipeSurfaceFUCHSIA)
if VK_USE_PLATFORM_GGP:
    PFN_vkCreateStreamDescriptorSurfaceGGP = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkStreamDescriptorSurfaceCreateInfoGGP), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateStreamDescriptorSurfaceGGP = vk_instance_fn(b'vkCreateStreamDescriptorSurfaceGGP', PFN_vkCreateStreamDescriptorSurfaceGGP)
PFN_vkCreateDebugReportCallbackEXT = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkDebugReportCallbackCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDebugReportCallbackEXT))
vkCreateDebugReportCallbackEXT = vk_instance_fn(b'vkCreateDebugReportCallbackEXT', PFN_vkCreateDebugReportCallbackEXT)
PFN_vkDestroyDebugReportCallbackEXT = VK_FUNCTYPE(None, VkInstance, VkDebugReportCallbackEXT, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDebugReportCallbackEXT = vk_instance_fn(b'vkDestroyDebugReportCallbackEXT', PFN_vkDestroyDebugReportCallbackEXT)
PFN_vkDebugReportMessageEXT = VK_FUNCTYPE(None, VkInstance, VkDebugReportFlagsEXT, VkDebugReportObjectTypeEXT, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p)
vkDebugReportMessageEXT = vk_instance_fn(b'vkDebugReportMessageEXT', PFN_vkDebugReportMessageEXT)
PFN_vkDebugMarkerSetObjectNameEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDebugMarkerObjectNameInfoEXT))
vkDebugMarkerSetObjectNameEXT = vk_device_fn(b'vkDebugMarkerSetObjectNameEXT', PFN_vkDebugMarkerSetObjectNameEXT)
PFN_vkDebugMarkerSetObjectTagEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDebugMarkerObjectTagInfoEXT))
vkDebugMarkerSetObjectTagEXT = vk_device_fn(b'vkDebugMarkerSetObjectTagEXT', PFN_vkDebugMarkerSetObjectTagEXT)
PFN_vkCmdDebugMarkerBeginEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkDebugMarkerMarkerInfoEXT))
vkCmdDebugMarkerBeginEXT = vk_device_fn(b'vkCmdDebugMarkerBeginEXT', PFN_vkCmdDebugMarkerBeginEXT)
PFN_vkCmdDebugMarkerEndEXT = VK_FUNCTYPE(None, VkCommandBuffer)
vkCmdDebugMarkerEndEXT = vk_device_fn(b'vkCmdDebugMarkerEndEXT', PFN_vkCmdDebugMarkerEndEXT)
PFN_vkCmdDebugMarkerInsertEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkDebugMarkerMarkerInfoEXT))
vkCmdDebugMarkerInsertEXT = vk_device_fn(b'vkCmdDebugMarkerInsertEXT', PFN_vkCmdDebugMarkerInsertEXT)
PFN_vkGetPhysicalDeviceExternalImageFormatPropertiesNV = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkFormat, VkImageType, VkImageTiling, VkImageUsageFlags, VkImageCreateFlags, VkExternalMemoryHandleTypeFlagsNV, ctypes.POINTER(VkExternalImageFormatPropertiesNV))
vkGetPhysicalDeviceExternalImageFormatPropertiesNV = vk_instance_fn(b'vkGetPhysicalDeviceExternalImageFormatPropertiesNV', PFN_vkGetPhysicalDeviceExternalImageFormatPropertiesNV)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetMemoryWin32HandleNV = VK_FUNCTYPE(VkResult, VkDevice, VkDeviceMemory, VkExternalMemoryHandleTypeFlagsNV, ctypes.POINTER(ctypes.wintypes.HANDLE))
    vkGetMemoryWin32HandleNV = vk_device_fn(b'vkGetMemoryWin32HandleNV', PFN_vkGetMemoryWin32HandleNV)
PFN_vkCmdExecuteGeneratedCommandsNV = VK_FUNCTYPE(None, VkCommandBuffer, VkBool32, ctypes.POINTER(VkGeneratedCommandsInfoNV))
vkCmdExecuteGeneratedCommandsNV = vk_device_fn(b'vkCmdExecuteGeneratedCommandsNV', PFN_vkCmdExecuteGeneratedCommandsNV)
PFN_vkCmdPreprocessGeneratedCommandsNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkGeneratedCommandsInfoNV))
vkCmdPreprocessGeneratedCommandsNV = vk_device_fn(b'vkCmdPreprocessGeneratedCommandsNV', PFN_vkCmdPreprocessGeneratedCommandsNV)
PFN_vkCmdBindPipelineShaderGroupNV = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineBindPoint, VkPipeline, ctypes.c_uint32)
vkCmdBindPipelineShaderGroupNV = vk_device_fn(b'vkCmdBindPipelineShaderGroupNV', PFN_vkCmdBindPipelineShaderGroupNV)
PFN_vkGetGeneratedCommandsMemoryRequirementsNV = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkGeneratedCommandsMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2))
vkGetGeneratedCommandsMemoryRequirementsNV = vk_device_fn(b'vkGetGeneratedCommandsMemoryRequirementsNV', PFN_vkGetGeneratedCommandsMemoryRequirementsNV)
PFN_vkCreateIndirectCommandsLayoutNV = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkIndirectCommandsLayoutCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkIndirectCommandsLayoutNV))
vkCreateIndirectCommandsLayoutNV = vk_device_fn(b'vkCreateIndirectCommandsLayoutNV', PFN_vkCreateIndirectCommandsLayoutNV)
PFN_vkDestroyIndirectCommandsLayoutNV = VK_FUNCTYPE(None, VkDevice, VkIndirectCommandsLayoutNV, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyIndirectCommandsLayoutNV = vk_device_fn(b'vkDestroyIndirectCommandsLayoutNV', PFN_vkDestroyIndirectCommandsLayoutNV)
PFN_vkGetPhysicalDeviceFeatures2 = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceFeatures2))
vkGetPhysicalDeviceFeatures2 = VK_DLL.vkGetPhysicalDeviceFeatures2
vkGetPhysicalDeviceFeatures2.restype = None
vkGetPhysicalDeviceFeatures2.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceFeatures2)]
PFN_vkGetPhysicalDeviceFeatures2KHR = PFN_vkGetPhysicalDeviceFeatures2
vkGetPhysicalDeviceFeatures2KHR = vkGetPhysicalDeviceFeatures2
PFN_vkGetPhysicalDeviceProperties2 = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceProperties2))
vkGetPhysicalDeviceProperties2 = VK_DLL.vkGetPhysicalDeviceProperties2
vkGetPhysicalDeviceProperties2.restype = None
vkGetPhysicalDeviceProperties2.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceProperties2)]
PFN_vkGetPhysicalDeviceProperties2KHR = PFN_vkGetPhysicalDeviceProperties2
vkGetPhysicalDeviceProperties2KHR = vkGetPhysicalDeviceProperties2
PFN_vkGetPhysicalDeviceFormatProperties2 = VK_FUNCTYPE(None, VkPhysicalDevice, VkFormat, ctypes.POINTER(VkFormatProperties2))
vkGetPhysicalDeviceFormatProperties2 = VK_DLL.vkGetPhysicalDeviceFormatProperties2
vkGetPhysicalDeviceFormatProperties2.restype = None
vkGetPhysicalDeviceFormatProperties2.argtypes = [VkPhysicalDevice, VkFormat, ctypes.POINTER(VkFormatProperties2)]
PFN_vkGetPhysicalDeviceFormatProperties2KHR = PFN_vkGetPhysicalDeviceFormatProperties2
vkGetPhysicalDeviceFormatProperties2KHR = vkGetPhysicalDeviceFormatProperties2
PFN_vkGetPhysicalDeviceImageFormatProperties2 = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceImageFormatInfo2), ctypes.POINTER(VkImageFormatProperties2))
vkGetPhysicalDeviceImageFormatProperties2 = VK_DLL.vkGetPhysicalDeviceImageFormatProperties2
vkGetPhysicalDeviceImageFormatProperties2.restype = VkResult
vkGetPhysicalDeviceImageFormatProperties2.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceImageFormatInfo2), ctypes.POINTER(VkImageFormatProperties2)]
PFN_vkGetPhysicalDeviceImageFormatProperties2KHR = PFN_vkGetPhysicalDeviceImageFormatProperties2
vkGetPhysicalDeviceImageFormatProperties2KHR = vkGetPhysicalDeviceImageFormatProperties2
PFN_vkGetPhysicalDeviceQueueFamilyProperties2 = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties2))
vkGetPhysicalDeviceQueueFamilyProperties2 = VK_DLL.vkGetPhysicalDeviceQueueFamilyProperties2
vkGetPhysicalDeviceQueueFamilyProperties2.restype = None
vkGetPhysicalDeviceQueueFamilyProperties2.argtypes = [VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties2)]
PFN_vkGetPhysicalDeviceQueueFamilyProperties2KHR = PFN_vkGetPhysicalDeviceQueueFamilyProperties2
vkGetPhysicalDeviceQueueFamilyProperties2KHR = vkGetPhysicalDeviceQueueFamilyProperties2
PFN_vkGetPhysicalDeviceMemoryProperties2 = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceMemoryProperties2))
vkGetPhysicalDeviceMemoryProperties2 = VK_DLL.vkGetPhysicalDeviceMemoryProperties2
vkGetPhysicalDeviceMemoryProperties2.restype = None
vkGetPhysicalDeviceMemoryProperties2.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceMemoryProperties2)]
PFN_vkGetPhysicalDeviceMemoryProperties2KHR = PFN_vkGetPhysicalDeviceMemoryProperties2
vkGetPhysicalDeviceMemoryProperties2KHR = vkGetPhysicalDeviceMemoryProperties2
PFN_vkGetPhysicalDeviceSparseImageFormatProperties2 = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceSparseImageFormatInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties2))
vkGetPhysicalDeviceSparseImageFormatProperties2 = VK_DLL.vkGetPhysicalDeviceSparseImageFormatProperties2
vkGetPhysicalDeviceSparseImageFormatProperties2.restype = None
vkGetPhysicalDeviceSparseImageFormatProperties2.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceSparseImageFormatInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties2)]
PFN_vkGetPhysicalDeviceSparseImageFormatProperties2KHR = PFN_vkGetPhysicalDeviceSparseImageFormatProperties2
vkGetPhysicalDeviceSparseImageFormatProperties2KHR = vkGetPhysicalDeviceSparseImageFormatProperties2
PFN_vkCmdPushDescriptorSetKHR = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineBindPoint, VkPipelineLayout, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet))
vkCmdPushDescriptorSetKHR = vk_device_fn(b'vkCmdPushDescriptorSetKHR', PFN_vkCmdPushDescriptorSetKHR)
PFN_vkTrimCommandPool = VK_FUNCTYPE(None, VkDevice, VkCommandPool, VkCommandPoolTrimFlags)
vkTrimCommandPool = VK_DLL.vkTrimCommandPool
vkTrimCommandPool.restype = None
vkTrimCommandPool.argtypes = [VkDevice, VkCommandPool, VkCommandPoolTrimFlags]
PFN_vkTrimCommandPoolKHR = PFN_vkTrimCommandPool
vkTrimCommandPoolKHR = vkTrimCommandPool
PFN_vkGetPhysicalDeviceExternalBufferProperties = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceExternalBufferInfo), ctypes.POINTER(VkExternalBufferProperties))
vkGetPhysicalDeviceExternalBufferProperties = VK_DLL.vkGetPhysicalDeviceExternalBufferProperties
vkGetPhysicalDeviceExternalBufferProperties.restype = None
vkGetPhysicalDeviceExternalBufferProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceExternalBufferInfo), ctypes.POINTER(VkExternalBufferProperties)]
PFN_vkGetPhysicalDeviceExternalBufferPropertiesKHR = PFN_vkGetPhysicalDeviceExternalBufferProperties
vkGetPhysicalDeviceExternalBufferPropertiesKHR = vkGetPhysicalDeviceExternalBufferProperties
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetMemoryWin32HandleKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkMemoryGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.wintypes.HANDLE))
    vkGetMemoryWin32HandleKHR = vk_device_fn(b'vkGetMemoryWin32HandleKHR', PFN_vkGetMemoryWin32HandleKHR)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetMemoryWin32HandlePropertiesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkExternalMemoryHandleTypeFlagBits, ctypes.wintypes.HANDLE, ctypes.POINTER(VkMemoryWin32HandlePropertiesKHR))
    vkGetMemoryWin32HandlePropertiesKHR = vk_device_fn(b'vkGetMemoryWin32HandlePropertiesKHR', PFN_vkGetMemoryWin32HandlePropertiesKHR)
PFN_vkGetMemoryFdKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkMemoryGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetMemoryFdKHR = vk_device_fn(b'vkGetMemoryFdKHR', PFN_vkGetMemoryFdKHR)
PFN_vkGetMemoryFdPropertiesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkExternalMemoryHandleTypeFlagBits, ctypes.c_int, ctypes.POINTER(VkMemoryFdPropertiesKHR))
vkGetMemoryFdPropertiesKHR = vk_device_fn(b'vkGetMemoryFdPropertiesKHR', PFN_vkGetMemoryFdPropertiesKHR)
PFN_vkGetPhysicalDeviceExternalSemaphoreProperties = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceExternalSemaphoreInfo), ctypes.POINTER(VkExternalSemaphoreProperties))
vkGetPhysicalDeviceExternalSemaphoreProperties = VK_DLL.vkGetPhysicalDeviceExternalSemaphoreProperties
vkGetPhysicalDeviceExternalSemaphoreProperties.restype = None
vkGetPhysicalDeviceExternalSemaphoreProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceExternalSemaphoreInfo), ctypes.POINTER(VkExternalSemaphoreProperties)]
PFN_vkGetPhysicalDeviceExternalSemaphorePropertiesKHR = PFN_vkGetPhysicalDeviceExternalSemaphoreProperties
vkGetPhysicalDeviceExternalSemaphorePropertiesKHR = vkGetPhysicalDeviceExternalSemaphoreProperties
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetSemaphoreWin32HandleKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSemaphoreGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.wintypes.HANDLE))
    vkGetSemaphoreWin32HandleKHR = vk_device_fn(b'vkGetSemaphoreWin32HandleKHR', PFN_vkGetSemaphoreWin32HandleKHR)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkImportSemaphoreWin32HandleKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkImportSemaphoreWin32HandleInfoKHR))
    vkImportSemaphoreWin32HandleKHR = vk_device_fn(b'vkImportSemaphoreWin32HandleKHR', PFN_vkImportSemaphoreWin32HandleKHR)
PFN_vkGetSemaphoreFdKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSemaphoreGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetSemaphoreFdKHR = vk_device_fn(b'vkGetSemaphoreFdKHR', PFN_vkGetSemaphoreFdKHR)
PFN_vkImportSemaphoreFdKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkImportSemaphoreFdInfoKHR))
vkImportSemaphoreFdKHR = vk_device_fn(b'vkImportSemaphoreFdKHR', PFN_vkImportSemaphoreFdKHR)
PFN_vkGetPhysicalDeviceExternalFenceProperties = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceExternalFenceInfo), ctypes.POINTER(VkExternalFenceProperties))
vkGetPhysicalDeviceExternalFenceProperties = VK_DLL.vkGetPhysicalDeviceExternalFenceProperties
vkGetPhysicalDeviceExternalFenceProperties.restype = None
vkGetPhysicalDeviceExternalFenceProperties.argtypes = [VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceExternalFenceInfo), ctypes.POINTER(VkExternalFenceProperties)]
PFN_vkGetPhysicalDeviceExternalFencePropertiesKHR = PFN_vkGetPhysicalDeviceExternalFenceProperties
vkGetPhysicalDeviceExternalFencePropertiesKHR = vkGetPhysicalDeviceExternalFenceProperties
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetFenceWin32HandleKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkFenceGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.wintypes.HANDLE))
    vkGetFenceWin32HandleKHR = vk_device_fn(b'vkGetFenceWin32HandleKHR', PFN_vkGetFenceWin32HandleKHR)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkImportFenceWin32HandleKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkImportFenceWin32HandleInfoKHR))
    vkImportFenceWin32HandleKHR = vk_device_fn(b'vkImportFenceWin32HandleKHR', PFN_vkImportFenceWin32HandleKHR)
PFN_vkGetFenceFdKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkFenceGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetFenceFdKHR = vk_device_fn(b'vkGetFenceFdKHR', PFN_vkGetFenceFdKHR)
PFN_vkImportFenceFdKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkImportFenceFdInfoKHR))
vkImportFenceFdKHR = vk_device_fn(b'vkImportFenceFdKHR', PFN_vkImportFenceFdKHR)
PFN_vkReleaseDisplayEXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkDisplayKHR)
vkReleaseDisplayEXT = vk_instance_fn(b'vkReleaseDisplayEXT', PFN_vkReleaseDisplayEXT)
if VK_USE_PLATFORM_XLIB_XRANDR_EXT:
    PFN_vkAcquireXlibDisplayEXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(Display), VkDisplayKHR)
    vkAcquireXlibDisplayEXT = vk_instance_fn(b'vkAcquireXlibDisplayEXT', PFN_vkAcquireXlibDisplayEXT)
if VK_USE_PLATFORM_XLIB_XRANDR_EXT:
    PFN_vkGetRandROutputDisplayEXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(Display), RROutput, ctypes.POINTER(VkDisplayKHR))
    vkGetRandROutputDisplayEXT = vk_instance_fn(b'vkGetRandROutputDisplayEXT', PFN_vkGetRandROutputDisplayEXT)
PFN_vkDisplayPowerControlEXT = VK_FUNCTYPE(VkResult, VkDevice, VkDisplayKHR, ctypes.POINTER(VkDisplayPowerInfoEXT))
vkDisplayPowerControlEXT = vk_device_fn(b'vkDisplayPowerControlEXT', PFN_vkDisplayPowerControlEXT)
PFN_vkRegisterDeviceEventEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDeviceEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkFence))
vkRegisterDeviceEventEXT = vk_device_fn(b'vkRegisterDeviceEventEXT', PFN_vkRegisterDeviceEventEXT)
PFN_vkRegisterDisplayEventEXT = VK_FUNCTYPE(VkResult, VkDevice, VkDisplayKHR, ctypes.POINTER(VkDisplayEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkFence))
vkRegisterDisplayEventEXT = vk_device_fn(b'vkRegisterDisplayEventEXT', PFN_vkRegisterDisplayEventEXT)
PFN_vkGetSwapchainCounterEXT = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR, VkSurfaceCounterFlagBitsEXT, ctypes.POINTER(ctypes.c_uint64))
vkGetSwapchainCounterEXT = vk_device_fn(b'vkGetSwapchainCounterEXT', PFN_vkGetSwapchainCounterEXT)
PFN_vkGetPhysicalDeviceSurfaceCapabilities2EXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkSurfaceKHR, ctypes.POINTER(VkSurfaceCapabilities2EXT))
vkGetPhysicalDeviceSurfaceCapabilities2EXT = vk_instance_fn(b'vkGetPhysicalDeviceSurfaceCapabilities2EXT', PFN_vkGetPhysicalDeviceSurfaceCapabilities2EXT)
PFN_vkEnumeratePhysicalDeviceGroups = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceGroupProperties))
vkEnumeratePhysicalDeviceGroups = VK_DLL.vkEnumeratePhysicalDeviceGroups
vkEnumeratePhysicalDeviceGroups.restype = VkResult
vkEnumeratePhysicalDeviceGroups.argtypes = [VkInstance, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceGroupProperties)]
PFN_vkEnumeratePhysicalDeviceGroupsKHR = PFN_vkEnumeratePhysicalDeviceGroups
vkEnumeratePhysicalDeviceGroupsKHR = vkEnumeratePhysicalDeviceGroups
PFN_vkGetDeviceGroupPeerMemoryFeatures = VK_FUNCTYPE(None, VkDevice, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkPeerMemoryFeatureFlags))
vkGetDeviceGroupPeerMemoryFeatures = VK_DLL.vkGetDeviceGroupPeerMemoryFeatures
vkGetDeviceGroupPeerMemoryFeatures.restype = None
vkGetDeviceGroupPeerMemoryFeatures.argtypes = [VkDevice, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkPeerMemoryFeatureFlags)]
PFN_vkGetDeviceGroupPeerMemoryFeaturesKHR = PFN_vkGetDeviceGroupPeerMemoryFeatures
vkGetDeviceGroupPeerMemoryFeaturesKHR = vkGetDeviceGroupPeerMemoryFeatures
PFN_vkBindBufferMemory2 = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkBindBufferMemoryInfo))
vkBindBufferMemory2 = VK_DLL.vkBindBufferMemory2
vkBindBufferMemory2.restype = VkResult
vkBindBufferMemory2.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkBindBufferMemoryInfo)]
PFN_vkBindBufferMemory2KHR = PFN_vkBindBufferMemory2
vkBindBufferMemory2KHR = vkBindBufferMemory2
PFN_vkBindImageMemory2 = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkBindImageMemoryInfo))
vkBindImageMemory2 = VK_DLL.vkBindImageMemory2
vkBindImageMemory2.restype = VkResult
vkBindImageMemory2.argtypes = [VkDevice, ctypes.c_uint32, ctypes.POINTER(VkBindImageMemoryInfo)]
PFN_vkBindImageMemory2KHR = PFN_vkBindImageMemory2
vkBindImageMemory2KHR = vkBindImageMemory2
PFN_vkCmdSetDeviceMask = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32)
vkCmdSetDeviceMask = VK_DLL.vkCmdSetDeviceMask
vkCmdSetDeviceMask.restype = None
vkCmdSetDeviceMask.argtypes = [VkCommandBuffer, ctypes.c_uint32]
PFN_vkCmdSetDeviceMaskKHR = PFN_vkCmdSetDeviceMask
vkCmdSetDeviceMaskKHR = vkCmdSetDeviceMask
PFN_vkGetDeviceGroupPresentCapabilitiesKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDeviceGroupPresentCapabilitiesKHR))
vkGetDeviceGroupPresentCapabilitiesKHR = vk_device_fn(b'vkGetDeviceGroupPresentCapabilitiesKHR', PFN_vkGetDeviceGroupPresentCapabilitiesKHR)
PFN_vkGetDeviceGroupSurfacePresentModesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkSurfaceKHR, ctypes.POINTER(VkDeviceGroupPresentModeFlagsKHR))
vkGetDeviceGroupSurfacePresentModesKHR = vk_device_fn(b'vkGetDeviceGroupSurfacePresentModesKHR', PFN_vkGetDeviceGroupSurfacePresentModesKHR)
PFN_vkAcquireNextImage2KHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkAcquireNextImageInfoKHR), ctypes.POINTER(ctypes.c_uint32))
vkAcquireNextImage2KHR = vk_device_fn(b'vkAcquireNextImage2KHR', PFN_vkAcquireNextImage2KHR)
PFN_vkCmdDispatchBase = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDispatchBase = VK_DLL.vkCmdDispatchBase
vkCmdDispatchBase.restype = None
vkCmdDispatchBase.argtypes = [VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDispatchBaseKHR = PFN_vkCmdDispatchBase
vkCmdDispatchBaseKHR = vkCmdDispatchBase
PFN_vkGetPhysicalDevicePresentRectanglesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkSurfaceKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkRect2D))
vkGetPhysicalDevicePresentRectanglesKHR = vk_device_fn(b'vkGetPhysicalDevicePresentRectanglesKHR', PFN_vkGetPhysicalDevicePresentRectanglesKHR)
PFN_vkCreateDescriptorUpdateTemplate = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDescriptorUpdateTemplateCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDescriptorUpdateTemplate))
vkCreateDescriptorUpdateTemplate = VK_DLL.vkCreateDescriptorUpdateTemplate
vkCreateDescriptorUpdateTemplate.restype = VkResult
vkCreateDescriptorUpdateTemplate.argtypes = [VkDevice, ctypes.POINTER(VkDescriptorUpdateTemplateCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDescriptorUpdateTemplate)]
PFN_vkCreateDescriptorUpdateTemplateKHR = PFN_vkCreateDescriptorUpdateTemplate
vkCreateDescriptorUpdateTemplateKHR = vkCreateDescriptorUpdateTemplate
PFN_vkDestroyDescriptorUpdateTemplate = VK_FUNCTYPE(None, VkDevice, VkDescriptorUpdateTemplate, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDescriptorUpdateTemplate = VK_DLL.vkDestroyDescriptorUpdateTemplate
vkDestroyDescriptorUpdateTemplate.restype = None
vkDestroyDescriptorUpdateTemplate.argtypes = [VkDevice, VkDescriptorUpdateTemplate, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkDestroyDescriptorUpdateTemplateKHR = PFN_vkDestroyDescriptorUpdateTemplate
vkDestroyDescriptorUpdateTemplateKHR = vkDestroyDescriptorUpdateTemplate
PFN_vkUpdateDescriptorSetWithTemplate = VK_FUNCTYPE(None, VkDevice, VkDescriptorSet, VkDescriptorUpdateTemplate, ctypes.c_void_p)
vkUpdateDescriptorSetWithTemplate = VK_DLL.vkUpdateDescriptorSetWithTemplate
vkUpdateDescriptorSetWithTemplate.restype = None
vkUpdateDescriptorSetWithTemplate.argtypes = [VkDevice, VkDescriptorSet, VkDescriptorUpdateTemplate, ctypes.c_void_p]
PFN_vkUpdateDescriptorSetWithTemplateKHR = PFN_vkUpdateDescriptorSetWithTemplate
vkUpdateDescriptorSetWithTemplateKHR = vkUpdateDescriptorSetWithTemplate
PFN_vkCmdPushDescriptorSetWithTemplateKHR = VK_FUNCTYPE(None, VkCommandBuffer, VkDescriptorUpdateTemplate, VkPipelineLayout, ctypes.c_uint32, ctypes.c_void_p)
vkCmdPushDescriptorSetWithTemplateKHR = vk_device_fn(b'vkCmdPushDescriptorSetWithTemplateKHR', PFN_vkCmdPushDescriptorSetWithTemplateKHR)
PFN_vkSetHdrMetadataEXT = VK_FUNCTYPE(None, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkSwapchainKHR), ctypes.POINTER(VkHdrMetadataEXT))
vkSetHdrMetadataEXT = vk_device_fn(b'vkSetHdrMetadataEXT', PFN_vkSetHdrMetadataEXT)
PFN_vkGetSwapchainStatusKHR = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR)
vkGetSwapchainStatusKHR = vk_device_fn(b'vkGetSwapchainStatusKHR', PFN_vkGetSwapchainStatusKHR)
PFN_vkGetRefreshCycleDurationGOOGLE = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR, ctypes.POINTER(VkRefreshCycleDurationGOOGLE))
vkGetRefreshCycleDurationGOOGLE = vk_device_fn(b'vkGetRefreshCycleDurationGOOGLE', PFN_vkGetRefreshCycleDurationGOOGLE)
PFN_vkGetPastPresentationTimingGOOGLE = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPastPresentationTimingGOOGLE))
vkGetPastPresentationTimingGOOGLE = vk_device_fn(b'vkGetPastPresentationTimingGOOGLE', PFN_vkGetPastPresentationTimingGOOGLE)
if VK_USE_PLATFORM_IOS_MVK:
    PFN_vkCreateIOSSurfaceMVK = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkIOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateIOSSurfaceMVK = vk_instance_fn(b'vkCreateIOSSurfaceMVK', PFN_vkCreateIOSSurfaceMVK)
if VK_USE_PLATFORM_MACOS_MVK:
    PFN_vkCreateMacOSSurfaceMVK = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkMacOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateMacOSSurfaceMVK = vk_instance_fn(b'vkCreateMacOSSurfaceMVK', PFN_vkCreateMacOSSurfaceMVK)
if VK_USE_PLATFORM_METAL_EXT:
    PFN_vkCreateMetalSurfaceEXT = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkMetalSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
    vkCreateMetalSurfaceEXT = vk_instance_fn(b'vkCreateMetalSurfaceEXT', PFN_vkCreateMetalSurfaceEXT)
PFN_vkCmdSetViewportWScalingNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewportWScalingNV))
vkCmdSetViewportWScalingNV = vk_device_fn(b'vkCmdSetViewportWScalingNV', PFN_vkCmdSetViewportWScalingNV)
PFN_vkCmdSetDiscardRectangleEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetDiscardRectangleEXT = vk_device_fn(b'vkCmdSetDiscardRectangleEXT', PFN_vkCmdSetDiscardRectangleEXT)
PFN_vkCmdSetSampleLocationsEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkSampleLocationsInfoEXT))
vkCmdSetSampleLocationsEXT = vk_device_fn(b'vkCmdSetSampleLocationsEXT', PFN_vkCmdSetSampleLocationsEXT)
PFN_vkGetPhysicalDeviceMultisamplePropertiesEXT = VK_FUNCTYPE(None, VkPhysicalDevice, VkSampleCountFlagBits, ctypes.POINTER(VkMultisamplePropertiesEXT))
vkGetPhysicalDeviceMultisamplePropertiesEXT = vk_device_fn(b'vkGetPhysicalDeviceMultisamplePropertiesEXT', PFN_vkGetPhysicalDeviceMultisamplePropertiesEXT)
PFN_vkGetPhysicalDeviceSurfaceCapabilities2KHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(VkSurfaceCapabilities2KHR))
vkGetPhysicalDeviceSurfaceCapabilities2KHR = vk_instance_fn(b'vkGetPhysicalDeviceSurfaceCapabilities2KHR', PFN_vkGetPhysicalDeviceSurfaceCapabilities2KHR)
PFN_vkGetPhysicalDeviceSurfaceFormats2KHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormat2KHR))
vkGetPhysicalDeviceSurfaceFormats2KHR = vk_instance_fn(b'vkGetPhysicalDeviceSurfaceFormats2KHR', PFN_vkGetPhysicalDeviceSurfaceFormats2KHR)
PFN_vkGetPhysicalDeviceDisplayProperties2KHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayProperties2KHR))
vkGetPhysicalDeviceDisplayProperties2KHR = vk_instance_fn(b'vkGetPhysicalDeviceDisplayProperties2KHR', PFN_vkGetPhysicalDeviceDisplayProperties2KHR)
PFN_vkGetPhysicalDeviceDisplayPlaneProperties2KHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlaneProperties2KHR))
vkGetPhysicalDeviceDisplayPlaneProperties2KHR = vk_instance_fn(b'vkGetPhysicalDeviceDisplayPlaneProperties2KHR', PFN_vkGetPhysicalDeviceDisplayPlaneProperties2KHR)
PFN_vkGetDisplayModeProperties2KHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, VkDisplayKHR, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModeProperties2KHR))
vkGetDisplayModeProperties2KHR = vk_instance_fn(b'vkGetDisplayModeProperties2KHR', PFN_vkGetDisplayModeProperties2KHR)
PFN_vkGetDisplayPlaneCapabilities2KHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(VkDisplayPlaneInfo2KHR), ctypes.POINTER(VkDisplayPlaneCapabilities2KHR))
vkGetDisplayPlaneCapabilities2KHR = vk_instance_fn(b'vkGetDisplayPlaneCapabilities2KHR', PFN_vkGetDisplayPlaneCapabilities2KHR)
PFN_vkGetBufferMemoryRequirements2 = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkBufferMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
vkGetBufferMemoryRequirements2 = VK_DLL.vkGetBufferMemoryRequirements2
vkGetBufferMemoryRequirements2.restype = None
vkGetBufferMemoryRequirements2.argtypes = [VkDevice, ctypes.POINTER(VkBufferMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2)]
PFN_vkGetBufferMemoryRequirements2KHR = PFN_vkGetBufferMemoryRequirements2
vkGetBufferMemoryRequirements2KHR = vkGetBufferMemoryRequirements2
PFN_vkGetImageMemoryRequirements2 = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkImageMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
vkGetImageMemoryRequirements2 = VK_DLL.vkGetImageMemoryRequirements2
vkGetImageMemoryRequirements2.restype = None
vkGetImageMemoryRequirements2.argtypes = [VkDevice, ctypes.POINTER(VkImageMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2)]
PFN_vkGetImageMemoryRequirements2KHR = PFN_vkGetImageMemoryRequirements2
vkGetImageMemoryRequirements2KHR = vkGetImageMemoryRequirements2
PFN_vkGetImageSparseMemoryRequirements2 = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkImageSparseMemoryRequirementsInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
vkGetImageSparseMemoryRequirements2 = VK_DLL.vkGetImageSparseMemoryRequirements2
vkGetImageSparseMemoryRequirements2.restype = None
vkGetImageSparseMemoryRequirements2.argtypes = [VkDevice, ctypes.POINTER(VkImageSparseMemoryRequirementsInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2)]
PFN_vkGetImageSparseMemoryRequirements2KHR = PFN_vkGetImageSparseMemoryRequirements2
vkGetImageSparseMemoryRequirements2KHR = vkGetImageSparseMemoryRequirements2
PFN_vkCreateSamplerYcbcrConversion = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSamplerYcbcrConversionCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSamplerYcbcrConversion))
vkCreateSamplerYcbcrConversion = VK_DLL.vkCreateSamplerYcbcrConversion
vkCreateSamplerYcbcrConversion.restype = VkResult
vkCreateSamplerYcbcrConversion.argtypes = [VkDevice, ctypes.POINTER(VkSamplerYcbcrConversionCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSamplerYcbcrConversion)]
PFN_vkCreateSamplerYcbcrConversionKHR = PFN_vkCreateSamplerYcbcrConversion
vkCreateSamplerYcbcrConversionKHR = vkCreateSamplerYcbcrConversion
PFN_vkDestroySamplerYcbcrConversion = VK_FUNCTYPE(None, VkDevice, VkSamplerYcbcrConversion, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySamplerYcbcrConversion = VK_DLL.vkDestroySamplerYcbcrConversion
vkDestroySamplerYcbcrConversion.restype = None
vkDestroySamplerYcbcrConversion.argtypes = [VkDevice, VkSamplerYcbcrConversion, ctypes.POINTER(VkAllocationCallbacks)]
PFN_vkDestroySamplerYcbcrConversionKHR = PFN_vkDestroySamplerYcbcrConversion
vkDestroySamplerYcbcrConversionKHR = vkDestroySamplerYcbcrConversion
PFN_vkGetDeviceQueue2 = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkDeviceQueueInfo2), ctypes.POINTER(VkQueue))
vkGetDeviceQueue2 = VK_DLL.vkGetDeviceQueue2
vkGetDeviceQueue2.restype = None
vkGetDeviceQueue2.argtypes = [VkDevice, ctypes.POINTER(VkDeviceQueueInfo2), ctypes.POINTER(VkQueue)]
PFN_vkCreateValidationCacheEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkValidationCacheCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkValidationCacheEXT))
vkCreateValidationCacheEXT = vk_device_fn(b'vkCreateValidationCacheEXT', PFN_vkCreateValidationCacheEXT)
PFN_vkDestroyValidationCacheEXT = VK_FUNCTYPE(None, VkDevice, VkValidationCacheEXT, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyValidationCacheEXT = vk_device_fn(b'vkDestroyValidationCacheEXT', PFN_vkDestroyValidationCacheEXT)
PFN_vkGetValidationCacheDataEXT = VK_FUNCTYPE(VkResult, VkDevice, VkValidationCacheEXT, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetValidationCacheDataEXT = vk_device_fn(b'vkGetValidationCacheDataEXT', PFN_vkGetValidationCacheDataEXT)
PFN_vkMergeValidationCachesEXT = VK_FUNCTYPE(VkResult, VkDevice, VkValidationCacheEXT, ctypes.c_uint32, ctypes.POINTER(VkValidationCacheEXT))
vkMergeValidationCachesEXT = vk_device_fn(b'vkMergeValidationCachesEXT', PFN_vkMergeValidationCachesEXT)
PFN_vkGetDescriptorSetLayoutSupport = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkDescriptorSetLayoutSupport))
vkGetDescriptorSetLayoutSupport = VK_DLL.vkGetDescriptorSetLayoutSupport
vkGetDescriptorSetLayoutSupport.restype = None
vkGetDescriptorSetLayoutSupport.argtypes = [VkDevice, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkDescriptorSetLayoutSupport)]
PFN_vkGetDescriptorSetLayoutSupportKHR = PFN_vkGetDescriptorSetLayoutSupport
vkGetDescriptorSetLayoutSupportKHR = vkGetDescriptorSetLayoutSupport
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkGetSwapchainGrallocUsageANDROID = VK_FUNCTYPE(VkResult, VkDevice, VkFormat, VkImageUsageFlags, ctypes.POINTER(ctypes.c_int))
    vkGetSwapchainGrallocUsageANDROID = vk_device_fn(b'vkGetSwapchainGrallocUsageANDROID', PFN_vkGetSwapchainGrallocUsageANDROID)
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkGetSwapchainGrallocUsage2ANDROID = VK_FUNCTYPE(VkResult, VkDevice, VkFormat, VkImageUsageFlags, VkSwapchainImageUsageFlagsANDROID, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
    vkGetSwapchainGrallocUsage2ANDROID = vk_device_fn(b'vkGetSwapchainGrallocUsage2ANDROID', PFN_vkGetSwapchainGrallocUsage2ANDROID)
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkAcquireImageANDROID = VK_FUNCTYPE(VkResult, VkDevice, VkImage, ctypes.c_int, VkSemaphore, VkFence)
    vkAcquireImageANDROID = vk_device_fn(b'vkAcquireImageANDROID', PFN_vkAcquireImageANDROID)
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkQueueSignalReleaseImageANDROID = VK_FUNCTYPE(VkResult, VkQueue, ctypes.c_uint32, ctypes.POINTER(VkSemaphore), VkImage, ctypes.POINTER(ctypes.c_int))
    vkQueueSignalReleaseImageANDROID = vk_device_fn(b'vkQueueSignalReleaseImageANDROID', PFN_vkQueueSignalReleaseImageANDROID)
PFN_vkGetShaderInfoAMD = VK_FUNCTYPE(VkResult, VkDevice, VkPipeline, VkShaderStageFlagBits, VkShaderInfoTypeAMD, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetShaderInfoAMD = vk_device_fn(b'vkGetShaderInfoAMD', PFN_vkGetShaderInfoAMD)
PFN_vkSetLocalDimmingAMD = VK_FUNCTYPE(None, VkDevice, VkSwapchainKHR, VkBool32)
vkSetLocalDimmingAMD = vk_device_fn(b'vkSetLocalDimmingAMD', PFN_vkSetLocalDimmingAMD)
PFN_vkGetPhysicalDeviceCalibrateableTimeDomainsEXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkTimeDomainEXT))
vkGetPhysicalDeviceCalibrateableTimeDomainsEXT = vk_device_fn(b'vkGetPhysicalDeviceCalibrateableTimeDomainsEXT', PFN_vkGetPhysicalDeviceCalibrateableTimeDomainsEXT)
PFN_vkGetCalibratedTimestampsEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkCalibratedTimestampInfoEXT), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkGetCalibratedTimestampsEXT = vk_device_fn(b'vkGetCalibratedTimestampsEXT', PFN_vkGetCalibratedTimestampsEXT)
PFN_vkSetDebugUtilsObjectNameEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT))
vkSetDebugUtilsObjectNameEXT = vk_instance_fn(b'vkSetDebugUtilsObjectNameEXT', PFN_vkSetDebugUtilsObjectNameEXT)
PFN_vkSetDebugUtilsObjectTagEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkDebugUtilsObjectTagInfoEXT))
vkSetDebugUtilsObjectTagEXT = vk_instance_fn(b'vkSetDebugUtilsObjectTagEXT', PFN_vkSetDebugUtilsObjectTagEXT)
PFN_vkQueueBeginDebugUtilsLabelEXT = VK_FUNCTYPE(None, VkQueue, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkQueueBeginDebugUtilsLabelEXT = vk_instance_fn(b'vkQueueBeginDebugUtilsLabelEXT', PFN_vkQueueBeginDebugUtilsLabelEXT)
PFN_vkQueueEndDebugUtilsLabelEXT = VK_FUNCTYPE(None, VkQueue)
vkQueueEndDebugUtilsLabelEXT = vk_instance_fn(b'vkQueueEndDebugUtilsLabelEXT', PFN_vkQueueEndDebugUtilsLabelEXT)
PFN_vkQueueInsertDebugUtilsLabelEXT = VK_FUNCTYPE(None, VkQueue, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkQueueInsertDebugUtilsLabelEXT = vk_instance_fn(b'vkQueueInsertDebugUtilsLabelEXT', PFN_vkQueueInsertDebugUtilsLabelEXT)
PFN_vkCmdBeginDebugUtilsLabelEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCmdBeginDebugUtilsLabelEXT = vk_instance_fn(b'vkCmdBeginDebugUtilsLabelEXT', PFN_vkCmdBeginDebugUtilsLabelEXT)
PFN_vkCmdEndDebugUtilsLabelEXT = VK_FUNCTYPE(None, VkCommandBuffer)
vkCmdEndDebugUtilsLabelEXT = vk_instance_fn(b'vkCmdEndDebugUtilsLabelEXT', PFN_vkCmdEndDebugUtilsLabelEXT)
PFN_vkCmdInsertDebugUtilsLabelEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCmdInsertDebugUtilsLabelEXT = vk_instance_fn(b'vkCmdInsertDebugUtilsLabelEXT', PFN_vkCmdInsertDebugUtilsLabelEXT)
PFN_vkCreateDebugUtilsMessengerEXT = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkDebugUtilsMessengerCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDebugUtilsMessengerEXT))
vkCreateDebugUtilsMessengerEXT = vk_instance_fn(b'vkCreateDebugUtilsMessengerEXT', PFN_vkCreateDebugUtilsMessengerEXT)
PFN_vkDestroyDebugUtilsMessengerEXT = VK_FUNCTYPE(None, VkInstance, VkDebugUtilsMessengerEXT, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDebugUtilsMessengerEXT = vk_instance_fn(b'vkDestroyDebugUtilsMessengerEXT', PFN_vkDestroyDebugUtilsMessengerEXT)
PFN_vkSubmitDebugUtilsMessageEXT = VK_FUNCTYPE(None, VkInstance, VkDebugUtilsMessageSeverityFlagBitsEXT, VkDebugUtilsMessageTypeFlagsEXT, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT))
vkSubmitDebugUtilsMessageEXT = vk_instance_fn(b'vkSubmitDebugUtilsMessageEXT', PFN_vkSubmitDebugUtilsMessageEXT)
PFN_vkGetMemoryHostPointerPropertiesEXT = VK_FUNCTYPE(VkResult, VkDevice, VkExternalMemoryHandleTypeFlagBits, ctypes.c_void_p, ctypes.POINTER(VkMemoryHostPointerPropertiesEXT))
vkGetMemoryHostPointerPropertiesEXT = vk_device_fn(b'vkGetMemoryHostPointerPropertiesEXT', PFN_vkGetMemoryHostPointerPropertiesEXT)
PFN_vkCmdWriteBufferMarkerAMD = VK_FUNCTYPE(None, VkCommandBuffer, VkPipelineStageFlagBits, VkBuffer, VkDeviceSize, ctypes.c_uint32)
vkCmdWriteBufferMarkerAMD = vk_device_fn(b'vkCmdWriteBufferMarkerAMD', PFN_vkCmdWriteBufferMarkerAMD)
PFN_vkCreateRenderPass2 = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkRenderPassCreateInfo2), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkRenderPass))
vkCreateRenderPass2 = VK_DLL.vkCreateRenderPass2
vkCreateRenderPass2.restype = VkResult
vkCreateRenderPass2.argtypes = [VkDevice, ctypes.POINTER(VkRenderPassCreateInfo2), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkRenderPass)]
PFN_vkCreateRenderPass2KHR = PFN_vkCreateRenderPass2
vkCreateRenderPass2KHR = vkCreateRenderPass2
PFN_vkCmdBeginRenderPass2 = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.POINTER(VkSubpassBeginInfo))
vkCmdBeginRenderPass2 = VK_DLL.vkCmdBeginRenderPass2
vkCmdBeginRenderPass2.restype = None
vkCmdBeginRenderPass2.argtypes = [VkCommandBuffer, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.POINTER(VkSubpassBeginInfo)]
PFN_vkCmdBeginRenderPass2KHR = PFN_vkCmdBeginRenderPass2
vkCmdBeginRenderPass2KHR = vkCmdBeginRenderPass2
PFN_vkCmdNextSubpass2 = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkSubpassBeginInfo), ctypes.POINTER(VkSubpassEndInfo))
vkCmdNextSubpass2 = VK_DLL.vkCmdNextSubpass2
vkCmdNextSubpass2.restype = None
vkCmdNextSubpass2.argtypes = [VkCommandBuffer, ctypes.POINTER(VkSubpassBeginInfo), ctypes.POINTER(VkSubpassEndInfo)]
PFN_vkCmdNextSubpass2KHR = PFN_vkCmdNextSubpass2
vkCmdNextSubpass2KHR = vkCmdNextSubpass2
PFN_vkCmdEndRenderPass2 = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkSubpassEndInfo))
vkCmdEndRenderPass2 = VK_DLL.vkCmdEndRenderPass2
vkCmdEndRenderPass2.restype = None
vkCmdEndRenderPass2.argtypes = [VkCommandBuffer, ctypes.POINTER(VkSubpassEndInfo)]
PFN_vkCmdEndRenderPass2KHR = PFN_vkCmdEndRenderPass2
vkCmdEndRenderPass2KHR = vkCmdEndRenderPass2
PFN_vkGetSemaphoreCounterValue = VK_FUNCTYPE(VkResult, VkDevice, VkSemaphore, ctypes.POINTER(ctypes.c_uint64))
vkGetSemaphoreCounterValue = VK_DLL.vkGetSemaphoreCounterValue
vkGetSemaphoreCounterValue.restype = VkResult
vkGetSemaphoreCounterValue.argtypes = [VkDevice, VkSemaphore, ctypes.POINTER(ctypes.c_uint64)]
PFN_vkGetSemaphoreCounterValueKHR = PFN_vkGetSemaphoreCounterValue
vkGetSemaphoreCounterValueKHR = vkGetSemaphoreCounterValue
PFN_vkWaitSemaphores = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSemaphoreWaitInfo), ctypes.c_uint64)
vkWaitSemaphores = VK_DLL.vkWaitSemaphores
vkWaitSemaphores.restype = VkResult
vkWaitSemaphores.argtypes = [VkDevice, ctypes.POINTER(VkSemaphoreWaitInfo), ctypes.c_uint64]
PFN_vkWaitSemaphoresKHR = PFN_vkWaitSemaphores
vkWaitSemaphoresKHR = vkWaitSemaphores
PFN_vkSignalSemaphore = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkSemaphoreSignalInfo))
vkSignalSemaphore = VK_DLL.vkSignalSemaphore
vkSignalSemaphore.restype = VkResult
vkSignalSemaphore.argtypes = [VkDevice, ctypes.POINTER(VkSemaphoreSignalInfo)]
PFN_vkSignalSemaphoreKHR = PFN_vkSignalSemaphore
vkSignalSemaphoreKHR = vkSignalSemaphore
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkGetAndroidHardwareBufferPropertiesANDROID = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(AHardwareBuffer), ctypes.POINTER(VkAndroidHardwareBufferPropertiesANDROID))
    vkGetAndroidHardwareBufferPropertiesANDROID = vk_device_fn(b'vkGetAndroidHardwareBufferPropertiesANDROID', PFN_vkGetAndroidHardwareBufferPropertiesANDROID)
if VK_USE_PLATFORM_ANDROID_KHR:
    PFN_vkGetMemoryAndroidHardwareBufferANDROID = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkMemoryGetAndroidHardwareBufferInfoANDROID), ctypes.POINTER(ctypes.POINTER(AHardwareBuffer)))
    vkGetMemoryAndroidHardwareBufferANDROID = vk_device_fn(b'vkGetMemoryAndroidHardwareBufferANDROID', PFN_vkGetMemoryAndroidHardwareBufferANDROID)
PFN_vkCmdDrawIndirectCount = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirectCount = VK_DLL.vkCmdDrawIndirectCount
vkCmdDrawIndirectCount.restype = None
vkCmdDrawIndirectCount.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDrawIndirectCountKHR = PFN_vkCmdDrawIndirectCount
vkCmdDrawIndirectCountKHR = vkCmdDrawIndirectCount
PFN_vkCmdDrawIndirectCountAMD = PFN_vkCmdDrawIndirectCount
vkCmdDrawIndirectCountAMD = vkCmdDrawIndirectCount
PFN_vkCmdDrawIndexedIndirectCount = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndexedIndirectCount = VK_DLL.vkCmdDrawIndexedIndirectCount
vkCmdDrawIndexedIndirectCount.restype = None
vkCmdDrawIndexedIndirectCount.argtypes = [VkCommandBuffer, VkBuffer, VkDeviceSize, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32]
PFN_vkCmdDrawIndexedIndirectCountKHR = PFN_vkCmdDrawIndexedIndirectCount
vkCmdDrawIndexedIndirectCountKHR = vkCmdDrawIndexedIndirectCount
PFN_vkCmdDrawIndexedIndirectCountAMD = PFN_vkCmdDrawIndexedIndirectCount
vkCmdDrawIndexedIndirectCountAMD = vkCmdDrawIndexedIndirectCount
PFN_vkCmdSetCheckpointNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_void_p)
vkCmdSetCheckpointNV = vk_device_fn(b'vkCmdSetCheckpointNV', PFN_vkCmdSetCheckpointNV)
PFN_vkGetQueueCheckpointDataNV = VK_FUNCTYPE(None, VkQueue, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCheckpointDataNV))
vkGetQueueCheckpointDataNV = vk_device_fn(b'vkGetQueueCheckpointDataNV', PFN_vkGetQueueCheckpointDataNV)
PFN_vkCmdBindTransformFeedbackBuffersEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkBuffer), ctypes.POINTER(VkDeviceSize), ctypes.POINTER(VkDeviceSize))
vkCmdBindTransformFeedbackBuffersEXT = vk_device_fn(b'vkCmdBindTransformFeedbackBuffersEXT', PFN_vkCmdBindTransformFeedbackBuffersEXT)
PFN_vkCmdBeginTransformFeedbackEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkBuffer), ctypes.POINTER(VkDeviceSize))
vkCmdBeginTransformFeedbackEXT = vk_device_fn(b'vkCmdBeginTransformFeedbackEXT', PFN_vkCmdBeginTransformFeedbackEXT)
PFN_vkCmdEndTransformFeedbackEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkBuffer), ctypes.POINTER(VkDeviceSize))
vkCmdEndTransformFeedbackEXT = vk_device_fn(b'vkCmdEndTransformFeedbackEXT', PFN_vkCmdEndTransformFeedbackEXT)
PFN_vkCmdBeginQueryIndexedEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkQueryPool, ctypes.c_uint32, VkQueryControlFlags, ctypes.c_uint32)
vkCmdBeginQueryIndexedEXT = vk_device_fn(b'vkCmdBeginQueryIndexedEXT', PFN_vkCmdBeginQueryIndexedEXT)
PFN_vkCmdEndQueryIndexedEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkQueryPool, ctypes.c_uint32, ctypes.c_uint32)
vkCmdEndQueryIndexedEXT = vk_device_fn(b'vkCmdEndQueryIndexedEXT', PFN_vkCmdEndQueryIndexedEXT)
PFN_vkCmdDrawIndirectByteCountEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirectByteCountEXT = vk_device_fn(b'vkCmdDrawIndirectByteCountEXT', PFN_vkCmdDrawIndirectByteCountEXT)
PFN_vkCmdSetExclusiveScissorNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetExclusiveScissorNV = vk_device_fn(b'vkCmdSetExclusiveScissorNV', PFN_vkCmdSetExclusiveScissorNV)
PFN_vkCmdBindShadingRateImageNV = VK_FUNCTYPE(None, VkCommandBuffer, VkImageView, VkImageLayout)
vkCmdBindShadingRateImageNV = vk_device_fn(b'vkCmdBindShadingRateImageNV', PFN_vkCmdBindShadingRateImageNV)
PFN_vkCmdSetViewportShadingRatePaletteNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkShadingRatePaletteNV))
vkCmdSetViewportShadingRatePaletteNV = vk_device_fn(b'vkCmdSetViewportShadingRatePaletteNV', PFN_vkCmdSetViewportShadingRatePaletteNV)
PFN_vkCmdSetCoarseSampleOrderNV = VK_FUNCTYPE(None, VkCommandBuffer, VkCoarseSampleOrderTypeNV, ctypes.c_uint32, ctypes.POINTER(VkCoarseSampleOrderCustomNV))
vkCmdSetCoarseSampleOrderNV = vk_device_fn(b'vkCmdSetCoarseSampleOrderNV', PFN_vkCmdSetCoarseSampleOrderNV)
PFN_vkCmdDrawMeshTasksNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksNV = vk_device_fn(b'vkCmdDrawMeshTasksNV', PFN_vkCmdDrawMeshTasksNV)
PFN_vkCmdDrawMeshTasksIndirectNV = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectNV = vk_device_fn(b'vkCmdDrawMeshTasksIndirectNV', PFN_vkCmdDrawMeshTasksIndirectNV)
PFN_vkCmdDrawMeshTasksIndirectCountNV = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkBuffer, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectCountNV = vk_device_fn(b'vkCmdDrawMeshTasksIndirectCountNV', PFN_vkCmdDrawMeshTasksIndirectCountNV)
PFN_vkCompileDeferredNV = VK_FUNCTYPE(VkResult, VkDevice, VkPipeline, ctypes.c_uint32)
vkCompileDeferredNV = vk_device_fn(b'vkCompileDeferredNV', PFN_vkCompileDeferredNV)
PFN_vkCreateAccelerationStructureNV = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkAccelerationStructureCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkAccelerationStructureNV))
vkCreateAccelerationStructureNV = vk_device_fn(b'vkCreateAccelerationStructureNV', PFN_vkCreateAccelerationStructureNV)
PFN_vkDestroyAccelerationStructureKHR = VK_FUNCTYPE(None, VkDevice, VkAccelerationStructureKHR, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyAccelerationStructureKHR = vk_device_fn(b'vkDestroyAccelerationStructureKHR', PFN_vkDestroyAccelerationStructureKHR)
PFN_vkDestroyAccelerationStructureNV = VK_FUNCTYPE(None, VkDevice, VkAccelerationStructureNV, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyAccelerationStructureNV = vk_device_fn(b'vkDestroyAccelerationStructureNV', PFN_vkDestroyAccelerationStructureNV)
PFN_vkGetAccelerationStructureMemoryRequirementsNV = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkAccelerationStructureMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2KHR))
vkGetAccelerationStructureMemoryRequirementsNV = vk_device_fn(b'vkGetAccelerationStructureMemoryRequirementsNV', PFN_vkGetAccelerationStructureMemoryRequirementsNV)
PFN_vkBindAccelerationStructureMemoryNV = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkBindAccelerationStructureMemoryInfoNV))
vkBindAccelerationStructureMemoryNV = vk_device_fn(b'vkBindAccelerationStructureMemoryNV', PFN_vkBindAccelerationStructureMemoryNV)
PFN_vkCmdCopyAccelerationStructureNV = VK_FUNCTYPE(None, VkCommandBuffer, VkAccelerationStructureNV, VkAccelerationStructureNV, VkCopyAccelerationStructureModeKHR)
vkCmdCopyAccelerationStructureNV = vk_device_fn(b'vkCmdCopyAccelerationStructureNV', PFN_vkCmdCopyAccelerationStructureNV)
PFN_vkCmdCopyAccelerationStructureKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
vkCmdCopyAccelerationStructureKHR = vk_device_fn(b'vkCmdCopyAccelerationStructureKHR', PFN_vkCmdCopyAccelerationStructureKHR)
PFN_vkCopyAccelerationStructureKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
vkCopyAccelerationStructureKHR = vk_device_fn(b'vkCopyAccelerationStructureKHR', PFN_vkCopyAccelerationStructureKHR)
PFN_vkCmdCopyAccelerationStructureToMemoryKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyAccelerationStructureToMemoryInfoKHR))
vkCmdCopyAccelerationStructureToMemoryKHR = vk_device_fn(b'vkCmdCopyAccelerationStructureToMemoryKHR', PFN_vkCmdCopyAccelerationStructureToMemoryKHR)
PFN_vkCopyAccelerationStructureToMemoryKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR, ctypes.POINTER(VkCopyAccelerationStructureToMemoryInfoKHR))
vkCopyAccelerationStructureToMemoryKHR = vk_device_fn(b'vkCopyAccelerationStructureToMemoryKHR', PFN_vkCopyAccelerationStructureToMemoryKHR)
PFN_vkCmdCopyMemoryToAccelerationStructureKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
vkCmdCopyMemoryToAccelerationStructureKHR = vk_device_fn(b'vkCmdCopyMemoryToAccelerationStructureKHR', PFN_vkCmdCopyMemoryToAccelerationStructureKHR)
PFN_vkCopyMemoryToAccelerationStructureKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
vkCopyMemoryToAccelerationStructureKHR = vk_device_fn(b'vkCopyMemoryToAccelerationStructureKHR', PFN_vkCopyMemoryToAccelerationStructureKHR)
PFN_vkCmdWriteAccelerationStructuresPropertiesKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureKHR), VkQueryType, VkQueryPool, ctypes.c_uint32)
vkCmdWriteAccelerationStructuresPropertiesKHR = vk_device_fn(b'vkCmdWriteAccelerationStructuresPropertiesKHR', PFN_vkCmdWriteAccelerationStructuresPropertiesKHR)
PFN_vkCmdWriteAccelerationStructuresPropertiesNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureNV), VkQueryType, VkQueryPool, ctypes.c_uint32)
vkCmdWriteAccelerationStructuresPropertiesNV = vk_device_fn(b'vkCmdWriteAccelerationStructuresPropertiesNV', PFN_vkCmdWriteAccelerationStructuresPropertiesNV)
PFN_vkCmdBuildAccelerationStructureNV = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkAccelerationStructureInfoNV), VkBuffer, VkDeviceSize, VkBool32, VkAccelerationStructureNV, VkAccelerationStructureNV, VkBuffer, VkDeviceSize)
vkCmdBuildAccelerationStructureNV = vk_device_fn(b'vkCmdBuildAccelerationStructureNV', PFN_vkCmdBuildAccelerationStructureNV)
PFN_vkWriteAccelerationStructuresPropertiesKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureKHR), VkQueryType, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)
vkWriteAccelerationStructuresPropertiesKHR = vk_device_fn(b'vkWriteAccelerationStructuresPropertiesKHR', PFN_vkWriteAccelerationStructuresPropertiesKHR)
PFN_vkCmdTraceRaysKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdTraceRaysKHR = vk_device_fn(b'vkCmdTraceRaysKHR', PFN_vkCmdTraceRaysKHR)
PFN_vkCmdTraceRaysNV = VK_FUNCTYPE(None, VkCommandBuffer, VkBuffer, VkDeviceSize, VkBuffer, VkDeviceSize, VkDeviceSize, VkBuffer, VkDeviceSize, VkDeviceSize, VkBuffer, VkDeviceSize, VkDeviceSize, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdTraceRaysNV = vk_device_fn(b'vkCmdTraceRaysNV', PFN_vkCmdTraceRaysNV)
PFN_vkGetRayTracingShaderGroupHandlesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkPipeline, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p)
vkGetRayTracingShaderGroupHandlesKHR = vk_device_fn(b'vkGetRayTracingShaderGroupHandlesKHR', PFN_vkGetRayTracingShaderGroupHandlesKHR)
PFN_vkGetRayTracingShaderGroupHandlesNV = PFN_vkGetRayTracingShaderGroupHandlesKHR
vkGetRayTracingShaderGroupHandlesNV = vkGetRayTracingShaderGroupHandlesKHR
PFN_vkGetRayTracingCaptureReplayShaderGroupHandlesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkPipeline, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p)
vkGetRayTracingCaptureReplayShaderGroupHandlesKHR = vk_device_fn(b'vkGetRayTracingCaptureReplayShaderGroupHandlesKHR', PFN_vkGetRayTracingCaptureReplayShaderGroupHandlesKHR)
PFN_vkGetAccelerationStructureHandleNV = VK_FUNCTYPE(VkResult, VkDevice, VkAccelerationStructureNV, ctypes.c_size_t, ctypes.c_void_p)
vkGetAccelerationStructureHandleNV = vk_device_fn(b'vkGetAccelerationStructureHandleNV', PFN_vkGetAccelerationStructureHandleNV)
PFN_vkCreateRayTracingPipelinesNV = VK_FUNCTYPE(VkResult, VkDevice, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipeline))
vkCreateRayTracingPipelinesNV = vk_device_fn(b'vkCreateRayTracingPipelinesNV', PFN_vkCreateRayTracingPipelinesNV)
PFN_vkCreateRayTracingPipelinesKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR, VkPipelineCache, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPipeline))
vkCreateRayTracingPipelinesKHR = vk_device_fn(b'vkCreateRayTracingPipelinesKHR', PFN_vkCreateRayTracingPipelinesKHR)
PFN_vkGetPhysicalDeviceCooperativeMatrixPropertiesNV = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCooperativeMatrixPropertiesNV))
vkGetPhysicalDeviceCooperativeMatrixPropertiesNV = vk_device_fn(b'vkGetPhysicalDeviceCooperativeMatrixPropertiesNV', PFN_vkGetPhysicalDeviceCooperativeMatrixPropertiesNV)
PFN_vkCmdTraceRaysIndirectKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), VkDeviceAddress)
vkCmdTraceRaysIndirectKHR = vk_device_fn(b'vkCmdTraceRaysIndirectKHR', PFN_vkCmdTraceRaysIndirectKHR)
PFN_vkGetDeviceAccelerationStructureCompatibilityKHR = VK_FUNCTYPE(None, VkDevice, ctypes.POINTER(VkAccelerationStructureVersionInfoKHR), ctypes.POINTER(VkAccelerationStructureCompatibilityKHR))
vkGetDeviceAccelerationStructureCompatibilityKHR = vk_device_fn(b'vkGetDeviceAccelerationStructureCompatibilityKHR', PFN_vkGetDeviceAccelerationStructureCompatibilityKHR)
PFN_vkGetRayTracingShaderGroupStackSizeKHR = VK_FUNCTYPE(VkDeviceSize, VkDevice, VkPipeline, ctypes.c_uint32, VkShaderGroupShaderKHR)
vkGetRayTracingShaderGroupStackSizeKHR = vk_device_fn(b'vkGetRayTracingShaderGroupStackSizeKHR', PFN_vkGetRayTracingShaderGroupStackSizeKHR)
PFN_vkCmdSetRayTracingPipelineStackSizeKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32)
vkCmdSetRayTracingPipelineStackSizeKHR = vk_device_fn(b'vkCmdSetRayTracingPipelineStackSizeKHR', PFN_vkCmdSetRayTracingPipelineStackSizeKHR)
PFN_vkGetImageViewHandleNVX = VK_FUNCTYPE(ctypes.c_uint32, VkDevice, ctypes.POINTER(VkImageViewHandleInfoNVX))
vkGetImageViewHandleNVX = vk_device_fn(b'vkGetImageViewHandleNVX', PFN_vkGetImageViewHandleNVX)
PFN_vkGetImageViewAddressNVX = VK_FUNCTYPE(VkResult, VkDevice, VkImageView, ctypes.POINTER(VkImageViewAddressPropertiesNVX))
vkGetImageViewAddressNVX = vk_device_fn(b'vkGetImageViewAddressNVX', PFN_vkGetImageViewAddressNVX)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetPhysicalDeviceSurfacePresentModes2EXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPresentModeKHR))
    vkGetPhysicalDeviceSurfacePresentModes2EXT = vk_device_fn(b'vkGetPhysicalDeviceSurfacePresentModes2EXT', PFN_vkGetPhysicalDeviceSurfacePresentModes2EXT)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkGetDeviceGroupSurfacePresentModes2EXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(VkDeviceGroupPresentModeFlagsKHR))
    vkGetDeviceGroupSurfacePresentModes2EXT = vk_device_fn(b'vkGetDeviceGroupSurfacePresentModes2EXT', PFN_vkGetDeviceGroupSurfacePresentModes2EXT)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkAcquireFullScreenExclusiveModeEXT = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR)
    vkAcquireFullScreenExclusiveModeEXT = vk_device_fn(b'vkAcquireFullScreenExclusiveModeEXT', PFN_vkAcquireFullScreenExclusiveModeEXT)
if VK_USE_PLATFORM_WIN32_KHR:
    PFN_vkReleaseFullScreenExclusiveModeEXT = VK_FUNCTYPE(VkResult, VkDevice, VkSwapchainKHR)
    vkReleaseFullScreenExclusiveModeEXT = vk_device_fn(b'vkReleaseFullScreenExclusiveModeEXT', PFN_vkReleaseFullScreenExclusiveModeEXT)
PFN_vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPerformanceCounterKHR), ctypes.POINTER(VkPerformanceCounterDescriptionKHR))
vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR = vk_device_fn(b'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR', PFN_vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR)
PFN_vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR = VK_FUNCTYPE(None, VkPhysicalDevice, ctypes.POINTER(VkQueryPoolPerformanceCreateInfoKHR), ctypes.POINTER(ctypes.c_uint32))
vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR = vk_device_fn(b'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR', PFN_vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR)
PFN_vkAcquireProfilingLockKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkAcquireProfilingLockInfoKHR))
vkAcquireProfilingLockKHR = vk_device_fn(b'vkAcquireProfilingLockKHR', PFN_vkAcquireProfilingLockKHR)
PFN_vkReleaseProfilingLockKHR = VK_FUNCTYPE(None, VkDevice)
vkReleaseProfilingLockKHR = vk_device_fn(b'vkReleaseProfilingLockKHR', PFN_vkReleaseProfilingLockKHR)
PFN_vkGetImageDrmFormatModifierPropertiesEXT = VK_FUNCTYPE(VkResult, VkDevice, VkImage, ctypes.POINTER(VkImageDrmFormatModifierPropertiesEXT))
vkGetImageDrmFormatModifierPropertiesEXT = vk_device_fn(b'vkGetImageDrmFormatModifierPropertiesEXT', PFN_vkGetImageDrmFormatModifierPropertiesEXT)
PFN_vkGetBufferOpaqueCaptureAddress = VK_FUNCTYPE(ctypes.c_uint64, VkDevice, ctypes.POINTER(VkBufferDeviceAddressInfo))
vkGetBufferOpaqueCaptureAddress = VK_DLL.vkGetBufferOpaqueCaptureAddress
vkGetBufferOpaqueCaptureAddress.restype = ctypes.c_uint64
vkGetBufferOpaqueCaptureAddress.argtypes = [VkDevice, ctypes.POINTER(VkBufferDeviceAddressInfo)]
PFN_vkGetBufferOpaqueCaptureAddressKHR = PFN_vkGetBufferOpaqueCaptureAddress
vkGetBufferOpaqueCaptureAddressKHR = vkGetBufferOpaqueCaptureAddress
PFN_vkGetBufferDeviceAddress = VK_FUNCTYPE(VkDeviceAddress, VkDevice, ctypes.POINTER(VkBufferDeviceAddressInfo))
vkGetBufferDeviceAddress = VK_DLL.vkGetBufferDeviceAddress
vkGetBufferDeviceAddress.restype = VkDeviceAddress
vkGetBufferDeviceAddress.argtypes = [VkDevice, ctypes.POINTER(VkBufferDeviceAddressInfo)]
PFN_vkGetBufferDeviceAddressKHR = PFN_vkGetBufferDeviceAddress
vkGetBufferDeviceAddressKHR = vkGetBufferDeviceAddress
PFN_vkGetBufferDeviceAddressEXT = PFN_vkGetBufferDeviceAddress
vkGetBufferDeviceAddressEXT = vkGetBufferDeviceAddress
PFN_vkCreateHeadlessSurfaceEXT = VK_FUNCTYPE(VkResult, VkInstance, ctypes.POINTER(VkHeadlessSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
vkCreateHeadlessSurfaceEXT = vk_instance_fn(b'vkCreateHeadlessSurfaceEXT', PFN_vkCreateHeadlessSurfaceEXT)
PFN_vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkFramebufferMixedSamplesCombinationNV))
vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV = vk_device_fn(b'vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV', PFN_vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV)
PFN_vkInitializePerformanceApiINTEL = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkInitializePerformanceApiInfoINTEL))
vkInitializePerformanceApiINTEL = vk_device_fn(b'vkInitializePerformanceApiINTEL', PFN_vkInitializePerformanceApiINTEL)
PFN_vkUninitializePerformanceApiINTEL = VK_FUNCTYPE(None, VkDevice)
vkUninitializePerformanceApiINTEL = vk_device_fn(b'vkUninitializePerformanceApiINTEL', PFN_vkUninitializePerformanceApiINTEL)
PFN_vkCmdSetPerformanceMarkerINTEL = VK_FUNCTYPE(VkResult, VkCommandBuffer, ctypes.POINTER(VkPerformanceMarkerInfoINTEL))
vkCmdSetPerformanceMarkerINTEL = vk_device_fn(b'vkCmdSetPerformanceMarkerINTEL', PFN_vkCmdSetPerformanceMarkerINTEL)
PFN_vkCmdSetPerformanceStreamMarkerINTEL = VK_FUNCTYPE(VkResult, VkCommandBuffer, ctypes.POINTER(VkPerformanceStreamMarkerInfoINTEL))
vkCmdSetPerformanceStreamMarkerINTEL = vk_device_fn(b'vkCmdSetPerformanceStreamMarkerINTEL', PFN_vkCmdSetPerformanceStreamMarkerINTEL)
PFN_vkCmdSetPerformanceOverrideINTEL = VK_FUNCTYPE(VkResult, VkCommandBuffer, ctypes.POINTER(VkPerformanceOverrideInfoINTEL))
vkCmdSetPerformanceOverrideINTEL = vk_device_fn(b'vkCmdSetPerformanceOverrideINTEL', PFN_vkCmdSetPerformanceOverrideINTEL)
PFN_vkAcquirePerformanceConfigurationINTEL = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPerformanceConfigurationAcquireInfoINTEL), ctypes.POINTER(VkPerformanceConfigurationINTEL))
vkAcquirePerformanceConfigurationINTEL = vk_device_fn(b'vkAcquirePerformanceConfigurationINTEL', PFN_vkAcquirePerformanceConfigurationINTEL)
PFN_vkReleasePerformanceConfigurationINTEL = VK_FUNCTYPE(VkResult, VkDevice, VkPerformanceConfigurationINTEL)
vkReleasePerformanceConfigurationINTEL = vk_device_fn(b'vkReleasePerformanceConfigurationINTEL', PFN_vkReleasePerformanceConfigurationINTEL)
PFN_vkQueueSetPerformanceConfigurationINTEL = VK_FUNCTYPE(VkResult, VkQueue, VkPerformanceConfigurationINTEL)
vkQueueSetPerformanceConfigurationINTEL = vk_device_fn(b'vkQueueSetPerformanceConfigurationINTEL', PFN_vkQueueSetPerformanceConfigurationINTEL)
PFN_vkGetPerformanceParameterINTEL = VK_FUNCTYPE(VkResult, VkDevice, VkPerformanceParameterTypeINTEL, ctypes.POINTER(VkPerformanceValueINTEL))
vkGetPerformanceParameterINTEL = vk_device_fn(b'vkGetPerformanceParameterINTEL', PFN_vkGetPerformanceParameterINTEL)
PFN_vkGetDeviceMemoryOpaqueCaptureAddress = VK_FUNCTYPE(ctypes.c_uint64, VkDevice, ctypes.POINTER(VkDeviceMemoryOpaqueCaptureAddressInfo))
vkGetDeviceMemoryOpaqueCaptureAddress = VK_DLL.vkGetDeviceMemoryOpaqueCaptureAddress
vkGetDeviceMemoryOpaqueCaptureAddress.restype = ctypes.c_uint64
vkGetDeviceMemoryOpaqueCaptureAddress.argtypes = [VkDevice, ctypes.POINTER(VkDeviceMemoryOpaqueCaptureAddressInfo)]
PFN_vkGetDeviceMemoryOpaqueCaptureAddressKHR = PFN_vkGetDeviceMemoryOpaqueCaptureAddress
vkGetDeviceMemoryOpaqueCaptureAddressKHR = vkGetDeviceMemoryOpaqueCaptureAddress
PFN_vkGetPipelineExecutablePropertiesKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPipelineInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutablePropertiesKHR))
vkGetPipelineExecutablePropertiesKHR = vk_device_fn(b'vkGetPipelineExecutablePropertiesKHR', PFN_vkGetPipelineExecutablePropertiesKHR)
PFN_vkGetPipelineExecutableStatisticsKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableStatisticKHR))
vkGetPipelineExecutableStatisticsKHR = vk_device_fn(b'vkGetPipelineExecutableStatisticsKHR', PFN_vkGetPipelineExecutableStatisticsKHR)
PFN_vkGetPipelineExecutableInternalRepresentationsKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableInternalRepresentationKHR))
vkGetPipelineExecutableInternalRepresentationsKHR = vk_device_fn(b'vkGetPipelineExecutableInternalRepresentationsKHR', PFN_vkGetPipelineExecutableInternalRepresentationsKHR)
PFN_vkCmdSetLineStippleEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint16)
vkCmdSetLineStippleEXT = vk_device_fn(b'vkCmdSetLineStippleEXT', PFN_vkCmdSetLineStippleEXT)
PFN_vkGetPhysicalDeviceToolPropertiesEXT = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceToolPropertiesEXT))
vkGetPhysicalDeviceToolPropertiesEXT = vk_device_fn(b'vkGetPhysicalDeviceToolPropertiesEXT', PFN_vkGetPhysicalDeviceToolPropertiesEXT)
PFN_vkCreateAccelerationStructureKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkAccelerationStructureCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkAccelerationStructureKHR))
vkCreateAccelerationStructureKHR = vk_device_fn(b'vkCreateAccelerationStructureKHR', PFN_vkCreateAccelerationStructureKHR)
PFN_vkCmdBuildAccelerationStructuresKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
vkCmdBuildAccelerationStructuresKHR = vk_device_fn(b'vkCmdBuildAccelerationStructuresKHR', PFN_vkCmdBuildAccelerationStructuresKHR)
PFN_vkCmdBuildAccelerationStructuresIndirectKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(VkDeviceAddress), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint32)))
vkCmdBuildAccelerationStructuresIndirectKHR = vk_device_fn(b'vkCmdBuildAccelerationStructuresIndirectKHR', PFN_vkCmdBuildAccelerationStructuresIndirectKHR)
PFN_vkBuildAccelerationStructuresKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
vkBuildAccelerationStructuresKHR = vk_device_fn(b'vkBuildAccelerationStructuresKHR', PFN_vkBuildAccelerationStructuresKHR)
PFN_vkGetAccelerationStructureDeviceAddressKHR = VK_FUNCTYPE(VkDeviceAddress, VkDevice, ctypes.POINTER(VkAccelerationStructureDeviceAddressInfoKHR))
vkGetAccelerationStructureDeviceAddressKHR = vk_device_fn(b'vkGetAccelerationStructureDeviceAddressKHR', PFN_vkGetAccelerationStructureDeviceAddressKHR)
PFN_vkCreateDeferredOperationKHR = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkDeferredOperationKHR))
vkCreateDeferredOperationKHR = vk_device_fn(b'vkCreateDeferredOperationKHR', PFN_vkCreateDeferredOperationKHR)
PFN_vkDestroyDeferredOperationKHR = VK_FUNCTYPE(None, VkDevice, VkDeferredOperationKHR, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDeferredOperationKHR = vk_device_fn(b'vkDestroyDeferredOperationKHR', PFN_vkDestroyDeferredOperationKHR)
PFN_vkGetDeferredOperationMaxConcurrencyKHR = VK_FUNCTYPE(ctypes.c_uint32, VkDevice, VkDeferredOperationKHR)
vkGetDeferredOperationMaxConcurrencyKHR = vk_device_fn(b'vkGetDeferredOperationMaxConcurrencyKHR', PFN_vkGetDeferredOperationMaxConcurrencyKHR)
PFN_vkGetDeferredOperationResultKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR)
vkGetDeferredOperationResultKHR = vk_device_fn(b'vkGetDeferredOperationResultKHR', PFN_vkGetDeferredOperationResultKHR)
PFN_vkDeferredOperationJoinKHR = VK_FUNCTYPE(VkResult, VkDevice, VkDeferredOperationKHR)
vkDeferredOperationJoinKHR = vk_device_fn(b'vkDeferredOperationJoinKHR', PFN_vkDeferredOperationJoinKHR)
PFN_vkCmdSetCullModeEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkCullModeFlags)
vkCmdSetCullModeEXT = vk_device_fn(b'vkCmdSetCullModeEXT', PFN_vkCmdSetCullModeEXT)
PFN_vkCmdSetFrontFaceEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkFrontFace)
vkCmdSetFrontFaceEXT = vk_device_fn(b'vkCmdSetFrontFaceEXT', PFN_vkCmdSetFrontFaceEXT)
PFN_vkCmdSetPrimitiveTopologyEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkPrimitiveTopology)
vkCmdSetPrimitiveTopologyEXT = vk_device_fn(b'vkCmdSetPrimitiveTopologyEXT', PFN_vkCmdSetPrimitiveTopologyEXT)
PFN_vkCmdSetViewportWithCountEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkViewport))
vkCmdSetViewportWithCountEXT = vk_device_fn(b'vkCmdSetViewportWithCountEXT', PFN_vkCmdSetViewportWithCountEXT)
PFN_vkCmdSetScissorWithCountEXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetScissorWithCountEXT = vk_device_fn(b'vkCmdSetScissorWithCountEXT', PFN_vkCmdSetScissorWithCountEXT)
PFN_vkCmdBindVertexBuffers2EXT = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkBuffer), ctypes.POINTER(VkDeviceSize), ctypes.POINTER(VkDeviceSize), ctypes.POINTER(VkDeviceSize))
vkCmdBindVertexBuffers2EXT = vk_device_fn(b'vkCmdBindVertexBuffers2EXT', PFN_vkCmdBindVertexBuffers2EXT)
PFN_vkCmdSetDepthTestEnableEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkBool32)
vkCmdSetDepthTestEnableEXT = vk_device_fn(b'vkCmdSetDepthTestEnableEXT', PFN_vkCmdSetDepthTestEnableEXT)
PFN_vkCmdSetDepthWriteEnableEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkBool32)
vkCmdSetDepthWriteEnableEXT = vk_device_fn(b'vkCmdSetDepthWriteEnableEXT', PFN_vkCmdSetDepthWriteEnableEXT)
PFN_vkCmdSetDepthCompareOpEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkCompareOp)
vkCmdSetDepthCompareOpEXT = vk_device_fn(b'vkCmdSetDepthCompareOpEXT', PFN_vkCmdSetDepthCompareOpEXT)
PFN_vkCmdSetDepthBoundsTestEnableEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkBool32)
vkCmdSetDepthBoundsTestEnableEXT = vk_device_fn(b'vkCmdSetDepthBoundsTestEnableEXT', PFN_vkCmdSetDepthBoundsTestEnableEXT)
PFN_vkCmdSetStencilTestEnableEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkBool32)
vkCmdSetStencilTestEnableEXT = vk_device_fn(b'vkCmdSetStencilTestEnableEXT', PFN_vkCmdSetStencilTestEnableEXT)
PFN_vkCmdSetStencilOpEXT = VK_FUNCTYPE(None, VkCommandBuffer, VkStencilFaceFlags, VkStencilOp, VkStencilOp, VkStencilOp, VkCompareOp)
vkCmdSetStencilOpEXT = vk_device_fn(b'vkCmdSetStencilOpEXT', PFN_vkCmdSetStencilOpEXT)
PFN_vkCreatePrivateDataSlotEXT = VK_FUNCTYPE(VkResult, VkDevice, ctypes.POINTER(VkPrivateDataSlotCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkPrivateDataSlotEXT))
vkCreatePrivateDataSlotEXT = vk_device_fn(b'vkCreatePrivateDataSlotEXT', PFN_vkCreatePrivateDataSlotEXT)
PFN_vkDestroyPrivateDataSlotEXT = VK_FUNCTYPE(None, VkDevice, VkPrivateDataSlotEXT, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPrivateDataSlotEXT = vk_device_fn(b'vkDestroyPrivateDataSlotEXT', PFN_vkDestroyPrivateDataSlotEXT)
PFN_vkSetPrivateDataEXT = VK_FUNCTYPE(VkResult, VkDevice, VkObjectType, ctypes.c_uint64, VkPrivateDataSlotEXT, ctypes.c_uint64)
vkSetPrivateDataEXT = vk_device_fn(b'vkSetPrivateDataEXT', PFN_vkSetPrivateDataEXT)
PFN_vkGetPrivateDataEXT = VK_FUNCTYPE(None, VkDevice, VkObjectType, ctypes.c_uint64, VkPrivateDataSlotEXT, ctypes.POINTER(ctypes.c_uint64))
vkGetPrivateDataEXT = vk_device_fn(b'vkGetPrivateDataEXT', PFN_vkGetPrivateDataEXT)
PFN_vkCmdCopyBuffer2KHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyBufferInfo2KHR))
vkCmdCopyBuffer2KHR = vk_device_fn(b'vkCmdCopyBuffer2KHR', PFN_vkCmdCopyBuffer2KHR)
PFN_vkCmdCopyImage2KHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyImageInfo2KHR))
vkCmdCopyImage2KHR = vk_device_fn(b'vkCmdCopyImage2KHR', PFN_vkCmdCopyImage2KHR)
PFN_vkCmdBlitImage2KHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkBlitImageInfo2KHR))
vkCmdBlitImage2KHR = vk_device_fn(b'vkCmdBlitImage2KHR', PFN_vkCmdBlitImage2KHR)
PFN_vkCmdCopyBufferToImage2KHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyBufferToImageInfo2KHR))
vkCmdCopyBufferToImage2KHR = vk_device_fn(b'vkCmdCopyBufferToImage2KHR', PFN_vkCmdCopyBufferToImage2KHR)
PFN_vkCmdCopyImageToBuffer2KHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkCopyImageToBufferInfo2KHR))
vkCmdCopyImageToBuffer2KHR = vk_device_fn(b'vkCmdCopyImageToBuffer2KHR', PFN_vkCmdCopyImageToBuffer2KHR)
PFN_vkCmdResolveImage2KHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkResolveImageInfo2KHR))
vkCmdResolveImage2KHR = vk_device_fn(b'vkCmdResolveImage2KHR', PFN_vkCmdResolveImage2KHR)
PFN_vkCmdSetFragmentShadingRateKHR = VK_FUNCTYPE(None, VkCommandBuffer, ctypes.POINTER(VkExtent2D), (VkFragmentShadingRateCombinerOpKHR * (2)))
vkCmdSetFragmentShadingRateKHR = vk_device_fn(b'vkCmdSetFragmentShadingRateKHR', PFN_vkCmdSetFragmentShadingRateKHR)
PFN_vkGetPhysicalDeviceFragmentShadingRatesKHR = VK_FUNCTYPE(VkResult, VkPhysicalDevice, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceFragmentShadingRateKHR))
vkGetPhysicalDeviceFragmentShadingRatesKHR = vk_device_fn(b'vkGetPhysicalDeviceFragmentShadingRatesKHR', PFN_vkGetPhysicalDeviceFragmentShadingRatesKHR)
PFN_vkCmdSetFragmentShadingRateEnumNV = VK_FUNCTYPE(None, VkCommandBuffer, VkFragmentShadingRateNV, (VkFragmentShadingRateCombinerOpKHR * (2)))
vkCmdSetFragmentShadingRateEnumNV = vk_device_fn(b'vkCmdSetFragmentShadingRateEnumNV', PFN_vkCmdSetFragmentShadingRateEnumNV)
PFN_vkGetAccelerationStructureBuildSizesKHR = VK_FUNCTYPE(None, VkDevice, VkAccelerationStructureBuildTypeKHR, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkAccelerationStructureBuildSizesInfoKHR))
vkGetAccelerationStructureBuildSizesKHR = vk_device_fn(b'vkGetAccelerationStructureBuildSizesKHR', PFN_vkGetAccelerationStructureBuildSizesKHR)

