import m06membreak
import msvcrt

debugger = m06membreak.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.get_debug_event()
printf = debugger.func_resolve("msvcrt.dll","printf")
print "[*] Address of printf: 0x%08x" % printf

debugger.bp_set_mem (printf,debugger.page_size)

debugger.run()
        