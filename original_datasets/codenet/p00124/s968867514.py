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

class Info:
    def __init__(self,arg_name,arg_index,arg_value):
        self.name = arg_name
        self.index = arg_index
        self.value = arg_value

    def __lt__(self,another):
        if self.value != another.value:
            return self.value > another.value
        else:
            return self.index < another.index

is_First = True

while True:
    N = int(input())
    if N == 0:
        break

    if is_First == False:
        print()

    table = []

    for i in range(N):
        tmp_name,win,lose,draw = map(str,input().split())
        table.append(Info(tmp_name,i,3*int(win)+int(draw)))

    table.sort()
    for i in range(N):
        print("%s,%d"%(table[i].name,table[i].value))

    is_First = False