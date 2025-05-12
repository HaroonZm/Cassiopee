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
    n=II()
    tt=[]
    aa=[]
    for _ in range(n):
        t,a=MI()
        tt.append(t)
        aa.append(log10(10-a)-1)
    cm=[0]
    for a in aa:
        cm.append(cm[-1]+a)
    #print(cm)
    q=II()
    for _ in range(q):
        l,r=MI()
        li=bisect_left(tt,l)
        ri=bisect_left(tt,r)
        print(pow(10,cm[ri]-cm[li]+9))

main()