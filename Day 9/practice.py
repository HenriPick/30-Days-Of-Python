#conditionals

#if : if the argument is true it will execute the block of code
if 3 > 0:
    print('yes')
    
if 4 > 10:
    print('yes') #this will not execute
    
#if else: If condition is true the first block will be executed, if not the else condition will run.

if 2 < 1:
    print('yes')
else:
    print('no')#no will get printed
    
#if elif else: we use elif if we have multiple conditions

a = 0
if a > 0:
    print('A > 0')
elif a < 0:
    print('A < 0')
else:
    print('A = zero')
    
#shorthand is a way to write code to make it more readable and efficient
#note you can not use elif in these

a = 3
print('A is positive') if a > 0 else print('A is negative')

#basically, Shorthand in Python is used to write code more concisely, improving readability and reducing the number of lines needed for certain operations.

#nested conditions are just conditions in conditions

if a > 2:
    if a > 6:
        print('a > 6')
    else:
        print('a = ]2,6[')
else:
    print('a < 2')
    
#you can also use logical operators

if a % 2 != 0 and a > 0:
    print('a is a positive and odd number')
else:
     print('a is not a positive and odd number')
     
# we can also use or operator
status = 'Employee'
if status == 'Visitor' or 'Employee':
    print('you may enter')
else:
    print('you may not enter')