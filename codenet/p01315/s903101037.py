#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve(n):
    lis = []
    for i in range(n):
        l = input().split()
        p,a,b,c,d,e,f,s,m = [int(i) for i in l[1:]]
        l = l[0]
        lis.append(((f*s*m-p)/(a+b+c+(d+e)*m),l))
    lis.sort(key = lambda x:(-x[0],x[1]))
    for i, j in lis:
        print(j)
    print("#")
    return

#Solve
if __name__ == "__main__":
    while 1:
        n = I()
        if n == 0:
            break
        solve(n)