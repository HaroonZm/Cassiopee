def calculate_and_print_weight_multiplier():
    """
    Lit un entier depuis l'entrée standard, multiplie cette valeur par 32,
    puis affiche le résultat.

    Étapes :
    1. Demande à l'utilisateur de saisir un entier via l'entrée standard.
    2. Multiplie la valeur saisie par 32.
    3. Affiche le résultat du calcul.

    Aucun paramètre n'est requis.
    Aucun retour de valeur : le résultat est affiché directement.
    """
    # Lecture de l'entier fourni par l'utilisateur depuis l'entrée standard
    W = int(input("Veuillez saisir un entier : "))

    # Calcul du produit de l'entier saisi par 32
    result = W * 32

    # Affichage du résultat du calcul à l'écran
    print(result)

# Appel de la fonction principale pour exécuter le processus
calculate_and_print_weight_multiplier()