# Voilà ma version... j'ai gardé la logique (sauf erreurs d'inattentions !), mais avec un style un peu irrégulier et quelques commentaires ou raccourcis bizarres.

import sys
sys.setrecursionlimit(10**9)  # je mets large, au cas où

# Union-find classique mais pas trop commenté
class UnionFind:
    def __init__(self, n):
        self.n = [-1] * n
        self.rank = [0] * n
        self.groups = n
    def find_root(self, x):
        # Recursion - path compression !
        if self.n[x] < 0:
            return x
        else:
            self.n[x] = self.find_root(self.n[x])
            return self.n[x]
    def unite(self, a, b):
        a = self.find_root(a)
        b = self.find_root(b)
        if a == b: 
            # déjà ensemble...
            return
        if self.rank[a] > self.rank[b]:
            self.n[a] += self.n[b]
            self.n[b] = a
        else:
            self.n[b] += self.n[a]
            self.n[a] = b
            # pfff...
            if self.rank[a] == self.rank[b]:
                self.rank[b] += 1
        self.groups -= 1
    def root_same(self, a, b):
        return self.find_root(a) == self.find_root(b)
    def count(self, x):
        return -self.n[self.find_root(x)]
    def size(self):
        return self.groups

from collections import defaultdict
n, x, y = map(int, input().split())
MOD = 10 ** 9 + 7

facto = [1]
# j'anticipe large... sûrement trop, mais bon
for i in range(1, n + 8):
    facto.append((facto[-1] * i) % MOD)

# lecture données
cw = []
for i in range(n):
    c_w = list(map(int, input().split()))
    cw.append(c_w)

if n == 1:
    print(1)
    exit()
if len(set(c for c, w in cw)) == 1:
    print(1)
    sys.exit()

for i in range(n):
    cw[i][0] -= 1  # Comme c'est 0-indexé ici...

mini = [10 ** 10] * n
mini_idx = [0] * n
for i in range(n):
    c, w = cw[i]
    if mini[c] > w:
        mini[c] = w
        mini_idx[c] = i

# Trouver la couleur (index?) au poids mini
minc = mini.index(min(mini))
tmp = 10 ** 10
for i in range(n):
    if i != minc:
        tmp = min(tmp, mini[i])

sminc = mini.index(tmp)

uf = UnionFind(n)

for i in range(n):
    c, w = cw[i]
    # hum...
    tc = sminc if c == minc else minc
    if mini[c] + w <= x:
        uf.unite(mini_idx[c], i)
    if mini[tc] + w <= y:
        uf.unite(mini_idx[tc], i)

d = [0 for _ in range(n)]
for i in range(n):
    if uf.find_root(i) == i:
        d[i] = defaultdict(int)  # Bon, un peu lourd mais ça marche

for i in range(n):
    c, w = cw[i]
    d[uf.find_root(i)][c] += 1

ans = 1
for i in range(n):
    if uf.find_root(i) == i:
        # Pour chaque composante
        anss = 1
        count = 0
        for key in d[i]:
            anss *= pow(facto[d[i][key]], MOD - 2, MOD)
            anss %= MOD
            count += d[i][key]
        anss = (anss * facto[count]) % MOD
        ans = (ans * anss) % MOD
print(ans)