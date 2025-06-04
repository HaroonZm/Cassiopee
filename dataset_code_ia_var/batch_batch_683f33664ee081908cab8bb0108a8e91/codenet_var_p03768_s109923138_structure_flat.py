import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

# Suppression de toutes les fonctions, réécriture plate :

n,m = [int(x) for x in sys.stdin.readline().split()]
e = collections.defaultdict(set)
i = 0
while i < m:
    ab = [int(x) for x in sys.stdin.readline().split()]
    a = ab[0]
    b = ab[1]
    e[a-1].add(b-1)
    e[b-1].add(a-1)
    i += 1

r = [0] * n

q = int(sys.stdin.readline())
qq = []
i = 0
while i < q:
    data = [int(x) for x in sys.stdin.readline().split()]
    qq.append([i]+data)
    i += 1

qq.sort(reverse=True)
f = [-1] * n
for item in qq:
    _, v, d, c = item
    v -= 1
    if f[v] >= d:
        continue
    if r[v] == 0:
        r[v] = c
    ql = [v]
    nd = d-1
    while nd >= 0:
        t = []
        for p in ql:
            for vv in e[p]:
                if f[vv] >= nd:
                    continue
                f[vv] = nd
                t.append(vv)
                if r[vv] == 0:
                    r[vv] = c
        ql = t
        nd -= 1

for x in r:
    print(x)