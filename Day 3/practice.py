# boolean = true or false

#assignment operators are basically adding, subtracting, multiplying, dividing, etc. to a variable that already exists.

x = 5
x += 3 # x is now 8

y = 10
y -= 2 # y is now 8

#basically same thing as basic operations but with a = sign at the end of it.

#Arithmetic operators are basically the same as basic operations but with a different syntax and not for assignment.

print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j)) # this will give us 2

#as you can see we can use them in the print statement as well and it will give us the result of the operation.

x = 10**2 # this will give us 100

#python can not perform opperations between different data types so we need to convert the input to the correct data type
# before performing operations on it.

# we can also use it to assign a value to a variable as well.

#comparison operators are basically used to compare two values and return a boolean value. 
# these operators are : ==, !=, >, <, >=, <= (!= means not equal to)

print(5 == 5) # this will return true because 5 is equal to 5

#Unlike other programming languages python uses keywords and, or, not for logical operations instead of &&, ||, !.
print(True and False) # this will return false because both values are not true
print(True or False) # this will return true because at least one value is true
print(not True or False) # this will return false because not True is False and False or False is False