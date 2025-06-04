import sys

input_stream = sys.stdin.readline
output_stream = sys.stdout.write

sys.setrecursionlimit(100000)

def solve():

    number_of_nodes, max_elements_to_sum = map(int, input_stream().split())

    adjacency_list = [[] for _ in range(number_of_nodes)]

    for edge_index in range(number_of_nodes - 1):

        start_node, end_node, edge_weight = map(int, input_stream().split())

        adjacency_list[start_node - 1].append((end_node - 1, edge_weight))
        adjacency_list[end_node - 1].append((start_node - 1, edge_weight))

    node_coefficients = list(map(int, input_stream().split()))

    def depth_first_search(
        current_node, parent_node, coefficient, result_values_list
    ):

        maximal_sum_from_subtree = 0

        for neighbor_node, connecting_edge_weight in adjacency_list[current_node]:

            if neighbor_node == parent_node:
                continue

            subtree_sum = (
                depth_first_search(
                    neighbor_node, current_node, coefficient, result_values_list
                )
                + coefficient * connecting_edge_weight
            )

            if maximal_sum_from_subtree < subtree_sum:
                maximal_sum_from_subtree, subtree_sum = subtree_sum, maximal_sum_from_subtree

            if subtree_sum > 0:
                result_values_list.append(subtree_sum)

        return maximal_sum_from_subtree

    collected_values = []

    for node_index in range(number_of_nodes):

        dfs_return_value = depth_first_search(
            node_index, -1, node_coefficients[node_index], collected_values
        )

        if dfs_return_value > 0:
            collected_values.append(dfs_return_value)

    collected_values.sort(reverse=True)

    total_sum_of_top_elements = sum(collected_values[:max_elements_to_sum])

    output_stream(f"{total_sum_of_top_elements}\n")

solve()