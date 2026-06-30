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
#it will add the key-value pair to the dictionnary

