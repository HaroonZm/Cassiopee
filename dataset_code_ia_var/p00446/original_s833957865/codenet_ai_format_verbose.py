while True:

    nombre_de_cartes_du_joueur_1 = input()

    if nombre_de_cartes_du_joueur_1 == 0:
        break

    cartes_du_joueur_1 = sorted([input() for index in range(nombre_de_cartes_du_joueur_1)])

    cartes_totales = list(range(1, 2 * nombre_de_cartes_du_joueur_1 + 1))

    cartes_du_joueur_2 = [
        carte for carte in cartes_totales if carte not in cartes_du_joueur_1
    ]

    derniere_carte_posee = 0

    tour_du_joueur_1 = True

    while cartes_du_joueur_1 and cartes_du_joueur_2:

        cartes_du_joueur_actuel = (
            cartes_du_joueur_1 if tour_du_joueur_1 else cartes_du_joueur_2
        )

        for index_carte, valeur_carte in enumerate(cartes_du_joueur_actuel):

            if valeur_carte > derniere_carte_posee:
                derniere_carte_posee = cartes_du_joueur_actuel.pop(index_carte)
                break

        else:
            derniere_carte_posee = 0

        tour_du_joueur_1 = not tour_du_joueur_1

    print len(cartes_du_joueur_2)
    print len(cartes_du_joueur_1)