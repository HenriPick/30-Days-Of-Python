empty_list = []

big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(big_list))

print(f'First item:', big_list[0], 'middle item:', big_list[(len(big_list) // 2)], 'last item:', big_list[-1])

mixed_data_types = ['Henri', 15, '6 foot', False, '123 hello lane']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(f'Number of companies:', len(it_companies))

print(f'First company:', it_companies[0], 'middle company:', it_companies[(len(it_companies) // 2)], 'last company:', it_companies[-1])

it_companies[0] = 'Dell'
print(it_companies)

it_companies.append('HP')
print(it_companies)

it_companies.insert(len(it_companies) // 2, 'Facebook')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print(' '.join(it_companies))

print('Apple' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[3:])

print(it_companies[:-3])

it_companies = it_companies[:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]
print(it_companies)

it_companies.pop(0)
print(it_companies)

it_companies.pop(len(it_companies) // 2)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
min_age = ages[0]
print(f'max age:', min)
max_age = ages[-1]
print(f'min age', max)

