from functools import reduce
from itertools import chain, repeat, islice, starmap
import operator
import sys

sys.setrecursionlimit(10**6)

id_ = lambda x: x
one = lambda _:1
zero = lambda _:0

def elaborate_forest():
    while True:
        try:
            n = int(next(sys.stdin))
        except StopIteration:
            break
        if n == 0:
            break
        G = list(map(list, islice(repeat([]), n)))
        for _ in range(n - 1):
            a, b, t = starmap(int, zip(*[iter(next(sys.stdin).split())]*1))
            a, b = a - 1, b - 1
            for u,v in ((a,b),(b,a)):
                G[u] += [[v,t]]
        U = bytearray(n)
        L = bytearray(n)
        list(map(lambda i: L.__setitem__(i,1), filter(lambda k: len(G[k])==1, range(1,n))))
        def recurse(x):
            U[x] = 1
            q=(0,)
            p=[0]
            for y,t in G[x]:
                if not U[y] and not L[y]:
                    tt,pp = recurse(y)
                    q += (tt + t*2,)
                    p.append(pp+t)
            return (reduce(operator.add, q, 0), max(p))
        print((lambda s,m: s-m)(*recurse(0)))
elaborate_forest()