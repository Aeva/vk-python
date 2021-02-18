

import ctypes
import platform


if ctypes.sizeof(ctypes.c_void_p) != 8:
    raise RuntimeError("Only 64 bit is supported.")


VK_DLL = None
VK_FUNCTYPE = None
if platform.system() == "Windows":
    VK_DLL = ctypes.windll.LoadLibrary("vulkan-1")
    VK_FUNCTYPE = ctypes.WINFUNCTYPE
elif platform.system() == "Linux":
    VK_DLL = ctypes.cdll.LoadLibrary("libvulkan.so.1")
    VK_FUNCTYPE = ctypes.CFUNCTYPE
else:
    raise RuntimeError(f"Unsupported platform: {platform.system()}")


# BASE TYPES
VkSampleMask = type('VkSampleMask', (ctypes.c_uint32,), dict())
VkBool32 = type('VkBool32', (ctypes.c_uint32,), dict())
VkFlags = type('VkFlags', (ctypes.c_uint32,), dict())
VkDeviceSize = type('VkDeviceSize', (ctypes.c_uint64,), dict())
VkDeviceAddress = type('VkDeviceAddress', (ctypes.c_uint64,), dict())


# BITMASK TYPES
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
VkGeometryFlagsNV = type('VkGeometryFlagsNV', (VkGeometryFlagsKHR,), dict())
VkGeometryInstanceFlagsKHR = type('VkGeometryInstanceFlagsKHR', (VkFlags,), dict())
VkGeometryInstanceFlagsNV = type('VkGeometryInstanceFlagsNV', (VkGeometryInstanceFlagsKHR,), dict())
VkBuildAccelerationStructureFlagsKHR = type('VkBuildAccelerationStructureFlagsKHR', (VkFlags,), dict())
VkBuildAccelerationStructureFlagsNV = type('VkBuildAccelerationStructureFlagsNV', (VkBuildAccelerationStructureFlagsKHR,), dict())
VkPrivateDataSlotCreateFlagsEXT = type('VkPrivateDataSlotCreateFlagsEXT', (VkFlags,), dict())
VkAccelerationStructureCreateFlagsKHR = type('VkAccelerationStructureCreateFlagsKHR', (VkFlags,), dict())
VkDescriptorUpdateTemplateCreateFlags = type('VkDescriptorUpdateTemplateCreateFlags', (VkFlags,), dict())
VkDescriptorUpdateTemplateCreateFlagsKHR = type('VkDescriptorUpdateTemplateCreateFlagsKHR', (VkDescriptorUpdateTemplateCreateFlags,), dict())
VkPipelineCreationFeedbackFlagsEXT = type('VkPipelineCreationFeedbackFlagsEXT', (VkFlags,), dict())
VkPerformanceCounterDescriptionFlagsKHR = type('VkPerformanceCounterDescriptionFlagsKHR', (VkFlags,), dict())
VkAcquireProfilingLockFlagsKHR = type('VkAcquireProfilingLockFlagsKHR', (VkFlags,), dict())
VkSemaphoreWaitFlags = type('VkSemaphoreWaitFlags', (VkFlags,), dict())
VkSemaphoreWaitFlagsKHR = type('VkSemaphoreWaitFlagsKHR', (VkSemaphoreWaitFlags,), dict())
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
VkPeerMemoryFeatureFlagsKHR = type('VkPeerMemoryFeatureFlagsKHR', (VkPeerMemoryFeatureFlags,), dict())
VkMemoryAllocateFlags = type('VkMemoryAllocateFlags', (VkFlags,), dict())
VkMemoryAllocateFlagsKHR = type('VkMemoryAllocateFlagsKHR', (VkMemoryAllocateFlags,), dict())
VkDeviceGroupPresentModeFlagsKHR = type('VkDeviceGroupPresentModeFlagsKHR', (VkFlags,), dict())
VkDebugReportFlagsEXT = type('VkDebugReportFlagsEXT', (VkFlags,), dict())
VkCommandPoolTrimFlags = type('VkCommandPoolTrimFlags', (VkFlags,), dict())
VkCommandPoolTrimFlagsKHR = type('VkCommandPoolTrimFlagsKHR', (VkCommandPoolTrimFlags,), dict())
VkExternalMemoryHandleTypeFlagsNV = type('VkExternalMemoryHandleTypeFlagsNV', (VkFlags,), dict())
VkExternalMemoryFeatureFlagsNV = type('VkExternalMemoryFeatureFlagsNV', (VkFlags,), dict())
VkExternalMemoryHandleTypeFlags = type('VkExternalMemoryHandleTypeFlags', (VkFlags,), dict())
VkExternalMemoryHandleTypeFlagsKHR = type('VkExternalMemoryHandleTypeFlagsKHR', (VkExternalMemoryHandleTypeFlags,), dict())
VkExternalMemoryFeatureFlags = type('VkExternalMemoryFeatureFlags', (VkFlags,), dict())
VkExternalMemoryFeatureFlagsKHR = type('VkExternalMemoryFeatureFlagsKHR', (VkExternalMemoryFeatureFlags,), dict())
VkExternalSemaphoreHandleTypeFlags = type('VkExternalSemaphoreHandleTypeFlags', (VkFlags,), dict())
VkExternalSemaphoreHandleTypeFlagsKHR = type('VkExternalSemaphoreHandleTypeFlagsKHR', (VkExternalSemaphoreHandleTypeFlags,), dict())
VkExternalSemaphoreFeatureFlags = type('VkExternalSemaphoreFeatureFlags', (VkFlags,), dict())
VkExternalSemaphoreFeatureFlagsKHR = type('VkExternalSemaphoreFeatureFlagsKHR', (VkExternalSemaphoreFeatureFlags,), dict())
VkSemaphoreImportFlags = type('VkSemaphoreImportFlags', (VkFlags,), dict())
VkSemaphoreImportFlagsKHR = type('VkSemaphoreImportFlagsKHR', (VkSemaphoreImportFlags,), dict())
VkExternalFenceHandleTypeFlags = type('VkExternalFenceHandleTypeFlags', (VkFlags,), dict())
VkExternalFenceHandleTypeFlagsKHR = type('VkExternalFenceHandleTypeFlagsKHR', (VkExternalFenceHandleTypeFlags,), dict())
VkExternalFenceFeatureFlags = type('VkExternalFenceFeatureFlags', (VkFlags,), dict())
VkExternalFenceFeatureFlagsKHR = type('VkExternalFenceFeatureFlagsKHR', (VkExternalFenceFeatureFlags,), dict())
VkFenceImportFlags = type('VkFenceImportFlags', (VkFlags,), dict())
VkFenceImportFlagsKHR = type('VkFenceImportFlagsKHR', (VkFenceImportFlags,), dict())
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
VkDescriptorBindingFlagsEXT = type('VkDescriptorBindingFlagsEXT', (VkDescriptorBindingFlags,), dict())
VkConditionalRenderingFlagsEXT = type('VkConditionalRenderingFlagsEXT', (VkFlags,), dict())
VkResolveModeFlags = type('VkResolveModeFlags', (VkFlags,), dict())
VkResolveModeFlagsKHR = type('VkResolveModeFlagsKHR', (VkResolveModeFlags,), dict())
VkPipelineRasterizationStateStreamCreateFlagsEXT = type('VkPipelineRasterizationStateStreamCreateFlagsEXT', (VkFlags,), dict())
VkPipelineRasterizationDepthClipStateCreateFlagsEXT = type('VkPipelineRasterizationDepthClipStateCreateFlagsEXT', (VkFlags,), dict())
VkSwapchainImageUsageFlagsANDROID = type('VkSwapchainImageUsageFlagsANDROID', (VkFlags,), dict())
VkToolPurposeFlagsEXT = type('VkToolPurposeFlagsEXT', (VkFlags,), dict())


# HANDLE TYPES
VK_NULL_HANDLE = 0
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


# VkImageLayout
VK_IMAGE_LAYOUT_UNDEFINED = 0
VK_IMAGE_LAYOUT_GENERAL = 1
VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL = 2
VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL = 3
VK_IMAGE_LAYOUT_DEPTH_STENCIL_READ_ONLY_OPTIMAL = 4
VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL = 5
VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL = 6
VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL = 7
VK_IMAGE_LAYOUT_PREINITIALIZED = 8


# VkAttachmentLoadOp
VK_ATTACHMENT_LOAD_OP_LOAD = 0
VK_ATTACHMENT_LOAD_OP_CLEAR = 1
VK_ATTACHMENT_LOAD_OP_DONT_CARE = 2


# VkAttachmentStoreOp
VK_ATTACHMENT_STORE_OP_STORE = 0
VK_ATTACHMENT_STORE_OP_DONT_CARE = 1


# VkImageType
VK_IMAGE_TYPE_1D = 0
VK_IMAGE_TYPE_2D = 1
VK_IMAGE_TYPE_3D = 2


# VkImageTiling
VK_IMAGE_TILING_OPTIMAL = 0
VK_IMAGE_TILING_LINEAR = 1


# VkImageViewType
VK_IMAGE_VIEW_TYPE_1D = 0
VK_IMAGE_VIEW_TYPE_2D = 1
VK_IMAGE_VIEW_TYPE_3D = 2
VK_IMAGE_VIEW_TYPE_CUBE = 3
VK_IMAGE_VIEW_TYPE_1D_ARRAY = 4
VK_IMAGE_VIEW_TYPE_2D_ARRAY = 5
VK_IMAGE_VIEW_TYPE_CUBE_ARRAY = 6


# VkCommandBufferLevel
VK_COMMAND_BUFFER_LEVEL_PRIMARY = 0
VK_COMMAND_BUFFER_LEVEL_SECONDARY = 1


