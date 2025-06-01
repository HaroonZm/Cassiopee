N = int(input())
a = list(map(int, input().split()))
dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1
ans = 0
i = 1
while i < N:
    n1 = a[i-1]
    n2 = a[i]
    if n1 != n2:
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = dp[i-1][1] + 1
        dp[i][2] = dp[i-1][2] + 1
    else:
        dp[i][0] = 1
        if dp[i-1][2] > ans:
            ans = dp[i-1][2]
        dp[i][2] = dp[i-1][1] + 1
        dp[i][1] = dp[i-1][0] + 1
    i += 1
res = max(dp[-1][0], dp[-1][1], dp[-1][2])
if ans > res:
    res = ans
print(res)