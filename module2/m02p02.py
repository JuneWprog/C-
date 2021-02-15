#!/usr/bin/python
#outputs a single line showing the host name memory size.
#(Hint: Look for MemTotal in pseudo-file /proc/meminfo.) 
#Hostname: SuperLinux, Memory: XXXX MB

import sys, os

#find the hostname
filename='/etc/hostname'
fd=open(filename,'r')
hostname=fd.readline().rstrip('\n')


#find the memory size
filename1='/proc/meminfo'
fd1=open(filename1,'r')
lines=fd1.readlines()
for line in lines:
    (a,b)=line.split(':',1)
    if "MemTotal" ==a:
        words=b.split()   #size in KB
memorysize=int(words[0])/1024
print ("Hostname: %s, Memorysize: %s MB" % (hostname, memorysize))
    
