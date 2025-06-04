#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools

sys.setrecursionlimit(10**5)

standard_input = sys.stdin

get_bisect_left = bisect.bisect_left
get_bisect_right = bisect.bisect_right

def read_integers_list():
    return list(map(int, standard_input.readline().split()))

def read_floats_list():
    return list(map(float, standard_input.readline().split()))

def read_zero_based_integers_list():
    return list(map(lambda x: int(x) - 1, standard_input.readline().split()))

def read_single_integer():
    return int(standard_input.readline())

def read_single_float():
    return float(standard_input.readline())

def read_list_of_lists():
    return list(map(list, standard_input.readline().split()))

def read_list_of_characters():
    return list(standard_input.readline().rstrip())

def read_multiple_integers(count):
    return [read_single_integer() for _ in range(count)]

def read_multiple_integer_lists(count):
    return [read_integers_list() for _ in range(count)]

def read_multiple_floats(count):
    return [read_single_float() for _ in range(count)]

def read_multiple_float_lists(count):
    return [read_floats_list() for _ in range(count)]

def read_multiple_zero_based_integer_lists(count):
    return [read_zero_based_integers_list() for _ in range(count)]

def read_multiple_character_lists(count):
    return [read_list_of_characters() for _ in range(count)]

def read_multiple_list_of_lists(count):
    return [read_list_of_lists() for _ in range(count)]

MODULO_CONSTANT = 1000000007
INFINITY = float('INF')

# Problem A: Arithmetic String Evaluation
def solve_arithmetic_result_identifier():
    input_string_characters = read_list_of_characters()
    target_value = read_single_integer()

    answer_labels = ["I", "L", "M", "U"]
    evaluation_flag = 0

    calculated_value = int(input_string_characters[0])

    for character_index, character in enumerate(input_string_characters):
        if character == "+":
            calculated_value += int(input_string_characters[character_index + 1])
        elif character == "*":
            calculated_value *= int(input_string_characters[character_index + 1])

    if calculated_value == target_value:
        evaluation_flag += 1

    calculated_sum_with_priority_multiplication = 0

    for character_index, character in enumerate(input_string_characters):
        if character == "*":
            input_string_characters[character_index + 1] = int(input_string_characters[character_index + 1]) * int(input_string_characters[character_index - 1])
            input_string_characters[character_index - 1] = 0

    for character in input_string_characters:
        if character != "*" and character != "+":
            calculated_sum_with_priority_multiplication += int(character)

    if calculated_sum_with_priority_multiplication == target_value:
        evaluation_flag += 2

    print(answer_labels[evaluation_flag])

    return

# Problem B: Range Addition Interpretation
def solve_minimum_cost_coverage():
    number_of_positions, number_of_intervals = read_integers_list()
    intervals = read_multiple_integer_lists(number_of_intervals)

    cumulative_counts_per_position = [0 for _ in range(number_of_positions + 1)]

    for interval_start, interval_end in intervals:
        cumulative_counts_per_position[interval_start] += 1
        cumulative_counts_per_position[interval_end] -= 1

    for index in range(number_of_positions):
        cumulative_counts_per_position[index + 1] += cumulative_counts_per_position[index]

    total_cost = 0
    was_previous_not_covered = 0

    for index in range(number_of_positions):

        if cumulative_counts_per_position[index]:
            total_cost += 3

        elif was_previous_not_covered:
            was_previous_not_covered = 0
            total_cost += 3

        else:
            total_cost += 1

    print(total_cost + 1)

    return

def solve_problem_C():
    return

def solve_problem_D():
    return

def solve_problem_E():
    return

def solve_problem_F():
    return

def solve_problem_G():
    return

def solve_problem_H():
    return

# Entry point
if __name__ == '__main__':
    solve_minimum_cost_coverage()