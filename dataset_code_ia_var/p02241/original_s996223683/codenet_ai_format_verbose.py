number_of_vertices = int(raw_input())

adjacency_matrix = []

for current_vertex_index in range(number_of_vertices):
    adjacency_matrix.append(map(int, raw_input().split()))

def compute_minimum_spanning_tree_weight(adjacency_matrix):

    vertex_colors = ['unvisited' for _ in range(number_of_vertices)]
    minimum_edge_weights = [float('inf') for _ in range(number_of_vertices)]
    parent_vertex_indices = [-1 for _ in range(number_of_vertices)]

    minimum_edge_weights[0] = 0

    while True:

        current_minimum_weight = float('inf')
        selected_vertex = -1

        for vertex_index in range(number_of_vertices):
            if vertex_colors[vertex_index] != 'included' and minimum_edge_weights[vertex_index] < current_minimum_weight:
                current_minimum_weight = minimum_edge_weights[vertex_index]
                selected_vertex = vertex_index

        if current_minimum_weight == float('inf'):
            break

        vertex_colors[selected_vertex] = 'included'

        for neighbor_index in range(number_of_vertices):
            if (vertex_colors[neighbor_index] != 'included' and 
                adjacency_matrix[selected_vertex][neighbor_index] != -1):

                if adjacency_matrix[selected_vertex][neighbor_index] < minimum_edge_weights[neighbor_index]:
                    minimum_edge_weights[neighbor_index] = adjacency_matrix[selected_vertex][neighbor_index]
                    parent_vertex_indices[neighbor_index] = selected_vertex
                    vertex_colors[neighbor_index] = 'candidate'

    print sum(minimum_edge_weights)

compute_minimum_spanning_tree_weight(adjacency_matrix)