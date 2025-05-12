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

while True:

    N = int(input())
    if N == 0:
        break

    me = list(map(int,input().split()))
    enemy = list(map(int,input().split()))

    me.sort(reverse=True)
    enemy.sort(reverse=True)

    num_win = 0
    ans = BIG_NUM

    k = 0

    for i in range(N-1):
        if me[i] > enemy[k]:
            num_win += 1
            if num_win > (i+1)//2:
                ans = i+1
                break
        else:
            k += 1

    if ans == BIG_NUM:
        print("NA")
    else:
        print("%d"%(ans))