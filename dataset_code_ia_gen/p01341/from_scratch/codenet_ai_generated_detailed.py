import sys
import math
sys.setrecursionlimit(10**7)

def main():
    # Lecture de N (piles) et M (clôtures)
    N, M = map(int, sys.stdin.readline().split())
    piles = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    fences = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # Calcul des longueurs des clôtures et stockage des arêtes
    # p_j et q_j sont les indices 1-based, on corrige en 0-based
    edges = []
    for p, q in fences:
        x1, y1 = piles[p-1]
        x2, y2 = piles[q-1]
        length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        edges.append((p-1, q-1, length))

    # Le problème consiste à détruire un ensemble minimal d'arêtes pour que tous les chats
    # soient sauvés. Les chats sont enfermés dans des faces formées par les clôtures.
    # En détruisant les clôtures d'une forêt couvrant tous les sommets (ou plutôt un
    # ensemble d'arêtes qui connecte tous les sommets dans l'ensemble), on minimise la
    # quantité d'eau nécessaire.
    #
    # L'aire minimale de clôtures à détruire correspond à l'ensemble d'arêtes à enlever
    # telle que le graphe devienne un arbre couvrant minimum sur chaque composant.
    #
    # Ici, la somme des longueurs des clôtures totales moins la somme des longueurs du
    # arbre couvrant minimum donne la longueur minimale à détruire (car toutes les bouts
    # entre piles restent sauf celles de l'arbre couvrant).
    #
    # Alternativement, la quantité minimale d'eau est égale à la somme des longueurs des
    # clôtures qui ne figurent pas dans l'arbre couvrant minimum.
    #
    # Donc :
    # sum_all_fences_length - sum_mst_length = sum_necessary_fences_to_destroy
    #
    # On peut donc calculer l'arbre couvrant minimum et soustraire.
    
    # Calcul de la somme totale des longueurs des clôtures
    total_length = sum(edge[2] for edge in edges)

    # Utilisation de l'algorithme de Kruskal pour trouver l'arbre couvrant minimum (MST)
    parent = list(range(N))
    rank = [0] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
        return True

    # Trier les arêtes par longueur croissante
    edges.sort(key=lambda x: x[2])

    mst_length = 0.0
    # Construire MST en ajoutant autant d'arêtes que possible sans créer de cycle
    for u, v, length in edges:
        if union(u, v):
            mst_length += length

    # Le montant minimal d'eau nécessaire est la somme des longueurs hors MST
    min_holy_water = total_length - mst_length

    # Affichage avec précision demandée (erreur absolue <= 0.001)
    print(f"{min_holy_water:.3f}")

if __name__ == "__main__":
    main()