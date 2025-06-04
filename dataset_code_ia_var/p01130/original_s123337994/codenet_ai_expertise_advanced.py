from sys import stdin
from itertools import product
from functools import partial

def floyd_warshall(L):
    n = len(L)
    for k, i, j in product(range(n), repeat=3):
        if L[i][j] > (alt := L[i][k] + L[k][j]):
            L[i][j] = alt

input_iter = iter(stdin.readline, '')
next_ints = lambda: map(int, next(input_iter).split())

INF = float('inf')
while True:
    try:
        n, m, s, g1, g2 = next_ints()
        if n == 0:
            break
        S, G1, G2 = s - 1, g1 - 1, g2 - 1

        L = [[0 if i == j else INF for j in range(n)] for i in range(n)]
        for _ in range(m):
            b1, b2, c = next_ints()
            L[b1 - 1][b2 - 1] = c

        floyd_warshall(L)

        ans = min(L[S][i] + L[i][G1] + L[i][G2] for i in range(n))
        print(int(ans) if ans < INF else "Impossible")
    except StopIteration:
        break