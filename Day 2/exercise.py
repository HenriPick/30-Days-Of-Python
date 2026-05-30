#Day 2: 30 Days of python programming

#level 1 exercises

first_name = "Henri"
last_name = "Pickford"
full_name = first_name + ' ' + last_name
country = 'Australia'
city = 'Perth'
age = 15
year = 2026
is_married = False
is_true = True
is_light_on = True
x, y, z = 1, 2, 3

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

#level 2 exercises

print(len(first_name))
if len(first_name) > len(last_name):
    print("first name is longer than last name")
else:
    print("last name is longer than first name")
    
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30

area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.1 * radius
radius_of_circle = input("Enter the radius of a circle: ")
area_of_circle = 3.14 * float(radius_of_circle) ** 2
print(area_of_circle)

first_name = input("First name:")
last_name = input("Last name:")
country = input("Country:")
age = input("Age:")

print(first_name, last_name, country, age)