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

class Edge:
    def __init__(self,arg_to,arg_cost):
        self.to = arg_to
        self.cost = arg_cost

class Info:
    def __init__(self,arg_node_id,arg_sum_cost):
        self.node_id = arg_node_id
        self.sum_cost = arg_sum_cost

    def __lt__(self,another):
        return self.sum_cost < another.sum_cost

N,R = map(int,input().split())

G = [[] for _ in range(N+1)]
value = [None]*(N+1)
root = 0

for i in range(1,N+1):
    cost,tmp = map(int,input().split())
    G[root].append(Edge(i,cost))
    value[i] = tmp

for _ in range(R):
    to_,from_,cost = map(int,input().split())
    G[from_].append(Edge(to_,cost-1))

min_cost = [BIG_NUM]*(N+1)
min_cost[root] = 0;
Q = []

heappush(Q, Info(root,0))

while len(Q) > 0:
    info = heappop(Q)
    if info.sum_cost > min_cost[info.node_id]:
        continue
    for edge in G[info.node_id]:
        if min_cost[edge.to] > info.sum_cost+edge.cost:
            min_cost[edge.to] = info.sum_cost+edge.cost
            heappush(Q, Info(edge.to,min_cost[edge.to]))

ans = 0
for i in range(1,N+1):
    ans += min_cost[i]*value[i]

print("%d"%(ans))