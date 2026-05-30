"""
Python has lots of built in functions that are used to do different tasks. some of the more common built in functions are:
print(): used to print something to the console
type(): used to find the data type of a value
len(): used to find the length of a string, list, tuple, etc.
input(): used to take input from the user

int(): used to convert a value to an integer
float(): used to convert a value to a float
str(): used to convert a value to a string
bool(): used to convert a value to a boolean
many others that do simmilar things but with different data types.

min(): used to find the minimum value in a list, tuple, etc.
max(): used to find the maximum value in a list, tuple, etc.

sorted(): used to sort a list, tuple, etc. in ascending order
open(): used to open a file and return a file object
round(): used to round a number to a specified number of decimal places
help(): used to get help on a function or module
dir(): used to get a list of attributes and methods of an object
"""

#some tests

print(int("10"))
print(type(10))
print(len("Hello World"))
print(float("9.8"))
print(str(10))
print(bool(1)) #1 is a truthy value, so it will return True
print(min(1, 2, 3, 4, 5))
print(max(1, 2, 3, 4, 5))
print(sorted([5, 4, 3, 2, 1]))
print(round(3.14159, 2)) #rounds the number to 2 decimal places
print(float(10)) #will add .0 to the end of the number to make it a float

"""
python Variable name rules
1. Variable names can only contain letters, numbers, and underscores. They cannot start with a number.
2. Variable names cannot be a reserved keyword in Python (like if, else, for, while, etc.)
3. variable names are case sensitive (myVariable and myvariable are different variables)
4. variable names should be descriptive and meaningful (like age, name, etc.)
"""

#print function takes a unlimited number of arguments and prints them to the console.
print("Hello", "World", "This is a test") #it automatically adds a space between the arguments when printing them to the console.
#to change the separator between the arguments, we can use the sep parameter of the print function.
print("Hello", "World", "This is a test", sep="-") #this will print "Hello-World-This is a test" instead of "Hello World This is a test"

#declaring multiple variables at once
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
#they are always assigned in the order that they are declared

#the input function takes input from the user and returns it as a string.
#We can also specify a prompt for the user to see when they are entering their input.
#i will comment out the input function for now so that it doesn't wait for user input when running the 
#code every time while im testing other things.

#name = input("What is your name? ")
#print("Hello", name) #this will print "Hello" followed by the name that the user entered.

"""
type(): used to find the data type of a variable or value.
example: type(10) will return <class 'int'>, type("Hello") will return <class 'str'>
"""

myint1 = 10
myfloat1 = 9.8

print(type(myint1))
print(type(myfloat1))

#casting is basically converting the type of a variable or value to another type 
# (some variables can not be converted to another type, like a string cannot be converted to an integer if it contains non-numeric characters)
num_int = 10
print('num_int:',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0
#also sometimes you have to pass a variable through multiple types to get the desired result, 
# for example if you want to convert a float to an integer, you have to first convert it to a string and then to an integer.
num_float = 9.8
num_str = str(num_float)
num_int = int(float(num_str))
print('num_int:', num_int)     # 9
#you need to convert the float to a string first because if you try to convert it directly to an integer, 
# it will give you an error because it cannot convert a float to an integer directly.
# in simpler terms python does not know how to convert a float to an integer directly 
# because it does not know how to handle the decimal part of the float when converting it to an integer,

#str to list
my_str = "Hello World"
my_list = list(my_str)
print(my_list)


