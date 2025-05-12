# AOJ GRL_5_C Lowest Common Ancestor
# calculate LCA O(logN) for each query

# start form 0 node

# prev[i][k]: 2^k parent of node i 
# Depth[i]: depth of node i from 0

import sys
input = sys.stdin.readline

N = int(input())
Log_N = (N-1).bit_length()

prev = [[-1]*(Log_N+1) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
    K, *A = map(int, input().split())
    graph[i] = A
    for a in A:
        prev[a][0] = i

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

# BFS
Depth = [-1]*N
q = [0]
Depth[0] = 0
d = 0
while q:
    qq = []
    d += 1
    for p in q:
        for np in graph[p]:
            if Depth[np] == -1:
                Depth[np] = d
                qq.append(np)
    q = qq

# construct
for k in range(Log_N):
    for i in range(N):
        if prev[i][k] == -1:
            prev[i][k+1] = -1
        else:
            prev[i][k+1] = prev[prev[i][k]][k]

# LCA
def LCA(u, v):
    dd = Depth[v] - Depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd
    
    # set same depth
    for k in range(Log_N+1):
        if dd & 1:
            v = prev[v][k]
        dd >>= 1
    
    if u == v:
        return u
    
    for k in reversed(range(Log_N)):
        pu = prev[u][k]
        pv = prev[v][k]
        if pu != pv:
            u, v = pu, pv
    
    return prev[u][0]

for a, b in Query:
    print(LCA(a, b))