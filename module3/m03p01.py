#!/usr/bin/python

#This program will print first 10 rows of Pascal triangle, making it look 
#like a triangle. Define recursive function pascal(row,col)
#which will calculate each element of the triangle. 

def pascal (row,col):
    if col==0:
        return 1
    elif col==row:
        return 1
    else:
        return pascal(row-1,col)+pascal(row-1, col-1)

for row in range (10):
    rowlist=[]
    rowstr=""
    for col in range (row+1):
        num = pascal(row,col)
        rowlist.append(str(num))      #add new element to list as a string 
    rowstr=(' ').join(rowlist)       #join the list items to a string  for each row
    spaces=(26-len(rowstr))/2 
    print (" "*spaces),      #print spaces in front of row
    print (rowstr)           #print one row a time 
    




