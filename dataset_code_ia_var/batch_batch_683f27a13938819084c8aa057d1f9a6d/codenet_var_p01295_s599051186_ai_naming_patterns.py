#!/usr/bin/env python

from collections import deque
import itertools as itertools_module
import sys

sys.setrecursionlimit(1000000)

def get_digit_count_upto_number(target_number):
    digit_total_count = 0
    number_as_string = str(target_number)
    digit_length = len(number_as_string)
    if digit_length == 1:
        return target_number
    for digit_index in range(digit_length - 1):
        digit_total_count += (digit_index + 1) * 9 * 10 ** digit_index
    return digit_total_count + digit_length * (target_number - 10 ** (digit_length - 1) + 1)

def find_position_for_digit_index(target_index, left_bound, right_bound):
    if right_bound - left_bound <= 1:
        return left_bound, target_index - get_digit_count_upto_number(left_bound)
    midpoint = (left_bound + right_bound) // 2
    if get_digit_count_upto_number(midpoint) > target_index:
        right_bound = midpoint
    else:
        left_bound = midpoint
    return find_position_for_digit_index(target_index, left_bound, right_bound)

while True:
    start_index, substring_length = map(int, raw_input().split())
    if start_index == 0:
        break

    position_base, character_offset = find_position_for_digit_index(start_index - 1, 0, 10 ** 18)

    concatenated_sequence_string = ''
    for incremented_number in range(position_base + 1, position_base + 101):
        concatenated_sequence_string += str(incremented_number)
    print concatenated_sequence_string[character_offset:character_offset + substring_length]