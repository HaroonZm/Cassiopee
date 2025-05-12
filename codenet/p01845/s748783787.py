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

def solve(r0,w,c,r):
    c0 = r0/w
    if c0 >= c:
        print(0)
        return
    x = math.ceil((w*c-r0)/r)
    print(x)
    return

#Solve
if __name__ == "__main__":
    while 1:
        r0,w,c,r = LI()
        if r0 == w == c == r == 0:
            break
        solve(r0,w,c,r)