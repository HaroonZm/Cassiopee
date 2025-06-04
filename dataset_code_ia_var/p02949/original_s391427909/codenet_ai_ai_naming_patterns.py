node_count, edge_count, param_p = map(int, input().split())
adjacency_list = [[] for _ in range(node_count)]
infinity_value = float("inf")
distance_array = [infinity_value] * node_count
distance_array[0] = 0

for _ in range(edge_count):
    from_node, to_node, edge_cost = map(int, input().split())
    adjacency_list[from_node - 1].append((to_node - 1, param_p - edge_cost))

for _ in range(node_count):
    is_updated = False
    for current_node, neighbors in enumerate(adjacency_list):
        for neighbor_node, neighbor_cost in neighbors:
            if distance_array[current_node] != infinity_value and distance_array[neighbor_node] > distance_array[current_node] + neighbor_cost:
                distance_array[neighbor_node] = distance_array[current_node] + neighbor_cost
                is_updated = True
    if not is_updated:
        break
else:
    previous_distance = distance_array[-1]
    for _ in range(node_count):
        is_negative_updated = False
        for current_node, neighbors in enumerate(adjacency_list):
            for neighbor_node, neighbor_cost in neighbors:
                if distance_array[current_node] != infinity_value and distance_array[neighbor_node] > distance_array[current_node] + neighbor_cost:
                    distance_array[neighbor_node] = distance_array[current_node] + neighbor_cost
                    is_negative_updated = True
        if not is_negative_updated:
            break
    if distance_array[-1] != previous_distance:
        print(-1)
        exit()

print(max(0, -distance_array[-1]))