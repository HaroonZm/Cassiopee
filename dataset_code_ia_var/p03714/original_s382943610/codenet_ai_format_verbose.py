import sys

from collections import defaultdict
import heapq as heapq_module

input_stream = sys.stdin
read_line_from_input = input_stream.readline

number_of_elements_per_group = int(read_line_from_input())
full_integer_list = list(map(int, read_line_from_input().split()))

sorted_first_two_groups = sorted(full_integer_list[:2 * number_of_elements_per_group])

smallest_n_elements = sorted_first_two_groups[:number_of_elements_per_group]
frequency_of_small_elements = defaultdict(int)
for index in range(len(smallest_n_elements)):
    frequency_of_small_elements[smallest_n_elements[index]] += 1

largest_n_elements = sorted_first_two_groups[number_of_elements_per_group:]
frequency_of_large_elements = defaultdict(int)
for index in range(len(largest_n_elements)):
    frequency_of_large_elements[largest_n_elements[index]] += 1

maximum_sum_left_part = sum(sorted_first_two_groups[number_of_elements_per_group:])

max_heap_for_smallest_elements = list(map(lambda value: -value, smallest_n_elements))
heapq_module.heapify(max_heap_for_smallest_elements)

rightmost_n_elements = full_integer_list[2 * number_of_elements_per_group:]
sum_of_rightmost_n_elements = sum(rightmost_n_elements)
max_heap_for_rightmost_elements = list(map(lambda value: -value, rightmost_n_elements))
heapq_module.heapify(max_heap_for_rightmost_elements)

maximum_difference = maximum_sum_left_part - sum_of_rightmost_n_elements

for current_index in range(2 * number_of_elements_per_group - 1, number_of_elements_per_group - 1, -1):

    current_value = full_integer_list[current_index]

    if frequency_of_large_elements[current_value] > 0:
        frequency_of_large_elements[current_value] -= 1
        maximum_sum_left_part -= current_value

        while True:
            candidate_value_for_movement = -heapq_module.heappop(max_heap_for_smallest_elements)
            if frequency_of_small_elements[candidate_value_for_movement] > 0:
                frequency_of_small_elements[candidate_value_for_movement] -= 1
                break
        maximum_sum_left_part += candidate_value_for_movement
        frequency_of_large_elements[candidate_value_for_movement] += 1

    else:
        frequency_of_small_elements[current_value] -= 1

    heapq_module.heappush(max_heap_for_rightmost_elements, -current_value)
    removed_value_from_right_heap = -heapq_module.heappop(max_heap_for_rightmost_elements)
    sum_of_rightmost_n_elements += current_value
    sum_of_rightmost_n_elements -= removed_value_from_right_heap

    current_difference = maximum_sum_left_part - sum_of_rightmost_n_elements
    if maximum_difference < current_difference:
        maximum_difference = current_difference

print(maximum_difference)