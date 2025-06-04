# Lire quatre entiers à partir de l'entrée standard. La fonction input() lit une ligne en entrée utilisateur.
# split() sépare la ligne en éléments par des espaces.
# map(int, ...) convertit chaque élément de la liste en entier.
# Les valeurs sont affectées respectivement à x0, y0, x1, y1.
x0, y0, x1, y1 = map(int, input().split())

# Créer une liste représentant le point p0 avec les coordonnées x0, y0.
p0 = [x0, y0]
# Créer une liste représentant le point p1 avec les coordonnées x1, y1.
p1 = [x1, y1]

# Créer le vecteur v1 allant de p0 à p1.
# Chaque composante est obtenue en soustrayant la coordonnée de p0 à celle de p1.
v1 = [p1[0] - p0[0], p1[1] - p0[1]]

# Lire un entier q représentant le nombre de requêtes. Il s'agit du nombre de points à traiter.
q = int(input())

# Définir une fonction cross() qui calcule le produit vectoriel (produit en croix) de deux vecteurs 2D a et b.
def cross(a, b):
    # Calculer le déterminant des deux vecteurs.
    crs = a[0] * b[1] - a[1] * b[0]
    # Retourner le résultat du produit en croix. Ceci est un scalaire (nombre réel).
    return crs

# Définir une fonction dot() qui calcule le produit scalaire de deux vecteurs 2D a et b.
def dot(a, b):
    # Calculer le produit des composantes x puis ajouter le produit des composantes y.
    dt = a[0] * b[0] + a[1] * b[1]
    # Retourner le résultat du produit scalaire. Ceci est également un scalaire.
    return dt

# Définir une petite valeur eps (epsilon) pour gérer les erreurs d'arrondi lors des comparaisons de nombres flottants.
eps = 0.000001

# Boucler pour traiter chacune des q requêtes.
for i in range(q):
    # Lire une ligne d'entrée, séparer en deux entiers pour obtenir les coordonnées du point p2
    p2 = list(map(int, input().split()))
    
    # Calculer le vecteur v2 allant de p0 à p2
    v2 = [p2[0] - p0[0], p2[1] - p0[1]]
    
    # Utiliser la fonction cross() pour déterminer l'orientation de v2 par rapport à v1.
    # Si le produit vectoriel est supérieur à eps, p2 est à gauche de la direction de v1 (sens anti-horaire).
    if cross(v1, v2) > eps:
        print("COUNTER_CLOCKWISE")
    # Si le produit vectoriel est inférieur à -eps, p2 est à droite de la direction de v1 (sens horaire).
    elif cross(v1, v2) < -eps:
        print("CLOCKWISE")
    # Si le produit vectoriel est environ nul, p2 est aligné avec v1.
    # On regarde maintenant le produit scalaire pour déterminer de quel côté de p0 est p2.
    elif dot(v1, v2) < -eps:
        # Si le produit scalaire est négatif, l'angle entre v1 et v2 est supérieur à 90°, c'est derrière l'origine v1.
        print("ONLINE_BACK")
    # Si the produit scalaire est non négatif, comparer leur longueur au carré.
    # v1[0]**2 + v1[1]**2 est la longueur au carré du segment p0p1.
    # v2[0]**2 + v2[1]**2 est la longueur au carré du segment p0p2.
    # Si la distance de p0 à p1 est plus petite que la distance de p0 à p2, alors p2 est sur la droite p0p1 mais devant p1.
    elif v1[0]**2 + v1[1]**2 < v2[0]**2 + v2[1]**2:
        print("ONLINE_FRONT")
    else:
        # Dans tous les autres cas, p2 est sur le segment p0p1, c'est-à-dire entre p0 et p1 inclus.
        print("ON_SEGMENT")