import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# 深さ優先探索で根から各頂点の深さを求める
depth = [0]*N
def dfs(v, p):
    for nv in graph[v]:
        if nv == p:
            continue
        depth[nv] = depth[v] + 1
        dfs(nv, v)
dfs(0, -1)

# 各頂点の次数を数える
degree = [len(adj) for adj in graph]

# 木の直径の長さを求めるためにBFSを2回実施
from collections import deque
def bfs(start):
    dist = [-1]*N
    dist[start] = 0
    que = deque([start])
    while que:
        v = que.popleft()
        for nv in graph[v]:
            if dist[nv]<0:
                dist[nv] = dist[v]+1
                que.append(nv)
    max_d = 0
    max_i = start
    for i,d in enumerate(dist):
        if d > max_d:
            max_d = d
            max_i = i
    return max_i, dist

# 木の直径の両端を探索
u,_ = bfs(0)
v, dist_u = bfs(u)
_, dist_v = bfs(v)

# 木の辺の数はN-1、全ての辺を2回通るものとして全体では2*(N-1)歩は最低必要
# スタート地点から一番遠い端までの距離分の節約が出来る。また出発地点によって節約出来る距離が変わる。
# u,vは直径の端点で、どちらかの端の距離をとる
for i in range(N):
    res = 2*(N-1) - max(dist_u[i], dist_v[i])
    print(res)