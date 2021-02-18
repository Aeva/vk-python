

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


# ENUM TYPES
VkAttachmentLoadOp = type('VkAttachmentLoadOp', (ctypes.c_int,), dict())
VkAttachmentStoreOp = type('VkAttachmentStoreOp', (ctypes.c_int,), dict())
VkBlendFactor = type('VkBlendFactor', (ctypes.c_int,), dict())
VkBlendOp = type('VkBlendOp', (ctypes.c_int,), dict())
VkBorderColor = type('VkBorderColor', (ctypes.c_int,), dict())
VkFramebufferCreateFlagBits = type('VkFramebufferCreateFlagBits', (ctypes.c_int,), dict())
VkQueryPoolCreateFlagBits = type('VkQueryPoolCreateFlagBits', (ctypes.c_int,), dict())
VkRenderPassCreateFlagBits = type('VkRenderPassCreateFlagBits', (ctypes.c_int,), dict())
VkSamplerCreateFlagBits = type('VkSamplerCreateFlagBits', (ctypes.c_int,), dict())
VkPipelineCacheHeaderVersion = type('VkPipelineCacheHeaderVersion', (ctypes.c_int,), dict())
VkPipelineCacheCreateFlagBits = type('VkPipelineCacheCreateFlagBits', (ctypes.c_int,), dict())
VkPipelineShaderStageCreateFlagBits = type('VkPipelineShaderStageCreateFlagBits', (ctypes.c_int,), dict())
VkDescriptorSetLayoutCreateFlagBits = type('VkDescriptorSetLayoutCreateFlagBits', (ctypes.c_int,), dict())
VkInstanceCreateFlagBits = type('VkInstanceCreateFlagBits', (ctypes.c_int,), dict())
VkDeviceQueueCreateFlagBits = type('VkDeviceQueueCreateFlagBits', (ctypes.c_int,), dict())
VkBufferCreateFlagBits = type('VkBufferCreateFlagBits', (ctypes.c_int,), dict())
VkBufferUsageFlagBits = type('VkBufferUsageFlagBits', (ctypes.c_int,), dict())
VkColorComponentFlagBits = type('VkColorComponentFlagBits', (ctypes.c_int,), dict())
VkComponentSwizzle = type('VkComponentSwizzle', (ctypes.c_int,), dict())
VkCommandPoolCreateFlagBits = type('VkCommandPoolCreateFlagBits', (ctypes.c_int,), dict())
VkCommandPoolResetFlagBits = type('VkCommandPoolResetFlagBits', (ctypes.c_int,), dict())
VkCommandBufferResetFlagBits = type('VkCommandBufferResetFlagBits', (ctypes.c_int,), dict())
VkCommandBufferLevel = type('VkCommandBufferLevel', (ctypes.c_int,), dict())
VkCommandBufferUsageFlagBits = type('VkCommandBufferUsageFlagBits', (ctypes.c_int,), dict())
VkCompareOp = type('VkCompareOp', (ctypes.c_int,), dict())
VkCullModeFlagBits = type('VkCullModeFlagBits', (ctypes.c_int,), dict())
VkDescriptorType = type('VkDescriptorType', (ctypes.c_int,), dict())
VkDeviceCreateFlagBits = type('VkDeviceCreateFlagBits', (ctypes.c_int,), dict())
VkDynamicState = type('VkDynamicState', (ctypes.c_int,), dict())
VkFenceCreateFlagBits = type('VkFenceCreateFlagBits', (ctypes.c_int,), dict())
VkPolygonMode = type('VkPolygonMode', (ctypes.c_int,), dict())
VkFormat = type('VkFormat', (ctypes.c_int,), dict())
VkFormatFeatureFlagBits = type('VkFormatFeatureFlagBits', (ctypes.c_int,), dict())
VkFrontFace = type('VkFrontFace', (ctypes.c_int,), dict())
VkImageAspectFlagBits = type('VkImageAspectFlagBits', (ctypes.c_int,), dict())
VkImageCreateFlagBits = type('VkImageCreateFlagBits', (ctypes.c_int,), dict())
VkImageLayout = type('VkImageLayout', (ctypes.c_int,), dict())
VkImageTiling = type('VkImageTiling', (ctypes.c_int,), dict())
VkImageType = type('VkImageType', (ctypes.c_int,), dict())
VkImageUsageFlagBits = type('VkImageUsageFlagBits', (ctypes.c_int,), dict())
VkImageViewCreateFlagBits = type('VkImageViewCreateFlagBits', (ctypes.c_int,), dict())
VkImageViewType = type('VkImageViewType', (ctypes.c_int,), dict())
VkSharingMode = type('VkSharingMode', (ctypes.c_int,), dict())
VkIndexType = type('VkIndexType', (ctypes.c_int,), dict())
VkLogicOp = type('VkLogicOp', (ctypes.c_int,), dict())
VkMemoryHeapFlagBits = type('VkMemoryHeapFlagBits', (ctypes.c_int,), dict())
VkAccessFlagBits = type('VkAccessFlagBits', (ctypes.c_int,), dict())
VkMemoryPropertyFlagBits = type('VkMemoryPropertyFlagBits', (ctypes.c_int,), dict())
VkPhysicalDeviceType = type('VkPhysicalDeviceType', (ctypes.c_int,), dict())
VkPipelineBindPoint = type('VkPipelineBindPoint', (ctypes.c_int,), dict())
VkPipelineCreateFlagBits = type('VkPipelineCreateFlagBits', (ctypes.c_int,), dict())
VkPrimitiveTopology = type('VkPrimitiveTopology', (ctypes.c_int,), dict())
VkQueryControlFlagBits = type('VkQueryControlFlagBits', (ctypes.c_int,), dict())
VkQueryPipelineStatisticFlagBits = type('VkQueryPipelineStatisticFlagBits', (ctypes.c_int,), dict())
VkQueryResultFlagBits = type('VkQueryResultFlagBits', (ctypes.c_int,), dict())
VkQueryType = type('VkQueryType', (ctypes.c_int,), dict())
VkQueueFlagBits = type('VkQueueFlagBits', (ctypes.c_int,), dict())
VkSubpassContents = type('VkSubpassContents', (ctypes.c_int,), dict())
VkResult = type('VkResult', (ctypes.c_int,), dict())
VkShaderStageFlagBits = type('VkShaderStageFlagBits', (ctypes.c_int,), dict())
VkSparseMemoryBindFlagBits = type('VkSparseMemoryBindFlagBits', (ctypes.c_int,), dict())
VkStencilFaceFlagBits = type('VkStencilFaceFlagBits', (ctypes.c_int,), dict())
VkStencilOp = type('VkStencilOp', (ctypes.c_int,), dict())
VkStructureType = type('VkStructureType', (ctypes.c_int,), dict())
VkSystemAllocationScope = type('VkSystemAllocationScope', (ctypes.c_int,), dict())
VkInternalAllocationType = type('VkInternalAllocationType', (ctypes.c_int,), dict())
VkSamplerAddressMode = type('VkSamplerAddressMode', (ctypes.c_int,), dict())
VkFilter = type('VkFilter', (ctypes.c_int,), dict())
VkSamplerMipmapMode = type('VkSamplerMipmapMode', (ctypes.c_int,), dict())
VkVertexInputRate = type('VkVertexInputRate', (ctypes.c_int,), dict())
VkPipelineStageFlagBits = type('VkPipelineStageFlagBits', (ctypes.c_int,), dict())
VkSparseImageFormatFlagBits = type('VkSparseImageFormatFlagBits', (ctypes.c_int,), dict())
VkSampleCountFlagBits = type('VkSampleCountFlagBits', (ctypes.c_int,), dict())
VkAttachmentDescriptionFlagBits = type('VkAttachmentDescriptionFlagBits', (ctypes.c_int,), dict())
VkDescriptorPoolCreateFlagBits = type('VkDescriptorPoolCreateFlagBits', (ctypes.c_int,), dict())
VkDependencyFlagBits = type('VkDependencyFlagBits', (ctypes.c_int,), dict())
VkObjectType = type('VkObjectType', (ctypes.c_int,), dict())
VkIndirectCommandsLayoutUsageFlagBitsNV = type('VkIndirectCommandsLayoutUsageFlagBitsNV', (ctypes.c_int,), dict())
VkIndirectCommandsTokenTypeNV = type('VkIndirectCommandsTokenTypeNV', (ctypes.c_int,), dict())
VkIndirectStateFlagBitsNV = type('VkIndirectStateFlagBitsNV', (ctypes.c_int,), dict())
VkPrivateDataSlotCreateFlagBitsEXT = type('VkPrivateDataSlotCreateFlagBitsEXT', (ctypes.c_int,), dict())
VkDescriptorUpdateTemplateType = type('VkDescriptorUpdateTemplateType', (ctypes.c_int,), dict())
VkDescriptorUpdateTemplateTypeKHR = VkDescriptorUpdateTemplateType
VkViewportCoordinateSwizzleNV = type('VkViewportCoordinateSwizzleNV', (ctypes.c_int,), dict())
VkDiscardRectangleModeEXT = type('VkDiscardRectangleModeEXT', (ctypes.c_int,), dict())
VkSubpassDescriptionFlagBits = type('VkSubpassDescriptionFlagBits', (ctypes.c_int,), dict())
VkPointClippingBehavior = type('VkPointClippingBehavior', (ctypes.c_int,), dict())
VkPointClippingBehaviorKHR = VkPointClippingBehavior
VkCoverageModulationModeNV = type('VkCoverageModulationModeNV', (ctypes.c_int,), dict())
VkCoverageReductionModeNV = type('VkCoverageReductionModeNV', (ctypes.c_int,), dict())
VkValidationCacheHeaderVersionEXT = type('VkValidationCacheHeaderVersionEXT', (ctypes.c_int,), dict())
VkShaderInfoTypeAMD = type('VkShaderInfoTypeAMD', (ctypes.c_int,), dict())
VkQueueGlobalPriorityEXT = type('VkQueueGlobalPriorityEXT', (ctypes.c_int,), dict())
VkTimeDomainEXT = type('VkTimeDomainEXT', (ctypes.c_int,), dict())
VkConservativeRasterizationModeEXT = type('VkConservativeRasterizationModeEXT', (ctypes.c_int,), dict())
VkResolveModeFlagBits = type('VkResolveModeFlagBits', (ctypes.c_int,), dict())
VkResolveModeFlagBitsKHR = VkResolveModeFlagBits
VkDescriptorBindingFlagBits = type('VkDescriptorBindingFlagBits', (ctypes.c_int,), dict())
VkDescriptorBindingFlagBitsEXT = VkDescriptorBindingFlagBits
VkConditionalRenderingFlagBitsEXT = type('VkConditionalRenderingFlagBitsEXT', (ctypes.c_int,), dict())
VkSemaphoreType = type('VkSemaphoreType', (ctypes.c_int,), dict())
VkSemaphoreTypeKHR = VkSemaphoreType
VkGeometryFlagBitsKHR = type('VkGeometryFlagBitsKHR', (ctypes.c_int,), dict())
VkGeometryFlagBitsNV = VkGeometryFlagBitsKHR
VkGeometryInstanceFlagBitsKHR = type('VkGeometryInstanceFlagBitsKHR', (ctypes.c_int,), dict())
VkGeometryInstanceFlagBitsNV = VkGeometryInstanceFlagBitsKHR
VkBuildAccelerationStructureFlagBitsKHR = type('VkBuildAccelerationStructureFlagBitsKHR', (ctypes.c_int,), dict())
VkBuildAccelerationStructureFlagBitsNV = VkBuildAccelerationStructureFlagBitsKHR
VkAccelerationStructureCreateFlagBitsKHR = type('VkAccelerationStructureCreateFlagBitsKHR', (ctypes.c_int,), dict())
VkBuildAccelerationStructureModeKHR = type('VkBuildAccelerationStructureModeKHR', (ctypes.c_int,), dict())
VkCopyAccelerationStructureModeKHR = type('VkCopyAccelerationStructureModeKHR', (ctypes.c_int,), dict())
VkCopyAccelerationStructureModeNV = VkCopyAccelerationStructureModeKHR
VkAccelerationStructureTypeKHR = type('VkAccelerationStructureTypeKHR', (ctypes.c_int,), dict())
VkAccelerationStructureTypeNV = VkAccelerationStructureTypeKHR
VkGeometryTypeKHR = type('VkGeometryTypeKHR', (ctypes.c_int,), dict())
VkGeometryTypeNV = VkGeometryTypeKHR
VkRayTracingShaderGroupTypeKHR = type('VkRayTracingShaderGroupTypeKHR', (ctypes.c_int,), dict())
VkRayTracingShaderGroupTypeNV = VkRayTracingShaderGroupTypeKHR
VkAccelerationStructureMemoryRequirementsTypeNV = type('VkAccelerationStructureMemoryRequirementsTypeNV', (ctypes.c_int,), dict())
VkAccelerationStructureBuildTypeKHR = type('VkAccelerationStructureBuildTypeKHR', (ctypes.c_int,), dict())
VkAccelerationStructureCompatibilityKHR = type('VkAccelerationStructureCompatibilityKHR', (ctypes.c_int,), dict())
VkShaderGroupShaderKHR = type('VkShaderGroupShaderKHR', (ctypes.c_int,), dict())
VkMemoryOverallocationBehaviorAMD = type('VkMemoryOverallocationBehaviorAMD', (ctypes.c_int,), dict())
VkScopeNV = type('VkScopeNV', (ctypes.c_int,), dict())
VkComponentTypeNV = type('VkComponentTypeNV', (ctypes.c_int,), dict())
VkDeviceDiagnosticsConfigFlagBitsNV = type('VkDeviceDiagnosticsConfigFlagBitsNV', (ctypes.c_int,), dict())
VkPipelineCreationFeedbackFlagBitsEXT = type('VkPipelineCreationFeedbackFlagBitsEXT', (ctypes.c_int,), dict())
VkPerformanceCounterScopeKHR = type('VkPerformanceCounterScopeKHR', (ctypes.c_int,), dict())
VkPerformanceCounterUnitKHR = type('VkPerformanceCounterUnitKHR', (ctypes.c_int,), dict())
VkPerformanceCounterStorageKHR = type('VkPerformanceCounterStorageKHR', (ctypes.c_int,), dict())
VkPerformanceCounterDescriptionFlagBitsKHR = type('VkPerformanceCounterDescriptionFlagBitsKHR', (ctypes.c_int,), dict())
VkAcquireProfilingLockFlagBitsKHR = type('VkAcquireProfilingLockFlagBitsKHR', (ctypes.c_int,), dict())
VkSemaphoreWaitFlagBits = type('VkSemaphoreWaitFlagBits', (ctypes.c_int,), dict())
VkSemaphoreWaitFlagBitsKHR = VkSemaphoreWaitFlagBits
VkPerformanceConfigurationTypeINTEL = type('VkPerformanceConfigurationTypeINTEL', (ctypes.c_int,), dict())
VkQueryPoolSamplingModeINTEL = type('VkQueryPoolSamplingModeINTEL', (ctypes.c_int,), dict())
VkPerformanceOverrideTypeINTEL = type('VkPerformanceOverrideTypeINTEL', (ctypes.c_int,), dict())
VkPerformanceParameterTypeINTEL = type('VkPerformanceParameterTypeINTEL', (ctypes.c_int,), dict())
VkPerformanceValueTypeINTEL = type('VkPerformanceValueTypeINTEL', (ctypes.c_int,), dict())
VkLineRasterizationModeEXT = type('VkLineRasterizationModeEXT', (ctypes.c_int,), dict())
VkShaderModuleCreateFlagBits = type('VkShaderModuleCreateFlagBits', (ctypes.c_int,), dict())
VkPipelineCompilerControlFlagBitsAMD = type('VkPipelineCompilerControlFlagBitsAMD', (ctypes.c_int,), dict())
VkShaderCorePropertiesFlagBitsAMD = type('VkShaderCorePropertiesFlagBitsAMD', (ctypes.c_int,), dict())
VkToolPurposeFlagBitsEXT = type('VkToolPurposeFlagBitsEXT', (ctypes.c_int,), dict())
VkFragmentShadingRateNV = type('VkFragmentShadingRateNV', (ctypes.c_int,), dict())
VkFragmentShadingRateTypeNV = type('VkFragmentShadingRateTypeNV', (ctypes.c_int,), dict())
VkColorSpaceKHR = type('VkColorSpaceKHR', (ctypes.c_int,), dict())
VkCompositeAlphaFlagBitsKHR = type('VkCompositeAlphaFlagBitsKHR', (ctypes.c_int,), dict())
VkDisplayPlaneAlphaFlagBitsKHR = type('VkDisplayPlaneAlphaFlagBitsKHR', (ctypes.c_int,), dict())
VkPresentModeKHR = type('VkPresentModeKHR', (ctypes.c_int,), dict())
VkSurfaceTransformFlagBitsKHR = type('VkSurfaceTransformFlagBitsKHR', (ctypes.c_int,), dict())
VkDebugReportFlagBitsEXT = type('VkDebugReportFlagBitsEXT', (ctypes.c_int,), dict())
VkDebugReportObjectTypeEXT = type('VkDebugReportObjectTypeEXT', (ctypes.c_int,), dict())
VkDeviceMemoryReportEventTypeEXT = type('VkDeviceMemoryReportEventTypeEXT', (ctypes.c_int,), dict())
VkRasterizationOrderAMD = type('VkRasterizationOrderAMD', (ctypes.c_int,), dict())
VkExternalMemoryHandleTypeFlagBitsNV = type('VkExternalMemoryHandleTypeFlagBitsNV', (ctypes.c_int,), dict())
VkExternalMemoryFeatureFlagBitsNV = type('VkExternalMemoryFeatureFlagBitsNV', (ctypes.c_int,), dict())
VkValidationCheckEXT = type('VkValidationCheckEXT', (ctypes.c_int,), dict())
VkValidationFeatureEnableEXT = type('VkValidationFeatureEnableEXT', (ctypes.c_int,), dict())
VkValidationFeatureDisableEXT = type('VkValidationFeatureDisableEXT', (ctypes.c_int,), dict())
VkExternalMemoryHandleTypeFlagBits = type('VkExternalMemoryHandleTypeFlagBits', (ctypes.c_int,), dict())
VkExternalMemoryHandleTypeFlagBitsKHR = VkExternalMemoryHandleTypeFlagBits
VkExternalMemoryFeatureFlagBits = type('VkExternalMemoryFeatureFlagBits', (ctypes.c_int,), dict())
VkExternalMemoryFeatureFlagBitsKHR = VkExternalMemoryFeatureFlagBits
VkExternalSemaphoreHandleTypeFlagBits = type('VkExternalSemaphoreHandleTypeFlagBits', (ctypes.c_int,), dict())
VkExternalSemaphoreHandleTypeFlagBitsKHR = VkExternalSemaphoreHandleTypeFlagBits
VkExternalSemaphoreFeatureFlagBits = type('VkExternalSemaphoreFeatureFlagBits', (ctypes.c_int,), dict())
VkExternalSemaphoreFeatureFlagBitsKHR = VkExternalSemaphoreFeatureFlagBits
VkSemaphoreImportFlagBits = type('VkSemaphoreImportFlagBits', (ctypes.c_int,), dict())
VkSemaphoreImportFlagBitsKHR = VkSemaphoreImportFlagBits
VkExternalFenceHandleTypeFlagBits = type('VkExternalFenceHandleTypeFlagBits', (ctypes.c_int,), dict())
VkExternalFenceHandleTypeFlagBitsKHR = VkExternalFenceHandleTypeFlagBits
VkExternalFenceFeatureFlagBits = type('VkExternalFenceFeatureFlagBits', (ctypes.c_int,), dict())
VkExternalFenceFeatureFlagBitsKHR = VkExternalFenceFeatureFlagBits
VkFenceImportFlagBits = type('VkFenceImportFlagBits', (ctypes.c_int,), dict())
VkFenceImportFlagBitsKHR = VkFenceImportFlagBits
VkSurfaceCounterFlagBitsEXT = type('VkSurfaceCounterFlagBitsEXT', (ctypes.c_int,), dict())
VkDisplayPowerStateEXT = type('VkDisplayPowerStateEXT', (ctypes.c_int,), dict())
VkDeviceEventTypeEXT = type('VkDeviceEventTypeEXT', (ctypes.c_int,), dict())
VkDisplayEventTypeEXT = type('VkDisplayEventTypeEXT', (ctypes.c_int,), dict())
VkPeerMemoryFeatureFlagBits = type('VkPeerMemoryFeatureFlagBits', (ctypes.c_int,), dict())
VkPeerMemoryFeatureFlagBitsKHR = VkPeerMemoryFeatureFlagBits
VkMemoryAllocateFlagBits = type('VkMemoryAllocateFlagBits', (ctypes.c_int,), dict())
VkMemoryAllocateFlagBitsKHR = VkMemoryAllocateFlagBits
VkDeviceGroupPresentModeFlagBitsKHR = type('VkDeviceGroupPresentModeFlagBitsKHR', (ctypes.c_int,), dict())
VkSwapchainCreateFlagBitsKHR = type('VkSwapchainCreateFlagBitsKHR', (ctypes.c_int,), dict())
VkSubgroupFeatureFlagBits = type('VkSubgroupFeatureFlagBits', (ctypes.c_int,), dict())
VkTessellationDomainOrigin = type('VkTessellationDomainOrigin', (ctypes.c_int,), dict())
VkTessellationDomainOriginKHR = VkTessellationDomainOrigin
VkSamplerYcbcrModelConversion = type('VkSamplerYcbcrModelConversion', (ctypes.c_int,), dict())
VkSamplerYcbcrModelConversionKHR = VkSamplerYcbcrModelConversion
VkSamplerYcbcrRange = type('VkSamplerYcbcrRange', (ctypes.c_int,), dict())
VkSamplerYcbcrRangeKHR = VkSamplerYcbcrRange
VkChromaLocation = type('VkChromaLocation', (ctypes.c_int,), dict())
VkChromaLocationKHR = VkChromaLocation
VkSamplerReductionMode = type('VkSamplerReductionMode', (ctypes.c_int,), dict())
VkSamplerReductionModeEXT = VkSamplerReductionMode
VkBlendOverlapEXT = type('VkBlendOverlapEXT', (ctypes.c_int,), dict())
VkDebugUtilsMessageSeverityFlagBitsEXT = type('VkDebugUtilsMessageSeverityFlagBitsEXT', (ctypes.c_int,), dict())
VkDebugUtilsMessageTypeFlagBitsEXT = type('VkDebugUtilsMessageTypeFlagBitsEXT', (ctypes.c_int,), dict())
VkFullScreenExclusiveEXT = type('VkFullScreenExclusiveEXT', (ctypes.c_int,), dict())
VkShaderFloatControlsIndependence = type('VkShaderFloatControlsIndependence', (ctypes.c_int,), dict())
VkShaderFloatControlsIndependenceKHR = VkShaderFloatControlsIndependence
VkSwapchainImageUsageFlagBitsANDROID = type('VkSwapchainImageUsageFlagBitsANDROID', (ctypes.c_int,), dict())
VkFragmentShadingRateCombinerOpKHR = type('VkFragmentShadingRateCombinerOpKHR', (ctypes.c_int,), dict())
VkVendorId = type('VkVendorId', (ctypes.c_int,), dict())
VkDriverId = type('VkDriverId', (ctypes.c_int,), dict())
VkDriverIdKHR = VkDriverId
VkShadingRatePaletteEntryNV = type('VkShadingRatePaletteEntryNV', (ctypes.c_int,), dict())
VkCoarseSampleOrderTypeNV = type('VkCoarseSampleOrderTypeNV', (ctypes.c_int,), dict())
VkPipelineExecutableStatisticFormatKHR = type('VkPipelineExecutableStatisticFormatKHR', (ctypes.c_int,), dict())


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


