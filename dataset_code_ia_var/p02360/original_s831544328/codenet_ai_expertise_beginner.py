import sys

sys.setrecursionlimit(10 ** 7)
N = int(sys.stdin.readline())
grid = []
for i in range(1002):
    grid.append([0] * 1002)

for _ in range(N):
    line = sys.stdin.readline()
    x, y, xx, yy = map(int, line.split())
    grid[x][y] += 1
    grid[x][yy] -= 1
    grid[xx][y] -= 1
    grid[xx][yy] += 1

for i in range(1002):
    for j in range(1, 1002):
        grid[i][j] += grid[i][j - 1]

for i in range(1, 1002):
    for j in range(1002):
        grid[i][j] += grid[i - 1][j]

ans = 0
for row in grid:
    m = max(row)
    if m > ans:
        ans = m

print(ans)