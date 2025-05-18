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
    input_str = input()
    if len(input_str) == 1 and input_str[0] == "0":
        break

    need,budget,aizu,normal,limit = map(int,input_str.split())

    left = 1;right = limit
    mid = (left+right)//2
    num_aizu = 0;num_normal = 0

    while left <= right:
        rest = budget-mid*aizu
        tmp_normal = rest//normal
        if rest >= 0 and mid+tmp_normal >= need:
            num_aizu = mid
            num_normal = tmp_normal
            left = mid+1
        else:
            right = mid-1
        mid = (left+right)//2

    if num_aizu == 0:
        print("NA")
    else:
        print("%d %d"%(num_aizu,num_normal))