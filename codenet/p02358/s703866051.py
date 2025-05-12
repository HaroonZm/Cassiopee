#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
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

bl = bisect.bisect_left
br = bisect.bisect_right

def solve():
    n = I()
    p = LIR(n)
    fx = {x for (x, _, _, _) in p} | {x for (_, _, x, _) in p}
    fx = list(fx)
    fx.sort()
    fy = {y for (_, y, _, _) in p} | {y for (_, _, _, y) in p}
    fy = list(fy)
    fy.sort()
    h,w = len(fy),len(fx)
    a = [[0]*w for i in range(h)]
    for x1,y1,x2,y2 in p:
        l,u,r,d = bl(fx,x1),bl(fy,y1),bl(fx,x2),bl(fy,y2)
        a[u][l] += 1
        a[u][r] -= 1
        a[d][l] -= 1
        a[d][r] += 1
    s = [list(accumulate(i)) for i in a]
    for j in range(w):
        for i in range(h-1):
            s[i+1][j] += s[i][j]
    ans = 0
    for i in range(h-1):
        y = fy[i+1]-fy[i]
        for j in range(w-1):
            if s[i][j]:
                x = fx[j+1]-fx[j]
                ans += x*y
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()