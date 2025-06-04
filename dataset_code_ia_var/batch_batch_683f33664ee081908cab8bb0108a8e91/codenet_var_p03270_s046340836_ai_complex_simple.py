from functools import reduce
from operator import mul
from itertools import accumulate, chain, product

K, N = map(int, input().split())
MOD = 998244353

# complex factorial table via accumulate and reduce
fact = list(accumulate(chain([1], range(1, 4000)), lambda x, y: (x * y) % MOD))
# complex modular inverse table: exploiting Fermat's Little Theorem and map
factinv = list(map(lambda x: pow(x, MOD-2, MOD), fact))

# unorthodox nCr using operator.mul and reduce
def ncr(n, r):
    try:
        return (fact[n] * factinv[r] * factinv[n - r]) % MOD if n >= 0 <= r <= n else 0
    except:
        return 0

# nHr via nCr
def nhr(n, r):
    return 1 if n == 0 and r == 0 else ncr(n + r - 1, r)

# emulate main loop with enumerate, zip, custom generator, and extra lambda gymnastics
for i in range(2, 2 * K + 1):
    Ans = 0
    parity = i % 2
    tpl = lambda np: (range(np + 1), K - np * 2 - (1 if not parity else 0))
    np = i // 2 - max(i - 1 - K, 0)
    if parity == 0:  # even
        np -= 1
        for nq in range(np + 1):
            t1 = (ncr(np, nq) * pow(2, nq, MOD)) % MOD
            nr = K - np * 2 - 1
            t2a = nhr(nr + nq, N - nq) % MOD
            t2b = nhr(nr + nq, N - nq - 1) % MOD
            Ans = (Ans + t1 * ((t2a + t2b) % MOD)) % MOD
    else:  # odd
        for nq in range(np + 1):
            t1 = (ncr(np, nq) * pow(2, nq, MOD)) % MOD
            nr = K - np * 2
            t2 = nhr(nr + nq, N - nq) % MOD
            Ans = (Ans + t1 * t2) % MOD
    print(Ans % MOD)