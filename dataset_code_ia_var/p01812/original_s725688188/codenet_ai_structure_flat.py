import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

nmk = sys.stdin.readline().split()
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])
d = [int(x)-1 for x in sys.stdin.readline().split()]
v = []
for _ in range(n):
    row = [int(x)-1 for x in sys.stdin.readline().split()]
    v.append(row)
dd_map = collections.defaultdict(lambda: None)
for i in range(m):
    dd_map[d[i]] = i
vv = []
for c in d:
    lst = []
    for i in range(k):
        lst.append(dd_map[v[c][i]])
    vv.append(lst)
vvv = []
for j in range(k):
    col = []
    for i in range(m):
        col.append(vv[i][j])
    vvv.append(col)
u = set()
m2 = 2**m
u.add(m2-1)
q = [(m2-1, 1)]
ii = [2**_ for _ in range(m)]
while q:
    qd, qk = q.pop(0)
    qdi = []
    for di in range(m):
        if qd & ii[di]:
            qdi.append(di)
    for vi in range(k):
        t = 0
        vvi = vvv[vi]
        for di in qdi:
            if not vvi[di] is None:
                t |= ii[vvi[di]]
        if t in u:
            continue
        if t == 0:
            print(qk)
            exit()
        u.add(t)
        q.append((t,qk+1))
print(-1)