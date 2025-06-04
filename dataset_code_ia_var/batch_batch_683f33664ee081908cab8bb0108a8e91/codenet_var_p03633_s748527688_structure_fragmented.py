from functools import reduce

def input_number():
    return int(input())

def input_list(size):
    return [input_number() for _ in range(size)]

def assign_zero_list(size):
    return [0] * size

def compute_gcd_iteration(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd(a, b):
    return compute_gcd_iteration(a, b)

def compute_lcm_formula(a, b, gcd_func):
    return a * b // gcd_func(a, b)

def lcm(a, b):
    return compute_lcm_formula(a, b, gcd)

def reduce_lcm(numbers, lcm_func):
    return reduce(lcm_func, numbers)

def lcmm(*args):
    return reduce_lcm(args, lcm)

def populate_list_from_input(size):
    inputted_list = assign_zero_list(size)
    for i in range(size):
        inputted_list[i] = input_number()
    return inputted_list

def print_result(result):
    print(result)

def main():
    N = input_number()
    T = populate_list_from_input(N)
    syuki = lcmm(*T)
    print_result(syuki)

main()