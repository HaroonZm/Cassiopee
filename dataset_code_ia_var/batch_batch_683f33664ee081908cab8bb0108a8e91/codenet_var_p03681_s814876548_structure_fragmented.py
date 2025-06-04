import math

def read_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_int(str_list):
    return list(map(int, str_list))

def get_numbers():
    user_input = read_input()
    splitted = split_input(user_input)
    numbers = map_to_int(splitted)
    return numbers

def get_factorial(n):
    return math.factorial(n)

def get_mod():
    return 10**9 + 7

def mod_factorial(f, mod):
    return f % mod

def product(a, b):
    return a * b

def absolute_difference(a, b):
    return abs(a - b)

def is_diff_ge_2(diff):
    return diff >= 2

def is_diff_eq_1(diff):
    return diff == 1

def is_diff_eq_0(diff):
    return diff == 0

def result_case_0():
    return 0

def result_case_1(k, mod):
    return k % mod

def result_case_2(k, mod):
    return (2 * k) % mod

def main():
    a, b = get_numbers()
    fa = get_factorial(a)
    fb = get_factorial(b)
    mod = get_mod()
    fa_mod = mod_factorial(fa, mod)
    fb_mod = mod_factorial(fb, mod)
    k = product(fa_mod, fb_mod)
    diff = absolute_difference(a, b)
    if is_diff_ge_2(diff):
        print(result_case_0())
    elif is_diff_eq_1(diff):
        print(result_case_1(k, mod))
    elif is_diff_eq_0(diff):
        print(result_case_2(k, mod))

main()