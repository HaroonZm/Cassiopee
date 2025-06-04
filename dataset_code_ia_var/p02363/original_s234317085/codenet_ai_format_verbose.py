infinite_distance = float('inf')

number_of_vertices, number_of_edges = map(int, input().split())

distance_matrix = [
    [infinite_distance for column_index in range(number_of_vertices)]
    for row_index in range(number_of_vertices)
]

for vertex_index in range(number_of_vertices):
    distance_matrix[vertex_index][vertex_index] = 0

for edge_input_index in range(number_of_edges):
    source_vertex, target_vertex, edge_weight = map(int, input().split())
    distance_matrix[source_vertex][target_vertex] = edge_weight

for intermediate_vertex in range(number_of_vertices):
    for start_vertex in range(number_of_vertices):
        for end_vertex in range(number_of_vertices):
            current_distance = distance_matrix[start_vertex][end_vertex]
            possible_shorter_path = (
                distance_matrix[start_vertex][intermediate_vertex]
                + distance_matrix[intermediate_vertex][end_vertex]
            )
            distance_matrix[start_vertex][end_vertex] = min(current_distance, possible_shorter_path)

contains_negative_cycle = False

for vertex_index in range(number_of_vertices):
    if distance_matrix[vertex_index][vertex_index] < 0:
        contains_negative_cycle = True

for row_index in range(number_of_vertices):
    for column_index in range(number_of_vertices):
        if distance_matrix[row_index][column_index] == infinite_distance:
            distance_matrix[row_index][column_index] = 'INF'
        else:
            distance_matrix[row_index][column_index] = str(distance_matrix[row_index][column_index])

if contains_negative_cycle:
    print('NEGATIVE CYCLE')
else:
    for formatted_row in distance_matrix:
        print(' '.join(formatted_row))