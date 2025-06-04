import sys
import json
import itertools

VERY_LARGE_NUMBER = 100000000

def parse_input_as_graph_and_preferences(input_string):
    INFINITY_PLACEHOLDER = VERY_LARGE_NUMBER

    first_linebreak_index = input_string.index('\n')
    number_of_nodes = int(input_string[:first_linebreak_index])

    favorite_pattern_list = [
        int(character) * INFINITY_PLACEHOLDER
        for character in input_string[-number_of_nodes - 1:-1]
    ]

    serialized_edges = "[" + input_string[
        first_linebreak_index + 1:-number_of_nodes - 2
    ].replace(" ", ",").replace("\n", ",") + "]"
    edge_nodes = json.loads(serialized_edges)

    adjacency_list_graph = [[] for _ in range(number_of_nodes)]
    adjacency_list_graph[0].append(None)
    for edge_index in range(0, (number_of_nodes - 1) * 2, 2):
        node_a = edge_nodes[edge_index] - 1
        node_b = edge_nodes[edge_index + 1] - 1
        adjacency_list_graph[node_a].append(node_b)
        adjacency_list_graph[node_b].append(node_a)

    return (number_of_nodes, favorite_pattern_list, adjacency_list_graph)

def compute_adjusted_tree_distance():
    INFINITY_CONST = VERY_LARGE_NUMBER

    (
        number_of_nodes,
        favorite_nodes_count,
        adjacency_graph
    ) = parse_input_as_graph_and_preferences(sys.stdin.read())

    max_child_height = [0] * number_of_nodes
    second_max_child_height = [0] * number_of_nodes
    traversal_order_for_dfs = []

    current_dfs_stack = [None, 0, 0]
    while True:
        current_node_in_traversal = current_dfs_stack[-1]
        current_child_index = current_dfs_stack[-2]
        if current_child_index < len(adjacency_graph[current_node_in_traversal]):
            child_node = adjacency_graph[current_node_in_traversal][current_child_index]
            current_dfs_stack[-2] += 1
            if child_node != current_dfs_stack[-3]:
                current_dfs_stack.extend((0, child_node))
                traversal_order_for_dfs.append(child_node)
            else:
                adjacency_graph[current_node_in_traversal][0], adjacency_graph[current_node_in_traversal][current_child_index] = (
                    child_node,
                    adjacency_graph[current_node_in_traversal][0],
                )
        else:
            del current_dfs_stack[-2:]
            if len(current_dfs_stack) <= 1:
                break
            parent_node = current_dfs_stack[-1]
            computed_child_height = max_child_height[current_node_in_traversal] + 1
            if computed_child_height >= max_child_height[parent_node]:
                max_child_height[parent_node], second_max_child_height[parent_node] = (
                    computed_child_height,
                    max_child_height[parent_node],
                )
            elif computed_child_height > second_max_child_height[parent_node]:
                second_max_child_height[parent_node] = computed_child_height
            if favorite_nodes_count[current_node_in_traversal] != 0:
                favorite_nodes_count[parent_node] += 1

    final_result = 0
    if favorite_nodes_count[0] >= INFINITY_CONST:
        minimum_bound = -1
    else:
        minimum_bound = min(
            (
                max_child_height[descendant_node]
                for descendant_node in adjacency_graph[0][1:]
                if favorite_nodes_count[descendant_node] != 0
            ),
            default=INFINITY_CONST,
        )
    maximum_bound = second_max_child_height[0]
    if maximum_bound > minimum_bound:
        final_result += maximum_bound - minimum_bound

    for traversal_node in traversal_order_for_dfs:
        parent_of_node = adjacency_graph[traversal_node][0]
        has_favorite_nodes_in_subtree = favorite_nodes_count[traversal_node] != 0
        has_favorite_nodes_above = favorite_nodes_count[parent_of_node] > has_favorite_nodes_in_subtree
        favorite_nodes_count[traversal_node] += has_favorite_nodes_above

        node_max_height = max_child_height[traversal_node]
        if node_max_height + 1 == max_child_height[parent_of_node]:
            minimum_bound = second_max_child_height[parent_of_node]
            if minimum_bound <= node_max_height and has_favorite_nodes_above:
                final_result += 1
            elif minimum_bound >= node_max_height and has_favorite_nodes_in_subtree:
                final_result += 1

            parent_new_height = minimum_bound + 1
            if parent_new_height >= node_max_height:
                max_child_height[traversal_node], second_max_child_height[traversal_node] = parent_new_height, node_max_height
            elif parent_new_height > second_max_child_height[traversal_node]:
                second_max_child_height[traversal_node] = parent_new_height
        else:
            final_result += has_favorite_nodes_in_subtree
            minimum_bound = max_child_height[parent_of_node]
            max_child_height[traversal_node], second_max_child_height[traversal_node] = (
                minimum_bound + 1,
                node_max_height,
            )
        if favorite_nodes_count[traversal_node] >= INFINITY_CONST:
            minimum_bound = -1
        else:
            if not has_favorite_nodes_above:
                minimum_bound = INFINITY_CONST
            for descendant_node in itertools.islice(adjacency_graph[traversal_node], 1, None):
                if favorite_nodes_count[descendant_node] != 0:
                    minimum_bound = min(max_child_height[descendant_node], minimum_bound)
        maximum_bound = second_max_child_height[traversal_node]
        if maximum_bound > minimum_bound:
            final_result += maximum_bound - minimum_bound

    print(final_result)

compute_adjusted_tree_distance()