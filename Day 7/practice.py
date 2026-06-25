#Sets

#creating a set
#empty set
my_set = set()
#set with initial items
fruits = {"apple", "banana", "cherry"}

#the difference between a set and a list is that a set 
# is unordered and does not allow duplicate values. if there
# are duplicate values in a set, they will be removed automatically

print(len(fruits))

#checking if an item exists in a set
print("apple" in fruits)

#adding items to a set
#for a single item : .add()
fruits.add("orange")
#for multiple items : .update() accepts a list, tuple, or another set
fruits.update(["kiwi", "mango"])

print(fruits)

#removing items from a set
#for a single item : .remove()
fruits.remove("banana")
print(fruits)
#.pop() removes a random item from the set
fruits.pop()
#if we want to know the removed item, we can store it in a 
# variable and it will return the removed item and remove it from the set
removed_item = fruits.pop()
print(fruits)

#clering set
fruits.clear()
print(fruits)

#deleting a set
del fruits

#converting a list to a set
my_list = [1, 2, 3, 4, 5,]
print(my_list)
my_set = set(my_list)
print(my_set)
#this works in the other way around too, we can convert a set to a list

#joining two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2) #we can also use the | operator to join two sets
print(set3)
set3 = set1 | set2
print(set3) #same result as above

#union returns a new set and you must assign it to a new variable if you want to keep the result.
seta = {1, 2, 3}
setb = {3, 4, 5}
seta.union(setb)
print(seta)
print(setb)# both are left unchanged so the only way to use union is to 
#assign the result to a new variable

# .update() works the same as explained earlier, it will update the set in place and not return a new set
seta.update(setb)
print(seta)
print(setb) #setb is unchanged

#.intersection() returns a new set with only the items that are present in both sets
whole_numbers = {1, 2, 3, 4, 5}
even_numbers = {2, 4, 6}
print(whole_numbers.intersection(even_numbers)) #like union, 
#intersection returns a new set and does not change the original sets 
#so you must assign it to a new variable or print it if you want to keep the result

#subset aka issubset() returns True if all items in the set are present in the other set
seta = {1, 2, 3}
subset = {1, 2}
print(subset.issubset(seta))

#superset aka issuperset() returns True if all items in the other set are present in the set
seta = {1, 2, 3}
superset = {1, 2, 3, 4, 5}
print(superset.issuperset(seta)) #True
#short summary:
#A subset means “everything in set A is also in set B”.
#A superset means “set B contains everything in set A”.

#checking difference between 2 sets with .difference (basically set1 - any items in set2)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2)) #returns {1, 2, 3} 

#symettric difference is basically the opposite of intersection, it returns a new set with items that are not present in both sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2)) #returns {1, 2, 3, 6, 7, 8}

#Checking if sets are joint or disjoint with .isdisjoint() returns True if the sets have no items in common
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) #True