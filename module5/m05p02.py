#!/usr/bin/python
#problem:
#explore Python to C calling convention, using the Python ctypes module. 
#Have the program get the proper parameters about itself (its own process), load the
#library libprintproc.so you just created, and use the printproc() to output the parameters.

from ctypes import *
import sys,os

#import the shared library
lib=CDLL('./libprintproc.so')
#declear the type of return value 
lib.printproc.restrype=c_void_p
#declear the type of parameters of the c_function
lib.printproc.argtypes=[c_char , c_int , c_int , c_ulonglong, c_ulonglong , c_ulonglong, c_ulonglong , c_ulonglong ]

class LinuxProcess:
    def __init__(self,pid):
        fname=os.path.join('/proc',pid,'stat')
        fd=open(fname,'r')
        self.data=fd.read()
        self.statlist=self.data.split(" ")
        self.pid=self.statlist[0]
        self.name=self.statlist[1].strip(")").strip("(")
        self.state=self.statlist[2]
        self.ppid=self.statlist[3]
        self.pgid=self.statlist[4]
        self.rss_lim=int(self.statlist[24])
        self.start_code=self.statlist[25]
        self.end_code=self.statlist[26]
        self.start_stack=self.statlist[27]
        self.esp=self.statlist[28]
        self.eip=self.statlist[29]
        self.start_data=self.statlist[44]
        self.end_data=self.statlist[45]
        self.start_brk=self.statlist[46]
        self.arg_start=self.statlist[47]
        self.arg_end=self.statlist[48]
        self.env_start=self.statlist[49]
        self.env_end=self.statlist[50]

class LinuxProcList():
    def proclist(self):
        self.validpids=[]
        proclists=os.listdir('/proc')
        for oneproc in proclists:
            try:
                pid=int(oneproc)
                if oneproc==str(pid):
                    self.validpids.append(oneproc)
            except:
                pass
        return self.validpids
        
def commandline(pid):
    try:
        fname=os.path.join('/proc',pid,'cmdline')
        fd=open(fname,'r')
        cmdlinestr=fd.read()
        if cmdlinestr=='':
            return "NONE"
        else:
            return cmdlinestr
    except:
        pass

if len(sys.argv)<2:
    print "need a pid number"
else:
    pid=""
    if str.isdigit(sys.argv[1]):
        pid=sys.argv[1]
    else:
        listproc=LinuxProcList()
        listprocn=listproc.proclist()
        for each in listprocn:
            if commandline(each)==sys.argv[1]:
                pid=each
processx=LinuxProcess(pid)
statestr=str(processx.state)
if len (statestr)>1:
    state=statestr[:1]
    print ("State:%24s"%statestr)
else:
    state=statestr
ppid=int(processx.ppid)
pgid=int(processx.pgid)
mm_start_code=int(processx.start_code)
mm_end_code=int(processx.end_code)
mm_start_stack=int(processx.start_stack)
esp=int(processx.esp)
eip=int(processx.eip)
try:
    lib.printproc(state,ppid,pgid,mm_start_code,mm_end_code,mm_start_stack,esp,eip)
except:
    pass
