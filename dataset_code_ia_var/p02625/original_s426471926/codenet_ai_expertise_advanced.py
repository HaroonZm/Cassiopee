from functools import lru_cache
from operator import mul
from itertools import islice, accumulate
from typing import List

class Combination:
    __slots__ = ('n', 'mod', 'fact', 'fact_inv')
    def __init__(self, n: int, mod: int) -> None:
        self.n, self.mod = n, mod
        self.fact = self._make_fact(n)
        self.fact_inv = self._make_fact_inv(n)

    def _make_fact(self, n: int) -> List[int]:
        return list(accumulate(range(1, n + 1), lambda x, y: x * y % self.mod, initial=1))

    def _make_fact_inv(self, n: int) -> List[int]:
        mod = self.mod
        fact, res = self.fact, [1] * (n + 1)
        res[n] = pow(fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            res[i - 1] = res[i] * i % mod
        return res

    @lru_cache(maxsize=None)
    def c(self, m: int, k: int) -> int:
        if not 0 <= k <= m:
            return 0
        return self.fact[m] * self.fact_inv[k] % self.mod * self.fact_inv[m - k] % self.mod

    @lru_cache(maxsize=None)
    def p(self, m: int, k: int) -> int:
        if not 0 <= k <= m:
            return 0
        return self.fact[m] * self.fact_inv[m - k] % self.mod

mod = 10**9 + 7
n, m = map(int, input().split())
com = Combination(m, mod)

ans = sum(
    com.c(n, i) * (-1 if i & 1 else 1) * com.p(m, i) * pow(com.p(m - i, n - i), 2, mod) % mod
    for i in range(n + 1)
) % mod

print(ans)