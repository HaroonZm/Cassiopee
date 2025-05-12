#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

while True:
    N, C = map(int, raw_input().split())
    if N == 0:
        break
    S = []
    for loop in range(N):
        lst = map(int, raw_input().split())
        S.append(lst)
    used = {}
    def func(x, y, c):
        if x < 0 or x > y or y >= N:
            return []
        if (x, y) in used:
            return []
        used[(x, y)] = 1
        if S[y][x] == 0:
            return [(x, y)]
        if S[y][x] != c:
            return []
        lst = []
        pos = [[x - 1, y], [x + 1, y], [x - 1, y - 1], [x, y - 1], [x, y + 1], [x + 1, y + 1]]
        for p in pos:
            p += [c]
            ret = func(*p)
            if ret:
                lst += ret
        return lst
    ans = -10000
    for y in range(N):
        for x in range(y + 1):
            if S[y][x] == 0:
                dum = S[y][x]
                S[y][x] = C
                ret = []
                for i in range(N):
                    for j in range(i + 1):
                        if S[i][j] != 0:
                            used = {}
                            if len(func(j, i, S[i][j])) == 0:
                                ret.append(S[i][j])
                S[y][x] = dum
                score = 0
                for num in ret:
                    if num == C:
                        score -= 1
                    else:
                        score += 1
                ans = max(ans, score)
    print ans