#!/usr/bin/python

#to generate pretty sine wave on the terminal using ascii star character.
#The amplitude of the sinewave shall be 10 lines, and one period of the sinewave shall be 60 
#points (60 characters). Draw the zero axis using the dash character. Use dictionary indexed by the 
#amplitude to keep track of which positions on the x axis should have the star

star_record={} 
lines=[]
newlines=[]
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

newlines= lines[:] #hard copy list, pop last str,  then reverse list.
newlines.pop()
for line in newlines:
    new=(' '*30)+line
    lines_rvs.append(new)

lines_rvs.reverse()
for line in lines_rvs:
    lines.append(line)

for line in lines:
    print line

linestr=""
for i in range(len (lines)):
    starpo=[]
    linestr=str(lines[i])
    for j in range(len(linestr)):
        if linestr[j] == star:
            starpo.append(j)
        else:
            continue
    star_record[i]=starpo
print star_record
            
            
        
    





