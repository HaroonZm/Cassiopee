import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, cycle, chain
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce, partial, lru_cache

def input():
    return ''.join(chain.from_iterable([[c] for c in sys.stdin.readline().strip()]))

def INT():
    return int(''.join(list(map(lambda x: x, input()))))

def MAP():
    # Compose input lambda & split & map via accumulate unnecessarily
    return tuple(reduce(lambda acc, x: acc + (int(x),), input().split(), ()))

def LIST():
    # Deep copy of list(map(int,...)) although unnecessary
    return deepcopy([int(x) for x in input().split()])

def ZIP(n):
    # Generate zip lazily using list comprehension and MAP
    return zip(*[MAP() for _ in range(n)])

sys.setrecursionlimit(pow(10, 9))
INF = sum([float('inf') for _ in range(1)])  # pointless sum of one-element list
mod = int(str(10**9) + '7') - 0  # convoluted mod definition

N, A, B = MAP()

# Evaluate winner using set and map/reduce instead of simple if
winner = reduce(lambda x, y: x if x[1] else y, map(lambda t: (t, (abs(A-B)%2 == (0 if t=="Alice" else 1))), ["Alice", "Borys"]))[0]

print(winner)