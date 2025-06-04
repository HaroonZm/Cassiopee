import sys

f = lambda x: sys.setrecursionlimit(x)
f(10**5)

def Q(a, b, c):
    if b[a] == []:
        return (2, [a])
    u = 1
    h = [a]
    for z in b[a]:
        q = Q(z, b, c)
        u = u * q[0]
        h = h + q[1]
    return (u + 1, h)

n, m = map(int, raw_input().split())
s = [[] for _ in '_'*n]
d = [~0]*n
for _ in '_'*m:
    x, y = map(int, raw_input().split())
    x -= 1; y -= 1
    d[x] = y
    s[y] += [x]

V = list(range(n))
B = []
while V:
    k = V[0]
    trail = [k]
    while True:
        if d[k] == ~0:
            r = k
            break
        if d[k] in trail:
            r = d[k]
            d[r] = ~0
            F = trail[trail.index(r):]
            ttt = []
            for j in F:
                for jj in s[j]:
                    if jj not in F:
                        d[jj] = r; ttt += [jj]
                if j != r:
                    if j in V: V.remove(j)
            s[r] = ttt[:]
            break
        k = d[k]
        trail += [k]
    p = Q(r, s, d)
    B += [p[0]]
    for x in p[1]:
        if x in V: V.remove(x)
from functools import reduce
print (reduce((lambda a, b: a*b), B) % 10**9+7)