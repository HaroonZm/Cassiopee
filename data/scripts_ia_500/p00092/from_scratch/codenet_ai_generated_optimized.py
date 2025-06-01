import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    grid = [input().rstrip() for _ in range(n)]
    dp = [0]*(n+1)
    max_side = 0
    for i in range(n):
        prev = 0
        for j in range(n):
            temp = dp[j+1]
            if grid[i][j] == '.':
                dp[j+1] = min(dp[j], dp[j+1], prev) + 1
                if dp[j+1] > max_side:
                    max_side = dp[j+1]
            else:
                dp[j+1] = 0
            prev = temp
    print(max_side)