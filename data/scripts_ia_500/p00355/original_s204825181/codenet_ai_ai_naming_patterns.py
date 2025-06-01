input_start, input_end = [int(value) for value in input().split()]
number_of_intervals = int(input())

overlap_flag = 0

for interval_index in range(number_of_intervals):
    interval_start, interval_end = [int(value) for value in input().split()]
    if input_start < interval_end and interval_start < input_end:
        overlap_flag = 1
        break

print(overlap_flag)