def calculate_average():
    """
    Lit deux entiers depuis l'entrée standard, calcule leur moyenne entière, puis affiche le résultat.

    Étapes effectuées :
    1. Lecture d'une ligne d'entrée utilisateur contenant deux entiers séparés par un espace.
    2. Conversion de cette ligne en une liste de deux entiers.
    3. Calcul de la moyenne entière des deux nombres.
    4. Affichage du résultat.
    """
    # Lecture de la ligne d'entrée, on la divise en sous-chaînes par espace, puis on convertit chaque sous-chaîne en entier
    s = list(map(int, input().split()))

    # Calcul de la moyenne des deux premiers nombres de la liste
    avr = int((s[0] + s[1]) / 2)

    # Affichage du résultat
    print(avr)

# Appel de la fonction principale
calculate_average()