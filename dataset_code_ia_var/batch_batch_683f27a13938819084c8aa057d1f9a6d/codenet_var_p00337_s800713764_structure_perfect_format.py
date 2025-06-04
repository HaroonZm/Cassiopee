def quickhull(l, r, s, k, il, ir):
    if not s:
        return
    su = []
    sd = []
    a = (r[0] - l[0], r[1] - l[1])
    for x, y in s:
        b = (x - l[0], y - l[1])
        cro = cross(a, b)
        if cro > 0:
            su.append((x, y))
        elif cro < 0:
            sd.append((x, y))
    ind = (ir - il) / 2
    if su:
        c, d = direction(l, r, su[0])
        p = su[0]
        for i in range(1, len(su)):
            c_, d_ = direction(l, r, su[i])
            if c * d_ < c_ * d:
                c, d = c_, d_
                p = su[i]
        i = ir + ind
        k.append((tuple(p), i))
        b = (l[0] - p[0], l[1] - p[1])
        c = (p[0] - r[0], p[1] - r[1])
        s1 = []
        s2 = []
        for x, y in su:
            b_ = (x - p[0], y - p[1])
            c_ = (x - r[0], y - r[1])
            cro_b, cro_c = cross(b, b_), cross(c, c_)
            if cro_b >= 0 and cro_c >= 0:
                continue
            else:
                if cro_b < 0:
                    s1.append((x, y))
                elif cro_c < 0:
                    s2.append((x, y))
        quickhull(l, p, s1, k, il, i)
        quickhull(r, p, s2, k, ir, i)
    if sd:
        c, d = direction(l, r, sd[0])
        p = sd[0]
        for i in range(1, len(sd)):
            c_, d_ = direction(l, r, sd[i])
            if c * d_ < c_ * d:
                c, d = c_, d_
                p = sd[i]
        i = il + ind
        k.append((tuple(p), i))
        b = (l[0] - p[0], l[1] - p[1])
        c = (p[0] - r[0], p[1] - r[1])
        s1 = []
        s2 = []
        for x, y in sd:
            b_ = (x - p[0], y - p[1])
            c_ = (x - r[0], y - r[1])
            cro_b, cro_c = cross(b, b_), cross(c, c_)
            if cro_b <= 0 and cro_c <= 0:
                continue
            else:
                if cro_b > 0:
                    s1.append((x, y))
                elif cro_c > 0:
                    s2.append((x, y))
        quickhull(l, p, s1, k, il, i)
        quickhull(p, r, s2, k, i, ir)
    k.sort(key=lambda x: x[1])
    return tuple(zip(*k))[0]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def direction(l, r, p):
    a = r[1] - l[1]
    b = l[0] - r[0]
    return (a * (p[0] - l[0]) + b * (p[1] - l[1])) ** 2, a ** 2 + b ** 2

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

from collections import defaultdict

n, r = [int(x) for x in input().split()]
s = [[int(x) for x in input().split()] for i in range(n)]
f = defaultdict(int)
for i in range(n):
    x, y = s[i]
    f[(x, y)] = i
q = [[s[i][j] for j in range(2)] for i in range(n)]
q.sort()
v = []
for i in range(r):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    c = ((s[a][0] - s[b][0]) ** 2 + (s[a][1] - s[b][1]) ** 2) ** 0.5
    v.append((a, b, c))
v.sort(key=lambda x: x[2])
l = tuple(q.pop(0))
r = tuple(q.pop(-1))
lis = quickhull(l, r, q, [(l, 0), (r, n)], 0, n)
par = [i for i in range(n + 1)]
rank = [0] * (n + 1)
for p in lis:
    par[f[p]] = n
    rank[n] = 1
l = 0
for i in range(len(lis)):
    l += ((lis[i - 1][0] - lis[i][0]) ** 2 + (lis[i - 1][1] - lis[i][1]) ** 2) ** 0.5
for x, y, c in v:
    if root(x) != root(y):
        l += c
        unite(x, y)
print(l)