def find_next_minimal_pair(input_h, input_w):
    input_sum_sq = input_h**2 + input_w**2

    best_h = 150
    best_w = 150
    best_sum_sq = 150**2 + 150**2

    for candidate_w in range(1, 150):
        for candidate_h in range(1, candidate_w):
            candidate_sum_sq = candidate_h**2 + candidate_w**2
            if (input_sum_sq < candidate_sum_sq) or (input_sum_sq == candidate_sum_sq and input_h < candidate_h):
                if (best_sum_sq > candidate_sum_sq) or (best_sum_sq == candidate_sum_sq and best_h > candidate_h):
                    best_h = candidate_h
                    best_w = candidate_w
                    best_sum_sq = candidate_sum_sq

    print(best_h, best_w)

import sys

for input_line in sys.stdin:
    input_values = input_line.split()
    if len(input_values) == 2:
        current_h, current_w = map(int, input_values)
        if current_h != 0 and current_w != 0:
            find_next_minimal_pair(current_h, current_w)