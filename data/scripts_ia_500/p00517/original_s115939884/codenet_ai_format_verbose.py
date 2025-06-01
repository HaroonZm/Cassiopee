largeur_plateau, hauteur_plateau, nombre_points = map(int, input().split())

coordonnees_points = []
for _ in range(nombre_points):
    coord_x, coord_y = map(int, input().split())
    coordonnees_points.append([coord_x, coord_y])

position_courante = coordonnees_points.pop(0)
position_x_courante, position_y_courante = position_courante

nombre_deplacements = 0

for position_suivante in coordonnees_points:
    position_x_suivante, position_y_suivante = position_suivante

    while True:
        if position_x_courante == position_x_suivante and position_y_courante == position_y_suivante:
            break

        nombre_deplacements += 1

        if position_x_courante < position_x_suivante and position_y_courante < position_y_suivante:
            position_x_courante += 1
            position_y_courante += 1

        elif position_x_courante == position_x_suivante and position_y_courante < position_y_suivante:
            position_y_courante += 1

        elif position_x_courante > position_x_suivante and position_y_courante < position_y_suivante:
            if position_y_courante != hauteur_plateau:
                position_y_courante += 1
            else:
                position_x_courante -= 1

        elif position_x_courante < position_x_suivante and position_y_courante == position_y_suivante:
            position_x_courante += 1

        elif position_x_courante > position_x_suivante and position_y_courante == position_y_suivante:
            position_x_courante -= 1

        elif position_x_courante < position_x_suivante and position_y_courante > position_y_suivante:
            if position_y_courante != 0:
                position_y_courante -= 1
            else:
                position_x_courante += 1

        elif position_x_courante == position_x_suivante and position_y_courante > position_y_suivante:
            position_y_courante -= 1

        elif position_x_courante > position_x_suivante and position_y_courante > position_y_suivante:
            position_x_courante -= 1
            position_y_courante -= 1

print(nombre_deplacements)