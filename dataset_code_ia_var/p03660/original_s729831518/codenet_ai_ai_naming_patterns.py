import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

def to_zero_based(value):
    return int(value) - 1

node_count = int(input())
edges = np.array([tuple(map(to_zero_based, input().split())) for _ in range(node_count - 1)]).T

adjacency_matrix = csr_matrix((np.ones(node_count - 1, dtype=int), edges), shape=(node_count, node_count))
dist_from_start = dijkstra(adjacency_matrix, indices=0, directed=False).astype(int)
dist_from_start[dist_from_start < 0] = node_count + 1
dist_from_end = dijkstra(adjacency_matrix, indices=node_count - 1, directed=False).astype(int)
dist_from_end[dist_from_start < 0] = node_count + 1

fennec_count = np.count_nonzero(dist_from_start <= dist_from_end)
print('Fennec' if fennec_count > node_count - fennec_count else 'Snuke')