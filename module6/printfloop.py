from ctypes import *
import threading
import os,sys
msvcrt = cdll.msvcrt

def printloop():
    pid=os.getpid()
    msvcrt.printf("My pid: %d \n",pid)
    sys.stdout.flush()
    threading.Timer(2.0, printloop).start()
printloop()