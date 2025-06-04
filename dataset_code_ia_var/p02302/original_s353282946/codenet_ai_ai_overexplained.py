# Fonction qui calcule le "produit vectoriel" (cross product) en 2D de deux nombres complexes.
def cross(c1, c2):
    # Prend deux nombres complexes c1 et c2.
    # Le nombre complexe c1 a une partie réelle (c1.real) correspondant à l'axe x,
    # et une partie imaginaire (c1.imag) correspondant à l'axe y.
    # Le produit vectoriel (cross product) en 2D se calcule par la formule suivante :
    # c1.real * c2.imag - c1.imag * c2.real
    # Ce résultat donne une valeur positive ou négative selon l'orientation des deux vecteurs.
    return c1.real * c2.imag - c1.imag * c2.real

# Fonction qui trouve le point d'intersection (cross point) de deux segments.
def cross_point(p1, p2, p3, p4):
    # p1 et p2 sont les deux extrémités du premier segment.
    # p3 et p4 sont les deux extrémités du second segment.
    # Calcul du vecteur reliant p3 à p4, appelé base.
    base = p4 - p3
    # Calcul des vecteurs reliant p3 à p1 et p3 à p2.
    hypo1 = p1 - p3
    hypo2 = p2 - p3
    # Calcul des produits vectoriels entre base et hypo1, hypo2,
    # puis normalisation par la norme (longueur) du vecteur base.
    # Cela donne la position relative de p1 et p2 par rapport au segment [p3, p4].
    d1 = cross(base, hypo1) / abs(base)
    d2 = cross(base, hypo2) / abs(base)
    # Calcule la position du point d'intersection le long du segment [p1, p2].
    # On utilise la formule paramétrique du segment et la proportion d1 / (d1 - d2)
    # pour trouver le point précis où a lieu l'intersection.
    cp = p1 + d1 / (d1 - d2) * (p2 - p1)
    # Retourne ce point d'intersection comme un nombre complexe.
    return cp

# Fonction interne qui calcule l'aire d'un triangle donné par 3 points complexes.
def _area_of_triangle(c1, c2, c3):
    # Calcule les vecteurs entre c1 et c2, puis entre c1 et c3.
    v1 = c2 - c1
    v2 = c3 - c1
    # L'aire d'un triangle de sommets c1, c2, c3 se calcule par la moitié du module
    # du produit vectoriel des deux vecteurs calculés précédemment.
    # L'expression v1.real * v2.imag - v1.imag * v2.real correspond à la norme du
    # produit vectoriel en 2D.
    return abs(v1.real * v2.imag - v1.imag * v2.real) / 2

