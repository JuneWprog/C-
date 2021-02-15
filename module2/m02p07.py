#!/usr/bin/python
#prints a list of all users on your Linux system who have a home directory in the format /home/username
#the username using 20 characters and aligned left, and the home directory.
#Hint: Make use of the file /etc/passwd. 

import sys, os

#this function for printing table of usernames and the related home directory
def user_line(username):
    
    borderline='+'+'-'*11+'+'+'-'*27+'+'
    print borderline
    for usr in username:
        print ("| %-10s| %-26s|" %(usr, '/home/'+usr))
    print borderline


#find the username in file '/etc/passwd'
filename='/etc/passwd'
fd=open(filename,'r')

# every user line ends with /bin/bash, so does root.
# Root has no /home/ directory
usr_list=[]
lines=fd.readlines()   
for line in lines:
    if ('/bin/bash' in line) and ('root' not in line):
        line=line.split(':')
        usr_list.append(line[0]) #usrname is in the first column
        
user_line(usr_list)



