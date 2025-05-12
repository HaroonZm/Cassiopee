import numpy as np
from scipy.sparse import csr_matrix, csgraph
N, M = map(int, input().split())
P = tuple(map(lambda n: int(n) - 1, input().split()))
row, column = zip(*tuple(tuple(map(lambda n: int(n) - 1, input().split())) for _ in range(M)))
matrix = csr_matrix((np.ones((M,), dtype=np.int8), (row, column)), dtype=np.int8, shape=(N, N))
connection = csgraph.connected_components(matrix)[1]
print(sum(len(set(connection[list(pair)])) == 1 for pair in enumerate(P)))