from heapq import heappop, heappush
import sys

# Shortcut to read a line from stdin efficiently
r = sys.stdin.readline

def g(n, E, S, G):
    """
    Implémente l'algorithme de Dijkstra pour trouver le plus court chemin entre S et G.

    Args:
        n (int): Nombre de sommets dans le graphe.
        E (list): Liste d'adjacence où E[u] est la liste des voisins (coût, sommet) de u.
        S (int): Sommet source.
        G (int): Sommet destination.

    Returns:
        int: Le coût du plus court chemin de S à G, ou -1 si G n'est pas accessible depuis S.
    """
    # Initialiser les distances à l'infini et la distance du sommet source à 0
    F = [1e7] * (n + 1)
    F[S] = 0
    # File de priorité (min-heap) contenant des tuples (coût total, sommet)
    H = [(0, S)]
    
    # Boucle principale de Dijkstra
    while H:
        c, u = heappop(H)  # Extraire le sommet au coût minimum
        # Si on atteint la destination, retourner le coût associé
        if u == G:
            return c
        # Explorer les voisins du sommet courant
        for f, v in E[u]:
            t = c + f  # Nouveau coût si on passe par u
            if t < F[v]:
                F[v] = t
                heappush(H, (t, v))  # Ajouter/mettre à jour le voisin avec le meilleur coût
    # Si le sommet destination n'a pas été atteint, retourner -1
    return -1

def s(n, k):
    """
    Traite une série d'opérations dynamiquement sur le graphe.

    Args:
        n (int): Nombre de sommets dans le graphe.
        k (int): Nombre d'opérations à effectuer.

    Pour chaque opération :
        - Si l'entrée commence par '1', ajoute une arête pondérée non orientée.
        - Si l'entrée commence par '0', effectue une requête de plus court chemin.
    """
    # Initialisation de la liste d'adjacence pour chaque sommet
    E = [[] for _ in range(n + 1)]
    for _ in range(k):
        f = r()  # Lire l'opération suivante
        p = map(int, f[2:].split())  # Extraire les paramètres de l'opération après le type
        if f[0] == '0':
            # Opération de requête de plus court chemin : '0 S G'
            print(g(n, E, *p))
        else:
            # Opération d'ajout d'arête : '1 c d e'
            c, d, e = p
            # Ajouter l'arête dans les deux sens (arête non orientée)
            E[c].append((e, d))
            E[d].append((e, c))

# Boucle principale : pour chaque composante du graphe
# La saisie commence par une ligne 'n k' qui indique le nombre de sommets et d'opérations
# et se termine avec la ligne '0 0'
for e in iter(r, '0 0\n'):
    s(*map(int, e.split()))