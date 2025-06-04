import sys
from heapq import heappop, heappush

INFINITE_DISTANCE = 10 ** 10

number_of_vertices = int(input())

adjacency_list = []

for _ in range(number_of_vertices):
    input_line_tokens = sys.stdin.readline().split()
    vertex_edges = [
        input_line_tokens[i:i + 2] for i in range(2, len(input_line_tokens), 2)
    ]
    adjacency_list.append(vertex_edges)

def dijkstra_shortest_paths():
    visited_vertices = [False] * number_of_vertices
    shortest_distances = [INFINITE_DISTANCE] * number_of_vertices
    previous_vertex = [None] * number_of_vertices

    priority_queue = []
    heappush(priority_queue, (0, 0))
    shortest_distances[0] = 0

    while len(priority_queue) > 0:
        current_distance, current_vertex_index = heappop(priority_queue)
        if visited_vertices[current_vertex_index]:
            continue

        visited_vertices[current_vertex_index] = True

        for edge in adjacency_list[current_vertex_index]:
            neighbor_vertex_index, edge_weight = [int(value) for value in edge]
            if visited_vertices[neighbor_vertex_index]:
                continue

            distance_through_current = current_distance + edge_weight

            if distance_through_current < shortest_distances[neighbor_vertex_index]:
                shortest_distances[neighbor_vertex_index] = distance_through_current
                previous_vertex[neighbor_vertex_index] = current_vertex_index
                heappush(priority_queue, (distance_through_current, neighbor_vertex_index))

    return shortest_distances

shortest_distances_from_source = dijkstra_shortest_paths()

for vertex_index in range(number_of_vertices):
    print(vertex_index, shortest_distances_from_source[vertex_index])