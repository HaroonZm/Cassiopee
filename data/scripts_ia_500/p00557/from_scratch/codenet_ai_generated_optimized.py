import sys
sys.setrecursionlimit(10**7)
H, W = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

idx = [[-1]*W for _ in range(H)]
cells = []
for i in range(H):
    for j in range(W):
        cells.append((grid[i][j], i, j))
cells.sort(key=lambda x: -x[0])

dp = [[0]*W for _ in range(H)]
for _, i, j in cells:
    basin_count = 0
    has_lower = False
    for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
        ni, nj = i+di, j+dj
        if 0 <= ni < H and 0 <= nj < W:
            if grid[ni][nj] < grid[i][j]:
                has_lower = True
                basin_count += 1 if dp[ni][nj]==0 else dp[ni][nj]
    dp[i][j] = basin_count if has_lower else 1

res = 0
for i in range(H):
    for j in range(W):
        if dp[i][j] > 1:
            res += 1
print(res)