# Fonction principale : réalise un "convex cut" (coupe convexe) sur un polygone.
def convex_cut(points, c1, c2):
    # points : liste d'objets complexes représentant les sommets d'un polygone convexe.
    # c1/c2 : points complexes définissant la ligne de coupe (le segment qui coupe le polygone).
    # On "referme" le polygone en ajoutant le premier point à la fin de la liste.
    points.append(points[0])
    # Calcul du vecteur de référence pour la coupe (ligne de coupe).
    ref_vec = c2 - c1
    # Variable pour stocker, plus tard, le premier point d'intersection détecté.
    cross_point1 = None
    # Variable de "flag" servant à sommer les signes des produits vectoriels pour détecter le côté.
    flag = 0
    # On parcourt chaque segment du polygone (points consécutifs).
    for i, segment in enumerate(zip(points, points[1:])):
        # Dépaquetage du tuple pour les deux points du segment courant.
        p1, p2 = segment
        # Calcul du produit vectoriel entre le vecteur de coupe et le vecteur du point par rapport à c1.
        cross1 = cross(ref_vec, p1 - c1)
        cross2 = cross(ref_vec, p2 - c1)
        # On additionne cross1 à flag, ce qui permet de détecter le côté global du polygone.
        flag += cross1
        # Si le segment croise la ligne de coupe d'un côté à l'autre.
        if cross1 <= 0 and cross2 > 0:
            # Un des deux points est du "mauvais" côté, donc intersection : on récupère le cross point.
            cross_point1 = cross_point(c1, c2, p1, p2)
            # On ignore les premiers points déjà "coupés" du polygone.
            points = points[i+1:]
            break
        # Cas symétrique où le segment croise dans l'autre sens.
        elif cross1 > 0 and cross2 <= 0:
            cross_point1 = cross_point(c1, c2, p1, p2)
            # Ici on prend les points dans l'ordre inverse pour couvrir le reste du polygone incluant l'intersection.
            points = points[i::-1] + points[:i:-1]
            break
    # Si aucune intersection n'a été trouvée lors du parcours.
    if cross_point1 == None:
        # Si le flag est positif, le polygone est complètement d'un côté de la ligne,
        # donc la coupe n'enlève rien (le polygone est entièrement du côté conservé).
        if flag > 0:
            cross_point1 = points[0]   # On prend le coin comme "point d'intersection fictif".
            points = points[1:]        # On enlève le premier point.
        # Sinon, le polygone est entièrement éliminé par la ligne de coupe. On retourne 0 (aucune aire).
        else:
            return 0
    # On va maintenant additionner des aires de triangles pour estimer l'aire du polygone coupé.
    cut_area = 0
    # On parcourt à nouveau les segments restants du polygone "coupé".
    for p1, p2 in zip(points, points[1:]):
        # Si un segment recroise la ligne de coupe (signes opposés ou nul).
        if cross(ref_vec, p1 - c1) * cross(ref_vec, p2 - c1) <= 0:
            # Calcul du second point d'intersection.
            cross_point2 = cross_point(c1, c2, p1, p2)
            # Additionne l'aire du triangle formé par :
            # - le premier point d'intersection,
            # - le second point d'intersection,
            # - le premier point du segment.
            cut_area += _area_of_triangle(cross_point1, cross_point2, p1)
            break   # Fin, car on a traité la coupe.
        # Sinon, on additionne l'aire du triangle formé par le point d'intersection initial
        # et le segment courant.
        else:
            cut_area += _area_of_triangle(cross_point1, p1, p2)
    # Retourne l'aire totale de la portion coupée du polygone.
    return cut_area

# Importation du module système pour la gestion des entrées/sorties standard (stdin/stdout).
import sys

# Définit file_input comme la "standard input" (entrée standard, habituellement le clavier ou un fichier redirigé).
file_input = sys.stdin

# Lecture du nombre de sommets du polygone, attendu sur la première ligne de l'entrée.
n = int(file_input.readline())

# Fonction pour convertir une chaîne de caractères (ex: "1.0 2.0") en un nombre complexe (1.0 + 2.0j).
def string_to_complex(s):
    # Prend une chaîne, sépare en x et y avec split(),
    # convertit en float puis crée un nombre complexe x + y*1j.
    x, y = map(float, s.split())
    # x est la partie réelle, y est la partie imaginaire du complexe.
    return x + y * 1j

# Lecture des sommets du polygone depuis l'entrée standard.
# Pour chaque sommet, on lit une ligne, on la convertit en complexe, et on ajoute à la liste G.
G = [string_to_complex(file_input.readline()) for i in range(n)]

# Lecture du nombre de requêtes, une par ligne, indiquant les lignes de coupe à traiter.
q = int(file_input.readline())

# Pour chaque ligne suivante de l'entrée (correspond à une requête de coupe):
for line in file_input:
    # On extrait les 4 entiers de la ligne, séparés par des espaces,
    # représentant les coordonnées de deux points de la ligne de coupe.
    p1x, p1y, p2x, p2y = map(int, line.split())
    # Création des points complexes pour les extrémités de la ligne de coupe.
    p1 = p1x + p1y * 1j
    p2 = p2x + p2y * 1j
    # On fait une copie du polygone G pour chaque requête,
    # afin que les modifications internes à convex_cut (append) ne se répercutent pas sur la liste d'origine.
    ans = convex_cut(G.copy(), p1, p2)
    # Affichage du résultat (l'aire de la portion coupée) formaté en virgule flottante.
    print("{:f}".format(ans))