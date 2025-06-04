from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

def is_a_less_than_b(a, b):
    return a < b

def swap_values(a, b):
    return b, a

def is_b_zero(b):
    return b == 0

def mod_of_a_by_b(a, b):
    return a % b

def calc_gcd_recursive(a, b):
    if is_a_less_than_b(a, b):
        a, b = swap_values(a, b)
    if is_b_zero(b):
        return a
    return calc_gcd_recursive(b, mod_of_a_by_b(a, b))

def read_input():
    return input()

def split_input(input_str):
    return input_str.split()

def map_input_to_ints(strs):
    return map(int, strs)

def unpack_values(mapped):
    mapped = list(mapped)
    return mapped[0], mapped[1]

def format_output(result):
    return "%d" % result

def print_result(formatted):
    print(formatted)

def main():
    input_str = read_input()
    splitted = split_input(input_str)
    mapped = map_input_to_ints(splitted)
    A, B = unpack_values(mapped)
    result = calc_gcd_recursive(A, B)
    formatted = format_output(result)
    print_result(formatted)

main()