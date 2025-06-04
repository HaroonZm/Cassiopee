node_count = int(input())
adjacency_list = [[] for node_index in range(node_count)]
total_subgraphs = 0
for start_index in range(1, node_count + 1):
    total_subgraphs += (node_count - start_index + 1) * (node_count - start_index + 2) // 2
for edge_index in range(node_count - 1):
    node_u, node_v = map(int, input().split())
    min_node = min(node_u, node_v)
    max_node = max(node_u, node_v)
    total_subgraphs -= min_node * (node_count - max_node + 1)
print(total_subgraphs)