#exercises are going to be named exercise instead of helloworld.py for ease of use/reading

print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

print("Henri")
print("Pickford")
print("Australia")
print("I am enjoying 30 days of Python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Henri'))
print(type('Pickford'))
print(type('Australia'))

myint = 10
myfloat = 9.8
mycomplex = 3 + 3j
mystring = "Henri Pickford"
myboolean = True
mylist = ['henri', 'pickford', 'australia']
mytuple = ('henri', 'pickford', 'australia')
mydict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
myset = {'henri', 'pickford', 'australia'}

import math

point1_x = 2
point2_x= 10
point1_y = 3
point2_y = 8
euclidian_distance = math.sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)
print(euclidian_distance)