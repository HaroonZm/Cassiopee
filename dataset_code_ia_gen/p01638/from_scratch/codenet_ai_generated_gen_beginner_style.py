import math

r, x, y, n = map(int, input().split())
p = list(map(int, input().split()))

total_area = math.pi * r * r
angles = [pi * 2 * (pi_ / 100) for pi_ in p]

# fonction pour calculer l'angle de chaque segment par rapport à centre déplacé
def sector_area(cx, cy, r, start_angle, end_angle):
    # on approxime le secteur avec une méthode simple en intégrant des petits segments
    steps = 1000
    delta = (end_angle - start_angle) / steps
    area = 0.0
    for i in range(steps):
        a1 = start_angle + i * delta
        a2 = a1 + delta
        # points sur le cercle pour les deux angles
        x1 = cx + r * math.cos(a1)
        y1 = cy + r * math.sin(a1)
        x2 = cx + r * math.cos(a2)
        y2 = cy + r * math.sin(a2)
        # aire du trapèze formé avec le centre déplacé (cx, cy)
        area += (x1 * y2 - y1 * x2) / 2.0
    return abs(area)

# calculer les aires originales
orig_areas = [total_area * pi_ / 100 for pi_ in p]

result = []
start_angle = math.pi/2  # coordonnées (0,r) correspond à angle pi/2 (vers le haut)
for pi_ in p:
    end_angle = start_angle - 2 * math.pi * pi_ / 100
    area = sector_area(x, y, r, end_angle, start_angle)
    start_angle = end_angle
    result.append(int(area / (total_area * pi_ / 100) * 100))  # pourcentage truncé

print(' '.join(map(str, result)))