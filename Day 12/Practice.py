#A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

#some of the code will be in mymodule.py

import mymodule
print(mymodule.generate_full_name('John', 'Doe'))

from mymodule import say_hi

print(say_hi())

#this way we do not have to use the module name to call the function. We can just call the function directly.

#we can also import them and give them a different name using the as keyword
from mymodule import generate_full_name as gfn
print(gfn('John', 'Doe'))

#importing built-in modules
import math

print(int(math.sqrt(9)))

# os mudule
# uses of the os module are to interact with the operating system. It provides functions to create, remove, change directories, fetch its contents, create files, etc.

import os
print(os.getcwd()) #get current working directory

#overall it is useful when you want to interact with the operating system and perform tasks like file management, directory management, and other OS-level operations.

#sys module
#in simple terms, the sys module is a built-in Python module that provides access to some variables and functions that interact with the Python interpreter. 
#interacting with the interpreter means that you can get information about the Python environment, manipulate the execution of your program, and handle command-line arguments.
#for example, you can use the sys module to get the version of Python you're running, the platform you're on, and the command-line arguments passed to your script. 
# You can also use it to exit your program or manipulate the module search path (witch means the list of directories where Python looks for modules).

import sys
print(sys.version)
print(sys.platform)
print(sys.argv)

# so basically it is useful when you need information about the Python interpreter, the environment, or when you want to manipulate the execution of your program in some way.

#statistics module
#the statistics module is a built-in Python module that provides functions for calculating mathematical statistics of data

from statistics import * # importing all the statistics modules
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mean(mylist))
print(median(mylist))
print(mode(mylist))


#math module
#math module brings a lot of useful things in math

#already imported earlier, so we can use it directly
print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.pow(2, 3))



#string module
#the string module is a built-in Python module that provides a collection of string constants, classes
import string
print(string.ascii_letters)


#Random module
#random is for random things quite self explanatory

import random
print(random.randint(1, 10)) 