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


