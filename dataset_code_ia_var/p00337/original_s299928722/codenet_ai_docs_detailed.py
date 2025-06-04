from math import sqrt

def dist2(A, B):
    """
    Calcule la distance Euclidienne au carré entre deux points A et B.

    Args:
        A (list or tuple): Coordonnées du premier point [x, y].
        B (list or tuple): Coordonnées du second point [x, y].
    
    Returns:
        int: Distance au carré entre les points A et B.
    """
    return (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2

def cross(A, B, C):
    """
    Calcule le produit croisé pour trois points A, B et C.
    Aide à déterminer l'orientation du triplet (gauche, droite ou alignés).

    Args:
        A (list or tuple): Coordonnées du point A [x, y].
        B (list or tuple): Coordonnées du point B [x, y].
        C (list or tuple): Coordonnées du point C [x, y].
    
    Returns:
        int: Le produit croisé. Positif pour un virage à gauche, négatif à droite, zéro si alignés.
    """
    return (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])

def convex_hull(PS):
    """
    Calcule l'enveloppe convexe d'un ensemble de points 2D en utilisant l'algorithme de Monotone Chain.
    Renvoie la liste des indices des points du polygone convexe dans l'ordre.

    Args:
        PS (list of list): Liste des points sous la forme [[x1, y1], [x2, y2], ...].
    
    Returns:
        list: Liste des indices des points de l'enveloppe convexe, dans l'ordre du parcours.
    """
    n = len(PS)
    # Ajout de l'indice aux coordonnées pour garder trace de l'origine après tri
    PP = sorted([p + [i] for i, p in enumerate(PS)])
    Q = []
    # Construction de la moitié basse de l'enveloppe convexe
    for i in range(n):
        while len(Q) > 1 and cross(PP[Q[-2]], PP[Q[-1]], PP[i]) >= 0:
            Q.pop()
        Q.append(i)
    k = len(Q)
    # Construction de la moitié haute
    for i in range(n - 2, -1, -1):
        while len(Q) > k and cross(PP[Q[-2]], PP[Q[-1]], PP[i]) >= 0:
            Q.pop()
        Q.append(i)
    # Retour des indices d'origine des points de l'enveloppe
    return [PP[i][2] for i in Q]

def root(x):
    """
    Trouve la racine d'un élément dans la structure d'union-find avec compression de chemin.

    Args:
        x (int): Élément pour lequel trouver la racine.

    Returns:
        int: Racine de l'ensemble contenant x.
    """
    if x == parent[x]:
        return x
    # Compression du chemin pour optimiser les prochaines recherches
    parent[x] = root(parent[x])
    return parent[x]

def unite(x, y):
    """
    Fusionne deux ensembles disjoints contenant x et y dans l'union-find.

    Args:
        x (int): Premier élément à unir.
        y (int): Second élément à unir.
    """
    px = root(x)
    py = root(y)
    # Rattache le plus grand arbre au plus petit pour équilibrer l'arbre
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def main():
    """
    Lit les entrées, construit l'enveloppe convexe, l'union-find, puis connecte les points comme spécifié,
    en calculant le coût total des ajouts de routes nécessaires pour connecter tous les points du graphe.

    Les entrées attendues sont au format :
        <v> <r>
        <x1> <y1>
        ...
        <xv> <yv>
        <s1> <t1>
        ...
        <sr> <tr>

    Où v est le nombre de points, r le nombre de routes potentielles, (xi, yi) les coordonnées,
    et (si, ti) une paire de sommets reliés par la i-ème route potentielle.
    """
    # Lecture du nombre de sommets (v) et du nombre de routes potentielles (r)
    v, r = map(int, input().split())
    # Lecture des coordonnées des points
    PS = [list(map(int, input().split())) for _ in range(v)]
    # Construction de l'enveloppe convexe et récupération des indices dans CH
    CH = convex_hull(PS)

    # Initialisation du tableau union-find pour chaque point
    global parent
    parent = list(range(v))

    # Initialisation de la variable qui stocke la somme des longueurs des routes utilisées
    ans = 0

    # Connexion des points de l'enveloppe convexe entre eux (chemin polygonal)
    for i in range(len(CH) - 1):
        unite(CH[i], CH[i + 1])
        ans += sqrt(dist2(PS[CH[i]], PS[CH[i + 1]]))

    # Lecture des routes potentielles et tri par distance croissante
    R = [list(map(int, input().split())) for _ in range(r)]
    # Trie les routes par distance croissante pour préparer l'algorithme de type Kruskal
    R.sort(key=lambda x: dist2(PS[x[0] - 1], PS[x[1] - 1]))

    # Pour chaque route potentielle, ajoute si utile pour connecter deux composantes disjointes
    for s, t in R:
        if root(s - 1) != root(t - 1):
            unite(s - 1, t - 1)
            ans += sqrt(dist2(PS[s - 1], PS[t - 1]))

    # Affichage du coût total minimal
    print(ans)

# Lancement du programme principal
if __name__ == "__main__":
    main()