from functools import reduce
from operator import xor
import itertools

root = lambda x: (lambda f, x: f(f, x))(lambda self, x: x if par[x] == x else (par.__setitem__(x, self(self, par[x])), par[x])[1], x)

def unite(u, v):
    pu, pv = map(root, (u, v))
    mx, mn = max(pu, pv, key=lambda x: rank[x]), min(pu, pv, key=lambda x: rank[x])
    rank[mx] += int(rank[mx] == rank[mn])
    par[mn] = mx

def init(n):
    seq = [(a[2*i], a[2*i+1]) for i in range(s)]
    for idx, (c1, c2) in enumerate(seq):
        (c1 == c2 == "0" and par.__setitem__(s + idx, ss)) or (c1 == c2 == "1" and par.__setitem__(s + idx, ss + 1))
    for (i, j) in itertools.combinations(range(s), 2):
        seq[i] == seq[j] and unite(s+i, s+j)

def union(k):
    sk, ssk = 1 << k, 1 << k + 1
    arr = [(root(ssk+2*l), root(ssk+2*l+1)) for l in range(sk)]
    [unite(ssk+2*l, sk+l) for l in range(sk) if arr[l][0] == arr[l][1]]
    for (i, j) in itertools.combinations(range(sk), 2):
        arr[i] == arr[j] and root(i) != root(j) and unite(sk+i, sk+j)

n = int(input())
s = 1 << (n-1)
ss = 1 << n
par = list(range(ss)) + [ss, ss+1]
rank = [0] * (ss+2)
a = input()
init(n)
for k in range(n-2,-1,-1): union(k)
print(len(set(map(root, range(len(par))))) - 3)