import math  # On importe le module math qui fournit des fonctions mathématiques comme atan2 et pi.

# On lit un entier N depuis l'entrée standard, qui représente le nombre de points à traiter pour la suite du programme.
N = int(input())

# On crée une liste vide ps, qui va contenir les coordonnées de tous les points ainsi qu'un identifiant unique pour chacun.
ps = []

# On boucle de 0 à N-1 (c'est-à-dire N fois) pour lire les coordonnées de chaque point.
for i in range(N):
    # On lit une ligne de l'entrée standard, on la découpe à l'aide de split()
    # Ensuite, on convertit les parties en entiers avec map(int, ...)
    x, y = map(int, input().split())
    # On ajoute à la liste ps un tuple contenant :
    # - la coordonnée x du point
    # - la coordonnée y du point
    # - l'indice original du point (permettra de faire correspondre les résultats à l'entrée)
    ps.append((x, y, i))

# On trie les points dans l'ordre lexicographique (d'abord selon x, puis y, puis indice), ce qui est utile pour l'algorithme du calcul du convex hull.
ps.sort()

# Définition d'une fonction vec(pi, pj) qui calcule le vecteur allant du point pi vers le point pj.
def vec(pi, pj):
    # pi et pj sont des tuples contenant x, y, indice
    # On retourne la différence sur x et la différence sur y entre pj et pi
    return (pj[0] - pi[0], pj[1] - pi[1])

# Définition d'une fonction det(vi, vj) qui calcule le déterminant (produit vectoriel) de deux vecteurs vi et vj.
def det(vi, vj):
    # vi[0] correspond à la composante x de vi, vi[1] à la composante y de vi.
    # vj idem. Le produit vectoriel de (a, b) et (c, d) est a*d - b*c.
    return vi[0] * vj[1] - vi[1] * vj[0]

# On va calculer l'enveloppe convexe (convex hull) des points.
# Pour cela, on utilise une construction de type "monotone chain".
cvx = []  # Cette liste contiendra les indices des points formant l'enveloppe convexe, dans l'ordre.

# On va parcourir deux fois tous les points :
# - une fois avec range(N) pour la partie inférieure,
# - une fois avec range(N-1, -1, -1) pour la partie supérieure (en inversant)
# La syntaxe [::-1] inverse la liste.
for i in list(range(N)) + list(range(N-1))[::-1]:
    # Tant qu'il y a au moins deux éléments dans cvx,
    # et que le dernier mouvement ne forme pas un virage à gauche (i.e. le déterminant des deux derniers segments est négatif),
    # on retire le dernier point ajouté (on veut un contour convexe).
    while len(cvx) >= 2 and det(
        vec(ps[cvx[-2]], ps[cvx[-1]]),  # Vecteur du point avant-dernier vers le dernier ajouté
        vec(ps[cvx[-1]], ps[i])         # Vecteur du dernier ajouté vers le point i courant
    ) < 0:
        cvx.pop()  # On enlève le dernier point car il casserait la convexité.
    # On ajoute le point courant i (son indice) à la liste des sommets de l'enveloppe convexe.
    cvx.append(i)

# Pour chaque sommet de l'enveloppe convexe, on veut calculer l'angle entre les deux arêtes incidentes (qui partent du sommet)
# On utilise un dictionnaire ans pour stocker les pentes (sous la forme d'angles) associées à chaque sommet (par leur indice d'origine)
ans = {}  # Dictionnaire qui contiendra pour chaque sommet deux angles : [angle sortant, angle entrant]

pi = None  # Variable temporaire pour mémoriser le sommet précédent dans l'itération.

# On parcourt les sommets de la convex hull dans l'ordre calculé précédemment.
for i in cvx:
    # On récupère les coordonnées et l'indice d'origine du sommet courant.
    x, y, j = ps[i]
    # Si on n'est pas sur le tout premier sommet de l'itération
    if pi is not None:
        # On récupère les coordonnées et l'indice d'origine du sommet précédent.
        px, py, pj = ps[pi]
        # On calcule l'angle (en radians) de la droite passant du point précédent au point courant,
        # par rapport à l'axe des x, en utilisant atan2 qui gère le cas x=0.
        slope = math.atan2(y-py, x-px)
        # Si le sommet courant n'a pas encore d'entrée dans ans, on l'initialise à [0, 0]
        if j not in ans:
            ans[j] = [0, 0]
        # Si le sommet précédent non plus, on l'initialise.
        if pj not in ans:
            ans[pj] = [0, 0]
        # On stocke l'angle dans le tableau de la manière suivante :
        # - Pour le sommet courant (j), la première valeur (index 0) prend la valeur slope (c'est l'angle de l'arête qui arrive).
        # - Pour le sommet précédent (pj), la deuxième valeur (index 1) prend la valeur slope (c'est l'angle de l'arête qui part).
        ans[j][0] = slope
        ans[pj][1] = slope
    # On met à jour pi avec l'indice courant, pour la prochaine itération.
    pi = i

# On parcourt tous les indices depuis 0 jusqu'à N-1 pour restituer les résultats dans l'ordre de l'entrée.
for i in range(N):
    # Si le point d'indice i n'est pas dans ans, cela signifie qu'il n'est pas sur l'enveloppe convexe,
    # donc par convention on affiche 0 (le centre d'un polygone convexe n'a pas d'angle).
    if i not in ans:
        print(0)
        continue  # On passe au point suivant

    # On récupère les deux angles stockés pour le sommet i.
    v1, v2 = ans[i]
    # Si v2 est inférieur à v1 (ce qui peut arriver à cause du passage à 2*Pi en radians),
    # on ajoute 2*Pi à v2 pour que la différence entre v2 et v1 soit toujours positive.
    if v2 < v1:
        v2 += 2*math.pi
    # On calcule l'angle au sommet formé par les deux segments, on divise par 2*Pi pour normaliser cette valeur entre 0 et 1,
    # puis on arrondit à 8 décimales avant de l'afficher.
    print(round((v2-v1) / (2*math.pi), 8))