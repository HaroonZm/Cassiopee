n, m = map(int, input().split())
mod = 10**9 + 7
a = list(map(int, input().split()))
dp = []
for _ in range(n+1):
    b = []
    for _ in range(n+1):
        b.append([0]*256)
    dp.append(b)
dp[0][0][0] = 1
i = 0
while i < n:
    x = a[i]
    for k in range(256):
        dp[i+1][0][k] = dp[i][0][k]
    j = 0
    while j < n:
        k = 0
        while k < 256:
            dp[i+1][j+1][k] = (dp[i][j+1][k] + dp[i][j][k^x]) % mod
            k += 1
        j += 1
    i += 1
f = 1
ans = 0
j = 1
while j <= n:
    f = (f * j) % mod
    ans = (ans + dp[n][j][m] * f) % mod
    j += 1
print(ans)