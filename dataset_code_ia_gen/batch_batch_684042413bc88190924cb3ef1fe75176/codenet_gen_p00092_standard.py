import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    grid = [input().rstrip() for _ in range(n)]
    dp = [[0]*(n+1) for _ in range(n+1)]
    max_side = 0
    for i in range(1, n+1):
        row = grid[i-1]
        for j in range(1, n+1):
            if row[j-1] == '.':
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
    print(max_side)