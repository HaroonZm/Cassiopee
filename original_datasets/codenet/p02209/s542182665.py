from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
from decimal import *
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
    n,k=MI()
    aa=LI()
    bek=[False]*(1<<n)
    for bit in range(1<<n):
        if bek[bit]==False:
            s=sum(a for i,a in enumerate(aa) if bit>>i&1)
            if s==k:bek[bit]=True
            else:continue
        for j in range(n):
            bek[bit|1<<j]=True
    mx=0
    for bit in range(1<<n):
        if bek[bit]:continue
        popcnt=bin(bit).count("1")
        if popcnt>mx:mx=popcnt
    print(n-mx)

main()