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

def solve():
    n,k,l,r = LI()
    a = LI()
    n1 = n>>1
    n2 = n-n1
    s1 = [[] for i in range(n1+1)]
    s2 = [[] for i in range(n2+1)]
    for b in range(1<<n1):
        s = 0
        j = 0
        for i in range(n1):
            if not b&(1<<i):
                continue
            s += a[i]
            j += 1
        s1[j].append(s)

    for b in range(1<<n2):
        s = 0
        j = 0
        for i in range(n2):
            if not b&(1<<i):
                continue
            s += a[i+n1]
            j += 1
        s2[j].append(s)
    for i in range(n2+1):
        s2[i].sort()
    ans = 0
    for i in range(n1+1):
        if i > k:
            break
        j = k-i
        if j > n2:
            continue
        for s in s1[i]:
            a,b = bisect.bisect_left(s2[j],l-s),bisect.bisect_right(s2[j],r-s)
            ans += b-a
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()