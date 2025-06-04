from collections import deque

def compute_children_from_parent_list(parent_list):
    children_per_node = [set() for _ in range(number_of_nodes)]
    for child_index, parent in enumerate(parent_list):
        children_per_node[parent].add(child_index + 1)
    return children_per_node

def generate_levels_and_level_map(children_per_node):
    node_levels_as_sets = []
    node_to_level_map = {}
    processing_queue = deque([(0, 0)])
    while processing_queue:
        current_node, current_level = processing_queue.popleft()
        if node_is_fixed[current_node]:
            continue
        if len(node_levels_as_sets) <= current_level:
            node_levels_as_sets.append(set())
        node_levels_as_sets[current_level].add(current_node)
        node_to_level_map[current_node] = current_level
        processing_queue.extend(
            (child_node, current_level + 1) for child_node in children_per_node[current_node]
        )
    return node_levels_as_sets, node_to_level_map

def compute_node_positions_in_permutation(permutation_list):
    node_to_position = [0] * number_of_nodes
    for position, node in enumerate(permutation_list):
        node_to_position[node] = position
    return node_to_position

def identify_leaf_nodes(levels_per_node):
    leaf_nodes_dict = {}
    child_node_identity = [-1] * number_of_nodes
    for level, nodes_in_level in reversed(list(enumerate(levels_per_node))):
        for node_index in nodes_in_level:
            leaf_child_value = child_node_identity[node_index]
            parent_index = parent_list[node_index - 1]
            if leaf_child_value == -2:
                child_node_identity[parent_index] = -2
                continue
            if leaf_child_value == -1:
                if permutation_list[node_index] == node_index:
                    node_is_fixed[node_index] = True
                    continue
                leaf_nodes_dict[node_index] = node_index
                leaf_child_value = node_index
            else:
                leaf_nodes_dict[node_index] = leaf_child_value
            if child_node_identity[parent_index] == -1:
                child_node_identity[parent_index] = leaf_child_value
            else:
                child_node_identity[parent_index] = -2
    return leaf_nodes_dict

def perform_swap_to_place_node(target_position, target_value):
    swap_operations_buffer.append(target_position)
    node_positions[target_value] = target_position
    target_value, permutation_list[target_position] = permutation_list[target_position], target_value
    while target_position:
        parent_index = parent_list[target_position - 1]
        node_positions[target_value] = parent_index
        target_value, permutation_list[parent_index] = permutation_list[parent_index], target_value
        target_position = parent_index

def solve_permutation_with_tree_constraints():
    children_per_node = compute_children_from_parent_list(parent_list)
    node_levels_as_sets, node_to_level_map = generate_levels_and_level_map(children_per_node)
    while not node_is_fixed[0]:
        leaf_nodes_dict = identify_leaf_nodes(node_levels_as_sets)
        while leaf_nodes_dict:
            current_root_value = permutation_list[0]
            if current_root_value in leaf_nodes_dict:
                current_leaf_index = leaf_nodes_dict[current_root_value]
                while True:
                    candidate_value = permutation_list[current_leaf_index]
                    if not node_is_fixed[candidate_value] or candidate_value < current_root_value:
                        perform_swap_to_place_node(current_leaf_index, current_root_value)
                        node_is_fixed[current_root_value] = True
                        break
                    current_leaf_index = parent_list[current_leaf_index - 1]
                del leaf_nodes_dict[current_root_value]
            else:
                max_level, target_index = max(
                    (node_to_level_map[node_positions[node]], node_positions[node]) 
                    for node in leaf_nodes_dict
                )
                perform_swap_to_place_node(target_index, current_root_value)

number_of_nodes = int(input())
parent_list = list(map(int, input().split()))
permutation_list = list(map(int, input().split()))
node_positions = compute_node_positions_in_permutation(permutation_list)
node_is_fixed = [False] * number_of_nodes
swap_operations_buffer = []
solve_permutation_with_tree_constraints()
print(len(swap_operations_buffer))
print('\n'.join(map(str, swap_operations_buffer)))