import sys

input_stream = sys.stdin.readline

number_of_nodes, maximum_depth = map(int, input_stream().split())

parent_indices = [int(input_stream()) - 1 for _ in range(number_of_nodes)]

initial_unassigned_count = parent_indices.count(-1)

repeated_parent_nodes = set()
add_to_repeated_parent_nodes = repeated_parent_nodes.add

observed_parent_nodes = set()
add_to_observed_parent_nodes = observed_parent_nodes.add

for current_index in range(number_of_nodes):
    parent_index = parent_indices[current_index]
    if parent_index in observed_parent_nodes:
        add_to_repeated_parent_nodes(parent_index)
    add_to_observed_parent_nodes(parent_index)

visited_nodes = set()
add_to_visited_nodes = visited_nodes.add

# Nodes with parents who are never used as children (potential roots)
potential_start_nodes = {node_index: maximum_depth - 1
                         for node_index in {i for i in range(number_of_nodes) if parent_indices[i] > -1} - set(parent_indices)}

total_reachable_nodes = initial_unassigned_count

while potential_start_nodes:
    next_nodes_to_explore = dict()
    for current_node, remaining_depth in potential_start_nodes.items():
        total_reachable_nodes += (current_node not in visited_nodes)
        add_to_visited_nodes(current_node)
        next_node = parent_indices[current_node]
        while (
            parent_indices[next_node] > -1 and
            next_node not in repeated_parent_nodes and
            remaining_depth > 0
        ):
            if next_node not in visited_nodes:
                total_reachable_nodes += 1
                add_to_visited_nodes(next_node)
            remaining_depth -= 1
            next_node = parent_indices[next_node]
        if (
            parent_indices[next_node] > -1 and
            next_node in repeated_parent_nodes and
            remaining_depth > 0
        ):
            next_nodes_to_explore[next_node] = max(
                next_nodes_to_explore.get(next_node, 0),
                remaining_depth - 1
            )
    potential_start_nodes = next_nodes_to_explore

print(total_reachable_nodes)