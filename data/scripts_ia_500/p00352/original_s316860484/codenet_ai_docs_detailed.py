def moyenne_entieres():
    """
    Lit deux entiers depuis l'entrée standard, calcul leur moyenne entière,
    puis affiche le résultat.

    La fonction attend que l'utilisateur entre deux nombres entiers séparés par un espace.
    Elle calcule ensuite la moyenne entière (division entière) des deux nombres
    et affiche ce résultat.
    """
    # Lecture de deux entiers séparés par un espace
    a, b = map(int, input("Entrez deux nombres entiers séparés par un espace : ").split())

    # Calcul de la moyenne entière des deux nombres
    moyenne = (a + b) // 2

    # Affichage du résultat
    print(moyenne)


# Appel de la fonction principale
moyenne_entieres()