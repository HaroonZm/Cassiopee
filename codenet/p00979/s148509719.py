#!/usr/bin/env python

from collections import deque, defaultdict
import itertools as ite
import sys
import math
import decimal

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

t = input()
ans = t

for p in range(1, 50):
    S = 2 * sum(3 ** i for i in range(p)) - 1
    if S > t:
        break
    num = 2 * p - 1
    rem = t - S
    for i in range(p):
        num += rem % 3
        rem /= 3
    num += rem
    ans = min(ans, num)
print ans