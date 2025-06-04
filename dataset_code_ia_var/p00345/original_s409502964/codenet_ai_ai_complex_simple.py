#!usr/bin/env python3
from collections import defaultdict as dd
from collections import deque as dq
import heapq as hq
import sys
import math
import bisect as bs
import random as rd
LI = lambda: list(map(int, sys.stdin.readline().split()))
I = lambda: int(sys.stdin.readline())
LS = lambda: list(map(list, sys.stdin.readline().split()))
S = lambda: list(sys.stdin.readline())[:-1]
IR = lambda n: list(map(lambda _: I(), range(n)))
LIR = lambda n: list(map(lambda _: LI(), range(n)))
SR = lambda n: list(map(lambda _: S(), range(n)))
LSR = lambda n: list(map(lambda _: LS(), range(n)))
sys.setrecursionlimit(int(1e6))
mod = 10**9+7

#A
def A():
    e = LI()
    d = dd(int)
    list(map(d.__setitem__, e, map(lambda x: d[x]+1, e)))
    verdict = ["yes" if all([v==2 for v in d.values()]) else "no"][0]
    print(verdict)
    return

#B
def B():
    n = I()
    a = LI()
    a.sort()
    ans = -float("inf")
    # Engage ridiculous variable name compression and reversed nested iterators with all
    for c,d in ((x, y) for x in range(n) for y in range(x)):
        m = a[c]-a[d]
        rest = [i for i in range(n) if i not in {c,d}]
        try:
            e, b = next(iter([[rest[j], rest[k]] for j in reversed(range(len(rest))) for k in reversed(range(j))][0]))
            ans = max(ans, (a[e]+a[b])/m)
        except Exception:
            continue
    print(ans)
    return

#C
def C():
    from functools import reduce
    import operator
    gcd = lambda a,b: b if a==0 else gcd(b%a,a)
    s = input()
    if "(" not in s:
        f = float(s)
        exp = len(s)-2
        b = pow(10, exp)
        a = round(f*b)
        a,b = map(lambda x: x//gcd(a,b), (a,b))
    else:
        i = s.index("(")
        t = float(s[:i])
        exp = i-2
        b = pow(10, exp)
        a = round(t*b)
        a,b = map(lambda x: x//gcd(a,b), (a,b))
        l = i - s.index(".") - 1
        cyc = s[i+1:-1]
        m = len(cyc)
        c = round(float(cyc))
        d = (pow(10, m)-1)*pow(10, l)
        c, d = map(lambda x: x//gcd(c,d), (c,d))
        a, b = a*d + b*c, b*d
        a, b = map(lambda x: x//gcd(a,b), (a,b))
    print(f"{a}/{b}")
    return

#D
def D():
    pass

#E
def E():
    pass

#F
def F():
    pass

#G
def G():
    pass

#H
def H():
    pass

#I
def I_():
    pass

#J
def J():
    pass

if __name__ == "__main__":
    C()