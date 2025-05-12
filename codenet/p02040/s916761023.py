#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N, K = map(int, raw_input().split())

if N <= 10:
    print 0
    sys.stdout.flush()
    for _ in range(K):
        for j in range(1, N + 1):
            print j
            sys.stdout.flush()
            if raw_input() == "Yes":
                break
    exit()

E = []
for i in range(8):
    E += [(1, i + 2)]

for v in range(10, N + 1):
    num = v - 10
    for i in range(8):
        if num & (1 << i):
            E += [(v, i + 2)]

print len(E)
for u, v in E:
    print u, v

for _ in range(K):
    print 1
    sys.stdout.flush()
    S = raw_input()
    if S == "Yes":
        continue
    if S == "Near":
        for i in range(2, 10):
            print i
            sys.stdout.flush()
            if raw_input() == "Yes":
                break
        continue
    ans = 10
    for i in range(2, 10):
        print i
        sys.stdout.flush()
        if raw_input() == "Near":
            ans += (1 << (i - 2))
    print ans
    sys.stdout.flush()
    S = raw_input()