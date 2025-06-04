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

N, LEN, LIMIT = map(int, input().split())

speed = [None]*N
loc = [None]*N
num_fill = [0]*LEN
num_empty = [0]*LEN

ans = N

for i in range(N):
    speed[i] = int(input())
    loc[i] = speed[i]

for current in range(2, LIMIT+1):
    for i in range(LEN):
        num_fill[i] += num_empty[i]
        num_empty[i] = 0
    for i in range(N):
        loc[i] += speed[i]
        loc[i] %= LEN
        num_empty[loc[i]] += 1
        if num_fill[loc[i]] > 0:
            num_fill[loc[i]] -= 1
        else:
            ans += 1

print("%d" % (ans))