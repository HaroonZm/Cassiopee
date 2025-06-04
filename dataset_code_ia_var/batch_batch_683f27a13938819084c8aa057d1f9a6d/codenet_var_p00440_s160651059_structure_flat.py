from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from fractions import gcd
from functools import lru_cache, reduce
from math import ceil, floor
from sys import setrecursionlimit
import heapq
import itertools
import operator

inf = float('inf')
N = []
K = []
C = []

setrecursionlimit(100000)

while True:
    s = input().split()
    if not s:
        continue
    n, k = int(s[0]), int(s[1])
    if n == 0 and k == 0:
        break
    N.append(n)
    K.append(k)
    c = []
    for _ in range(k):
        c.append(int(input()))
    C.append(c)

for idx in range(len(N)):
    n = N[idx]
    k = K[idx]
    c = C[idx][:]
    c.sort()
    ans = 0
    if len(c) > 0 and c[0] == 0:
        tmp = 1
        for i in range(1, len(c)-1):
            v1 = c[i]
            v2 = c[i+1]
            if v2 - v1 == 1:
                if tmp == 0:
                    s = 0
                elif tmp > 0:
                    s = 1
                else:
                    s = -1
                tmp += 1 * s
                if abs(tmp) > abs(ans):
                    ans = tmp
            elif v2 - v1 == 2:
                if tmp > 0:
                    tmp = -tmp - 2
                else:
                    tmp = -3
            else:
                tmp = 1
        if ans > 0:
            ans += 1
        ans = abs(ans)
    else:
        tmp = 1
        for i in range(len(c)-1):
            v1, v2 = c[i], c[i+1]
            if v2 - v1 == 1:
                tmp += 1
                if tmp > ans:
                    ans = tmp
            else:
                tmp = 1
    print(ans)