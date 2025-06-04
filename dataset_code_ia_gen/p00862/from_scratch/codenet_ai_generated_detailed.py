import sys
import math

def dist_point_to_segment(px, py, x1, y1, x2, y2):
    """
    Calcule la distance minimale entre un point P(px, py) 
    et un segment défini par les points (x1, y1) et (x2, y2).
    """
    # vecteur segment
    vx = x2 - x1
    vy = y2 - y1
    # vecteur point vers début segment
    wx = px - x1
    wy = py - y1
    
    c1 = vx*wx + vy*wy
    if c1 <= 0:
        # le plus proche est le point (x1, y1)
        return math.hypot(px - x1, py - y1)
    c2 = vx*vx + vy*vy
    if c2 <= c1:
        # le plus proche est le point (x2, y2)
        return math.hypot(px - x2, py - y2)
    # projection sur le segment
    b = c1 / c2
    pbx = x1 + b*vx
    pby = y1 + b*vy
    return math.hypot(px - pbx, py - pby)

def dist_to_sea(px, py, polygon):
    """
    Pour un point donné, calcule sa distance minimale à l'un des segments 
    bordant le polygone (donc la mer).
    """
    min_dist = float('inf')
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%n]
        d = dist_point_to_segment(px, py, x1, y1, x2, y2)
        if d < min_dist:
            min_dist = d
    return min_dist

def inside_polygon(px, py, polygon):
    """
    Vérifie si un point est à l'intérieur du polygone convexe.
    Comme le polygone est convexe, on peut utiliser un test par produits vectoriels.
    Le polygone est en orientation sens anti horaire.
    On vérifie que pour chaque edge, le point est à gauche (produit vectoriel > 0).
    """
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%n]
        # vecteur bord
        vx = x2 - x1
        vy = y2 - y1
        # vecteur point depuis x1,y1
        wx = px - x1
        wy = py - y1
        cross = vx * wy - vy * wx
        if cross < -1e-14:
            # point hors polygone
            return False
    return True

def solve_dataset(polygon):
    """
    Résout un dataset : trouve le point dans le polygone convexe qui maximise la 
    distance à la mer (bord).
    Approach:
    - On cherche à maximiser la distance minimale aux segments (bord).
    - Le problème est convexe, donc la distance maximale se trouve à l'intérieur.
    - On peut utiliser une méthode d'optimisation par recherche dichotomique ou ternary search 2D.
    - Pour cela, il faut délimiter le rectangle contenant le polygone.
    - Puis utiliser une méthode de recherche 2D (ternary search sur x, puis sur y).
    """

    # bornes du polygone
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    # méthode auxiliaire pour la recherche ternaire sur y pour un x donné
    def ternary_search_y(x):
        low = ymin
        high = ymax
        for _ in range(60):  # 60 itérations suffisent pour précision 1e-15
            y1 = low + (high - low) / 3
            y2 = high - (high - low) / 3
            if inside_polygon(x, y1, polygon):
                d1 = dist_to_sea(x, y1, polygon)
            else:
                d1 = -1
            if inside_polygon(x, y2, polygon):
                d2 = dist_to_sea(x, y2, polygon)
            else:
                d2 = -1
            if d1 < d2:
                low = y1
            else:
                high = y2
        yfinal = (low + high)/2
        if inside_polygon(x, yfinal, polygon):
            return dist_to_sea(x, yfinal, polygon)
        else:
            return -1

    # recherche ternaire sur x, en cherchant la meilleure distance max sur y
    low = xmin
    high = xmax
    for _ in range(60):
        x1 = low + (high - low) / 3
        x2 = high - (high - low) / 3
        d1 = ternary_search_y(x1)
        d2 = ternary_search_y(x2)
        if d1 < d2:
            low = x1
        else:
            high = x2

    # calcul final sur point trouvé
    xfinal = (low + high)/2
    # on cherche y optimal pour ce xfinal (encore 60 itérations)
    lowy = ymin
    highy = ymax
    for _ in range(60):
        y1 = lowy + (highy - lowy) / 3
        y2 = highy - (highy - lowy) / 3
        if inside_polygon(xfinal, y1, polygon):
            d1 = dist_to_sea(xfinal, y1, polygon)
        else:
            d1 = -1
        if inside_polygon(xfinal, y2, polygon):
            d2 = dist_to_sea(xfinal, y2, polygon)
        else:
            d2 = -1
        if d1 < d2:
            lowy = y1
        else:
            highy = y2
    yfinal = (lowy + highy) / 2
    max_dist = dist_to_sea(xfinal, yfinal, polygon)
    return max_dist

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = input_lines[idx].strip()
        idx += 1
        if n == '0':
            break
        n = int(n)
        polygon = []
        for _ in range(n):
            x, y = map(int, input_lines[idx].split())
            idx += 1
            polygon.append( (x,y) )
        # résoudre ce dataset
        res = solve_dataset(polygon)
        # afficher sans espaces et avec précision suffisante
        print(f"{res:.6f}")

if __name__ == "__main__":
    main()