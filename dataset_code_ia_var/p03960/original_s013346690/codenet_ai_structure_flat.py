import sys
input = sys.stdin.readline
H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(input().rstrip('\n'))
le = [''] * H
for i in range(H):
    le[i] = grid[i][0]
ans = 0
for w in range(1, W):
    ri = [''] * H
    for i in range(H):
        ri[i] = grid[i][w]
    cost = [[0] * (H+1) for _ in range(H+1)]
    for i in range(1, H+1):
        for j in range(1, H+1):
            cost[i][j] = cost[i-1][j-1] + int(le[i-1] == ri[j-1])
    inf = 1000000007
    dp = [[inf] * (H+1) for _ in range(H+1)]
    dp[0][0] = 0
    for i in range(H+1):
        for j in range(H+1):
            if i+1 <= H:
                if dp[i][j] + cost[i+1][j] < dp[i+1][j]:
                    dp[i+1][j] = dp[i][j] + cost[i+1][j]
            if j+1 <= H:
                if dp[i][j] + cost[i][j+1] < dp[i][j+1]:
                    dp[i][j+1] = dp[i][j] + cost[i][j+1]
    ans += dp[-1][-1]
    le = ri[:]
print(ans)