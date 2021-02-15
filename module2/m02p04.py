#!/usr/bin/python
#This program takes two numbers as parameters,
#and one of the operator words plus,minus,times
# e.g. m02p04.py 5 6 times  prints:5 x 6 = 30

import sys,os
#sys.argv is a list contains commandline parameters, index from 0 
if len (sys.argv)<4:
    print "want some arguments"
    sys.exit(-1)
else:
    a=int(sys.argv[1])   #a takes the first int
    b=int(sys.argv[2])   #b takes the second int
    if sys.argv[3]=='times': #the operation sign
        print ('%d x %d = %d' % (a,b,a*b))
    elif sys.argv[3]=='plus':
        print ('%d + %d = %d' % (a,b,a+b))
    elif sys.argv[3]=='minus':
        print ('%d - %d = %d' % (a,b,a-b))

    
