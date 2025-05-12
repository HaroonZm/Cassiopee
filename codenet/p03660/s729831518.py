import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

int1 = lambda x: int(x) - 1

N = int(input())
P = np.array([tuple(map(int1, input().split())) for _ in range(N - 1)]).T

matr = csr_matrix((np.ones(N - 1, dtype=int), P), shape=(N, N))
way_F = dijkstra(matr, indices=0, directed=False).astype(int)
way_F[way_F < 0] = N + 1
way_S = dijkstra(matr, indices=N - 1, directed=False).astype(int)
way_S[way_F < 0] = N + 1

fc = np.count_nonzero(way_F <= way_S)
print('Fennec' if fc > N - fc else 'Snuke')