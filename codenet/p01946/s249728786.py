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
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
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

def solve():
    s,t,d = LI()
    w = LI()
    W = -sum(w)
    if W <= 0:
        for i in range(d):
            s += w[i]
            if s <= t:
                print(i+1)
                return
        print(-1)
    else:
        S = [s]
        for i in range(d):
            S.append(S[-1]+w[i])
            if S[-1] <= t:
                print(i+1)
                return
        m = min(S)
        for j in range(d+1):
            if S[j] == m:
                break
        s = S[j]
        w = w[j:]+w[:j]
        k = (s-t)//W
        s -= k*W
        if s <= t:
            print(k*d+j)
            return
        for i in range(d):
            s += w[i]
            if s <= t:
                print(k*d+i+1+j)
                return
    return

#Solve
if __name__ == "__main__":
    solve()