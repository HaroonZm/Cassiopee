def sum_of_input_numbers():
    """
    Lit une ligne d'entrée utilisateur contenant plusieurs nombres séparés par des espaces,
    convertit chaque élément en entier, puis calcule et affiche la somme de ces nombres.
    
    Exemple d'utilisation:
    Si l'entrée est '1 2 3', la sortie sera '6'.
    """
    # Lecture d'une ligne depuis l'entrée standard,
    # Splitting la chaîne en une liste de sous-chaînes sur les espaces,
    # Conversion de chaque sous-chaîne en entier,
    # Calcul de la somme de ces entiers,
    # Affichage du résultat.
    numbers = input().split()  # Lecture et découpage de l'entrée en une liste de nombres sous forme de chaines
    int_numbers = map(int, numbers)  # Conversion de chaque chaine en entier
    total = sum(int_numbers)  # Calcule de la somme des entiers
    print(total)  # Affiche la somme calculée

sum_of_input_numbers()