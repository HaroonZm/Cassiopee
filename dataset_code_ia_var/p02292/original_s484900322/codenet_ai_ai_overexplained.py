# Définition d'une fonction dot qui calcule le produit scalaire (dot product) entre deux vecteurs a et b
def dot(a, b):
    # Le produit scalaire de deux vecteurs a = [a0, a1] et b = [b0, b1] est calculé comme :
    # a0*b0 + a1*b1
    # Cela mesure dans quelle mesure deux vecteurs pointent dans la même direction.
    return a[0] * b[0] + a[1] * b[1]

# Définition d'une fonction cross qui calcule le produit vectoriel (wedge or cross product) en 2D
def cross(a, b):
    # Pour deux vecteurs en 2D, le produit vectoriel est un scalaire :
    # a0*b1 - a1*b0
    # Il donne la "surface" du parallélogramme défini par les deux vecteurs.
    # Son signe indique le sens de rotation de a vers b : positif = sens trigo, négatif = sens horaire.
    return a[0] * b[1] - a[1] * b[0]

# Définition d'une fonction Order qui détermine la relation spatiale entre deux vecteurs a et b
def Order(a, b):
    # On calcule le produit vectoriel (cross product) entre a et b pour déterminer leur orientation relative
    crs = cross(a, b)
    # Si le résultat est strictement positif, alors b est à gauche de a
    if crs > 0:
        # Il s'agit d'un déplacement dans le sens anti-horaire (trigonometrique) de a à b (Gauche)
        return "COUNTER_CLOCKWISE"
    # Si le résultat est strictement négatif, alors b est à droite de a
    elif crs < 0:
        # Il s'agit d'un déplacement dans le sens horaire de a à b (Droite)
        return "CLOCKWISE"
    else:
        # Si le résultat est nul, alors a et b sont colinéaires (sur la même droite)
        # On vérifie alors leur position relative via le produit scalaire
        # Si le produit scalaire est négatif, b pointe dans la direction strictement opposée à a
        if dot(a, b) < 0:
            # Cela veut dire que b est derrière a par rapport à l'origine
            return "ONLINE_BACK"
        # Si le produit scalaire de a avec lui-même est plus petit que celui de b avec lui-même,
        # alors b est plus loin de l'origine que a - donc il se trouve devant a
        elif dot(a, a) < dot(b, b):
            # Cela veut dire que b est en avant après a (hors du segment)
            return "ONLINE_FRONT"
        else:
            # Sinon b est sur le segment [origine, extrémité de a]
            return "ON_SEGMENT"

# Lecture des coordonnées de deux points (x0, y0) et (x1, y1) à partir d'une seule ligne d'entrée utilisateur
# L'utilisateur entre les 4 entiers séparés par des espaces
x0, y0, x1, y1 = [int(i) for i in input().split()]
# On construit le vecteur a correspondant au déplacement de (x0, y0) à (x1, y1)
# Cela se fait en soustrayant les coordonnées du point d'origine (x0, y0) à celles du point final (x1, y1)
a = [x1 - x0, y1 - y0]

# Lecture du nombre de requêtes q
q = int(input())
# Pour chaque requête, on lit les coordonnées d'un point (x2, y2)
for i in range(q):
    # On lit et convertit les deux entiers de la ligne saisie en coordonnées x2 et y2
    x2, y2 = [int(i) for i in input().split()]
    # On construit le vecteur b du point de départ d'origine (x0, y0) vers ce nouveau point (x2, y2)
    b = [x2 - x0, y2 - y0]
    # On affiche la relation spatiale entre les vecteurs a et b en appelant la fonction Order
    print(Order(a, b))