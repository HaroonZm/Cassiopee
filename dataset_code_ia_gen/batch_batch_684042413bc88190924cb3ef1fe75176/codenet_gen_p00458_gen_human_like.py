import sys
sys.setrecursionlimit(10**7)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]
    max_len = 1
    for direction in range(4):
        ni = i + dy[direction]
        nj = j + dx[direction]
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == 1:
                length = 1 + dfs(ni, nj)
                if length > max_len:
                    max_len = length
    dp[i][j] = max_len
    return max_len

while True:
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    if m == 0 and n == 0:
        break
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                ans = max(ans, dfs(i, j))
    print(ans)