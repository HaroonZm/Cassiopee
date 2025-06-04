num_intervals, num_bridges = (int(value) - 1 for value in input().split())
interval_list = []
for bridge_index in range(num_bridges + 1):
    interval_list.append(list(map(int, input().split())))
interval_list.sort(key=lambda interval: interval[1])
bridge_destroyed_count = 0
current_right_position = -1
for interval in interval_list:
    interval_left = interval[0]
    interval_right = interval[1]
    if not (interval_left <= current_right_position < interval_right):
        current_right_position = interval_right - 1
        bridge_destroyed_count += 1
print(bridge_destroyed_count)