from sys import stdin
from functools import partial

MOD = 10**9 + 7

read_ints = partial(map, int)
m, n = read_ints(stdin.readline().split())
print(pow(m, n, MOD))