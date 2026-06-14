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



#checking if an item is in a list with in operator
print('apple' in fruits)
print('carrot' in fruits)



#adding items to a list, to do this we use the append() function to add something at the END of a list
fruits.append('kiwi')
print(fruits)



#inserting items into a list : .insert(index, item) the item currently in that index gets pushed to 1 index higher

my_list = [10, 20, 30, 40]
print(my_list)
my_list.insert(2, 25)  # Inserting 25 at index 2
print(my_list)



#Removing items from a list : .remove(item) only removes first occurenco of an item

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  #this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']



#removing items using the .pop(index) funcion, if index is unspecified removes last item of the list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)



#just small experiment i wanted to test out not linked with course
size = 8

for i in range(size // 2):
    print('□■' * (size // 2))
    print('■□' * (size // 2))
    
    
    
#removing items using del [index] or remove [] and leave index blank to delete entire list, 
#also you can give range such as 1:3 (3 will be excluded)

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print(fruits)
del fruits[1]
print(fruits)       
del fruits[1:3]    
print(fruits)      
del fruits
#print(fruits)   this would return NameError : name 'fruits' is not defined   



#clearing a list with .clear()

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits.clear()
print(fruits) #returns empty list



#copying a list with .copy()
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits_2 = fruits.copy()
print(fruits)
print(fruits_2)



#joining lists with + or .extent()

#+ operator
fruits = ['apple', 'banana']
vegetables = ['carrot', 'brocoli']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#.extend(list) method add list at the end of another list
num_1 = [1, 2, 3]
num_2 = [4, 5, 6]
num_1.extend(num_2)
print(num_1)



#counting items in a list with .count(item)
numbers = [1, 2, 2, 3, 3, 3]
print(numbers.count(1))
print(numbers.count(2))
print(numbers.count(3))



#finding index of a item in a list with .index(item), will return first occurence of item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))



#reversing a list with .reverse()
numbers = [1, 2, 3, 4, 5, 6]
numbers.reverse()
print(numbers)



#sorting a list with .sort(), empty is ascending and .sort(reverse=True) is descending
letters = ['b', 'c', 'a']
print(letters)
letters.sort() #will sort alphabetically
print(letters)
letters.sort(reverse=True)#descending (z to a)
print(letters)

# sorted() returns a sorted list without modifying the original
numbers = [3, 4, 1, 2]
print(sorted(numbers))
print(numbers)