def calculer_cercle_circonscrit_aux_trois_points(liste_points):

    difference_x1 = liste_points[1][0] - liste_points[0][0]
    difference_y1 = liste_points[1][1] - liste_points[0][1]

    difference_x2 = liste_points[2][0] - liste_points[0][0]
    difference_y2 = liste_points[2][1] - liste_points[0][1]

    coefficient_A1 = 2 * difference_x1
    coefficient_B1 = 2 * difference_y1
    coefficient_A2 = 2 * difference_x2
    coefficient_B2 = 2 * difference_y2

    terme_C1 = (liste_points[0][0] ** 2 - liste_points[1][0] ** 2) + (liste_points[0][1] ** 2 - liste_points[1][1] ** 2)
    terme_C2 = (liste_points[0][0] ** 2 - liste_points[2][0] ** 2) + (liste_points[0][1] ** 2 - liste_points[2][1] ** 2)

    denominateur = coefficient_A1 * coefficient_B2 - coefficient_A2 * coefficient_B1

    centre_X = (coefficient_B1 * terme_C2 - coefficient_B2 * terme_C1) / denominateur
    centre_Y = (terme_C1 * coefficient_A2 - terme_C2 * coefficient_A1) / denominateur

    rayon_cercle = ((centre_X - liste_points[0][0]) ** 2 + (centre_Y - liste_points[0][1]) ** 2) ** 0.5

    return tuple(
        map(
            round,
            [centre_X, centre_Y, rayon_cercle],
            [3, 3, 3]
        )
    )

nombre_de_lignes = int(input())

liste_groupes_points = []

for _ in range(nombre_de_lignes):

    points_str = input().split()
    points_floats = list(map(float, points_str))
    groupe_points = list(zip(*[iter(points_floats)] * 2))
    liste_groupes_points.append(groupe_points)

for triplet_points in liste_groupes_points:

    centre_x_arrondi, centre_y_arrondi, rayon_arrondi = calculer_cercle_circonscrit_aux_trois_points(triplet_points)

    print("%.3f %.3f %.3f" % (centre_x_arrondi, centre_y_arrondi, rayon_arrondi))