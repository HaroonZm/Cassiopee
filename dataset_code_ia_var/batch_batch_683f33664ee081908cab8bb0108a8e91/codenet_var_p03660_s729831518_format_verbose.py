import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

convert_input_to_index = lambda x: int(x) - 1

number_of_nodes = int(input())

edges_array = np.array([
    tuple(map(convert_input_to_index, input().split()))
    for _ in range(number_of_nodes - 1)
]).T

adjacency_matrix = csr_matrix(
    (
        np.ones(number_of_nodes - 1, dtype=int),
        edges_array
    ),
    shape=(number_of_nodes, number_of_nodes)
)

shortest_distances_from_fennec = dijkstra(
    adjacency_matrix, 
    indices=0, 
    directed=False
).astype(int)

shortest_distances_from_fennec[shortest_distances_from_fennec < 0] = number_of_nodes + 1

shortest_distances_from_snuke = dijkstra(
    adjacency_matrix, 
    indices=number_of_nodes - 1, 
    directed=False
).astype(int)

shortest_distances_from_snuke[shortest_distances_from_fennec < 0] = number_of_nodes + 1

fennec_controlled_nodes_count = np.count_nonzero(
    shortest_distances_from_fennec <= shortest_distances_from_snuke
)

if fennec_controlled_nodes_count > number_of_nodes - fennec_controlled_nodes_count:
    print('Fennec')
else:
    print('Snuke')