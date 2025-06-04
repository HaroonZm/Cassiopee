def swap_case_from_input():
    """
    Demande à l'utilisateur une chaîne de caractères par le biais de l'entrée standard,
    puis affiche cette chaîne avec les majuscules transformées en minuscules et vice versa.

    Retourne:
        None
    """
    # Demander à l'utilisateur de saisir une chaîne
    a = raw_input()  # Pour Python 2, 'raw_input' lit une ligne de texte entrée par l'utilisateur

    # Utiliser la méthode swapcase pour inverser la casse des caractères de la chaîne
    result = a.swapcase()

    # Afficher le résultat à l'utilisateur
    print result

# Appel de la fonction pour exécuter le programme
swap_case_from_input()