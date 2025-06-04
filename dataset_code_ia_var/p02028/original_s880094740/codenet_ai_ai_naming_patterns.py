from bisect import bisect_left as bisect_left_func
from itertools import accumulate as accumulate_func

row_count, col_count = map(int, input().split())
primary_list = sorted(map(int, input().split()))
secondary_list = list(map(int, input().split()))
primary_prefix_sum = [0] + list(accumulate_func(primary_list))
primary_list.insert(0, -1)

total_sum = 0
for secondary_value in secondary_list:
    insert_index = bisect_left_func(primary_list, secondary_value)
    total_sum += primary_prefix_sum[insert_index - 1] + (row_count - insert_index + 1) * secondary_value
print(total_sum)