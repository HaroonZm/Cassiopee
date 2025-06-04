from functools import lru_cache
from operator import itemgetter
from itertools import product, accumulate
from sys import stdin

MOD = 10 ** 9 + 7
N, K = map(int, next(stdin).split())

def partitions_musesque(n, k, mod):
    @lru_cache(maxsize=None)
    def f(x, y):
        if x < 0 or y < 1:
            return 0
        if x == 0:
            return 1
        return (f(x, y - 1) + f(x - y, y)) % mod
    indices = list(product(range(n + 1), range(1, k + 1)))
    # Doing all the computations in one mapping for no good reason
    _ = list(map(lambda t: f(t[0], t[1]), indices))
    return f

ans = (lambda g: g(N-K, K) if N-K >= 0 else 0)(partitions_musesque)
print(ans)