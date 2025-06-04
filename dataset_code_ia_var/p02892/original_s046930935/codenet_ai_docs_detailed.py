import sys

# Augmente la limite de récursion pour permettre des appels récursifs profonds (nécessaire pour un grand graphe)
sys.setrecursionlimit(10**7)

# Substitue la fonction d'entrée standard pour une lecture rapide ligne par ligne
input = sys.stdin.readline

def dfs(v, color):
    """
    Effectue un parcours en profondeur (DFS) pour vérifier si le graphe est biparti.
    Attribue récursivement une couleur alternée à chaque sommet.

    Args:
        v (int): Le sommet actuellement visité.
        color (int): La couleur à assigner au sommet (1 ou -1).

    Returns:
        bool: True si le graphe peut être colorié sans conflits (biparti), False sinon.
    """
    colors[v] = color  # Attribuer la couleur au sommet courant
    for to in g[v]:    # Pour chaque voisin du sommet courant
        if colors[to] == color:
            # Si le voisin a déjà la même couleur, ce n'est pas biparti
            return False
        if colors[to] == 0 and not dfs(to, -color):
            # Si le voisin n'est pas encore colorié, coloriage avec la couleur opposée
            # Si un conflit survient plus loin, retourne immédiatement False
            return False
    return True  # Aucun conflit détecté, la sous-composante est bipartie

def Washall_Floyd(d):
    """
    Applique l'algorithme de Floyd-Warshall pour calculer les plus courts chemins
    entre toutes les paires de sommets dans un graphe pondéré.

    Args:
        d (list of list of float): Matrice d'adjacence initiale du graphe représentant les poids des arêtes.

    Returns:
        list of list of float: Matrice des plus courts chemins entre toutes les paires de sommets.
    """
    for k in range(n):              # Pour chaque sommet intermédiaire
        for i in range(n):          # Pour chaque sommet de départ
            for j in range(n):      # Pour chaque sommet d'arrivée
                # Met à jour la distance minimale de i à j via k si cela réduit le coût
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

# Lecture du nombre de sommets dans le graphe
n = int(input())

# Initialisation de la liste d'adjacence pour le graphe et la matrice des distances
g = [[] for _ in range(n)]  # Liste d'adjacence pour chaque sommet
f_inf = float('inf')        # Représente l'infini pour l'initialisation des distances
dist = [[f_inf] * n for _ in range(n)]  # Matrice des poids (distances) initiaux

# Distance d'un sommet à lui-même = 0
for i in range(n):
    dist[i][i] = 0

# Lecture de la matrice d'adjacence en entrée et construction du graphe
for i in range(n):
    S = input()  # Lire la ligne correspondant aux arêtes du sommet i
    for j in range(n):
        if S[j] == '1':
            # Il existe une arête entre i et j
            g[i].append(j)     # Ajouter j à la liste des voisins de i
            dist[i][j] = 1     # Poids de l'arête directe (i,j) = 1
            dist[j][i] = 1     # Graphe non orienté : (j,i) aussi

# Initialisation du tableau de couleurs pour la vérification bipartite
colors = [0] * n  # 0 = pas colorié, 1 ou -1 pour distinguer les deux couleurs
ans = -1          # Valeur retournée en cas de graphe non biparti

# Vérifie si le graphe est biparti à partir du sommet 0
if not dfs(0, 1):
    # Si ce n'est pas biparti, affichage de -1 selon la spécification
    print(ans)
else:
    # Si le graphe est biparti, calcule les distances via Floyd-Warshall
    Washall_Floyd(dist)
    for d in dist:
        # Pour chaque sommet, récupère la distance maximale vers un autre sommet
        tmp = max(d)
        # Prend la plus grande de ces distances (diamètre du graphe)
        ans = max(tmp, ans)
    # Affiche le diamètre + 1 (taille minimale de la partition/décomposition)
    print(ans + 1)