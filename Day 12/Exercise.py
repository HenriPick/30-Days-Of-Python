import random
import string

def random_user_id():
    id = ''
    all_alphanumeric = string.ascii_letters + string.digits
    for i in range(6):
        id += all_alphanumeric[random.randint(0,len(all_alphanumeric)-1)]
    return id    
print(random_user_id())


def user_id_gen_by_user(a, b):
    final_id = ''
    all_alphanumeric = string.ascii_letters + string.digits
    for j in range(b):
        temp_id = ''
        for i in range(a):
            temp_id += all_alphanumeric[random.randint(0,len(all_alphanumeric)-1)]
        final_id += temp_id + '\n'
    return final_id

print(user_id_gen_by_user(16, 6))


def rgb_color_gen():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

print(rgb_color_gen())


def list_of_hexa_colors(a):
    output = []
    hexa_options = string.digits + 'abcdef'
    for i in range(a):
        hexa = '#'
        for j in range(6):
            hexa += hexa_options[random.randint(0, len(hexa_options)-1)]
        output.append(hexa)
    return output
            
print(list_of_hexa_colors(3))

def list_of_rgb_colors(a):
    output = []
    for i in range(a):
        output.append(f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})")
    return output
        
print(list_of_rgb_colors(3))

def generate_colors(a, b):
    output = []
    if a == 'hexa':
        return list_of_hexa_colors(b)
    elif a == 'rgb':
        return list_of_rgb_colors(b)
    else:
        return 'Please enter either rgb or hexa'
    
print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))


def shuffle_list(a):
    if isinstance(a, list):
        mylist = a
        random.shuffle(mylist)
        return mylist
    else:
        return 'please input a list'
    
print(shuffle_list([1, 2, 3, 4, 5, 6]))


def seven_random_num():
    output = set()
    while len(output) < 7:
        output.add(random.randint(0, 9))
    return list(output)

print(seven_random_num())