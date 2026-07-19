#Loops

#there are 2 main types of loops in python: While loops and For loops


#A while loop executes a block of code untill its condition becomes false

count = 0
while count < 5:
    print(count)
    count = count + 1
#will count up to 4 but once count = 5 condition becomes untrue so the code stops

#if we are interested to make the loop do something when it stops we can use else

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#this makes it so that the loop will print five at the end so it will count from 1 to 5

#break is used to stop a loop early on and break out of it

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
#this loop stops counting at 3

#continue is used to end a loop early on but restart it afterwards

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
    #this loop skips 3 when counting
    
    

#for loops are used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
    
#example with a string

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
    
#example with dictionnary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
    
#others are a bit more self explanatory


#the range() function is used to create a list of numbers
#range(start, end, step) takes three parameters: starting, ending and increment
#default it starts from 0 and the increment is 1
#the range function needs at least 1 argument witch is the end

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
    
    
#you can nest for and while loops
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
            
#you can also use else if you want something to be done at the end of a for loop

for number in renge(5):
    print(number)
else:
    print('The loop is finished!')
    
#in python a statement is required after every semicolon but if we do not want to put anything we can just put pass, 
#it is useful to use as a placeholder

for number in range(6):
    pass