# Bon, une classe UnionFind (structure disjoint set). Attention, indices à partir de 0.
class UnionFind:
    def __init__(self, n):
        self.size_total = n  # doit-on vraiment stocker n? On verra...
        self.parents = [-1 for _ in range(n)]

    def find(self, x):
        # Trouve le "leader" (la racine ?) du groupe de x
        if self.parents[x] < 0:
            return x
        # Un peu magique mais ça marche pour compresser le chemin:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        # Fusionne les ensembles contenant x et y...
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return  # déja unis, rien à faire
        # Petite convention, on garde celui avec le plus petit index (pourquoi pas?)
        if self.parents[x_root] > self.parents[y_root]:
            # swap x_root et y_root
            x_root, y_root = y_root, x_root
        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root

    def size(self, x):
        # Nombre d'éléments dans le groupe de x
        return -self.parents[self.find(x)]

    def same(self, x, y):
        # Vérifie si x et y sont dans le même "groupe"
        return self.find(x) == self.find(y)

# Lecture des données
N, M = map(int, input().split())
uf = UnionFind(N)

# Je crois qu'on n’utilise pas z, mais je le lis quand même par sécurité
for _ in range(M):
    a, b, z = map(int, input().split())
    uf.unite(a-1, b-1)  # je suppose que les entrées sont base-1

# Pour chaque élément on trouve la racine (c’est lent ? pas trop normalement).
# Y'a sûrement plus propre mais tant pis.
liste_racines = []
for idx in range(N):
    leader = uf.find(idx)
    liste_racines.append(leader)

# Pour compter les groupes, on fait un set (c’est facile).
diff_roots = set(liste_racines)

# Affichage du nombre de groupes "magiques"
print(len(diff_roots))