# VkComponentSwizzle
VK_COMPONENT_SWIZZLE_IDENTITY = 0
VK_COMPONENT_SWIZZLE_ZERO = 1
VK_COMPONENT_SWIZZLE_ONE = 2
VK_COMPONENT_SWIZZLE_R = 3
VK_COMPONENT_SWIZZLE_G = 4
VK_COMPONENT_SWIZZLE_B = 5
VK_COMPONENT_SWIZZLE_A = 6


# VkDescriptorType
VK_DESCRIPTOR_TYPE_SAMPLER = 0
VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER = 1
VK_DESCRIPTOR_TYPE_SAMPLED_IMAGE = 2
VK_DESCRIPTOR_TYPE_STORAGE_IMAGE = 3
VK_DESCRIPTOR_TYPE_UNIFORM_TEXEL_BUFFER = 4
VK_DESCRIPTOR_TYPE_STORAGE_TEXEL_BUFFER = 5
VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER = 6
VK_DESCRIPTOR_TYPE_STORAGE_BUFFER = 7
VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER_DYNAMIC = 8
VK_DESCRIPTOR_TYPE_STORAGE_BUFFER_DYNAMIC = 9
VK_DESCRIPTOR_TYPE_INPUT_ATTACHMENT = 10


# VkQueryType
VK_QUERY_TYPE_OCCLUSION = 0
VK_QUERY_TYPE_PIPELINE_STATISTICS = 1
VK_QUERY_TYPE_TIMESTAMP = 2


# VkBorderColor
VK_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK = 0
VK_BORDER_COLOR_INT_TRANSPARENT_BLACK = 1
VK_BORDER_COLOR_FLOAT_OPAQUE_BLACK = 2
VK_BORDER_COLOR_INT_OPAQUE_BLACK = 3
VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE = 4
VK_BORDER_COLOR_INT_OPAQUE_WHITE = 5


# VkPipelineBindPoint
VK_PIPELINE_BIND_POINT_GRAPHICS = 0
VK_PIPELINE_BIND_POINT_COMPUTE = 1


# VkPipelineCacheHeaderVersion
VK_PIPELINE_CACHE_HEADER_VERSION_ONE = 1


# VkPipelineCacheCreateFlagBits


# VkPrimitiveTopology
VK_PRIMITIVE_TOPOLOGY_POINT_LIST = 0
VK_PRIMITIVE_TOPOLOGY_LINE_LIST = 1
VK_PRIMITIVE_TOPOLOGY_LINE_STRIP = 2
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST = 3
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_STRIP = 4
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_FAN = 5
VK_PRIMITIVE_TOPOLOGY_LINE_LIST_WITH_ADJACENCY = 6
VK_PRIMITIVE_TOPOLOGY_LINE_STRIP_WITH_ADJACENCY = 7
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST_WITH_ADJACENCY = 8
VK_PRIMITIVE_TOPOLOGY_TRIANGLE_STRIP_WITH_ADJACENCY = 9
VK_PRIMITIVE_TOPOLOGY_PATCH_LIST = 10


# VkSharingMode
VK_SHARING_MODE_EXCLUSIVE = 0
VK_SHARING_MODE_CONCURRENT = 1


# VkIndexType
VK_INDEX_TYPE_UINT16 = 0
VK_INDEX_TYPE_UINT32 = 1


# VkFilter
VK_FILTER_NEAREST = 0
VK_FILTER_LINEAR = 1


# VkSamplerMipmapMode
VK_SAMPLER_MIPMAP_MODE_NEAREST = 0
VK_SAMPLER_MIPMAP_MODE_LINEAR = 1


# VkSamplerAddressMode
VK_SAMPLER_ADDRESS_MODE_REPEAT = 0
VK_SAMPLER_ADDRESS_MODE_MIRRORED_REPEAT = 1
VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE = 2
VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_BORDER = 3


# VkCompareOp
VK_COMPARE_OP_NEVER = 0
VK_COMPARE_OP_LESS = 1
VK_COMPARE_OP_EQUAL = 2
VK_COMPARE_OP_LESS_OR_EQUAL = 3
VK_COMPARE_OP_GREATER = 4
VK_COMPARE_OP_NOT_EQUAL = 5
VK_COMPARE_OP_GREATER_OR_EQUAL = 6
VK_COMPARE_OP_ALWAYS = 7


# VkPolygonMode
VK_POLYGON_MODE_FILL = 0
VK_POLYGON_MODE_LINE = 1
VK_POLYGON_MODE_POINT = 2


# VkFrontFace
VK_FRONT_FACE_COUNTER_CLOCKWISE = 0
VK_FRONT_FACE_CLOCKWISE = 1


# VkBlendFactor
VK_BLEND_FACTOR_ZERO = 0
VK_BLEND_FACTOR_ONE = 1
VK_BLEND_FACTOR_SRC_COLOR = 2
VK_BLEND_FACTOR_ONE_MINUS_SRC_COLOR = 3
VK_BLEND_FACTOR_DST_COLOR = 4
VK_BLEND_FACTOR_ONE_MINUS_DST_COLOR = 5
VK_BLEND_FACTOR_SRC_ALPHA = 6
VK_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA = 7
VK_BLEND_FACTOR_DST_ALPHA = 8
VK_BLEND_FACTOR_ONE_MINUS_DST_ALPHA = 9
VK_BLEND_FACTOR_CONSTANT_COLOR = 10
VK_BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR = 11
VK_BLEND_FACTOR_CONSTANT_ALPHA = 12
VK_BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA = 13
VK_BLEND_FACTOR_SRC_ALPHA_SATURATE = 14
VK_BLEND_FACTOR_SRC1_COLOR = 15
VK_BLEND_FACTOR_ONE_MINUS_SRC1_COLOR = 16
VK_BLEND_FACTOR_SRC1_ALPHA = 17
VK_BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA = 18


# VkBlendOp
VK_BLEND_OP_ADD = 0
VK_BLEND_OP_SUBTRACT = 1
VK_BLEND_OP_REVERSE_SUBTRACT = 2
VK_BLEND_OP_MIN = 3
VK_BLEND_OP_MAX = 4


# VkStencilOp
VK_STENCIL_OP_KEEP = 0
VK_STENCIL_OP_ZERO = 1
VK_STENCIL_OP_REPLACE = 2
VK_STENCIL_OP_INCREMENT_AND_CLAMP = 3
VK_STENCIL_OP_DECREMENT_AND_CLAMP = 4
VK_STENCIL_OP_INVERT = 5
VK_STENCIL_OP_INCREMENT_AND_WRAP = 6
VK_STENCIL_OP_DECREMENT_AND_WRAP = 7


# VkLogicOp
VK_LOGIC_OP_CLEAR = 0
VK_LOGIC_OP_AND = 1
VK_LOGIC_OP_AND_REVERSE = 2
VK_LOGIC_OP_COPY = 3
VK_LOGIC_OP_AND_INVERTED = 4
VK_LOGIC_OP_NO_OP = 5
VK_LOGIC_OP_XOR = 6
VK_LOGIC_OP_OR = 7
VK_LOGIC_OP_NOR = 8
VK_LOGIC_OP_EQUIVALENT = 9
VK_LOGIC_OP_INVERT = 10
VK_LOGIC_OP_OR_REVERSE = 11
VK_LOGIC_OP_COPY_INVERTED = 12
VK_LOGIC_OP_OR_INVERTED = 13
VK_LOGIC_OP_NAND = 14
VK_LOGIC_OP_SET = 15


# VkInternalAllocationType
VK_INTERNAL_ALLOCATION_TYPE_EXECUTABLE = 0


# VkSystemAllocationScope
VK_SYSTEM_ALLOCATION_SCOPE_COMMAND = 0
VK_SYSTEM_ALLOCATION_SCOPE_OBJECT = 1
VK_SYSTEM_ALLOCATION_SCOPE_CACHE = 2
VK_SYSTEM_ALLOCATION_SCOPE_DEVICE = 3
VK_SYSTEM_ALLOCATION_SCOPE_INSTANCE = 4


# VkPhysicalDeviceType
VK_PHYSICAL_DEVICE_TYPE_OTHER = 0
VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU = 1
VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU = 2
VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU = 3
VK_PHYSICAL_DEVICE_TYPE_CPU = 4


# VkVertexInputRate
VK_VERTEX_INPUT_RATE_VERTEX = 0
VK_VERTEX_INPUT_RATE_INSTANCE = 1


