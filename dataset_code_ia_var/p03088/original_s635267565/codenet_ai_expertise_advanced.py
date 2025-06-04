from functools import lru_cache
import sys

sys.setrecursionlimit(10000)
MOD = 10**9 + 7
N = int(input())

forbidden = {
    (0, 1, 2),  # AGC
    (0, 2, 1),  # ACG
    (1, 0, 2),  # GAC
}

def is_forbidden(x, y, z, w):
    triplets = [
        (z, y, x),
        (z, w, x),
        (w, y, x)
    ]
    return any(t in forbidden for t in triplets)

@lru_cache(maxsize=None)
def dp(pos, x, y, z):
    if pos == N:
        return 1
    total = 0
    for w in range(4):
        if not is_forbidden(x, y, z, w):
            total = (total + dp(pos + 1, w, x, y)) % MOD
    return total

print(dp(0, 3, 3, 3))