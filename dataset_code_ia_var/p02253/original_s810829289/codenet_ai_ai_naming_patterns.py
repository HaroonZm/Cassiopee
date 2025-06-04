interval_count = int(input())
interval_list = [list(map(int, input().split())) for _ in range(interval_count)]
interval_list.sort(key=lambda interval: interval[1])
current_end = -1
selected_count = 0
for interval_start, interval_end in interval_list:
    if current_end < interval_start:
        selected_count += 1
        current_end = interval_end
print(selected_count)