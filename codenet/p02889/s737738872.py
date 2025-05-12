#!/usr/bin/env python3
import sys
import heapq
import functools
INF = float("inf")

# 無向グラフを仮定する。

class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = [[] for _ in range(N)]

    def add_edge(self, s, t, w=1):
        self.E[s].append((t, w))
        self.E[t].append((s, w))

def Warshall_Floyd(g: Graph):
    N = g.N
    dist = [[INF]*N for _ in range(N)]
    for from_, toweights in enumerate(g.E):
        for to_, w in toweights:
            dist[from_][to_] = w

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def solve(N: int,
          M: int,
          L: int,
          A: "List[int]",
          B: "List[int]",
          C: "List[int]",
          Q: int,
          s: "List[int]",
          t: "List[int]"):
    g = Graph(N)
    for i in range(M):
        g.add_edge(A[i]-1, B[i]-1, C[i])
    dist = Warshall_Floyd(g)

    g = Graph(N)
    for i in range(N):
        for j in range(i+1, N):
            if dist[i][j] <= L:
                g.add_edge(i, j, 1)
    dist = Warshall_Floyd(g)

    for i in range(Q):
        ans = dist[s[i]-1][t[i]-1]-1
        if ans == INF:
            print(-1)
        else:
            print(ans)

    return

def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    s = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, M, L, A, B, C, Q, s, t)

if __name__ == '__main__':
    main()