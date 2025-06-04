import sys
from heapq import heappop, heappush

r = sys.stdin.readline  # Shortcut to read a line from standard input

def g(n, E, S, G):
    """
    Utilise l'algorithme de Dijkstra pour trouver le coût minimal du chemin entre S (départ) et G (arrivée)
    dans un graphe pondéré avec 'n' sommets et 'E' comme liste d'adjacence.

    Paramètres :
        n (int) : nombre de sommets dans le graphe (indices de 0 à n-1)
        E (list) : liste d'adjacence, E[u] = liste de tuples (coût, voisin)
        S (int) : sommet de départ
        G (int) : sommet d'arrivée

    Retourne :
        int : coût minimal de S à G, ou -1 si pas de chemin
    """
    # Distance la plus courte connue vers chaque sommet ; initialisée à un grand nombre
    F = [1e7] * (n + 1)
    F[S] = 0  # Distance au sommet source est 0
    H = [(0, S)]  # File de priorité pour traiter les sommets (coût, sommet courant)

    while H:
        c, u = heappop(H)  # Sélection du sommet avec le coût le plus faible actuel
        if u == G:
            return c  # Atteint le sommet d'arrivée : retourne le coût minimal trouvé
        for f, v in E[u]:  # Parcours de tous les voisins
            t = c + f  # Calcul du coût pour atteindre le voisin
            if t < F[v]:
                F[v] = t  # Mise à jour si un chemin meilleur est trouvé
                heappush(H, (t, v))  # Ajoute le voisin à traiter
    return -1  # Aucun chemin trouvé entre S et G

def s():
    """
    Gère l'entrée standard pour construire dynamiquement le graphe et répondre aux requêtes.
    Lit une séquence d'instructions pour ajouter des arêtes ou demander des plus courts chemins,
    puis affiche les résultats selon les requêtes.
    - Une requête pour un chemin le fait avec une ligne commencant par '0' suivie de deux entiers S et G.
    - Une requête d'ajout d'arête commence par '1' suivie de trois entiers c, d, e (arête entre c et d de coût e).
    La lecture s'arrête à la ligne '0 0'.
    """

    for e in iter(r, '0 0\n'):  # Lecture des graphes jusqu'à la sentinelle '0 0'
        n, k = map(int, e.split())  # n = nombre de sommets, k = nombre d'instructions
        E = [[] for _ in range(n + 1)]  # Initialisation de la liste d'adjacence (1-indexé)
        for _ in range(k):
            f = r()
            if f[0] == '0':
                # Requête de plus court chemin : '0 S G'
                print(g(n, E, *map(int, f[2:].split())))
            else:
                # Ajout d'arête : '1 c d e' (arête non orientée entre c et d de coût e)
                c, d, e = map(int, f[2:].split())
                E[c].append((e, d))
                E[d].append((e, c))

s()