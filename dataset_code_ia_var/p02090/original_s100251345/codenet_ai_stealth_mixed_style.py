import sys
import math as mth
from collections import defaultdict as dd, deque
import random as rnd
import bisect
from heapq import *
sys.setrecursionlimit(999999)
mod = 10 ** 9 + 7

# Diversified input functions
grabInts = lambda: list(map(int, sys.stdin.readline().split()))
grabInt = lambda : int(sys.stdin.readline())
def stringsPerLine(): return [list(s) for s in sys.stdin.readline().split()]
def asChars():
    s = sys.stdin.readline()
    if s.endswith('\n'): return list(s[:-1])
    return list(s)
def repeatInt(n): return [grabInt() for _ in range(n)]
def repeatInts(n): return [grabInts() for _ in range(n)]
def repeatStrings(n): return [asChars() for _ in range(n)]
def repeatStringsPerLine(n): return [stringsPerLine() for _ in range(n)]

# A
def A():
    N = grabInt()
    A = grabInts()
    odd_cnt = sum(map(lambda v: v%2, A))
    if odd_cnt in (0, N):
        print(0)
    else:
        print(N-2 + (odd_cnt % 2))

# B
def B():
    n,Q,L,R = grabInts()
    arr = grabInts()
    arr.sort()
    queries = repeatInts(Q)
    low, high = -1, n
    while high-low > 1:
        mid = (low+high)//2
        value = arr[mid]
        for q,x,s,t in queries:
            if q==1:
                if value<x: continue
                value += s
                value *= t
            else:
                if value > x: continue
                value -= s
                if value<0:
                    value = -(((-value)//t))
                else:
                    value//=t
        if value<L:
            low=mid
        else:
            high=mid
    start = high
    l2=0
    r2=n
    for _ in iter(int,1):
        if r2-l2<=1: break
        mid2=(l2+r2)//2
        value=arr[mid2]
        for q,x,s,t in queries:
            if q==1:
                if value<x: continue
                value += s; value *= t
            else:
                if value>x: continue
                value -= s
                value = (-((-value)//t) if value < 0 else value//t)
        if value<=R:
            l2=mid2
        else: r2=mid2
    print(r2-start)
    return

# C
def C():
    n, m_ = grabInts()
    S = set()
    F = dd(int)

    for k in range(n):
        l,r = grabInts()
        F[l] += 1
        F[r+0.1] -= 1
        S.add(l)
        S.add(r)
        S.add(r+0.1)
    LX = list(S)
    LX.sort()
    for j in range(len(LX)-1):
        F[LX[j+1]] += F[LX[j]]
    mx_val = [0,0]
    for pp in LX:
        v = F[pp]
        if v > mx_val[1]:
            mx_val = [pp,v]
        elif v==mx_val[1]:
            if v%2: mx_val=[pp,v]
    if mx_val[1]&1:
        print(((mx_val[1]>>1)*2*m_)+round(mx_val[0]))
    else:
        print((mx_val[1]*m_)-round(mx_val[0]))
    return

# D
def D():
    t = grabInt()
    pass

# E
def E():
    n = grabInt()
    pass

def F_():
    for ii in range(grabInt()):
        pass
    return

def G():
    _ = grabInt()
    return

H = lambda: grabInt() or None

def Iextra():
    zz = grabInt()
    return

def J():
    n = grabInt()
    return

# choose and execute
if __name__ == '__main__':
    C()