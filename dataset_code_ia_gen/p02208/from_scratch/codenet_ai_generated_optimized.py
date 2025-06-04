import sys
from collections import deque
input = sys.stdin.readline

X,Y,Z,N,M,S,T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(M)]

# ノード番号付け
# カツサンド：0〜N-1
# カツ(素材)：N〜N+Y-1
# カツカレー：N+Y〜N+Y+M-1

offset_cut = N
offset_curry = N + Y

graph = [[] for _ in range(N + Y + M)]

# カツサンドとカツの辺 (双方向)
for i, (a,b) in enumerate(AB):
    b_node = offset_cut + (b - 1)
    graph[i].append(b_node)
    graph[b_node].append(i)

# カツカレーとカツの辺 (双方向)
for i, (c,d) in enumerate(CD):
    c_node = offset_cut + (c - 1)
    curry_node = offset_curry + i
    graph[curry_node].append(c_node)
    graph[c_node].append(curry_node)

start = S - 1
goal = offset_curry + (T - 1)

dist = [-1]*(N+Y+M)
dist[start] = 0
queue = deque([start])

while queue:
    v = queue.popleft()
    if v == goal:
        print(dist[v]//2)
        break
    for nv in graph[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            queue.append(nv)
else:
    print(-1)