# VkFormat
VK_FORMAT_UNDEFINED = 0
VK_FORMAT_R4G4_UNORM_PACK8 = 1
VK_FORMAT_R4G4B4A4_UNORM_PACK16 = 2
VK_FORMAT_B4G4R4A4_UNORM_PACK16 = 3
VK_FORMAT_R5G6B5_UNORM_PACK16 = 4
VK_FORMAT_B5G6R5_UNORM_PACK16 = 5
VK_FORMAT_R5G5B5A1_UNORM_PACK16 = 6
VK_FORMAT_B5G5R5A1_UNORM_PACK16 = 7
VK_FORMAT_A1R5G5B5_UNORM_PACK16 = 8
VK_FORMAT_R8_UNORM = 9
VK_FORMAT_R8_SNORM = 10
VK_FORMAT_R8_USCALED = 11
VK_FORMAT_R8_SSCALED = 12
VK_FORMAT_R8_UINT = 13
VK_FORMAT_R8_SINT = 14
VK_FORMAT_R8_SRGB = 15
VK_FORMAT_R8G8_UNORM = 16
VK_FORMAT_R8G8_SNORM = 17
VK_FORMAT_R8G8_USCALED = 18
VK_FORMAT_R8G8_SSCALED = 19
VK_FORMAT_R8G8_UINT = 20
VK_FORMAT_R8G8_SINT = 21
VK_FORMAT_R8G8_SRGB = 22
VK_FORMAT_R8G8B8_UNORM = 23
VK_FORMAT_R8G8B8_SNORM = 24
VK_FORMAT_R8G8B8_USCALED = 25
VK_FORMAT_R8G8B8_SSCALED = 26
VK_FORMAT_R8G8B8_UINT = 27
VK_FORMAT_R8G8B8_SINT = 28
VK_FORMAT_R8G8B8_SRGB = 29
VK_FORMAT_B8G8R8_UNORM = 30
VK_FORMAT_B8G8R8_SNORM = 31
VK_FORMAT_B8G8R8_USCALED = 32
VK_FORMAT_B8G8R8_SSCALED = 33
VK_FORMAT_B8G8R8_UINT = 34
VK_FORMAT_B8G8R8_SINT = 35
VK_FORMAT_B8G8R8_SRGB = 36
VK_FORMAT_R8G8B8A8_UNORM = 37
VK_FORMAT_R8G8B8A8_SNORM = 38
VK_FORMAT_R8G8B8A8_USCALED = 39
VK_FORMAT_R8G8B8A8_SSCALED = 40
VK_FORMAT_R8G8B8A8_UINT = 41
VK_FORMAT_R8G8B8A8_SINT = 42
VK_FORMAT_R8G8B8A8_SRGB = 43
VK_FORMAT_B8G8R8A8_UNORM = 44
VK_FORMAT_B8G8R8A8_SNORM = 45
VK_FORMAT_B8G8R8A8_USCALED = 46
VK_FORMAT_B8G8R8A8_SSCALED = 47
VK_FORMAT_B8G8R8A8_UINT = 48
VK_FORMAT_B8G8R8A8_SINT = 49
VK_FORMAT_B8G8R8A8_SRGB = 50
VK_FORMAT_A8B8G8R8_UNORM_PACK32 = 51
VK_FORMAT_A8B8G8R8_SNORM_PACK32 = 52
VK_FORMAT_A8B8G8R8_USCALED_PACK32 = 53
VK_FORMAT_A8B8G8R8_SSCALED_PACK32 = 54
VK_FORMAT_A8B8G8R8_UINT_PACK32 = 55
VK_FORMAT_A8B8G8R8_SINT_PACK32 = 56
VK_FORMAT_A8B8G8R8_SRGB_PACK32 = 57
VK_FORMAT_A2R10G10B10_UNORM_PACK32 = 58
VK_FORMAT_A2R10G10B10_SNORM_PACK32 = 59
VK_FORMAT_A2R10G10B10_USCALED_PACK32 = 60
VK_FORMAT_A2R10G10B10_SSCALED_PACK32 = 61
VK_FORMAT_A2R10G10B10_UINT_PACK32 = 62
VK_FORMAT_A2R10G10B10_SINT_PACK32 = 63
VK_FORMAT_A2B10G10R10_UNORM_PACK32 = 64
VK_FORMAT_A2B10G10R10_SNORM_PACK32 = 65
VK_FORMAT_A2B10G10R10_USCALED_PACK32 = 66
VK_FORMAT_A2B10G10R10_SSCALED_PACK32 = 67
VK_FORMAT_A2B10G10R10_UINT_PACK32 = 68
VK_FORMAT_A2B10G10R10_SINT_PACK32 = 69
VK_FORMAT_R16_UNORM = 70
VK_FORMAT_R16_SNORM = 71
VK_FORMAT_R16_USCALED = 72
VK_FORMAT_R16_SSCALED = 73
VK_FORMAT_R16_UINT = 74
VK_FORMAT_R16_SINT = 75
VK_FORMAT_R16_SFLOAT = 76
VK_FORMAT_R16G16_UNORM = 77
VK_FORMAT_R16G16_SNORM = 78
VK_FORMAT_R16G16_USCALED = 79
VK_FORMAT_R16G16_SSCALED = 80
VK_FORMAT_R16G16_UINT = 81
VK_FORMAT_R16G16_SINT = 82
VK_FORMAT_R16G16_SFLOAT = 83
VK_FORMAT_R16G16B16_UNORM = 84
VK_FORMAT_R16G16B16_SNORM = 85
VK_FORMAT_R16G16B16_USCALED = 86
VK_FORMAT_R16G16B16_SSCALED = 87
VK_FORMAT_R16G16B16_UINT = 88
VK_FORMAT_R16G16B16_SINT = 89
VK_FORMAT_R16G16B16_SFLOAT = 90
VK_FORMAT_R16G16B16A16_UNORM = 91
VK_FORMAT_R16G16B16A16_SNORM = 92
VK_FORMAT_R16G16B16A16_USCALED = 93
VK_FORMAT_R16G16B16A16_SSCALED = 94
VK_FORMAT_R16G16B16A16_UINT = 95
VK_FORMAT_R16G16B16A16_SINT = 96
VK_FORMAT_R16G16B16A16_SFLOAT = 97
VK_FORMAT_R32_UINT = 98
VK_FORMAT_R32_SINT = 99
VK_FORMAT_R32_SFLOAT = 100
VK_FORMAT_R32G32_UINT = 101
VK_FORMAT_R32G32_SINT = 102
VK_FORMAT_R32G32_SFLOAT = 103
VK_FORMAT_R32G32B32_UINT = 104
VK_FORMAT_R32G32B32_SINT = 105
VK_FORMAT_R32G32B32_SFLOAT = 106
VK_FORMAT_R32G32B32A32_UINT = 107
VK_FORMAT_R32G32B32A32_SINT = 108
VK_FORMAT_R32G32B32A32_SFLOAT = 109
VK_FORMAT_R64_UINT = 110
VK_FORMAT_R64_SINT = 111
VK_FORMAT_R64_SFLOAT = 112
VK_FORMAT_R64G64_UINT = 113
VK_FORMAT_R64G64_SINT = 114
VK_FORMAT_R64G64_SFLOAT = 115
VK_FORMAT_R64G64B64_UINT = 116
VK_FORMAT_R64G64B64_SINT = 117
VK_FORMAT_R64G64B64_SFLOAT = 118
VK_FORMAT_R64G64B64A64_UINT = 119
VK_FORMAT_R64G64B64A64_SINT = 120
VK_FORMAT_R64G64B64A64_SFLOAT = 121
VK_FORMAT_B10G11R11_UFLOAT_PACK32 = 122
VK_FORMAT_E5B9G9R9_UFLOAT_PACK32 = 123
VK_FORMAT_D16_UNORM = 124
VK_FORMAT_X8_D24_UNORM_PACK32 = 125
VK_FORMAT_D32_SFLOAT = 126
VK_FORMAT_S8_UINT = 127
VK_FORMAT_D16_UNORM_S8_UINT = 128
VK_FORMAT_D24_UNORM_S8_UINT = 129
VK_FORMAT_D32_SFLOAT_S8_UINT = 130
VK_FORMAT_BC1_RGB_UNORM_BLOCK = 131
VK_FORMAT_BC1_RGB_SRGB_BLOCK = 132
VK_FORMAT_BC1_RGBA_UNORM_BLOCK = 133
VK_FORMAT_BC1_RGBA_SRGB_BLOCK = 134
VK_FORMAT_BC2_UNORM_BLOCK = 135
VK_FORMAT_BC2_SRGB_BLOCK = 136
VK_FORMAT_BC3_UNORM_BLOCK = 137
VK_FORMAT_BC3_SRGB_BLOCK = 138
VK_FORMAT_BC4_UNORM_BLOCK = 139
VK_FORMAT_BC4_SNORM_BLOCK = 140
VK_FORMAT_BC5_UNORM_BLOCK = 141
VK_FORMAT_BC5_SNORM_BLOCK = 142
VK_FORMAT_BC6H_UFLOAT_BLOCK = 143
VK_FORMAT_BC6H_SFLOAT_BLOCK = 144
VK_FORMAT_BC7_UNORM_BLOCK = 145
VK_FORMAT_BC7_SRGB_BLOCK = 146
VK_FORMAT_ETC2_R8G8B8_UNORM_BLOCK = 147
VK_FORMAT_ETC2_R8G8B8_SRGB_BLOCK = 148
VK_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK = 149
VK_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK = 150
VK_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK = 151
VK_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK = 152
VK_FORMAT_EAC_R11_UNORM_BLOCK = 153
VK_FORMAT_EAC_R11_SNORM_BLOCK = 154
VK_FORMAT_EAC_R11G11_UNORM_BLOCK = 155
VK_FORMAT_EAC_R11G11_SNORM_BLOCK = 156
VK_FORMAT_ASTC_4x4_UNORM_BLOCK = 157
VK_FORMAT_ASTC_4x4_SRGB_BLOCK = 158
VK_FORMAT_ASTC_5x4_UNORM_BLOCK = 159
VK_FORMAT_ASTC_5x4_SRGB_BLOCK = 160
VK_FORMAT_ASTC_5x5_UNORM_BLOCK = 161
VK_FORMAT_ASTC_5x5_SRGB_BLOCK = 162
VK_FORMAT_ASTC_6x5_UNORM_BLOCK = 163
VK_FORMAT_ASTC_6x5_SRGB_BLOCK = 164
VK_FORMAT_ASTC_6x6_UNORM_BLOCK = 165
VK_FORMAT_ASTC_6x6_SRGB_BLOCK = 166
VK_FORMAT_ASTC_8x5_UNORM_BLOCK = 167
VK_FORMAT_ASTC_8x5_SRGB_BLOCK = 168
VK_FORMAT_ASTC_8x6_UNORM_BLOCK = 169
VK_FORMAT_ASTC_8x6_SRGB_BLOCK = 170
VK_FORMAT_ASTC_8x8_UNORM_BLOCK = 171
VK_FORMAT_ASTC_8x8_SRGB_BLOCK = 172
VK_FORMAT_ASTC_10x5_UNORM_BLOCK = 173
VK_FORMAT_ASTC_10x5_SRGB_BLOCK = 174
VK_FORMAT_ASTC_10x6_UNORM_BLOCK = 175
VK_FORMAT_ASTC_10x6_SRGB_BLOCK = 176
VK_FORMAT_ASTC_10x8_UNORM_BLOCK = 177
VK_FORMAT_ASTC_10x8_SRGB_BLOCK = 178
VK_FORMAT_ASTC_10x10_UNORM_BLOCK = 179
VK_FORMAT_ASTC_10x10_SRGB_BLOCK = 180
VK_FORMAT_ASTC_12x10_UNORM_BLOCK = 181
VK_FORMAT_ASTC_12x10_SRGB_BLOCK = 182
VK_FORMAT_ASTC_12x12_UNORM_BLOCK = 183
VK_FORMAT_ASTC_12x12_SRGB_BLOCK = 184


