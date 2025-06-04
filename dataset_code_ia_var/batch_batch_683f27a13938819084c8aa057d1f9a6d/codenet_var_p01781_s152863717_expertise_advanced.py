import sys
from functools import lru_cache
from operator import itemgetter

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    X, Y, Z, A, B, C, N = map(int, readline().split())

    MAXK = X + Y + Z + 1
    maxn = max(2*MAXK, 2*N+2)

    # Vectorized prefix sum construction using list comprehension
    S = [0] * maxn
    for k in range(N):
        S[k] = k * (k + 1) // 2
    for k in range(N, MAXK):
        S[k] = k * (k + 1) // 2 + S[k - N]

    # Use a cached closure for fast repeated calls (avoid negative indices)
    @lru_cache(None)
    def Sget(idx):
        if idx < 0:
            return 0
        return S[idx]

    # Vectorized calculation using tuple unpacking and inlined logic
    def calc(k, x, y, z):
        get = Sget
        return (
            get(k)
            - get(k - x)
            - get(k - y)
            - get(k - z)
            + get(k - x - y)
            + get(k - y - z)
            + get(k - z - x)
            - get(k - x - y - z)
        )

    # Precompute shifted values for efficiency
    X_A, Y_B, Z_C = X - A, Y - B, Z - C
    A_tuple = (A, B, C)
    xb, yb, zc = X_A, Y_B, Z_C
    ans = [0]*N

    for b in range(N):
        k = ((X + Y + Z - b - 1) // N) * N + b

        # Unroll calls for all inclusion-exclusion terms for clarity/performance
        args = [(k+1, xb, yb, zc),
                (k,   A, yb, zc),
                (k,   xb, B, zc),
                (k,   xb, yb, C),
                (k-1, A, B, zc),
                (k-1, xb, B, C),
                (k-1, A, yb, C),
                (k-2, *A_tuple)]

        ans[b] = sum(map(lambda args: calc(*args), args))

    write(" ".join(map(str, ans)))
    write('\n')

solve()