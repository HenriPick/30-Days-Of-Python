# Strings are a data type that represents text.
# They are made up of characters and are enclosed in either single quotes (' ') or double quotes (" ").
# We use the len() function to find the length of a string, which counts the number of characters in it.

#Creating a string
my_string = "Hello, World!"

#Finding the length of the string
length_of_string = len(my_string)

#multiple lines string
multi_line_string = """This is a string
that spans multiple lines."""

#String concatenation (merging two or more strings)
First_name = 'Henri'
Last_name = 'Pickford'
space = ' '
Full_name = First_name + space + Last_name
print(Full_name)

#Esscape sequences in strings
# In python a \ is used to escape characters that have a special meaning in strings, such as quotes or newlines.
# Common ones are:
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

#Example of escape sequences
escaped_string = "This is the First line.\nThis is the second line and this is a backslash \\"
print(escaped_string)

#Old style String formatting
name = "Henri"
age = 25
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)

"""
%s is for adding a string variable or value
%d is for adding an integer variable or value
%f is for adding a float variable or value
%.2f is for adding a float variable or value with 2 decimal places
"""

#New style String formatting
formatted_string_new = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string_new)
#self explanatory

#F strings (formatted string literals)
formatted_string_f = f"My name is {name} and I am {age} years old."
print(formatted_string_f)

#does the same thing as the above two but is easier to read.

#if you want to include a curly brace in an f-string, you can use double curly braces {{ and }} to escape them.
#also if you want to add a float variable with 2 decimal places in an f-string or .format()
#you can use the format specifier :.2f inside the curly braces.

#Unpacking characters in a string
word = "Hello"
a, b, c, d, e = word
print(a)  # H
print(b)  # e
print(c)  # l
#etc.

# you basically assign each character in the string to a variable. 
# The number of variables must match the number of characters in the string, otherwise you will get a ValueError.

#alternatively you can just use regular indexing to access specific characters in the string, like this:
word = "Hello"
first_character = word[0]  # H
second_character = word[1]  # e

#note: indexing always starts at 0 and you can also use negative indexing to access characters from the end of the string 
#(there is no -0 so it starts at -1), Example:
last_character = word[-1]  # o

#slicing strings
# you can use slicing to extract a portion of a string by specifying a start index and an end index, like this:
substring = word[1:4]  # ell
# the start index is inclusive and the end index is exclusive, so it will include characters from index 1 to index 3 (but not index 4).

#you can also not specify the start or end index to slice from the beginning or end of the string, like this:
substring_from_start = word[:3]  # Hel
substring_to_end = word[2:]  # llo

#finally you can also use negative indices in slicing to slice from the end of the string, like this:
substring_negative = word[-4:-1]  # ell

#small note there is no error if you try to slice beyond the length of the string, it will just return as much as it can. For example:
long_string = "Hello"
slice_beyond = long_string[0:10]  # Hello

#reversing a string
reversed_string = word[::-1]  # olleH
# the slice [::-1] means to start from the end of the string and move backwards with a step of -1

#skipping characters in a string
skipped_string = word[::2]  # Hlo
#this can also be written as [0:6:2] but since the start and end indices are not specified, it defaults to the entire string. 
#The step of 2 means to skip every other character.

#so when you do not specify the start and end indices in slicing, it defaults to the entire string.

#string methods

