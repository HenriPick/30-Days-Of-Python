#a dictionnary has the following characteristics:
#1. It is unordered, meaning that the items do not have a defined order.
#2. It is mutable, meaning that we can change, add or remove items after the dictionnary has been created.
#the only difference between a set and a dictionnary is that a dictionnary has key-value pairs,
#key value pairs are basically 2 or more items that are related to each other,
#for example if we put 'name' as a key and 'John' as a value, it means that the name of the person is John.


#creating a dictionnary
my_dict = dict()
print(my_dict)
filled_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(filled_dict)
filled_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print(filled_dict) #as you can see it can also be written in multiple lines for better readability

#just as a note the len() function counts the number of key-value pairs in a dictionnary, not the number of items in the dictionnary.


#accessing dictionnary items example:
"""
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
"""

#example
print(filled_dict['name'])
print(filled_dict['age'])


#accessing an item by its key will return an error if the key does not exist, 
# to fix this we can use the get() method to avoid this error

print(filled_dict.get('name'))
print(filled_dict.get('age'))
print(filled_dict.get('country')) #this will return None because the key does not exist


#adding items to a dictionnary
print(filled_dict)
filled_dict['country'] = 'Australia'
print(filled_dict)
#so basically its the same as accessing an item by its key, but instead of returning the value, 
#it will add the key-value pair to the dictionnary if the key does not exist, if the key already exists it will update the value of that key.


#as mentionned above to modify an item in a dictionary you just do the same as adding an item but you put an already present value

print(filled_dict)
filled_dict['name'] = 'bob'
print(filled_dict)

#to check if a key is in a dictionary we use the in operator
print('age' in filled_dict)
print('weight' in filled_dict)


#removing items from dictionaries

#pop(key): removes the item with the specified key name and its acosiated value:
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
dct.pop('1') 
print(dct) 

#popitem(): removes the last item
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
dct.popitem() 
print(dct)

#del: removes an item with specified key name
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
del dct['2']
print(dct)

#the difference between .pop and del in this case is that .pop can return the value of the deleted item while del simply deletes it


#Misc

#The items() method changes dictionary to a list of tuples.
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
print(dct.items())


#If we don't want the items in a dictionary we can clear them using clear() method
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
print(dct.clear())


#If we do not use the dictionary we can delete it completely
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
del dct


#We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.  (Would have been good to know early)
dct = {'1':'A', '2':'B', '3':'C', '4':'D'}
dct_copy = dct.copy()


#The keys() method gives us all the keys of a a dictionary as a list.
print(dct.keys())


#The values method gives us all the values of a a dictionary as a list.
print(dct.values())