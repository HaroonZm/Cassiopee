number_of_positions, number_of_intervals = map(int, raw_input().split())

position_covered_by_interval = [False] * number_of_positions

for interval_index in xrange(number_of_intervals):

    interval_start, interval_end = map(int, raw_input().split())

    if interval_start < interval_end:
        covered_length = interval_end - interval_start
        position_covered_by_interval[interval_start:interval_end] = [True] * covered_length

total_value = 0

for position_index in xrange(number_of_positions):

    total_value += 1

    if position_covered_by_interval[position_index]:
        total_value += 2

print total_value + 1