#!/usr/bin/python
# prompted for two numbers and an operator  continues repetitively until the word "exit"is typed


while (1):
    
    input_str = raw_input("Calc: ")
    if (input_str == 'exit'):
        break;
    else:
        input_str=input_str.split()
#split input string to a list of parameters and get riddle of the space after each parameter
        num1= int(input_str[0])
        num2= int(input_str[1])
        operation=(input_str[2])
        if operation == 'times':
            print ('%d x %d = %d' % (num1,num2,num1*num2))
        elif operation == 'plus':
            print ('%d + %d = %d' % (num1,num2,num1+num2))
        elif operation == 'minus':
            print ('%d - %d = %d' % (num1,num2,num1-num2))
        
        
        

    

