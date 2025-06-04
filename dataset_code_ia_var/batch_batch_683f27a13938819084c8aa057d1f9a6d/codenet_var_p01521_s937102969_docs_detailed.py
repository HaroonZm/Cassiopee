def main():
    """
    Fonction principale qui lit une chaîne de caractères depuis l'entrée standard,
    puis imprime le caractère 'o' si le premier caractère de la chaîne est 'o'.
    Sinon, elle imprime le dernier caractère de la chaîne.
    """
    # Lecture de l'entrée utilisateur sous forme de chaîne de caractères
    s = input()

    # Vérification du premier caractère de la chaîne
    if s[0] == 'o':
        # Si le premier caractère est 'o', afficher 'o'
        print('o')
    else:
        # Sinon, afficher le dernier caractère de la chaîne
        print(s[-1])

# Appel de la fonction principale
if __name__ == "__main__":
    main()