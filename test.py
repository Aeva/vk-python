
import sdl2
import sdl2.ext
import sdl2.vulkan

from vulkan import *
from ctypes import *


window = sdl2.ext.Window("test", size=(512, 512), flags=sdl2.SDL_WINDOW_VULKAN)

AppInfo = VkApplicationInfo()
AppInfo.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO
AppInfo.pNext = None
AppInfo.pApplicationName = b"test application name"
AppInfo.applicationVersion = 1
AppInfo.pEngineName = b"test engine name"
AppInfo.engineVersion = 0
AppInfo.apiVersion = VK_API_VERSION_1_0

InstanceExtensionCount = c_uint32()
sdl2.vulkan.SDL_Vulkan_GetInstanceExtensions(window.window, byref(InstanceExtensionCount), None)
InstanceExtensions = (c_char_p * InstanceExtensionCount.value)()
sdl2.vulkan.SDL_Vulkan_GetInstanceExtensions(window.window, byref(InstanceExtensionCount), InstanceExtensions)

print("Found the following instance extensions:")
for extension in InstanceExtensions:
	print(f" - {extension.decode('utf-8')}")

ValidationLayer = c_char_p(b"VK_LAYER_KHRONOS_validation")

CreateInfo = VkInstanceCreateInfo()
CreateInfo.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
CreateInfo.pNext = None
CreateInfo.flags = 0
CreateInfo.pApplicationInfo = pointer(AppInfo)
CreateInfo.enabledExtensionCount = InstanceExtensionCount
CreateInfo.ppEnabledExtensionNames = InstanceExtensions
CreateInfo.enabledLayerCount = 1
CreateInfo.ppEnabledLayerNames = pointer(ValidationLayer)

Instance = VkInstance()
result = vkCreateInstance(byref(CreateInfo), None, byref(Instance))
assert(result.value == VK_SUCCESS.value)

Surface = VkSurfaceKHR()
sdl2.vulkan.SDL_Vulkan_CreateSurface(window.window, cast(pointer(Instance), POINTER(sdl2.vulkan.VkInstance)).contents, cast(pointer(Surface), POINTER(sdl2.vulkan.VkSurfaceKHR)))

vkDestroySurfaceKHR(Instance, Surface, None)
