import sys
from collections import deque
from functools import partial

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v, color):
    stack = [(v, color)]
    while stack:
        node, c = stack.pop()
        if colors[node]:
            if colors[node] != c:
                return False
            continue
        colors[node] = c
        stack.extend((neigh, -c) for neigh in g[node] if colors[neigh] != c)
        if any(colors[neigh] == c for neigh in g[node]):
            return False
    return True

def floyd_warshall(d):
    for k in range(n):
        d_k = d[k]
        for i, d_i in enumerate(d):
            aik = d_i[k]
            for j in range(n):
                if d_i[j] > aik + d_k[j]:
                    d_i[j] = aik + d_k[j]
    return d

n = int(input())
g = [[] for _ in range(n)]
f_inf = float('inf')
dist = [[0 if i == j else f_inf for j in range(n)] for i in range(n)]

for i in range(n):
    S = input().strip()
    for j, val in enumerate(S):
        if val == '1':
            g[i].append(j)
            dist[i][j] = dist[j][i] = 1

colors = [0] * n
ans = -1

if not dfs(0, 1):
    print(ans)
else:
    floyd_warshall(dist)
    ans = max(max(row) for row in dist)
    print(ans + 1)