# ENUM VkImageLayout
VK_IMAGE_LAYOUT_UNDEFINED = VkImageLayout(0)
VK_IMAGE_LAYOUT_GENERAL = VkImageLayout(1)
VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL = VkImageLayout(2)
VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL = VkImageLayout(3)
VK_IMAGE_LAYOUT_DEPTH_STENCIL_READ_ONLY_OPTIMAL = VkImageLayout(4)
VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL = VkImageLayout(5)
VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL = VkImageLayout(6)
VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL = VkImageLayout(7)
VK_IMAGE_LAYOUT_PREINITIALIZED = VkImageLayout(8)


# ENUM VkAttachmentLoadOp
VK_ATTACHMENT_LOAD_OP_LOAD = VkAttachmentLoadOp(0)
VK_ATTACHMENT_LOAD_OP_CLEAR = VkAttachmentLoadOp(1)
VK_ATTACHMENT_LOAD_OP_DONT_CARE = VkAttachmentLoadOp(2)


# ENUM VkAttachmentStoreOp
VK_ATTACHMENT_STORE_OP_STORE = VkAttachmentStoreOp(0)
VK_ATTACHMENT_STORE_OP_DONT_CARE = VkAttachmentStoreOp(1)


# ENUM VkImageType
VK_IMAGE_TYPE_1D = VkImageType(0)
VK_IMAGE_TYPE_2D = VkImageType(1)
VK_IMAGE_TYPE_3D = VkImageType(2)


