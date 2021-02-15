#!/usr/bin/python
#outputs a line consisting of the year, month, date, your SAIT email address,
#and your first and last name, each separated by a single space. 
import datetime

datem = datetime.datetime.now().strftime("%Y-%m-%d")
firstname='jun'
lastname='wang'
email=firstname+'.'+lastname+'@edu.sait.ca '
name=firstname+ ' '+lastname

print ('%s %s %s'%(datem,email,name))

