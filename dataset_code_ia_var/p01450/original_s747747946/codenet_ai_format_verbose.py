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

# Augment the recursion limit in case of large recursive calls
sys.setrecursionlimit(10**7)

infinity_for_comparison = 10**20
epsilon_for_floats = 1.0 / 10**13
modulo_value = 10**9 + 7

# Directions for grid navigation (4-way and 8-way)
grid_4_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid_8_directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def read_integers_from_stdin_as_list():
    return [int(single_string) for single_string in sys.stdin.readline().split()]


def read_integers_from_stdin_as_zero_based():
    return [int(single_string) - 1 for single_string in sys.stdin.readline().split()]


def read_floats_from_stdin_as_list():
    return [float(single_string) for single_string in sys.stdin.readline().split()]


def read_strings_from_stdin_as_list():
    return sys.stdin.readline().split()


def read_single_integer_from_stdin():
    return int(sys.stdin.readline())


def read_single_float_from_stdin():
    return float(sys.stdin.readline())


def read_single_string_interactively():
    return input()


def print_and_flush(output_value):
    return print(output_value, flush=True)


def main():
    list_of_results = []

    def count_valid_subsets(number_of_items, weight_limit):
        item_weights = sorted([read_single_integer_from_stdin() for _ in range(number_of_items)], reverse=True)

        dynamic_programming_combinations = [0] * (weight_limit + 1)
        dynamic_programming_combinations[0] = 1

        total_weight_sum = sum(item_weights)

        if total_weight_sum <= weight_limit:
            return 1

        current_result = 0

        for current_weight in item_weights:
            total_weight_sum -= current_weight

            if weight_limit >= total_weight_sum:
                lower_bound = max(0, weight_limit - total_weight_sum - current_weight + 1)
                upper_bound = weight_limit - total_weight_sum + 1
                current_result += sum(dynamic_programming_combinations[lower_bound:upper_bound])
                current_result %= modulo_value

            for index_weight in range(weight_limit - current_weight, -1, -1):
                dynamic_programming_combinations[index_weight + current_weight] += dynamic_programming_combinations[index_weight]
                dynamic_programming_combinations[index_weight + current_weight] %= modulo_value

        return current_result % modulo_value

    while True:
        input_number_of_items, input_weight_limit = read_integers_from_stdin_as_list()
        if input_number_of_items == 0:
            break

        list_of_results.append(
            count_valid_subsets(input_number_of_items, input_weight_limit)
        )
        break

    return '\n'.join(map(str, list_of_results))


print(main())