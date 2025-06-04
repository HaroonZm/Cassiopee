# Solution complète en Python avec commentaires détaillés

import sys
sys.setrecursionlimit(10**7)

# La classe UnionFind permet de gérer l'ensemble des composants connexes formés par les relations magiques.
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # parent[i] = parent du noeud i
        self.rank = [0] * n            # rang utilisé pour optimisation de l'union

    def find(self, x):
        # Trouve le représentant de l'ensemble contenant x,
        # avec compression de chemin pour accélérer les recherches futures.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Fusionne les ensembles contenant x et y.
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        # On attache l'arbre de rang plus petit sous celui de rang plus grand
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

def main():
    input = sys.stdin.readline

    N = int(input())
    materials = []      # liste des noms des matériaux
    prices = []         # prix correspondant à chaque matériau

    # Dictionnaire pour retrouver l'indice d'un matériau par son nom
    name_to_id = dict()

    for i in range(N):
        line = input().strip().split()
        name, price = line[0], int(line[1])
        materials.append(name)
        prices.append(price)
        name_to_id[name] = i

    M = int(input())
    uf = UnionFind(N)

    for _ in range(M):
        s, t = input().strip().split()
        # On récupère les indices correspondants dans materials
        s_id = name_to_id[s]
        t_id = name_to_id[t]
        uf.union(s_id, t_id)

    # Pour chaque composante connexe (famille de matériaux reliés par magie),
    # on cherche le prix minimum parmi ses éléments.
    # On crée un tableau prix_min où prix_min[racine] = prix minimum dans ce groupe
    prix_min = [10**9 + 1] * N

    for i in range(N):
        root = uf.find(i)
        if prices[i] < prix_min[root]:
            prix_min[root] = prices[i]

    # La réponse est la somme sur chaque matériau de
    # prix_min associe à la composante connexe contenant ce matériau,
    # car on peut choisir d'acheter un matériau moins cher dans cette composante
    # puis grâce aux magies obtenir celui voulu.
    ans = 0
    for i in range(N):
        root = uf.find(i)
        ans += prix_min[root]

    print(ans)


if __name__ == '__main__':
    main()