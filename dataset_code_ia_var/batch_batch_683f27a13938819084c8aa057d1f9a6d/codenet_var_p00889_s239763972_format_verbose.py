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
EPSILON = 1.0 / 10 ** 13
MODULO = 10 ** 9 + 9

DIRECTION_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_zero_based_int_list():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def print_flushed(output):
    return print(output, flush=True)

def main():
    results_list = []

    def compute_value(sequence_length, initial_seed, xor_mask, divisor):
        seed_value = initial_seed
        digits_list = []

        for position in range(sequence_length):
            current_digit = seed_value // 7 % 10
            digits_list.append(current_digit)

            if seed_value % 2 == 1:
                seed_value = (seed_value // 2) ^ xor_mask
            else:
                seed_value //= 2

        if divisor % 2 == 0 or divisor % 5 == 0:
            total_sum = 0
            positive_count = 0
            for digit in digits_list:
                if digit > 0:
                    positive_count += 1
                if digit % divisor == 0:
                    total_sum += positive_count
            return total_sum

        remainders_suffix = [0] * (sequence_length + 1)
        power_of_ten_mod_q = 1

        for index in range(sequence_length - 1, -1, -1):
            remainders_suffix[index] = (remainders_suffix[index + 1] + digits_list[index] * power_of_ten_mod_q) % divisor
            power_of_ten_mod_q = (power_of_ten_mod_q * 10) % divisor

        remainder_count_dict = collections.defaultdict(int)
        positive_digit_substring_count = 0

        for index in range(sequence_length):
            if digits_list[index] > 0:
                remainder_count_dict[remainders_suffix[index]] += 1
            positive_digit_substring_count += remainder_count_dict[remainders_suffix[index + 1]]

        return positive_digit_substring_count

    while True:
        input_sequence = read_int_list()
        sequence_length, initial_seed, xor_mask, divisor = input_sequence

        if sequence_length == 0:
            break

        result = compute_value(sequence_length, initial_seed, xor_mask, divisor)
        results_list.append(result)

    return '\n'.join(str(result) for result in results_list)

print(main())