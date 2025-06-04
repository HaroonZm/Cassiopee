import math

nombre_de_paires_de_cercles = input()

for indice_paquet in range(nombre_de_paires_de_cercles):

    centre_x_cercle_1, centre_y_cercle_1, rayon_cercle_1, centre_x_cercle_2, centre_y_cercle_2, rayon_cercle_2 = map(float, raw_input().split())

    distance_entre_centres = math.sqrt(
        (centre_x_cercle_1 - centre_x_cercle_2) ** 2 +
        (centre_y_cercle_1 - centre_y_cercle_2) ** 2
    )

    somme_rayons = rayon_cercle_1 + rayon_cercle_2
    difference_absolue_rayons = abs(rayon_cercle_1 - rayon_cercle_2)
    difference_rayons = rayon_cercle_1 - rayon_cercle_2

    if somme_rayons < distance_entre_centres:
        print 0

    elif difference_absolue_rayons <= distance_entre_centres:
        print 1

    elif difference_rayons > distance_entre_centres:
        print 2

    else:
        print -2