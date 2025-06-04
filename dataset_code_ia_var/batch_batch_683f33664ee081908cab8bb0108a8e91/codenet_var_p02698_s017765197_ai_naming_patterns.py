import bisect

node_count = int(input())
node_values = list(map(int, input().split()))
adjacency_list = [[] for _ in range(node_count)]

for edge_index in range(node_count - 1):
    node_u, node_v = map(int, input().split())
    adjacency_list[node_u - 1].append(node_v - 1)
    adjacency_list[node_v - 1].append(node_u - 1)

infinity_value = 10 ** 10
dp_lis = [infinity_value for _ in range(node_count)]
longest_path_lengths = [0 for _ in range(node_count)]
stack_traversal = [(-1, 0, None)]

while stack_traversal:
    parent_node, current_node, backup_value = stack_traversal.pop()
    if current_node == -1:
        dp_lis[parent_node] = backup_value
        continue
    replace_index = bisect.bisect_left(dp_lis, node_values[current_node])
    stack_traversal.append((replace_index, -1, dp_lis[replace_index]))
    dp_lis[replace_index] = node_values[current_node]
    longest_path_lengths[current_node] = bisect.bisect_left(dp_lis, infinity_value)
    for neighbor_node in adjacency_list[current_node]:
        if neighbor_node != parent_node:
            stack_traversal.append((current_node, neighbor_node, None))

for path_length in longest_path_lengths:
    print(path_length)