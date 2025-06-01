from collections import deque
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
counts = [[0]*C for _ in range(R)]
adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for i in range(R):
    for j in range(C):
        if grid[i][j] != '.':
            grid[i][j] = int(grid[i][j])

for i in range(1, R-1):
    for j in range(1, C-1):
        counts[i][j] = sum(grid[i+di][j+dj] == '.' for di, dj in adj)

queues = [deque(), deque()]
for i in range(R):
    for j in range(C):
        if grid[i][j] != '.' and grid[i][j] <= counts[i][j]:
            grid[i][j] = '.'
            queues[0].append((i, j))

if not queues[0]:
    exit()

ans = 0
q = 0
while queues[q]:
    while queues[q]:
        x, y = queues[q].popleft()
        for dx, dy in adj:
            nx, ny = x+dx, y+dy
            counts[nx][ny] += 1
            if grid[nx][ny] != '.' and grid[nx][ny] == counts[nx][ny]:
                grid[nx][ny] = '.'
                queues[q ^ 1].append((nx, ny))
    q ^= 1
    ans += 1

print(ans)