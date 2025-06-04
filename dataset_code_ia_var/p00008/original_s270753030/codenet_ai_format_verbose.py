import sys
import itertools

for input_line in sys.stdin:

    target_sum = int(input_line)
    number_of_combinations_with_target_sum = 0

    for four_digit_tuple in itertools.product(range(10), repeat=4):

        sum_of_digits = sum(four_digit_tuple)

        if sum_of_digits == target_sum:
            number_of_combinations_with_target_sum += 1

    print(number_of_combinations_with_target_sum)