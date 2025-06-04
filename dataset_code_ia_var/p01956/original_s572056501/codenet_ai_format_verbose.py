#!/usr/bin/env python3

from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_integer_list():
    return list(map(int, sys.stdin.readline().split()))

def read_single_integer():
    return int(sys.stdin.readline())

def read_list_of_strings():
    return list(map(list, sys.stdin.readline().split()))

def read_string_as_char_list():
    return list(sys.stdin.readline())[:-1]

def read_multiple_integers(number_of_lines):
    integer_list = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        integer_list[index] = read_single_integer()
    return integer_list

def read_multiple_integer_lists(number_of_lines):
    list_of_integer_lists = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        list_of_integer_lists[index] = read_integer_list()
    return list_of_integer_lists

def read_multiple_strings(number_of_lines):
    string_list = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        string_list[index] = read_string_as_char_list()
    return string_list

def read_multiple_list_of_strings(number_of_lines):
    list_of_lists_of_strings = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        list_of_lists_of_strings[index] = read_list_of_strings()
    return list_of_lists_of_strings

sys.setrecursionlimit(1000000)
MODULO_VALUE = 1000000007

# Problem A
def solve_problem_A():
    number_of_steps, rectangle_height, rectangle_width = read_integer_list()
    step_offsets = read_integer_list()
    coverage_counter = [0 for _ in range(rectangle_width * number_of_steps + 1)]
    for step_index in range(number_of_steps):
        if step_index % 2 == 0:  # Even step
            start_position = step_index * rectangle_width + step_offsets[step_index]
            end_position = (step_index + 1) * rectangle_width + step_offsets[step_index]
            coverage_counter[start_position] += 1
            coverage_counter[end_position] -= 1
        else:  # Odd step
            start_position = step_index * rectangle_width - step_offsets[step_index]
            end_position = (step_index + 1) * rectangle_width - step_offsets[step_index]
            coverage_counter[start_position] += 1
            coverage_counter[end_position] -= 1
    for position in range(rectangle_width * number_of_steps):
        coverage_counter[position + 1] += coverage_counter[position]
    uncovered_area = 0
    for coverage in coverage_counter[:-1]:
        if coverage == 0:
            uncovered_area += rectangle_height
    print(uncovered_area)
    return

# Problem B
def solve_problem_B():
    return

# Problem C
def solve_problem_C():
    return

# Problem D
def solve_problem_D():
    return

# Problem E
def solve_problem_E():
    return

# Problem F
def solve_problem_F():
    return

# Problem G
def solve_problem_G():
    return

# Problem H
def solve_problem_H():
    return

# Problem I
def solve_problem_I():
    return

# Problem J
def solve_problem_J():
    return

# Main execution
if __name__ == "__main__":
    solve_problem_A()