#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N = input()
P = raw_input().split()

ans = P[0]
for i in range(1, N):
    if ans + P[i] == 'TF':
        ans = 'F'
    else:
        ans = 'T'

print ans