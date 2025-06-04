import heapq

number_of_elements = int(input())
full_input_array = list(map(int, input().split()))

# Prepare minimal prefix sum array using a min-heap
prefix_sum_array = [0] * (number_of_elements + 1)
min_heap_prefix = [element for element in full_input_array[:number_of_elements]]
heapq.heapify(min_heap_prefix)
current_prefix_sum = sum(min_heap_prefix)
prefix_sum_array[0] = current_prefix_sum

for position_in_input in range(number_of_elements, 2 * number_of_elements):
    smallest_element_removed = heapq.heappushpop(min_heap_prefix, full_input_array[position_in_input])
    current_prefix_sum += full_input_array[position_in_input] - smallest_element_removed
    prefix_sum_array[position_in_input - number_of_elements + 1] = current_prefix_sum

# Prepare maximal suffix sum array using a min-heap of negatives (to simulate max-heap)
suffix_sum_array = [0] * (number_of_elements + 1)
negative_max_heap_suffix = [-element for element in full_input_array[2 * number_of_elements:]]
heapq.heapify(negative_max_heap_suffix)
current_suffix_sum = -sum(negative_max_heap_suffix)
suffix_sum_array[-1] = current_suffix_sum

for position_in_input in range(2 * number_of_elements - 1, number_of_elements - 1, -1):
    largest_element_removed = -heapq.heappushpop(negative_max_heap_suffix, -full_input_array[position_in_input])
    current_suffix_sum += full_input_array[position_in_input] - largest_element_removed
    suffix_sum_array[position_in_input - number_of_elements] = current_suffix_sum

# Compute the maximal possible difference between prefix and suffix sums
maximum_difference = max([
    prefix_sum_array[index] - suffix_sum_array[index]
    for index in range(number_of_elements + 1)
])

print(maximum_difference)