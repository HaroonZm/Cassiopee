import copy

def get_integer_input(prompt):
    """
    Demande à l'utilisateur d'entrer un entier via l'invite 'prompt' et retourne la valeur entière.
    Args:
        prompt (str): Le texte affiché pour demander l'entrée de l'utilisateur.
    Returns:
        int: La valeur entière entrée par l'utilisateur.
    """
    return int(input(prompt))

def get_integer_list(size):
    """
    Demande à l'utilisateur de saisir 'size' entiers, un par un, et retourne la liste de ces entiers.
    Args:
        size (int): Le nombre d'entiers à saisir.
    Returns:
        list: Liste des entiers saisis.
    """
    numbers = []
    for i in range(size):
        number = get_integer_input("")
        numbers.append(number)
    return numbers

def print_substitute_max_values(values):
    """
    Pour chaque élément de la liste, affiche le plus grand des autres éléments de la liste.
    Si l'élément courant est le maximum de la liste, affiche le second maximum,
    sinon affiche le maximum.
    Args:
        values (list): Liste d'entiers.
    """
    import copy  # Ce module permet de créer une copie superficielle de la liste

    # Trouve la valeur maximale de la liste
    max_value = max(values)
    # Fait une copie de la liste d'origine pour la comparaison ultérieure
    original_values = copy.copy(values)
    # Supprime la première occurrence du maximum pour trouver le second maximum
    values.remove(max_value)
    second_max = max(values)
    # Parcourt la liste copiée pour afficher le résultat approprié pour chaque élément
    for val in original_values:
        if val == max_value:
            # Si l'élément est le maximum, affiche le second maximum
            print(second_max)
        else:
            # Sinon, affiche le maximum
            print(max_value)

def main():
    """
    Fonction principale du programme. Demande une longueur de liste et les entiers,
    puis affiche, pour chaque entier, le maximum parmi les autres éléments de la liste.
    """
    # Demande la taille de la liste à l'utilisateur
    N = get_integer_input("")
    # Récupère la liste des entiers saisis
    values_list = get_integer_list(N)
    # Affiche le résultat pour chaque élément comme décrit ci-dessus
    print_substitute_max_values(values_list)

if __name__ == "__main__":
    main()