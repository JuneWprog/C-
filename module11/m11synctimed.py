#!/usr/bin/python
import socket
import threading
import datetime
import struct
import sys
import time

def sntp_client():
	NTP_SERVER = "time.nist.gov"
	ntp_port=123
	TIME1970 = 2208988800L  
	client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = '\x1b' + 47 * '\0'
	client.sendto(data, (NTP_SERVER, ntp_port))
	data, address = client.recvfrom( 1024 )
	sec = struct.unpack( '!12I', data )[10]
	sec-= TIME1970
	return sec

bind_ip   = "127.0.0.1"
bind_port = 2013
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind((bind_ip,bind_port))
print "[*] UDP Listening on %s:%d" % (bind_ip,bind_port)
while True:
	udp, csocket = server.recvfrom(512)  
	#sent = server.sendto('%s' % datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), csocket)
	sntp_time=time.localtime(sntp_client())
	sent = server.sendto('SNTP Time : %s' %time.strftime("%Y-%m-%d %H:%M:%S", sntp_time), csocket)









    
