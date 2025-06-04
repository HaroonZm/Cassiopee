import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random,resource

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

rr = []

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        sp = line.strip().split()
        if not sp:
            continue
        n, m = map(int, sp)
        if n == 0:
            break
        bb = []
        for _ in range(n):
            bb.append(int(input(), 2))
        bc = collections.defaultdict(int)
        for i in bb:
            bc[i] += 1
        rt = 0
        b = []
        for k, v in bc.items():
            if v > 2:
                if v % 2 == 0:
                    rt += v - 2
                    v = 2
                else:
                    rt += v - 1
                    v = 1
            for i in range(v):
                b.append(k)
        n2 = len(b)
        c = collections.defaultdict(int)
        c[0] = 0
        for i in b:
            oldc = list(c.items())
            for k, v in oldc:
                t = k ^ i
                if c[t] <= v:
                    c[t] = v + 1
        rr.append(c[0] + rt)
    except Exception:
        break

print('\n'.join(map(str, rr)))