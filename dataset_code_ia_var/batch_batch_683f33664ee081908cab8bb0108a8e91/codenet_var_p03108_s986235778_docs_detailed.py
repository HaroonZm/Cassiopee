"""
Ce programme implémente l'algorithme "union-find" (ou DSU, Disjoint Set Union)
pour résoudre un problème de dénombrement de paires connectées dans un graphe dynamique,
où les arêtes sont "ajoutées" dans l'ordre inverse, simulant leur suppression dans l'ordre d'entrée.
"""

# Lecture des deux entiers : n = nombre de sommets, m = nombre d'arêtes
n, m = map(int, input().split())

# Initialisation du tableau de liens pour les ensembles disjoints.
# d[x] < 0 signifie que x est racine et -d[x] sa taille.
# Sinon, d[x] est le parent de x.
d = [-1] * n

def find(x):
    """
    Trouve la racine représentant du composant contenant x.
    Applique la compression de chemin pour accélérer les recherches futures.

    Args:
        x (int): Le sommet dont on cherche la racine.

    Returns:
        int: La racine de l'ensemble auquel x appartient.
    """
    # Si x est la racine de son ensemble
    if d[x] < 0:
        return x
    # Compression de chemin : attache x directement à la racine.
    d[x] = find(d[x])
    return d[x]

def unite(x, y):
    """
    Fusionne les ensembles auxquels appartiennent x et y.
    Utilise l'union par taille : l'ensemble le plus petit devient enfant du plus grand.

    Args:
        x (int): Un sommet appartenant au premier ensemble.
        y (int): Un sommet appartenant au second ensemble.
    """
    # Trouver les racines respectives
    x = find(x)
    y = find(y)
    # Si déjà dans le même ensemble, rien à faire
    if x == y:
        return
    # Garantir que x est la racine du plus grand ensemble (par taille négative)
    if d[x] > d[y]:
        x, y = y, x
    # Fusionner les ensembles : ajouter la taille de y à celle de x
    d[x] += d[y]
    d[y] = x

# Calcul initial du nombre total de paires possibles (sans arêtes)
# Soit n*(n-1)/2 paires distinctes possibles au début
ans = int(n * (n - 1) / 2)

# Tableaux pour stocker les extrémités de chaque arête
a = [0] * m
b = [0] * m

# Pile pour stocker les réponses de chaque itération
stack = []

# Lecture de toutes les arêtes du graphe (indices 1-based modifiés en 0-based)
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

# On inverse l'ordre pour traiter les arêtes dans l'ordre inverse d'ajout (simule suppression)
a.reverse()
b.reverse()

# Simulation : on commence avec un graphe sans arêtes, on ajoute une par une en sens inverse
for i in range(m):
    # Stocke la réponse actuelle avant d'ajouter l'arête
    stack.append(ans)
    # Trouver les représentants des ensembles de a[i] et b[i]
    a_root = find(a[i])
    b_root = find(b[i])
    # Si les deux sommets ne sont pas déjà connectés
    if a_root != b_root:
        # On retire le nombre de paires qui deviennent connectées par cette union
        ans -= (-d[a_root]) * (-d[b_root])
        # Fusionner les ensembles
        unite(a_root, b_root)

# On affiche les réponses accumulées dans l'ordre d'origine (car empilées à l'envers)
while stack:
    print(stack.pop())