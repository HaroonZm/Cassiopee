import sys
import copy
import heapq
from collections import deque
import decimal

INF = sys.maxsize

while True:
    n = int(input())
    if n == 0:
        exit(0)
    # UnionFind flat
    uf_n = n
    uf_parents = [-1] * uf_n

    def uf_find(x):
        stk = []
        while uf_parents[x] >= 0:
            stk.append(x)
            x = uf_parents[x]
        for y in stk:
            uf_parents[y] = x
        return x

    def uf_union(x, y):
        x = uf_find(x)
        y = uf_find(y)
        if x == y:
            return
        if uf_parents[x] > uf_parents[y]:
            x, y = y, x
        uf_parents[x] += uf_parents[y]
        uf_parents[y] = x

    def uf_same(x, y):
        return uf_find(x) == uf_find(y)

    data = [input().split() for i in range(n)]
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1, r1 = data[i]
            x2, y2, z2, r2 = data[j]
            dist = ((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2 + (float(z1) - float(z2)) ** 2) ** 0.5
            dist = max(0, dist - float(r1) - float(r2))
            edges.append((dist, i, j))
    edges.sort()
    ans = 0
    for d, s, t in edges:
        if not uf_same(s, t):
            uf_union(s, t)
            ans += d
    print("{:.3f}".format(ans))