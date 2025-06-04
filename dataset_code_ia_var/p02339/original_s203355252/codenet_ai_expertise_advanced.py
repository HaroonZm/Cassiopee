from functools import lru_cache

MOD = 10**9 + 7

@lru_cache(maxsize=None)
def stirling(n: int, k: int) -> int:
    if k == 0 or k > n:
        return 0
    if k == 1 or k == n:
        return 1
    return (stirling(n - 1, k - 1) + k * stirling(n - 1, k)) % MOD

n, k = map(int, input().split())
print(stirling(n, k)) if n >= k else print(0)