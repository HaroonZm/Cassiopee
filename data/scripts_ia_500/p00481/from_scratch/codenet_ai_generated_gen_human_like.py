import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W, N = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]

positions = [None] * (N + 1)
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            positions[0] = (i, j)
        elif grid[i][j].isdigit():
            num = int(grid[i][j])
            positions[num] = (i, j)

def bfs(start, goal):
    dist = [[-1]*W for _ in range(H)]
    queue = deque()
    si, sj = start
    gi, gj = goal
    dist[si][sj] = 0
    queue.append((si, sj))
    while queue:
        i, j = queue.popleft()
        if (i, j) == (gi, gj):
            return dist[i][j]
        for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] != 'X' and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))
    return -1

total_time = 0
for i in range(N):
    total_time += bfs(positions[i], positions[i+1])

print(total_time)