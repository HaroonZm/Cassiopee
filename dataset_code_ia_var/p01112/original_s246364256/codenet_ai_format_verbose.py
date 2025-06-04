import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

def count_perfect_matchings(
    current_pairing_index,
    current_degree_list,
    total_pairs_to_form,
    matching_pair_candidates,
    memoization_dictionary
):
    degree_list_key = tuple(current_degree_list)

    if memoization_dictionary[(current_pairing_index, degree_list_key)] is not None:
        return memoization_dictionary[(current_pairing_index, degree_list_key)]

    if current_pairing_index == total_pairs_to_form:
        memoization_dictionary[(current_pairing_index, degree_list_key)] = 1
        for vertex_degree in current_degree_list:
            if vertex_degree > (number_of_vertices // 2):
                memoization_dictionary[(current_pairing_index, degree_list_key)] = 0
                return 0
        return 1
    else:
        total_valid_matchings = 0
        vertex_a, vertex_b = matching_pair_candidates[current_pairing_index]

        if current_degree_list[vertex_a] < (number_of_vertices // 2):
            current_degree_list[vertex_a] += 1
            total_valid_matchings += count_perfect_matchings(
                current_pairing_index + 1,
                current_degree_list,
                total_pairs_to_form,
                matching_pair_candidates,
                memoization_dictionary
            )
            current_degree_list[vertex_a] -= 1

        if current_degree_list[vertex_b] < (number_of_vertices // 2):
            current_degree_list[vertex_b] += 1
            total_valid_matchings += count_perfect_matchings(
                current_pairing_index + 1,
                current_degree_list,
                total_pairs_to_form,
                matching_pair_candidates,
                memoization_dictionary
            )
            current_degree_list[vertex_b] -= 1

        memoization_dictionary[(current_pairing_index, degree_list_key)] = total_valid_matchings
        return total_valid_matchings

def process_matching_problem(number_of_vertices):
    memoization_dictionary = defaultdict(lambda: None)

    number_of_removed_edges = int(sys.stdin.readline())
    current_degrees = [0] * number_of_vertices

    adjacency_matrix = [
        [1] * number_of_vertices
        for _ in range(number_of_vertices)
    ]
    for i in range(number_of_vertices):
        adjacency_matrix[i][i] = 0

    for _ in range(number_of_removed_edges):
        vertex_x, vertex_y = [int(token) for token in sys.stdin.readline().split()]
        vertex_x -= 1
        vertex_y -= 1
        current_degrees[vertex_x] += 1

        adjacency_matrix[vertex_x][vertex_y] = 0
        adjacency_matrix[vertex_y][vertex_x] = 0

    matching_pair_candidates = []
    for i in range(number_of_vertices):
        for j in range(i+1, number_of_vertices):
            if adjacency_matrix[i][j]:
                matching_pair_candidates.append((i, j))

    total_pairs_to_form = len(matching_pair_candidates)
    print(
        count_perfect_matchings(
            0,
            current_degrees,
            total_pairs_to_form,
            matching_pair_candidates,
            memoization_dictionary
        )
    )

while True:
    input_line = sys.stdin.readline()
    if not input_line:
        break
    number_of_vertices = int(input_line)
    if number_of_vertices == 0:
        break
    process_matching_problem(number_of_vertices)