import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solve():
    while True:
        m = int(input())
        n = int(input())
        if m == 0 and n == 0:
            break
        grid = [list(map(int, input().split())) for _ in range(n)]

        dp = [[-1]*m for _ in range(n)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            max_len = 1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+dy, j+dx
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    max_len = max(max_len, 1 + dfs(ni, nj))
            dp[i][j] = max_len
            return max_len

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        print(ans)

solve()