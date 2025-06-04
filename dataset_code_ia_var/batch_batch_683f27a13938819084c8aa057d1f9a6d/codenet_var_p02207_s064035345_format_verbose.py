from math import log10
from bisect import bisect_left

number_of_intervals = int(input())

interval_data = [[0, 0]] + [list(map(int, input().split())) for _ in range(number_of_intervals)]

for interval_index in range(1, number_of_intervals + 1):
    interval_position = interval_data[interval_index][0]
    interval_probability_percentage = interval_data[interval_index][1]
    interval_data[interval_index][1] = log10(1 - interval_probability_percentage / 10)

for cumulative_index in range(number_of_intervals):
    interval_data[cumulative_index + 1][1] += interval_data[cumulative_index][1]

number_of_queries = int(input())

for _ in range(number_of_queries):
    query_start, query_end = map(int, input().split())
    left_interval_index = bisect_left(interval_data, [query_start, 0]) - 1
    right_interval_index = bisect_left(interval_data, [query_end, 0]) - 1
    cumulative_probability_log_difference = interval_data[right_interval_index][1] - interval_data[left_interval_index][1] + 9
    cumulative_probability = 10 ** cumulative_probability_log_difference
    print(cumulative_probability)