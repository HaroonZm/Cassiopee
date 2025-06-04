import sys

sys.setrecursionlimit(10 ** 6)

def solve():
    read_line_from_input = sys.stdin.readline
    write_output = sys.stdout.write

    number_of_nodes, number_of_edges = map(int, read_line_from_input().split())
    node_weights = list(map(int, read_line_from_input().split()))

    adjacency_list = [[] for _ in range(number_of_nodes)]

    for _ in range(number_of_edges):
        node_u, node_v = map(int, read_line_from_input().split())
        adjacency_list[node_u - 1].append(node_v - 1)
        adjacency_list[node_v - 1].append(node_u - 1)

    visited_nodes = [0] * number_of_nodes
    has_back_edge = [0] * number_of_nodes
    max_subtree_weight = [0] * number_of_nodes
    marker_array = [0] * number_of_nodes

    visited_nodes[0] = 1
    stack = [0]
    neighbor_position_iterator = [0] * number_of_nodes

    while stack:
        current_node = stack[-1]
        parent_node = stack[-2] if len(stack) > 1 else -1

        if neighbor_position_iterator[current_node] == 0:
            visited_nodes[current_node] = 1
        else:
            previous_neighbor = adjacency_list[current_node][neighbor_position_iterator[current_node] - 1]
            max_subtree_weight[current_node] = max(max_subtree_weight[current_node], max_subtree_weight[previous_neighbor])
            if has_back_edge[previous_neighbor]:
                has_back_edge[current_node] = 1

        while neighbor_position_iterator[current_node] < len(adjacency_list[current_node]):
            neighbor = adjacency_list[current_node][neighbor_position_iterator[current_node]]
            neighbor_position_iterator[current_node] += 1
            if visited_nodes[neighbor]:
                if neighbor != parent_node:
                    has_back_edge[current_node] = 1
                continue
            visited_nodes[neighbor] = 1
            stack.append(neighbor)
            break
        else:
            max_subtree_weight[current_node] += node_weights[current_node]
            stack.pop()

    total_cyclic_weights = 0
    maximal_acyclic_path_weight = 0

    for node_index in range(number_of_nodes):
        if has_back_edge[node_index]:
            total_cyclic_weights += node_weights[node_index]
        else:
            maximal_acyclic_path_weight = max(maximal_acyclic_path_weight, max_subtree_weight[node_index])

    write_output("%d\n" % (total_cyclic_weights + maximal_acyclic_path_weight))

solve()