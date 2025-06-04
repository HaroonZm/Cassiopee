from collections import deque
import itertools as itertools_module
import sys

# Augmenter la limite de récursion pour permettre des recherches profondes
sys.setrecursionlimit(1000000)

def compute_total_digits_up_to_number(target_number):
    total_digit_count = 0
    target_as_string = str(target_number)
    num_of_digits = len(target_as_string)

    if num_of_digits == 1:
        return target_number

    for digit_length in range(num_of_digits - 1):
        numbers_with_this_length = 9 * 10 ** digit_length
        digit_contribution = (digit_length + 1) * numbers_with_this_length
        total_digit_count += digit_contribution

    numbers_with_target_length = target_number - 10 ** (num_of_digits - 1) + 1
    total_digit_count += num_of_digits * numbers_with_target_length

    return total_digit_count

def find_number_and_offset(target_digit_position, search_left, search_right):
    if search_right - search_left <= 1:
        number_at_position = search_left
        digit_offset = target_digit_position - compute_total_digits_up_to_number(search_left)
        return number_at_position, digit_offset

    mid_value = (search_left + search_right) / 2
    if compute_total_digits_up_to_number(mid_value) > target_digit_position:
        return find_number_and_offset(target_digit_position, search_left, mid_value)
    else:
        return find_number_and_offset(target_digit_position, mid_value, search_right)

while True:
    (start_digit_index, output_length) = map(int, raw_input().split())
    if start_digit_index == 0:
        break

    position_info = find_number_and_offset(start_digit_index - 1, 0, 10 ** 18)

    starting_number = position_info[0]
    digit_index_within_starting_number = position_info[1]

    concatenated_number_string = ''
    for number in range(starting_number + 1, starting_number + 101):
        concatenated_number_string += str(number)

    print concatenated_number_string[digit_index_within_starting_number : digit_index_within_starting_number + output_length]