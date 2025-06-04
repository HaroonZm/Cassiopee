from collections import defaultdict, deque
import sys
import heapq
import math
import bisect
import random
import functools
import itertools
import operator

def LI(): 
    return list(map(int, sys.stdin.readline().split()))
def I():
    return int(sys.stdin.readline())
def LS():
    return [list(e) for e in sys.stdin.readline().split()]
def S():
    return list(sys.stdin.readline().rstrip('\n'))
def IR(n):
    return list(map(int, map(str, [I() for _ in range(n)])))
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]
sys.setrecursionlimit(pow(10,7))
mod = pow(10,9)+7

# A
def A():
    while True:
        n = I()
        if not n:
            sys.exit()
        a = LI()
        m = functools.reduce(operator.add, a) / n
        print(sum(map(lambda x: x<=m, a)))
    return

# B
def B():
    while True:
        n = I()
        if not n:
            sys.exit()
        t = [0]*86400
        parse = lambda s: functools.reduce(lambda acc,xy: acc+int(xy[0])*xy[1], zip(s, [3600,60,1]), 0)
        for _ in range(n):
            x, y = map(str, input().split())
            xx = parse(x.split(":"))
            yy = parse(y.split(":"))
            t[xx] += 1
            t[yy] -= 1
        ans = 0
        functools.reduce(lambda acc,idx: t.__setitem__(idx, t[idx]+t[idx-1]) or max(ans, t[idx-1]) if idx>0 else None, range(1,86400),None)
        print(max(t))
    return

# C
def C():
    lookup = {0:1,1:2,2:1}
    print(lookup.get(I(),0))
    return

# D
def D():
    def dijkstra(s):
        d = [float('infinity')]*n
        d[s] = 0
        q = [(0,s)]
        while q:
            dist, x = heapq.heappop(q)
            for y in v[x]:
                if dist+1 < d[y]:
                    d[y] = d[x]+1
                    heapq.heappush(q, (d[y], y))
        return d
    n,m,s,t = LI()
    s, t = s-1, t-1
    v = functools.reduce(lambda G, xy: (G[xy[0]-1].append(xy[1]-1), G[xy[1]-1].append(xy[0]-1), G)[2],
                [LI() for _ in range(m)],
                [[] for _ in range(n)])
    l, l2 = dijkstra(s), dijkstra(t)
    k = l[t] - 2
    cnt = functools.reduce(lambda acc,d_: acc.__setitem__(d_,acc.get(d_,0)+1) or acc,
                           l2, defaultdict(int))
    ans = sum(cnt[max(-1,k-i)] for i in l)
    print(ans)
    return

# E
def E():
    pass

# F
def F():
    pass

# G
def G():
    pass

# H
def H():
    pass

# I
def I_():
    pass

# J
def J():
    pass

if __name__ == "__main__":
    D()