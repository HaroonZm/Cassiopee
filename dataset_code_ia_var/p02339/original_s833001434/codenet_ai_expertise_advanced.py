from functools import lru_cache

N, K = map(int, input().split())
MOD = 10**9 + 7

@lru_cache(maxsize=None)
def stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    if k == 1 or n == k:
        return 1
    return (stirling(n-1, k-1) + k * stirling(n-1, k)) % MOD

print(stirling(N, K))