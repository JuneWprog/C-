#!/usr/bin/python

#generates a sine wave on the terminal using the ASCII star character. 
# Make the amplitude of the sine wave 10 lines, and make one period of the sine wave 60 points (60 characters). 
#  Draw the zero axis using the dash character.
#   Create an empty list of lines, fill each line with 60 spaces, and then place the stars and dashes.
  
lines=[]
lines_rvs=[]
space=' '
star='*'
dash='-'
length=30

lines.append((space*12)+(star*7))

fsp=10  #number of spaces in front of stars
msp=7   #number of spaces between stars 
for i in range (2):
    lines.append(space*fsp+star*2+space*msp+star*2)
    fsp-=1      #next line 1 star move forward  
    msp+=4      #last line 2 star, make 2 space on each side 2*2
    lines.append(space*fsp+star*1+space*msp+star*1)
    fsp-=2      #next line 2 stars move forward
    msp+=2      #last line 1 star, make 1 space on each side 1*2
    
fsp+=1         #last loop moved 2 space forward, but next line only move 1 star forward

for i in range (5):
    lines.append(space*fsp+star*1+space*msp+star*1)
    fsp-=1
    msp+=2
lines.append((star+dash*29)*2)  # the zero axis. 
for line in lines:
    print line
for i in range(9,-1,-1):        #print backwords of list,without the zero axis, which is the last element
     print space*length+lines[i] #print 30 spaces before lines

    
"""lines_rvs = lines[:] #hard copy list, pop last str,  then reverse list.
lines_rvs.pop()
lines_rvs.reverse()

for line in lines_rvs:
    print space*length+line"""
    




