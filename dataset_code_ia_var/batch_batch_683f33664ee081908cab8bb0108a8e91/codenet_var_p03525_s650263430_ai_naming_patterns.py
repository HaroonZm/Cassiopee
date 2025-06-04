num_offsets = int(input())
offset_list = list(map(int, input().split()))

from collections import Counter
from collections import defaultdict

offset_counter = Counter(offset_list)
offset_counter[0] += 1

for offset_value in range(13):
    if offset_value == 0 or offset_value == 12:
        if offset_counter[offset_value] >= 2:
            print(0)
            exit()
    else:
        if offset_counter[offset_value] >= 3:
            print(0)
            exit()

offset_list.sort()

time_count_map = defaultdict(int)
time_count_map[24] += 1
use_original_offset = True
for offset in offset_list:
    if use_original_offset:
        time_count_map[offset] += 1
        use_original_offset = False
    else:
        time_count_map[24 - offset] += 1
        use_original_offset = True

min_time_diff = min(offset_list)
time_markers = list(time_count_map.keys())
time_markers.sort()
for prev_time, next_time in zip(time_markers, time_markers[1:]):
    min_time_diff = min(min_time_diff, next_time - prev_time)

print(min_time_diff)