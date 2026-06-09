#Lists

#there are 4 collection data types in Python and they all have different qualities and usage:
#1.List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
#2.Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
#3.Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
#4.Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

#how to create a list
#using built in list function
empty_list = list()
#using square brackets
empty_list_2 = []

#these are lists with initial values
fruits = ['banana', 'orange', 'mango', 'lemon']
numbers = [1, 2, 3, 4, 5]

print('Fruits:', fruits)
print('number of fruits:', len(fruits))
print('Numbers:', numbers)
print('number of numbers:', len(numbers))

#lists can have different data types
mixed_list = ['Henri', 15, True, 3.14, {'coding' : True}]
print('Mixed list:', mixed_list)



#as most data types in python, lists use zero based indexing (starts at 0)

print('first fruit:', fruits[0])
print('second fruit:', fruits[1])

print('first number:', numbers[0])
print('second number:', numbers[1])

last_index = len(fruits) - 1
print(last_index)

#can also do negative indexing

#unpacking list items
name, age, is_student, *rest = mixed_list
print('Name:', name)
print('Age:', age)
print('Is Student:', is_student)
print('Rest:', rest)



#list slicing : list[start:end:step]

print('first three fruits:', fruits[0:3])

#as usual end is exclusive, so it will not include the item at index 3 which is 'lemon'

#negative slicing : list[start:end:step]
print('three last fruits:', fruits[-3:])

#we can exclude the end index and it will slice until the end of the list



#modifying list items

print(fruits)
fruits[0] = 'apple'
print(fruits)
fruits[last_index] = 'grape'
print(fruits)

#as you can see we can use a variable as an index



#adding items to a list, to do this we use the append() function
fruits.append('kiwi')
print(fruits)



