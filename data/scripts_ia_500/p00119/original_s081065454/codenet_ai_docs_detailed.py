from collections import deque

def solve():
    """
    Résout un problème d'ordonnancement ou de tri topologique sur un graphe dirigé.
    
    Lit en entrée :
    - M : le nombre de nœuds (sommets) dans le graphe.
    - N : le nombre d'arêtes dans le graphe.
    - N paires d'entiers (x, y) représentant une arête dirigée de x vers y.
    
    Le but est de déterminer un ordre linéaire des sommets tel que pour chaque arête (x -> y),
    x apparaisse avant y dans l'ordre (tri topologique).
    
    Procède par :
    - Construction de la liste d'adjacence du graphe.
    - Calcul du degré d'entrée (nombre d'arêtes entrantes) de chaque sommet.
    - Utilisation d'une file (deque) pour extraire les sommets sans prérequis (deg=0).
    - Parcours des sommets et mise à jour des degrés d'entrée pour trouver l'ordre.
    
    Affiche l'ordre topologique trouvé, un sommet par ligne.
    """
    # Lecture du nombre de sommets du graphe
    M = int(input())
    # Initialisation de la liste d'adjacence : une liste de listes vide pour chaque sommet
    G = [[] for i in range(M)]
    # Initialisation du tableau des degrés d'entrée pour chaque sommet à 0
    deg = [0]*M
    # Lecture du nombre d'arêtes
    N = int(input())
    # Lecture des arêtes et construction du graphe dirigé
    for i in range(N):
        x, y = map(int, input().split())
        # On stocke y-1 dans la liste du sommet x-1 (indices 0-based)
        G[x-1].append(y-1)
        # On incrémente le degré d'entrée de y-1
        deg[y-1] += 1

    # Initialisation d'une file pour les sommets avec degré d'entrée nul (pas de prédécesseurs)
    que = deque()
    # Liste pour stocker l'ordre topologique final des sommets
    ans = []
    # On ajoute dans la file tous les sommets sans prédécesseurs
    for i in range(M):
        if deg[i] == 0:
            que.append(i)

    # Tant qu'il reste des sommets sans prédécesseurs dans la file
    while que:
        # On enlève le premier sommet de la file
        v = que.popleft()
        # On ajoute ce sommet à la solution (en rebasant l'index de 0 à 1)
        ans.append(v+1)
        # Pour chaque sommet atteignable directement depuis v
        for w in G[v]:
            # On réduit le degré d'entrée de w car v est traité
            deg[w] -= 1
            # Si w n'a plus de prédécesseurs non traités, on l'ajoute à la file
            if deg[w] == 0:
                que.append(w)

    # Impression du résultat : un sommet par ligne, dans l'ordre topologique trouvé
    print(*ans, sep='\n')

solve()