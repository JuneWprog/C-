#!/usr/bin/python
# takes a single parameter, a file name, and prints a hexadecimal dump

import sys

def check_file():
  # This method ensures a valid file was provided to the invoked script ##
  if len(sys.argv) < 2:
    print ""
    print "Error -need one file name "
    sys.exit(0)
  
def read_bytes(filename, chunksize=8192):
  # This method returns the bytes of a provided file ##
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
                else:
                    break

        
def check_printable(s):
  ## This method returns true if a byte is a printable ascii character ##
  return all((ord(c) < 128) and (ord(c) >= 32) for c in s)
  

def validate_byte_as_printable(byte):
  ## Check if byte is a printable ascii character. If not replace with a '.' character ##
  if check_printable(byte):
    return byte
  else:
    return '.'
  
## main ##
check_file()
memory_address = 0
ascii_string = ""


## Loop through the given file while printing the address, hex and ascii output ##
count=0
for byte in read_bytes(sys.argv[1]):
  count+=1
  ascii_string = ascii_string + validate_byte_as_printable(byte)
  if memory_address%16 == 0:
    print( '%08X'%memory_address),
    print(byte.encode('hex')),
  elif memory_address%16 == 15:
    print(byte.encode('hex')),
    print ascii_string
    ascii_string = ""
  else:
    print(byte.encode('hex')),
  memory_address = memory_address + 1

print'\r'
print ('Total length %d (%xh)'%(count,count))
