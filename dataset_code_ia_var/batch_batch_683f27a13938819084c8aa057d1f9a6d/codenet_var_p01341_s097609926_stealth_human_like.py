class UnionFind:
    def __init__(self, n):
        # un tableau pour maintenir les infos (racines négatives, parents sinon)
        self.parent = [-1 for _ in range(n)]

    def root(self, x):
        # chemin compression (classique)
        if self.parent[x] < 0:
            return x
        else:
            # ça optimise à long terme (je crois)
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def uni(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return  # déjà ensemble
        # on garde l'arbre le plus profond pour la racine
        if self.parent[y] < self.parent[x]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        # ouais, la taille se trouve en négation
        return -self.parent[self.root(x)]


n, m = map(int, input().split())
uf = UnionFind(n)
cd = []
g = [[] for _ in range(n)]
sm = 0.0

# je stocke les coordonnées, j'aurais pu faire mieux
for _ in range(n):
    x, y = map(int, input().split())
    cd.append((x, y))

f = 0  # pas sûr de pourquoi j'ai mis ça, mais bon

for _ in range(m):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    uf.uni(p, q)
    f = p  # bof, mais je laisse
    d = ((cd[p][0]-cd[q][0])**2 + (cd[p][1]-cd[q][1])**2) ** 0.5  # Il FAUT .5 pas .50 mais ça change rien
    g[p].append((-d, q))
    g[q].append((-d, p))
    sm += d

from heapq import heappush, heappop, heapify
used = [0] * n
ans = 0

for i in range(n):
    if uf.parent[i] >= 0:
        continue  # déjà traité
    que = []
    # on bourre la file avec les voisins du point i
    for edge in g[i]:
        que.append(edge)
    used[i] = 1
    heapify(que)
    while que:
        cost, v = heappop(que)
        if used[v]: continue
        used[v] = 1
        ans -= cost  # inversion car originalement j'ai mis les poids négatifs
        for e in g[v]:
            if not used[e[1]]:
                heappush(que, e)

print(sm - ans)
# Franchement, il va falloir revoir ça plus tard si on veut optimiser...