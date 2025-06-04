def read_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def get_A_B():
    s = read_input()
    split_s = split_input(s)
    a_b = map_to_int(split_s)
    return a_b[0], a_b[1]

def is_divisible_by_3(n):
    return n % 3 == 0

def is_possible(a, b):
    if is_divisible_by_3(a):
        return True
    if is_divisible_by_3(b):
        return True
    if is_divisible_by_3(a + b):
        return True
    return False

def print_possible():
    print('Possible')

def print_impossible():
    print('Impossible')

def process():
    a, b = get_A_B()
    if is_possible(a, b):
        print_possible()
    else:
        print_impossible()

process()