# ENUM VkImageTiling
VK_IMAGE_TILING_OPTIMAL = VkImageTiling(0)
VK_IMAGE_TILING_LINEAR = VkImageTiling(1)


# ENUM VkImageViewType
VK_IMAGE_VIEW_TYPE_1D = VkImageViewType(0)
VK_IMAGE_VIEW_TYPE_2D = VkImageViewType(1)
VK_IMAGE_VIEW_TYPE_3D = VkImageViewType(2)
VK_IMAGE_VIEW_TYPE_CUBE = VkImageViewType(3)
VK_IMAGE_VIEW_TYPE_1D_ARRAY = VkImageViewType(4)
VK_IMAGE_VIEW_TYPE_2D_ARRAY = VkImageViewType(5)
VK_IMAGE_VIEW_TYPE_CUBE_ARRAY = VkImageViewType(6)


# ENUM VkCommandBufferLevel
VK_COMMAND_BUFFER_LEVEL_PRIMARY = VkCommandBufferLevel(0)
VK_COMMAND_BUFFER_LEVEL_SECONDARY = VkCommandBufferLevel(1)


# ENUM VkComponentSwizzle
VK_COMPONENT_SWIZZLE_IDENTITY = VkComponentSwizzle(0)
VK_COMPONENT_SWIZZLE_ZERO = VkComponentSwizzle(1)
VK_COMPONENT_SWIZZLE_ONE = VkComponentSwizzle(2)
VK_COMPONENT_SWIZZLE_R = VkComponentSwizzle(3)
VK_COMPONENT_SWIZZLE_G = VkComponentSwizzle(4)
VK_COMPONENT_SWIZZLE_B = VkComponentSwizzle(5)
VK_COMPONENT_SWIZZLE_A = VkComponentSwizzle(6)


# ENUM VkDescriptorType
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


# ENUM VkQueryType
VK_QUERY_TYPE_OCCLUSION = VkQueryType(0)
VK_QUERY_TYPE_PIPELINE_STATISTICS = VkQueryType(1)
VK_QUERY_TYPE_TIMESTAMP = VkQueryType(2)


# ENUM VkBorderColor
VK_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK = VkBorderColor(0)
VK_BORDER_COLOR_INT_TRANSPARENT_BLACK = VkBorderColor(1)
VK_BORDER_COLOR_FLOAT_OPAQUE_BLACK = VkBorderColor(2)
VK_BORDER_COLOR_INT_OPAQUE_BLACK = VkBorderColor(3)
VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE = VkBorderColor(4)
VK_BORDER_COLOR_INT_OPAQUE_WHITE = VkBorderColor(5)


# ENUM VkPipelineBindPoint
VK_PIPELINE_BIND_POINT_GRAPHICS = VkPipelineBindPoint(0)
VK_PIPELINE_BIND_POINT_COMPUTE = VkPipelineBindPoint(1)


# ENUM VkPipelineCacheHeaderVersion
VK_PIPELINE_CACHE_HEADER_VERSION_ONE = VkPipelineCacheHeaderVersion(1)


# ENUM VkPipelineCacheCreateFlagBits


# ENUM VkPrimitiveTopology
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


# ENUM VkSharingMode
VK_SHARING_MODE_EXCLUSIVE = VkSharingMode(0)
VK_SHARING_MODE_CONCURRENT = VkSharingMode(1)


# ENUM VkIndexType
VK_INDEX_TYPE_UINT16 = VkIndexType(0)
VK_INDEX_TYPE_UINT32 = VkIndexType(1)


# ENUM VkFilter
VK_FILTER_NEAREST = VkFilter(0)
VK_FILTER_LINEAR = VkFilter(1)


# ENUM VkSamplerMipmapMode
VK_SAMPLER_MIPMAP_MODE_NEAREST = VkSamplerMipmapMode(0)
VK_SAMPLER_MIPMAP_MODE_LINEAR = VkSamplerMipmapMode(1)


# ENUM VkSamplerAddressMode
VK_SAMPLER_ADDRESS_MODE_REPEAT = VkSamplerAddressMode(0)
VK_SAMPLER_ADDRESS_MODE_MIRRORED_REPEAT = VkSamplerAddressMode(1)
VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE = VkSamplerAddressMode(2)
VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_BORDER = VkSamplerAddressMode(3)


# ENUM VkCompareOp
VK_COMPARE_OP_NEVER = VkCompareOp(0)
VK_COMPARE_OP_LESS = VkCompareOp(1)
VK_COMPARE_OP_EQUAL = VkCompareOp(2)
VK_COMPARE_OP_LESS_OR_EQUAL = VkCompareOp(3)
VK_COMPARE_OP_GREATER = VkCompareOp(4)
VK_COMPARE_OP_NOT_EQUAL = VkCompareOp(5)
VK_COMPARE_OP_GREATER_OR_EQUAL = VkCompareOp(6)
VK_COMPARE_OP_ALWAYS = VkCompareOp(7)


# ENUM VkPolygonMode
VK_POLYGON_MODE_FILL = VkPolygonMode(0)
VK_POLYGON_MODE_LINE = VkPolygonMode(1)
VK_POLYGON_MODE_POINT = VkPolygonMode(2)


# ENUM VkFrontFace
VK_FRONT_FACE_COUNTER_CLOCKWISE = VkFrontFace(0)
VK_FRONT_FACE_CLOCKWISE = VkFrontFace(1)


