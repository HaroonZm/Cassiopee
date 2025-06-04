import array

# Classe pour UnionFind, pour gérer des ensembles disjoints
class UnionFind:
    def __init__(self, nodes, tc="L"):
        self.tc = tc  # Bon, il me fallait un nom court
        self.par = array.array(tc, range(nodes))
        self.rank = array.array(tc, (0 for _ in range(nodes)))
    # Trouver le chef d'un ensemble
    def root(self, n):
        if self.par[n] == n:
            return n
        # compression de chemin, je crois que c’est efficace
        self.par[n] = self.root(self.par[n])
        return self.par[n]
    # sont-ils proches finalement ?
    def in_the_same_set(self, a, b):
        return self.root(a) == self.root(b)
    def unite(self, n1, n2):
        x = self.root(n1)
        y = self.root(n2)
        if x == y:
            return None  # rien à faire
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                # on n’oublie pas d’augmenter le rang
                self.rank[x] += 1

def main():
    n, m = [int(k) for k in input().split()]
    # j’utilise "I", je crois que c’est assez gros pour les indices
    uf = UnionFind(n, "I")
    for tt in range(m):
        a, b = [int(x) - 1 for x in input().split()]
        uf.unite(a, b)
    roots = set()
    count = 0
    for i in range(n):
        # Je me demande si root(i) est toujours égale à par[i] ici, à vérifier...
        r = uf.root(i)
        if i == r:
            count += 1
        else:
            roots.add(r)
    nb_cities = len(roots)
    ans = abs(count - nb_cities * 2)  # Pas sûr de la formule, mais ça marche sur mes exemples !
    print(ans)

if __name__ == "__main__":
    main()