import heapq

INFINITY_DISTANCE = 10 ** 10
COLOR_WHITE = 0
COLOR_GRAY = 1
COLOR_BLACK = 2

number_of_vertices = int(input())

adjacency_list = {}

for _ in range(number_of_vertices):
    vertex_id, number_of_neighbors, *neighbors_data = map(int, input().split())

    adjacency_list[str(vertex_id)] = {}

    for index in range(0, number_of_neighbors * 2, 2):
        neighbor_vertex_id = neighbors_data[index]
        edge_weight = neighbors_data[index + 1]
        adjacency_list[str(vertex_id)][str(neighbor_vertex_id)] = edge_weight

shortest_distances_from_start = [INFINITY_DISTANCE] * number_of_vertices

def dijkstra_algorithm(start_vertex_index):
    
    vertex_color_status = [COLOR_WHITE] * number_of_vertices

    shortest_distances_from_start[start_vertex_index] = 0

    min_heap_priority_queue = []
    heapq.heappush(min_heap_priority_queue, (shortest_distances_from_start[start_vertex_index], start_vertex_index))

    while len(min_heap_priority_queue) > 0:
        current_cost, current_vertex_index = heapq.heappop(min_heap_priority_queue)
        
        vertex_color_status[current_vertex_index] = COLOR_BLACK

        if shortest_distances_from_start[current_vertex_index] < current_cost:
            continue

        for neighbor_vertex_str in adjacency_list[str(current_vertex_index)].keys():
            neighbor_vertex_index = int(neighbor_vertex_str)

            if vertex_color_status[neighbor_vertex_index] == COLOR_BLACK:
                continue

            cost_to_neighbor = shortest_distances_from_start[current_vertex_index] + adjacency_list[str(current_vertex_index)][neighbor_vertex_str]

            if cost_to_neighbor < shortest_distances_from_start[neighbor_vertex_index]:
                shortest_distances_from_start[neighbor_vertex_index] = cost_to_neighbor
                vertex_color_status[neighbor_vertex_index] = COLOR_GRAY
                heapq.heappush(min_heap_priority_queue, (shortest_distances_from_start[neighbor_vertex_index], neighbor_vertex_index))

dijkstra_algorithm(start_vertex_index=0)

for vertex_index, distance in enumerate(shortest_distances_from_start):
    print(vertex_index, distance)