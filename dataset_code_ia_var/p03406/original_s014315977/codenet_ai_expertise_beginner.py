def combo(n, r, mod):
    if r < 0 or r > n:
        return 0
    if r > n - r:
        r = n - r
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10**9 + 7
N = 10**5
g1 = [1] * (N + 1)
g2 = [1] * (N + 1)
inv = [1] * (N + 1)

for i in range(2, N + 1):
    g1[i] = g1[i - 1] * i % mod
    inv[i] = (-inv[mod % i] * (mod // i)) % mod
    g2[i] = g2[i - 1] * inv[i] % mod
inv[0] = 0

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
size = 2 ** N
dp = []
for i in range(M + 1):
    dp.append([0] * size)

dp[0][0] = g1[size - 1]

for i in range(1, M + 1):
    for j in range(size):
        dp[i][j] = dp[i - 1][j]
        for k in range(N):
            if ((j >> k) & 1) == 0 and (size - A[i] - j) >= (2 ** k - 1):
                val = (g1[size - A[i] - j] * g2[size - A[i] + 1 - (j + 2 ** k)]) % mod
                add = ((-1) * val * ((dp[i - 1][j + 2 ** k] + g1[size - 1 - j - 2 ** k]) * (2 ** k)) % mod) % mod
                dp[i][j] = (dp[i][j] + add) % mod

ans = dp[M][0] * pow(2, N, mod) % mod
print(ans)