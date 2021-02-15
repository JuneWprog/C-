#!/usr/bin/python

#print rows of Pascal triangle numbers in the shape of a triangle. 
# Make the printing stop when the row would exceed 80 characters. 
#Define the function pascal(row), which takes as a parameter the list of numbers in a row, and returns a list of numbers for the next row. 


linelen=80
def pascal(row):           #calculate next row
    nextrow=[1]                   #first element of new row is 1
    for i in range(1,(len(row))): #contains one more element than previous row
        nextrow.append(row[i-1]+row[i]) #generate elements in middle 
    nextrow.append(1)
    
    return nextrow
    

onerow=[1]
while 1:
    rowstr=''
    for num in onerow:
        rowstr += str(num) + ' '
    if len (rowstr) >= linelen:
        break
    print (" "*((linelen-len(rowstr))/2)), #print spaces in front of row
    print rowstr
    onerow=pascal(onerow) #get nextrow


