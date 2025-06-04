import sys
import re
from collections import Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
from fractions import Fraction
from bisect import bisect
from typing import List

input = sys.stdin.readline
def INT() -> int: return int(input())
def MAP(): return map(int, input().split())
def LIST() -> List[int]: return list(map(int, input().split()))

sys.setrecursionlimit(1 << 25)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
sigs = (''.join(sorted(input().strip())) for _ in range(N))
ctr = Counter(sigs)
print(sum(n * (n-1) // 2 for n in ctr.values()))