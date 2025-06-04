import sys
sys.setrecursionlimit(10**7)

class UnionFind:
    """
    Structure de données Union-Find pour gérer des ensembles disjoints.
    Permet de regrouper des indices de lignes de convoyeurs qui sont connectées
    via des bras robotiques. Chaque ensemble représente un groupe de lignes
    entre lesquelles les marchandises peuvent être échangées.
    """
    def __init__(self, n):
        # Initialisation avec chaque élément dans son propre ensemble
        self.parent = list(range(n))
        self.size = [1] * n  # Taille de chaque ensemble

    def find(self, a):
        # Trouve le représentant (parent) de l'ensemble contenant 'a',
        # avec compression de chemin pour accélérer les futures recherches
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a, b):
        # Fusionne les ensembles contenant 'a' et 'b'
        a = self.find(a)
        b = self.find(b)
        if a != b:
            # On attache le plus petit arbre au plus grand pour équilibrer
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

def main():
    # Lecture des entrées
    n, m = map(int, sys.stdin.readline().split())
    arms = []
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        # On note y-1 car on veut des indices 0-based pour nos structures
        arms.append((x, y-1))

    # On doit relier les lignes adjacentes connectées via un bras robotique
    # Peu importe la position x car le robot permet un passage entre ces lignes.
    # On peut donc simplement faire l'union des indices y_i et y_i+1
    uf = UnionFind(n)

    for x, y in arms:
        # Relie les lignes y et y+1
        uf.union(y, y+1)

    # Pour chaque ligne, on cherche la taille de son ensemble,
    # c'est-à-dire combien de lignes sont connectées
    result = [0] * n
    for i in range(n):
        root = uf.find(i)
        result[i] = uf.size[root]

    # Affichage du résultat
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()