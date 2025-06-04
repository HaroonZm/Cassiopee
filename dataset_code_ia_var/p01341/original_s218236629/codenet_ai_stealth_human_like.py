import math

def dist(pointA, pointB):
    # Calcul basique de distance euclidienne, rien de bien sorcier ici
    dx = pointA[0] - pointB[0]
    dy = pointA[1] - pointB[1]
    return math.sqrt(dx * dx + dy * dy) # j'ai préféré utiliser math.sqrt (c'est plus explicite je trouve)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # j’utilise une liste ici
        self.rank = [0]*n # ranks inutiles au début

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a]) # compression de chemin
        return self.parent[a]

    def unite(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return # déjà ensemble, on fait rien
        # On attache le plus petit au plus grand (c'est ce que j'ai compris du tuto)
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootX] += 1 # on augmente le rang, classique

    def same(self, x, y):
        return self.find(x) == self.find(y) # si racine commune

def kruskal(edgeList, num_nodes):
    uf = UnionFind(num_nodes)
    # On trie les arêtes mais du plus grand au plus petit, c'est fait exprès pour l'exo
    edgeList.sort(key=lambda tup: tup[2], reverse=True)
    total = 0 # On commence à zéro hein
    for e in edgeList:
        a, b, w = e
        if not uf.same(a, b):
            uf.unite(a, b)
            total += w
    return total

# --------- Entrée / sortie --------
# J'aurais pu mettre tout ça dans un main() mais bon.

N, M = map(int, input().split())
coords = []
for j in range(N):
    part = input().split()
    coords.append((int(part[0]), int(part[1])))  # tuple(x, y)

edges = []
for _ in range(M):
    s = list(map(int, input().split()))
    # indexation à partir de zéro sinon ça foire complètement
    p = s[0] - 1
    q = s[1] - 1
    d = dist(coords[p], coords[q])
    edges.append((p, q, d)) # (from, to, weight)

res = 0.0
for x in edges:
    res += x[2]
print(res - kruskal(edges, N))  # Résultat final ; espérons que ça marche