# ENUM VkBlendFactor
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


# ENUM VkBlendOp
VK_BLEND_OP_ADD = VkBlendOp(0)
VK_BLEND_OP_SUBTRACT = VkBlendOp(1)
VK_BLEND_OP_REVERSE_SUBTRACT = VkBlendOp(2)
VK_BLEND_OP_MIN = VkBlendOp(3)
VK_BLEND_OP_MAX = VkBlendOp(4)


# ENUM VkStencilOp
VK_STENCIL_OP_KEEP = VkStencilOp(0)
VK_STENCIL_OP_ZERO = VkStencilOp(1)
VK_STENCIL_OP_REPLACE = VkStencilOp(2)
VK_STENCIL_OP_INCREMENT_AND_CLAMP = VkStencilOp(3)
VK_STENCIL_OP_DECREMENT_AND_CLAMP = VkStencilOp(4)
VK_STENCIL_OP_INVERT = VkStencilOp(5)
VK_STENCIL_OP_INCREMENT_AND_WRAP = VkStencilOp(6)
VK_STENCIL_OP_DECREMENT_AND_WRAP = VkStencilOp(7)


# ENUM VkLogicOp
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


# ENUM VkInternalAllocationType
VK_INTERNAL_ALLOCATION_TYPE_EXECUTABLE = VkInternalAllocationType(0)


# ENUM VkSystemAllocationScope
VK_SYSTEM_ALLOCATION_SCOPE_COMMAND = VkSystemAllocationScope(0)
VK_SYSTEM_ALLOCATION_SCOPE_OBJECT = VkSystemAllocationScope(1)
VK_SYSTEM_ALLOCATION_SCOPE_CACHE = VkSystemAllocationScope(2)
VK_SYSTEM_ALLOCATION_SCOPE_DEVICE = VkSystemAllocationScope(3)
VK_SYSTEM_ALLOCATION_SCOPE_INSTANCE = VkSystemAllocationScope(4)


# ENUM VkPhysicalDeviceType
VK_PHYSICAL_DEVICE_TYPE_OTHER = VkPhysicalDeviceType(0)
VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU = VkPhysicalDeviceType(1)
VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU = VkPhysicalDeviceType(2)
VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU = VkPhysicalDeviceType(3)
VK_PHYSICAL_DEVICE_TYPE_CPU = VkPhysicalDeviceType(4)


# ENUM VkVertexInputRate
VK_VERTEX_INPUT_RATE_VERTEX = VkVertexInputRate(0)
VK_VERTEX_INPUT_RATE_INSTANCE = VkVertexInputRate(1)


# ENUM VkFormat
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


# ENUM VkStructureType
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


# ENUM VkSubpassContents
VK_SUBPASS_CONTENTS_INLINE = VkSubpassContents(0)
VK_SUBPASS_CONTENTS_SECONDARY_COMMAND_BUFFERS = VkSubpassContents(1)


# ENUM VkResult
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


# ENUM VkDynamicState
VK_DYNAMIC_STATE_VIEWPORT = VkDynamicState(0)
VK_DYNAMIC_STATE_SCISSOR = VkDynamicState(1)
VK_DYNAMIC_STATE_LINE_WIDTH = VkDynamicState(2)
VK_DYNAMIC_STATE_DEPTH_BIAS = VkDynamicState(3)
VK_DYNAMIC_STATE_BLEND_CONSTANTS = VkDynamicState(4)
VK_DYNAMIC_STATE_DEPTH_BOUNDS = VkDynamicState(5)
VK_DYNAMIC_STATE_STENCIL_COMPARE_MASK = VkDynamicState(6)
VK_DYNAMIC_STATE_STENCIL_WRITE_MASK = VkDynamicState(7)
VK_DYNAMIC_STATE_STENCIL_REFERENCE = VkDynamicState(8)


# ENUM VkDescriptorUpdateTemplateType
VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET = VkDescriptorUpdateTemplateType(0)


# ENUM VkObjectType
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


# ENUM VkQueueFlagBits
VK_QUEUE_GRAPHICS_BIT = VkQueueFlagBits(1)
VK_QUEUE_COMPUTE_BIT = VkQueueFlagBits(2)
VK_QUEUE_TRANSFER_BIT = VkQueueFlagBits(4)
VK_QUEUE_SPARSE_BINDING_BIT = VkQueueFlagBits(8)


# ENUM VkCullModeFlagBits
VK_CULL_MODE_NONE = VkCullModeFlagBits(0)
VK_CULL_MODE_FRONT_BIT = VkCullModeFlagBits(1)
VK_CULL_MODE_BACK_BIT = VkCullModeFlagBits(2)
VK_CULL_MODE_FRONT_AND_BACK = VkCullModeFlagBits(0x00000003)


# ENUM VkRenderPassCreateFlagBits


# ENUM VkDeviceQueueCreateFlagBits


# ENUM VkMemoryPropertyFlagBits
VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT = VkMemoryPropertyFlagBits(1)
VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT = VkMemoryPropertyFlagBits(2)
VK_MEMORY_PROPERTY_HOST_COHERENT_BIT = VkMemoryPropertyFlagBits(4)
VK_MEMORY_PROPERTY_HOST_CACHED_BIT = VkMemoryPropertyFlagBits(8)
VK_MEMORY_PROPERTY_LAZILY_ALLOCATED_BIT = VkMemoryPropertyFlagBits(16)


# ENUM VkMemoryHeapFlagBits
VK_MEMORY_HEAP_DEVICE_LOCAL_BIT = VkMemoryHeapFlagBits(1)


# ENUM VkAccessFlagBits
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


# ENUM VkBufferUsageFlagBits
VK_BUFFER_USAGE_TRANSFER_SRC_BIT = VkBufferUsageFlagBits(1)
VK_BUFFER_USAGE_TRANSFER_DST_BIT = VkBufferUsageFlagBits(2)
VK_BUFFER_USAGE_UNIFORM_TEXEL_BUFFER_BIT = VkBufferUsageFlagBits(4)
VK_BUFFER_USAGE_STORAGE_TEXEL_BUFFER_BIT = VkBufferUsageFlagBits(8)
VK_BUFFER_USAGE_UNIFORM_BUFFER_BIT = VkBufferUsageFlagBits(16)
VK_BUFFER_USAGE_STORAGE_BUFFER_BIT = VkBufferUsageFlagBits(32)
VK_BUFFER_USAGE_INDEX_BUFFER_BIT = VkBufferUsageFlagBits(64)
VK_BUFFER_USAGE_VERTEX_BUFFER_BIT = VkBufferUsageFlagBits(128)
VK_BUFFER_USAGE_INDIRECT_BUFFER_BIT = VkBufferUsageFlagBits(256)


# ENUM VkBufferCreateFlagBits
VK_BUFFER_CREATE_SPARSE_BINDING_BIT = VkBufferCreateFlagBits(1)
VK_BUFFER_CREATE_SPARSE_RESIDENCY_BIT = VkBufferCreateFlagBits(2)
VK_BUFFER_CREATE_SPARSE_ALIASED_BIT = VkBufferCreateFlagBits(4)


# ENUM VkShaderStageFlagBits
VK_SHADER_STAGE_VERTEX_BIT = VkShaderStageFlagBits(1)
VK_SHADER_STAGE_TESSELLATION_CONTROL_BIT = VkShaderStageFlagBits(2)
VK_SHADER_STAGE_TESSELLATION_EVALUATION_BIT = VkShaderStageFlagBits(4)
VK_SHADER_STAGE_GEOMETRY_BIT = VkShaderStageFlagBits(8)
VK_SHADER_STAGE_FRAGMENT_BIT = VkShaderStageFlagBits(16)
VK_SHADER_STAGE_COMPUTE_BIT = VkShaderStageFlagBits(32)
VK_SHADER_STAGE_ALL_GRAPHICS = VkShaderStageFlagBits(0x0000001F)
VK_SHADER_STAGE_ALL = VkShaderStageFlagBits(0x7FFFFFFF)


# ENUM VkImageUsageFlagBits
VK_IMAGE_USAGE_TRANSFER_SRC_BIT = VkImageUsageFlagBits(1)
VK_IMAGE_USAGE_TRANSFER_DST_BIT = VkImageUsageFlagBits(2)
VK_IMAGE_USAGE_SAMPLED_BIT = VkImageUsageFlagBits(4)
VK_IMAGE_USAGE_STORAGE_BIT = VkImageUsageFlagBits(8)
VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT = VkImageUsageFlagBits(16)
VK_IMAGE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT = VkImageUsageFlagBits(32)
VK_IMAGE_USAGE_TRANSIENT_ATTACHMENT_BIT = VkImageUsageFlagBits(64)
VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT = VkImageUsageFlagBits(128)


# ENUM VkImageCreateFlagBits
VK_IMAGE_CREATE_SPARSE_BINDING_BIT = VkImageCreateFlagBits(1)
VK_IMAGE_CREATE_SPARSE_RESIDENCY_BIT = VkImageCreateFlagBits(2)
VK_IMAGE_CREATE_SPARSE_ALIASED_BIT = VkImageCreateFlagBits(4)
VK_IMAGE_CREATE_MUTABLE_FORMAT_BIT = VkImageCreateFlagBits(8)
VK_IMAGE_CREATE_CUBE_COMPATIBLE_BIT = VkImageCreateFlagBits(16)


# ENUM VkImageViewCreateFlagBits


# ENUM VkSamplerCreateFlagBits


# ENUM VkPipelineCreateFlagBits
VK_PIPELINE_CREATE_DISABLE_OPTIMIZATION_BIT = VkPipelineCreateFlagBits(1)
VK_PIPELINE_CREATE_ALLOW_DERIVATIVES_BIT = VkPipelineCreateFlagBits(2)
VK_PIPELINE_CREATE_DERIVATIVE_BIT = VkPipelineCreateFlagBits(4)


# ENUM VkPipelineShaderStageCreateFlagBits


# ENUM VkColorComponentFlagBits
VK_COLOR_COMPONENT_R_BIT = VkColorComponentFlagBits(1)
VK_COLOR_COMPONENT_G_BIT = VkColorComponentFlagBits(2)
VK_COLOR_COMPONENT_B_BIT = VkColorComponentFlagBits(4)
VK_COLOR_COMPONENT_A_BIT = VkColorComponentFlagBits(8)


