from scipy.sparse import *
(n, m), *d = [map(int, o.split()) for o in open(0)]
*w, a = zip(*[(i, j + n - 1, 1) for i, (_, *d) in enumerate(d) for j in d])
matrix = csr_matrix((a, w), [n + m] * 2)
components = csgraph.connected_components(matrix)[1]
result = "YNEOS"[1 in components[:n] :: 2]
print(result)