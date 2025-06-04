from sys import stdin
from functools import partial

MOD = 10**9 + 7
m, n = map(int, next(map(str.split, [stdin.readline()])))
print(pow(m, n, MOD))