#!/usr/bin/python
#takes two numbers as parameters, operator words: plus, minus, times
#and prints the result of the operation.
#e.g.m02p05.py
#First Number: 5
#Second Number: 6
#Operation: times
#5 x 6 = 30


a=int(raw_input("First Number: "))
b=int(raw_input("Second Number: "))
operation=(raw_input("Operation: "))
if operation =='times':
    print ('%d x %d = %d' % (a,b,a*b))
elif operation =='plus':
    print ('%d + %d = %d' % (a,b,a+b))
elif operation=='minus':
    print ('%d - %d = %d' % (a,b,a-b))

    

