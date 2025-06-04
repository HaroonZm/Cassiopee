import sys

class UnionFind:
    def __init__(self, n):
        # Initialisation d'un tableau parent pour union-find
        self.parent = list(range(n))
        self.rank = [0] * n  # Pour optimiser les unions
    
    def find(self, x):
        # Recherche récursive avec compression de chemin
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Union par rang entre deux composantes
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Ils sont déjà dans la même composante
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def can_build_spanning_tree(edges, n, start, end):
    """
    Teste si on peut construire un arbre couvrant avec des arêtes entre indices start et end inclus.
    On essaie de connecter tous les sommets en utilisant uniquement ces arêtes.
    """
    uf = UnionFind(n)
    count = 0  # Compte le nombre d'arêtes ajoutées
    for i in range(start, end + 1):
        a, b, _ = edges[i]
        if uf.union(a, b):
            count += 1
            if count == n - 1:  # Arbre couvrant complet
                return True
    return False

def find_min_slimness(n, edges):
    """
    Recherche la plus petite différence entre poids max et min d'un arbre couvrant.
    """
    edges.sort(key=lambda x: x[2])  # Tri par poids croissant
    
    m = len(edges)
    min_slimness = None
    
    # On essaie d'utiliser une approche deux pointeurs sur l'intervalle d'arêtes triées.
    # L'intervalle représente les arêtes dont les poids sont entre edges[i] et edges[j].
    j = 0
    for i in range(m):
        # Avance j pour trouver un intervalle où un arbre couvrant est possible
        while j < m and not can_build_spanning_tree(edges, n, i, j):
            j += 1
        if j == m:
            # Plus possible de trouver un intervalle à partir de i
            break
        # Si on peut construire un arbre couvrant entre i et j, on calcule la taille de l'intervalle de poids
        diff = edges[j][2] - edges[i][2]
        if min_slimness is None or diff < min_slimness:
            min_slimness = diff
    
    if min_slimness is None:
        return -1
    else:
        return min_slimness

def main():
    input = sys.stdin.readline
    while True:
        line = input().strip()
        if line == '':
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        
        edges = []
        for _ in range(m):
            a, b, w = map(int, input().split())
            # Stockage en indice 0-based
            edges.append((a - 1, b - 1, w))
        
        if n == 1:
            # Un seul sommet, pas d'arête, slimness = 0
            print(0)
            continue
        
        # Si pas assez d'arêtes pour un arbre couvrant
        if m < n - 1:
            print(-1)
            continue
        
        # Recherche de la plus petite slimness possible
        result = find_min_slimness(n, edges)
        print(result)

if __name__ == "__main__":
    main()