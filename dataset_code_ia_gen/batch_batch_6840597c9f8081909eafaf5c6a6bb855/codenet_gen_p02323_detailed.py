import sys

def tsp(V, E, edges):
    """
    Résout le problème du voyageur de commerce (TSP) sur un graphe orienté pondéré.

    Arguments:
    V -- nombre de sommets
    E -- nombre d'arêtes
    edges -- liste de triplets (s, t, d) représentant une arête de s vers t avec distance d

    Retour:
    La distance minimale d'un cycle hamiltonien, ou -1 s'il n'existe pas.
    """

    # Construire la matrice d'adjacence avec des poids infinis par défaut
    INF = float('inf')
    dist = [[INF]*V for _ in range(V)]
    for s, t, d in edges:
        dist[s][t] = d

    # Utilisation d'une programmation dynamique avec bitmask
    # dp[mask][i] représente la distance minimale pour visiter les sommets dans mask
    # et finir au sommet i
    # mask est un entier où chaque bit représente un sommet visité (1) ou non (0).
    dp = [[INF]*V for _ in range(1 << V)]
    
    # Initialisation: on commence le cycle à chaque sommet (choix arbitraire)
    # On peut choisir comme sommet de départ 0 (ex.); distance à 0
    # On impose le départ à 0 pour éviter les permutations redondantes
    start = 0
    dp[1 << start][start] = 0

    for mask in range(1 << V):
        for u in range(V):
            if dp[mask][u] == INF:
                continue
            # pour chaque sommet v non encore visité
            for v in range(V):
                if (mask & (1 << v)) == 0 and dist[u][v] != INF:
                    next_mask = mask | (1 << v)
                    new_dist = dp[mask][u] + dist[u][v]
                    if new_dist < dp[next_mask][v]:
                        dp[next_mask][v] = new_dist

    full_mask = (1 << V) - 1
    res = INF

    # Pour fermer le cycle, on doit revenir au point de départ
    for u in range(V):
        if dp[full_mask][u] != INF and dist[u][start] != INF:
            candidate = dp[full_mask][u] + dist[u][start]
            if candidate < res:
                res = candidate

    return res if res != INF else -1


if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]

    print(tsp(V, E, edges))