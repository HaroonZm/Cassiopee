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

sys.setrecursionlimit(100001)

class Edge:
    def __init__(self,arg_to,arg_dist):
        self.to = arg_to
        self.dist = arg_dist

V = int(input())
G = [[] for _ in range(V)]

for _ in range(V-1):
    from_,to_,dist_ = map(int,input().split())
    G[from_].append(Edge(to_,dist_))
    G[to_].append(Edge(from_,dist_))

ans = 0

def recursive(node_id,parent):
    max_path1 = 0
    max_path2 = 0

    global ans

    for edge in G[node_id]:
        if edge.to == parent:
            continue
        tmp_dist = edge.dist+recursive(edge.to,node_id)
        if tmp_dist > max_path1:
            max_path2 = max_path1
            max_path1 = tmp_dist
        elif tmp_dist > max_path2:
            max_path2 = tmp_dist

    ans = max(ans,max_path1+max_path2)
    return max_path1

recursive(V//2,-1)
print("%d"%(ans))