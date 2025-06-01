import itertools
import sys

sum_counts = [0] * 51
digit_range = range(10)

for digit_a, digit_b, digit_c, digit_d in itertools.product(digit_range, digit_range, digit_range, digit_range):
    sum_index = digit_a + digit_b + digit_c + digit_d
    sum_counts[sum_index] += 1

for input_line in sys.stdin.readlines():
    input_value = int(input_line)
    print(sum_counts[input_value])