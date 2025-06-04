import copy

INFINITY_VALUE = float("inf")

def compute_all_pairs_shortest_paths(distance_matrix):
    vertex_count = len(distance_matrix)
    shortest_paths = copy.deepcopy(distance_matrix)
    for intermediate_vertex in range(vertex_count):
        for start_vertex in range(vertex_count):
            for end_vertex in range(vertex_count):
                shortest_paths[start_vertex][end_vertex] = min(
                    shortest_paths[start_vertex][end_vertex],
                    shortest_paths[start_vertex][intermediate_vertex] + shortest_paths[intermediate_vertex][end_vertex]
                )
    return shortest_paths

def main():
    vertex_count = int(input())
    input_distance_matrix = [
        list(map(int, input().split()))
        for _ in range(vertex_count)
    ]

    shortest_paths_matrix = compute_all_pairs_shortest_paths(input_distance_matrix)

    if input_distance_matrix != shortest_paths_matrix:
        print(-1)
        return

    total_minimal_edge_sum = 0
    for source_vertex in range(vertex_count):
        for destination_vertex in range(source_vertex + 1, vertex_count):
            if source_vertex == destination_vertex:
                continue

            total_minimal_edge_sum += input_distance_matrix[source_vertex][destination_vertex]
            for intermediate_vertex in range(vertex_count):
                if intermediate_vertex in (source_vertex, destination_vertex):
                    continue
                if input_distance_matrix[source_vertex][intermediate_vertex] + input_distance_matrix[intermediate_vertex][destination_vertex] == input_distance_matrix[source_vertex][destination_vertex]:
                    total_minimal_edge_sum -= input_distance_matrix[source_vertex][destination_vertex]
                    break

    print(total_minimal_edge_sum)

if __name__ == "__main__":
    main()