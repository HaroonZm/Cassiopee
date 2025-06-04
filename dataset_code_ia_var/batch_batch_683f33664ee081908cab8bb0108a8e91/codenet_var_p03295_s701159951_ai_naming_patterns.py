num_points, num_intervals = map(int, input().split())
interval_list = []
for idx_interval in range(num_intervals):
    interval_start, interval_end = map(int, input().split())
    interval_list.append([interval_start, interval_end])
interval_list_sorted = sorted(interval_list, key=lambda interval: interval[1])

if num_intervals == 0:
    print(0)
else:
    current_end = interval_list_sorted[0][1]
    interval_list_sorted.pop(0)
    num_selected = 1
    while interval_list_sorted:
        if interval_list_sorted[0][0] >= current_end:
            num_selected += 1
            current_end = interval_list_sorted[0][1]
        interval_list_sorted.pop(0)
    print(num_selected)