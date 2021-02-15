#!/usr/bin/python
import struct
import os,sys,re
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

class LinuxProcess:
    def __init__(self,pid):
        fname=os.path.join('/proc',pid,'stat')
        fd=open(fname,'r')
        self.data=fd.read()
        self.statlist=self.data.split(" ")
        self.pid=self.statlist[0]
        self.name=self.statlist[1].strip(")").strip("(")
        self.state=self.statlist[2]
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

    
    def printstat(self):
        print """            name:  """,self.name
        #print("             pid:%20s" %(self.pid))
        #print("          states:%20s" %(self.state))
        print("        ress_lim:%20s"%hex(int(self.rss_lim)))
        print("      start_code:%20s"%hex(int(self.start_code)))
        print("        end_code:%20s"%hex(int(self.end_code)))
        print("     start_stack:%20s"%hex(int(self.start_stack)))
        print("             esp:%20s"%hex(int(self.esp)))
        print("             eip:%20s"%hex(int(self.eip)))
        print("      start_data:%20s"%hex(int(self.start_data)))
        print("        end_data:%20s"%hex(int(self.end_data)))
        print("       start_brk:%20s"%hex(int(self.start_brk)))
        print("       arg_start:%20s"%hex(int(self.arg_start)))
        print("         arg_end:%20s"%hex(int(self.arg_end)))
        print("       env_start:%20s"%hex(int(self.env_start)))
        print("         env_end:%20s"%hex(int(self.env_end)))

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
        

lprocess= LinuxProcess(pid)
lprocess.printstat()
#for i in range(len(lprocess.statlist)):
#   print i, lprocess.statlist[i]