# ENUM VkFenceCreateFlagBits
VK_FENCE_CREATE_SIGNALED_BIT = VkFenceCreateFlagBits(1)


# ENUM VkFormatFeatureFlagBits
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


# ENUM VkQueryControlFlagBits
VK_QUERY_CONTROL_PRECISE_BIT = VkQueryControlFlagBits(1)


# ENUM VkQueryResultFlagBits
VK_QUERY_RESULT_64_BIT = VkQueryResultFlagBits(1)
VK_QUERY_RESULT_WAIT_BIT = VkQueryResultFlagBits(2)
VK_QUERY_RESULT_WITH_AVAILABILITY_BIT = VkQueryResultFlagBits(4)
VK_QUERY_RESULT_PARTIAL_BIT = VkQueryResultFlagBits(8)


# ENUM VkCommandBufferUsageFlagBits
VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT = VkCommandBufferUsageFlagBits(1)
VK_COMMAND_BUFFER_USAGE_RENDER_PASS_CONTINUE_BIT = VkCommandBufferUsageFlagBits(2)
VK_COMMAND_BUFFER_USAGE_SIMULTANEOUS_USE_BIT = VkCommandBufferUsageFlagBits(4)


# ENUM VkQueryPipelineStatisticFlagBits
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


# ENUM VkImageAspectFlagBits
VK_IMAGE_ASPECT_COLOR_BIT = VkImageAspectFlagBits(1)
VK_IMAGE_ASPECT_DEPTH_BIT = VkImageAspectFlagBits(2)
VK_IMAGE_ASPECT_STENCIL_BIT = VkImageAspectFlagBits(4)
VK_IMAGE_ASPECT_METADATA_BIT = VkImageAspectFlagBits(8)


# ENUM VkSparseImageFormatFlagBits
VK_SPARSE_IMAGE_FORMAT_SINGLE_MIPTAIL_BIT = VkSparseImageFormatFlagBits(1)
VK_SPARSE_IMAGE_FORMAT_ALIGNED_MIP_SIZE_BIT = VkSparseImageFormatFlagBits(2)
VK_SPARSE_IMAGE_FORMAT_NONSTANDARD_BLOCK_SIZE_BIT = VkSparseImageFormatFlagBits(4)


# ENUM VkSparseMemoryBindFlagBits
VK_SPARSE_MEMORY_BIND_METADATA_BIT = VkSparseMemoryBindFlagBits(1)


# ENUM VkPipelineStageFlagBits
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


# ENUM VkCommandPoolCreateFlagBits
VK_COMMAND_POOL_CREATE_TRANSIENT_BIT = VkCommandPoolCreateFlagBits(1)
VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT = VkCommandPoolCreateFlagBits(2)


# ENUM VkCommandPoolResetFlagBits
VK_COMMAND_POOL_RESET_RELEASE_RESOURCES_BIT = VkCommandPoolResetFlagBits(1)


# ENUM VkCommandBufferResetFlagBits
VK_COMMAND_BUFFER_RESET_RELEASE_RESOURCES_BIT = VkCommandBufferResetFlagBits(1)


# ENUM VkSampleCountFlagBits
VK_SAMPLE_COUNT_1_BIT = VkSampleCountFlagBits(1)
VK_SAMPLE_COUNT_2_BIT = VkSampleCountFlagBits(2)
VK_SAMPLE_COUNT_4_BIT = VkSampleCountFlagBits(4)
VK_SAMPLE_COUNT_8_BIT = VkSampleCountFlagBits(8)
VK_SAMPLE_COUNT_16_BIT = VkSampleCountFlagBits(16)
VK_SAMPLE_COUNT_32_BIT = VkSampleCountFlagBits(32)
VK_SAMPLE_COUNT_64_BIT = VkSampleCountFlagBits(64)


# ENUM VkAttachmentDescriptionFlagBits
VK_ATTACHMENT_DESCRIPTION_MAY_ALIAS_BIT = VkAttachmentDescriptionFlagBits(1)


# ENUM VkStencilFaceFlagBits
VK_STENCIL_FACE_FRONT_BIT = VkStencilFaceFlagBits(1)
VK_STENCIL_FACE_BACK_BIT = VkStencilFaceFlagBits(2)
VK_STENCIL_FACE_FRONT_AND_BACK = VkStencilFaceFlagBits(0x00000003)
VK_STENCIL_FRONT_AND_BACK = VK_STENCIL_FACE_FRONT_AND_BACK


# ENUM VkDescriptorPoolCreateFlagBits
VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT = VkDescriptorPoolCreateFlagBits(1)


# ENUM VkDependencyFlagBits
VK_DEPENDENCY_BY_REGION_BIT = VkDependencyFlagBits(1)


# ENUM VkSemaphoreType
VK_SEMAPHORE_TYPE_BINARY = VkSemaphoreType(0)
VK_SEMAPHORE_TYPE_TIMELINE = VkSemaphoreType(1)


# ENUM VkSemaphoreWaitFlagBits
VK_SEMAPHORE_WAIT_ANY_BIT = VkSemaphoreWaitFlagBits(1)


# ENUM VkPresentModeKHR
VK_PRESENT_MODE_IMMEDIATE_KHR = VkPresentModeKHR(0)
VK_PRESENT_MODE_MAILBOX_KHR = VkPresentModeKHR(1)
VK_PRESENT_MODE_FIFO_KHR = VkPresentModeKHR(2)
VK_PRESENT_MODE_FIFO_RELAXED_KHR = VkPresentModeKHR(3)


# ENUM VkColorSpaceKHR
VK_COLOR_SPACE_SRGB_NONLINEAR_KHR = VkColorSpaceKHR(0)
VK_COLORSPACE_SRGB_NONLINEAR_KHR = VK_COLOR_SPACE_SRGB_NONLINEAR_KHR


# ENUM VkDisplayPlaneAlphaFlagBitsKHR
VK_DISPLAY_PLANE_ALPHA_OPAQUE_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(1)
VK_DISPLAY_PLANE_ALPHA_GLOBAL_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(2)
VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(4)
VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_PREMULTIPLIED_BIT_KHR = VkDisplayPlaneAlphaFlagBitsKHR(8)


# ENUM VkCompositeAlphaFlagBitsKHR
VK_COMPOSITE_ALPHA_OPAQUE_BIT_KHR = VkCompositeAlphaFlagBitsKHR(1)
VK_COMPOSITE_ALPHA_PRE_MULTIPLIED_BIT_KHR = VkCompositeAlphaFlagBitsKHR(2)
VK_COMPOSITE_ALPHA_POST_MULTIPLIED_BIT_KHR = VkCompositeAlphaFlagBitsKHR(4)
VK_COMPOSITE_ALPHA_INHERIT_BIT_KHR = VkCompositeAlphaFlagBitsKHR(8)


# ENUM VkSurfaceTransformFlagBitsKHR
VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR = VkSurfaceTransformFlagBitsKHR(1)
VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR = VkSurfaceTransformFlagBitsKHR(2)
VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR = VkSurfaceTransformFlagBitsKHR(4)
VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR = VkSurfaceTransformFlagBitsKHR(8)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_BIT_KHR = VkSurfaceTransformFlagBitsKHR(16)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_90_BIT_KHR = VkSurfaceTransformFlagBitsKHR(32)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_180_BIT_KHR = VkSurfaceTransformFlagBitsKHR(64)
VK_SURFACE_TRANSFORM_HORIZONTAL_MIRROR_ROTATE_270_BIT_KHR = VkSurfaceTransformFlagBitsKHR(128)
VK_SURFACE_TRANSFORM_INHERIT_BIT_KHR = VkSurfaceTransformFlagBitsKHR(256)


# ENUM VkSwapchainImageUsageFlagBitsANDROID
VK_SWAPCHAIN_IMAGE_USAGE_SHARED_BIT_ANDROID = VkSwapchainImageUsageFlagBitsANDROID(1)


# ENUM VkTimeDomainEXT
VK_TIME_DOMAIN_DEVICE_EXT = VkTimeDomainEXT(0)
VK_TIME_DOMAIN_CLOCK_MONOTONIC_EXT = VkTimeDomainEXT(1)
VK_TIME_DOMAIN_CLOCK_MONOTONIC_RAW_EXT = VkTimeDomainEXT(2)
VK_TIME_DOMAIN_QUERY_PERFORMANCE_COUNTER_EXT = VkTimeDomainEXT(3)


# ENUM VkDebugReportFlagBitsEXT
VK_DEBUG_REPORT_INFORMATION_BIT_EXT = VkDebugReportFlagBitsEXT(1)
VK_DEBUG_REPORT_WARNING_BIT_EXT = VkDebugReportFlagBitsEXT(2)
VK_DEBUG_REPORT_PERFORMANCE_WARNING_BIT_EXT = VkDebugReportFlagBitsEXT(4)
VK_DEBUG_REPORT_ERROR_BIT_EXT = VkDebugReportFlagBitsEXT(8)
VK_DEBUG_REPORT_DEBUG_BIT_EXT = VkDebugReportFlagBitsEXT(16)


# ENUM VkDebugReportObjectTypeEXT
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


# ENUM VkDeviceMemoryReportEventTypeEXT
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATE_EXT = VkDeviceMemoryReportEventTypeEXT(0)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_FREE_EXT = VkDeviceMemoryReportEventTypeEXT(1)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_IMPORT_EXT = VkDeviceMemoryReportEventTypeEXT(2)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_UNIMPORT_EXT = VkDeviceMemoryReportEventTypeEXT(3)
VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATION_FAILED_EXT = VkDeviceMemoryReportEventTypeEXT(4)


# ENUM VkRasterizationOrderAMD
VK_RASTERIZATION_ORDER_STRICT_AMD = VkRasterizationOrderAMD(0)
VK_RASTERIZATION_ORDER_RELAXED_AMD = VkRasterizationOrderAMD(1)


# ENUM VkExternalMemoryHandleTypeFlagBitsNV
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(1)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(2)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(4)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_KMT_BIT_NV = VkExternalMemoryHandleTypeFlagBitsNV(8)


# ENUM VkExternalMemoryFeatureFlagBitsNV
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_NV = VkExternalMemoryFeatureFlagBitsNV(1)
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_NV = VkExternalMemoryFeatureFlagBitsNV(2)
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_NV = VkExternalMemoryFeatureFlagBitsNV(4)


