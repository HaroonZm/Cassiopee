import math

# Fonction principale pour trouver les points d'intersection entre deux cercles
def find_circle_cross_points(c1x, c1y, c1r, c2x, c2y, c2r):
    # Calculer la distance entre les deux centres
    dx = c2x - c1x
    dy = c2y - c1y
    d = math.sqrt(dx*dx + dy*dy)
    
    # On sait que d != 0 (centres distincts) et qu'il y a au moins un point d'intersection.
    
    # a est la distance entre c1 et le point de projection de l'intersection sur la ligne entre centres
    a = (c1r**2 - c2r**2 + d**2) / (2 * d)
    # h est la distance entre ce point de projection et chaque point d'intersection perpendiculaire à la ligne centres
    h = math.sqrt(max(0, c1r**2 - a**2))
    
    # Point p2 est la projection de l'intersection sur la ligne entre c1 et c2
    px = c1x + (a * dx) / d
    py = c1y + (a * dy) / d
    
    # Calcul des deux points d'intersection p3_1 et p3_2
    # En cas d'un seul point d'intersection (cercles tangents), h=0 donc les deux points seront égaux
    offset_x = (h * dy) / d
    offset_y = (h * dx) / d
    
    p1x = px - offset_x
    p1y = py + offset_y
    p2x = px + offset_x
    p2y = py - offset_y
    
    # Organisation des points selon la règle:
    # Le point avec x plus petit en premier; en cas d'égalité, celui avec y plus petit en premier
    points = [(p1x, p1y), (p2x, p2y)]
    points.sort(key=lambda p: (p[0], p[1]))
    
    return points

# Lecture des entrées
c1x, c1y, c1r = map(int, input().split())
c2x, c2y, c2r = map(int, input().split())

# Calcul des points croisés
points = find_circle_cross_points(c1x, c1y, c1r, c2x, c2y, c2r)

# Affichage au format demandé avec précision demandée
# Si un seul point d'intersection (capturé par deux points identiques), on répète le même point
if abs(points[0][0] - points[1][0]) < 1e-15 and abs(points[0][1] - points[1][1]) < 1e-15:
    print(f"{points[0][0]:.8f} {points[0][1]:.8f} {points[0][0]:.8f} {points[0][1]:.8f}")
else:
    print(f"{points[0][0]:.8f} {points[0][1]:.8f} {points[1][0]:.8f} {points[1][1]:.8f}")