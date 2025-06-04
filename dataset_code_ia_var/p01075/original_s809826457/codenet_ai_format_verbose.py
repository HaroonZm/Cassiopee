import heapq

INFINITE_DISTANCE = 0x7fffffff

def dijkstra_algorithm(
    total_vertices,
    adjacency_list,
    start_vertex
):
    minimum_distance_to_vertex = [INFINITE_DISTANCE] * total_vertices

    vertex_priority_queue = []

    minimum_distance_to_vertex[start_vertex] = 0

    heapq.heappush(vertex_priority_queue, (0, start_vertex))

    while vertex_priority_queue:

        current_cost, current_vertex = heapq.heappop(vertex_priority_queue)

        if minimum_distance_to_vertex[current_vertex] < current_cost:
            continue

        for neighbor_vertex, edge_cost in adjacency_list[current_vertex]:

            if (
                current_cost <= edge_cost
                and edge_cost < minimum_distance_to_vertex[neighbor_vertex]
            ):
                minimum_distance_to_vertex[neighbor_vertex] = edge_cost
                heapq.heappush(
                    vertex_priority_queue,
                    (edge_cost, neighbor_vertex)
                )

    return minimum_distance_to_vertex


number_of_vertices, number_of_edges = map(int, input().split())

last_vertex_index = number_of_vertices - 1

edges_leading_to_last_vertex = []

vertex_adjacency_list = [
    []
    for _ in range(number_of_vertices)
]

for _ in range(number_of_edges):

    origin_vertex, target_vertex, edge_weight = map(int, input().split())
    origin_vertex -= 1
    target_vertex -= 1

    vertex_adjacency_list[origin_vertex].append(
        (target_vertex, edge_weight)
    )

    if target_vertex == last_vertex_index:
        edges_leading_to_last_vertex.append(
            (origin_vertex, edge_weight)
        )


minimum_distances_from_source = dijkstra_algorithm(
    number_of_vertices,
    vertex_adjacency_list,
    start_vertex=0
)

if minimum_distances_from_source[last_vertex_index] >= INFINITE_DISTANCE:
    print(-1)
else:
    edges_leading_to_last_vertex.sort(
        key=lambda edge: -edge[1]
    )
    for adjacent_vertex, edge_weight in edges_leading_to_last_vertex:
        if minimum_distances_from_source[adjacent_vertex] <= edge_weight:
            print(edge_weight)
            break