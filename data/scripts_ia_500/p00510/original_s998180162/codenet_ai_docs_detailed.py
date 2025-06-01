def max_cars_in_parking_lot():
    """
    Calcule le nombre maximum de voitures présentes dans un parking au cours d'une série d'entrées et de sorties.

    L'utilisateur doit fournir en entrée :
    - n : le nombre d'intervalles (périodes pendant lesquelles des voitures entrent ou sortent)
    - m : le nombre initial de voitures dans le parking au début de la première période
    Puis, pour chaque intervalle, deux nombres entiers :
    - in_car : nombre de voitures entrant dans le parking pendant l'intervalle
    - out_car : nombre de voitures sortant du parking pendant l'intervalle

    La fonction met à jour le nombre de voitures présentes après chaque intervalle et garde en mémoire
    le nombre maximal atteint. Si jamais le nombre de voitures devient négatif (ce qui est impossible),
    le programme considère que les données sont invalides et s'arrête immédiatement en affichant 0.

    Enfin, la fonction affiche le nombre maximal de voitures présentes simultanément dans le parking.
    """
    # Lecture du nombre d'intervalles pendant lesquels des voitures entrent/sortent
    n = int(input())

    # Lecture du nombre initial de voitures dans le parking au début
    s = m = int(input())

    # Pour chaque intervalle, on lit le nombre de voitures entrantes et sortantes
    for i in range(n):
        in_car, out_car = map(int, input().split())

        # Mise à jour du nombre actuel de voitures dans le parking
        m += in_car - out_car

        # Si le nombre de voitures devient négatif, les données sont incohérentes
        if m < 0:
            s = 0  # On considère que le maximum n'a pas de sens et on met zéro
            break  # Sortie immédiate de la boucle

        else:
            # On met à jour le maximum de voitures présents simultanément
            s = max(s, m)

    # Affichage du nombre maximal de voitures présentes dans le parking
    print(s)

# Appel de la fonction principale pour exécuter le programme
max_cars_in_parking_lot()