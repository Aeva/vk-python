
import os
import re
import ctypes
import bs4


# Khronos Vulkan API registry specification:
# https://www.khronos.org/registry/vulkan/specs/1.2/registry.html

REGISTRY_URL = "https://raw.githubusercontent.com/KhronosGroup/Vulkan-Docs/main/xml/vk.xml"


SDK_PATH = os.environ["VULKAN_SDK"]
assert(os.path.isdir(SDK_PATH))
XML_PATH = os.path.join(SDK_PATH, "share", "vulkan", "registry", "vk.xml")
assert(os.path.isfile(XML_PATH))
with open(XML_PATH, 'r') as infile:
    REGISTRY = bs4.BeautifulSoup(infile.read(), 'html.parser')


def rewrite_type(typename):
    basic = {
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


def find_one(tag, *args, **kargs):
    found = tag.find_all(*args, **kargs)
    if len(found) == 0:
        return None
    else:
        assert(len(found) == 1)
        return found[0]


common_constants = {
    "(~0U)" : "0xFFFFFFFF",
    "(~0U-1)" : "0xFFFFFFFF - 1",
    "(~0U-2)" : "0xFFFFFFFF - 2",
    "(~0ULL)" : "0xFFFFFFFFFFFFFFFF",
}


def parse_type(c_noise):
    match = re.match(r'^(\w[A-Za-z0-9_* ]+?)\s+(\w[A-Za-z0-9_]*)(\[[A-Za-z0-9_\[\]]*\])?(:\d+)?$', c_noise)
    assert(match is not None)
    m_type, m_name, m_subscript, m_bitfield = match.groups()
    if m_subscript:
        assert(m_bitfield is None)
        m_subscript = re.findall(r'\[([^\[\]]*)\]', m_subscript)
        assert(len(m_subscript) > 0)
    if m_bitfield:
        assert(m_subscript is None)
        m_bitfield = m_bitfield[1:]

    scrub = re.sub(r'(const|struct|union)', '', m_type).strip()
    match = re.match(r'^(\w[A-Za-z0-9_]*)([* ]+)?$', scrub)
    assert(match is not None)
    m_type, pointers = match.groups()
    if pointers:
        pointers = pointers.count("*")
    else:
        pointers = 0
    if m_type == "void":
        if pointers > 0:
            m_type = "ctypes.c_void_p"
            pointers -= 1
        else:
            m_type = "None"
    m_type = rewrite_type(m_type)
    if m_subscript:
        m_type = f"({m_type} * ({' * '.join(m_subscript)}))"
    for i in range(pointers):
        m_type = f"ctypes.POINTER({m_type})"
    return m_type, m_name, m_bitfield


class vk_type:
    def __init__(self, tag):
        self.requires = tag.get("requires")
        self.name = tag.get("name")
        self.alias = tag.get("alias")
        self.ctype = None
        if self.name is None:
            name = find_one(tag, "name")
            if name:
                self.name = name.text
        assert(self.name)

    def __str__(self):
        assert(self.name is not None)
        if self.alias:
            return f"{self.name} = {self.alias}\n"
        elif self.ctype:
            return f"{self.name} = type('{self.name}', ({self.ctype},), dict())\n"
        else:
            return f"# {self.name}\n"


class vk_basetype(vk_type):
    def __init__(self, tag):
        super().__init__(tag)
        if not self.alias:
            typedef = find_one(tag, "type")
            if typedef:
                # basetype is a typedef, probably
                self.ctype = rewrite_type(typedef.text)
            else:
                # basetype is an empty struct, probably
                self.ctype = f"ctypes.Structure"


class vk_bitmask(vk_type):
    def __init__(self, tag):
        super().__init__(tag)
        if not self.alias:
            typedef = find_one(tag, "type")
            assert(typedef is not None)
            self.ctype = rewrite_type(typedef.text)


class vk_handle(vk_type):
    def __init__(self, tag):
        super().__init__(tag)
        if not self.alias:
            typedef = find_one(tag, "type")
            assert(typedef is not None)
            assert(typedef.text in ["VK_DEFINE_HANDLE", "VK_DEFINE_NON_DISPATCHABLE_HANDLE"])
            self.ctype = "ctypes.Structure"


class vk_enum_value():
    def __init__(self, tag, enum_type):
        self.type = enum_type
        self.name = tag.get("name")
        self.value = tag.get("value")
        self.alias = tag.get("alias")
        self.sign = "-" if tag.get("dir") is not None else ""
        assert(self.name is not None)
        if self.alias:
            assert(self.value is None)
        elif self.value is None:
            bitpos = tag.get("bitpos")
            if bitpos:
                self.value = 1 << int(bitpos)
            else:
                offset = tag.get("offset")
                assert(offset is not None)
                ext_tag = tag.parent.parent
                assert(ext_tag.name in ["extension", "feature"])
                extnumber = tag.get("extnumber") or ext_tag.get("number")
                assert(extnumber is not None)
                self.value = 1000000000 + (int(extnumber) - 1) * 1000 + int(offset)
            assert(self.value is not None)
        if self.value:
            if self.value in common_constants:
                self.value = common_constants.get(self.value)
            if type(self.value) == str and self.value.endswith("f"):
                self.value = self.value[:-1]

    def __str__(self):
        if self.alias:
            return f"{self.name} = {self.alias}\n"
        elif self.type:
            return f"{self.name} = {self.type}({self.sign}{self.value})\n"
        else:
            return f"{self.name} = {self.sign}{self.value}\n"


class vk_enum(vk_type):
    def __init__(self, tag, soup):
        if tag is not None:
            super().__init__(tag)
            self.ctype = rewrite_type("int")
            type_name = self.name
        else:
            self.name = "API Constants"
            self.alias = None
            self.ctype = None
            type_name = None
        enums_tag = find_one(soup, "enums", attrs={"name":self.name})
        self.enums = []
        if enums_tag:
            for enum_tag in enums_tag.find_all("enum"):
                value = vk_enum_value(enum_tag, type_name)
                self.enums.append(value)
        for enum_tag in soup.find_all("enum", extends=self.name):
            ext_tag = enum_tag.parent.parent
            if ext_tag.name in ["extension", "feature"]:
                if ext_tag.get("supported") != "disabled":
                    value = vk_enum_value(enum_tag, type_name)
                    self.enums.append(value)

    def __str__(self):
        src = super().__str__()
        for enum in self.enums:
            src += str(enum)
        return src


class vk_funcpointer(vk_type):
    def __init__(self, tag):
        super().__init__(tag)
        lines = [i.strip() for i in tag.text.split("\n")]
        match = re.match(r'^typedef\s*(\w[A-Za-z0-9_*]*)\s*\(', lines.pop(0))
        assert(match is not None)
        r_type, r_name, r_bitfield = parse_type(match.groups()[0] + " name")
        assert(r_bitfield is None)
        self.args = [r_type]
        for line in lines:
            line = line.strip()
            if not line:
                continue
            line = re.sub(r'(,|\);)$', '', line)
            a_type, a_name, a_bitfield = parse_type(line)
            assert(a_bitfield is None)
            assert(a_type != "None")
            self.args.append(a_type)

    def __str__(self):
        assert(self.alias is None)
        args = ", ".join(self.args)
        return f"{self.name} = VK_FUNCTYPE({args})\n"


class vk_struct(vk_type):
    def __init__(self, tag):
        super().__init__(tag)
        self.kind = "Structure"
        for child in tag.find_all("comment"):
            child.replace_with("")
        for child in tag.find_all("type"):
            # VkBufferViewCreateInfo has problems without this :|
            child.insert_after(" ")
        lines = tag.text.strip().split("\n")
        self.fields = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            m_type, m_name, m_bitfield = parse_type(line)
            assert(m_type != "None")
            self.fields.append((m_type, m_name, m_bitfield))

    def declare(self):
        if self.alias:
            return f"{self.name} = type('{self.name}', ({self.alias},), dict())\n"
        else:
            return f"{self.name} = type('{self.name}', (ctypes.{self.kind},), dict())\n"

    def define(self):
        if self.alias:
            return ""
        else:
            fields = ", ".join([f"('{n}', {t}, {b})" if b else f"('{n}', {t})" for (t, n, b) in self.fields])
            return f"{self.name}._fields_ = [{fields}]\n"


class vk_union(vk_struct):
    def __init__(self, tag):
        super().__init__(tag)
        self.kind = "Union"


class vk_boilerplate:
    def __init__(self, soup):
        self.basetypes = []
        self.bitmasks = []
        self.handles = []
        self.enums = []
        self.funcpointers = []
        self.structs = []

        # API Constants
        self.enums.append(vk_enum(None, soup))

        categories = ('basetype', 'bitmask', 'handle', 'enum', 'funcpointer', 'struct', 'union')
        for types_tag in soup.find_all("types"):
            for type_tag in types_tag.find_all("type"):
                category = type_tag.get("category")
                if category == "basetype":
                    self.basetypes.append(vk_basetype(type_tag))
                elif category == "bitmask":
                    self.bitmasks.append(vk_bitmask(type_tag))
                elif category == "handle":
                    self.handles.append(vk_handle(type_tag))
                elif category == "enum":
                    self.enums.append(vk_enum(type_tag, soup))
                elif category == "funcpointer":
                    self.funcpointers.append(vk_funcpointer(type_tag))
                elif category == "struct":
                    self.structs.append(vk_struct(type_tag))
                elif category == "union":
                    self.structs.append(vk_union(type_tag))

    def __str__(self):
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

#=============================================================================#
# The remainder of this file was generated automatically from the Vulkan API  #
# Registry XML file.                                                          #
#=============================================================================#

"""
        src += "".join(map(str, self.basetypes)) + "\n"
        src += "".join(map(str, self.bitmasks)) + "\n"
        src += "".join(map(str, self.handles)) + "\n"
        src += "\n".join(map(str, self.enums)) + "\n"
        src += "".join(map(lambda x: x.declare(), self.structs)) + "\n"
        src += "".join(map(str, self.funcpointers)) + "\n"
        src += "".join(map(lambda x: x.define(), self.structs)) + "\n"
        return src

boilerplate = vk_boilerplate(REGISTRY)
if __name__ == "__main__":
    with open("vulkan.py", 'w') as outfile:
        outfile.write(str(boilerplate))
