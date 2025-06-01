from bisect import bisect
import sys
from collections import defaultdict

input_readline = sys.stdin.readline
output_write = sys.stdout.write

num_elements, num_queries = map(int, input_readline().split())
original_values = [int(input_readline()) for _index in range(num_elements)]
unique_values = list(set(original_values))
unique_values.sort()
value_to_unique_index = {value: index for index, value in enumerate(unique_values)}
value_counts = defaultdict(int)

sorted_values = original_values[:]
sorted_values.sort()
value_to_sorted_index = {}
for index, value in enumerate(sorted_values):
    value_to_sorted_index[value] = index

infinity = 10**9 + 1
present_unique_indices = []

for _query_index in range(num_queries):
    query_type, query_param = input_readline().split()
    query_param_int = int(query_param)
    if query_type == 'ADD':
        target_value = original_values[query_param_int - 1]
        if value_counts[target_value] == 0:
            unique_index = value_to_unique_index[target_value]
            insert_position = bisect(present_unique_indices, unique_index - 1)
            present_unique_indices = present_unique_indices[:insert_position] + [unique_index] + present_unique_indices[insert_position:]
        value_counts[target_value] += 1
    elif query_type == 'REMOVE':
        target_value = original_values[query_param_int - 1]
        value_counts[target_value] -= 1
        if value_counts[target_value] == 0:
            unique_index = value_to_unique_index[target_value]
            remove_position = bisect(present_unique_indices, unique_index - 1)
            present_unique_indices.pop(remove_position)
    else:
        left_bound = -1
        right_bound = infinity
        while left_bound + 1 < right_bound:
            midpoint = (left_bound + right_bound) >> 1
            previous_sorted_index = -1
            count = 0
            for unique_index in present_unique_indices:
                unique_value = unique_values[unique_index]
                current_sorted_index = value_to_sorted_index[unique_value]
                bisect_pos = max(bisect(sorted_values, unique_value - midpoint - 1) - 1, previous_sorted_index)
                count += current_sorted_index - bisect_pos
                previous_sorted_index = current_sorted_index
            if num_elements - count <= query_param_int:
                right_bound = midpoint
            else:
                left_bound = midpoint
        if right_bound == infinity:
            output_write("NA\n")
        else:
            output_write(f"{right_bound}\n")