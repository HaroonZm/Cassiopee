import sys
exit = sys.exit
setrecursionlimit = sys.setrecursionlimit
stderr = sys.stderr

from functools import reduce as red
import itertools as it
from bisect import bisect_left as bl, bisect_right as br
from collections import deque, defaultdict as dd

def r():
    return int(input())

def rs():
    return list(map(int, input().split()))

INF = float('inf')
N, K, Q = rs()
A = rs()
A += [-10**18]

def lub(y):
    rez = []
    left = 0
    i = 0
    while i < N+1:
        if A[i] < y:
            chunk = A[left:i]
            chunk = sorted(chunk)
            if len(chunk) >= K-1:
                for e in it.islice(chunk, len(chunk)-K+1):
                    rez.append(e)
            left = i+1
        i += 1
    rez.sort()
    if len(rez) >= Q:
        return rez[Q-1]
    return INF

res = INF
for ival in filter(lambda z: True, A[:-1]):
    candidate = lub(ival)
    if candidate - ival < res:
        res = candidate - ival
print(res)