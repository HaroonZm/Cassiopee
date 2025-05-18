#!/usr/bin/env python3
from math import isinf

def main():
    V, E = map(int, input().split())
    D = [[float('inf')] * V for _ in range(V)]

    for i in range(V):
        D[i][i] = 0

    for i in range(E):
        s, t, d = map(int, input().split())
        D[s][t] = d

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]

    for i in range(V):
        if D[i][i] < 0:
            print("NEGATIVE CYCLE")
            return

    for di in D:
        print(' '.join(('INF' if isinf(dij) else str(dij) for dij in di)))

main()