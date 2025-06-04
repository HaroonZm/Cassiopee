def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_int(lst):
    return list(map(int, lst))

def assign_values(ints):
    return ints[0], ints[1], ints[2], ints[3]

def multiply(x, y):
    return x * y

def compare(val1, val2):
    return val1 >= val2

def print_value(val):
    print(val)

def process():
    user_input = get_input()
    splitted = split_input(user_input)
    ints = map_to_int(splitted)
    a, b, c, d = assign_values(ints)
    first = multiply(a, b)
    second = multiply(c, d)
    if compare(first, second):
        print_value(first)
    else:
        print_value(second)

process()