# VkStructureType
VK_STRUCTURE_TYPE_APPLICATION_INFO = 0
VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO = 1
VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO = 2
VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO = 3
VK_STRUCTURE_TYPE_SUBMIT_INFO = 4
VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO = 5
VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE = 6
VK_STRUCTURE_TYPE_BIND_SPARSE_INFO = 7
VK_STRUCTURE_TYPE_FENCE_CREATE_INFO = 8
VK_STRUCTURE_TYPE_SEMAPHORE_CREATE_INFO = 9
VK_STRUCTURE_TYPE_EVENT_CREATE_INFO = 10
VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO = 11
VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO = 12
VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO = 13
VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO = 14
VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO = 15
VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO = 16
VK_STRUCTURE_TYPE_PIPELINE_CACHE_CREATE_INFO = 17
VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO = 18
VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO = 19
VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO = 20
VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_STATE_CREATE_INFO = 21
VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO = 22
VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO = 23
VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO = 24
VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO = 25
VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO = 26
VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO = 27
VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO = 28
VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO = 29
VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO = 30
VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO = 31
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO = 32
VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO = 33
VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO = 34
VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET = 35
VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET = 36
VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO = 37
VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO = 38
VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO = 39
VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO = 40
VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO = 41
VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO = 42
VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO = 43
VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER = 44
VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER = 45
VK_STRUCTURE_TYPE_MEMORY_BARRIER = 46
VK_STRUCTURE_TYPE_LOADER_INSTANCE_CREATE_INFO = 47
VK_STRUCTURE_TYPE_LOADER_DEVICE_CREATE_INFO = 48


# VkSubpassContents
VK_SUBPASS_CONTENTS_INLINE = 0
VK_SUBPASS_CONTENTS_SECONDARY_COMMAND_BUFFERS = 1


# VkResult
VK_SUCCESS = 0
VK_NOT_READY = 1
VK_TIMEOUT = 2
VK_EVENT_SET = 3
VK_EVENT_RESET = 4
VK_INCOMPLETE = 5
VK_ERROR_OUT_OF_HOST_MEMORY = -1
VK_ERROR_OUT_OF_DEVICE_MEMORY = -2
VK_ERROR_INITIALIZATION_FAILED = -3
VK_ERROR_DEVICE_LOST = -4
VK_ERROR_MEMORY_MAP_FAILED = -5
VK_ERROR_LAYER_NOT_PRESENT = -6
VK_ERROR_EXTENSION_NOT_PRESENT = -7
VK_ERROR_FEATURE_NOT_PRESENT = -8
VK_ERROR_INCOMPATIBLE_DRIVER = -9
VK_ERROR_TOO_MANY_OBJECTS = -10
VK_ERROR_FORMAT_NOT_SUPPORTED = -11
VK_ERROR_FRAGMENTED_POOL = -12
VK_ERROR_UNKNOWN = -13


# VkDynamicState
VK_DYNAMIC_STATE_VIEWPORT = 0
VK_DYNAMIC_STATE_SCISSOR = 1
VK_DYNAMIC_STATE_LINE_WIDTH = 2
VK_DYNAMIC_STATE_DEPTH_BIAS = 3
VK_DYNAMIC_STATE_BLEND_CONSTANTS = 4
VK_DYNAMIC_STATE_DEPTH_BOUNDS = 5
VK_DYNAMIC_STATE_STENCIL_COMPARE_MASK = 6
VK_DYNAMIC_STATE_STENCIL_WRITE_MASK = 7
VK_DYNAMIC_STATE_STENCIL_REFERENCE = 8


# VkDescriptorUpdateTemplateType
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET = 0


# VkObjectType
VK_OBJECT_TYPE_UNKNOWN = 0
VK_OBJECT_TYPE_INSTANCE = 1
VK_OBJECT_TYPE_PHYSICAL_DEVICE = 2
VK_OBJECT_TYPE_DEVICE = 3
VK_OBJECT_TYPE_QUEUE = 4
VK_OBJECT_TYPE_SEMAPHORE = 5
VK_OBJECT_TYPE_COMMAND_BUFFER = 6
VK_OBJECT_TYPE_FENCE = 7
VK_OBJECT_TYPE_DEVICE_MEMORY = 8
VK_OBJECT_TYPE_BUFFER = 9
VK_OBJECT_TYPE_IMAGE = 10
VK_OBJECT_TYPE_EVENT = 11
VK_OBJECT_TYPE_QUERY_POOL = 12
VK_OBJECT_TYPE_BUFFER_VIEW = 13
VK_OBJECT_TYPE_IMAGE_VIEW = 14
VK_OBJECT_TYPE_SHADER_MODULE = 15
VK_OBJECT_TYPE_PIPELINE_CACHE = 16
VK_OBJECT_TYPE_PIPELINE_LAYOUT = 17
VK_OBJECT_TYPE_RENDER_PASS = 18
VK_OBJECT_TYPE_PIPELINE = 19
VK_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT = 20
VK_OBJECT_TYPE_SAMPLER = 21
VK_OBJECT_TYPE_DESCRIPTOR_POOL = 22
VK_OBJECT_TYPE_DESCRIPTOR_SET = 23
VK_OBJECT_TYPE_FRAMEBUFFER = 24
VK_OBJECT_TYPE_COMMAND_POOL = 25


# VkQueueFlagBits
VK_QUEUE_GRAPHICS_BIT = 1
VK_QUEUE_COMPUTE_BIT = 2
VK_QUEUE_TRANSFER_BIT = 4
VK_QUEUE_SPARSE_BINDING_BIT = 8


# VkCullModeFlagBits
VK_CULL_MODE_NONE = 0
VK_CULL_MODE_FRONT_BIT = 1
VK_CULL_MODE_BACK_BIT = 2
VK_CULL_MODE_FRONT_AND_BACK = 0x00000003


# VkRenderPassCreateFlagBits


# VkDeviceQueueCreateFlagBits


# VkMemoryPropertyFlagBits
VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT = 1
VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT = 2
VK_MEMORY_PROPERTY_HOST_COHERENT_BIT = 4
VK_MEMORY_PROPERTY_HOST_CACHED_BIT = 8
VK_MEMORY_PROPERTY_LAZILY_ALLOCATED_BIT = 16


# VkMemoryHeapFlagBits
VK_MEMORY_HEAP_DEVICE_LOCAL_BIT = 1


# VkAccessFlagBits
VK_ACCESS_INDIRECT_COMMAND_READ_BIT = 1
VK_ACCESS_INDEX_READ_BIT = 2
VK_ACCESS_VERTEX_ATTRIBUTE_READ_BIT = 4
VK_ACCESS_UNIFORM_READ_BIT = 8
VK_ACCESS_INPUT_ATTACHMENT_READ_BIT = 16
VK_ACCESS_SHADER_READ_BIT = 32
VK_ACCESS_SHADER_WRITE_BIT = 64
VK_ACCESS_COLOR_ATTACHMENT_READ_BIT = 128
VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT = 256
VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_READ_BIT = 512
VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT = 1024
VK_ACCESS_TRANSFER_READ_BIT = 2048
VK_ACCESS_TRANSFER_WRITE_BIT = 4096
VK_ACCESS_HOST_READ_BIT = 8192
VK_ACCESS_HOST_WRITE_BIT = 16384
VK_ACCESS_MEMORY_READ_BIT = 32768
VK_ACCESS_MEMORY_WRITE_BIT = 65536


# VkBufferUsageFlagBits
VK_BUFFER_USAGE_TRANSFER_SRC_BIT = 1
VK_BUFFER_USAGE_TRANSFER_DST_BIT = 2
VK_BUFFER_USAGE_UNIFORM_TEXEL_BUFFER_BIT = 4
VK_BUFFER_USAGE_STORAGE_TEXEL_BUFFER_BIT = 8
VK_BUFFER_USAGE_UNIFORM_BUFFER_BIT = 16
VK_BUFFER_USAGE_STORAGE_BUFFER_BIT = 32
VK_BUFFER_USAGE_INDEX_BUFFER_BIT = 64
VK_BUFFER_USAGE_VERTEX_BUFFER_BIT = 128
VK_BUFFER_USAGE_INDIRECT_BUFFER_BIT = 256


# VkBufferCreateFlagBits
VK_BUFFER_CREATE_SPARSE_BINDING_BIT = 1
VK_BUFFER_CREATE_SPARSE_RESIDENCY_BIT = 2
VK_BUFFER_CREATE_SPARSE_ALIASED_BIT = 4


