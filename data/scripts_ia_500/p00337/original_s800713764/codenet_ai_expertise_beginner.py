def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def direction(l, r, p):
    a = r[1] - l[1]
    b = l[0] - r[0]
    return (a * (p[0] - l[0]) + b * (p[1] - l[1]))**2, a**2 + b**2

def quickhull(l, r, s, k, il, ir):
    if len(s) == 0:
        return
    su = []
    sd = []
    a = (r[0] - l[0], r[1] - l[1])
    for point in s:
        x = point[0]
        y = point[1]
        b = (x - l[0], y - l[1])
        cro = cross(a, b)
        if cro > 0:
            su.append(point)
        elif cro < 0:
            sd.append(point)
    ind = (ir - il) / 2
    if len(su) > 0:
        c, d = direction(l, r, su[0])
        p = su[0]
        for i in range(1, len(su)):
            c_, d_ = direction(l, r, su[i])
            if c * d_ < c_ * d:
                c = c_
                d = d_
                p = su[i]
        i = ir + ind
        k.append((tuple(p), i))
        b = (l[0] - p[0], l[1] - p[1])
        c_ = (p[0] - r[0], p[1] - r[1])
        s1 = []
        s2 = []
        for point in su:
            x = point[0]
            y = point[1]
            b_ = (x - p[0], y - p[1])
            c__ = (x - r[0], y - r[1])
            cro_b = cross(b, b_)
            cro_c = cross(c_, c__)
            if cro_b >= 0 and cro_c >= 0:
                continue
            else:
                if cro_b < 0:
                    s1.append(point)
                elif cro_c < 0:
                    s2.append(point)
        quickhull(l, p, s1, k, il, i)
        quickhull(r, p, s2, k, ir, i)
    if len(sd) > 0:
        c, d = direction(l, r, sd[0])
        p = sd[0]
        for i in range(1, len(sd)):
            c_, d_ = direction(l, r, sd[i])
            if c * d_ < c_ * d:
                c = c_
                d = d_
                p = sd[i]
        i = il + ind
        k.append((tuple(p), i))
        b = (l[0] - p[0], l[1] - p[1])
        c_ = (p[0] - r[0], p[1] - r[1])
        s1 = []
        s2 = []
        for point in sd:
            x = point[0]
            y = point[1]
            b_ = (x - p[0], y - p[1])
            c__ = (x - r[0], y - r[1])
            cro_b = cross(b, b_)
            cro_c = cross(c_, c__)
            if cro_b <= 0 and cro_c <= 0:
                continue
            else:
                if cro_b > 0:
                    s1.append(point)
                elif cro_c > 0:
                    s2.append(point)
        quickhull(l, p, s1, k, il, i)
        quickhull(p, r, s2, k, i, ir)
    k.sort(key=lambda x: x[1])
    return tuple(zip(*k))[0]

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def unite(x, y):
    xroot = root(x)
    yroot = root(y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            par[xroot] = yroot
        else:
            par[yroot] = xroot
            if rank[xroot] == rank[yroot]:
                rank[xroot] += 1

from collections import defaultdict

n, r = map(int, input().split())
s = []
for _ in range(n):
    x, y = map(int, input().split())
    s.append([x, y])

f = defaultdict(int)
for i in range(n):
    x, y = s[i]
    f[(x, y)] = i

q = [point[:] for point in s]
q.sort()
v = []
for _ in range(r):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    dist = ((s[a][0] - s[b][0])**2 + (s[a][1] - s[b][1])**2)**0.5
    v.append((a, b, dist))

v.sort(key=lambda x: x[2])
l = tuple(q.pop(0))
rr = tuple(q.pop(-1))
lis = quickhull(l, rr, q, [(l, 0), (rr, n)], 0, n)

par = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for p in lis:
    par[f[p]] = n
    rank[n] = 1

length = 0
for i in range(len(lis)):
    x1, y1 = lis[i - 1]
    x2, y2 = lis[i]
    length += ((x1 - x2)**2 + (y1 - y2)**2)**0.5

for x, y, c in v:
    if root(x) != root(y):
        length += c
        unite(x, y)

print(length)