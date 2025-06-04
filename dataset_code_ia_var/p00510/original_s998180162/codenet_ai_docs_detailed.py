def calculate_max_cars(n, initial_cars, car_movements):
    """
    Calcule le nombre maximum de voitures présentes dans le parking à tout moment,
    en tenant compte des entrées et sorties sur une période donnée.

    Args:
        n (int): Nombre d'itérations ou de périodes.
        initial_cars (int): Nombre initial de voitures présentes dans le parking.
        car_movements (list of tuple): Liste de tuples, chaque tuple contient deux entiers.
                                       Le premier entier est le nombre de voitures qui entrent,
                                       le second est le nombre de voitures qui sortent à chaque période.

    Returns:
        int: Le nombre maximum de voitures présentes dans le parking à un instant donné.
             Renvoie 0 si, à un moment, le nombre de voitures devient négatif (invalide).
    """

    s = m = initial_cars  # s : maximum de voitures, m : nombre courant

    # Parcourir chaque période/tour, mettre à jour les nombres,
    # et suivre le nombre maximum de voitures.
    for i in range(n):
        in_car, out_car = car_movements[i]  # Récupérer les entrées et sorties pour la période courante

        m += in_car - out_car  # Mettre à jour le nombre de voitures dans le parking

        if m < 0:
            # Si le nombre devient négatif, situation invalide, retourner 0
            s = 0
            break
        else:
            # Sinon, mettre à jour la valeur maximale si nécessaire
            s = max(s, m)

    return s


def main():
    """
    Fonction principale du script.
    Lit les entrées de l'utilisateur, appelle la fonction de calcul,
    et affiche le résultat final.
    """

    # Lire le nombre de périodes
    n = int(input())

    # Lire le nombre initial de voitures dans le parking
    initial_cars = int(input())

    # Préparer la liste pour stocker le mouvement des voitures pour chaque période
    car_movements = []

    # Lire les entrées/sorties pour chaque période
    for _ in range(n):
        in_car, out_car = map(int, input().split())
        car_movements.append((in_car, out_car))

    # Calculer le maximum de voitures présentes
    max_cars = calculate_max_cars(n, initial_cars, car_movements)

    # Afficher le résultat
    print(max_cars)


if __name__ == "__main__":
    main()