# ENUM VkValidationCheckEXT
VK_VALIDATION_CHECK_ALL_EXT = VkValidationCheckEXT(0)
VK_VALIDATION_CHECK_SHADERS_EXT = VkValidationCheckEXT(1)


# ENUM VkValidationFeatureEnableEXT
VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_EXT = VkValidationFeatureEnableEXT(0)
VK_VALIDATION_FEATURE_ENABLE_GPU_ASSISTED_RESERVE_BINDING_SLOT_EXT = VkValidationFeatureEnableEXT(1)
VK_VALIDATION_FEATURE_ENABLE_BEST_PRACTICES_EXT = VkValidationFeatureEnableEXT(2)
VK_VALIDATION_FEATURE_ENABLE_DEBUG_PRINTF_EXT = VkValidationFeatureEnableEXT(3)
VK_VALIDATION_FEATURE_ENABLE_SYNCHRONIZATION_VALIDATION_EXT = VkValidationFeatureEnableEXT(4)


# ENUM VkValidationFeatureDisableEXT
VK_VALIDATION_FEATURE_DISABLE_ALL_EXT = VkValidationFeatureDisableEXT(0)
VK_VALIDATION_FEATURE_DISABLE_SHADERS_EXT = VkValidationFeatureDisableEXT(1)
VK_VALIDATION_FEATURE_DISABLE_THREAD_SAFETY_EXT = VkValidationFeatureDisableEXT(2)
VK_VALIDATION_FEATURE_DISABLE_API_PARAMETERS_EXT = VkValidationFeatureDisableEXT(3)
VK_VALIDATION_FEATURE_DISABLE_OBJECT_LIFETIMES_EXT = VkValidationFeatureDisableEXT(4)
VK_VALIDATION_FEATURE_DISABLE_CORE_CHECKS_EXT = VkValidationFeatureDisableEXT(5)
VK_VALIDATION_FEATURE_DISABLE_UNIQUE_HANDLES_EXT = VkValidationFeatureDisableEXT(6)


# ENUM VkSubgroupFeatureFlagBits
VK_SUBGROUP_FEATURE_BASIC_BIT = VkSubgroupFeatureFlagBits(1)
VK_SUBGROUP_FEATURE_VOTE_BIT = VkSubgroupFeatureFlagBits(2)
VK_SUBGROUP_FEATURE_ARITHMETIC_BIT = VkSubgroupFeatureFlagBits(4)
VK_SUBGROUP_FEATURE_BALLOT_BIT = VkSubgroupFeatureFlagBits(8)
VK_SUBGROUP_FEATURE_SHUFFLE_BIT = VkSubgroupFeatureFlagBits(16)
VK_SUBGROUP_FEATURE_SHUFFLE_RELATIVE_BIT = VkSubgroupFeatureFlagBits(32)
VK_SUBGROUP_FEATURE_CLUSTERED_BIT = VkSubgroupFeatureFlagBits(64)
VK_SUBGROUP_FEATURE_QUAD_BIT = VkSubgroupFeatureFlagBits(128)


# ENUM VkIndirectCommandsLayoutUsageFlagBitsNV
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_EXPLICIT_PREPROCESS_BIT_NV = VkIndirectCommandsLayoutUsageFlagBitsNV(1)
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_INDEXED_SEQUENCES_BIT_NV = VkIndirectCommandsLayoutUsageFlagBitsNV(2)
VK_INDIRECT_COMMANDS_LAYOUT_USAGE_UNORDERED_SEQUENCES_BIT_NV = VkIndirectCommandsLayoutUsageFlagBitsNV(4)


# ENUM VkIndirectStateFlagBitsNV
VK_INDIRECT_STATE_FLAG_FRONTFACE_BIT_NV = VkIndirectStateFlagBitsNV(1)


# ENUM VkIndirectCommandsTokenTypeNV
VK_INDIRECT_COMMANDS_TOKEN_TYPE_SHADER_GROUP_NV = VkIndirectCommandsTokenTypeNV(0)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_STATE_FLAGS_NV = VkIndirectCommandsTokenTypeNV(1)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_INDEX_BUFFER_NV = VkIndirectCommandsTokenTypeNV(2)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_VERTEX_BUFFER_NV = VkIndirectCommandsTokenTypeNV(3)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_PUSH_CONSTANT_NV = VkIndirectCommandsTokenTypeNV(4)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_INDEXED_NV = VkIndirectCommandsTokenTypeNV(5)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_NV = VkIndirectCommandsTokenTypeNV(6)
VK_INDIRECT_COMMANDS_TOKEN_TYPE_DRAW_TASKS_NV = VkIndirectCommandsTokenTypeNV(7)


# ENUM VkPrivateDataSlotCreateFlagBitsEXT


# ENUM VkDescriptorSetLayoutCreateFlagBits


# ENUM VkExternalMemoryHandleTypeFlagBits
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT = VkExternalMemoryHandleTypeFlagBits(1)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT = VkExternalMemoryHandleTypeFlagBits(2)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = VkExternalMemoryHandleTypeFlagBits(4)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_BIT = VkExternalMemoryHandleTypeFlagBits(8)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_TEXTURE_KMT_BIT = VkExternalMemoryHandleTypeFlagBits(16)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP_BIT = VkExternalMemoryHandleTypeFlagBits(32)
VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE_BIT = VkExternalMemoryHandleTypeFlagBits(64)


# ENUM VkExternalMemoryFeatureFlagBits
VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT = VkExternalMemoryFeatureFlagBits(1)
VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT = VkExternalMemoryFeatureFlagBits(2)
VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT = VkExternalMemoryFeatureFlagBits(4)


# ENUM VkExternalSemaphoreHandleTypeFlagBits
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT = VkExternalSemaphoreHandleTypeFlagBits(1)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT = VkExternalSemaphoreHandleTypeFlagBits(2)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = VkExternalSemaphoreHandleTypeFlagBits(4)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT = VkExternalSemaphoreHandleTypeFlagBits(8)
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_FENCE_BIT = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE_BIT
VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_SYNC_FD_BIT = VkExternalSemaphoreHandleTypeFlagBits(16)


# ENUM VkExternalSemaphoreFeatureFlagBits
VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT = VkExternalSemaphoreFeatureFlagBits(1)
VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT = VkExternalSemaphoreFeatureFlagBits(2)


# ENUM VkSemaphoreImportFlagBits
VK_SEMAPHORE_IMPORT_TEMPORARY_BIT = VkSemaphoreImportFlagBits(1)


# ENUM VkExternalFenceHandleTypeFlagBits
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT = VkExternalFenceHandleTypeFlagBits(1)
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT = VkExternalFenceHandleTypeFlagBits(2)
VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = VkExternalFenceHandleTypeFlagBits(4)
VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT = VkExternalFenceHandleTypeFlagBits(8)


# ENUM VkExternalFenceFeatureFlagBits
VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT = VkExternalFenceFeatureFlagBits(1)
VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT = VkExternalFenceFeatureFlagBits(2)


# ENUM VkFenceImportFlagBits
VK_FENCE_IMPORT_TEMPORARY_BIT = VkFenceImportFlagBits(1)


# ENUM VkSurfaceCounterFlagBitsEXT
VK_SURFACE_COUNTER_VBLANK_BIT_EXT = VkSurfaceCounterFlagBitsEXT(1)
VK_SURFACE_COUNTER_VBLANK_EXT = VK_SURFACE_COUNTER_VBLANK_BIT_EXT


# ENUM VkDisplayPowerStateEXT
VK_DISPLAY_POWER_STATE_OFF_EXT = VkDisplayPowerStateEXT(0)
VK_DISPLAY_POWER_STATE_SUSPEND_EXT = VkDisplayPowerStateEXT(1)
VK_DISPLAY_POWER_STATE_ON_EXT = VkDisplayPowerStateEXT(2)


# ENUM VkDeviceEventTypeEXT
VK_DEVICE_EVENT_TYPE_DISPLAY_HOTPLUG_EXT = VkDeviceEventTypeEXT(0)


# ENUM VkDisplayEventTypeEXT
VK_DISPLAY_EVENT_TYPE_FIRST_PIXEL_OUT_EXT = VkDisplayEventTypeEXT(0)


# ENUM VkPeerMemoryFeatureFlagBits
VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT = VkPeerMemoryFeatureFlagBits(1)
VK_PEER_MEMORY_FEATURE_COPY_DST_BIT = VkPeerMemoryFeatureFlagBits(2)
VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT = VkPeerMemoryFeatureFlagBits(4)
VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT = VkPeerMemoryFeatureFlagBits(8)


# ENUM VkMemoryAllocateFlagBits
VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT = VkMemoryAllocateFlagBits(1)


# ENUM VkDeviceGroupPresentModeFlagBitsKHR
VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(1)
VK_DEVICE_GROUP_PRESENT_MODE_REMOTE_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(2)
VK_DEVICE_GROUP_PRESENT_MODE_SUM_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(4)
VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_MULTI_DEVICE_BIT_KHR = VkDeviceGroupPresentModeFlagBitsKHR(8)


# ENUM VkSwapchainCreateFlagBitsKHR


# ENUM VkViewportCoordinateSwizzleNV
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_X_NV = VkViewportCoordinateSwizzleNV(0)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_X_NV = VkViewportCoordinateSwizzleNV(1)
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Y_NV = VkViewportCoordinateSwizzleNV(2)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Y_NV = VkViewportCoordinateSwizzleNV(3)
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Z_NV = VkViewportCoordinateSwizzleNV(4)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Z_NV = VkViewportCoordinateSwizzleNV(5)
VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_W_NV = VkViewportCoordinateSwizzleNV(6)
VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_W_NV = VkViewportCoordinateSwizzleNV(7)


# ENUM VkDiscardRectangleModeEXT
VK_DISCARD_RECTANGLE_MODE_INCLUSIVE_EXT = VkDiscardRectangleModeEXT(0)
VK_DISCARD_RECTANGLE_MODE_EXCLUSIVE_EXT = VkDiscardRectangleModeEXT(1)


# ENUM VkSubpassDescriptionFlagBits


# ENUM VkPointClippingBehavior
VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES = VkPointClippingBehavior(0)
VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY = VkPointClippingBehavior(1)


