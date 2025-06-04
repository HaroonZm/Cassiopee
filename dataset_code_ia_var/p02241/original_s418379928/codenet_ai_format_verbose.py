INFINITY_COST = 1 << 21

COLOR_UNVISITED = 0
COLOR_IN_PROCESS = 1
COLOR_VISITED = 2

number_of_vertices = int(input())

adjacency_matrix = [
    list(map(int, input().split()))
    for current_row_index in range(number_of_vertices)
]

minimum_edge_cost = [
    INFINITY_COST
    for vertex_index in range(number_of_vertices)
]

parent_vertex = [
    -1
    for vertex_index in range(number_of_vertices)
]

vertex_color = [
    COLOR_UNVISITED
    for vertex_index in range(number_of_vertices)
]

for source_vertex in range(number_of_vertices):
    for destination_vertex in range(number_of_vertices):
        if adjacency_matrix[source_vertex][destination_vertex] == -1:
            adjacency_matrix[source_vertex][destination_vertex] = INFINITY_COST

def calculate_minimum_spanning_tree_total_cost():
    global adjacency_matrix, minimum_edge_cost, parent_vertex, vertex_color

    minimum_edge_cost[0] = 0

    while True:
        current_minimum_cost = INFINITY_COST
        selected_vertex = -1

        for scan_vertex in range(number_of_vertices):
            if (
                current_minimum_cost > minimum_edge_cost[scan_vertex]
                and vertex_color[scan_vertex] != COLOR_VISITED
            ):
                selected_vertex = scan_vertex
                current_minimum_cost = minimum_edge_cost[scan_vertex]

        if selected_vertex == -1:
            break

        vertex_color[selected_vertex] = COLOR_VISITED

        for adjacent_vertex in range(number_of_vertices):
            if (
                vertex_color[adjacent_vertex] != COLOR_VISITED
                and adjacency_matrix[selected_vertex][adjacent_vertex] != INFINITY_COST
            ):
                if minimum_edge_cost[adjacent_vertex] > adjacency_matrix[selected_vertex][adjacent_vertex]:
                    minimum_edge_cost[adjacent_vertex] = adjacency_matrix[selected_vertex][adjacent_vertex]
                    parent_vertex[adjacent_vertex] = selected_vertex
                    vertex_color[adjacent_vertex] = COLOR_IN_PROCESS

    total_cost = sum(
        adjacency_matrix[vertex_index][parent_vertex[vertex_index]]
        for vertex_index in range(number_of_vertices)
        if parent_vertex[vertex_index] != -1
    )

    return total_cost

print(calculate_minimum_spanning_tree_total_cost())