# VkShaderStageFlagBits
VK_SHADER_STAGE_VERTEX_BIT = 1
VK_SHADER_STAGE_TESSELLATION_CONTROL_BIT = 2
VK_SHADER_STAGE_TESSELLATION_EVALUATION_BIT = 4
VK_SHADER_STAGE_GEOMETRY_BIT = 8
VK_SHADER_STAGE_FRAGMENT_BIT = 16
VK_SHADER_STAGE_COMPUTE_BIT = 32
VK_SHADER_STAGE_ALL_GRAPHICS = 0x0000001F
VK_SHADER_STAGE_ALL = 0x7FFFFFFF


# VkImageUsageFlagBits
VK_IMAGE_USAGE_TRANSFER_SRC_BIT = 1
VK_IMAGE_USAGE_TRANSFER_DST_BIT = 2
VK_IMAGE_USAGE_SAMPLED_BIT = 4
VK_IMAGE_USAGE_STORAGE_BIT = 8
VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT = 16
VK_IMAGE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT = 32
VK_IMAGE_USAGE_TRANSIENT_ATTACHMENT_BIT = 64
VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT = 128


# VkImageCreateFlagBits
VK_IMAGE_CREATE_SPARSE_BINDING_BIT = 1
VK_IMAGE_CREATE_SPARSE_RESIDENCY_BIT = 2
VK_IMAGE_CREATE_SPARSE_ALIASED_BIT = 4
VK_IMAGE_CREATE_MUTABLE_FORMAT_BIT = 8
VK_IMAGE_CREATE_CUBE_COMPATIBLE_BIT = 16


# VkImageViewCreateFlagBits


# VkSamplerCreateFlagBits


# VkPipelineCreateFlagBits
VK_PIPELINE_CREATE_DISABLE_OPTIMIZATION_BIT = 1
VK_PIPELINE_CREATE_ALLOW_DERIVATIVES_BIT = 2
VK_PIPELINE_CREATE_DERIVATIVE_BIT = 4


# VkPipelineShaderStageCreateFlagBits


# VkColorComponentFlagBits
VK_COLOR_COMPONENT_R_BIT = 1
VK_COLOR_COMPONENT_G_BIT = 2
VK_COLOR_COMPONENT_B_BIT = 4
VK_COLOR_COMPONENT_A_BIT = 8


# VkFenceCreateFlagBits
VK_FENCE_CREATE_SIGNALED_BIT = 1


# VkFormatFeatureFlagBits
VK_FORMAT_FEATURE_SAMPLED_IMAGE_BIT = 1
VK_FORMAT_FEATURE_STORAGE_IMAGE_BIT = 2
VK_FORMAT_FEATURE_STORAGE_IMAGE_ATOMIC_BIT = 4
VK_FORMAT_FEATURE_UNIFORM_TEXEL_BUFFER_BIT = 8
VK_FORMAT_FEATURE_STORAGE_TEXEL_BUFFER_BIT = 16
VK_FORMAT_FEATURE_STORAGE_TEXEL_BUFFER_ATOMIC_BIT = 32
VK_FORMAT_FEATURE_VERTEX_BUFFER_BIT = 64
VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BIT = 128
VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BLEND_BIT = 256
VK_FORMAT_FEATURE_DEPTH_STENCIL_ATTACHMENT_BIT = 512
VK_FORMAT_FEATURE_BLIT_SRC_BIT = 1024
VK_FORMAT_FEATURE_BLIT_DST_BIT = 2048
VK_FORMAT_FEATURE_SAMPLED_IMAGE_FILTER_LINEAR_BIT = 4096


# VkQueryControlFlagBits
VK_QUERY_CONTROL_PRECISE_BIT = 1


# VkQueryResultFlagBits
VK_QUERY_RESULT_64_BIT = 1
VK_QUERY_RESULT_WAIT_BIT = 2
VK_QUERY_RESULT_WITH_AVAILABILITY_BIT = 4
VK_QUERY_RESULT_PARTIAL_BIT = 8


# VkCommandBufferUsageFlagBits
VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT = 1
VK_COMMAND_BUFFER_USAGE_RENDER_PASS_CONTINUE_BIT = 2
VK_COMMAND_BUFFER_USAGE_SIMULTANEOUS_USE_BIT = 4


# VkQueryPipelineStatisticFlagBits
VK_QUERY_PIPELINE_STATISTIC_INPUT_ASSEMBLY_VERTICES_BIT = 1
VK_QUERY_PIPELINE_STATISTIC_INPUT_ASSEMBLY_PRIMITIVES_BIT = 2
VK_QUERY_PIPELINE_STATISTIC_VERTEX_SHADER_INVOCATIONS_BIT = 4
VK_QUERY_PIPELINE_STATISTIC_GEOMETRY_SHADER_INVOCATIONS_BIT = 8
VK_QUERY_PIPELINE_STATISTIC_GEOMETRY_SHADER_PRIMITIVES_BIT = 16
VK_QUERY_PIPELINE_STATISTIC_CLIPPING_INVOCATIONS_BIT = 32
VK_QUERY_PIPELINE_STATISTIC_CLIPPING_PRIMITIVES_BIT = 64
VK_QUERY_PIPELINE_STATISTIC_FRAGMENT_SHADER_INVOCATIONS_BIT = 128
VK_QUERY_PIPELINE_STATISTIC_TESSELLATION_CONTROL_SHADER_PATCHES_BIT = 256
VK_QUERY_PIPELINE_STATISTIC_TESSELLATION_EVALUATION_SHADER_INVOCATIONS_BIT = 512
VK_QUERY_PIPELINE_STATISTIC_COMPUTE_SHADER_INVOCATIONS_BIT = 1024


# VkImageAspectFlagBits
VK_IMAGE_ASPECT_COLOR_BIT = 1
VK_IMAGE_ASPECT_DEPTH_BIT = 2
VK_IMAGE_ASPECT_STENCIL_BIT = 4
VK_IMAGE_ASPECT_METADATA_BIT = 8


# VkSparseImageFormatFlagBits
VK_SPARSE_IMAGE_FORMAT_SINGLE_MIPTAIL_BIT = 1
VK_SPARSE_IMAGE_FORMAT_ALIGNED_MIP_SIZE_BIT = 2
VK_SPARSE_IMAGE_FORMAT_NONSTANDARD_BLOCK_SIZE_BIT = 4


# VkSparseMemoryBindFlagBits
VK_SPARSE_MEMORY_BIND_METADATA_BIT = 1


# VkPipelineStageFlagBits
VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT = 1
VK_PIPELINE_STAGE_DRAW_INDIRECT_BIT = 2
VK_PIPELINE_STAGE_VERTEX_INPUT_BIT = 4
VK_PIPELINE_STAGE_VERTEX_SHADER_BIT = 8
VK_PIPELINE_STAGE_TESSELLATION_CONTROL_SHADER_BIT = 16
VK_PIPELINE_STAGE_TESSELLATION_EVALUATION_SHADER_BIT = 32
VK_PIPELINE_STAGE_GEOMETRY_SHADER_BIT = 64
VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT = 128
VK_PIPELINE_STAGE_EARLY_FRAGMENT_TESTS_BIT = 256
VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT = 512
VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT = 1024
VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT = 2048
VK_PIPELINE_STAGE_TRANSFER_BIT = 4096
VK_PIPELINE_STAGE_BOTTOM_OF_PIPE_BIT = 8192
VK_PIPELINE_STAGE_HOST_BIT = 16384
VK_PIPELINE_STAGE_ALL_GRAPHICS_BIT = 32768
VK_PIPELINE_STAGE_ALL_COMMANDS_BIT = 65536


# VkCommandPoolCreateFlagBits
VK_COMMAND_POOL_CREATE_TRANSIENT_BIT = 1
VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT = 2


# VkCommandPoolResetFlagBits
VK_COMMAND_POOL_RESET_RELEASE_RESOURCES_BIT = 1


# VkCommandBufferResetFlagBits
VK_COMMAND_BUFFER_RESET_RELEASE_RESOURCES_BIT = 1


# VkSampleCountFlagBits
VK_SAMPLE_COUNT_1_BIT = 1
VK_SAMPLE_COUNT_2_BIT = 2
VK_SAMPLE_COUNT_4_BIT = 4
VK_SAMPLE_COUNT_8_BIT = 8
VK_SAMPLE_COUNT_16_BIT = 16
VK_SAMPLE_COUNT_32_BIT = 32
VK_SAMPLE_COUNT_64_BIT = 64


# VkAttachmentDescriptionFlagBits
VK_ATTACHMENT_DESCRIPTION_MAY_ALIAS_BIT = 1


# VkStencilFaceFlagBits
VK_STENCIL_FACE_FRONT_BIT = 1
VK_STENCIL_FACE_BACK_BIT = 2
VK_STENCIL_FACE_FRONT_AND_BACK = 0x00000003
VK_STENCIL_FRONT_AND_BACK = VK_STENCIL_FACE_FRONT_AND_BACK


# VkDescriptorPoolCreateFlagBits
VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT = 1


# VkDependencyFlagBits
VK_DEPENDENCY_BY_REGION_BIT = 1


# VkSemaphoreType
VK_SEMAPHORE_TYPE_BINARY = 0
VK_SEMAPHORE_TYPE_TIMELINE = 1


# VkSemaphoreWaitFlagBits
VK_SEMAPHORE_WAIT_ANY_BIT = 1


# VkPresentModeKHR
VK_PRESENT_MODE_IMMEDIATE_KHR = 0
VK_PRESENT_MODE_MAILBOX_KHR = 1
VK_PRESENT_MODE_FIFO_KHR = 2
VK_PRESENT_MODE_FIFO_RELAXED_KHR = 3


