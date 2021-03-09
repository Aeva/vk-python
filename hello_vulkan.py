
import time
import sdl2
import sdl2.ext
import sdl2.vulkan
from vulkan import *
from ctypes import *


class VulkanWindow:
    def __init__(self, title, width, height, position=None, flags=0, validate=True):
        flags = flags | sdl2.SDL_WINDOW_VULKAN
        self.width = width
        self.height = height
        self.sdl_window = sdl2.ext.Window(title, size=(width, height), flags=flags)
        window = self.sdl_window.window

        AppInfo = VkApplicationInfo()
        AppInfo.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO
        AppInfo.pNext = None
        AppInfo.pApplicationName = title.encode()
        AppInfo.applicationVersion = 1
        AppInfo.pEngineName = title.encode()
        AppInfo.engineVersion = 0
        AppInfo.apiVersion = VK_API_VERSION_1_0

        InstanceExtensionCount = c_uint32()
        sdl2.vulkan.SDL_Vulkan_GetInstanceExtensions(window, byref(InstanceExtensionCount), None)
        InstanceExtensions = (c_char_p * InstanceExtensionCount.value)()
        sdl2.vulkan.SDL_Vulkan_GetInstanceExtensions(window, byref(InstanceExtensionCount), InstanceExtensions)

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
        CreateInfo.enabledLayerCount = 1 if validate else 0
        CreateInfo.ppEnabledLayerNames = pointer(ValidationLayer) if validate else None

        self.instance = VkInstance()
        result = vkCreateInstance(byref(CreateInfo), None, byref(self.instance))
        assert(result == VK_SUCCESS)

        self.surface = VkSurfaceKHR()
        sdl2.vulkan.SDL_Vulkan_CreateSurface(
            window,
            cast(pointer(self.instance), POINTER(sdl2.vulkan.VkInstance)).contents,
            cast(pointer(self.surface), POINTER(sdl2.vulkan.VkSurfaceKHR)))
        assert(self.surface)

    def shutdown(self):
        vkDestroySurfaceKHR(self.instance, self.surface, None)

    def pump_events(self):
        return not sdl2.SDL_QuitRequested()


if __name__ == "__main__":
    sdl2.ext.init()
    window = VulkanWindow("Hello World!", 800, 600, flags=sdl2.SDL_WINDOW_RESIZABLE)
    while window.pump_events():
        time.sleep(0.01)
    window.shutdown()
    sdl2.ext.quit()
