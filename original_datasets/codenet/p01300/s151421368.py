#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

while True:
    S = raw_input()
    if S == '0':
        break
    m = [1] + [0 for i in range(10)]
    diff = ans = 0
    even = 1
    S = reversed(S)
    for c in S:
        num = int(c)
        diff = (diff + num * even) % 11
        if num != 0:
            ans += m[diff]
        m[diff] += 1
        even *= -1
    print ans