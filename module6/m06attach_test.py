import m06attach
from my_debugger_defines import *
import sys


print"Enter the PID of the process to attach to: "
sys.stdout.flush()
pid = raw_input()

debugger = m06attach.debugger()
debugger.attach(int(pid))
debugger.detach()

