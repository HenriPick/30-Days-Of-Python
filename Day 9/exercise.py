while True:
    try:
        your_age = int(input('Input your age:'))
        break
    except ValueError:
        print('Enter a valid age')

if your_age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - your_age} more years to learn to drive.')

my_age = 15
if my_age == your_age:
    print('we are the same age')
elif your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print('You are 1 year older than me.')
    else:
        print(f'You are {difference} years older than me.')
else:
    difference = my_age - your_age
    if difference == 1:
        print('You are 1 year younger than me.')
    else:
        print(f'You are {difference} years younger than me.')
        
while True:
    try:
        a = int(input('Input a random whole number:'))
        b = int(input('Input another random whole number:'))
        break
    except ValueError:
        print('Enter valid numbers')

if a > b:
    print('A is larger than B')
elif a < b:
    print('A is smaller than B')
else:
    print('A is equal to B')
    