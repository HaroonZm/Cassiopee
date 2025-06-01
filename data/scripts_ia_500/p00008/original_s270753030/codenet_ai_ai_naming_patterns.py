import sys
import itertools

for input_line in sys.stdin:
    target_sum = int(input_line)
    count_matching_combinations = 0
    for digit_tuple in itertools.product(range(10), repeat=4):
        if sum(digit_tuple) == target_sum:
            count_matching_combinations += 1
    print(count_matching_combinations)