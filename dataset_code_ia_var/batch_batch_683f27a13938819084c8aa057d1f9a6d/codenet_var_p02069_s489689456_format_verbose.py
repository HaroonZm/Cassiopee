import heapq
import sys
from operator import itemgetter

read_line = sys.stdin.readline

number_of_intervals, maximum_value = map(int, read_line().split())

interval_list = []
interval_endpoints = []

for _ in range(number_of_intervals):
    left_endpoint, right_endpoint = map(int, read_line().split())
    interval_list.append((left_endpoint, right_endpoint))
    interval_endpoints.append(left_endpoint)
    interval_endpoints.append(right_endpoint)

sorted_unique_endpoints = sorted(set(interval_endpoints))

coordinate_compression_mapping = {}

for compressed_index, original_endpoint in enumerate(sorted_unique_endpoints):
    coordinate_compression_mapping[original_endpoint] = compressed_index

imos_algorithm_array = [0] * (len(coordinate_compression_mapping) + 1)

interval_list.sort(key=itemgetter(0))

max_heap_of_right_endpoints = []
minimum_number_of_operations_x = 0
current_rightmost_point = 0

for interval_index, (interval_left, interval_right) in enumerate(interval_list, 1):

    heapq.heappush(max_heap_of_right_endpoints, -interval_right)

    if interval_index < number_of_intervals and interval_list[interval_index][0] > current_rightmost_point:
        next_rightmost = -heapq.heappop(max_heap_of_right_endpoints)
        current_rightmost_point = next_rightmost
        minimum_number_of_operations_x += 1

    imos_algorithm_array[coordinate_compression_mapping[interval_left]] += 1
    imos_algorithm_array[coordinate_compression_mapping[interval_right]] -= 1

if maximum_value > current_rightmost_point:
    minimum_number_of_operations_x += 1

for index in range(1, len(imos_algorithm_array)):
    imos_algorithm_array[index] += imos_algorithm_array[index - 1]

minimum_number_of_operations_y = number_of_intervals + 1 - min(imos_algorithm_array[:coordinate_compression_mapping[maximum_value]])

print(minimum_number_of_operations_x, minimum_number_of_operations_y)