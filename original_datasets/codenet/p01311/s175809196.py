#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

INF = 10 ** 9
L = input()

for loop in range(L):
    n, m = map(int, raw_input().split())
    S, T = map(int, raw_input().split())
    E = [[] for i in range(n + 1)]
    for i in range(m):
        u, v, tp = raw_input().split()
        u = int(u)
        v = int(v)
        E[u].append((v, tp))
        E[v].append((u, tp))
    C1 = [INF] * (n + 1)
    que = deque()
    que.append((S, 0))
    while len(que) > 0:
        p = que.popleft()
        if C1[p[0]] <= p[1]:
            continue
        C1[p[0]] = p[1]
        for e in E[p[0]]:
            if e[1] == 'N':
                que.append((e[0], p[1] + 1))
    
    C2 = [INF] * (n + 1)
    que = deque()
    que.append((T, 0))
    while len(que) > 0:
        p = que.popleft()
        if C2[p[0]] <= p[1]:
            continue
        C2[p[0]] = p[1]
        for e in E[p[0]]:
            if e[1] == 'L':
                que.append((e[0], p[1]))
    if C2[0] == 0:
        print 0
        continue
    que = deque()
    for i in range(n + 1):
        if C2[i] == 0:
            que.append((i, 0))
    C2 = [INF] * (n + 1)
    while len(que) > 0:
        p = que.popleft()
        if C2[p[0]] <= p[1]:
            continue
        C2[p[0]] = p[1]
        for e in E[p[0]]:
            if e[1] == 'N':
                que.append((e[0], p[1] + 1))
    
    C3 = [INF] * (n + 1)
    que = deque()
    que.append((0, 0))
    while len(que) > 0:
        p = que.popleft()
        if C3[p[0]] <= p[1]:
            continue
        C3[p[0]] = p[1]
        for e in E[p[0]]:
            if e[1] == 'L':
                que.append((e[0], p[1]))
    que = deque()
    for i in range(n + 1):
        if C3[i] == 0:
            que.append((i, 0))
    C3 = [INF] * (n + 1)
    while len(que) > 0:
        p = que.popleft()
        if C3[p[0]] <= p[1]:
            continue
        C3[p[0]] = p[1]
        for e in E[p[0]]:
            if e[1] == 'N':
                que.append((e[0], p[1] + 1))
    ans = 10 ** 9
    for i in range(1, n + 1):
        ans = min(ans, C1[i] + C2[i] + C3[i])
    print ans