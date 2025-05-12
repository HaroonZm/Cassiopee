import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

class Info:
    def __init__(self,arg_num,arg_loc):
        self.num = arg_num
        self.loc = arg_loc

    def __lt__(self,another):
        if self.num != another.num:
            return self.num > another.num
        else:
            return self.loc < another.loc

N,K = map(int,input().split())

Q = []

rest = N
need_out = N-K
out = 0

table = list(map(int,input().split()))

for loc in range(N):
    tmp = table[loc]
    heappush(Q,Info(tmp,loc))
    rest -= 1

    if out+rest >= need_out:
        continue

    info = heappop(Q)
    print("%d"%(info.num),end="")

    while len(Q) > 0 and Q[0].loc <= info.loc:
        heappop(Q)

print("")