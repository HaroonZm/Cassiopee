num_nodes, num_edges = map(int, input().split())
segment_limits = [200000 for idx in range(num_nodes - 1)]

for edge_idx in range(num_edges):
    node_a, node_b = map(int, input().split())
    segment_limits[node_a - 1] = min(segment_limits[node_a - 1], node_b - 2)

current_right = -1
segment_count = 0

for segment_idx in range(num_nodes - 1):
    if segment_idx > current_right and segment_limits[segment_idx] != 200000:
        segment_count += 1
        current_right = segment_limits[segment_idx]
    elif segment_idx <= current_right and segment_limits[segment_idx] != 200000:
        current_right = min(segment_limits[segment_idx], current_right)

print(segment_count)