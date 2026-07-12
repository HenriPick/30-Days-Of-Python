dog = dict()

dog['name'] = 'ben'
dog['color'] = 'brown'
dog['breed'] = 'dog'
dog['legs'] = 'short'
dog['age'] = '10'

print(dog)

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'male',
    'age': 21,
    'is_married': True,
    'skills': [],
    'country': 'Australia',
    'city': 'Perth'
}

print(len(student))

print(type(student['skills']))

student['skills'] = ['coding', 'math']
print(student)

print(student.keys())

print(student.values())

print(student.items())

del student['age']
print(student)

del dog