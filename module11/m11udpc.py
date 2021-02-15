#!/usr/bin/python
import socket
from datetime import *


target_host = "127.0.0.1"
target_port = 2013
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send some data
client.sendto("AAABBBCCC",(target_host,target_port))
# receive some data
data, addr = client.recvfrom(512)
print data

timestring=data[12:]
time_object=datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S')
print 'local time:',time_object.now().strftime('%Y-%m-%d %H:%M:%S')