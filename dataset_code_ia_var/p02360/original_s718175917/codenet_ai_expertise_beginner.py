import sys

N = int(sys.stdin.readline())

grid = []
for i in range(1001):
    line = []
    for j in range(1001):
        line.append(0)
    grid.append(line)

for i in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    grid[x1][y1] = grid[x1][y1] + 1
    grid[x2][y2] = grid[x2][y2] + 1
    grid[x2][y1] = grid[x2][y1] - 1
    grid[x1][y2] = grid[x1][y2] - 1

for i in range(1001):
    for j in range(1, 1001):
        grid[i][j] = grid[i][j] + grid[i][j-1]

for j in range(1001):
    for i in range(1, 1001):
        grid[i][j] = grid[i][j] + grid[i-1][j]

ans = 0
for i in range(1001):
    for j in range(1001):
        if grid[i][j] > ans:
            ans = grid[i][j]

print(ans)