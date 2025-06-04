def compute_tsp_minimum_path(weight_matrix):
    constant_infinity = float("inf")
    node_count = len(weight_matrix)
    dp_table = [[constant_infinity] * node_count for partial_state_mask in range(1 << node_count)]
    dp_table[1 << 0][0] = 0

    for partial_state_mask in range(1 << node_count):
        for current_node in range(node_count):
            if (partial_state_mask >> current_node) & 1:
                for next_node in range(node_count):
                    if not ((partial_state_mask >> next_node) & 1):
                        next_mask = partial_state_mask | (1 << next_node)
                        new_cost = dp_table[partial_state_mask][current_node] + weight_matrix[current_node][next_node]
                        if new_cost < dp_table[next_mask][next_node]:
                            dp_table[next_mask][next_node] = new_cost
    final_min_cost = constant_infinity
    for last_node in range(node_count):
        complete_mask = (1 << node_count) - 1
        tour_cost = dp_table[complete_mask][last_node] + weight_matrix[last_node][0]
        if tour_cost < final_min_cost:
            final_min_cost = tour_cost
    return final_min_cost

node_total, edge_total = map(int, input().split())
edge_list = [list(map(int, input().split())) for edge_index in range(edge_total)]
const_infinite_cost = float("inf")

adjacency_matrix = [[const_infinite_cost] * node_total for row_index in range(node_total)]
for edge_index in range(edge_total):
    node_from, node_to, edge_weight = edge_list[edge_index]
    adjacency_matrix[node_from][node_to] = edge_weight
for node_index in range(node_total):
    adjacency_matrix[node_index][node_index] = 0

minimal_tsp_cost = compute_tsp_minimum_path(adjacency_matrix)
if minimal_tsp_cost == const_infinite_cost:
    print(-1)
else:
    print(minimal_tsp_cost)