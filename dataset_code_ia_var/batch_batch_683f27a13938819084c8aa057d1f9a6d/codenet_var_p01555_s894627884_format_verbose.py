from collections import deque
import itertools as itertools_module
import sys

sys.setrecursionlimit(1000000)

input_position_in_fizzbuzz_sequence = input()

cumulative_length_by_digit_count = {}

cumulative_length_by_digit_count[0] = 0

fizzbuzz_digit_length = 0

for digit_count in range(20):

    minimum_number_with_digit_count = 10 ** digit_count
    maximum_number_with_digit_count = 10 ** (digit_count + 1) - 1

    fizz_count = maximum_number_with_digit_count // 3 - minimum_number_with_digit_count // 3
    buzz_count = maximum_number_with_digit_count // 5 - (minimum_number_with_digit_count - 1) // 5
    fizzbuzz_count = maximum_number_with_digit_count // 15 - minimum_number_with_digit_count // 15

    normal_number_count = (maximum_number_with_digit_count - minimum_number_with_digit_count 
                          - fizz_count - buzz_count + fizzbuzz_count + 1)

    cumulative_length_by_digit_count[digit_count + 1] = (
        cumulative_length_by_digit_count[digit_count] +
        normal_number_count * (digit_count + 1) +
        fizz_count * 4 +
        buzz_count * 4
    )

    if input_position_in_fizzbuzz_sequence <= cumulative_length_by_digit_count[digit_count + 1]:
        input_position_in_fizzbuzz_sequence -= cumulative_length_by_digit_count[digit_count]
        fizzbuzz_digit_length = digit_count + 1
        break

partial_number = 0

for current_digit_index in range(fizzbuzz_digit_length - 1, -1, -1):

    partial_number *= 10

    digits_to_test = range(10)

    if partial_number == 0:
        digits_to_test = range(1, 11)

    for current_digit in digits_to_test:

        left_endpoint = partial_number + current_digit * (10 ** current_digit_index)
        right_endpoint = partial_number + (current_digit + 1) * (10 ** current_digit_index) - 1

        fizz_count = right_endpoint // 3 - (left_endpoint - 1) // 3
        buzz_count = right_endpoint // 5 - (left_endpoint - 1) // 5
        fizzbuzz_count = right_endpoint // 15 - (left_endpoint - 1) // 15

        normal_number_count = (right_endpoint - left_endpoint 
                               - fizz_count - buzz_count + fizzbuzz_count + 1)

        sub_range_length = (normal_number_count * fizzbuzz_digit_length
                            + fizz_count * 4
                            + buzz_count * 4
        )

        if input_position_in_fizzbuzz_sequence > sub_range_length:
            input_position_in_fizzbuzz_sequence -= sub_range_length
        else:
            partial_number += current_digit
            break

fizzbuzz_output_string = ''

for value in range(partial_number, partial_number + 100):

    is_fizz = (value % 3 == 0)
    is_buzz = (value % 5 == 0)

    if is_fizz:
        fizzbuzz_output_string += 'Fizz'
    if is_buzz:
        fizzbuzz_output_string += 'Buzz'
    if not is_fizz and not is_buzz:
        fizzbuzz_output_string += str(value)

print fizzbuzz_output_string[input_position_in_fizzbuzz_sequence - 1 : input_position_in_fizzbuzz_sequence + 19]