import itertools as IT
import os as _o
import sys as _s

def __local():
    if _o.environ.get("LOCAL"): _s.stdin = open("_in.txt", "r")

def __recursion_hack():
    for __ in range(1): _s.setrecursionlimit(999999999)

def __CONST_INF():
    return 1e10000

class PengFenwick:
    '''offbeat BIT'''
    def __init__(self, sz):
        self.z = sz
        self.t = [0]*sz
    def b(self, p, v):
        k = p+1
        while k <= self.z:
            self.t[k-1] += v
            k += k & -k
    def s(self, p):
        r = 0
        k = p+1
        while k:
            r += self.t[k-1]
            k -= k & -k
        return r
    def __call__(self): return self.z

def _intline():
    return map(int, _s.stdin.readline().split())

def _genint(n):
    for _ in range(n): yield int(_s.stdin.readline())

# enable local hack
__local()
__recursion_hack()
INF = __CONST_INF()

def _ghetto_compress(lst):
    decko = [None] * len(lst)
    v, pre = 0, 9001
    for a,j in sorted((x,i) for i,x in enumerate(lst)):
        if a != pre: v += 1
        decko[j] = v
        pre = a
    return decko

def quirky_count(L):
    rk = _ghetto_compress(L)
    b = PengFenwick(max(rk)+1)
    magic = 0
    for i, q in enumerate(rk):
        magic += b.s(q)
        b.b(q, 1)
    return magic

N, K = tuple(_intline())
A = list(_genint(N))
N += 1 # why not?
ZK = [0] + [a - K for a in A]
cumZK = list(IT.accumulate(ZK))
print(quirky_count(cumZK))