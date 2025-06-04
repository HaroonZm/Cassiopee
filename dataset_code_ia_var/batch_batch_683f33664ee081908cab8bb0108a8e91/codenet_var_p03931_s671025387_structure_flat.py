mod = 10 ** 9 + 7
n, x = map(int, input().split())
a = list(map(int, input().split()))
dp = [[[0] * 256 for _ in range(n + 1)] for _ in range(2)]
dp[0][0][0] = 1
i = 0
while i < n:
    j = 0
    while j <= n:
        k = 0
        while k < 256:
            dp[(i + 1) & 1][j][k] = dp[i & 1][j][k]
            k += 1
        j += 1
    j = 0
    while j < n:
        k = 0
        while k < 256:
            dp[(i + 1) & 1][j + 1][k ^ a[i]] += dp[i & 1][j][k]
            if dp[(i + 1) & 1][j + 1][k ^ a[i]] >= mod:
                dp[(i + 1) & 1][j + 1][k ^ a[i]] -= mod
            k += 1
        j += 1
    i += 1
ans = 0
fac = [1] * (n + 1)
i = 1
while i <= n:
    fac[i] = fac[i - 1] * i
    if fac[i] >= mod:
        fac[i] -= mod
    i += 1
j = 0
while j <= n:
    ans += dp[n & 1][j][x] * fac[j]
    ans %= mod
    j += 1
print(ans)