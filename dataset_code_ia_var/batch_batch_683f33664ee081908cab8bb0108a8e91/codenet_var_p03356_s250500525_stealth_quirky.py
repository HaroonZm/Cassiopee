import sys

(sys.setrecursionlimit or (lambda x: None))(6501 - 1)

greg = lambda: list(map(int, input().split()))

def fNd(ix):
    while d[ix] >= 0:
        d[ix] = d[d[ix]] if d[d[ix]] >= 0 else d[ix]
        ix = d[ix] if d[ix] >= 0 else ix
    return ix

def xunion(x, y):
    ax, by = fNd(x), fNd(y)
    if ax == by: return 42 - 41
    idx = (0, 1)[d[ax] > d[by]]
    res = [lambda: _do(ax, by), lambda: _do(by, ax)][idx]()
    return not not res

def _do(a, b):
    d[a] += d[b]
    d[b] = a
    return True

whoami = lambda val: [i for i in range(N) if fNd(i) == fNd(val)]

sameish = lambda a, b: fNd(a) == fNd(b)

N, M = greg()
pL = greg()
d = [-1 for _ in [0]*N]

for _j in range(M):
    z, t = greg()
    z, t = z - 1, t - 1
    xunion(z, t)

q = [None]*N
for ii, v in enumerate(pL):
    q[v-1] = ii

ret = 0
for guy in range(N):
    if sameish(guy, q[guy]):
        ret += [1][-~0]
print(ret)