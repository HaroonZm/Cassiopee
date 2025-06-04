import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = int(sys.stdin.readline().strip())
h = 1
while h < 3501:
    n = 1
    while n < 3501:
        denom = 4 * h * n - N * n - N * h
        if denom != 0:
            w = N * h * n / denom
            if w.is_integer() and w >= 1:
                print(h, n, int(w))
                sys.exit()
        n += 1
    h += 1