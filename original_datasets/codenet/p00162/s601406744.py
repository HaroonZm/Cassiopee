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

SIZE_2 = 20
SIZE_3 = 13
SIZE_5 = 9
NUM = 1000001

POW_2 = [1]*SIZE_2
for i in range(1,SIZE_2):
    POW_2[i] = POW_2[i-1]*2

POW_3 = [1]*SIZE_3
for i in range(1,SIZE_3):
    POW_3[i] = POW_3[i-1]*3

POW_5 = [1]*SIZE_5
for i in range(1,SIZE_5):
    POW_5[i] = POW_5[i-1]*5

table = [0]*(NUM)

for i in range(SIZE_2):
    for k in range(SIZE_3):
        if POW_2[i]*POW_3[k] >= NUM:
            break
        for p in range(SIZE_5):
            if POW_2[i]*POW_3[k]*POW_5[p] >= NUM:
                break
            table[POW_2[i]*POW_3[k]*POW_5[p]] = 1

for i in range(1,NUM):
    table[i] += table[i-1]

while True:
    tmp_str = input()
    if len(tmp_str) == 1 and tmp_str[0] == "0":
        break
    left,right = map(int,tmp_str.split())
    print("%d"%(table[right]-table[left-1]))