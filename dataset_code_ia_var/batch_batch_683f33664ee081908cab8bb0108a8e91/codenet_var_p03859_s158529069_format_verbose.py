from collections import deque
import heapq

# Lecture des entrées
number_of_characters, number_of_intervals = map(int, input().split())
binary_string = input()

# Préparation des bornes des intervalles
interval_boundaries = []
for interval_index in range(number_of_intervals):
    left_endpoint, right_endpoint = map(int, input().split())
    interval_boundaries.append([left_endpoint - 1, right_endpoint - 1, interval_index])
interval_boundaries.append([number_of_characters, float("inf"), float("inf")])

next_index_to_inspect = 0
remaining_ones_in_interval = 0
ones_movement_range_list = []
current_one_index = 0
current_interval_right_end = 0

for interval_iteration in range(number_of_intervals):
    current_interval_left, current_interval_right, _ = interval_boundaries[interval_iteration]
    current_interval_right_end = max(current_interval_right, current_interval_right_end)
    next_interval_left = interval_boundaries[interval_iteration + 1][0]

    for character_index in range(max(current_interval_left, next_index_to_inspect), current_interval_right_end + 1):
        if binary_string[character_index] == "1":
            ones_movement_range_list.append([current_interval_left, None])
            remaining_ones_in_interval += 1
            next_index_to_inspect = max(next_index_to_inspect, character_index + 1)

    if current_interval_right_end - next_interval_left + 1 < remaining_ones_in_interval:
        for _ in range(min(remaining_ones_in_interval, remaining_ones_in_interval - (current_interval_right_end - next_interval_left + 1))):
            ones_movement_range_list[current_one_index][1] = current_interval_right_end - remaining_ones_in_interval + 1
            remaining_ones_in_interval -= 1
            current_one_index += 1

modulo = 10 ** 9 + 7
number_of_arrangements_dp = [0] * (number_of_characters + 1)

for one_index in range(len(ones_movement_range_list)):
    leftmost_index, rightmost_index = ones_movement_range_list[one_index]
    next_dp = [0] * (number_of_characters + 1)

    if one_index == 0:
        next_dp[leftmost_index] += 1
        next_dp[rightmost_index + 1] -= 1
    else:
        for current_position in range(rightmost_index):
            next_dp[max(leftmost_index, current_position + 1)] += number_of_arrangements_dp[current_position]
            next_dp[rightmost_index + 1] -= number_of_arrangements_dp[current_position]

    for accumulation_index in range(number_of_characters):
        next_dp[accumulation_index + 1] += next_dp[accumulation_index]
        next_dp[accumulation_index] %= modulo
        next_dp[accumulation_index + 1] %= modulo

    number_of_arrangements_dp = next_dp

print(sum(number_of_arrangements_dp[0:number_of_characters]) % modulo)