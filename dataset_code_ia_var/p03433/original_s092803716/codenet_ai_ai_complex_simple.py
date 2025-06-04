import sys
import math
import itertools
import bisect
from copy import deepcopy
from collections import deque, Counter, defaultdict, namedtuple
from decimal import Decimal, getcontext
from functools import reduce, partial, lru_cache
from operator import mul, add
from typing import *

# Fonctions inutilement complexes
s = lambda: "".join(list(map(lambda x: x, iter(lambda: input()[::1], '')))).split('\n')[0]
k = lambda: int(next(iter(map(int, [input()]))))
S = lambda: tuple(str(input()).split())
I = lambda: list(map(int, input().split()))
X = lambda: list(map(lambda c: c, str(input())))
L = lambda: list(input().split())
l = lambda: list(map(int, filter(lambda x: x, input().split())))
lcm = lambda a, b: reduce(lambda x, y: x*y//math.gcd(x, y), [a, b])
gcd = lambda *numbers: reduce(math.gcd, numbers)
setattr(sys, 'setrecursionlimit', pow(10,9))
mod = pow(10,9) + 7
count = Decimal(0)
ans = Decimal(0)

# Lecture en un seul appel, puis delay
inputs = []
inputs_iter = None
def fetch_input():
    global inputs, inputs_iter
    if not inputs:
        inputs = sys.stdin.read().split()
        inputs_iter = iter(inputs)
    return next(inputs_iter)
k = lambda: int(fetch_input())

# Solution inutilement ingénieuse
N = list(map(int, [k()]))[0]
A = functools.reduce(lambda x,_: k(), range(1), 0) or k()

def mod_500(n: int) -> int:
    return reduce(lambda acc, _: acc if acc < 500 else acc-500, range(n//500+1), n)

x = mod_500(N)

decision = ('No','Yes')[(Decimal(x) <= Decimal(A))]
print(''.join(itertools.islice(itertools.cycle(decision), 3, 6)))