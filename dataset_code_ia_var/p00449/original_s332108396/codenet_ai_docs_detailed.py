from heapq import heappop, heappush
import sys

# Shortcut for reading lines from standard input
r = sys.stdin.readline

def g(n, E, S, G):
    """
    Calcule le coût minimal pour aller du sommet S au sommet G dans un graphe non orienté pondéré en utilisant l'algorithme de Dijkstra.

    Args:
        n (int): Nombre de sommets dans le graphe.
        E (list): Liste d'adjacence où E[u] contient la liste des tuples (poids, voisin) pour chaque sommet u.
        S (int): Sommet source.
        G (int): Sommet destination.

    Returns:
        int: Coût minimal pour aller de S à G. Retourne -1 si G est inatteignable depuis S.
    """
    # Initialisation du tableau des distances à l'infini et de la distance à la source à 0
    F = [1e7] * (n + 1)
    F[S] = 0
    # Initialisation de la file de priorité avec le sommet source
    H = [(0, S)]
    while H:
        # Récupère le sommet avec la plus petite distance actuelle
        c, u = heappop(H)
        # Si on atteint la destination, on retourne son coût d'accès minimal
        if u == G:
            return c
        # Parcours des voisins du sommet courant
        for f, v in E[u]:
            # Si un chemin plus court vers v est trouvé via u, on le met à jour
            if c + f < F[v]:
                F[v] = c + f
                heappush(H, (F[v], v))
    # Si G est inatteignable, retourne -1
    return -1

def s(n, k):
    """
    Traite k commandes pour construire le graphe et effectuer des requêtes de coût entre deux sommets.

    Args:
        n (int): Nombre de sommets dans le graphe.
        k (int): Nombre de commandes à traiter.

    Cette fonction lit k lignes à partir de l'entrée standard.
    Si la ligne commence par '0', il s'agit d'une requête de distance entre deux sommets.
    Sinon, il s'agit de l'ajout d'une arête non orientée dans le graphe.
    """
    # Initialisation de la liste d'adjacence pour chaque sommet
    E = [[] for _ in range(n + 1)]
    for _ in range(k):
        # Lecture d'une commande
        f = r()
        # Extraction des paramètres sous forme d'entiers
        p = map(int, f[2:].split())
        # Requête de coût entre deux sommets
        if f[0] == '0':
            print(g(n, E, *p))
        # Ajout d'une arête non orientée (commande formatée : 1 c d e)
        else:
            c, d, e = p
            E[c].append((e, d))
            E[d].append((e, c))

def main():
    """
    Fonction principale qui lit les paramètres d'instances et traite les commandes correspondantes.

    Lit de l'entrée standard des lignes du type 'n k', où n est le nombre de sommets et k le nombre de commandes à suivre.
    L'arrêt s'effectue lorsqu'on lit la ligne '0 0\n'.
    """
    for e in iter(r, '0 0\n'):
        s(*map(int, e.split()))

# Lancement du programme principal
if __name__ == "__main__":
    main()