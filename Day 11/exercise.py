def add_two_numbers(x, y):
    return(x+y)

print(add_two_numbers(1, 2))


def area_of_circle(radius):
    return(3.14*radius**2)

print(area_of_circle(3))


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            return('Please input valid numbers')
    return(total)

print(add_all_nums(1, 9, 33, 4444, 55555, 333, 44444444))


def convert_celsius_to_fahrenheit(celsius):
    return((celsius*9/5)+32)

print(convert_celsius_to_fahrenheit(0))


def check_season(month):
        if month in ['December', 'January', 'February']:
            return('Winter')
        elif month in ['March', 'April', 'May']:
            return('Spring')
        elif month in ['June', 'July', 'August']:
            return('Summer')
        elif month in ['September', 'October', 'November']:
            return('Fall')
        else:
            return('Input a valid month with a capital letter at the start')
    
month = 'January'  
print(f'The month {month} is in {check_season(month)}')

def solve_quadratic_eqn(a, b, c):
    discriminant = (b**2) - (4*a*c)
    root1 = (-b - discriminant**0.5) / (2*a)
    root2 = (-b + discriminant**0.5) / (2*a)
    return root1, root2

print(solve_quadratic_eqn(2, 5, 3))

def print_list(a):
    if isinstance(a, list):
        for i in a:
            print(i)
    else:
        print('Please enter a list as an argument for this function')
        
print_list([1, 2, 3, 4, 5, 6])
print_list('hello')

def reverse_list(a):
    if isinstance(a, list):
        index = -1
        for i in a:
            print(a[index])
            index -= 1
    else:
        print('Please enter a list as an argument for this function')
        
reverse_list([1, 2, 3, 4, 5])
        
def capitalize_list_items(a):
    list_copy = a
    if isinstance(list_copy, list):
        index = 0
        for i in list_copy:
            list_copy[index] = i.capitalize()
            index += 1
        return list_copy
    else:
        print('Please enter a list as an argument for this function')
        
print(capitalize_list_items(['Hello', 'gg', 'llllllll', 'qwerty']))

def add_item(a, item):
    a.append(item)
    
list_1 = [1, 2, 3, 4]
add_item(list_1, 5)
print(list_1)


def remove_item(a, item):
    list_copy = a.copy()
    if isinstance(list_copy, list):
        while item in list_copy:
            list_copy.remove(item)
        return list_copy
    else:
        print('Please enter a list as an argument for this function')

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk', 'Mango'] 
print(remove_item(food_stuff, 'Mango'))


def sum_of_numbers(a):
    total = 0
    for i in range(a+1):
        total += i
    return total

print(sum_of_numbers(5))

def sum_of_odds(a):
    total = 0
    for i in range(a+1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(5))

def sum_of_even(a):
    total = 0
    for i in range(a+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(5))


def evens_and_odds(a):
    even = 0
    odds = 0
    if isinstance(a, int) and a >= 0:
        for i in range(a + 1):
            if i % 2 == 0:
                even += 1
            else:
                odds += 1
        return even, odds
    else:
        return('Please input a positive integer')
    
print(evens_and_odds(100))


def factorial(a):
    if isinstance(a, int):
        total = 1
        for i in range(1, a + 1):
            total *= i
        return total
    else:
        return ('please enter a whole number')
    
print(factorial(5))


def is_empty(a):
    if not a and isinstance(a, (str, list, dict, tuple)):
        return(f'This {type(a).__name__} is empty')
    
print(is_empty(''))


def calculate_mean(data):
    sum(data) / len(data)
    
def calculate_median(data):
    data_sorted = sorted(data)
    if len(data) % 2 == 0:
        return (data_sorted[len(data)//2 -1] + data_sorted[len(data)//2]) / 2
    else:
        return data_sorted[len(data)//2]
    

def calculate_mode(data):
    y = {}
    for i in data:
        if i not in y:
            y[i] = 1
        else:
            y[i] += 1
    return max(y, key=y.get)


def calculate_range(data):
    return max(data)-min(data)
