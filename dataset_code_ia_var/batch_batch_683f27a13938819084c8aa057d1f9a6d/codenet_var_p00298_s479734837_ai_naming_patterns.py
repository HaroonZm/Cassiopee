import sys

input_stream = sys.stdin

item_count = int(input_stream.readline())
item_data_list = [list(map(int, line.split())) for line in input_stream]

can_partition = [[i == j for j in range(item_count + 1)] for i in range(item_count + 1)]
capacity_list = [0] + [cap for cap, wt in item_data_list]
weight_prefix_sum = [0] + [wt for cap, wt in item_data_list]
for idx in range(1, len(weight_prefix_sum)):
    weight_prefix_sum[idx] += weight_prefix_sum[idx - 1]

for sub_len in range(item_count):
    for start_idx in range(1, item_count + 1 - sub_len):
        end_idx = start_idx + sub_len
        if not can_partition[start_idx][end_idx]:
            continue
        if end_idx + 1 <= item_count:
            total_weight = weight_prefix_sum[end_idx] - weight_prefix_sum[start_idx - 1]
            if total_weight <= capacity_list[end_idx + 1]:
                can_partition[start_idx][end_idx + 1] = True
        total_weight = weight_prefix_sum[end_idx] - weight_prefix_sum[start_idx - 1]
        if total_weight <= capacity_list[start_idx - 1]:
            can_partition[start_idx - 1][end_idx] = True

min_partitions_dp = [999999999] * (item_count + 1)
min_partitions_dp[0] = 0
for begin_idx in range(1, item_count + 1):
    for end_idx in range(1, item_count + 1):
        if can_partition[begin_idx][end_idx]:
            min_partitions_dp[end_idx] = min(min_partitions_dp[end_idx], min_partitions_dp[begin_idx - 1] + 1)

print(min_partitions_dp[-1])