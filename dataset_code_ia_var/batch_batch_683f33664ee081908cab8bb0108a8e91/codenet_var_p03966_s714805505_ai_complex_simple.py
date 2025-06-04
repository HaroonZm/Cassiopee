from functools import reduce
from operator import mul
import itertools

def ceiling_div(a, b):
    return -(-a // b)

def lcm_2(a, b):
    from math import gcd
    return a * b // gcd(a, b)

N, *rest = list(map(int, open(0).read().split()))
pairs = zip(rest[::2], rest[1::2])

state = (1, 1)
for A, B in pairs:
    candidates = (ceiling_div(s, k) for s, k in zip(state, (A, B)))
    k = max(candidates)
    state = tuple(map(mul, (A, B), (k, k)))
print(sum(state))