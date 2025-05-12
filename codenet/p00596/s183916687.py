#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

while True:
    try:
        n = input()
    except:
        break
    A = raw_input().split()
    E = [[] for i in range(7)]
    for s in A:
        u = int(s[0])
        v = int(s[1])
        E[u].append(v)
        E[v].append(u)
    cnt = 0
    for i in range(7):
        if len(E[i]) % 2 == 1:
            cnt += 1
    if cnt > 2:
        print "No"
        continue
    used = [len(E[i]) == 0 for i in range(7)]
    def func(num):
        if used[num]:
            return
        used[num] = True
        for u in E[num]:
            func(u)
    for i in range(7):
        if len(E[i]) > 0:
            func(i)
            break
    if False in used:
        print "No"
    else:
        print "Yes"