import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    m = int(input())
    n = int(input())
    if m == 0 and n == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]

    def dfs(y, x):
        if dp[y][x]:
            return dp[y][x]
        max_len = 1
        for dir in range(4):
            ny, nx = y + dy[dir], x + dx[dir]
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx]:
                    res = dfs(ny, nx) + 1
                    if res > max_len:
                        max_len = res
        dp[y][x] = max_len
        return max_len

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                res = dfs(i, j)
                if res > ans:
                    ans = res
    print(ans)