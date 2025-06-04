def main():
    """
    Lit une chaîne de caractères saisie par l'utilisateur,
    la convertit en majuscules, puis l'affiche.
    """
    # Demander à l'utilisateur de saisir une chaîne via l'entrée standard (console)
    user_input = raw_input()
    # Convertir la chaîne en majuscules à l'aide de la méthode upper()
    uppercased_input = user_input.upper()
    # Afficher le résultat à l'écran
    print(uppercased_input)

# Point d'entrée du script
if __name__ == '__main__':
    main()