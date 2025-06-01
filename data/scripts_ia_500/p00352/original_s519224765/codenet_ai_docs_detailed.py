def moyenne_entiers():
    """
    Lit deux nombres entiers depuis l'entrée standard, séparés par un espace,
    calcule leur moyenne entière (division entière), puis affiche le résultat.

    Étapes :
    1. Lire une ligne d'entrée utilisateur contenant deux entiers séparés par un espace.
    2. Convertir ces entrées en deux entiers, a et b.
    3. Calculer la moyenne entière de ces deux entiers, c'est-à-dire la division entière de leur somme par 2.
    4. Afficher le résultat.
    """
    # Lecture d'une ligne d'entrée utilisateur et séparation des valeurs
    a, b = map(int, input("Entrez deux nombres entiers séparés par un espace : ").split())

    # Calcul de la moyenne entière des deux nombres
    moyenne = (a + b) // 2

    # Affichage du résultat
    print(moyenne)

# Appel de la fonction principale
moyenne_entiers()