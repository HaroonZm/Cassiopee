def read_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def get_a_b():
    s = read_input()
    lst = split_input(s)
    ints = map_to_int(lst)
    return ints[0], ints[1]

def is_divisible(b, a):
    return b % a == 0

def compute_quotient(b, a):
    return b // a

def compute_quotient_plus_one(b, a):
    return compute_quotient(b, a) + 1

def print_result(result):
    print(result)

def main_logic():
    a, b = get_a_b()
    if is_divisible(b, a):
        res = compute_quotient(b, a)
    else:
        res = compute_quotient_plus_one(b, a)
    print_result(res)

main_logic()