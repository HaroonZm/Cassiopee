import sys
import math

def polygon_area(poly):
    """
    Calcule l'aire d'un polygone donné par une liste de points (x, y) en utilisant la formule du shoelace.
    Le polygone est supposé simple (non auto-intersectant) et les points sont ordonnés.
    """
    area = 0.0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

def line_from_points(p1, p2):
    """
    Renvoie les coefficients A, B, C de la droite Ax + By + C = 0 passant par p1 et p2.
    """
    x1, y1 = p1
    x2, y2 = p2
    A = y2 - y1
    B = x1 - x2
    C = -(A * x1 + B * y1)
    return A, B, C

def point_side(A, B, C, p):
    """
    Calcule le signe de Ax + By + C pour le point p.
    Si >0, point est d'un côté, si <0 de l'autre.
    """
    x, y = p
    return A * x + B * y + C

def midpoint(p1, p2):
    """
    Calcule le point milieu entre p1 et p2.
    """
    return ((p1[0] + p2[0])/2.0, (p1[1] + p2[1])/2.0)

def cut_polygon(polygon, A, B, C):
    """
    Coupe le polygone par la ligne Ax + By + C = 0 et retourne la partie du polygone où Ax + By + C >= 0.
    Utilise une variante de l'algorithme de découpage de polygone par une demi-droite.
    """
    new_poly = []
    n = len(polygon)
    for i in range(n):
        curr = polygon[i]
        next = polygon[(i+1) % n]
        val_curr = A*curr[0] + B*curr[1] + C
        val_next = A*next[0] + B*next[1] + C

        # Si point courant est du bon côté, on le garde
        if val_curr >= -1e-14:
            new_poly.append(curr)

        # Si on traverse la ligne on insère le point d'intersection
        if val_curr * val_next < -1e-14:
            # Calcul de l'intersection paramétrique
            t = val_curr / (val_curr - val_next)
            ix = curr[0] + t * (next[0] - curr[0])
            iy = curr[1] + t * (next[1] - curr[1])
            new_poly.append((ix, iy))

    # Filtrage corner case : si polygon réduit à moins de 3 points, aire nulle
    if len(new_poly) < 3:
        return []
    return new_poly

def voronoi_cell(island, castles, idx):
    """
    Calcule la cellule de Voronoi (zone du lord idx) limitée par la polygon island.
    - island : liste des sommets (x, y) du polygone de l'île
    - castles : liste des positions des chateaux
    - idx : indice du lord pour lequel on calcule la cellule
    """
    # On commence avec tout l'île
    poly = island[:]

    c0 = castles[idx]
    # Pour chaque autre château, on coupe la zone avec la médiatrice entre c0 et c_other
    for j, c_other in enumerate(castles):
        if j == idx:
            continue

        # Calcul de la médiatrice entre c0 et c_other
        mid = midpoint(c0, c_other)

        # vecteur normal de la médiatrice (perpendiculaire à c_other - c0)
        dx = c_other[0] - c0[0]
        dy = c_other[1] - c0[1]

        # La médiatrice est la droite passant par mid et orthogonale à (dx, dy)
        # donc vecteur normal est (dx, dy), et axe de la droite est (dy, -dx)

        # Equation de la médiatrice: A*x + B*y + C = 0
        # Le vecteur (A,B) est (dx, dy)
        # On veut C = - (A*x0 + B*y0) avec (x0,y0) = mid
        A = dx
        B = dy
        C = -(A * mid[0] + B * mid[1])

        # On veut garder la partie du polygone où c0 est plus proche que c_other
        # Pour cela, on teste le signe de A*x + B*y + C au point c0 et on garde les points du même côté
        side_c0 = A * c0[0] + B * c0[1] + C
        # Si side_c0 < 0 on inverse la coupe
        if side_c0 < 0:
            A, B, C = -A, -B, -C

        # On coupe le polygone actuel avec cette demi-droite
        poly = cut_polygon(poly, A, B, C)
        if not poly:
            break  # zone vide, plus besoin de continuer
    return poly

def main():
    input = sys.stdin.read().strip().split()
    pos = 0
    while True:
        if pos + 2 > len(input):
            break
        N = int(input[pos])
        M = int(input[pos+1])
        pos += 2
        if N == 0 and M == 0:
            break

        # Lire les sommets de l'île
        island = []
        for _ in range(N):
            x = float(input[pos])
            y = float(input[pos+1])
            pos += 2
            island.append((x, y))

        # Lire les chateaux
        castles = []
        for _ in range(M):
            x = float(input[pos])
            y = float(input[pos+1])
            pos += 2
            castles.append((x, y))

        # Calculer la zone de chaque lord et afficher l'aire
        for i in range(M):
            cell = voronoi_cell(island, castles, i)
            area = polygon_area(cell) if cell else 0.0
            # Affichage avec erreur absolue <= 10^-4
            print(area)

if __name__ == "__main__":
    main()