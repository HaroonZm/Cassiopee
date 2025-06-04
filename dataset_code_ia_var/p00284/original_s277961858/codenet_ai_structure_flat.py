import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)

SIZE = 32
POW = [1]*SIZE
i = 1
while i < SIZE:
    POW[i] = POW[i-1]*2
    i += 1

N = int(input())
n_iter = 0
while n_iter < N:
    vals = input().split()
    start = int(vals[0])
    goal = int(vals[1])
    ans = 0
    rank = 0
    current = start
    while current != goal:
        rank = 0
        i = SIZE-1
        while i > 0:
            if abs(current)%POW[i] == 0 and current+POW[i] <= goal:
                rank = i
                break
            i -= 1
        current += POW[rank]
        ans += 1
    print("%d"%(ans))
    n_iter += 1