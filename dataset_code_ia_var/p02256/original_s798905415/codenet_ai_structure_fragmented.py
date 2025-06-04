def swap_if_needed(x, y):
    if x < y:
        return y, x
    return x, y

def mod(a, b):
    return a % b

def update_values(x, y):
    return y, x

def is_greater_than_zero(val):
    return val > 0

def gcd_loop(x, y):
    while is_greater_than_zero(y):
        r = mod(x, y)
        x, y = update_values(x, r)
    return x

def gcd(x, y):
    x, y = swap_if_needed(x, y)
    return gcd_loop(x, y)

def input_values():
    return input()

def split_input(s):
    return s.split()

def map_to_ints(lst):
    return map(int, lst)

def read_and_parse_input():
    s = input_values()
    lst = split_input(s)
    return map_to_ints(lst)

def print_result(res):
    print(res)

def main():
    x, y = read_and_parse_input()
    result = gcd(x, y)
    print_result(result)

main()