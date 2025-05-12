n = int(input())
a = list(map(int,input().split()))

dp = [[1]*3 for i in range(n)]
ans = 1
for i in range(n-1):
    for j in range(3):
        if a[i] != a[i+1]:
            if dp[i+1][j] < dp[i][j] + 1:
                dp[i+1][j] = dp[i][j] + 1
        if j<2 and a[i] == a[i+1]:
            if dp[i+1][j+1] < dp[i][j] + 1:
                dp[i+1][j+1] = dp[i][j] + 1
for v in dp:
    t = max(v)
    if ans < t:
        ans = t
print(ans)