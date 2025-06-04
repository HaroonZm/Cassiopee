# Solution utilisant l'algorithme de Kruskal pour trouver l'arbre couvrant de poids minimum (MST).
# Kruskal trie les arêtes par poids croissant et les ajoute une par une en s'assurant de ne pas créer de cycle,
# en utilisant une structure Union-Find (disjoint set) pour vérifier rapidement les cycles.

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        # Initialise la structure Union-Find avec chaque noeud comme parent de lui-même
        self.parent = list(range(n))
        self.rank = [0] * n  # Utilisé pour optimisation par rang
    
    def find(self, x):
        # Trouve le représentant (parent) de l'ensemble contenant x avec compression de chemin
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Fusionne les ensembles contenant x et y, retourne True si fusion effectuée, False sinon
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        # Attacher l'arbre de rang plus petit sous celui de rang plus grand
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def main():
    # Lecture du nombre de sommets V et d'arêtes E
    V, E = map(int, input().split())
    edges = []
    
    # Lecture des arêtes
    for _ in range(E):
        s, t, w = map(int, input().split())
        edges.append((w, s, t))
    
    # Trie les arêtes par poids croissant
    edges.sort(key=lambda x: x[0])
    
    uf = UnionFind(V)
    mst_weight_sum = 0
    edges_used = 0
    
    # Parcours en ordre croissant des arêtes pour construire MST
    for w, s, t in edges:
        if uf.union(s, t):  # Si l'ajout ne forme pas de cycle
            mst_weight_sum += w
            edges_used += 1
            # Dès qu'on a V-1 arêtes dans l'arbre, on peut arrêter
            if edges_used == V - 1:
                break
    
    print(mst_weight_sum)

if __name__ == "__main__":
    main()