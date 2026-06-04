course = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(course)

goal = ' '.join(['Coding', 'For', 'All'])
print(goal)

company = 'Coding For All'

print(company)

print(len(company))

company_upper = company.upper()
print(company_upper)

company_lower = company.lower()
print(company_lower)

capitalized_company = company.capitalize()
print(capitalized_company)

title_company = company.title()
print(title_company)

swapcase_company = company.swapcase()
print(swapcase_company)

coding_excluded = company[7:]
print(coding_excluded)

print('Coding' in company)

coding_replaced = company.replace('Coding', 'Python')
print(coding_replaced)

print('Python for Everyone'.replace('Everyone', 'All'))

split_company = company.split(' ')
print(split_company)

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

print(company[0])
print(company[-1])
print(company[10])

words = 'Python For Everyone'.split(' ')
acronym = ''
for i in words:
    acronym += i[0]
print(acronym)

words_2 = company.split(' ')
acronym_2 = ''
for i in words_2:
    acronym_2 += i[0]
print(acronym_2)

print(company.index('C'))

print(company.index('F'))

print('Coding For All People'.rfind('I'))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

print(company.startswith('Coding'))

print(company.endswith('coding'))

print('   Coding For All      '.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier()) #this one returns true because it can be used to name a variable

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki')

print('radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.')

print('8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')