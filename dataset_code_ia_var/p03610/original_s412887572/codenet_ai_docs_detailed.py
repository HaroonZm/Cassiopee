def get_string_odd_positions():
    """
    Demande à l'utilisateur de saisir une chaîne de caractères,
    puis affiche les caractères situés à des positions impaires (1re, 3e, 5e, ...),
    c'est-à-dire ceux avec des indices pairs dans la chaîne (car les indices commencent à 0),
    sans saut de ligne entre les caractères affichés.
    """
    # Demande à l'utilisateur d'entrer une chaîne de caractères, stockée sous forme de liste de caractères
    strings = list(input("Veuillez saisir une chaîne de caractères : "))

    # Parcours chaque indice de la liste de caractères
    for number in range(len(strings)):
        # Vérifie si l'indice est pair (positions 0, 2, 4, ...)
        if number % 2 == 0:
            # Affiche le caractère correspondant sans saut de ligne
            print(strings[number], end="")

# Appel de la fonction principale
get_string_odd_positions()