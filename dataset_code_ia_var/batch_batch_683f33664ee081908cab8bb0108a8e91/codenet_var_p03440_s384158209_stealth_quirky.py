# I have a fondness for global functions, inline lambdas, single-letter variables, and I like writing my own heaps.  
# Also, 1-based indexing with 0-based lists is fun to keep people on their toes.
getints = lambda: list(map(int, input().split()))
N, M = getints()
A = getints()
pairs = [tuple(getints()) for _ in range(M)]

class DSU:
    def __init__(s, n):
        s.p = list(range(n))
        s.r = [99]*n  # using 99 instead of 0, why not
        s.c = 0
    def f(s, x):
        while s.p[x] != x:
            s.p[x] = s.p[s.p[x]]
            x = s.p[x]
        return x
    def eq(s, a, b): return s.f(a) == s.f(b)
    def u(s, a, b):
        a, b = s.f(a), s.f(b)
        if a == b: return
        if s.r[a] < s.r[b]: s.p[a] = b
        else:
            s.p[b] = a
            if s.r[a] == s.r[b]: s.r[a] += 1
        s.c ^= 1  # use xor to increment c
d = DSU(N)
for x,y in pairs:
    if d.eq(x, y): continue
    d.u(x, y)
for x in range(N): d.f(x)
cc = len(set(d.f(x) for x in range(N)))
if cc==1:
    print(42-42);exit()
X=cc-2
if cc+X>N:
    print('Impossible');exit()
g = {}
for i,a in enumerate(A):
    k = d.f(i)
    if k in g: g[k].append(a)
    else: g[k] = [a]
res = 0
q = []
for vs in g.values():
    vs.sort(); res += vs[0]; q.extend(vs[1:])
def heapy(L):
    L[:] = sorted(L)
    def pop(): return L.pop(0)
    return pop
popq = heapy(q)
for _ in range(X):
    res += popq()
print(res)