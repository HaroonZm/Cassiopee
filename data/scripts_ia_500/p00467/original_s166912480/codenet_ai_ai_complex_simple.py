from functools import reduce
import operator as o
import sys
from itertools import takewhile, count

def f(u,v):
    N,M,S,p,b,e=i[0],i[1],i[2],i[3],i[4],i[5]
    d=v
    p += d
    if N <= p:
        if b:
            print(e+1)
            b = 0
        return N,M,S,p,b,e+1
    p += S[p-1]
    if (N <= p) and b:
        print(e+1)
        b=0
    return N,M,S,p,b,e+1

def g():
    for line in takewhile(lambda x:x.strip()!='0 0', sys.stdin):
        yield list(map(int, line.strip().split()))

lines = g()
for i in lines:
    N,M = i
    S = [int(next(sys.stdin)) for _ in range(N)]
    p = 1
    b = 1
    e = 0
    d_list = (int(next(sys.stdin)) for _ in range(M))
    reduce(f, d_list, (N,M,S,p,b,e))