#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

for line in sys.stdin:
    V, d = map(int, line.split())
    N = [False for i in range(2000)]
    p = pp = 1
    for i in range(V):
        num = (p + pp) % 1001
        N[num] = True
        p = pp
        pp = num
    ans = 0
    p = -10000
    for i in range(2000):
        if N[i]:
            if i - p >= d:
                ans += 1
            p = i
    print ans