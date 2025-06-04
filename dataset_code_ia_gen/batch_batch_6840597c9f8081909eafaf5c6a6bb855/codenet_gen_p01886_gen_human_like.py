import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# On trie les points selon leur coordonnée en x pour envisager les lignes verticales possibles
points.sort(key=lambda p: p[0])

INF = 10**18

# Pré-calcul des min/max en y depuis la gauche
min_y_left = [0]*N
max_y_left = [0]*N
min_y_left[0] = points[0][1]
max_y_left[0] = points[0][1]
for i in range(1, N):
    min_y_left[i] = min(min_y_left[i-1], points[i][1])
    max_y_left[i] = max(max_y_left[i-1], points[i][1])

# Pré-calcul des min/max en y depuis la droite
min_y_right = [0]*N
max_y_right = [0]*N
min_y_right[-1] = points[-1][1]
max_y_right[-1] = points[-1][1]
for i in range(N-2, -1, -1):
    min_y_right[i] = min(min_y_right[i+1], points[i][1])
    max_y_right[i] = max(max_y_right[i+1], points[i][1])

# Pré-calcul des min/max en x pour la gauche et droite (utile pour l'enveloppe)
min_x_left = [0]*N
max_x_left = [0]*N
min_x_left[0] = points[0][0]
max_x_left[0] = points[0][0]
for i in range(1, N):
    min_x_left[i] = min(min_x_left[i-1], points[i][0])
    max_x_left[i] = max(max_x_left[i-1], points[i][0])

min_x_right = [0]*N
max_x_right = [0]*N
min_x_right[-1] = points[-1][0]
max_x_right[-1] = points[-1][0]
for i in range(N-2, -1, -1):
    min_x_right[i] = min(min_x_right[i+1], points[i][0])
    max_x_right[i] = max(max_x_right[i+1], points[i][0])

# Fonction calculant l'aire (rectangle) englobant un ensemble de points données par min/max x,y
def rect_area(min_x, max_x, min_y, max_y):
    if max_x < min_x or max_y < min_y:
        return 0
    return (max_x - min_x) * (max_y - min_y)

# Recherche de la séparation optimale
res = INF

# Cas où tout à gauche (ICPC tous les points, JAG aucun)
area_all = rect_area(min_x_left[-1], max_x_left[-1], min_y_left[-1], max_y_left[-1])
res = min(res, area_all)

# Cas où tout à droite (JAG tous les points, ICPC aucun)
area_all = rect_area(min_x_right[0], max_x_right[0], min_y_right[0], max_y_right[0])
res = min(res, area_all)

# Parcours des séparations possibles entre i et i+1
# La droite verticale doit être placée entre points[i].x et points[i+1].x sans intersecter de ruine
# Donc on considère chaque coupe entre points[i] à gauche et points[i+1] à droite
for i in range(N-1):
    # Si plusieurs points ont même x, on ne peut pas tracer de ligne entre eux
    if points[i][0] == points[i+1][0]:
        continue
    # Aire gauche
    area_left = rect_area(min_x_left[i], max_x_left[i], min_y_left[i], max_y_left[i])
    # Aire droite
    area_right = rect_area(min_x_right[i+1], max_x_right[i+1], min_y_right[i+1], max_y_right[i+1])
    total_area = area_left + area_right
    if total_area < res:
        res = total_area

# Arrondi au plus proche entier
print(round(res))