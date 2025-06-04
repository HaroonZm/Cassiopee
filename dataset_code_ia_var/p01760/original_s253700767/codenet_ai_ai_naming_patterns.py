import sys

target_value, max_total_count = [int(value) for value in sys.stdin.readline().split()]
time_values = [int(value) for value in sys.stdin.readline().split()]
count_steps = [int(value) for value in sys.stdin.readline().split()]

min_abs_difference = float("inf")

for count_first in range(max_total_count + 1):
    total_step_first = count_steps[0] * count_first
    if total_step_first > max_total_count:
        continue
    for count_second in range(max_total_count + 1):
        total_step_second = count_steps[1] * count_second
        combined_steps = total_step_first + total_step_second
        if combined_steps > max_total_count or combined_steps < 1:
            continue
        weighted_time_sum = total_step_first * time_values[0] + total_step_second * time_values[1]
        weighted_time_avg = weighted_time_sum / combined_steps
        current_difference = abs(target_value - weighted_time_avg)
        if current_difference < min_abs_difference:
            min_abs_difference = current_difference

print(min_abs_difference)