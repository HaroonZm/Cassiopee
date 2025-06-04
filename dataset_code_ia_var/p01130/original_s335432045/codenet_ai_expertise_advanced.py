from sys import stdin
from itertools import starmap, repeat
from operator import itemgetter

INF = 10 ** 5

def floyd_warshall(N, D):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (alt := D[i][k] + D[k][j]) < D[i][j]:
                    D[i][j] = alt
    return D

input_iter = iter(stdin.readline, '')
while True:
    try:
        N, M, s, g1, g2 = map(int, next(input_iter).split())
        if not any((N, M, s, g1, g2)):
            break
        s, g1, g2 = (x - 1 for x in (s, g1, g2))
        D = [[0 if i == j else INF for j in range(N)] for i in range(N)]
        edges = (map(int, next(input_iter).split()) for _ in range(M))
        for b1, b2, c in edges:
            D[b1-1][b2-1] = c
        dist = floyd_warshall(N, D)
        print(min(starmap(lambda i: dist[s][i] + dist[i][g1] + dist[i][g2], enumerate(repeat(None, N)))))
    except StopIteration:
        break