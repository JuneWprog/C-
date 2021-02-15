#!/usr/bin/python
import socket
import threading
import datetime
bind_ip   = "127.0.0.1" #	The ip address will always be different!!
bind_port = 2013
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind((bind_ip,bind_port))
#server.listen(5)
print "[*] UDP Listening on %s:%d" % (bind_ip,bind_port)

while True:
	
	udp, csocket = server.recvfrom(512)  
	sent = server.sendto('UTC Time  : %s' % datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), csocket)
    
