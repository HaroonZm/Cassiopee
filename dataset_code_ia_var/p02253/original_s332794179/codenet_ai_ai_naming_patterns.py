num_intervals = int(input())
interval_list = [[int(value) for value in input().split()] for _ in range(num_intervals)]
interval_list.sort(key=lambda interval: interval[1])
current_end_time = 0
selected_intervals_count = 0
for interval in interval_list:
    interval_start = interval[0]
    interval_end = interval[1]
    if current_end_time < interval_start:
        selected_intervals_count += 1
        current_end_time = interval_end
print(selected_intervals_count)