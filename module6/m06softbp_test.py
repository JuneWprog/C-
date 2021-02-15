import ctypes
import m06softbp
import msvcrt

debugger =m06softbp.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.get_debug_event()
printf_address = debugger.func_resolve("msvcrt.dll","printf")
print "[*] Address of printf: 0x%08x" % printf_address
debugger.bp_set(printf_address)
debugger.run()
 


