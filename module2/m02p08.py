#!/usr/bin/python
#Install Python module pyutmp: sudo pip install pyutmp
#if pip is not installed:  sudo apt install pip
#prints all user login/logout information for the past 24 hours.
#Use the sequence: date, user, where from, sorted in descending time order
#/var/run/utmp and /var/log/wtmp contains logs for logins and logouts

import sys,os
import time

from pyutmp import UtmpFile

logs = []
for utmp in UtmpFile():
        if utmp.ut_user_process:
        
        #print utmp.ut_time        (float number for time in  seconds)
        #print time.ctime(utmp.ut_time)  (convert seconds to  time)
        #print time.strptime(time.ctime(utmp.ut_time)) (time in structure)
        #print time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time.ctime(utmp.ut_time)) (time in format)
                logs.append(str (time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time.ctime(utmp.ut_time))))+' '+str( utmp.ut_user )+' '+str( utmp.ut_line))

for i in range((len(logs)-1),-1,-1):  #reverse list from ascending to descending
        print logs[i]
