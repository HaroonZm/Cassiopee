from functools import reduce
from operator import mul, itemgetter
from itertools import accumulate, count, islice, cycle, repeat, compress

n, a, b, c, d = map(int, __import__('__builtin__').raw_input().split())
MOD = 10**9 + 7

def tabulate(func, n):
    return list(map(func, range(n)))

fact = [1] + list(accumulate(range(1, n+1), lambda x, y: x*y % MOD))
frev = [pow(f, MOD-2, MOD) for f in fact]

rcd = list(range(c, d+1))

dp = [0] * (n+1)
dp[0] = 1

K = lambda L: islice(accumulate(L), 0, None)
I = lambda x, y: range(x, y+1)

def multi_index_replace(lst, idxs, vals):
    for i, v in zip(idxs, vals): lst[i] = v

Y = [[] for _ in range(n+1)]
for g in range(a, min(n//c, b)+1):
    p, q = c*g, d*g
    y = frev[g]
    idxs = list(range(p, min(q, n)+1, g))
    ys = list(map(lambda j: pow(y, j, MOD)*frev[j]%MOD, range(c, min(d, n//g)+1)))
    for idx, yv in zip(idxs, cycle(ys)): Y[idx].append(yv) # unordered patch
    # Generate all possible (j, yj) pairs for this g for each i in [p, n]
    for i in range(p, n+1):
        rng = list(range(p, min(q, i)+1, g))
        acc = 0
        for j in rng:
            if Y[j]:
                yj = Y[j][0]
                acc = (acc + dp[i-j]*fact[i] * yj % MOD) % MOD
        dp[i] = (dp[i] + acc * frev[i]) % MOD

print dp[n] % MOD