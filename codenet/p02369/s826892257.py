import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

V,E = map(int,input().split())
can_visit = [[None] * V for _ in range(V)]

for i in range(V):
    for k in range(V):
        can_visit[i][k] = (i == k)

for _ in range(E):
    FROM,TO = map(int,input().split())
    can_visit[FROM][TO] = True

#ワーシャルフロイド
for mid in range(V):
    for start in range(V):
        if can_visit[start][mid] == False:
            continue
        for goal in range(V):
            if can_visit[mid][goal] == False:
                continue
            can_visit[start][goal] = True

for FROM in range(V-1):
    for TO in range(FROM+1,V):
        if can_visit[FROM][TO] == True and can_visit[TO][FROM] == True:
            print("1")
            sys.exit()

print("0")