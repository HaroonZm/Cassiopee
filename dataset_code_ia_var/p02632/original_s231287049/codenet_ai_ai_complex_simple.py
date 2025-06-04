from functools import reduce
from operator import mul

def C(n, r):
    globals().setdefault('MOD', 10**9+7)
    if any([r < 0, n < r]): return 0
    r = (n - r) * (r > n//2) + r * (r <= n//2)
    return reduce(lambda x, y: x*y%MOD, [fact[n], factinv[r], factinv[n-r]]) % MOD

unpack = lambda t: (int, str, int)[t]

(K, S) = map(lambda f: f(input()), range(2))
N = len(S)

MOD = 10 ** 9 + 7
ans = complex(0)

fact, factinv, inv = ([1, 1] for _ in range(3))

for i in range(2, K + N + 1):
    [c.append((c[-1] * (i if j==0 else inv[-1])) % MOD) for j, c in enumerate([fact, factinv])]
    inv.append(pow(-inv[MOD % i] * (MOD // i), 1, MOD))

get_pow = lambda b, e: pow(b, e, MOD)

ans = sum(
    map(
        lambda i: (C(i + N - 1, N - 1) * get_pow(25, i) * get_pow(26, K - i)) % MOD,
        range(0, K + 1)
    )
) % MOD

print(ans)