from math import sqrt, atan2

# Fonction pour trouver les points d'intersection d'un segment avec un cercle
# cx, cy: coordonnées du centre du cercle
# r: rayon du cercle
# x1, y1: coordonnées du premier point du segment
# x2, y2: coordonnées du second point du segment
def intersection01(cx, cy, r, x1, y1, x2, y2):
    # Calcul de la différence des coordonnées entre les deux points du segment
    xd = x2 - x1  # Différence en x
    yd = y2 - y1  # Différence en y
    # Translation du segment pour recentrer le cercle en (0, 0)
    X = x1 - cx   # Décalage de x1 par rapport au centre du cercle
    Y = y1 - cy   # Décalage de y1 par rapport au centre du cercle
    # Calcul des coefficients de l'équation quadratique
    a = xd**2 + yd**2             # Coefficient a (toujours positif car c'est la somme des carrés)
    b = xd * X + yd * Y           # Coefficient b
    c = X**2 + Y**2 - r**2        # Coefficient c (pour savoir si le segment est à une distance inférieure ou supérieure au rayon)
    # Calcul du discriminant (D = b^2 - a*c) pour déterminer le nombre de solutions réelles
    D = b**2 - a*c
    result = []  # Liste pour stocker les points d'intersection
    # S'il y a deux points d'intersection réels (le discriminant est strictement positif)
    if D > 0:
        d = sqrt(D)  # La racine carrée du discriminant
        # Calcul du paramètre s pour le premier point d'intersection sur le segment
        # Les intersections sont valides seulement si 0 < s < 1 (donc à l'intérieur du segment)
        if 0 < -b - d < a:
            s = (-b - d) / a
            # Calcul de la position exacte du point d'intersection
            result.append((x1 + xd*s, y1 + yd*s))
        # Même chose pour l'autre solution
        if 0 < -b + d < a:
            s = (-b + d) / a
            result.append((x1 + xd*s, y1 + yd*s))
    # Cas où le segment est tangent au cercle (une seule intersection, discriminant nul)
    elif D == 0:
        if 0 < -b < a:
            s = -b / a
            result.append((x1 + xd*s, y1 + yd*s))
    # Si le discriminant est négatif, il n'y a pas d'intersection
    return result  # Retourne la liste des points d'intersection

# Fonction pour calculer la contribution signée d'un arc ou d'un segment à l'aire totale
# x0, y0 : coordonnées du premier point
# x1, y1 : coordonnées du second point
# rr     : carré du rayon du cercle
def calc(x0, y0, x1, y1, rr):
    # Vérifier si les deux points sont à l'intérieur du cercle (<= rr, tolérance 1e-8)
    if x0**2 + y0**2 - rr <= 1e-8 and x1**2 + y1**2 - rr <= 1e-8:
        # Aire du trapèze formé par l'origine et le segment (formule du produit vectoriel)
        return (x0 * y1 - x1 * y0) / 2.
    # Si un des points est à l'extérieur, calculer avec l'angle entre les deux points depuis l'origine
    theta = atan2(x0*y1 - x1*y0, x0*x1 + y0*y1)
    # Aire du secteur de cercle correspondant à cet angle (aire secteur = ½ × angle × r^2)
    return theta*rr/2.

# Lecture des entrées utilisateur
n, r = map(int, input().split()) # n : nombre de points, r : rayon du cercle
# Lecture des coordonnées des points du polygone (liste de points)
P = [list(map(int, input().split())) for i in range(n)]

rr = r**2  # Calcul du carré du rayon (pour des comparaisons plus rapides et éviter sqrt)
# La fonction principale pour calculer l'aire d'intersection dans une configuration donnée de cercle polygone
def solve(xb, yb):
    ans = 0  # Variable pour stocker la somme des aires partielles
    # Parcourir chaque arête (segment) du polygone
    for i in range(n):
        x0, y0 = P[i-1]  # Point de départ du segment (indice circulaire : P[-1] = P[n-1])
        x1, y1 = P[i]    # Point d'arrivée du segment
        # Translation des points pour que le centre du cercle soit en (0,0)
        x0 -= xb; y0 -= yb
        x1 -= xb; y1 -= yb
        # Recherche des points d'intersection éventuels entre le segment polygone et le cercle
        result = intersection01(0, 0, r, x0, y0, x1, y1)
        px = x0; py = y0  # Initialisation des coordonnées précédentes pour faire des découpages entre intersections
        # Pour chaque point d'intersection trouvé
        for x, y in result:
            # Calcul de la contribution d'aire entre le segment précédent et le point d'intersection
            ans += calc(px, py, x, y, rr)
            px = x; py = y  # Mise à jour du point précédent
        # Calcul de la dernière portion de l'arête jusqu'au sommet final
        ans += calc(px, py, x1, y1, rr)
    return ans  # Retourne l'aire totale (signée) de l'intersection

# Calcul du barycentre (centre de gravité) du polygone en moyenne arithmétique des coordonnées
x0 = sum(x for x, y in P)/n
y0 = sum(y for x, y in P)/n
# Calcul de l'aire d'intersection pour le cercle centré en (x0, y0)
ans = solve(x0, y0)

import random  # Import du module random pour sélectionner des déplacements aléatoires

random.seed()  # Initialisation du générateur de nombres aléatoires
randint = random.randint  # Pour gagner du temps d'appel de fonction

# Recherche stochastique pour maximiser l'aire d'intersection entre le polygone et le disque
for i in range(1000):  # Effectuer 1000 cycles d'optimisation
    ma = ans          # Stocke la meilleure aire trouvée jusqu'à présent
    nxt = None        # Sera la nouvelle position optimale si trouvée
    for j in range(100):  # Pour chaque cycle, tester 100 positions aléatoires
        # Génère un déplacement aléatoire dx, dy autour du centre courant (plus fin à chaque itération car i+1 grandit)
        dx = randint(-1000000, 1000000) / 10000 / (i+1)
        dy = randint(-1000000, 1000000) / 10000 / (i+1)
        # Essayer le disque centré en (x0 + dx, y0 + dy)
        res = solve(x0 + dx, y0 + dy)
        # On garde la nouvelle position si elle donne une aire strictement meilleure que la meilleure actuelle
        if ma < res:
            ma = res
            nxt = (x0 + dx, y0 + dy)
    # Mettre à jour la meilleure solution si une meilleure position a été trouvée
    if nxt is not None:
        ans = ma
        x0, y0 = nxt  # Déplacement du centre du disque
# Afficher l'aire maximale d'intersection trouvée après l'optimisation
print(ans)