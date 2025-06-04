import heapq

def dijkstra_algorithm(start_node, adjacency_list, total_nodes):
    VISITED = 2
    UNVISITED = 0
    IN_QUEUE = 1

    node_status = [UNVISITED] * total_nodes
    shortest_distances = {}

    for node_index in range(total_nodes):
        shortest_distances[node_index] = float('inf')
    shortest_distances[start_node] = 0

    min_heap = []
    heapq.heappush(min_heap, [0, start_node])

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        node_status[current_node] = VISITED

        if shortest_distances[current_node] < current_distance:
            continue

        for neighbor_node, edge_cost in adjacency_list[current_node]:
            if node_status[neighbor_node] != VISITED:
                if shortest_distances[current_node] + edge_cost < shortest_distances[neighbor_node]:
                    shortest_distances[neighbor_node] = shortest_distances[current_node] + edge_cost
                    node_status[neighbor_node] = IN_QUEUE
                    heapq.heappush(min_heap, [shortest_distances[neighbor_node], neighbor_node])

    return shortest_distances

number_of_nodes, number_of_edges, constant_c = map(int, raw_input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]
sum_of_all_edge_costs = 0

for edge_iteration in range(number_of_edges):
    node_u, node_v, edge_weight = map(int, raw_input().split())
    adjacency_list[node_u - 1].append([node_v - 1, edge_weight])
    adjacency_list[node_v - 1].append([node_u - 1, edge_weight])
    sum_of_all_edge_costs += edge_weight

shortest_distances_from_source = dijkstra_algorithm(0, adjacency_list, number_of_nodes)
sorted_nodes_by_distance = sorted(shortest_distances_from_source.items(), key=lambda distance_pair: distance_pair[1])

minimum_total_cost = float('inf')
node_has_been_visited = [0] * number_of_nodes

for node_index, distance_from_source in sorted_nodes_by_distance:
    node_has_been_visited[node_index] = 1
    for neighbor_index, edge_cost in adjacency_list[node_index]:
        if node_has_been_visited[neighbor_index] == 1:
            sum_of_all_edge_costs -= edge_cost
    calculated_cost = sum_of_all_edge_costs + constant_c * distance_from_source
    minimum_total_cost = min(minimum_total_cost, calculated_cost)

print minimum_total_cost