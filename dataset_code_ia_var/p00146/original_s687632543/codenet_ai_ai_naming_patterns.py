def initialize_distance_matrix(node_count):
    distance_matrix_index = 0
    node_items_list = list(node_distance_dict.items())
    for source_index, source_distance in node_items_list:
        distance_matrix_index += 1
        for target_index, target_distance in node_items_list[distance_matrix_index:]:
            distance_value = abs(source_distance - target_distance)
            node_distance_dict_tuple[(source_index, target_index)] = distance_value
            node_distance_dict_tuple[(target_index, source_index)] = distance_value
    return

def tsp_solver(current_idx, visited_mask, current_weight):
    if visited_mask == (1 << total_nodes) - 1:
        return 0, node_name_dict[current_idx]
    cached_result, cached_route = dp_table[current_idx][visited_mask]
    if cached_result != 1e12:
        return cached_result, cached_route

    min_cost = 1e12
    min_route = []
    for next_node in range(total_nodes):
        next_node_mask = 1 << next_node
        if (visited_mask & next_node_mask) == 0:
            result_cost, result_route = tsp_solver(next_node, visited_mask | next_node_mask, current_weight + node_weight_dict[next_node])
            result_cost += node_distance_dict_tuple[(next_node, current_idx)] / 2000.0 * (current_weight + 70.0)
            if min_cost > result_cost:
                min_cost = result_cost
                min_route = result_route
    min_route = node_name_dict[current_idx] + min_route
    dp_table[current_idx][visited_mask] = [min_cost, min_route]
    return min_cost, min_route

node_name_dict = {}
node_distance_dict = {}
node_weight_dict = {}
node_distance_dict_tuple = {}
total_nodes = int(input())
dp_table = [[[1e12, []] for _ in [0] * (1 << total_nodes)] for _ in range(total_nodes)]
for node_idx in range(total_nodes):
    node_info_1, node_info_2, node_info_3 = map(int, input().split())
    node_name_dict[node_idx] = [node_info_1]
    node_distance_dict[node_idx] = node_info_2
    node_weight_dict[node_idx] = node_info_3 * 20
initialize_distance_matrix(total_nodes)

optimal_cost = 1e12
optimal_route = []
for start_node_idx, start_node_weight in node_weight_dict.items():
    current_cost, current_route = tsp_solver(start_node_idx, 1 << start_node_idx, start_node_weight)
    if optimal_cost > current_cost:
        optimal_cost = current_cost
        optimal_route = current_route

for route_node in optimal_route[:-1]:
    print(str(route_node), end=' ')
print(str(optimal_route[-1]))