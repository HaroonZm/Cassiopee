import sys
import math

# On va résoudre le problème en suivant cette approche détaillée:
# 1. Trier les ruines par leur coordonnée x (longitude).
# 2. On envisage de tracer la ligne verticale juste avant chaque x possible entre les ruines,
#    cela inclut aussi les cas extrêmes où toutes les ruines sont à gauche (ICPC) ou à droite (JAG).
# 3. Pour chaque séparation possible, on calcule l'enveloppe convexe (convex hull) des ruines à gauche
#    et à droite. L'enveloppe convexe permet de trouver la zone minimale qui entoure tous les points.
# 4. On calcule l'aire polygonale de chaque enveloppe convexe.
# 5. On cherche la séparation qui minimise la somme des aires des deux enveloppes.
#
# Contraintes importantes:
# - Jusqu'à 100000 ruines => calculer l'enveloppe convexe et les aires à chaque séparation est impossible en O(N²).
# Solution:
# - Puisque la ligne verticale doit éviter de couper une ruine, on ne considère que les x distincts présents.
# - Pré-calculate les enveloppes convexes progressives de gauche à droite et de droite à gauche.
# - Ainsi, on peut pour chaque séparation récupérer en O(1) l'enveloppe convexe cumulée à gauche et la droite.
# - Calculer les aires des enveloppes progressives pour chaque coté.
#
# Note: Comme il n'y a aucune ruine avec une coordonnée x identique (car points distincts et positions),
#    on peut partitionner facilement.

sys.setrecursionlimit(10**7)

def cross(o, a, b):
    # Produit vectoriel OA x OB
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def convex_hull(points):
    # Algorithme de Graham ou Andrew pour trouver l'enveloppe convexe
    points = sorted(points)
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Enveloppe convexe sans duplication des points extrêmes
    return lower[:-1] + upper[:-1]

def polygon_area(poly):
    # Calcul de l'aire d'un polygone simple
    area = 0
    n = len(poly)
    if n < 3:
        return 0
    for i in range(n):
        j = (i+1)%n
        area += poly[i][0]*poly[j][1] - poly[j][0]*poly[i][1]
    return abs(area)/2

