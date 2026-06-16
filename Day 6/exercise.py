empty_tuple = ()

sisters = ('Charlotte',)
brothers = ('George', 'Alex')
siblings = sisters + brothers
print(siblings)

print(f'I have', len(siblings), 'siblings')

family_members = tuple(siblings + ('Andrew', 'Marie-eve'))
print(family_members)

siblings = family_members[:3]
parents = family_members[3:]
print(siblings)
print(parents)

fruits = ('apple', 'banana')
vegetables = ('cucumber', 'zuchini')
animal_products = ('eggs', 'milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_item = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 != 0:
    middle_food = food_stuff_lt[middle_item]

else:
    middle_food = food_stuff_lt[middle_item - 1], food_stuff_lt[middle_item]
print(middle_food)

first_3 = food_stuff_lt[:3]
print(first_3)
last_3 = food_stuff_lt[-3:]
print(last_3)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f'Estonia is a nordic country :', 'Estonia' in nordic_countries)
print(f'Iceland is a nordic country :', 'Iceland' in nordic_countries)