import sys
import math
from functools import reduce, lru_cache, partial
from itertools import starmap, product, chain, repeat, islice
from collections import defaultdict
from operator import mul
sys.setrecursionlimit(10**9 << 5)

mod = 10**9 + 7
inf = float("inf")
def I():
    return int(next(sys.stdin))

def LI():
    return list(map(int, next(sys.stdin).split()))

def make_dp(n):
    # Nested defaultdict representing a matrix
    def z(): return defaultdict(int)
    return defaultdict(z, {0: defaultdict(int, {0: 1})})

n = I()
dp = make_dp(n)

inc = lambda x, y: (x + y) % mod

def symbol_logic(i, j, s):
    # dispatch logic for each symbol using dict and lambdas
    return {
        'U': lambda: [(j, dp[i][j]), 
                      (j+1, dp[i][j] * (i-j) % mod)],
        '-': lambda: [(j+1, dp[i][j])],
        'D': lambda: [(j+2, pow(i-j, 2, mod) * dp[i][j] % mod), 
                      (j+1, (i-j) * dp[i][j] % mod)]
    }[s]()

symbols = [next(sys.stdin).strip() for _ in range(n)]

for i, s in enumerate(symbols):
    pairs = chain.from_iterable(starmap(partial(symbol_logic, i), 
                          ((j,s) for j in range(n) if dp[i][j])) )
    updates = defaultdict(int)
    for k,v in pairs:
        updates[k] = (updates[k] + v)%mod
    for k,v in updates.items():
        dp[i+1][k] = (dp[i+1][k] + v)%mod

print(dp[n][n])