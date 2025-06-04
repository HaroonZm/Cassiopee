from collections import deque

def build_children_list(parent_indices_list):
    children_sets_per_node = [set() for _ in range(number_of_nodes)]
    for child_index, parent_index in enumerate(parent_indices_list):
        children_sets_per_node[parent_index].add(child_index + 1)
    return children_sets_per_node

def build_tree_levels(children_sets_per_node):
    nodes_per_level = []
    traversal_queue = deque([(0, 0)])  # (node_index, level_number)
    while traversal_queue:
        current_node_index, current_level = traversal_queue.popleft()
        if nodes_already_fixed[current_node_index]:
            continue
        if len(nodes_per_level) <= current_level:
            nodes_per_level.append(set())
        nodes_per_level[current_level].add(current_node_index)
        for child_index in children_sets_per_node[current_node_index]:
            traversal_queue.append((child_index, current_level + 1))
    return nodes_per_level

def build_value_to_position_mapping():
    node_index_for_value = [0] * number_of_nodes
    for position_index, node_value in enumerate(current_node_values):
        node_index_for_value[node_value] = position_index
    return node_index_for_value

def collect_leaf_nodes_per_level(nodes_per_level):
    leaf_nodes = {}
    last_unified_child_per_node = [-1] * number_of_nodes
    for level_index, node_indices_at_level in reversed(list(enumerate(nodes_per_level))):
        for node_index in node_indices_at_level:
            unified_child_index = last_unified_child_per_node[node_index]
            parent_index_of_node = parent_indices_list[node_index - 1]
            if unified_child_index == -1:
                if current_node_values[node_index] == node_index:
                    nodes_already_fixed[node_index] = True
                    continue
                else:
                    leaf_nodes[node_index] = node_index
                if last_unified_child_per_node[parent_index_of_node] == -1:
                    last_unified_child_per_node[parent_index_of_node] = node_index
                else:
                    last_unified_child_per_node[parent_index_of_node] = -2
            elif unified_child_index == -2:
                last_unified_child_per_node[parent_index_of_node] = -2
            else:
                leaf_nodes[node_index] = unified_child_index
                if last_unified_child_per_node[parent_index_of_node] == -1:
                    last_unified_child_per_node[parent_index_of_node] = unified_child_index
                else:
                    last_unified_child_per_node[parent_index_of_node] = -2
    return leaf_nodes

def move_value_to_position(destination_index, source_value, node_index_for_value):
    solution_moves.append(destination_index)
    node_index_for_value[source_value] = destination_index
    source_value, current_node_values[destination_index] = current_node_values[destination_index], source_value
    while destination_index:
        parent_node_index = parent_indices_list[destination_index - 1]
        node_index_for_value[source_value] = parent_node_index
        source_value, current_node_values[parent_node_index] = current_node_values[parent_node_index], source_value
        destination_index = parent_node_index

def main_solver():
    children_sets_per_node = build_children_list(parent_indices_list)
    while not nodes_already_fixed[0]:
        nodes_per_level = build_tree_levels(children_sets_per_node)
        leaf_nodes = collect_leaf_nodes_per_level(nodes_per_level)
        node_index_for_value = build_value_to_position_mapping()
        while leaf_nodes:
            value_at_root = current_node_values[0]
            if value_at_root in leaf_nodes:
                leaf_node_index = leaf_nodes[value_at_root]
                while True:
                    current_value_at_leaf = current_node_values[leaf_node_index]
                    if not nodes_already_fixed[current_value_at_leaf] or current_value_at_leaf < value_at_root:
                        move_value_to_position(leaf_node_index, value_at_root, node_index_for_value)
                        nodes_already_fixed[value_at_root] = True
                        break
                    leaf_node_index = parent_indices_list[leaf_node_index - 1]
                del leaf_nodes[value_at_root]
            else:
                max_position_of_remaining_leaf = max(
                    node_index_for_value[leaf_value]
                    for leaf_value in leaf_nodes
                    if not nodes_already_fixed[leaf_value]
                )
                move_value_to_position(max_position_of_remaining_leaf, value_at_root, node_index_for_value)

number_of_nodes = int(input())
parent_indices_list = list(map(int, input().split()))
current_node_values = list(map(int, input().split()))
nodes_already_fixed = [False] * number_of_nodes
solution_moves = []
main_solver()
print(len(solution_moves))
print('\n'.join(map(str, solution_moves)))