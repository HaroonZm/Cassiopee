import os
import sys

for input_line in sys.stdin:
    value_limit, diff_threshold = [int(parsed_item) for parsed_item in input_line.split()]

    fibonacci_sequence = [1, 1]

    for sequence_index in range(value_limit):
        fibonacci_sequence.append((fibonacci_sequence[-1] + fibonacci_sequence[-2]) % 1001)

    fibonacci_sorted = sorted(fibonacci_sequence[2:])

    consecutive_difference_count = 1
    for diff_index in range(len(fibonacci_sorted) - 1):
        if fibonacci_sorted[diff_index + 1] - fibonacci_sorted[diff_index] >= diff_threshold:
            consecutive_difference_count += 1

    print(consecutive_difference_count)