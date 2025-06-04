def compute_gcd(value_a, value_b):
    current_max = max(value_a, value_b)
    current_min = min(value_a, value_b)
    while True:
        temp_mod = current_max % current_min
        current_max = current_min
        current_min = temp_mod
        if temp_mod == 0:
            break
    return current_max

while True:
    node_count = input()
    if not node_count:
        break
    cost_pairs = []
    edge_links = []
    root_index = node_count * (node_count - 1) / 2
    for node_idx in range(node_count):
        input_parts = raw_input().split()
        left_cost, right_cost, left_edge, right_edge = list(map(int, input_parts))
        cost_pairs.append((left_cost, right_cost))
        root_index -= left_edge + right_edge
        left_edge -= 1
        right_edge -= 1
        edge_links.append((left_edge, right_edge))
    def traverse_tree(current_edge_idx):
        left_nodes = []
        right_nodes = []
        left_values = []
        right_values = []
        left_child_idx, right_child_idx = edge_links[current_edge_idx]
        if left_child_idx != -1:
            left_nodes, left_values = traverse_tree(left_child_idx)
        else:
            left_nodes = [1]
            left_values = []
        if right_child_idx != -1:
            right_nodes, right_values = traverse_tree(right_child_idx)
        else:
            right_nodes = [1]
            right_values = []
        left_multiplier = cost_pairs[current_edge_idx][0]
        for left_factor in left_values:
            left_multiplier *= left_factor
        right_multiplier = cost_pairs[current_edge_idx][1]
        for right_factor in right_values:
            right_multiplier *= right_factor
        for idx in range(len(left_nodes)):
            left_nodes[idx] *= right_multiplier
        for idx in range(len(right_nodes)):
            right_nodes[idx] *= left_multiplier
        return left_nodes + right_nodes, left_values + right_values + [cost_pairs[current_edge_idx][0] + cost_pairs[current_edge_idx][1]]
    result_nodes, result_values = traverse_tree(root_index - 1)
    gcd_value = result_nodes[0]
    for candidate in result_nodes:
        gcd_value = compute_gcd(candidate, gcd_value)
    for idx in range(len(result_nodes)):
        result_nodes[idx] //= gcd_value
    print sum(result_nodes)