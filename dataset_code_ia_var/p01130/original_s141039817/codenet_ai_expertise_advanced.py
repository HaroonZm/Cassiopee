import sys
from functools import partial
from operator import itemgetter

def warshall(n, matrix):
    for i in range(n):
        matrix[i][i] = 0
    for k in range(n):
        row_k = matrix[k]
        for i in range(n):
            row_i = matrix[i]
            mij, mik = row_i, row_i[k]
            for j in range(n):
                alt = mik + row_k[j]
                if alt < mij[j]:
                    mij[j] = alt
    return matrix

get_input = partial(map, int)
INF = float('inf')
stdin = sys.stdin

while True:
    try:
        n, m, s, g1, g2 = get_input(stdin.readline().split())
        if not (n or m or s or g1 or g2):
            break

        matrix = [[INF]*n for _ in range(n)]
        for _ in range(m):
            b1, b2, c = get_input(stdin.readline().split())
            matrix[b1-1][b2-1] = c

        costs = warshall(n, matrix)
        s_idx, g1_idx, g2_idx = s-1, g1-1, g2-1
        mincost = min(costs[s_idx][i] + costs[i][g1_idx] + costs[i][g2_idx] for i in range(n))
        print(mincost)
    except Exception:
        break