import sys
import math
from collections import defaultdict as dd, deque as dq
import bisect as bi
from heapq import *
from itertools import permutations as perm, accumulate as acc

sys.setrecursionlimit(10**6)
MODULO = 1000000007

I = lambda: int(sys.stdin.readline())
LI = lambda : list(map(int, sys.stdin.readline().split()))
LS = lambda : [list(x) for x in sys.stdin.readline().split()]
def S(): 
    line = sys.stdin.readline()
    if line.endswith('\n'):
        return list(line[:-1])
    else:
        return list(line)
def IR(n):
    result = []
    c = 0
    while c < n:
        result.append(I())
        c += 1
    return result
def LIR(n):
    res = []
    for _ in range(n):
        res.append(LI())
    return res
SR = lambda n: [S() for _ in range(n)]
def LSR(n):
    out = []
    loop_count = 0
    while loop_count < n:
        out.append(LS())
        loop_count += 1
    return out

def solve():
    det = lambda a, b: a[0]*b[1] - a[1]*b[0]
    def minus(a, b):
        arr = []
        arr.append(a[0] - b[0])
        arr.append(a[1] - b[1])
        return tuple(arr)
    def convex_hull(points):
        size = len(points)
        points.sort()
        hull = [0] * (size + 5)
        idx = 0
        for i in range(size):
            while idx > 1:
                d = det(minus(hull[idx-1], hull[idx-2]), minus(points[i], hull[idx-1]))
                if d < 0:
                    idx -= 1
                else:
                    break
            hull[idx] = points[i]
            idx += 1
        last = idx
        for i in reversed(range(size-1)):
            while idx > last and det(minus(hull[idx-1], hull[idx-2]), minus(points[i], hull[idx-1])) < 0:
                idx -= 1
            hull[idx] = points[i]
            idx += 1
        nout = hull[:min(size, idx-1)]
        return nout

    n = I()
    points = LIR(n)
    ans = 0
    hull_pts = convex_hull(points)
    if len(hull_pts) == n:
        ans = 1
    else:
        ans = 0
    print(ans)

if __name__=='__main__': solve()