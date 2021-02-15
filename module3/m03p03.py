#!/usr/bin/python
#This program will take one parameter, a file name, and display information about the file

import os,sys
import stat
import time

if len (sys.argv)<2:
    print "need an executable file name"
    sys.exit(-1)
else:
    filename=sys.argv[1]
    print """File Name: %s""" % (filename)
    print """File Size: %s""" % (os.stat(filename).st_size)
    print """Inode    : %s""" % (os.stat(filename).st_ino)
    tm=os.stat(filename).st_mtime
    print """Last Mod : %s""" % (time.ctime(tm))  
     
    

#stat.ST_SIZE
#Size in bytes of a plain file; amount of data waiting on some special files.
#stat.ST_MTIME
#Time of last modification.
#stat.ST_INO
#Inode number.
#format of time in python
 #print utmp.ut_time        (float number for time in  seconds)
 #print time.ctime(utmp.ut_time)  (convert seconds to  time)
 #print time.strptime(time.ctime(utmp.ut_time)) (time in structure)
 #print time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time.ctime(utmp.ut_time)) (time in format)
 # (time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time.ctime(utmp.ut_time))))

