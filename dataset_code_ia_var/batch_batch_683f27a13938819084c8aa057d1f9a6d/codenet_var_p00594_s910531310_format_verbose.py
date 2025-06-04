while True:

    nombre_de_boules = input()

    if nombre_de_boules == 0:
        break

    boules_entrees = raw_input().split()
    couleurs_liste = list(map(int, boules_entrees))
    couleurs_triees = sorted(couleurs_liste)

    couleur_courante = couleurs_triees[0]
    compteur_couleur = 0

    for couleur in couleurs_triees:
        if couleur == couleur_courante:
            compteur_couleur += 1
            if compteur_couleur > nombre_de_boules / 2:
                print couleur_courante
                break
        else:
            couleur_courante = couleur
            compteur_couleur = 1
    else:
        print "NO COLOR"