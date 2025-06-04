def main():
    """
    Demande à l'utilisateur d'entrer du texte, puis affiche ce texte préfixé par 'ABC'.
    """
    # Demande à l'utilisateur une saisie via le clavier
    user_input = input()
    # Affiche la chaîne 'ABC' suivie de la saisie utilisateur
    print("ABC" + user_input)

# Point d'entrée du script
if __name__ == "__main__":
    main()