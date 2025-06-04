def read_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_ints(str_list):
    return list(map(int, str_list))

def get_values():
    user_input = read_input()
    splitted = split_input(user_input)
    ints = convert_to_ints(splitted)
    return ints[0], ints[1]

def is_divisible_by_3(n):
    return n % 3 == 0

def check_conditions(a, b):
    return not is_divisible_by_3(a) and not is_divisible_by_3(b) and not is_divisible_by_3(a + b)

def print_impossible():
    print('Impossible')

def print_possible():
    print('Possible')

def main_logic():
    a, b = get_values()
    if check_conditions(a, b):
        print_impossible()
    else:
        print_possible()

main_logic()