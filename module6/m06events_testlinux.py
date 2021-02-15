import ctypes
import m06events
import sys

debugger = m06events.debugger()

print"Enter the PID of the process to attach to: "
sys.stdout.flush()
pid = raw_input()
debugger.attach(int(pid))
debugger.get_debug_event()

while (1):
    print("Press 'q/Q' to quit, press ENTER to continue")
    sys.stdout.flush()
    command =raw_input()
    if command == 'q'or command=='Q':
        debugger.detach()
        break
