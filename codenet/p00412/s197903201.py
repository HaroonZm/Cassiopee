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

num_lane,num_info = map(int,input().split())
Q = []
for _ in range(num_lane):
    Q.append(deque())

for _ in range(num_info):
    command,value = map(int,input().split())
    if command == 0:
        value -= 1
        print("%d"%(Q[value].popleft()))
    else:
        min_car = BIG_NUM
        min_lane = BIG_NUM
        for i in range(num_lane):
            if len(Q[i]) < min_car:
                min_car = len(Q[i])
                min_lane = i
        Q[min_lane].append(value)