nombre_points = int(input())
points = [list(map(int, input().split())) for indice_point in range(nombre_points)]
points.sort()

somme_partielle = 0
minimum_valeur_courante = -points[0][0]
valeur_maximale = -10**19
for coord_x, coord_y in points:
    minimum_valeur_courante = min(minimum_valeur_courante, somme_partielle - coord_x)
    valeur_maximale = max(valeur_maximale, somme_partielle + coord_y - coord_x - minimum_valeur_courante)
    somme_partielle += coord_y
print(valeur_maximale)