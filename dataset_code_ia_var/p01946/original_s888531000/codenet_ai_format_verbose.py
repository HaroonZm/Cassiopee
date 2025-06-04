#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math

sys.setrecursionlimit(10 ** 5)

read_input_line = sys.stdin.readline
sqrt_function = math.sqrt

def read_int_list():
    return list(map(int, read_input_line().split()))

def read_float_list():
    return list(map(float, read_input_line().split()))

def read_zero_indexed_int_list():
    return list(map(lambda x: int(x) - 1, read_input_line().split()))

def read_single_int():
    return int(read_input_line())

def read_single_float():
    return float(read_input_line())

def read_list_of_strings():
    return list(map(list, read_input_line().split()))

def read_char_list():
    return list(read_input_line().rstrip())

def read_multiple_ints(number_of_lines):
    return [read_single_int() for _ in range(number_of_lines)]

def read_multiple_int_lists(number_of_lines):
    return [read_int_list() for _ in range(number_of_lines)]

def read_multiple_floats(number_of_lines):
    return [read_single_float() for _ in range(number_of_lines)]

def read_multiple_float_lists(number_of_lines):
    return [read_float_list() for _ in range(number_of_lines)]

def read_multiple_zero_indexed_int_lists(number_of_lines):
    return [read_zero_indexed_int_list() for _ in range(number_of_lines)]

def read_multiple_char_lists(number_of_lines):
    return [read_char_list() for _ in range(number_of_lines)]

def read_multiple_lists_of_strings(number_of_lines):
    return [read_list_of_strings() for _ in range(number_of_lines)]

MODULO = 1000000007
INFINITY_FLOAT = float('INF')

# Problem A
def solve_problem_a():
    initial_value, target_threshold, sequence_length = read_int_list()
    sequence_increment_values = read_int_list()
    total_increment_per_cycle = sum(sequence_increment_values)
    current_sum = initial_value
    minimum_sum_encountered = initial_value

    for sequence_index in range(sequence_length):
        current_sum += sequence_increment_values[sequence_index]
        minimum_sum_encountered = min(minimum_sum_encountered, current_sum)
        if current_sum <= target_threshold:
            print(sequence_index + 1)
            return

    if total_increment_per_cycle >= 0:
        print(-1)
    else:
        cycles_to_reach_target = ((minimum_sum_encountered - target_threshold) // abs(total_increment_per_cycle)) * sequence_length
        adjusted_initial_value = initial_value + (cycles_to_reach_target // sequence_length) * total_increment_per_cycle
        step_index = 0
        while True:
            if adjusted_initial_value <= target_threshold:
                print(cycles_to_reach_target + step_index)
                return
            adjusted_initial_value += sequence_increment_values[step_index % sequence_length]
            step_index += 1
        print(cycles_to_reach_target + step_index + 1)
    return

# Problem B (placeholder)
def solve_problem_b():
    return

# Problem C (placeholder)
def solve_problem_c():
    return

# Problem D (placeholder)
def solve_problem_d():
    return

# Problem E (placeholder)
def solve_problem_e():
    return

# Problem F (placeholder)
def solve_problem_f():
    return

# Problem G (placeholder)
def solve_problem_g():
    return

# Problem H (placeholder)
def solve_problem_h():
    return

# Entry point
if __name__ == '__main__':
    solve_problem_a()