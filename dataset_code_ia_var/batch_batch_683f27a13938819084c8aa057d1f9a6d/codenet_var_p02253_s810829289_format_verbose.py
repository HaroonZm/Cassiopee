total_number_of_time_intervals = int(input())

list_of_time_intervals = [
    list(map(int, input().split())) for _ in range(total_number_of_time_intervals)
]

list_of_time_intervals.sort(key=lambda interval: interval[1])

last_selected_end_time = -1
number_of_non_overlapping_intervals_selected = 0

for interval_start_time, interval_end_time in list_of_time_intervals:
    if last_selected_end_time < interval_start_time:
        number_of_non_overlapping_intervals_selected += 1
        last_selected_end_time = interval_end_time

print(number_of_non_overlapping_intervals_selected)