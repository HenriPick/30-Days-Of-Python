#test single line comment
"""
test multi line comment can
do multiple lines
"""

#Data types

"""
Numbers
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j
"""

x= 10 #integer
y= 3.14 #float
z= 1 + 2j #complex

print(x)
print(y)
print(z)

#just testing the print function and how it works with different data types

"""
String: A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.
examples: 'Hello World', "Python is great", '''This is a multi line string
and it can span multiple lines.'''
"""

name = 'hello world'
multiple_line_string = '''multi line string example
this is the second line'''

print(name)
print(multiple_line_string)

"""
Boolean: A data type that can only have two values: True or False.
"""
is_true = True
is_false = False

print(is_true)
print(is_false)

"""
List: A collection of different data types that are ordered and changeable. Lists are written with square brackets [].
Example: [1, 2, 3, 'hello', True]
"""

Fruits = ["apple", "banana", "orange", "grape"]
profile_info = ["John morgan", 30, "electrician", True]

print(Fruits)
print(profile_info)

"""
dictionary: A collection of key-value (like a label or identifier of a value) pairs that are unordered, changeable and indexed. 
Dictionaries are written with curly brackets {}.
Example: {'name': 'John', 'age': 30, 'city': 'New York'}
multi line dictionary example:
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
"""

mydict = {
    "name": "John",
    "age": 30
}

print(mydict)

"""
tuple: A collection of different data types that are ordered and unchangeable. Tuples are written with round brackets ().
example: (1, 2, 3, 'hello', True)
you can not change the values of a tuple once it is created, but you can access the values using indexing (0, 1, 2, etc.)
"""

mytuple = (1, 2, 3, "hello", True)
print(mytuple)

"""
A set is a collection of data types similar to list and tuple.
Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.
"""

myset = {1, 2 , 3, 4, 4, 5} #this is not a list or tuple because it is not ordered and does not allow duplicates
print(myset)
#if there are duplicate items in a set, only one of them will be stored. In this case, the number 4 is duplicated,
# so only one 4 will be stored in the set.

#to check the data type of a variable, we can use the type() function

print(type(x)) #this will print <class 'int'> because x is an integer

