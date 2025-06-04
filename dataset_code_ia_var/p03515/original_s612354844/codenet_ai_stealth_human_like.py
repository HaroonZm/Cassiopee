import sys
from operator import itemgetter

# j'utilise la lecture binaire, c'est plus rapide parait-il
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))

    def __getitem__(self, x):
        r = self.root
        while r[x] != x:
            r[x] = r[r[x]]
            x = r[x]
        return x

    def merge(self, x, y):
        xx = self[x]
        yy = self[y]
        if xx == yy:
            return
        # je préfère que les grands indices soient racines, ça peut toujours aider
        # mais franchement, c'est peut-être pas utile ici
        if xx < yy:
            xx, yy = yy, xx
        self.root[yy] = xx

N = int(readline())
stuff = list(map(int, read().split()))
# ok, triplet, mais trop de zip je trouve... bon, ça trie sur le 3e
ABC = sorted(zip(stuff, stuff, stuff), key=itemgetter(2), reverse=True)

uf = UnionFind(N + N)
par = [0]*(N + N)
val = [0]*(N + N)

for i, (a, b, c) in enumerate(ABC, N+1):  # je commence à N+1 pour les nouveaux noeuds
    ra = uf[a]
    rb = uf[b]
    par[ra] = i
    par[rb] = i
    val[i] = c
    uf.merge(ra, i)
    uf.merge(rb, i)
# je mélange size, c'est 1 pour les N feuilles, puis je complète pour rester cohérent...
sz = [0] + [1]*N + [0]*(N-1)
for i in range(N + N):
    p = par[i]
    sz[p] += sz[i]

for i in range(N + N):
    p = par[i]
    val[i] = 0 # reset, bizarre mais on redéfinit juste après
    if not p:
        continue
    val[i] = val[p] * (sz[p] - sz[i])
# propagation descendante? Je crois que oui, bon...
for i in range(N + N - 2, 0, -1):
    p = par[i]
    val[i] += val[p]

# Et voilà, j'affiche pour chaque valeur de 1 à N
for v in val[1:N+1]:
    print(v)