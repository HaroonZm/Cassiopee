import sys
import collections

# Lecture du nombre de sommets et d'arêtes depuis l'entrée standard
number_of_vertices, number_of_edges = tuple(map(int, sys.stdin.readline().split()))

INFINITY = float("inf")
set_of_all_vertices = set(range(number_of_vertices))

# Initialisation de la matrice des distances avec l'infini,
# Distance de chaque sommet à lui-même fixée à zéro
shortest_distances = [
    [INFINITY for _ in range(number_of_vertices)]
    for _ in range(number_of_vertices)
]
for vertex_index in range(number_of_vertices):
    shortest_distances[vertex_index][vertex_index] = 0

# Lecture et ajout des arêtes pondérées à la matrice des distances
for _ in range(number_of_edges):
    source_vertex, destination_vertex, edge_weight = map(
        int, sys.stdin.readline().rstrip().split()
    )
    shortest_distances[source_vertex][destination_vertex] = edge_weight

def floyd_warshall_algorithm():
    for intermediate_vertex in range(number_of_vertices):
        for start_vertex in range(number_of_vertices):
            for end_vertex in range(number_of_vertices):
                if (
                    shortest_distances[start_vertex][intermediate_vertex] != INFINITY
                    and shortest_distances[intermediate_vertex][end_vertex] != INFINITY
                ):
                    shortest_distances[start_vertex][end_vertex] = min(
                        shortest_distances[start_vertex][end_vertex],
                        shortest_distances[start_vertex][intermediate_vertex]
                        + shortest_distances[intermediate_vertex][end_vertex]
                    )

floyd_warshall_algorithm()

# Détection de cycle négatif
for vertex_index in range(number_of_vertices):
    if shortest_distances[vertex_index][vertex_index] < 0:
        print("NEGATIVE CYCLE")
        exit()

# Affichage des distances résultantes
for start_vertex in range(number_of_vertices):
    output_row = []
    for end_vertex in range(number_of_vertices):
        if shortest_distances[start_vertex][end_vertex] == INFINITY:
            output_row.append("INF")
        else:
            output_row.append(str(shortest_distances[start_vertex][end_vertex]))
    print(" ".join(output_row))