# ENUM VkSamplerReductionMode
VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE = VkSamplerReductionMode(0)
VK_SAMPLER_REDUCTION_MODE_MIN = VkSamplerReductionMode(1)
VK_SAMPLER_REDUCTION_MODE_MAX = VkSamplerReductionMode(2)


# ENUM VkTessellationDomainOrigin
VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT = VkTessellationDomainOrigin(0)
VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT = VkTessellationDomainOrigin(1)


# ENUM VkSamplerYcbcrModelConversion
VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY = VkSamplerYcbcrModelConversion(0)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY = VkSamplerYcbcrModelConversion(1)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709 = VkSamplerYcbcrModelConversion(2)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601 = VkSamplerYcbcrModelConversion(3)
VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020 = VkSamplerYcbcrModelConversion(4)


# ENUM VkSamplerYcbcrRange
VK_SAMPLER_YCBCR_RANGE_ITU_FULL = VkSamplerYcbcrRange(0)
VK_SAMPLER_YCBCR_RANGE_ITU_NARROW = VkSamplerYcbcrRange(1)


# ENUM VkChromaLocation
VK_CHROMA_LOCATION_COSITED_EVEN = VkChromaLocation(0)
VK_CHROMA_LOCATION_MIDPOINT = VkChromaLocation(1)


# ENUM VkBlendOverlapEXT
VK_BLEND_OVERLAP_UNCORRELATED_EXT = VkBlendOverlapEXT(0)
VK_BLEND_OVERLAP_DISJOINT_EXT = VkBlendOverlapEXT(1)
VK_BLEND_OVERLAP_CONJOINT_EXT = VkBlendOverlapEXT(2)


# ENUM VkCoverageModulationModeNV
VK_COVERAGE_MODULATION_MODE_NONE_NV = VkCoverageModulationModeNV(0)
VK_COVERAGE_MODULATION_MODE_RGB_NV = VkCoverageModulationModeNV(1)
VK_COVERAGE_MODULATION_MODE_ALPHA_NV = VkCoverageModulationModeNV(2)
VK_COVERAGE_MODULATION_MODE_RGBA_NV = VkCoverageModulationModeNV(3)


# ENUM VkCoverageReductionModeNV
VK_COVERAGE_REDUCTION_MODE_MERGE_NV = VkCoverageReductionModeNV(0)
VK_COVERAGE_REDUCTION_MODE_TRUNCATE_NV = VkCoverageReductionModeNV(1)


# ENUM VkValidationCacheHeaderVersionEXT
VK_VALIDATION_CACHE_HEADER_VERSION_ONE_EXT = VkValidationCacheHeaderVersionEXT(1)


# ENUM VkShaderInfoTypeAMD
VK_SHADER_INFO_TYPE_STATISTICS_AMD = VkShaderInfoTypeAMD(0)
VK_SHADER_INFO_TYPE_BINARY_AMD = VkShaderInfoTypeAMD(1)
VK_SHADER_INFO_TYPE_DISASSEMBLY_AMD = VkShaderInfoTypeAMD(2)


# ENUM VkQueueGlobalPriorityEXT
VK_QUEUE_GLOBAL_PRIORITY_LOW_EXT = VkQueueGlobalPriorityEXT(128)
VK_QUEUE_GLOBAL_PRIORITY_MEDIUM_EXT = VkQueueGlobalPriorityEXT(256)
VK_QUEUE_GLOBAL_PRIORITY_HIGH_EXT = VkQueueGlobalPriorityEXT(512)
VK_QUEUE_GLOBAL_PRIORITY_REALTIME_EXT = VkQueueGlobalPriorityEXT(1024)


# ENUM VkDebugUtilsMessageSeverityFlagBitsEXT
VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(1)
VK_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(16)
VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(256)
VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT = VkDebugUtilsMessageSeverityFlagBitsEXT(4096)


# ENUM VkDebugUtilsMessageTypeFlagBitsEXT
VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT = VkDebugUtilsMessageTypeFlagBitsEXT(1)
VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT = VkDebugUtilsMessageTypeFlagBitsEXT(2)
VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT = VkDebugUtilsMessageTypeFlagBitsEXT(4)


# ENUM VkConservativeRasterizationModeEXT
VK_CONSERVATIVE_RASTERIZATION_MODE_DISABLED_EXT = VkConservativeRasterizationModeEXT(0)
VK_CONSERVATIVE_RASTERIZATION_MODE_OVERESTIMATE_EXT = VkConservativeRasterizationModeEXT(1)
VK_CONSERVATIVE_RASTERIZATION_MODE_UNDERESTIMATE_EXT = VkConservativeRasterizationModeEXT(2)


# ENUM VkDescriptorBindingFlagBits
VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT = VkDescriptorBindingFlagBits(1)
VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT = VkDescriptorBindingFlagBits(2)
VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT = VkDescriptorBindingFlagBits(4)
VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT = VkDescriptorBindingFlagBits(8)


# ENUM VkVendorId
VK_VENDOR_ID_VIV = VkVendorId(0x10001)
VK_VENDOR_ID_VSI = VkVendorId(0x10002)
VK_VENDOR_ID_KAZAN = VkVendorId(0x10003)
VK_VENDOR_ID_CODEPLAY = VkVendorId(0x10004)
VK_VENDOR_ID_MESA = VkVendorId(0x10005)


# ENUM VkDriverId
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


# ENUM VkConditionalRenderingFlagBitsEXT
VK_CONDITIONAL_RENDERING_INVERTED_BIT_EXT = VkConditionalRenderingFlagBitsEXT(1)


# ENUM VkResolveModeFlagBits
VK_RESOLVE_MODE_NONE = VkResolveModeFlagBits(0)
VK_RESOLVE_MODE_SAMPLE_ZERO_BIT = VkResolveModeFlagBits(1)
VK_RESOLVE_MODE_AVERAGE_BIT = VkResolveModeFlagBits(2)
VK_RESOLVE_MODE_MIN_BIT = VkResolveModeFlagBits(4)
VK_RESOLVE_MODE_MAX_BIT = VkResolveModeFlagBits(8)


# ENUM VkShadingRatePaletteEntryNV
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


# ENUM VkCoarseSampleOrderTypeNV
VK_COARSE_SAMPLE_ORDER_TYPE_DEFAULT_NV = VkCoarseSampleOrderTypeNV(0)
VK_COARSE_SAMPLE_ORDER_TYPE_CUSTOM_NV = VkCoarseSampleOrderTypeNV(1)
VK_COARSE_SAMPLE_ORDER_TYPE_PIXEL_MAJOR_NV = VkCoarseSampleOrderTypeNV(2)
VK_COARSE_SAMPLE_ORDER_TYPE_SAMPLE_MAJOR_NV = VkCoarseSampleOrderTypeNV(3)


# ENUM VkGeometryInstanceFlagBitsKHR
VK_GEOMETRY_INSTANCE_TRIANGLE_FACING_CULL_DISABLE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(1)
VK_GEOMETRY_INSTANCE_TRIANGLE_FRONT_COUNTERCLOCKWISE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(2)
VK_GEOMETRY_INSTANCE_FORCE_OPAQUE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(4)
VK_GEOMETRY_INSTANCE_FORCE_NO_OPAQUE_BIT_KHR = VkGeometryInstanceFlagBitsKHR(8)


# ENUM VkGeometryFlagBitsKHR
VK_GEOMETRY_OPAQUE_BIT_KHR = VkGeometryFlagBitsKHR(1)
VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR = VkGeometryFlagBitsKHR(2)


# ENUM VkBuildAccelerationStructureFlagBitsKHR
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(1)
VK_BUILD_ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(2)
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(4)
VK_BUILD_ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(8)
VK_BUILD_ACCELERATION_STRUCTURE_LOW_MEMORY_BIT_KHR = VkBuildAccelerationStructureFlagBitsKHR(16)


# ENUM VkAccelerationStructureCreateFlagBitsKHR
VK_ACCELERATION_STRUCTURE_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = VkAccelerationStructureCreateFlagBitsKHR(1)


# ENUM VkCopyAccelerationStructureModeKHR
VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_KHR = VkCopyAccelerationStructureModeKHR(0)
VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_KHR = VkCopyAccelerationStructureModeKHR(1)
VK_COPY_ACCELERATION_STRUCTURE_MODE_SERIALIZE_KHR = VkCopyAccelerationStructureModeKHR(2)
VK_COPY_ACCELERATION_STRUCTURE_MODE_DESERIALIZE_KHR = VkCopyAccelerationStructureModeKHR(3)


# ENUM VkBuildAccelerationStructureModeKHR
VK_BUILD_ACCELERATION_STRUCTURE_MODE_BUILD_KHR = VkBuildAccelerationStructureModeKHR(0)
VK_BUILD_ACCELERATION_STRUCTURE_MODE_UPDATE_KHR = VkBuildAccelerationStructureModeKHR(1)


# ENUM VkAccelerationStructureTypeKHR
VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR = VkAccelerationStructureTypeKHR(0)
VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR = VkAccelerationStructureTypeKHR(1)
VK_ACCELERATION_STRUCTURE_TYPE_GENERIC_KHR = VkAccelerationStructureTypeKHR(2)


# ENUM VkGeometryTypeKHR
VK_GEOMETRY_TYPE_TRIANGLES_KHR = VkGeometryTypeKHR(0)
VK_GEOMETRY_TYPE_AABBS_KHR = VkGeometryTypeKHR(1)
VK_GEOMETRY_TYPE_INSTANCES_KHR = VkGeometryTypeKHR(2)


# ENUM VkAccelerationStructureMemoryRequirementsTypeNV
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_OBJECT_NV = VkAccelerationStructureMemoryRequirementsTypeNV(0)
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_BUILD_SCRATCH_NV = VkAccelerationStructureMemoryRequirementsTypeNV(1)
VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_UPDATE_SCRATCH_NV = VkAccelerationStructureMemoryRequirementsTypeNV(2)


# ENUM VkAccelerationStructureBuildTypeKHR
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_KHR = VkAccelerationStructureBuildTypeKHR(0)
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR = VkAccelerationStructureBuildTypeKHR(1)
VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_OR_DEVICE_KHR = VkAccelerationStructureBuildTypeKHR(2)


