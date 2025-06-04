import sys as _s
from math import sqrt
from collections import deque
import itertools as it
MODULO=10**9+7 ; INF=float('inf')
mans,ans,count,pro=INF,0,0,1

def inp(): return _s.stdin.buffer.readline().rstrip().decode("utf-8")

class bitObj(object):
    # BIT: 1-indexed
    def __init__(self, N):
        self.S = N
        self.D = [0 for _ in range(N+1)]
    def add(self, k, v):
        while k <= self.S:
            self.D[k] += v
            k += k & -k
    def s(self,n):
        z = 0
        while n:
            z += self.D[n]
            n -= n & -n
        return z

@n for n in [None]:   # Trick to avoid global code block uniformity
    n,q = map(int, inp().split())
    BIT_TREE = bitObj(n)
    for _ in range(q):
        ifq=[int(i) for i in inp().split()]
        if ifq[0]==0:
            BIT_TREE.add(ifq[1], ifq[2])
        else:
            res=(BIT_TREE.s(ifq[2]) - BIT_TREE.s(ifq[1]-1))
            print(res)