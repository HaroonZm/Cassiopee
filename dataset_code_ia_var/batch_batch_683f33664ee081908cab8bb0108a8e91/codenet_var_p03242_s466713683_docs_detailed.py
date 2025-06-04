def transform_number(input_number):
    """
    Transforme un nombre représenté sous forme de chaîne.
    Pour chaque chiffre de l'entrée :
        - Si le chiffre est '1', il est remplacé par '9'.
        - Sinon, il est remplacé par '1'.

    Args:
        input_number (str): Le nombre à transformer, sous forme de chaîne de caractères.

    Returns:
        str: Le nombre transformé, sous forme de chaîne de caractères.
    """
    ans = []  # Liste pour stocker chaque chiffre transformé

    # Parcourt chaque caractère (chiffre) du nombre d'entrée
    for i in range(len(input_number)):
        if input_number[i] == "1":
            # Si le chiffre courant est '1', ajoute '9' à la liste
            ans.append('9')
        else:
            # Sinon, ajoute '1' à la liste
            ans.append('1')

    # Rejoint la liste des chiffres transformés en une chaîne et la retourne
    return ''.join(ans)

# Lecture de la chaîne d'entrée
N = input()

# Appel de la fonction de transformation et affichage du résultat
print(transform_number(N))