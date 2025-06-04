from collections import deque
import itertools as itertools_module
import sys

# Augment the recursion limit to a large value
sys.setrecursionlimit(1000000)

INFINITY_MODULO = 1000000007

while True:
    first_number_input = raw_input()
    
    if first_number_input == '0':
        break

    second_number_input = raw_input()
    sum_result_input = raw_input()
    
    reversed_first_number = first_number_input[::-1]
    reversed_second_number = second_number_input[::-1]
    reversed_sum_result = sum_result_input[::-1]

    maximum_length_ab = max(len(reversed_first_number), len(reversed_second_number))
    acceptable_lengths_for_sum = [len(reversed_sum_result), len(reversed_sum_result) + 1]

    if maximum_length_ab not in acceptable_lengths_for_sum:
        print 0
        continue

    # Pad first and second numbers with zeros to match length with sum result
    while len(reversed_first_number) < len(reversed_sum_result):
        reversed_first_number += '0'
    while len(reversed_second_number) < len(reversed_sum_result):
        reversed_second_number += '0'

    count_without_carry = 1
    count_with_carry = 0

    for digit_position in range(len(reversed_sum_result)):
        next_count_without_carry = 0
        next_count_with_carry = 0

        # Generate possible digits for operand A
        if reversed_first_number[digit_position] == '?':
            minimum_digit_a = max(0, digit_position - len(reversed_sum_result) + 2)
            possible_digits_a = range(minimum_digit_a, 10)
        else:
            possible_digits_a = [int(reversed_first_number[digit_position])]

        # Generate possible digits for operand B
        if reversed_second_number[digit_position] == '?':
            minimum_digit_b = max(0, digit_position - len(reversed_sum_result) + 2)
            possible_digits_b = range(minimum_digit_b, 10)
        else:
            possible_digits_b = [int(reversed_second_number[digit_position])]

        # Generate possible digits for result digit (C)
        if reversed_sum_result[digit_position] == '?':
            minimum_digit_c = max(0, digit_position - len(reversed_sum_result) + 2)
            possible_digits_c = range(minimum_digit_c, 10)
        else:
            possible_digits_c = [int(reversed_sum_result[digit_position])]

        # Test all digit combinations for this position
        for digit_a, digit_b, digit_c in itertools_module.product(possible_digits_a, possible_digits_b, possible_digits_c):
            if digit_a + digit_b == digit_c:
                next_count_without_carry += count_without_carry
            if digit_a + digit_b == 10 + digit_c:
                next_count_with_carry += count_without_carry
            if digit_a + digit_b == digit_c - 1:
                next_count_without_carry += count_with_carry
            if digit_a + digit_b == 10 + digit_c - 1:
                next_count_with_carry += count_with_carry

        count_without_carry = next_count_without_carry % INFINITY_MODULO
        count_with_carry = next_count_with_carry % INFINITY_MODULO

    print count_without_carry