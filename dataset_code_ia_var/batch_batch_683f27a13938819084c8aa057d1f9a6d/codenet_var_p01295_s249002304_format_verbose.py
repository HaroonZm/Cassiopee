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

infinity = 10 ** 20
epsilon = 1.0 / 10 ** 13
modulus = 10 ** 9 + 7

four_direction_deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
eight_direction_deltas = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_int_list():
    return [int(token) for token in sys.stdin.readline().split()]

def read_int_list_zero_based():
    return [int(token) - 1 for token in sys.stdin.readline().split()]

def read_float_list():
    return [float(token) for token in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def print_flush(output_value):
    print(output_value, flush=True)

def main():
    all_result_lines = []

    def extract_concatenated_digits(start_index_1_based, number_of_digits_to_extract):
        zero_based_index = start_index_1_based - 1
        minimum_integer_with_desired_digits = 1
        current_digit_length = 1

        # Find the starting number where the sequence shifts to numbers with higher digit count
        for digit_length in range(1, 10):
            numbers_with_this_length = 10 ** (digit_length - 1) * 9
            total_digits_in_this_length = numbers_with_this_length * digit_length
            if zero_based_index > total_digits_in_this_length:
                zero_based_index -= total_digits_in_this_length
                minimum_integer_with_desired_digits = 10 ** digit_length
                current_digit_length = digit_length + 1
            else:
                break

        starting_integer = minimum_integer_with_desired_digits + (zero_based_index // current_digit_length)
        digit_offset = zero_based_index % current_digit_length

        concatenated_numbers_string = ''
        for numeric_value in range(starting_integer, starting_integer + 101):
            concatenated_numbers_string += str(numeric_value)
        return concatenated_numbers_string[digit_offset : digit_offset + number_of_digits_to_extract]

    while True:
        user_input_pair = read_int_list()
        start_index, number_of_digits_to_extract = user_input_pair
        if start_index == 0 and number_of_digits_to_extract == 0:
            break

        sequence_segment = extract_concatenated_digits(start_index, number_of_digits_to_extract)
        all_result_lines.append(sequence_segment)

    return '\n'.join(str(result_line) for result_line in all_result_lines)

print(main())