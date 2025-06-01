def main():
    """
    Programme principal qui calcule la somme de quatre durées données en minutes,
    puis affiche le résultat en minutes et secondes.

    Étapes :
    1. Lire quatre durées (en secondes) depuis l'entrée standard.
    2. Calculer la somme totale de ces durées.
    3. Convertir cette somme en minutes et secondes.
    4. Afficher le nombre entier de minutes, suivi du reste en secondes.
    """
    # Initialisation de la variable 'time' pour accumuler la somme des durées saisies
    time = 0

    # Boucle pour lire quatre valeurs entières depuis l'entrée standard
    for i in range(4):
        # Conversion de l'entrée en entier avant de l'ajouter à 'time'
        time += int(input())

    # Calcul du nombre total de minutes en divisant le temps total par 60
    minutes = int(time / 60)
    # Calcul du reste en secondes à l'aide de l'opérateur modulo
    seconds = int(time % 60)

    # Affichage du nombre de minutes
    print(minutes)
    # Affichage du reste des secondes
    print(seconds)

if __name__ == "__main__":
    main()