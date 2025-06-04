# Solution Python utilisant l'algorithme de Prim pour trouver le Minimum Spanning Tree (MST)
# Le programme lit en entrée la taille du graphe et sa matrice d'adjacence, puis calcule la somme des poids
# des arêtes de l'arbre couvrant de poids minimum.

import sys

def prim_mst(n, graph):
    # Cette fonction implémente l'algorithme de Prim pour calculer le poids total du MST.
    # Arguments :
    # - n : nombre de sommets
    # - graph : matrice d'adjacence (n x n), où graph[i][j] est le poids de l'arête i-j ou -1 si aucune arête.

    # initialisation :
    # key[i] = poids minimum d'une arête connectant i à l'arbre déjà construit
    key = [float('inf')] * n
    # mstSet[i] indique si le sommet i est inclus dans le MST
    mstSet = [False] * n
    # on démarre par le sommet 0
    key[0] = 0
    # parent[i] mémorise le parent de i dans le MST (inutile ici, mais standard)
    parent = [-1] * n

    for _ in range(n):
        # Sélectionner le sommet u non encore inclus dans le MST qui a la clé minimale
        u = -1
        min_key = float('inf')
        for v in range(n):
            if not mstSet[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        # marquer u comme inclus dans le MST
        mstSet[u] = True

        # Mettre à jour les clés des sommets adjacents à u
        for v in range(n):
            # Il doit exister une arête u-v
            # v ne doit pas être dans le MST
            # le poids doit être inférieur à la clé actuelle de v
            if graph[u][v] != -1 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # la somme des poids des arêtes du MST est la somme des clés
    return sum(key)


def main():
    # lecture du nombre de sommets
    n = int(sys.stdin.readline().strip())
    graph = []
    for _ in range(n):
        line = sys.stdin.readline().strip().split()
        # conversion en entier
        row = list(map(int, line))
        graph.append(row)

    # calcul et affichage du poids total du MST
    total_weight = prim_mst(n, graph)
    print(total_weight)

if __name__ == "__main__":
    main()