H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# BFSで伐採工場(0,0)から各場所への最短距離を求める
from collections import deque

def bfs():
    dist = [[-1]*W for _ in range(H)]
    dist[0][0] = 0
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W:
                if A[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return dist

dist = bfs()

total_time = 0
for i in range(H):
    for j in range(W):
        if A[i][j] > 0:
            # (i,j) に木があるなら、そこまでの距離を2倍して木の本数をかける
            if dist[i][j] == -1:
                # 伐採工場から行けないところに木があるなら、無理なのでスキップ（条件的に無い想定）
                continue
            total_time += A[i][j] * 2 * dist[i][j]

print(total_time)