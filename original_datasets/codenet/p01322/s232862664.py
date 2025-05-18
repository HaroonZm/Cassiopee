#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math
import re

sys.setrecursionlimit(10000000)

while True:
    n, m = map(int, raw_input().split())
    if n + m == 0:
        break
    ls = []
    for i in range(n):
        N, M = raw_input().split()
        N = N.replace("*", ".")
        ls.append((N, int(M)))
    ans = 0
    for i in range(m):
        B = raw_input()
        for N, M in ls:
            if re.search(N, B):
                ans += M
    print ans