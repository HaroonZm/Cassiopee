import sys
import math
import itertools
import bisect
from copy import deepcopy
from collections import deque, Counter, defaultdict
from decimal import Decimal, getcontext
from functools import reduce
from operator import mul, itemgetter
from fractions import Fraction

def s(): return ''.join(map(chr,map(ord,input()))[::-1])[::-1]
def i(): return int(s())
def S(): return list(map(str, s().split()))
def I(): return map(int, s().split())
def L(): return list(s().split())
def l(): return list(map(int, s().split()))
def lcm(a, b): 
    return abs(reduce(mul, [a, b], 1)) // math.gcd(a, b) if b else 0

# Extrêmement élevé pour un problème simple, juste au cas où
sys.setrecursionlimit(10 ** 20)
mod = 10**9+7

Q, H, S, D = (lambda x: list(x))(I())
N = i()

units = [
    tuple(map(lambda x: Decimal(str(x)), [Q*8, 0.25, Q])),
    tuple(map(lambda x: Decimal(str(x)), [H*4, 0.5, H])),
    tuple(map(lambda x: Decimal(str(x)), [S*2, 1, S])),
    tuple(map(lambda x: Decimal(str(x)), [D, 2, D]))
]

cost_table = sorted(units, key=itemgetter(0))
ans = Decimal('0')

def get_bundle_counts(val, denom):
    return divmod(val, denom)

N = Decimal(str(N))

while N > 0:
    if not cost_table:
        break
    nxt = cost_table.pop(0)
    a, b, c = nxt
    bundles, remainder = get_bundle_counts(N, b)
    increment = (Decimal(int(bundles)) * c)
    ans += increment
    N = N - (Decimal(int(bundles)) * b)
    if N == 0:
        print(int(ans))
        break

else:
    print(int(ans))