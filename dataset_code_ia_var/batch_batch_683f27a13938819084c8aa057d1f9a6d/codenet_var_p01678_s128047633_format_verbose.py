import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10 ** 7)

INFINITY = 10 ** 20
EPSILON = 1.0 / 10 ** 10
MODULO = 10 ** 9 + 7

# Directions for 4-connectivity (up, right, down, left)
CARDINAL_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Directions for 8-connectivity (including diagonals)
ALL_DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_list_of_ints():
    return [int(element) for element in sys.stdin.readline().split()]

def read_list_of_ints_zero_based():
    return [int(element) - 1 for element in sys.stdin.readline().split()]

def read_list_of_floats():
    return [float(element) for element in sys.stdin.readline().split()]

def read_list_of_strings():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_line_string():
    return input()

def print_flush(line):
    print(line, flush=True)

def main():
    list_of_result_counts = []

    while True:
        input_string_a = read_single_line_string()
        if input_string_a == '0':
            break

        input_string_b = read_single_line_string()
        input_string_c = read_single_line_string()

        max_length = max(len(input_string_a), len(input_string_b), len(input_string_c))

        # Pad numbers with leading zeros to make their lengths equal
        if len(input_string_a) < max_length:
            input_string_a = '0' * (max_length - len(input_string_a)) + input_string_a

        if len(input_string_b) < max_length:
            input_string_b = '0' * (max_length - len(input_string_b)) + input_string_b

        if len(input_string_c) < max_length:
            input_string_c = '0' * (max_length - len(input_string_c)) + input_string_c

        dp_carry_counts = [[0, 0] for _ in range(max_length + 1)]
        # dp_carry_counts[i][0]: Ways at digit i without carry
        # dp_carry_counts[i][1]: Ways at digit i with carry

        dp_carry_counts[0][0] = 1  # Start with least significant digit, no carry, one way

        for digit_index in range(max_length):
            current_digit_a = input_string_a[max_length - digit_index - 1]
            current_digit_b = input_string_b[max_length - digit_index - 1]
            current_digit_c = input_string_c[max_length - digit_index - 1]

            count_no_carry = [0, 0]  # [no_carry, with_carry]
            count_with_carry = [0, 0]

            is_most_significant = (digit_index == max_length - 1)
            min_digit = 1 if is_most_significant else 0

            possible_digits_a = range(min_digit, 10) if current_digit_a == '?' else [int(current_digit_a)]
            possible_digits_b = range(min_digit, 10) if current_digit_b == '?' else [int(current_digit_b)]
            possible_digits_c = range(min_digit, 10) if current_digit_c == '?' else [int(current_digit_c)]

            for digit_a, digit_b, digit_c in itertools.product(possible_digits_a, possible_digits_b, possible_digits_c):
                digit_a_plus_b = digit_a + digit_b
                if digit_a_plus_b % 10 == digit_c:
                    if digit_a_plus_b > 9:
                        count_no_carry[1] += 1
                    else:
                        count_no_carry[0] += 1
                elif (digit_a_plus_b + 1) % 10 == digit_c:
                    if digit_a_plus_b > 8:
                        count_with_carry[1] += 1
                    else:
                        count_with_carry[0] += 1

            dp_carry_counts[digit_index + 1][0] += count_no_carry[0] * dp_carry_counts[digit_index][0]
            dp_carry_counts[digit_index + 1][0] += count_with_carry[0] * dp_carry_counts[digit_index][1]
            dp_carry_counts[digit_index + 1][1] += count_no_carry[1] * dp_carry_counts[digit_index][0]
            dp_carry_counts[digit_index + 1][1] += count_with_carry[1] * dp_carry_counts[digit_index][1]

        list_of_result_counts.append(dp_carry_counts[max_length][0] % MODULO)

    return '\n'.join(map(str, list_of_result_counts))

print(main())