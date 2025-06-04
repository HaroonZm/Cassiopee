input_value_n = int(raw_input())
input_edges_raw = [raw_input().split() for input_edge_index in range(input_value_n - 1)]
input_edges_sorted = [sorted(map(int, input_edge_pair)) for input_edge_pair in input_edges_raw]

sum_total_segments = sum([segment_index * (input_value_n - segment_index + 1) for segment_index in range(1, input_value_n + 1)])
sum_removed_segments = sum([edge_start * (input_value_n - edge_end + 1) for edge_start, edge_end in input_edges_sorted])

print sum_total_segments - sum_removed_segments