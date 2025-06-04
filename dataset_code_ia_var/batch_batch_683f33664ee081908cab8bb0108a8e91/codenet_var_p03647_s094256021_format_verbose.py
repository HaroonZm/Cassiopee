def main():

    number_of_nodes, number_of_edges = map(int, input().split())

    has_direct_edge_from_node_1 = [False] * number_of_nodes

    has_direct_edge_to_node_n = [False] * number_of_nodes

    for edge_index in range(number_of_edges):

        start_node, end_node = map(int, input().split())

        start_node_index = start_node - 1
        end_node_index = end_node - 1

        if start_node == 1:
            has_direct_edge_from_node_1[end_node_index] = True

        if start_node == number_of_nodes:
            has_direct_edge_to_node_n[end_node_index] = True

        elif end_node == number_of_nodes:
            has_direct_edge_to_node_n[start_node_index] = True

    for node_index in range(number_of_nodes):

        if has_direct_edge_from_node_1[node_index] and has_direct_edge_to_node_n[node_index]:
            print("POSSIBLE")
            return

    print("IMPOSSIBLE")


main()