(n, m, *b), a, *q = [map(int, t.split()) for t in open(0)]

t = [-1] * n

def r(x):
    while -1 < t[x]:
        x = t[x]
    return x

def u(x):
    x, y = map(r, x)
    if x != y:
        if t[x] > t[y]:
            x, y = y, x
        t[x] += t[y]
        t[y] = x

[*map(u, q)]

i = c = 0
k = j = (n + ~m) << 1
*d, = eval('[],' * n)
for v in a:
    d[r(i)] += v,
    i += 1
for p in d:
    x, *y = sorted(p) + [0]
    c += x
    b += y[:-1]
    j -= p > []
print((c + sum(sorted(b)[:j]), 'Impossible')[k > n] * (k > 0))