# VkColorSpaceKHR
VK_COLOR_SPACE_SRGB_NONLINEAR_KHR = 0
VK_COLORSPACE_SRGB_NONLINEAR_KHR = VK_COLOR_SPACE_SRGB_NONLINEAR_KHR


# VkDisplayPlaneAlphaFlagBitsKHR
VK_DISPLAY_PLANE_ALPHA_OPAQUE_BIT_KHR = 1
VK_DISPLAY_PLANE_ALPHA_GLOBAL_BIT_KHR = 2
VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_BIT_KHR = 4
VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_PREMULTIPLIED_BIT_KHR = 8


# VkCompositeAlphaFlagBitsKHR
VK_COMPOSITE_ALPHA_OPAQUE_BIT_KHR = 1
VK_COMPOSITE_ALPHA_PRE_MULTIPLIED_BIT_KHR = 2
VK_COMPOSITE_ALPHA_POST_MULTIPLIED_BIT_KHR = 4
VK_COMPOSITE_ALPHA_INHERIT_BIT_KHR = 8


# VkSurfaceTransformFlagBitsKHR
VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR = 1
VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR = 2
VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR = 4
VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR = 8
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_BIT_KHR = 16
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_90_BIT_KHR = 32
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_180_BIT_KHR = 64
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_270_BIT_KHR = 128
VK_SURFACE_TRANSFORM_INHERIT_BIT_KHR = 256


# VkSwapchainImageUsageFlagBitsANDROID
VK_SWAPCHAIN_IMAGE_USAGE_SHARED_BIT_ANDROID = 1


# VkTimeDomainEXT
VK_TIME_DOMAIN_DEVICE_EXT = 0
VK_TIME_DOMAIN_CLOCK_MONOTONIC_EXT = 1
VK_TIME_DOMAIN_CLOCK_MONOTONIC_RAW_EXT = 2
VK_TIME_DOMAIN_QUERY_PERFORMANCE_COUNTER_EXT = 3


# VkDebugReportFlagBitsEXT
VK_DEBUG_REPORT_INFORMATION_BIT_EXT = 1
VK_DEBUG_REPORT_WARNING_BIT_EXT = 2
VK_DEBUG_REPORT_PERFORMANCE_WARNING_BIT_EXT = 4
VK_DEBUG_REPORT_ERROR_BIT_EXT = 8
VK_DEBUG_REPORT_DEBUG_BIT_EXT = 16


# VkDebugReportObjectTypeEXT
VK_DEBUG_REPORT_OBJECT_TYPE_UNKNOWN_EXT = 0
VK_DEBUG_REPORT_OBJECT_TYPE_INSTANCE_EXT = 1
VK_DEBUG_REPORT_OBJECT_TYPE_PHYSICAL_DEVICE_EXT = 2
VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_EXT = 3
VK_DEBUG_REPORT_OBJECT_TYPE_QUEUE_EXT = 4
VK_DEBUG_REPORT_OBJECT_TYPE_SEMAPHORE_EXT = 5
VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_BUFFER_EXT = 6
VK_DEBUG_REPORT_OBJECT_TYPE_FENCE_EXT = 7
VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_MEMORY_EXT = 8
VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_EXT = 9
VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_EXT = 10
VK_DEBUG_REPORT_OBJECT_TYPE_EVENT_EXT = 11
VK_DEBUG_REPORT_OBJECT_TYPE_QUERY_POOL_EXT = 12
VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_VIEW_EXT = 13
VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_VIEW_EXT = 14
VK_DEBUG_REPORT_OBJECT_TYPE_SHADER_MODULE_EXT = 15
VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_CACHE_EXT = 16
VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_LAYOUT_EXT = 17
VK_DEBUG_REPORT_OBJECT_TYPE_RENDER_PASS_EXT = 18
VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_EXT = 19
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT_EXT = 20
VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_EXT = 21
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_POOL_EXT = 22
VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_EXT = 23
VK_DEBUG_REPORT_OBJECT_TYPE_FRAMEBUFFER_EXT = 24
VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_POOL_EXT = 25
VK_DEBUG_REPORT_OBJECT_TYPE_SURFACE_KHR_EXT = 26
VK_DEBUG_REPORT_OBJECT_TYPE_SWAPCHAIN_KHR_EXT = 27
VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT = 28
VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT
VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_KHR_EXT = 29
VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_MODE_KHR_EXT = 30
VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT = 33
VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT


# VkDeviceMemoryReportEventTypeEXT
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATE_EXT = 0
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_FREE_EXT = 1
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_IMPORT_EXT = 2
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_UNIMPORT_EXT = 3
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATION_FAILED_EXT = 4


# VkRasterizationOrderAMD
VK_RASTERIZATION_ORDER_STRICT_AMD = 0
VK_RASTERIZATION_ORDER_RELAXED_AMD = 1


# VkExternalMemoryHandleTypeFlagBitsNV
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT_NV = 1
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_NV = 2
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_BIT_NV = 4
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_KMT_BIT_NV = 8


# VkExternalMemoryFeatureFlagBitsNV
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_NV = 1
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_NV = 2
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_NV = 4


# VkValidationCheckEXT
VK_VALIDATION_CHECK_ALL_EXT = 0
VK_VALIDATION_CHECK_SHADERS_EXT = 1


# VkValidationFeatureEnableEXT
VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_EXT = 0
VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_RESERVE_BINDING_SLOT_EXT = 1
VK_VALIDATION_FEATURE_ENABLE_BEST_PRACTICES_EXT = 2
VK_VALIDATION_FEATURE_ENABLE_DEBUG_PRINTF_EXT = 3
VK_VALIDATION_FEATURE_ENABLE_SYNCHRONIZATION_VALIDATION_EXT = 4


# VkValidationFeatureDisableEXT
VK_VALIDATION_FEATURE_DISABLE_ALL_EXT = 0
VK_VALIDATION_FEATURE_DISABLE_SHADERS_EXT = 1
VK_VALIDATION_FEATURE_DISABLE_THREAD_SAFETY_EXT = 2
VK_VALIDATION_FEATURE_DISABLE_API_PARAMETERS_EXT = 3
VK_VALIDATION_FEATURE_DISABLE_OBJECT_LIFETIMES_EXT = 4
VK_VALIDATION_FEATURE_DISABLE_CORE_CHECKS_EXT = 5
VK_VALIDATION_FEATURE_DISABLE_UNIQUE_HANDLES_EXT = 6


# VkSubgroupFeatureFlagBits
VK_SUBGROUP_FEATURE_BASIC_BIT = 1
VK_SUBGROUP_FEATURE_VOTE_BIT = 2
VK_SUBGROUP_FEATURE_ARITHMETIC_BIT = 4
VK_SUBGROUP_FEATURE_BALLOT_BIT = 8
VK_SUBGROUP_FEATURE_SHUFFLE_BIT = 16
VK_SUBGROUP_FEATURE_SHUFFLE_RELATIVE_BIT = 32
VK_SUBGROUP_FEATURE_CLUSTERED_BIT = 64
VK_SUBGROUP_FEATURE_QUAD_BIT = 128


# VkIndirectCommandsLayoutUsageFlagBitsNV
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_EXPLICIT_PREPROCESS_BIT_NV = 1
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_INDEXED_SEQUENCES_BIT_NV = 2
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_UNORDERED_SEQUENCES_BIT_NV = 4


# VkIndirectStateFlagBitsNV
VK_INDIRECT_STATE_FLAG_FRONTFACE_BIT_NV = 1


# VkIndirectCommandsTokenTypeNV
VK_INDIRECT_COMMANDS_TOKEN_TYPE_SHADER_GROUP_NV = 0
VK_INDIRECT_COMMANDS_TOKEN_TYPE_STATE_FLAGS_NV = 1
VK_INDIRECT_COMMANDS_TOKEN_TYPE_INDEX_BUFFER_NV = 2
VK_INDIRECT_COMMANDS_TOKEN_TYPE_VERTEX_BUFFER_NV = 3
VK_INDIRECT_COMMANDS_TOKEN_TYPE_PUSH_CONSTANT_NV = 4
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_INDEXED_NV = 5
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_NV = 6
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_TASKS_NV = 7


# VkPrivateDataSlotCreateFlagBitsEXT


# VkDescriptorSetLayoutCreateFlagBits


# VkExternalMemoryHandleTypeFlagBits
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT = 1
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT = 2
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = 4
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_BIT = 8
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_KMT_BIT = 16
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP_BIT = 32
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE_BIT = 64


# VkExternalMemoryFeatureFlagBits
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT = 1
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT = 2
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT = 4


# VkExternalSemaphoreHandleTypeFlagBits
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT = 1
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT = 2
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = 4
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT = 8
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_FENCE_BIT = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_SYNC_FD_BIT = 16


# VkExternalSemaphoreFeatureFlagBits
VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT = 1
VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT = 2


# VkSemaphoreImportFlagBits
VK_SEMAPHORE_IMPORT_TEMPORARY_BIT = 1


# VkExternalFenceHandleTypeFlagBits
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT = 1
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT = 2
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = 4
VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT = 8


# VkExternalFenceFeatureFlagBits
VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT = 1
VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT = 2


# VkFenceImportFlagBits
VK_FENCE_IMPORT_TEMPORARY_BIT = 1


# VkSurfaceCounterFlagBitsEXT
VK_SURFACE_COUNTER_VBLANK_BIT_EXT = 1
VK_SURFACE_COUNTER_VBLANK_EXT = VK_SURFACE_COUNTER_VBLANK_BIT_EXT


# VkDisplayPowerStateEXT
VK_DISPLAY_POWER_STATE_OFF_EXT = 0
VK_DISPLAY_POWER_STATE_SUSPEND_EXT = 1
VK_DISPLAY_POWER_STATE_ON_EXT = 2


