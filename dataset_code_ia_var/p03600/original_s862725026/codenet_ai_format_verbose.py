def floyd_warshall_algorithm(adjacency_matrix):
    number_of_vertices = len(adjacency_matrix)

    for intermediate_vertex in range(number_of_vertices):

        for source_vertex in range(number_of_vertices):

            for destination_vertex in range(number_of_vertices):

                if adjacency_matrix[source_vertex][destination_vertex] > adjacency_matrix[source_vertex][intermediate_vertex] + adjacency_matrix[intermediate_vertex][destination_vertex]:

                    adjacency_matrix[source_vertex][destination_vertex] = adjacency_matrix[source_vertex][intermediate_vertex] + adjacency_matrix[intermediate_vertex][destination_vertex]

    return adjacency_matrix


number_of_nodes = int(input())

distance_matrix = [
    [float("inf") for _ in range(number_of_nodes)]
    for _ in range(number_of_nodes)
]

for row_index in range(number_of_nodes):

    input_distances = list(map(int, input().split()))

    for column_index in range(number_of_nodes):

        if row_index == column_index:
            continue

        distance_matrix[row_index][column_index] = input_distances[column_index]


import numpy as np
from scipy.sparse.csgraph import floyd_warshall

shortest_path_matrix = floyd_warshall(distance_matrix, directed=False)

total_minimum_distance = 0

for diagonal_index in range(number_of_nodes):

    shortest_path_matrix[diagonal_index][diagonal_index] = float("inf")


for row in range(number_of_nodes):

    for column in range(row):

        if row == column:
            continue

        if shortest_path_matrix[row][column] != distance_matrix[row][column]:
            print(-1)
            exit()

        if shortest_path_matrix[row][column] < np.min(
            np.append(shortest_path_matrix[row], shortest_path_matrix[column])
        ):
            total_minimum_distance += shortest_path_matrix[row][column]

print(int(total_minimum_distance))