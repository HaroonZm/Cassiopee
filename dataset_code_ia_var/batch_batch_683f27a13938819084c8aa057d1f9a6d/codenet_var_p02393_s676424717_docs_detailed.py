def main():
    """
    Fonction principale qui lit trois entiers de l'entrée standard, 
    les trie puis les affiche dans l'ordre croissant séparés par un espace.
    """
    # Demander à l'utilisateur de saisir une ligne d'entiers séparés par des espaces
    input_str = raw_input("Veuillez saisir trois entiers séparés par un espace : ")

    # Convertir la chaîne d'entrée en une liste d'entiers à l'aide de la fonction map
    numbers = list(map(int, input_str.split()))

    # Trier la liste d'entiers en ordre croissant
    numbers.sort()

    # Afficher les trois nombres triés, séparés par des espaces
    print numbers[0], numbers[1], numbers[2]

if __name__ == "__main__":
    main()