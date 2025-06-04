import heapq
from collections import deque

number_of_nodes, number_of_edges = map(int, input().split())

adjacency_matrix_weights = [
    [float("inf") for _ in range(number_of_nodes)]
    for _ in range(number_of_nodes)
]

shortest_path_usage = [
    [-float("inf") for _ in range(number_of_nodes)]
    for _ in range(number_of_nodes)
]

adjacency_list_neighbors = [[] for _ in range(number_of_nodes)]

for edge_index in range(number_of_edges):
    node_start, node_end, edge_weight = map(int, input().split())
    adjacency_matrix_weights[node_start - 1][node_end - 1] = edge_weight
    adjacency_matrix_weights[node_end - 1][node_start - 1] = edge_weight
    adjacency_list_neighbors[node_start - 1].append(node_end - 1)
    adjacency_list_neighbors[node_end - 1].append(node_start - 1)
    shortest_path_usage[node_start - 1][node_end - 1] = 0
    shortest_path_usage[node_end - 1][node_start - 1] = 0

for diagonal_index in range(number_of_nodes):
    adjacency_matrix_weights[diagonal_index][diagonal_index] = 0

for source_node in range(number_of_nodes):

    shortest_distances = [float("inf") for _ in range(number_of_nodes)]
    shortest_distances[source_node] = 0

    priority_queue = []
    previous_node = [-1] * number_of_nodes

    priority_queue.append([0, source_node])
    heapq.heapify(priority_queue)

    while len(priority_queue) > 0:
        current_distance, current_node = heapq.heappop(priority_queue)

        if shortest_distances[current_node] < current_distance:
            continue

        predecessor = previous_node[current_node]
        path_node = current_node

        while predecessor != -1:
            shortest_path_usage[predecessor][path_node] = 1
            shortest_path_usage[path_node][predecessor] = 1
            path_node = predecessor
            predecessor = previous_node[predecessor]

        for neighbor in adjacency_list_neighbors[current_node]:
            distance_through_current = shortest_distances[current_node] + adjacency_matrix_weights[current_node][neighbor]
            if shortest_distances[neighbor] > distance_through_current:
                shortest_distances[neighbor] = distance_through_current
                heapq.heappush(priority_queue, [distance_through_current, neighbor])
                previous_node[neighbor] = current_node

number_of_unused_edges = 0

for first_node in range(number_of_nodes):
    for second_node in range(number_of_nodes):
        if shortest_path_usage[first_node][second_node] == 0:
            number_of_unused_edges += 1

print(number_of_unused_edges // 2)