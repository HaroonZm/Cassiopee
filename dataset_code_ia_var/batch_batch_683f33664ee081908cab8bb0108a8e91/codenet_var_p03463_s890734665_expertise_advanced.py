import sys
import math
import itertools
from functools import partial

input = partial(next, sys.stdin)
INT = lambda: int(input())
MAP = lambda: map(int, input().split())
sys.setrecursionlimit(1_000_000)
INF = math.inf
mod = 10**9 + 7

N, A, B = MAP()
print("Alice" if (A - B) % 2 == 0 else "Borys")