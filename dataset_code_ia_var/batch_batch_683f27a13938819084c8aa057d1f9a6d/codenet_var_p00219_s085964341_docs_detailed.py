def read_and_display_ice_counts():
    """
    Lis des groupes de chiffres via l'entrée utilisateur, compte les occurrences
    de chaque chiffre entre 0 et 9, et affiche un histogramme vertical pour chaque chiffre.
    Répète ce processus jusqu'à ce que l'utilisateur saisisse 0 pour arrêter.

    Entrée utilisateur :
        - Un nombre entier n (nombre de valeurs à lire).
        - n entiers entre 0 et 9.

    Affichage :
        - Pour chaque chiffre de 0 à 9, affiche une ligne contenant
          autant d'étoiles '*' que le chiffre a été saisi, ou un tiret '-' si jamais saisi.
        - Une fois le groupe traité, recommence jusqu'à ce que 0 soit entré pour n.
    """
    while True:
        # Lecture du nombre d'éléments à traiter
        n = int(input())

        # Condition d'arrêt : si n vaut 0, on sort de la boucle
        if n == 0:
            break

        # Initialisation de la liste des compteurs pour chaque chiffre de 0 à 9
        ice = [0] * 10  # ice[i] comptera le nombre de fois que i a été saisi

        # Lecture des n chiffres et incrémentation du compteur correspondant
        for i in range(n):
            digit = int(input())
            ice[digit] += 1

        # Affichage de l'histogramme pour chaque chiffre de 0 à 9
        for i in range(10):
            if ice[i] > 0:
                # Si le chiffre i a été trouvé au moins une fois,
                # afficher autant de '*' que sa fréquence
                for j in range(ice[i]):
                    print("*", sep="", end="")
                print()  # Saut de ligne entre les chiffres
            else:
                # Si le chiffre i n'a jamais été saisi, afficher '-'
                print("-")

# Appel de la fonction principale pour exécuter le programme
read_and_display_ice_counts()