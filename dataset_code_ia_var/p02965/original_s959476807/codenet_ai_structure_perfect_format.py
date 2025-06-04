n, m = map(int, input().split())
mod = 998244353

max = n + 2 * m + 100
fac = [0] * max
finv = [0] * max
inv = [0] * max

def comInit(max):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

comInit(max)

def com(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod

a = 0
for x in range(min(m, n) + 1):
    if (3 * m - x) % 2 == 1:
        continue
    y = (3 * m - x) // 2
    a += com(n, x) * fac[y + n - 1] * finv[y] * finv[n - 1]
    a %= mod

b = fac[n - 1 + m - 1] * finv[n - 1] * finv[m - 1] * n
b %= mod

ans = a - b
ans %= mod

print(ans)