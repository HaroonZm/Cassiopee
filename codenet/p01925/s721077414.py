from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

while True:
    N,M = inpl()
    if N == 0 and M == 0:
        break
    else:
        MINlist = [[0,i] for i in range(N)]
        MAXlist = [[0,i] for i in range(N)]
        for _ in range(M):
            arg = inpl()
            s = arg[0]
            k = arg[1]
            cc = arg[2:]
            for c in cc:
                MAXlist[c-1][0] += s
            if k == 1:
                MINlist[c-1][0] += s

        MINlist.sort()
        MAXlist.sort(reverse=True)
        MinVal1,MinId1 = MINlist[0]
        MinVal2,MinId2 = MINlist[1]
        MaxVal1,MaxId1 = MAXlist[0]
        MaxVal2,MaxId2 = MAXlist[1]
        if MinId1 != MaxId1:
            print(MaxVal1-MinVal1+1)
        else:
            print(max(MaxVal2-MinVal1,MaxVal1-MinVal2)+1)