#functions are reusable blocks of code

#declaring functions

# syntax
# Declaring a function
def function_name():
    print('Hello')
# Calling a function
function_name()#will print hello

#this function had no parameters functions can also have parameters

def addition(x, y):
    return x + y

print(addition(1, 2))

#this function has 2 parameters and is returning a value we have to use return or a function wiill return None

#we can also have arguments with key values

def substraction(x, y):
    return x- y

print(substraction(x = 3, y= 1))

#note as soon as a return gets executed, the function stops so we can have things like this 

def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

#functions can have default values to parameters

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Henri'))

#if we do not know the number of arguments a function will have we can use a * before the arguments

def total(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print(total(5, 6, 2, 6))

#we can also have arbitrary and default parameters

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

#dictionary unpacking (i took copied this example from 30 days of python because it was really well done)

# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

#we can also have an arbitrary number of named arguments but we should avoit this because it causes confusion on what the function actually does

#finally we can use functions as arguments for other functions

#funtion that takes another function as an argument
def square(x):
    return x * x

def cubed(x):
    return x * x * x

print(cubed(square(2)))