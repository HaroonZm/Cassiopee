import numpy as np
from copy import deepcopy
import math
import itertools

input_integer = int(input())

def get_number_of_digits(number):
    """
    Returns the number of digits in the given integer.
    """
    return len(str(number))

def generate_all_753_numbers_with_fixed_digits(number_of_digits):
    """
    Generates all numbers with 'number_of_digits' digits,
    using only the digits 7, 5, and 3, such that each number
    contains at least one of each digit.
    """
    all_possible_digit_tuples = list(itertools.product([7, 5, 3], repeat=number_of_digits))
    
    all_possible_numbers_as_strings = [
        ''.join(map(str, digit_tuple))
        for digit_tuple in all_possible_digit_tuples
    ]
    
    numbers_containing_7 = [number_str for number_str in all_possible_numbers_as_strings if '7' in number_str]
    numbers_containing_7_and_5 = [number_str for number_str in numbers_containing_7 if '5' in number_str]
    numbers_containing_7_5_3 = [number_str for number_str in numbers_containing_7_and_5 if '3' in number_str]
    
    valid_753_numbers = list(map(int, numbers_containing_7_5_3))
    
    return valid_753_numbers

total_valid_753_numbers = 0

number_of_digits_of_input = get_number_of_digits(input_integer)

for current_digit_length in range(number_of_digits_of_input):
    
    number_list_with_current_digits = generate_all_753_numbers_with_fixed_digits(current_digit_length)
    
    total_valid_753_numbers += len(number_list_with_current_digits)

valid_753_numbers_with_same_digits = generate_all_753_numbers_with_fixed_digits(number_of_digits_of_input)

valid_753_numbers_less_than_or_equal_to_input = [
    number
    for number in valid_753_numbers_with_same_digits
    if number <= input_integer
]

total_valid_753_numbers += len(valid_753_numbers_less_than_or_equal_to_input)

print(total_valid_753_numbers)