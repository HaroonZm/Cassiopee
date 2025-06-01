import bisect
import sys

def count_elements_outside_ranges(sorted_values, range_leaders, max_offset):
    total_count = 0
    previous_upper_bound = 0

    for leader_value in range_leaders:
        lower_bound = bisect.bisect_left(sorted_values, leader_value - max_offset)
        upper_bound = bisect.bisect_right(sorted_values, leader_value)
        if previous_upper_bound < lower_bound:
            total_count += lower_bound - previous_upper_bound
        previous_upper_bound = upper_bound
    total_count += len(sorted_values) - previous_upper_bound
    return total_count

def binary_search_min_offset(sorted_values, range_leaders, target_count):
    if len(range_leaders) == 0:
        if target_count < len(sorted_values):
            return 'NA'
        else:
            return 0

    min_possible = len(sorted_values) - bisect.bisect_right(sorted_values, range_leaders[-1])
    if target_count < min_possible:
        return 'NA'

    left, right = 0, sorted_values[-1]
    prev_difference = right - 1

    while True:
        mid = (left + right) // 2
        current_count = count_elements_outside_ranges(sorted_values, range_leaders, mid)

        if target_count < current_count:
            left = mid
        else:  # current_count <= target_count
            right = mid

        current_difference = left - right
        if prev_difference == current_difference:
            return right
        prev_difference = current_difference

input_file = sys.stdin
num_values, num_queries = (int(x) for x in input_file.readline().split())
values = [int(input_file.readline()) for _ in range(num_values)]
queries = [line.split() for line in input_file]

sorted_values = sorted(values)
current_range_leaders = []

for operation, arg in queries:
    arg_int = int(arg)
    if operation.startswith('A'):
        current_range_leaders.append(values[arg_int - 1])
        current_range_leaders.sort()
    elif operation.startswith('R'):
        current_range_leaders.remove(values[arg_int - 1])
    else:
        result = binary_search_min_offset(sorted_values, current_range_leaders, arg_int)
        print(result)