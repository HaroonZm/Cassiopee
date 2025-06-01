largeur, hauteur, nombre_points = map(int, input().split())

coordonnees_points = [list(map(int, input().split())) for _ in range(nombre_points)]

distance_totale = 0

for index in range(nombre_points):

    if index == 0:

        x_precedent, y_precedent = coordonnees_points[0]

    else:

        x_courant, y_courant = coordonnees_points[index]

        delta_x = x_courant - x_precedent

        delta_y = y_courant - y_precedent

        if delta_x * delta_y >= 0:

            distance_totale += max(abs(delta_x), abs(delta_y))

        else:

            distance_totale += abs(delta_x) + abs(delta_y)

        x_precedent, y_precedent = x_courant, y_courant

print(distance_totale)