# VkDeviceEventTypeEXT
VK_DEVICE_EVENT_TYPE_DISPLAY_HOTPLUG_EXT = 0


# VkDisplayEventTypeEXT
VK_DISPLAY_EVENT_TYPE_FIRST_PIXEL_OUT_EXT = 0


# VkPeerMemoryFeatureFlagBits
VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT = 1
VK_PEER_MEMORY_FEATURE_COPY_DST_BIT = 2
VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT = 4
VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT = 8


# VkMemoryAllocateFlagBits
VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT = 1


# VkDeviceGroupPresentModeFlagBitsKHR
VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_BIT_KHR = 1
VK_DEVICE_GROUP_PRESENT_MODE_REMOTE_BIT_KHR = 2
VK_DEVICE_GROUP_PRESENT_MODE_SUM_BIT_KHR = 4
VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_MULTI_DEVICE_BIT_KHR = 8


# VkSwapchainCreateFlagBitsKHR


# VkViewportCoordinateSwizzleNV
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_X_NV = 0
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_X_NV = 1
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Y_NV = 2
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Y_NV = 3
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Z_NV = 4
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Z_NV = 5
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_W_NV = 6
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_W_NV = 7


# VkDiscardRectangleModeEXT
VK_DISCARD_RECTANGLE_MODE_INCLUSIVE_EXT = 0
VK_DISCARD_RECTANGLE_MODE_EXCLUSIVE_EXT = 1


# VkSubpassDescriptionFlagBits


# VkPointClippingBehavior
VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES = 0
VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY = 1


# VkSamplerReductionMode
VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE = 0
VK_SAMPLER_REDUCTION_MODE_MIN = 1
VK_SAMPLER_REDUCTION_MODE_MAX = 2


# VkTessellationDomainOrigin
VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT = 0
VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT = 1


# VkSamplerYcbcrModelConversion
VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY = 0
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY = 1
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709 = 2
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601 = 3
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020 = 4


# VkSamplerYcbcrRange
VK_SAMPLER_YCBCR_RANGE_ITU_FULL = 0
VK_SAMPLER_YCBCR_RANGE_ITU_NARROW = 1


# VkChromaLocation
VK_CHROMA_LOCATION_COSITED_EVEN = 0
VK_CHROMA_LOCATION_MIDPOINT = 1


# VkBlendOverlapEXT
VK_BLEND_OVERLAP_UNCORRELATED_EXT = 0
VK_BLEND_OVERLAP_DISJOINT_EXT = 1
VK_BLEND_OVERLAP_CONJOINT_EXT = 2


# VkCoverageModulationModeNV
VK_COVERAGE_MODULATION_MODE_NONE_NV = 0
VK_COVERAGE_MODULATION_MODE_RGB_NV = 1
VK_COVERAGE_MODULATION_MODE_ALPHA_NV = 2
VK_COVERAGE_MODULATION_MODE_RGBA_NV = 3


# VkCoverageReductionModeNV
VK_COVERAGE_REDUCTION_MODE_MERGE_NV = 0
VK_COVERAGE_REDUCTION_MODE_TRUNCATE_NV = 1


# VkValidationCacheHeaderVersionEXT
VK_VALIDATION_CACHE_HEADER_VERSION_ONE_EXT = 1


# VkShaderInfoTypeAMD
VK_SHADER_INFO_TYPE_STATISTICS_AMD = 0
VK_SHADER_INFO_TYPE_BINARY_AMD = 1
VK_SHADER_INFO_TYPE_DISASSEMBLY_AMD = 2


# VkQueueGlobalPriorityEXT
VK_QUEUE_GLOBAL_PRIORITY_LOW_EXT = 128
VK_QUEUE_GLOBAL_PRIORITY_MEDIUM_EXT = 256
VK_QUEUE_GLOBAL_PRIORITY_HIGH_EXT = 512
VK_QUEUE_GLOBAL_PRIORITY_REALTIME_EXT = 1024


# VkDebugUtilsMessageSeverityFlagBitsEXT
VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT = 1
VK_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT = 16
VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT = 256
VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT = 4096


# VkDebugUtilsMessageTypeFlagBitsEXT
VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT = 1
VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT = 2
VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT = 4


# VkConservativeRasterizationModeEXT
VK_CONSERVATIVE_RASTERIZATION_MODE_DISABLED_EXT = 0
VK_CONSERVATIVE_RASTERIZATION_MODE_OVERESTIMATE_EXT = 1
VK_CONSERVATIVE_RASTERIZATION_MODE_UNDERESTIMATE_EXT = 2


# VkDescriptorBindingFlagBits
VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT = 1
VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT = 2
VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT = 4
VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT = 8


# VkVendorId
VK_VENDOR_ID_VIV = 0x10001
VK_VENDOR_ID_VSI = 0x10002
VK_VENDOR_ID_KAZAN = 0x10003
VK_VENDOR_ID_CODEPLAY = 0x10004
VK_VENDOR_ID_MESA = 0x10005


# VkDriverId
VK_DRIVER_ID_AMD_PROPRIETARY = 1
VK_DRIVER_ID_AMD_OPEN_SOURCE = 2
VK_DRIVER_ID_MESA_RADV = 3
VK_DRIVER_ID_NVIDIA_PROPRIETARY = 4
VK_DRIVER_ID_INTEL_PROPRIETARY_WINDOWS = 5
VK_DRIVER_ID_INTEL_OPEN_SOURCE_MESA = 6
VK_DRIVER_ID_IMAGINATION_PROPRIETARY = 7
VK_DRIVER_ID_QUALCOMM_PROPRIETARY = 8
VK_DRIVER_ID_ARM_PROPRIETARY = 9
VK_DRIVER_ID_GOOGLE_SWIFTSHADER = 10
VK_DRIVER_ID_GGP_PROPRIETARY = 11
VK_DRIVER_ID_BROADCOM_PROPRIETARY = 12
VK_DRIVER_ID_MESA_LLVMPIPE = 13
VK_DRIVER_ID_MOLTENVK = 14


# VkConditionalRenderingFlagBitsEXT
VK_CONDITIONAL_RENDERING_INVERTED_BIT_EXT = 1


# VkResolveModeFlagBits
VK_RESOLVE_MODE_NONE = 0
VK_RESOLVE_MODE_SAMPLE_ZERO_BIT = 1
VK_RESOLVE_MODE_AVERAGE_BIT = 2
VK_RESOLVE_MODE_MIN_BIT = 4
VK_RESOLVE_MODE_MAX_BIT = 8


# VkShadingRatePaletteEntryNV
VK_SHADING_RATE_PALETTE_ENTRY_NO_INVOCATIONS_NV = 0
VK_SHADING_RATE_PALETTE_ENTRY_16_INVOCATIONS_PER_PIXEL_NV = 1
VK_SHADING_RATE_PALETTE_ENTRY_8_INVOCATIONS_PER_PIXEL_NV = 2
VK_SHADING_RATE_PALETTE_ENTRY_4_INVOCATIONS_PER_PIXEL_NV = 3
VK_SHADING_RATE_PALETTE_ENTRY_2_INVOCATIONS_PER_PIXEL_NV = 4
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_PIXEL_NV = 5
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X1_PIXELS_NV = 6
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_1X2_PIXELS_NV = 7
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X2_PIXELS_NV = 8
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_4X2_PIXELS_NV = 9
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_2X4_PIXELS_NV = 10
VK_SHADING_RATE_PALETTE_ENTRY_1_INVOCATION_PER_4X4_PIXELS_NV = 11


# VkCoarseSampleOrderTypeNV
VK_COARSE_SAMPLE_ORDER_TYPE_DEFAULT_NV = 0
VK_COARSE_SAMPLE_ORDER_TYPE_CUSTOM_NV = 1
VK_COARSE_SAMPLE_ORDER_TYPE_PIXEL_MAJOR_NV = 2
VK_COARSE_SAMPLE_ORDER_TYPE_SAMPLE_MAJOR_NV = 3


# VkGeometryInstanceFlagBitsKHR
VK_GEOMETRY_INSTANCE_TRIANGLE_FACING_CULL_DISABLE_BIT_KHR = 1
VK_GEOMETRY_INSTANCE_TRIANGLE_FRONT_COUNTERCLOCKWISE_BIT_KHR = 2
VK_GEOMETRY_INSTANCE_FORCE_OPAQUE_BIT_KHR = 4
VK_GEOMETRY_INSTANCE_FORCE_NO_OPAQUE_BIT_KHR = 8


# VkGeometryFlagBitsKHR
VK_GEOMETRY_OPAQUE_BIT_KHR = 1
VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR = 2


# VkBuildAccelerationStructureFlagBitsKHR
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT_KHR = 1
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT_KHR = 2
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT_KHR = 4
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT_KHR = 8
VK_BUILD_ACCELERATION_STRUCTURE_LOW_MEMORY_BIT_KHR = 16


# VkAccelerationStructureCreateFlagBitsKHR
VK_ACCELERATION_STRUCTURE_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = 1


# VkCopyAccelerationStructureModeKHR
VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_KHR = 0
VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_KHR = 1
VK_COPY_ACCELERATION_STRUCTURE_MODE_SERIALIZE_KHR = 2
VK_COPY_ACCELERATION_STRUCTURE_MODE_DESERIALIZE_KHR = 3


# VkBuildAccelerationStructureModeKHR
VK_BUILD_ACCELERATION_STRUCTURE_MODE_BUILD_KHR = 0
VK_BUILD_ACCELERATION_STRUCTURE_MODE_UPDATE_KHR = 1


