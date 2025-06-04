import numpy as np
from scipy.sparse import csr_matrix, csgraph

number_of_nodes, number_of_edges = map(int, input().split())

permutation_target_nodes = tuple(
    map(lambda node_label: int(node_label) - 1, input().split())
)

edge_indices = [
    tuple(map(lambda node_index: int(node_index) - 1, input().split()))
    for _ in range(number_of_edges)
]

edge_start_nodes, edge_end_nodes = zip(*edge_indices)

adjacency_matrix = csr_matrix(
    (
        np.ones((number_of_edges,), dtype=np.int8),
        (edge_start_nodes, edge_end_nodes)
    ),
    dtype=np.int8,
    shape=(number_of_nodes, number_of_nodes)
)

connected_component_labels = csgraph.connected_components(adjacency_matrix)[1]

count_fixed_connections = 0

for original_node_index, target_node_index in enumerate(permutation_target_nodes):

    connected_component_set = set(
        connected_component_labels[index]
        for index in (original_node_index, target_node_index)
    )

    if len(connected_component_set) == 1:
        count_fixed_connections += 1

print(count_fixed_connections)