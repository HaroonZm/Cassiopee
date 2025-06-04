from functools import lru_cache

MOD = 10**9 + 7
n, kk = map(int, input().split())

@lru_cache(maxsize=None)
def dp(i, j, k):
    if i == 0:
        return int(j == 0 and k == 0)
    if k < 0 or j < 0 or j > n:
        return 0
    res = ((2 * j + 1) * dp(i - 1, j, k - 2 * j)) % MOD
    if j + 1 <= n:
        res = (res + ((j + 1) ** 2) * dp(i - 1, j + 1, k - 2 * j)) % MOD
    if j - 1 >= 0:
        res = (res + dp(i - 1, j - 1, k - 2 * j)) % MOD
    return res

print(dp(n, 0, kk))