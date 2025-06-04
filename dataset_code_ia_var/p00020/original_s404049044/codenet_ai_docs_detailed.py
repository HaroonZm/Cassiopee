def to_uppercase():
    """
    Demande à l'utilisateur d'entrer une chaîne de caractères,
    convertit cette chaîne en majuscules, puis l'affiche.

    Returns:
        None
    """
    # Sollicite une entrée de la part de l'utilisateur
    user_input = input("Veuillez saisir une chaîne de caractères : ")

    # Convertit la chaîne saisie en majuscules
    uppercase_input = user_input.upper()

    # Affiche la chaîne convertie en majuscules
    print(uppercase_input)

# Appelle la fonction pour exécuter le programme
to_uppercase()