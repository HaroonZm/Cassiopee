import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

N = ii()
A = [ii() for i in range(N)]

A.sort()
u1, u2 = [], []
l1, l2 = [], []
for i in range(N):
    if i < N//2:
        l1.append(A[i])
    else:
        u1.append(A[i])

    if i < (N+1)//2:
        l2.append(A[i])
    else:
        u2.append(A[i])

if N%2:
    ans = max(
        (2*sum(u1)-u1[0]-u1[1]) - 2*sum(l1),
        2*sum(u2) - (2*sum(l2)-l2[-1]-l2[-2])
    )
else:
    ans = (2*sum(u1)-u1[0]) - (2*sum(l1)-l1[-1])

print(ans)