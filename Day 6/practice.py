#a tuple is a data type that is similar to a list but it is mutable (we can not change its values one it is created)
#tuples are written with ()

#creating a tuple

#empty tuple:
empty_tuple_1 = ()
print(empty_tuple_1)
empty_tuple_2 = tuple()
print(empty_tuple_2)

#tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)


#tuple length:
print(len(fruits))


#indexing is the same as lists (starting at 0 and negative starts at -1)


#slicing also works the same as lists (fruits[start:end:step]) end excluded as usual


#changing tuples to lists
print(list(fruits))


#checking if item is in a tuple
print('banana' in fruits)
print('Canada' in fruits)


#deleting tuples
del fruits
#print(fruits) this would return name error because fruits is not defined


