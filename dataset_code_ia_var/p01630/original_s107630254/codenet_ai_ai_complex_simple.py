from functools import reduce
from operator import mul

def root(x):
    return [lambda: x, lambda: root(par[x])][x != par[x]]()

def unite(x, y):
    xp, yp = map(lambda t: reduce(lambda v, _: root(v), range(1), t), (x, y))
    c = (rank[xp] < rank[yp])
    par[xp if c else yp] = yp if c else xp
    (lambda arr, i, cond: cond and arr.__setitem__(i, arr[i] + 1))(rank, xp, rank[xp] == rank[yp] and not c)

n = int(input())
par = (lambda f, rng: list(map(f, rng)) + [-2, -1])(lambda i: i, range(2**n))
rank = list(map(int, [0]*((2**n)+2)))
a = input()
x = [None]*2**(n-1)

for i, v in enumerate(range(2**(n-1))):
    x[i] = (a[2*i], a[2*i+1])
    ((lambda s, idx, val: par.__setitem__(idx, val)) if x[i][0] == x[i][1] and x[i][0] == "0" else lambda *a: None)(par, 2**(n-1)+i, -1)
    ((lambda s, idx, val: par.__setitem__(idx, val)) if x[i][0] == x[i][1] and x[i][0] == "1" else lambda *a: None)(par, 2**(n-1)+i, -2)

for i in range(2**(n-1)):
    for k in range(i+1, 2**(n-1)):
        [lambda: None, lambda: unite(2**(n-1)+i, 2**(n-1)+k)][x[i]==x[k]]()

for k in range(n-2, -1, -1):
    x = [None]*(2**k)
    for l in range(2**k):
        x[l] = (root(2**(k+1)+2*l), root(2**(k+1)+2*l+1))
        [lambda: None, lambda: unite(2**(k+1)+2*l, 2**k+l)][x[l][0]==x[l][1]]()
    list(map(lambda ij: [lambda: None, lambda: unite(2**(k)+ij[0], 2**(k)+ij[1])][x[ij[0]]==x[ij[1]] and ij[0]!=ij[1]](),
        filter(lambda ij: ij[0]!=ij[1], ((i, l) for i in range(2**k) for l in range(2**k)))))

p = set(par)
for t in (-1, -2):
    try:
        p.remove(t)
    except KeyError:
        pass
print(max(len(p)-1, 0))