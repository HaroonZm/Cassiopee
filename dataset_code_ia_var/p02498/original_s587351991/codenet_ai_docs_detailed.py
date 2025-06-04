def main():
    """
    Lit une chaîne depuis l'entrée standard, convertit chaque majuscule en minuscule et vice versa,
    puis affiche le résultat à l'écran.
    """
    # Demande à l'utilisateur de saisir une chaîne via l'entrée standard
    user_input = raw_input()
    # Inverse la casse : les majuscules deviennent minuscules et vice versa
    swapped = user_input.swapcase()
    # Affiche la chaîne convertie
    print swapped

# Point d'entrée du programme
if __name__ == "__main__":
    main()