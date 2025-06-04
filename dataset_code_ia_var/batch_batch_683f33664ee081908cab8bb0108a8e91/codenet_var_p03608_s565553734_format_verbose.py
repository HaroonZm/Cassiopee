import itertools
import sys

def main(command_line_arguments):

    input_line = sys.stdin.readline()

    while input_line:

        total_number_of_vertices, total_number_of_edges, total_number_of_required_vertices = map(int, input_line.split(" ", 3))

        required_vertices_list = list(map(lambda vertex: int(vertex) - 1, sys.stdin.readline().split(" ")))

        adjacency_matrix_weights = [
            [0 for column_index in range(total_number_of_vertices)]
            for row_index in range(total_number_of_vertices)
        ]

        for edge_index in range(total_number_of_edges):

            vertex_a, vertex_b, edge_weight = map(int, sys.stdin.readline().split(" ", 3))

            adjacency_matrix_weights[vertex_a - 1][vertex_b - 1] = edge_weight
            adjacency_matrix_weights[vertex_b - 1][vertex_a - 1] = edge_weight

        for intermediate_vertex in range(total_number_of_vertices):
            for start_vertex in range(total_number_of_vertices):
                for end_vertex in range(total_number_of_vertices):
                    if end_vertex > start_vertex:
                        if (
                            adjacency_matrix_weights[start_vertex][intermediate_vertex] > 0 and
                            adjacency_matrix_weights[intermediate_vertex][end_vertex] > 0
                        ):
                            path_length = (
                                adjacency_matrix_weights[start_vertex][intermediate_vertex] +
                                adjacency_matrix_weights[intermediate_vertex][end_vertex]
                            )
                            if (
                                adjacency_matrix_weights[start_vertex][end_vertex] == 0 or
                                adjacency_matrix_weights[start_vertex][end_vertex] > path_length
                            ):
                                adjacency_matrix_weights[start_vertex][end_vertex] = path_length
                                adjacency_matrix_weights[end_vertex][start_vertex] = path_length

        minimal_total_path_length = -1

        for current_permutation_of_required_vertices in itertools.permutations(required_vertices_list):

            current_path_length = 0
            previous_vertex = current_permutation_of_required_vertices[0]

            for current_vertex in current_permutation_of_required_vertices[1:]:
                current_path_length += adjacency_matrix_weights[previous_vertex][current_vertex]
                previous_vertex = current_vertex

            if minimal_total_path_length == -1:
                minimal_total_path_length = current_path_length
            elif minimal_total_path_length > current_path_length:
                minimal_total_path_length = current_path_length

        print(minimal_total_path_length)

        input_line = sys.stdin.readline()

if __name__ == "__main__":
    main(sys.argv)