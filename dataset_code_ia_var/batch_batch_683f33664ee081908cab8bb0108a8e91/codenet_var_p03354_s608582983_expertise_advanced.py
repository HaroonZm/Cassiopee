import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

def main():
    N, M = map(int, sys.stdin.readline().split())
    P = np.array(sys.stdin.readline().split(), dtype=int) - 1

    edges = np.loadtxt((sys.stdin.readline() for _ in range(M)), dtype=int) - 1
    if edges.ndim == 1:
        edges = edges.reshape(1, 2)

    data = np.ones(M, dtype=bool)
    matrix = csr_matrix((data, (edges[:,0], edges[:,1])), shape=(N, N), dtype=bool)
    matrix = matrix.maximum(matrix.transpose())  # Ensure undirected

    _, labels = connected_components(matrix)

    print(np.count_nonzero(labels == labels[P]))

if __name__ == "__main__":
    main()