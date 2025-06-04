import math

MOD = 10 ** 9 + 7

def read_input():
    return input()

def parse_input(inp):
    return list(map(int, inp.split()))

def get_n(parsed):
    return parsed[0]

def get_m(parsed):
    return parsed[1]

def calc_difference(a, b):
    return abs(a - b)

def is_difference_ge_two(diff):
    return diff >= 2

def compute_initial_pattern():
    return 1

def zero_pattern():
    return 0

def calc_factorial(x):
    return math.factorial(x)

def multiply(a, b):
    return a * b

def should_double(diff):
    return diff == 0

def double_value(val):
    return val * 2

def apply_mod(val, mod):
    return val % mod

def print_result(val):
    print(val)

def main():
    inp = read_input()
    parsed = parse_input(inp)
    n = get_n(parsed)
    m = get_m(parsed)
    diff = calc_difference(n, m)
    if is_difference_ge_two(diff):
        ptn = zero_pattern()
    else:
        fact_n = calc_factorial(n)
        fact_m = calc_factorial(m)
        ptn = multiply(fact_n, fact_m)
        if should_double(diff):
            ptn = double_value(ptn)
    res = apply_mod(ptn, MOD)
    print_result(res)

main()