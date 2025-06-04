def ceil_division_of_sum():
    """
    Lit deux entiers de l'entrée standard, calcule la somme des deux,
    puis effectue une division entière "plafond" (c'est-à-dire le plus petit entier
    supérieur ou égal au quotient de la somme par le deuxième entier).
    Affiche ensuite ce résultat.

    Exemple :
        Entrée : 7 3
        Affichage : 3
    """
    # Lecture de deux entiers depuis l'entrée standard, séparés par un espace
    a, b = map(int, input().split())
    # Calcul du résultat : (a + b - 1) // b équivaut à un arrondi par excès de a/b
    result = (a + b - 1) // b
    # Affichage du résultat
    print(result)

# Appelle la fonction principale pour exécuter le calcul
ceil_division_of_sum()