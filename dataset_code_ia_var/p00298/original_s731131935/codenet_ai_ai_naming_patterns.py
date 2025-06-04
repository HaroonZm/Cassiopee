import sys
from itertools import accumulate

CONST_INF = 10 ** 20

num_nodes = int(input())
capacity_list = []
weight_list = []
for _ in range(num_nodes):
    cur_capacity, cur_weight = map(int, input().split())
    capacity_list.append(cur_capacity)
    weight_list.append(cur_weight)

prefix_weight_sum = [0] + list(accumulate(weight_list))

connection_matrix = [[None] * num_nodes for _ in range(num_nodes)]
for idx in range(num_nodes):
    connection_matrix[idx][idx] = True

def is_connection_possible(start_idx, end_idx):
    if connection_matrix[start_idx][end_idx] is not None:
        return connection_matrix[start_idx][end_idx]
    can_left = (capacity_list[start_idx] >= prefix_weight_sum[end_idx + 1] - prefix_weight_sum[start_idx + 1]) and is_connection_possible(start_idx + 1, end_idx)
    can_right = (capacity_list[end_idx] >= prefix_weight_sum[end_idx] - prefix_weight_sum[start_idx]) and is_connection_possible(start_idx, end_idx - 1)
    connection_matrix[start_idx][end_idx] = can_left or can_right
    return connection_matrix[start_idx][end_idx]

for left_idx in range(num_nodes):
    for right_idx in range(left_idx + 1, num_nodes):
        is_connection_possible(left_idx, right_idx)

min_partition_steps = [CONST_INF] * (num_nodes + 1)
min_partition_steps[0] = 0
for seg_start in range(num_nodes):
    for seg_end in range(seg_start, num_nodes):
        if connection_matrix[seg_start][seg_end]:
            min_partition_steps[seg_end + 1] = min(min_partition_steps[seg_end + 1], min_partition_steps[seg_start] + 1)
        else:
            break
print(min_partition_steps[num_nodes])