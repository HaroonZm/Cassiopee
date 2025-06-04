"""
Shopping in JOI Kingdom
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0562

Ce script résout le problème du plus long temps nécessaire pour atteindre un magasin,
en parcourant une carte de royaumes avec des routes, en tenant compte des routes gratuites
entre centres commerciaux (malls).
"""

import sys
from heapq import heappush, heappop
from itertools import combinations

def dijkstra(adj, start):
    """
    Exécute l'algorithme de Dijkstra pour trouver les plus courts chemins à partir d'un sommet source.

    Args:
        adj (List[List[Tuple[int, int]]]): Liste d'adjacence du graphe, chaque élément est une liste de tuples (voisin, coût).
        start (int): Sommet source à partir duquel calculer les distances.

    Returns:
        List[float]: Liste des distances minimales depuis 'start' vers chaque sommet.
    """
    # États de traitement des sommets
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * len(adj)             # Blanc: non visité, Gris: dans la file, Noir: traité
    dist = [float('inf')] * len(adj)       # Distance minimale du sommet de départ
    dist[start] = 0
    pq = []
    heappush(pq, (0, start))               # Initialisation de la file de priorité (distance, sommet)

    while pq:
        cost_u, u = heappop(pq)            # Récupère le sommet avec la distance minimale
        color[u] = BLACK
        if dist[u] < cost_u:
            continue                       # Ignore les chemins sous-optimaux
        for v, cost_uv in adj[u]:
            if color[v] == BLACK:
                continue                   # Ignore déjà traité
            if dist[v] > dist[u] + cost_uv:
                dist[v] = dist[u] + cost_uv
                heappush(pq, (dist[v], v))
                color[v] = GRAY
    return dist

def solve(adj, malls, n):
    """
    Calcule le temps nécessaire pour atteindre le magasin le plus éloigné,
    en tenant compte des routes gratuites entre tous les pairs de centres commerciaux.

    Args:
        adj (List[List[Tuple[int, int]]]): Liste d'adjacence du graphe.
        malls (List[int]): Liste des indices des centres commerciaux.
        n (int): Nombre de sommets du graphe.

    Returns:
        int: Le temps minimal maximal nécessaire pour atteindre tous les magasins, arrondi correctement.
    """
    # Calcule les distances du mall de départ (premier de la liste) vers tous les sommets.
    distance = dijkstra(adj, malls[0])

    # Pour chaque sommet, calcule la contrainte maximale imposée par ses voisins
    # La formule suivante, ajustée par le problème, représente la solution exacte attendue.
    ans = []
    for node_index, node_distance in enumerate(distance[1:], start=1):
        # Pour chaque arc (node_index, voisin), calcule un certain coût,
        # correspondant à la logique du problème.
        max_value = max(
            (
                (node_distance + cost + distance[neighbor]) / 2
                for neighbor, cost in adj[node_index]
            ),
            default=0  # Par sécurité, si un sommet sans voisins
        )
        ans.append(max_value)

    # Retourne le maximum des valeurs arrondi à l'entier le plus proche.
    return int(max(ans) + 0.5)

def main(args):
    """
    Fonction principale qui lit les entrées, construit le graphe, ajoute les routes gratuites,
    puis affiche le résultat du calcul du temps minimum maximal pour visiter les magasins.

    Args:
        args (List[str]): Liste des arguments de la ligne de commande (non utilisée ici).
    """
    # Lecture du nombre de villes, de routes et de centres commerciaux
    n, m, k = map(int, input().split())
    # Prépare la liste d'adjacence (n+1 pour l'indexation 1-based)
    adj = [[] for _ in range(n+1)]

    # Lecture des routes ordinaires du graphe
    for _ in range(m):
        f, t, c = map(int, input().split())
        adj[f].append((t, c))
        adj[t].append((f, c))

    # Lecture des indices des malls
    malls = [int(input()) for _ in range(k)]

    # Ajout des routes gratuites (coût nul) entre tous les pairs de malls
    for f, t in combinations(malls, 2):
        adj[f].append((t, 0))
        adj[t].append((f, 0))

    # Calcule et affiche la réponse
    ans = solve(adj, malls, n)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])