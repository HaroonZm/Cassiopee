from collections import deque

H, W, N = map(int, input().split())
grid = [input() for _ in range(H)]

# 座標を格納するリスト、S の位置を最初に追加しその後 1～N のチーズの位置を追加
positions = [None] * (N + 1)
for i in range(H):
    for j in range(W):
        c = grid[i][j]
        if c == 'S':
            positions[0] = (i, j)
        elif c.isdigit():
            num = int(c)
            positions[num] = (i, j)

def bfs(start, goal):
    """startとgoalは座標タプル、最短距離を返す"""
    queue = deque()
    queue.append(start)
    dist = [[-1]*W for _ in range(H)]
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return dist[x][y]
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] != 'X' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return -1  # 不可能な場合

time = 0
for i in range(N):
    time += bfs(positions[i], positions[i+1])
print(time)