# VkAccelerationStructureTypeKHR
VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR = 0
VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR = 1
VK_ACCELERATION_STRUCTURE_TYPE_GENERIC_KHR = 2


# VkGeometryTypeKHR
VK_GEOMETRY_TYPE_TRIANGLES_KHR = 0
VK_GEOMETRY_TYPE_AABBS_KHR = 1
VK_GEOMETRY_TYPE_INSTANCES_KHR = 2


# VkAccelerationStructureMemoryRequirementsTypeNV
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_OBJECT_NV = 0
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_BUILD_SCRATCH_NV = 1
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_UPDATE_SCRATCH_NV = 2


# VkAccelerationStructureBuildTypeKHR
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_KHR = 0
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR = 1
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_OR_DEVICE_KHR = 2


# VkRayTracingShaderGroupTypeKHR
VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_KHR = 0
VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_KHR = 1
VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_KHR = 2


# VkAccelerationStructureCompatibilityKHR
VK_ACCELERATION_STRUCTURE_COMPATIBILITY_COMPATIBLE_KHR = 0
VK_ACCELERATION_STRUCTURE_COMPATIBILITY_INCOMPATIBLE_KHR = 1


# VkShaderGroupShaderKHR
VK_SHADER_GROUP_SHADER_GENERAL_KHR = 0
VK_SHADER_GROUP_SHADER_CLOSEST_HIT_KHR = 1
VK_SHADER_GROUP_SHADER_ANY_HIT_KHR = 2
VK_SHADER_GROUP_SHADER_INTERSECTION_KHR = 3


# VkMemoryOverallocationBehaviorAMD
VK_MEMORY_OVERALLOCATION_BEHAVIOR_DEFAULT_AMD = 0
VK_MEMORY_OVERALLOCATION_BEHAVIOR_ALLOWED_AMD = 1
VK_MEMORY_OVERALLOCATION_BEHAVIOR_DISALLOWED_AMD = 2


# VkFramebufferCreateFlagBits


# VkScopeNV
VK_SCOPE_DEVICE_NV = 1
VK_SCOPE_WORKGROUP_NV = 2
VK_SCOPE_SUBGROUP_NV = 3
VK_SCOPE_QUEUE_FAMILY_NV = 5


# VkComponentTypeNV
VK_COMPONENT_TYPE_FLOAT16_NV = 0
VK_COMPONENT_TYPE_FLOAT32_NV = 1
VK_COMPONENT_TYPE_FLOAT64_NV = 2
VK_COMPONENT_TYPE_SINT8_NV = 3
VK_COMPONENT_TYPE_SINT16_NV = 4
VK_COMPONENT_TYPE_SINT32_NV = 5
VK_COMPONENT_TYPE_SINT64_NV = 6
VK_COMPONENT_TYPE_UINT8_NV = 7
VK_COMPONENT_TYPE_UINT16_NV = 8
VK_COMPONENT_TYPE_UINT32_NV = 9
VK_COMPONENT_TYPE_UINT64_NV = 10


# VkDeviceDiagnosticsConfigFlagBitsNV
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_SHADER_DEBUG_INFO_BIT_NV = 1
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_RESOURCE_TRACKING_BIT_NV = 2
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_AUTOMATIC_CHECKPOINTS_BIT_NV = 4


# VkPipelineCreationFeedbackFlagBitsEXT
VK_PIPELINE_CREATION_FEEDBACK_VALID_BIT_EXT = 1
VK_PIPELINE_CREATION_FEEDBACK_APPLICATION_PIPELINE_CACHE_HIT_BIT_EXT = 2
VK_PIPELINE_CREATION_FEEDBACK_BASE_PIPELINE_ACCELERATION_BIT_EXT = 4


# VkFullScreenExclusiveEXT
VK_FULL_SCREEN_EXCLUSIVE_DEFAULT_EXT = 0
VK_FULL_SCREEN_EXCLUSIVE_ALLOWED_EXT = 1
VK_FULL_SCREEN_EXCLUSIVE_DISALLOWED_EXT = 2
VK_FULL_SCREEN_EXCLUSIVE_APPLICATION_CONTROLLED_EXT = 3


# VkPerformanceCounterScopeKHR
VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR = 0
VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR = 1
VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR = 2
VK_QUERY_SCOPE_COMMAND_BUFFER_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR
VK_QUERY_SCOPE_RENDER_PASS_KHR = VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR
VK_QUERY_SCOPE_COMMAND_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR


# VkPerformanceCounterUnitKHR
VK_PERFORMANCE_COUNTER_UNIT_GENERIC_KHR = 0
VK_PERFORMANCE_COUNTER_UNIT_PERCENTAGE_KHR = 1
VK_PERFORMANCE_COUNTER_UNIT_NANOSECONDS_KHR = 2
VK_PERFORMANCE_COUNTER_UNIT_BYTES_KHR = 3
VK_PERFORMANCE_COUNTER_UNIT_BYTES_PER_SECOND_KHR = 4
VK_PERFORMANCE_COUNTER_UNIT_KELVIN_KHR = 5
VK_PERFORMANCE_COUNTER_UNIT_WATTS_KHR = 6
VK_PERFORMANCE_COUNTER_UNIT_VOLTS_KHR = 7
VK_PERFORMANCE_COUNTER_UNIT_AMPS_KHR = 8
VK_PERFORMANCE_COUNTER_UNIT_HERTZ_KHR = 9
VK_PERFORMANCE_COUNTER_UNIT_CYCLES_KHR = 10


# VkPerformanceCounterStorageKHR
VK_PERFORMANCE_COUNTER_STORAGE_INT32_KHR = 0
VK_PERFORMANCE_COUNTER_STORAGE_INT64_KHR = 1
VK_PERFORMANCE_COUNTER_STORAGE_UINT32_KHR = 2
VK_PERFORMANCE_COUNTER_STORAGE_UINT64_KHR = 3
VK_PERFORMANCE_COUNTER_STORAGE_FLOAT32_KHR = 4
VK_PERFORMANCE_COUNTER_STORAGE_FLOAT64_KHR = 5


# VkPerformanceCounterDescriptionFlagBitsKHR
VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR = 1
VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_KHR = VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR
VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR = 2
VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_KHR = VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR


# VkAcquireProfilingLockFlagBitsKHR


# VkShaderCorePropertiesFlagBitsAMD


# VkPerformanceConfigurationTypeINTEL
VK_PERFORMANCE_CONFIGURATION_TYPE_COMMAND_QUEUE_METRICS_DISCOVERY_ACTIVATED_INTEL = 0


# VkQueryPoolSamplingModeINTEL
VK_QUERY_POOL_SAMPLING_MODE_MANUAL_INTEL = 0


# VkPerformanceOverrideTypeINTEL
VK_PERFORMANCE_OVERRIDE_TYPE_NULL_HARDWARE_INTEL = 0
VK_PERFORMANCE_OVERRIDE_TYPE_FLUSH_GPU_CACHES_INTEL = 1


# VkPerformanceParameterTypeINTEL
VK_PERFORMANCE_PARAMETER_TYPE_HW_COUNTERS_SUPPORTED_INTEL = 0
VK_PERFORMANCE_PARAMETER_TYPE_STREAM_MARKER_VALID_BITS_INTEL = 1


# VkPerformanceValueTypeINTEL
VK_PERFORMANCE_VALUE_TYPE_UINT32_INTEL = 0
VK_PERFORMANCE_VALUE_TYPE_UINT64_INTEL = 1
VK_PERFORMANCE_VALUE_TYPE_FLOAT_INTEL = 2
VK_PERFORMANCE_VALUE_TYPE_BOOL_INTEL = 3
VK_PERFORMANCE_VALUE_TYPE_STRING_INTEL = 4


# VkShaderFloatControlsIndependence
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY = 0
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL = 1
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE = 2


# VkPipelineExecutableStatisticFormatKHR
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_BOOL32_KHR = 0
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_INT64_KHR = 1
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_UINT64_KHR = 2
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_FLOAT64_KHR = 3


# VkLineRasterizationModeEXT
VK_LINE_RASTERIZATION_MODE_DEFAULT_EXT = 0
VK_LINE_RASTERIZATION_MODE_RECTANGULAR_EXT = 1
VK_LINE_RASTERIZATION_MODE_BRESENHAM_EXT = 2
VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_EXT = 3


# VkShaderModuleCreateFlagBits


# VkPipelineCompilerControlFlagBitsAMD


# VkToolPurposeFlagBitsEXT
VK_TOOL_PURPOSE_VALIDATION_BIT_EXT = 1
VK_TOOL_PURPOSE_PROFILING_BIT_EXT = 2
VK_TOOL_PURPOSE_TRACING_BIT_EXT = 4
VK_TOOL_PURPOSE_ADDITIONAL_FEATURES_BIT_EXT = 8
VK_TOOL_PURPOSE_MODIFYING_FEATURES_BIT_EXT = 16


# VkFragmentShadingRateCombinerOpKHR
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_KEEP_KHR = 0
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_REPLACE_KHR = 1
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MIN_KHR = 2
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR = 3
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MUL_KHR = 4


# VkFragmentShadingRateNV
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV = 0
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV = 1
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV = 4
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV = 5
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV = 6
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV = 9
VK_FRAGMENT_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV = 10
VK_FRAGMENT_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV = 11
VK_FRAGMENT_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV = 12
VK_FRAGMENT_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV = 13
VK_FRAGMENT_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV = 14
VK_FRAGMENT_SHADING_RATE_NO_INVOCATIONS_NV = 15


# VkFragmentShadingRateTypeNV
VK_FRAGMENT_SHADING_RATE_TYPE_FRAGMENT_SIZE_NV = 0
VK_FRAGMENT_SHADING_RATE_TYPE_ENUMS_NV = 1
