from math import isinf

def main():
    number_of_vertices, number_of_edges = map(int, input().split())

    shortest_distances = [
        [float('inf')] * number_of_vertices for _ in range(number_of_vertices)
    ]

    for vertex_index in range(number_of_vertices):
        shortest_distances[vertex_index][vertex_index] = 0

    for _ in range(number_of_edges):
        source_vertex, target_vertex, edge_weight = map(int, input().split())
        shortest_distances[source_vertex][target_vertex] = edge_weight

    for intermediate_vertex in range(number_of_vertices):
        for start_vertex in range(number_of_vertices):
            for end_vertex in range(number_of_vertices):
                if (
                    shortest_distances[start_vertex][end_vertex] >
                    shortest_distances[start_vertex][intermediate_vertex] +
                    shortest_distances[intermediate_vertex][end_vertex]
                ):
                    shortest_distances[start_vertex][end_vertex] = (
                        shortest_distances[start_vertex][intermediate_vertex] +
                        shortest_distances[intermediate_vertex][end_vertex]
                    )

    for vertex_index in range(number_of_vertices):
        if shortest_distances[vertex_index][vertex_index] < 0:
            print("NEGATIVE CYCLE")
            return

    for distance_row in shortest_distances:
        print(
            ' '.join(
                ('INF' if isinf(distance_value) else str(distance_value))
                for distance_value in distance_row
            )
        )

main()