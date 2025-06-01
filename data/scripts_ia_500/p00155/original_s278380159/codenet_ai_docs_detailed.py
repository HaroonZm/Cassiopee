import sys
from sys import stdin
from math import sqrt

# Use fast input method
input = stdin.readline

def dijkstra(s, G):
    """
    Applique l'algorithme de Dijkstra pour trouver le plus court chemin depuis un sommet s
    dans un graphe pondéré représenté par une matrice d'adjacence G.

    Args:
        s (int): Le sommet de départ.
        G (list of list of float): Matrice d'adjacence où G[u][v] est la distance entre u et v,
                                   ou float('inf') s'il n'y a pas de lien direct.

    Returns:
        tuple:
            d (list of float): Liste des distances minimales depuis s vers tous les sommets.
            p (list of int): Liste des prédecesseurs pour reconstruire les chemins les plus courts.
    """
    # Définition des états des sommets :
    # BLACK : sommet dont la distance minimale est définitivement connue
    # GRAY : sommet découvert mais pas encore définitivement traité
    # WHITE : sommet non découvert
    BLACK, GRAY, WHITE = 0, 1, 2

    # Initialisation des distances à l'infini, des couleurs à WHITE, et des prédecesseurs à -1
    d = [float('inf')] * 101
    color = [WHITE] * 101
    p = [-1] * 101

    d[s] = 0  # Distance du sommet source à lui-même vaut 0

    while True:
        mincost = float('inf')
        # Recherche du sommet u non encore définitivement traité avec la plus petite distance d[u]
        for i in range(101):
            if color[i] != BLACK and d[i] < mincost:
                mincost = d[i]
                u = i
        # Si tous les sommets restants sont inaccessibles (distance infini), on arrête
        if mincost == float('inf'):
            break

        color[u] = BLACK  # On marque u comme définitivement traité

        # Mise à jour des distances pour les voisins v de u non encore définitivement traités
        for v in range(101):
            if color[v] != BLACK and G[u][v] != float('inf'):
                # Calcul d'une nouvelle distance potentielle via u
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]  # Mise à jour de la distance minimale
                    p[v] = u  # u devient le prédecesseur de v
                    color[v] = GRAY  # v est désormais découvert

    return d, p

def main(args):
    """
    Fonction principale qui lit les données d'entrée, construit le graphe et répond
    aux requêtes de plus court chemin entre deux bus arrêts.

    Le graphe est formé en connectant uniquement les arrêts de bus de différents bus
    dont la distance euclidienne est inférieure ou égale à 50 unités.

    Args:
        args (list): Arguments en ligne de commande (non utilisés ici).
    """
    while True:
        n = int(input())  # Nombre de points d'arrêt
        if n == 0:
            break  # Fin du traitement si aucun arrêt

        # Initialisation de la matrice d'adjacence avec une taille fixe (101)
        G = [[float('inf')] * 101 for _ in range(101)]
        data = []

        # Lecture des informations des arrêts (bus, x, y)
        for _ in range(n):
            b, x, y = map(int, input().split())
            data.append([b, x, y])

        # Construction du graphe : on connecte uniquement des arrêts appartenant à des bus différents
        # si la distance euclidienne entre eux est <= 50
        for i in range(n):
            b1, x1, y1 = data[i]
            for j in range(n):
                b2, x2, y2 = data[j]
                if b1 == b2:
                    # Pas d'arête entre arrêts du même bus
                    continue
                dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if dist <= 50.0:
                    # On ajoute une arête bidirectionnelle dans le graphe
                    G[b1][b2] = dist
                    G[b2][b1] = dist

        m = int(input())  # Nombre de requêtes
        for _ in range(m):
            s, g = map(int, input().split())  # sommet source et sommet destination

            # Si source et destination sont identiques, on affiche simplement la source
            if s == g:
                print(s)
                continue

            # Vérification des bornes valides des sommets
            if (not 1 <= s <= 100) or (not 1 <= g <= 100):
                print('NA')
                continue

            # Calcul du plus court chemin avec Dijkstra
            d, p = dijkstra(s, G)

            # Si la distance est infinie, le chemin n'existe pas
            if d[g] == float('inf'):
                print('NA')
            else:
                # Reconstruction du chemin en remontant la liste des prédecesseurs
                path = [g]
                while p[g] != s:
                    path.append(p[g])
                    g = p[g]
                path.append(s)

                # Inversion du chemin pour avoir l'ordre source -> destination
                rev = path[::-1]
                print(' '.join(map(str, rev)))

def main2(args):
    """
    Fonction alternative (incomplète) ne réalisant pas de calcul de plus court chemin.
    Lit seulement les données et affiche toujours 'NA' pour les requêtes.
    """
    while True:
        n = int(input())
        if n == 0:
            break

        for _ in range(n):
            b, x, y = map(int, input().split())

        m = int(input())
        for _ in range(m):
            s, g = map(int, input().split())
            print('NA')

if __name__ == '__main__':
    main(sys.argv[1:])