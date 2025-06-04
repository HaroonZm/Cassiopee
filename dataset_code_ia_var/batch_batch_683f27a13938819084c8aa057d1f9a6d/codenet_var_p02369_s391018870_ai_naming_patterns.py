def compute_bellman_ford(node_count, source_node):
    distance_list = [float('inf')] * node_count
    distance_list[source_node] = 0
    for iteration_index in range(node_count):
        has_updated = False
        for edge_start, edge_end, edge_weight in edge_list:
            if distance_list[edge_end] > distance_list[edge_start] + edge_weight:
                distance_list[edge_end] = distance_list[edge_start] + edge_weight
                has_updated = True
                if iteration_index == node_count - 1:
                    return False
        if not has_updated:
            break
    return True

total_nodes, total_edges = map(int, input().split())
edge_list = []
for edge_index in range(total_edges):
    start_node, end_node = map(int, input().split())
    edge_list.append([start_node, end_node, -1])
for node_index in range(total_nodes):
    if not compute_bellman_ford(total_nodes, node_index):
        print(1)
        quit()
print(0)