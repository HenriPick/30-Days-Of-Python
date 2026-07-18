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

while True:
    try:
        test_score = float(input('Input your test score:'))
        break
    except ValueError:
        print('Enter a valid test score')
        
if test_score >= 90:
    print('You got an A')
elif test_score >= 80:
    print('You got a B')
elif test_score >=70:
    print('You got a C')
elif test_score >= 60:
    print('You got a D')
else:
    print('You got a F and failed ')

while True: #checks if month is valid and if not asks you to reinput month
    month = input('Chose a month: ').lower() #.lower is just to deal with if the user put an uppercase or not
    if month in ['september', 'october', 'november', 'december', 'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august']:
        if month in ['september', 'october', 'november']:
            print(f'The month {month} is in autumn')
        elif month in ['december', 'january', 'febuary']:
            print(f'The month {month} is in winter')
        elif month in ['march', 'april', 'may']:
            print(f'The month {month} is in spring')
        else:
            print(f'The month {month} is in summer')
        break
    else:
        print('invalid month, please ensure you typed it propperly')
        
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit to add to the list: ').lower()
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)
    
    person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
    
    if 'skills' in person:
        skills_list = person['skills']
        print(skills_list[len(skills_list)//2])
        if 'Python' in skills_list:
            print(f'{person["first_name"]}knows Python')
        if 'JavaScript' in skills_list and 'React' in skills_list and len(skills_list) == 2:
            print('He is a front end developer')
        elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
            print('He is a fullstack developer')
        elif 'Python' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
            print('He is a backend developer')
        else:
            print('unknown title')
    if person['is_married'] and person['country'] == 'Finland':
        print(f'{person['first_name']}{person['last_name']} lives in {person['country']} and he is married')