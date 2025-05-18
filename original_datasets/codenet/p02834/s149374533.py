from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
# import numpy as np
# import scipy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
 
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return [list(map(int, input().split())) for _ in range(n)]

def bfs(s,n,g):
    went = [False]*n
    dis = [0]*n
    que = deque([])
    que.append(s)
    went[s] = True
    while que:
        go = que.pop()
        for i in range(len(g[go])):
            if went[g[go][i]]:
                continue
            dis[g[go][i]] = dis[go] + 1
            went[g[go][i]] = True
            que.append(g[go][i])
    return dis

def main():
    n,u,v = inpm()
    g = [[] for _ in range(n)]
    g1 = [[] for _ in range(n)]
    ab = []
    for _ in range(n-1):
        a,b = inpm()
        a -= 1
        b -= 1
        g[b].append(a)
        g[a].append(b)
        ab.append((a,b))
    dis = bfs(u-1,n,g)
    path = [v-1]
    que = deque([])
    que.append(v-1)
    d = dis[v-1]-1
    while que:
        go = que.pop()
        for i in range(len(g[go])):
            if dis[g[go][i]] == d:
                d -= 1
                path.append(g[go][i])
                que.append(g[go][i])
    ans = int(len(path)/2)-1
    path.reverse()
    for i in range(n-1):
        if (ab[i][0],ab[i][1]) == (path[ans],path[ans+1]) or (ab[i][1],ab[i][0]) == (path[ans],path[ans+1]):
            continue
        g1[ab[i][0]].append(ab[i][1])
        g1[ab[i][1]].append(ab[i][0])
    dis1 = bfs(path[ans],n,g1)
    x = ans+max(dis1)
    if len(path)%2==1:
        x+=1    
    print(x)

if __name__ == "__main__":
    main()