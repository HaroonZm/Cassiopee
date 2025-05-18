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

MAX = 10
POW = [1]*(MAX)

for i in range(1,MAX):
    POW[i] = POW[i-1]*4

while True:
    NUM = int(input())
    if NUM == -1:
        break
    elif NUM == 0:
        print("0")
        continue

    First = True
    for i in range(MAX-1,-1,-1):
        if POW[i] <= NUM:
            print("%d"%(NUM//POW[i]),end="")
            NUM %= POW[i]
            First = False
        else:
            if First: #
                pass
            else:
                print("0",end="")
    print()