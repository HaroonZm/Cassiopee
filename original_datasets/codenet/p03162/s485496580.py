n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n+1)]
abc = []

for i in range(1, n+1):
    abc.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + abc[i][k])

ans = 0
for i in range(3):
    ans = max(ans, dp[n][i])
    
print(ans)