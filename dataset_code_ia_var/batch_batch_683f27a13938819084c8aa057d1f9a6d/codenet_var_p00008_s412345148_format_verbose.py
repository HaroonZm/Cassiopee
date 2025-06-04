import itertools
import sys

number_of_sums_per_digit_sum = [0] * 51

digits_range = range(10)

for first_digit, second_digit, third_digit, fourth_digit in itertools.product(digits_range, digits_range, digits_range, digits_range):
    digit_sum = first_digit + second_digit + third_digit + fourth_digit
    number_of_sums_per_digit_sum[digit_sum] += 1

for input_line in sys.stdin.readlines():
    input_digit_sum = int(input_line)
    print(number_of_sums_per_digit_sum[input_digit_sum])