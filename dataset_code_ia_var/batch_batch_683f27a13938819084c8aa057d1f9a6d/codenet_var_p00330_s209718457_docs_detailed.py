def multiply_by_32():
    """
    Demande à l'utilisateur de saisir un nombre entier,
    le multiplie par 32 et affiche le résultat.

    Aucun paramètre n'est requis.
    Aucun retour de valeur.
    """
    # Demander à l'utilisateur de saisir un nombre entier via la console.
    # La fonction input() lit la saisie comme une chaîne de caractères.
    user_input = input("Veuillez entrer un nombre entier : ")
    
    # Convertir la saisie utilisateur de chaîne de caractères en entier.
    integer_value = int(user_input)
    
    # Multiplier la valeur entière par 32.
    result = integer_value * 32
    
    # Afficher le résultat de la multiplication.
    print(result)

# Appeler la fonction pour exécuter le programme principal.
multiply_by_32()