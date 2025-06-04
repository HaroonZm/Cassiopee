from heapq import heappop, heappush
import sys

# Alias for fast input reading
r = sys.stdin.readline

def g(n, E, S, G):
    """
    Trouve le chemin le plus court entre le sommet S et G dans un graphe pondéré en utilisant Dijkstra.

    Args:
        n (int): Nombre de sommets dans le graphe.
        E (List[List[List[int, int]]]): Liste d'adjacence représentant le graphe. Chaque E[u] est une liste de (poids, voisin).
        S (int): Indice du sommet de départ.
        G (int): Indice du sommet d'arrivée (goal).

    Returns:
        int: Le coût du chemin le plus court de S à G, ou -1 si aucun chemin n'existe.
    """
    # Initialisation: coût infini pour tous les sommets sauf le départ
    F = [1e7] * (n + 1)
    F[S] = 0
    # File de priorité pour Dijkstra: (coût actuel, sommet)
    H = [(0, S)]
    while H:
        c, u = heappop(H)
        if u == G:
            return c  # Chemin trouvé, on retourne son coût
        # Parcours des voisins de u
        for f, v in E[u]:
            t = c + f  # Nouveau coût potentiel
            if t < F[v]:  # Si meilleur chemin trouvé
                F[v] = t
                heappush(H, (t, v))
    return -1  # Aucun chemin trouvé

def s(n, k):
    """
    Traite une séquence d'opérations sur un graphe à n sommets, avec k requêtes.
    Les requêtes modifient le graphe ou demandent le chemin le plus court.

    Args:
        n (int): Nombre de sommets dans le graphe.
        k (int): Nombre de requêtes à traiter.

    Operation:
        - Si une ligne commence par '0', c'est une requête de plus court chemin: '0 S G'
        - Sinon, c'est une arête à ajouter: '1 u v w' (arête entre u et v de poids w, non orientée)

    Effet de bord: écrit sur stdout les résultats des requêtes de chemin le plus court.
    """
    # Initialisation: liste d'adjacence vide pour chaque sommet (indice 0 à n)
    E = [[] for _ in range(n + 1)]
    for _ in range(k):
        f = r()
        if f[0] == '0':
            # Requête de plus court chemin
            S, G = map(int, f[2:].split())
            print(g(n, E, S, G))
        else:
            # Ajout d'une nouvelle arête non orientée
            c = list(map(int, f[2:].split()))  # c = [u, v, w]
            # On ajoute dans les deux sens car le graphe est non orienté
            E[c[0]].append([c[2], c[1]])
            E[c[1]].append([c[2], c[0]])

# Boucle principale: traite chaque test fourni jusqu'à '0 0'
# Chaque test: ligne 'n k' -> n sommets, k requêtes
for e in iter(r, '0 0\n'):
    s(*map(int, e.split()))