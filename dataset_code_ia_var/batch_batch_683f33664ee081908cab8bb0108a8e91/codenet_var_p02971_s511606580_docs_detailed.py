def get_input_list(n):
    """
    Demande à l'utilisateur de saisir n entiers (un par ligne) et retourne ces entiers sous forme de liste.

    Args:
        n (int): Le nombre d'entiers à saisir.

    Returns:
        list of int: La liste des entiers saisis par l'utilisateur.
    """
    input_list = []
    for i in range(n):
        value = int(input())
        input_list.append(value)
    return input_list

def find_two_largest(numbers):
    """
    Trouve les deux plus grandes valeurs distinctes dans une liste d'entiers.

    Args:
        numbers (list of int): La liste des entiers.

    Returns:
        tuple: Un tuple contenant la plus grande valeur et la deuxième plus grande valeur.
    """
    first_max = max(numbers)
    # Création d'une copie de la liste pour éviter de modifier l'originale
    numbers_copy = numbers[:]
    # Suppression d'une occurrence du plus grand élément pour trouver le second
    numbers_copy.remove(first_max)
    second_max = max(numbers_copy)
    return first_max, second_max

def print_results(numbers, first, second):
    """
    Affiche, pour chaque élément de la liste :
      - la deuxième plus grande valeur si l'élément est le plus grand,
      - la plus grande valeur sinon.

    Args:
        numbers (list of int): Liste des entiers à traiter.
        first (int): La plus grande valeur trouvée dans la liste.
        second (int): La deuxième plus grande valeur trouvée dans la liste.
    """
    for value in numbers:
        if value == first:
            print(second)
        else:
            print(first)

def main():
    """
    Point d'entrée principal du script.
    Lit un entier N, puis N entiers, puis affiche pour chaque entier la valeur demandée selon l'énoncé.
    """
    N = int(input())
    ai = get_input_list(N)
    first, second = find_two_largest(ai)
    print_results(ai, first, second)

if __name__ == "__main__":
    main()