# ENUM VkRayTracingShaderGroupTypeKHR
VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_KHR = VkRayTracingShaderGroupTypeKHR(0)
VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_KHR = VkRayTracingShaderGroupTypeKHR(1)
VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_KHR = VkRayTracingShaderGroupTypeKHR(2)


# ENUM VkAccelerationStructureCompatibilityKHR
VK_ACCELERATION_STRUCTURE_COMPATIBILITY_COMPATIBLE_KHR = VkAccelerationStructureCompatibilityKHR(0)
VK_ACCELERATION_STRUCTURE_COMPATIBILITY_INCOMPATIBLE_KHR = VkAccelerationStructureCompatibilityKHR(1)


# ENUM VkShaderGroupShaderKHR
VK_SHADER_GROUP_SHADER_GENERAL_KHR = VkShaderGroupShaderKHR(0)
VK_SHADER_GROUP_SHADER_CLOSEST_HIT_KHR = VkShaderGroupShaderKHR(1)
VK_SHADER_GROUP_SHADER_ANY_HIT_KHR = VkShaderGroupShaderKHR(2)
VK_SHADER_GROUP_SHADER_INTERSECTION_KHR = VkShaderGroupShaderKHR(3)


# ENUM VkMemoryOverallocationBehaviorAMD
VK_MEMORY_OVERALLOCATION_BEHAVIOR_DEFAULT_AMD = VkMemoryOverallocationBehaviorAMD(0)
VK_MEMORY_OVERALLOCATION_BEHAVIOR_ALLOWED_AMD = VkMemoryOverallocationBehaviorAMD(1)
VK_MEMORY_OVERALLOCATION_BEHAVIOR_DISALLOWED_AMD = VkMemoryOverallocationBehaviorAMD(2)


# ENUM VkFramebufferCreateFlagBits


# ENUM VkScopeNV
VK_SCOPE_DEVICE_NV = VkScopeNV(1)
VK_SCOPE_WORKGROUP_NV = VkScopeNV(2)
VK_SCOPE_SUBGROUP_NV = VkScopeNV(3)
VK_SCOPE_QUEUE_FAMILY_NV = VkScopeNV(5)


# ENUM VkComponentTypeNV
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


# ENUM VkDeviceDiagnosticsConfigFlagBitsNV
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_SHADER_DEBUG_INFO_BIT_NV = VkDeviceDiagnosticsConfigFlagBitsNV(1)
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_RESOURCE_TRACKING_BIT_NV = VkDeviceDiagnosticsConfigFlagBitsNV(2)
VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_AUTOMATIC_CHECKPOINTS_BIT_NV = VkDeviceDiagnosticsConfigFlagBitsNV(4)


# ENUM VkPipelineCreationFeedbackFlagBitsEXT
VK_PIPELINE_CREATION_FEEDBACK_VALID_BIT_EXT = VkPipelineCreationFeedbackFlagBitsEXT(1)
VK_PIPELINE_CREATION_FEEDBACK_APPLICATION_PIPELINE_CACHE_HIT_BIT_EXT = VkPipelineCreationFeedbackFlagBitsEXT(2)
VK_PIPELINE_CREATION_FEEDBACK_BASE_PIPELINE_ACCELERATION_BIT_EXT = VkPipelineCreationFeedbackFlagBitsEXT(4)


# ENUM VkFullScreenExclusiveEXT
VK_FULL_SCREEN_EXCLUSIVE_DEFAULT_EXT = VkFullScreenExclusiveEXT(0)
VK_FULL_SCREEN_EXCLUSIVE_ALLOWED_EXT = VkFullScreenExclusiveEXT(1)
VK_FULL_SCREEN_EXCLUSIVE_DISALLOWED_EXT = VkFullScreenExclusiveEXT(2)
VK_FULL_SCREEN_EXCLUSIVE_APPLICATION_CONTROLLED_EXT = VkFullScreenExclusiveEXT(3)


# ENUM VkPerformanceCounterScopeKHR
VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR = VkPerformanceCounterScopeKHR(0)
VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR = VkPerformanceCounterScopeKHR(1)
VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR = VkPerformanceCounterScopeKHR(2)
VK_QUERY_SCOPE_COMMAND_BUFFER_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR
VK_QUERY_SCOPE_RENDER_PASS_KHR = VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR
VK_QUERY_SCOPE_COMMAND_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR


# ENUM VkPerformanceCounterUnitKHR
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


# ENUM VkPerformanceCounterStorageKHR
VK_PERFORMANCE_COUNTER_STORAGE_INT32_KHR = VkPerformanceCounterStorageKHR(0)
VK_PERFORMANCE_COUNTER_STORAGE_INT64_KHR = VkPerformanceCounterStorageKHR(1)
VK_PERFORMANCE_COUNTER_STORAGE_UINT32_KHR = VkPerformanceCounterStorageKHR(2)
VK_PERFORMANCE_COUNTER_STORAGE_UINT64_KHR = VkPerformanceCounterStorageKHR(3)
VK_PERFORMANCE_COUNTER_STORAGE_FLOAT32_KHR = VkPerformanceCounterStorageKHR(4)
VK_PERFORMANCE_COUNTER_STORAGE_FLOAT64_KHR = VkPerformanceCounterStorageKHR(5)


# ENUM VkPerformanceCounterDescriptionFlagBitsKHR
VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR = VkPerformanceCounterDescriptionFlagBitsKHR(1)
VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_KHR = VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR
VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR = VkPerformanceCounterDescriptionFlagBitsKHR(2)
VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_KHR = VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR


# ENUM VkAcquireProfilingLockFlagBitsKHR


# ENUM VkShaderCorePropertiesFlagBitsAMD


# ENUM VkPerformanceConfigurationTypeINTEL
VK_PERFORMANCE_CONFIGURATION_TYPE_COMMAND_QUEUE_METRICS_DISCOVERY_ACTIVATED_INTEL = VkPerformanceConfigurationTypeINTEL(0)


# ENUM VkQueryPoolSamplingModeINTEL
VK_QUERY_POOL_SAMPLING_MODE_MANUAL_INTEL = VkQueryPoolSamplingModeINTEL(0)


# ENUM VkPerformanceOverrideTypeINTEL
VK_PERFORMANCE_OVERRIDE_TYPE_NULL_HARDWARE_INTEL = VkPerformanceOverrideTypeINTEL(0)
VK_PERFORMANCE_OVERRIDE_TYPE_FLUSH_GPU_CACHES_INTEL = VkPerformanceOverrideTypeINTEL(1)


# ENUM VkPerformanceParameterTypeINTEL
VK_PERFORMANCE_PARAMETER_TYPE_HW_COUNTERS_SUPPORTED_INTEL = VkPerformanceParameterTypeINTEL(0)
VK_PERFORMANCE_PARAMETER_TYPE_STREAM_MARKER_VALID_BITS_INTEL = VkPerformanceParameterTypeINTEL(1)


# ENUM VkPerformanceValueTypeINTEL
VK_PERFORMANCE_VALUE_TYPE_UINT32_INTEL = VkPerformanceValueTypeINTEL(0)
VK_PERFORMANCE_VALUE_TYPE_UINT64_INTEL = VkPerformanceValueTypeINTEL(1)
VK_PERFORMANCE_VALUE_TYPE_FLOAT_INTEL = VkPerformanceValueTypeINTEL(2)
VK_PERFORMANCE_VALUE_TYPE_BOOL_INTEL = VkPerformanceValueTypeINTEL(3)
VK_PERFORMANCE_VALUE_TYPE_STRING_INTEL = VkPerformanceValueTypeINTEL(4)


# ENUM VkShaderFloatControlsIndependence
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY = VkShaderFloatControlsIndependence(0)
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL = VkShaderFloatControlsIndependence(1)
VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE = VkShaderFloatControlsIndependence(2)


# ENUM VkPipelineExecutableStatisticFormatKHR
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_BOOL32_KHR = VkPipelineExecutableStatisticFormatKHR(0)
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_INT64_KHR = VkPipelineExecutableStatisticFormatKHR(1)
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_UINT64_KHR = VkPipelineExecutableStatisticFormatKHR(2)
VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_FLOAT64_KHR = VkPipelineExecutableStatisticFormatKHR(3)


# ENUM VkLineRasterizationModeEXT
VK_LINE_RASTERIZATION_MODE_DEFAULT_EXT = VkLineRasterizationModeEXT(0)
VK_LINE_RASTERIZATION_MODE_RECTANGULAR_EXT = VkLineRasterizationModeEXT(1)
VK_LINE_RASTERIZATION_MODE_BRESENHAM_EXT = VkLineRasterizationModeEXT(2)
VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_EXT = VkLineRasterizationModeEXT(3)


# ENUM VkShaderModuleCreateFlagBits


# ENUM VkPipelineCompilerControlFlagBitsAMD


# ENUM VkToolPurposeFlagBitsEXT
VK_TOOL_PURPOSE_VALIDATION_BIT_EXT = VkToolPurposeFlagBitsEXT(1)
VK_TOOL_PURPOSE_PROFILING_BIT_EXT = VkToolPurposeFlagBitsEXT(2)
VK_TOOL_PURPOSE_TRACING_BIT_EXT = VkToolPurposeFlagBitsEXT(4)
VK_TOOL_PURPOSE_ADDITIONAL_FEATURES_BIT_EXT = VkToolPurposeFlagBitsEXT(8)
VK_TOOL_PURPOSE_MODIFYING_FEATURES_BIT_EXT = VkToolPurposeFlagBitsEXT(16)


# ENUM VkFragmentShadingRateCombinerOpKHR
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_KEEP_KHR = VkFragmentShadingRateCombinerOpKHR(0)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_REPLACE_KHR = VkFragmentShadingRateCombinerOpKHR(1)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MIN_KHR = VkFragmentShadingRateCombinerOpKHR(2)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR = VkFragmentShadingRateCombinerOpKHR(3)
VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MUL_KHR = VkFragmentShadingRateCombinerOpKHR(4)


# ENUM VkFragmentShadingRateNV
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


# ENUM VkFragmentShadingRateTypeNV
VK_FRAGMENT_SHADING_RATE_TYPE_FRAGMENT_SIZE_NV = VkFragmentShadingRateTypeNV(0)
VK_FRAGMENT_SHADING_RATE_TYPE_ENUMS_NV = VkFragmentShadingRateTypeNV(1)
