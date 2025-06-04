from functools import lru_cache

MOD = 10**9 + 7
N = int(input())

@lru_cache(maxsize=None)
def dp(n, a, b, c, d):
    if n == 3:
        if a == 0:
            # Remove forbidden patterns at initialization
            if (b, c, d) in [(0, 1, 2), (1, 0, 2), (0, 2, 1)]:
                return 0
            return 1
        return 0
    total = 0
    # Prune forbidden substrings early
    s1 = (b, c, d)
    s2 = (a, c, d)
    s3 = (a, b, d)
    if s1 in [(0, 1, 2), (1, 0, 2), (0, 2, 1)] or \
       s2 == (0, 1, 2) or s3 == (0, 1, 2):
        return 0
    for x in range(4):
        total = (total + dp(n-1, x, a, b, c)) % MOD
    return total

result = sum(dp(N, i, j, k, l) for i in range(4) for j in range(4) for k in range(4) for l in range(4)) % MOD
print(result)