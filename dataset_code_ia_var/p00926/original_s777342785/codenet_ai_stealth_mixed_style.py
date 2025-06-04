import collections as coll
import math as m
from heapq import *
import bisect as bs
import random as rnd
import sys
from functools import reduce

sys.setrecursionlimit(99999)
inp = sys.stdin

bl = bs.bisect_left
br = bs.bisect_right

LInt = lambda: [int(f) for f in inp.readline().split()]
LFloat = lambda : list(map(float, inp.readline().split()))
LInt_ = lambda: [int(q)-1 for q in inp.readline().split()]
IInt = lambda: int(inp.readline())
IFloat = lambda: float(inp.readline())
LStr = lambda: list(map(list, inp.readline().split()))
StrR = lambda: list(inp.readline().rstrip())
ReadIter = lambda cnt: [IInt() for __ in range(cnt)]
LReadIter = lambda n: [LInt() for _ in range(n)]
FReadIter = lambda n: [IFloat() for _ in range(n)]
LFloatMatrix = lambda n: [LFloat() for _ in range(n)]
LReadIter_ = lambda n: [LInt_() for _ in range(n)]
SReadIter = lambda n: [StrR() for _ in range(n)]
LStrReadIter = lambda n: [LStr() for _ in range(n)]

MODULO = 1000000007
INF = float('INF')

def funcA():
    s_ = StrR()
    m_ = IInt()
    x = ["I", "L", "M", "U"]
    v = 0
    arr = []
    p = int(s_[0])
    for idx, ch in enumerate(s_):
        if ch == "+":
            p += int(s_[idx+1])
        elif ch == "*":
            p *= int(s_[idx+1])
    if p == m_:
        v = v+1
    arr.clear()
    tmp = 0
    s_b = s_[:]
    for i, z in enumerate(s_b):
        if z == "*":
            s_b[i+1] = int(s_b[i+1]) * int(s_b[i-1])
            s_b[i-1] = 0
    for w in s_b:
        if w != "*" and w != "+":
            tmp += int(w)
    if tmp == m_:
        v += 2
    print(x[v])
    return None

def funcB():
    (n, m), getlist = LInt(), LReadIter
    rec = getlist(m)
    buf = [0] * (n+1)
    for a, b in rec:
        buf[a] += 1
        buf[b] -= 1
    # scan
    for j in range(n):
        buf[j+1] += buf[j]
    answer = fl = 0
    for k in range(n):
        if buf[k]:
            for _ in range(1):
                answer += 3
        elif fl:
            fl = 0
            answer += 3
        else:
            answer += 1
    print(answer+1)
    return 0

def C(): pass
def D(): pass
class E:
    def __call__(self): return
def F(): return None
G=lambda: None
def H():
    return 0

if __name__ == '__main__':
    funcB()