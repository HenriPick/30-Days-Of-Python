def add_two_numbers(x, y):
    return(x+y)

print(add_two_numbers(1, 2))


def area_of_circle(radius):
    return(3.14*radius**2)

print(area_of_circle(3))


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, int):
            total += num
        else:
            return('Please input valid numbers')
    return(total)

print(add_all_nums(1, 9, 33, 4444, 55555, 333, 44444444))


def convert_celsius_to_fahrenheit(celsius):
    return((celsius*9/5)+32)

print(convert_celsius_to_fahrenheit(0))


