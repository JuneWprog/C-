from ctypes import *
#import threading
import os,sys,time

pid=os.getpid()
def printloop():
    print("My pid: %d " %pid)
    sys.stdout.flush()
    
while(1):
    printloop()
    time.sleep(2)