#!/usr/bin/python
# will dump ELF file header and identify its parameters

import sys,os
import struct

if len(sys.argv)==1:
    print """need an executable file name"""
    sys.exit(-1)
else:
    filename=sys.argv[1]
    print """File   : %s""" %(filename)
    fd=open(filename,'rb')
    header=fd.read(6)
    magic,form,endian=struct.unpack("IBB",header)
    print """Magic  :""", hex(magic)
    if form==1:
        print """Format : %s""" %('32 bit')
    else:
         print """Format : %s""" %('64 bit')
    if endian==1:
        print """Endian : %s""" %('little')
    else:
         print """Endian : %s""" %('big')
    fd.seek(18,0)
    data=fd.read(2)
    machine=struct.unpack('h',data)[0]
    if machine==0x02:
        val='SPARC'
    elif machine==0x03:
        val='x86'
    elif machine==0x08:
        val='MIPS'
    elif machine==0x14:
        val='PowerPC'
    elif machine==0x16:
        val='S390'
    elif machine==0x28:
        val='ARM'
    elif machine==0x2A:
        val='SuperH'
    elif machine==0x32:
        val='IA-64'
    elif machine==0x3E:
        val='x86-64'
    elif machine==0xB7:
        val='AArch64'
    elif machine==0xF3:
        val='RISC-V'
        
    print """Machine: %s""" %(val)
