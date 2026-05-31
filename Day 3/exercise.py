age = 15

height = 6.1

complex = 2 - 4j



base = int(input('Enter base:'))
height = int(input('Enter height:'))
print('The area of the triangle is:', 0.5 * base * height)

a = int(input('Enter side a:'))
b = int(input('Enter side b:'))
c = int(input('Enter side c:'))
print('The perimeter of the triangle is:', a + b + c)

length = int(input('Enter length:'))
width = int(input('Enter width:'))
print('The area of the rectangle is:', length * width, 'and the perimeter is:', 2 * (length + width))

radius = int(input('Enter radius:'))
print('The circumference of the circle is:', 2 * radius * 3.14)

function = 'y = 2x-2'
slope_1 = 2
x_intercept = 1
y_intercept = -2

point_1 = (2, 2)
point_2 = (6, 10)
slope_2 = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
euclidian_distance = ((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)**0.5

print('Are the slopes equal?', slope_1 == slope_2)

x = -3
y = x**2 + 6*x + 9 
print(y)
print('for y = 0 x is:', x)

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon.')

print(not ('on' in 'python' and 'on' in 'dragon'))

print(str(float(len('python'))))

number = 435782
print(number%2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(float('9.8') == 10))

hours = int(input('Enter hours:'))
rate = int(input('Enter rate per hour:'))
print('Your weekly earning is:', hours * rate)

years = int(input('Enter number of years you have lived:'))
print('You have lived for', years * 365 *24 * 60 *60, 'seconds')

print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')