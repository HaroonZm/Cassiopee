import sys
import numpy as np

stdin_buffer = sys.stdin.buffer
stdin_read = stdin_buffer.read
stdin_readline = stdin_buffer.readline
stdin_readlines = stdin_buffer.readlines

node_count, edge_count, reward_base = map(int, stdin_readline().split())
edge_data_flat = np.array(stdin_read().split(), dtype=np.int64)

edge_from_nodes = edge_data_flat[::3]
edge_to_nodes = edge_data_flat[1::3]
edge_weights = edge_data_flat[2::3]
edge_adjusted_weights = reward_base - edge_weights

distance_inf = 10**18
distance_arr = np.full(node_count + 1, distance_inf, dtype=np.int64)
distance_arr[1] = 0

for iteration_index in range(node_count * 2 + 10):
    distance_candidate = distance_arr[edge_from_nodes] + edge_adjusted_weights
    update_mask = (distance_arr[edge_to_nodes] > distance_candidate) & (distance_candidate < distance_inf // 2)
    update_targets = edge_to_nodes[update_mask]
    update_values = distance_candidate[update_mask]
    if iteration_index > node_count:
        distance_arr[update_targets] = -distance_inf
    else:
        sort_indices = update_values.argsort()[::-1]
        update_targets = update_targets[sort_indices]
        update_values = update_values[sort_indices]
        distance_arr[update_targets] = update_values

final_result = -distance_arr[node_count]
if final_result < 0:
    final_result = 0
elif final_result == distance_inf:
    final_result = -1
print(final_result)