#1. capitalize() - capitalizes the first character of the string and lowercases the rest
capitalized_string = word.capitalize()  # Hello
#2. upper() - converts all characters in the string to uppercase
uppercase_string = word.upper()  # HELLO
#3. lower() - converts all characters in the string to lowercase
lowercase_string = word.lower()  # hello
#4. count() - counts the number of occurrences of a substring in the string
count_l = word.count('l')  # 2
#5. endwith() - checks if the string ends with a specified substring
ends_with_o = word.endswith('o')  # True
#6. expandtabs() - replaces tabs with spaces (you can specify the number of spaces to replace each tab with)
tabbed_string = "Hello\tWorld"
expanded_string = tabbed_string.expandtabs(4)  # Hello    World
#7. find() - returns the lowest index of the substring if it is found in the string, otherwise it returns -1
index_of_l = word.find('l')  # 2
#8. rfind() - returns the highest index of the substring if it is found in the string, otherwise it returns -1
index_of_last_l = word.rfind('l')  # 3
#9. format() - formats the string using placeholders (as shown in the new style string formatting example above)
#10. index() - returns the lowest index of the substring if it is found in the string, otherwise it raises a ValueError, 
index_of_l_index = word.index('l')  # 2
# (accepts parameters for start and end index as well)
index_of_l_index_with_bounds = word.index('l', 2, 4)  # 2
#11. rindex() - returns the highest index of the substring if it is found in the string, otherwise it raises a ValueError
index_of_last_l_index = word.rindex('l')  # 3
#12. isalnum() - checks if all characters in the string are alphanumeric (letters and numbers) and there is at least one character
alphanumeric_string = "Hello123"
is_alphanumeric = alphanumeric_string.isalnum()  # True
#spaces and special characters are not considered alphanumeric, so if you have a string with spaces or special characters,
# it will return False. For example:
not_alphanumeric_string = "Hello World!"
is_not_alphanumeric = not_alphanumeric_string.isalnum()  # False
#13. isalpha() - checks if all characters in the string are alphabetic (letters) and there is at least one character
alphabetic_string = "Hello"
is_alphabetic = alphabetic_string.isalpha()  # True
#14. isdecimal() - checks if all characters in the string are decimal characters (0-9) and there is at least one character
decimal_string = "12345"
is_decimal = decimal_string.isdecimal()  # True
#15. isdigit() - checks if all characters in the string are digits (0-9) and there is at least one character
digit_string = "12345"
is_digit = digit_string.isdigit()  # True
# the difference between isdecimal() and isdigit() is that isdecimal() only considers characters that are decimal digits (0-9) as valid,
# while isdigit() also considers characters that are digits but also exponential notation (like ²) as valid. For example:
exponential_string = "²"
is_decimal_exponential = exponential_string.isdecimal()  # False
is_digit_exponential = exponential_string.isdigit()  # True
#16. isnumeric() - checks if all characters in the string are numeric characters 
# (which includes more types of numeric characters than isdigit()) and there is at least one character
numeric_string = "12345"
is_numeric = numeric_string.isnumeric()  # True
# the difference between isdigit() and isnumeric() is that isnumeric() considers a wider range of numeric characters,
# including characters from other languages and scripts that represent numbers, while isdigit() only considers characters
# that are digits (0-9) as valid. 
#17. isidentifier() - checks if the string is a valid identifier (a name that can be used for variables, functions, etc.)
identifier_string = "my_variable"
is_identifier = identifier_string.isidentifier()  # True
#18. islower() - checks if all characters in the string are lowercase and there is at least one character
lowercase_string = "hello"
is_lowercase = lowercase_string.islower()  # True
#19. isupper() - checks if all characters in the string are uppercase and there is at least one character
uppercase_string = "HELLO"
is_uppercase = uppercase_string.isupper()  # True
#20. join() - joins a list of strings into a single string, using the string as a separator
list_of_strings = ["Hello", "World", "Python"]
joined_string = " ".join(list_of_strings)  # Hello World Python
#21. strip() - removes leading and trailing whitespace from the string
string_with_whitespace = "   Hello, World!   "
stripped_string = string_with_whitespace.strip()  # Hello, World!
#22. replace() - replaces occurrences of a substring with another substring
original_string = "Hello, World!"
replaced_string = original_string.replace("World", "Python")  # Hello, Python!
#23. split() - splits the string into a list of substrings based on a specified separator (default is any whitespace)
string_to_split = "Hello, World! Welcome to Python."
split_string = string_to_split.split()  # ['Hello,', 'World!', 'Welcome', 'to', 'Python.']
#you can also specify a different separator, like this:
fruits_string = "apple,banana,orange"
split_csv_string = fruits_string.split(",")  # ['apple', 'banana', 'orange']
#24. title() - converts the first character of each word to uppercase and the rest to lowercase
title_string = "hello, world!"
titled_string = title_string.title()  # Hello, World!
#25. swapcase() - converts uppercase characters to lowercase and lowercase characters to uppercase
swapcase_string = "Hello, World!"
swapped_string = swapcase_string.swapcase()  # hELLO, wORLD!
#26. startswith() - checks if the string starts with a specified substring
starts_with_hello = word.startswith('H')  # True