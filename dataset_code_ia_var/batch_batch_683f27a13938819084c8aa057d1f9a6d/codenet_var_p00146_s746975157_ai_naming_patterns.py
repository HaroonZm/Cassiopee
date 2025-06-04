def initialize_distances(node_count):
    pair_count = 0
    node_pairs = list(distance_dict.items())
    for index_a, value_a in node_pairs:
        pair_count += 1
        for index_b, value_b in node_pairs[pair_count:]:
            abs_distance = abs(value_a - value_b)
            distance_dict[(index_a, index_b)] = abs_distance
            distance_dict[(index_b, index_a)] = abs_distance
    return

def dynamic_solve(current_node, visited_mask, cumulative_weight):
    if visited_mask == (1 << total_nodes) - 1:
        return 0, node_names[current_node]
    cost, path = dp_table[current_node][visited_mask]
    if cost >= 0:
        return cost, path

    min_cost = 1e10
    optimal_path = []
    for next_node in range(total_nodes):
        next_mask = 1 << next_node
        if (visited_mask & next_mask) == 0:
            candidate_cost, candidate_path = dynamic_solve(next_node, visited_mask | next_mask, cumulative_weight + node_weights[next_node])
            candidate_cost += distance_dict[(next_node, current_node)] * cumulative_weight
            if min_cost > candidate_cost:
                min_cost = candidate_cost
                optimal_path = candidate_path
    optimal_path = node_names[current_node] + optimal_path
    dp_table[current_node][visited_mask] = [min_cost, optimal_path]
    return min_cost, optimal_path

node_names = {}
distance_dict = {}
node_weights = {}
total_nodes = input()
dp_table = [[[-1, []] for _ in range(1 << total_nodes)] for _ in range(total_nodes)]
for node_index in range(total_nodes):
    node_value, distance_value, weight_value = map(int, raw_input().split())
    node_names[node_index] = [node_value]
    distance_dict[node_index] = distance_value / 2000.0
    node_weights[node_index] = weight_value * 20
initialize_distances(total_nodes)

global_min_cost = 1e10
optimal_result_path = []
for node_index, weight in node_weights.items():
    result_cost, result_path = dynamic_solve(node_index, 1 << node_index, weight + 70.0)
    if global_min_cost > result_cost:
        global_min_cost = result_cost
        optimal_result_path = result_path

for node in optimal_result_path:
    print str(node),