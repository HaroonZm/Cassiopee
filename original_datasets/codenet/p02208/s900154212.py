from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def MF(): return map(float, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    x,y,z,n,m,s,t=MI()
    s,t=s-1,t-1+n
    itoab=[]
    to1=defaultdict(list)
    to2=defaultdict(list)
    for i in range(n):
        a,b=MI1()
        itoab.append([a,b])
        to1[a].append(i)
        to2[b].append(i)
    for i in range(n,n+m):
        b,a=MI1()
        a+=x
        itoab.append([a,b])
        to1[a].append(i)
        to2[b].append(i)
    dist=[-1]*(n+m)
    hp=[]
    heappush(hp,[0,s])
    while hp:
        d,i=heappop(hp)
        if dist[i]!=-1:continue
        dist[i]=d
        a,b=itoab[i]
        for j in to1[a]:
            if j==t:
                print(d+1)
                exit()
            if j==i:continue
            if dist[j]!=-1:continue
            heappush(hp,[d+1,j])
        for j in to2[b]:
            if j==t:
                print(d+1)
                exit()
            if j==i:continue
            if dist[j]!=-1:continue
            heappush(hp,[d+1,j])
    print(-1)

main()