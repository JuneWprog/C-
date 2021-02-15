import m06events
import msvcrt

debugger = m06events.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.get_debug_event()


