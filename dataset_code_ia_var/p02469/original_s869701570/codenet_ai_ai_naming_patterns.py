import sys
from functools import reduce
from operator import mod

def compute_gcd(value_a, value_b):
    if value_a < value_b:
        value_a, value_b = value_b, value_a
    while value_b > 0:
        remainder = mod(value_a, value_b)
        value_a = value_b
        value_b = remainder
    return value_a

def compute_lcm(value_a, value_b):
    return value_a * value_b // compute_gcd(value_a, value_b)

def calculate_lcm_list(number_sequence):
    return reduce(compute_lcm, number_sequence)

def main():
    input_lines = sys.stdin.readlines()
    sequence_count = int(input_lines[0])
    number_sequence = tuple(map(int, input_lines[1].split()))
    print(calculate_lcm_list(number_sequence))

if __name__ == '__main__':
    main()