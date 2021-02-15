#!/usr/bin/python
name="Jun Wang"
length=len(name)
for i in range(length-1,-1,-1):
    print """%c""" % (name[i]),
for i in range(length):
    print """%c""" % (name[length-i-1]),


name1=list(name)
name1.reverse()
name1str=''.join(name1)
print name1str

