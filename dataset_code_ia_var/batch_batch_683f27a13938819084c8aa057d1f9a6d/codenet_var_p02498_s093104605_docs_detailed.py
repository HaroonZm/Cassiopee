def swapcase_input():
    """
    Lit une chaîne de caractères fournie par l'utilisateur via l'entrée standard, 
    inverse la casse de chaque lettre (les minuscules deviennent majuscules et vice versa),
    puis affiche le résultat.

    Returns:
        None
    """
    # Lire la chaîne saisie par l'utilisateur
    user_input = input()
    # Inverser la casse de chaque caractère de la chaîne
    swapped = user_input.swapcase()
    # Afficher la chaîne avec la casse inversée
    print(swapped)

# Appeler la fonction principale
swapcase_input()