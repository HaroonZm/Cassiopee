from heapq import heappop, heappush

INFINITY = float("inf")

def dijkstra_shortest_paths():
    number_of_nodes = int(input())
    adjacency_list = []

    for _ in range(number_of_nodes):
        node_data = list(map(int, input().split()))
        neighbors = list(zip(node_data[2::2], node_data[3::2]))
        adjacency_list.append(neighbors)

    shortest_distances = [0] + [INFINITY] * (number_of_nodes - 1)

    priority_queue = [(0, 0)]  # Each entry is a tuple (distance_from_start, node_index)

    while priority_queue:
        current_distance, current_node = heappop(priority_queue)

        for neighbor_node_index, edge_weight in adjacency_list[current_node]:
            candidate_distance = shortest_distances[current_node] + edge_weight

            if shortest_distances[neighbor_node_index] > candidate_distance:
                shortest_distances[neighbor_node_index] = candidate_distance
                heappush(priority_queue, (candidate_distance, neighbor_node_index))

    output_lines = [f'{node_index} {shortest_distances[node_index]}' for node_index in range(number_of_nodes)]
    print('\n'.join(output_lines))

dijkstra_shortest_paths()