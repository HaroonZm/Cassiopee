#!/usr/bin/env python3

from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_list_of_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_list_of_strings_as_lists():
    return list(map(list, sys.stdin.readline().split()))

def read_string_as_list():
    return list(sys.stdin.readline())[:-1]

def read_n_ints(number_of_lines):
    input_integers = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        input_integers[index] = read_int()
    return input_integers

def read_n_list_of_ints(number_of_lines):
    input_lists = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        input_lists[index] = read_list_of_ints()
    return input_lists

def read_n_strings_as_list(number_of_lines):
    string_lists = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        string_lists[index] = read_string_as_list()
    return string_lists

def read_n_list_of_strings_as_lists(number_of_lines):
    list_of_string_lists = [None for _ in range(number_of_lines)]
    for index in range(number_of_lines):
        list_of_string_lists[index] = read_list_of_strings_as_lists()
    return list_of_string_lists

sys.setrecursionlimit(1000000)
MODULO = 1000000007

# A
def solve_problem_A():
    number_of_cases = read_int()
    roman_characters_list = list("ixcm")
    roman_powers = [1, 10, 100, 1000]
    roman_value_dict = {"i": 1, "x": 10, "c": 100, "m": 1000}
    roman_chars = ["i", "x", "c", "m"]

    for _ in range(number_of_cases):
        roman_digits_1, roman_digits_2 = read_list_of_strings_as_lists()
        total_value = 0

        for character_index in range(len(roman_digits_1)):
            current_char = roman_digits_1[character_index]
            if current_char in roman_characters_list:
                roman_digits_1[character_index] = roman_value_dict[current_char]
                if (character_index > 0) and (roman_digits_1[character_index - 1] not in roman_powers):
                    total_value += roman_digits_1[character_index - 1] * roman_digits_1[character_index]
                else:
                    total_value += roman_digits_1[character_index]
            else:
                roman_digits_1[character_index] = int(current_char)

        for character_index in range(len(roman_digits_2)):
            current_char = roman_digits_2[character_index]
            if current_char in roman_characters_list:
                roman_digits_2[character_index] = roman_value_dict[current_char]
                if (character_index > 0) and (roman_digits_2[character_index - 1] not in roman_powers):
                    total_value += roman_digits_2[character_index - 1] * roman_digits_2[character_index]
                else:
                    total_value += roman_digits_2[character_index]
            else:
                roman_digits_2[character_index] = int(current_char)

        answer_representation = []
        while total_value != 0:
            roman_power_index = int(math.log(total_value + 0.1, 10))
            quantity = total_value // roman_powers[roman_power_index]
            total_value %= roman_powers[roman_power_index]
            if quantity != 1:
                answer_representation.append(quantity)
            answer_representation.append(roman_chars[roman_power_index])
        for value in answer_representation:
            print(value, end="")
        print()
    return

# B
def solve_problem_B():
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]
    while True:
        max_turns, number_of_blocked_cells = read_list_of_ints()
        if max_turns == 0 and number_of_blocked_cells == 0:
            break
        is_cell_blocked = defaultdict(lambda: 1)
        for _ in range(number_of_blocked_cells):
            blocked_x, blocked_y = read_list_of_ints()
            is_cell_blocked[(blocked_x, blocked_y)] = 0
        starting_x, starting_y = read_list_of_ints()
        has_visited = defaultdict(lambda: 1)
        cell_queue = deque()
        cell_queue.append((starting_x, starting_y, 0))
        has_visited[(starting_x, starting_y)] = 0
        total_reachable = 1
        while cell_queue:
            current_x, current_y, current_turn = cell_queue.popleft()
            if current_turn < max_turns:
                for move_x, move_y in possible_moves:
                    next_x = current_x + move_x
                    next_y = current_y + move_y
                    if has_visited[(next_x, next_y)]:
                        if is_cell_blocked[(next_x, next_y)]:
                            total_reachable += 1
                            has_visited[(next_x, next_y)] = 0
                            cell_queue.append((next_x, next_y, current_turn + 1))
        print(total_reachable)
    return

# C
def solve_problem_C():
    return

# D
def solve_problem_D():
    def get_cumulative_digit_count(up_to_number):
        if digit_count_cache[up_to_number] is not None:
            return digit_count_cache[up_to_number]
        else:
            power_of_ten_index = int(math.log(up_to_number + 0.1, 10))
            digit_count_cache[up_to_number] = digit_count_cache[10 ** power_of_ten_index]
            numbers_in_this_block = up_to_number - 10 ** power_of_ten_index
            digit_count_cache[up_to_number] += (power_of_ten_index + 1) * numbers_in_this_block
            return digit_count_cache[up_to_number]

    cumulative_digit_counts = [1]
    for i in range(10):
        cumulative_digit_counts.append(
            cumulative_digit_counts[-1] + (i + 1) * 9 * 10 ** i
        )
    digit_count_cache = defaultdict(lambda: None)
    for i in range(11):
        digit_count_cache[10 ** i] = cumulative_digit_counts[i]

    while True:
        start_position, num_digits_to_output = read_list_of_ints()
        if start_position == 0 and num_digits_to_output == 0:
            break
        left = 0
        right = 1000000000
        while right - left > 1:
            midpoint = (right + left) // 2
            if start_position < get_cumulative_digit_count(midpoint):
                right = midpoint
            else:
                left = midpoint
        start_string = str(left)[start_position - get_cumulative_digit_count(left) :]
        current_number = left
        remaining_digits_to_print = num_digits_to_output
        while len(start_string) <= remaining_digits_to_print:
            remaining_digits_to_print -= len(start_string)
            print(start_string, end="")
            current_number += 1
            start_string = str(current_number)
        print(start_string[:remaining_digits_to_print])
    return

# E
def solve_problem_E():
    return

# F
def solve_problem_F():
    return

# G
def solve_problem_G():
    return

# H
def solve_problem_H():
    return

# I
def solve_problem_I():
    return

# J
def solve_problem_J():
    return

# Main caller
if __name__ == "__main__":
    solve_problem_D()