import heapq
while True:
    num_nodes = int(input())
    if not num_nodes:
        break
    node_neighbors = [0] * num_nodes
    for node_idx in range(num_nodes):
        node_neighbors[node_idx] = list(map(int, input().split()[1:]))

    reachability_matrix = [[0] * 51 for _ in range(51)]

    for src_idx in range(num_nodes):
        for dst_idx in range(num_nodes):
            reachability_matrix[dst_idx][src_idx] = 1 << src_idx
    for step in range(1, 31):
        current_nodes = [node for node in range(num_nodes) if step in node_neighbors[node]]
        for from_node in current_nodes:
            for to_node in current_nodes:
                reachability_matrix[step][from_node] |= reachability_matrix[step - 1][to_node]
        for node in range(num_nodes):
            reachability_matrix[step][node] |= reachability_matrix[step - 1][node]
    min_days_needed = 40
    for day in range(31):
        for node in range(num_nodes):
            if reachability_matrix[day][node] == (1 << num_nodes) - 1:
                min_days_needed = min(min_days_needed, day)
    if min_days_needed > 30:
        print(-1)
    else:
        print(min_days_needed)