def main():
    input = sys.stdin.readline
    N = int(input())
    ruins = [tuple(map(int, input().split())) for _ in range(N)]

    # Trier les ruines selon leur x (position east)
    ruins.sort(key=lambda p: p[0])
    
    # Extraire les x distincts en ordre pour partition
    xs = sorted(set(p[0] for p in ruins))
    # Pour partitionner on doit pouvoir récupérer à chaque étape par x distinct:
    # - Ruines à gauche (x <= seuil)
    # - Ruines à droite (x > seuil)

    # Groupement des indices dans ruins selon x distinct
    # Construire un tableau où on peut accéder à la limite de séparation facilement.
    # ruins est trié donc on peut faire un scan.

    # Indices de début de chaque x distinct dans ruins
    # Utilisé pour diviser facilement en groupes "à gauche" en incluant tous les points avec x = x_i
    x_to_idx = {}
    cur = 0
    for x in xs:
        # Advance cur jusqu'à la première ruine avec x >= x
        # ruins est trié par x croissant, donc cur est croissant aussi
        start = cur
        while cur < N and ruins[cur][0] == x:
            cur += 1
        x_to_idx[x] = (start, cur)  # intervalle [start, cur) des ruines with x

    # Pré-calculer les enveloppes convexes cumulées par fusion progressive des points:
    # Une difficulté: Nous voulons l'enveloppe convexe des ruines ayant x <= seuil pour les "gauche"
    # et x > seuil pour "droite".
    # Or les points sont triés par x croissant.
    # Donc pour la gauche, on prend les premiers M points (croissance de M)
    # Pour la droite, on prend à l'inverse les derniers N-M points.

    # On doit stocker pour chaque limite les enveloppes convexes des deux côtés.

    # Pour optimiser, on va stocker à chaque "segment" de ruines correspondant à un x distinct
    # l'enveloppe convexe cumulée pour la gauche.

    # Pour la partie gauche progressive:
    left_points = []
    left_hulls = []
    # Pour la partie droite progressive:
    right_points = []
    right_hulls = []

    # On va stocker la liste cumulative des points triés
    # pour "left" on cumule du début vers la fin
    # pour "right" du fin vers le début

    # Construire tableaux cumulés
    # left_points[i]: tous les points avec x <= xs[i]
    # right_points[i]: tous les points avec x >= xs[i]
    # Pour indice i, left_points = toutes les ruines avec x <= xs[i], right_points = toutes les ruines avec x > xs[i]

    # Construire un tableau où left_points[i] = toutes les ruines avec x <= xs[i]
    # On va d'abord créer un tableau cumulatif complet
    cumul_points = []
    idx = 0
    for x in xs:
        start, end = x_to_idx[x]
        # Ajouter tous les points avec ce x
        for i_p in range(start, end):
            cumul_points.append(ruins[i_p])

    # Left hulls: on ajoute point par point et recalcul l'enveloppe convexe
    # C'est coûteux de recalculer l'enveloppe complète à chaque ajout.
    # L'enveloppe convexe peut être mise à jour en O(log n) si on utilise des structures sophistiquées,
    # Mais ici, on doit optimiser.

    # Astuce: on utilise un algorithme d'enveloppe convexe "monotone chain"
    # Ici, tous les points sont triés par x croissant,
    # donc on peut construire la cout la fermeture convexe "monotone" dans l'ordre.

    # Construire ENVELOPPES cumulées pour left_points:
    left_upper = []
    left_lower = []
    left_areas = []
    # On va construire l'enveloppe convexe monotone chain tout en ajoutant points:
    # lower et upper sont deux listes qui forment l'enveloppe convexe

    for p in cumul_points:
        # Construire lower hull (inférieur)
        while len(left_lower) >= 2 and cross(left_lower[-2], left_lower[-1], p) <= 0:
            left_lower.pop()
        left_lower.append(p)
        # Construire upper hull (supérieur)
        while len(left_upper) >= 2 and cross(left_upper[-2], left_upper[-1], p) >= 0:
            left_upper.pop()
        left_upper.append(p)
        # Construire l'enveloppe convexe complète à chaque étape
        hull = left_lower[:-1] + left_upper[::-1][:-1]
        area = polygon_area(hull)
        left_areas.append(area)

    # Construire right hulls cumulés inversement
    cumul_points_r = []
    for x in reversed(xs):
        start, end = x_to_idx[x]
        # Ajouter tous les points pour ce x de manière inversée pour construire la liste cumulée à droite
        # On veut tous les points avec x >= xs[i] pour right_points[i]
        # Nous allons cumuler dans l'ordre décroissant
        for i_p in range(end-1, start-1, -1):
            cumul_points_r.append(ruins[i_p])

    right_upper = []
    right_lower = []
    right_areas = []
    for p in cumul_points_r:
        while len(right_lower) >= 2 and cross(right_lower[-2], right_lower[-1], p) <= 0:
            right_lower.pop()
        right_lower.append(p)
        while len(right_upper) >= 2 and cross(right_upper[-2], right_upper[-1], p) >= 0:
            right_upper.pop()
        right_upper.append(p)
        hull = right_lower[:-1] + right_upper[::-1][:-1]
        area = polygon_area(hull)
        right_areas.append(area)
    # right_areas correspond à cumul de la droite depuis la fin (de gros x) au début (de petit x)
    # on va l'inverser pour correspondre à xs[...]
    right_areas.reverse()

    # Maintenant on peut tenter toutes les positions de ligne verticale possible:
    # On peut mettre la ligne:
    # - tout à gauche : 0 ruines à gauche, N à droite
    # - avant le premier x : left=empty, right=all: left_area=0, right_area=aire envelope all
    # - entre deux x distincts i et i+1: left_points = tous points avec x <= xs[i], right_points = tous points avec x > xs[i]
    # - tout à droite : left=all, right=empty

    # Comme left_areas[i] contient aire enveloppe des points x <= xs[i]
    # right_areas[i] contient aire enveloppe des points x >= xs[i] (mais on veut les points strictement > xs[i],
    # on fera un décalage)

    # On teste les découpages sur i:
    # On place ligne juste à droite de xs[i], donc:
    # gauche = ruines avec x <= xs[i] -> left_areas[i]
    # droite = ruines avec x > xs[i] -> right_areas[i+1] (si i+1 < len(xs)) sinon 0

    minimal_sum_area = math.inf
    m = len(xs)

    for i in range(m+1):
        # i représente le nombre de x distincts assignés à gauche (de 0 à m)
        # Si i==0 -> gauche vide (aucune ruine), droite = toutes les ruines
        if i == 0:
            left_area = 0
            right_area = right_areas[0] if m > 0 else 0
        elif i == m:
            # tous à gauche, droite vide
            left_area = left_areas[m-1]
            right_area = 0
        else:
            left_area = left_areas[i-1]
            right_area = right_areas[i]
        total_area = left_area + right_area
        if total_area < minimal_sum_area:
            minimal_sum_area = total_area

    # Afficher l'aire minimale arrondie à l'entier le plus proche
    print(int(round(minimal_sum_area)))

if __name__ == '__main__':
    main()