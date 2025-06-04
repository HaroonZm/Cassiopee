def get_weekday_name():
    """
    Demande à l'utilisateur de saisir un entier, calcule son modulo 7,
    puis retourne le nom du jour correspondant dans la semaine
    (format abrégé : "thu", "fri", ..., "wed").

    Returns:
        str: Le nom abrégé du jour de la semaine correspondant à l'entier saisi modulo 7.
    """
    # Liste des noms abrégés des jours de la semaine, commençant par "thu"
    weekdays = ["thu", "fri", "sat", "sun", "mon", "tue", "wed"]

    # Demande à l'utilisateur de saisir un entier
    user_input = input("Entrez un entier pour trouver le jour correspondant : ")

    # Convertit l'entrée utilisateur en un entier
    try:
        day_number = int(user_input)
    except ValueError:
        # Gère le cas où l'utilisateur ne saisit pas un nombre valide
        raise ValueError("Veuillez entrer un nombre entier valide.")

    # Calcule l'indice modulo 7 pour garantir une valeur de 0 à 6
    index = day_number % 7

    # Récupère le nom du jour correspondant dans la liste
    weekday_name = weekdays[index]

    return weekday_name

# Appelle la fonction et affiche le résultat à l'écran
print(get_weekday_name())