#!/usr/bin/python
import os,sys,re

#/proc/[pid]/stat

class LinuxProcess:
    def __init__(self,pid):
        fname=os.path.join('/proc',pid,'stat')
        fd=open(fname,'r')
        self.data=fd.read()
        self.statlist=self.data.split(" ")
        self.pid=self.statlist[0]
        self.statlist[1]=self.statlist[1].strip("(")
        self.name=self.statlist[1].strip(")")
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
    def commandline(self,pid):
        try:
            fname=os.path.join('/proc',pid,'cmdline')
            fd=open(fname,'r')
            self.cmdlinestr=fd.read()
            if self.cmdlinestr=='':
                return "NONE"
            elif len(self.cmdlinestr)>133:
                self.cmdlinestr=self.cmdlinestr[:132]
                return self.cmdlinestr
            else:
                return self.cmdlinestr
        except:
            pass
    def children(self,pid):
        pidlist=self.proclist()
        #print pidlist
        self.childrenlist=[]
        for onepid in pidlist:
            fname=os.path.join('/proc',onepid,'stat')
            fd=open(fname,'r')
            data=fd.read()
            statlist=data.split(" ")
            ppid=statlist[3]
            childpid=statlist[4]
            if ppid==pid:
                self.childrenlist.append(onepid)
        return self.childrenlist
lipro=LinuxProcList()
procs=lipro.proclist()

def show(pid,depth=1):
        if lipro.commandline(pid)!="NONE":
            print '  |'*depth,'-', pid, lipro.commandline(pid)
            childlist = lipro.children(pid)
            if childlist!=[]:
                depth += 1
                for c in childlist:
                    show(c, depth)
for p in procs:
    show(p)



