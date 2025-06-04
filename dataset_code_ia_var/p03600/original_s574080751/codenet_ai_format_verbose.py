number_of_nodes = int(input())

INFINITY_COST = float("inf")

graph_cost_matrix = [ [ INFINITY_COST ] * number_of_nodes for _ in range(number_of_nodes) ]

total_minimum_cost = 0

for source_node_index in range(number_of_nodes):

    input_costs = map(int, input().split())

    for destination_node_index, edge_cost in enumerate(input_costs):

        if source_node_index != destination_node_index:

            graph_cost_matrix[source_node_index][destination_node_index] = edge_cost

for source_node_index in range(number_of_nodes):

    for destination_node_index in range(source_node_index):

        minimum_alternative_cost = min(
            cost_from_source + cost_from_destination
            for cost_from_source, cost_from_destination in zip(
                graph_cost_matrix[source_node_index],
                graph_cost_matrix[destination_node_index]
            )
        )

        direct_edge_cost = graph_cost_matrix[source_node_index][destination_node_index]

        if direct_edge_cost > minimum_alternative_cost:

            print(-1)

            exit()

        if direct_edge_cost < minimum_alternative_cost:

            total_minimum_cost += direct_edge_cost

print(total_minimum_cost)