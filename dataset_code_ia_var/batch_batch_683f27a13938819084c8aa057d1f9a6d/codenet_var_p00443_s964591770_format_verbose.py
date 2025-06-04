def compute_greatest_common_divisor(integer_a, integer_b):
    current_maximum = max(integer_a, integer_b)
    current_minimum = min(integer_a, integer_b)
    
    while True:
        remainder = current_maximum % current_minimum
        current_maximum = current_minimum
        current_minimum = remainder
        
        if remainder == 0:
            break
            
    return current_maximum


while True:
    user_input = input()
    
    if not user_input:
        break
    
    number_of_nodes = int(user_input)
    
    edge_weights = []
    child_indices_list = []
    root_index = number_of_nodes * (number_of_nodes - 1) // 2
    
    for current_node_index in range(number_of_nodes):
        input_line = input().split()
        left_edge_weight, right_edge_weight, left_child_index, right_child_index = list(map(int, input_line))
        
        edge_weights.append((left_edge_weight, right_edge_weight))
        root_index -= left_child_index + right_child_index
        left_child_index -= 1
        right_child_index -= 1
        child_indices_list.append((left_child_index, right_child_index))
    
    def generate_leaf_product_values(node_index):
        left_subtree_leaf_values = []
        right_subtree_leaf_values = []
        left_subtree_multipliers = []
        right_subtree_multipliers = []
        
        if child_indices_list[node_index][0] != -1:
            left_subtree_leaf_values, left_subtree_multipliers = generate_leaf_product_values(child_indices_list[node_index][0])
        else:
            left_subtree_leaf_values = [1]
            left_subtree_multipliers = []
        
        if child_indices_list[node_index][1] != -1:
            right_subtree_leaf_values, right_subtree_multipliers = generate_leaf_product_values(child_indices_list[node_index][1])
        else:
            right_subtree_leaf_values = [1]
            right_subtree_multipliers = []
        
        left_multiplier = edge_weights[node_index][0]
        for multiplier in left_subtree_multipliers:
            left_multiplier *= multiplier
            
        right_multiplier = edge_weights[node_index][1]
        for multiplier in right_subtree_multipliers:
            right_multiplier *= multiplier
        
        for i in range(len(left_subtree_leaf_values)):
            left_subtree_leaf_values[i] *= right_multiplier
        
        for i in range(len(right_subtree_leaf_values)):
            right_subtree_leaf_values[i] *= left_multiplier
        
        return (
            left_subtree_leaf_values + right_subtree_leaf_values,
            left_subtree_multipliers + right_subtree_multipliers + [edge_weights[node_index][0] + edge_weights[node_index][1]]
        )
    
    leaf_values, multiplication_factors = generate_leaf_product_values(root_index - 1)
    
    current_gcd = leaf_values[0]
    for value in leaf_values:
        current_gcd = compute_greatest_common_divisor(value, current_gcd)
    
    for i in range(len(leaf_values)):
        leaf_values[i] //= current_gcd
    
    print(sum(leaf_values))