import sys
input_stream_buffer = sys.stdin.buffer
read_input_buffer = input_stream_buffer.read
read_line_buffer = input_stream_buffer.readline
read_lines_buffer = input_stream_buffer.readlines

from bisect import bisect_left as bisect_left_c, bisect_right as bisect_right_c

node_count = int(read_line_buffer())
map_values = map(int, read_input_buffer().split())
edge_pairs = zip(map_values, map_values)

adjacency_list = [[] for _ in range(node_count + 1)]
for edge_node_u, edge_node_v in edge_pairs:
    adjacency_list[edge_node_u].append(edge_node_v)
    adjacency_list[edge_node_v].append(edge_node_u)

root_node = 1
parent_node = [0] * (node_count + 1)
traversal_order = []
dfs_stack = [root_node]
while dfs_stack:
    current_node = dfs_stack.pop()
    traversal_order.append(current_node)
    for neighbor_node in adjacency_list[current_node]:
        if neighbor_node == parent_node[current_node]:
            continue
        parent_node[neighbor_node] = current_node
        dfs_stack.append(neighbor_node)

def pair_segments_with_bound(segment_lengths, max_length):
    paired_count = 0
    while segment_lengths and segment_lengths[-1] == max_length:
        segment_lengths.pop()
        paired_count += 1
    bisect_idx = bisect_right_c(segment_lengths, max_length // 2)
    lower_segments = segment_lengths[:bisect_idx][::-1]
    upper_segments = segment_lengths[bisect_idx:]
    candidate_list = []
    remaining_segments = []
    for segment_b in upper_segments[::-1]:
        while lower_segments and lower_segments[-1] + segment_b <= max_length:
            candidate_list.append(lower_segments.pop())
        if candidate_list:
            candidate_list.pop()
            paired_count += 1
        else:
            remaining_segments.append(segment_b)
    candidate_list += lower_segments[::-1]
    candidate_length = len(candidate_list)
    quotient, remainder = divmod(candidate_length, 2)
    if remainder:
        return paired_count + len(remaining_segments) + quotient, candidate_list[0]
    else:
        paired_count += quotient
        if remaining_segments:
            return paired_count + len(remaining_segments) - 1, remaining_segments[-1]
        else:
            return paired_count, 0

def calculate_min_segments(max_allowed_length):
    segment_dp = [0] * (node_count + 1)
    pending_segments = [[] for _ in range(node_count + 1)]
    for visiting_node in reversed(traversal_order):
        parent_visiting = parent_node[visiting_node]
        segment_set = pending_segments[visiting_node]
        segment_set.sort()
        segments_formed, segment_left = pair_segments_with_bound(segment_set, max_allowed_length)
        segment_dp[visiting_node] += segments_formed
        segment_dp[parent_visiting] += segment_dp[visiting_node]
        pending_segments[parent_visiting].append(segment_left + 1)
        if visiting_node == root_node:
            return segment_dp[root_node] if not segment_left else segment_dp[root_node] + 1

total_segments = calculate_min_segments(node_count + 10)
binary_search_left = 0
binary_search_right = node_count
while binary_search_left + 1 < binary_search_right:
    mid_length = (binary_search_left + binary_search_right) // 2
    if calculate_min_segments(mid_length) == total_segments:
        binary_search_right = mid_length
    else:
        binary_search_left = mid_length
print(total_segments, binary_search_right)