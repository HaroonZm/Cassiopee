def read_input():
    return input()

def split_chars(s):
    return list(s)

def str_list_to_int_list(l):
    return list(map(int, l))

def calc_sum(l):
    return sum(l)

def is_divisible_by_nine(x):
    return x % 9 == 0

def print_yes():
    print('Yes')

def print_no():
    print('No')

def process():
    s = read_input()
    chars = split_chars(s)
    digits = str_list_to_int_list(chars)
    total = calc_sum(digits)
    if is_divisible_by_nine(total):
        print_yes()
    else:
        print_no()

process()