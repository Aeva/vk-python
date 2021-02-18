
import os
import ctypes
import bs4


SDK_PATH = os.environ["VULKAN_SDK"]
assert(os.path.isdir(SDK_PATH))
XML_PATH = os.path.join(SDK_PATH, "share", "vulkan", "registry", "vk.xml")
assert(os.path.isfile(XML_PATH))
with open(XML_PATH, 'r') as infile:
    REGISTRY = bs4.BeautifulSoup(infile.read(), 'html.parser')


src = """

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
"""


def rewrite_type(typename):
    basic = {
        "void" : "ctypes.c_void",
        "char" : "ctypes.c_char",
        "float" : "ctypes.c_float",
        "double" : "ctypes.c_double",
        "uint8_t" : "ctypes.c_uint8",
        "uint16_t" : "ctypes.c_uint16",
        "uint32_t" : "ctypes.c_uint32",
        "uint64_t" : "ctypes.c_uint64",
        "int32_t" : "ctypes.c_int32",
        "int64_t" : "ctypes.c_int64",
        "size_t" : "ctypes.c_size_t",
        "int" : "ctypes.c_int",
    }
    return basic.get(typename) or typename


def specialize(name, ctype):
    return f"{name} = type('{name}', ({ctype},), dict())\n"


src += "\n\n# BASE TYPES\n"
for entry in REGISTRY.find_all("type", category="basetype"):
    name_tag = entry.find_next("name")
    type_tag = entry.find_next("type")
    if name_tag.parent != entry or type_tag.parent != entry:
        continue
    name = name_tag.text
    ctype = rewrite_type(type_tag.text)
    src += specialize(name, ctype)


src += "\n\n# BITMASK TYPES\n"
for entry in REGISTRY.find_all("type", category="bitmask"):
    if entry.get("alias"):
        src += specialize(entry['name'], entry['alias'])
    else:
        name_tag = entry.find_next("name")
        type_tag = entry.find_next("type")
        assert(name_tag.parent == entry)
        assert(type_tag.parent == entry)
        name = name_tag.text
        ctype = rewrite_type(type_tag.text)
        src += specialize(name, ctype)


src += "\n\n# HANDLE TYPES\n"
src += "VK_NULL_HANDLE = 0\n"
for entry in REGISTRY.find_all("type", category="handle"):
    if entry.get("alias"):
        src += f"{entry['name']} = {entry['alias']}\n"
    else:
        name_tag = entry.find_next("name")
        type_tag = entry.find_next("type")
        assert(name_tag.parent == entry)
        assert(type_tag.parent == entry)
        assert(type_tag.text in ["VK_DEFINE_HANDLE", "VK_DEFINE_NON_DISPATCHABLE_HANDLE"])
        name = name_tag.text
        src += f"{name} = ctypes.POINTER(type('{name}', (ctypes.Structure,), dict()))\n"


common_constants = {
    "(~0U)" : "0xFFFFFFFF",
    "(~0U-1)" : "0xFFFFFFFF - 1",
    "(~0U-2)" : "0xFFFFFFFF - 2",
    "(~0ULL)" : "0xFFFFFFFFFFFFFFFF",
}


enum_categories = []
src += "\n\n# ENUM TYPES\n"
for entry in REGISTRY.find_all("type", category="enum"):
    name = entry['name']
    if entry.get("alias"):
        src += f"{name} = {entry['alias']}\n"
    else:
        src += specialize(name, "ctypes.c_int")
    enum_categories.append(name)


for enum_group in REGISTRY.find_all("enums"):
    ctype = enum_group['name'] if enum_group['name'] in enum_categories else None
    if ctype:
        src += f"\n\n# ENUM {enum_group['name']}\n"
    else:
        src += f"\n\n# {enum_group['name']}\n"
    for entry in enum_group.find_all("enum"):
        if entry.get("alias"):
            src += f"{entry['name']} = {entry['alias']}\n"
        elif entry.get("bitpos"):
            name = entry['name']
            value = 1 << int(entry['bitpos'])
            if ctype:
                src += f"{name} = {ctype}({value})\n"
            else:
                src += f"{name} = {value}\n"
        elif entry.get("value"):
            name = entry['name']
            value = common_constants.get(entry['value']) or entry['value']
            if value.endswith("f"):
                value = value[:-1]
            if ctype:
                src += f"{name} = {ctype}({value})\n"
            else:
                src += f"{name} = {value}\n"
        else:
            breakpoint()


if __name__ == "__main__":
    with open("vulkan.py", 'w') as outfile:
        outfile.write(src)
