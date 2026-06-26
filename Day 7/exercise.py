# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['company_1', 'company_2'])
print(it_companies)

it_companies.remove('IBM')
print(it_companies)

#.remove() returns an error if discarded element is not present in the set and .discard() does not


C = A | B
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B

age_set = set(age)
if len(age) > len(age_set):
    print('The list is bigger')
else:
    print('The set is bigger')

#string is used for plain text and is basically like 1 item
#list can hold many items and are mutable, ordered and allows duplicates and is written with []
#tuple has the same properties as a list, but is immutable and is written with ()
#set is unordered, does not allow duplicates and is written with {}

print(len(set('I am a teacher and I love to inspire and teach people'.split(' '))))