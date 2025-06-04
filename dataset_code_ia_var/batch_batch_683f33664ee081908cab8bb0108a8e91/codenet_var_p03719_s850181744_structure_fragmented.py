def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_ints(lst):
    return list(map(int, lst))

def assign_variables(ints):
    return ints[0], ints[1], ints[2]

def check_in_range(a, b, c):
    return a <= c <= b

def print_yes():
    print("Yes")

def print_no():
    print("No")

def process():
    s = read_input()
    lst = split_input(s)
    ints = convert_to_ints(lst)
    a, b, c = assign_variables(ints)
    if check_in_range(a, b, c):
        print_yes()
    else:
        print_no()

process()