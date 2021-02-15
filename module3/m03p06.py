#!/usr/bin/python
# For each Program Header entry, dump at least the p_type, p_offset, p_vaddr, p_filesz and p_memsz.
#For each Section Header, dump at least Name, Type, Address, Offset and Size.
import struct
import sys

def findType(t):
    if t==0x0:
        v='SHT_NULL'
    elif t==0x1:
        v='SHT_PROGBITS'
    elif t==0x2:
        v='SHT_SYMTAB'
    elif t==0x3:
        v='SHT_STRTAB'
    elif t==0x4:
        v='SHT_RELA'
    elif t==0x5:
        v='SHT_HASH'
    elif t==0x6:
        v='SHT_DYNAMIC'
    elif t==0x7:
        v='SHT_NOTE'
    elif t==0x8:
        v='SHT_NOBITS'
    elif t==0x9:
        v='SHT_REL'
    elif t==0x0A:
        v='SHT_SHLIB'
    elif t==0x0B:
        v='SHT_DYNSYM'
    elif t==0x0E:
        v='SHT_INIT_ARRAY'
    elif t==0x0F:
        v='SHT_FINI_ARRAY'
    elif t==0x10:
        v='SHT_PREINI_ARRAY'
    elif t==0x11:
        v='SHT_GROUP'
    elif t==0x12:
        v='SHT_SYMTAB_SHNDX'
    elif t==0x13:
        v='SHT_NUM'
    elif t==0x60000000:
        v='SHT_LOOS'

    return v

def find_p_type(t):
    if t==0x00000000:
        v='PT_NULL'
    elif t==0x00000001:
        v='PT_LOAD'
    elif t==0x00000002:
        v='PT_DYNAMIC'
    elif t==0x00000003:
        v='PT_INTERP'
    elif t==0x00000004:
        v='PT_NOTE'
    elif t==0x00000005:
        v='PT__SHLIB'
    elif t==0x00000006:
        v='PT_PHDR'
    elif t==0x60000000:
        v='PT_LOOS'
    elif t==0x6FFFFFFF:
        v='PT_HIOS'
    elif t==0x70000000:
        v='PT_LOPROC'
    elif t==0x7FFFFFFF:
        v='PT_HIPROC'
    return v


if len(sys.argv)<2:
    print"""need an file name"""
else:
    filename=sys.argv[1]
    fd=open (filename, 'rb')    
    fd.seek(62,0)
    strtable=fd.read(2)
    stable=struct.unpack("H",strtable)[0]
   
    fd.seek(64,0)
    h1=fd.read(4)
    p_type=struct.unpack("I", h1)[0]
    ptype=find_p_type(p_type)
    fd.seek(72,0)
    h2=fd.read(32)
    p_offset, p_vaddr, p_filesz,p_memsz=struct.unpack("QQQQ", h2)

    fd.seek(120,0)
    s1=fd.read(8)
    Name, Type=struct.unpack("II", s1)
    
    sh_type=findType(Type)
    fd.seek(136,0)
    s2 =fd.read(24)
    Address, Offset, Size=struct.unpack("QQQ", s2)

  
    print '''String Table Index: ''',stable 
    print '''Program Type      :''', ptype
    print '''Program Offset    :''', hex(p_offset)
    print '''Program Vaddr     :''',hex(p_vaddr)
    print '''File Size         :''', p_filesz/1024, 'KB'
    print '''Memory Size       :''', p_memsz/1024,'KB'
    print '''Section Name      :''', Name
    print '''Section Type      :''',sh_type
    print '''Section Address   :''',hex(Address)
    print '''Section Offset    :''',hex(Offset)
    print '''Section Size      :''',Size/1024, 'KB'
    
    
