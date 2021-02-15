import sys
# Read in the DLL
FileName=raw_input("Enter the target filename to be attach to:    ")
DllName =raw_input("Enter the .dll filename to be hidden:    ") 
fd1=open( DllName, "rb" )
dll_contents = fd1.read()
fd1.close()
print "[*] Filesize: %d" % len( dll_contents )
# Now write it out to the ADS . target file whose ADS we will be
# storing the DLL in.
fd2= open( "%s:%s" % ( FileName, DllName ), "wb" )
fd2.write( dll_contents )
fd2.close()
