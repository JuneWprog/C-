#!/usr/bin/python
name="Jun Wang"
length=len(name)
fname=[]
for i in range(length):
    fname.append(name[i])
print fname

fname.reverse()
fnamestr=''.join(fname)
print fnamestr

fname.sort(key=lowercase)
fnamestr=''.join(fname)
print fnamestr

