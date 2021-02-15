#!/usr/bin/python
import os,sys,re
import time
#/proc/[pid]/stat

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
if len(sys.argv)<2:
    print"need a pid"
    exit(-1)
else:
    linuxprocess=LinuxProcList()
    liproclist=[]
    liproclist=linuxprocess.proclist()
    print """      valid pid list
    --------------------------------------------"""
    print liproclist
    print"""       command line:  """ ,linuxprocess.commandline(sys.argv[1]) 
    print """      children process pid list
    --------------------------------------------"""
    print linuxprocess.children(sys.argv[1])


