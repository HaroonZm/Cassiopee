from sys import stdin
from functools import partial

MOD = 10**9 + 7

m, n = map(int, stdin.readline().split())
fast_pow = partial(pow, mod=MOD)
print(fast_pow(m, n))