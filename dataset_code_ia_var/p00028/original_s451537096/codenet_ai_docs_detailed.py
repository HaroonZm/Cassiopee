def read_input():
    """
    Lit les entiers depuis l'entrée standard jusqu'à une fin de flux (EOF).
    
    Returns:
        list: Une liste d'entiers entrés par l'utilisateur.
    """
    numbers = []
    try:
        while True:
            # Tente de lire une ligne de l'entrée utilisateur, la convertit en entier et l'ajoute à la liste.
            numbers.append(int(input()))
    except EOFError:
        # Sort de la boucle lorsque EOF est rencontré (Ctrl+D sous Unix ou Ctrl+Z sous Windows).
        pass
    return numbers

def compute_frequencies(numbers, max_value=100):
    """
    Construit une liste des fréquences d'apparition pour chaque entier entre 0 et max_value.
    
    Args:
        numbers (list): Liste des entiers dont on veut compter les occurrences.
        max_value (int): La valeur maximale attendue pour les éléments (incluse).

    Returns:
        list: Une liste de longueur max_value+1 où l'indice correspond à un nombre 
              et la valeur à sa fréquence dans 'numbers'.
    """
    counts = [0] * (max_value + 1)
    for n in numbers:
        # Incrémente le compteur à l'indice correspondant à la valeur rencontrée.
        counts[n] += 1
    return counts

def print_modes(numbers):
    """
    Affiche les valeurs apparaissant le plus fréquemment dans la liste 'numbers'.
    Si plusieurs valeurs ont la même fréquence maximale, elles sont toutes affichées 
    dans l'ordre croissant.

    Args:
        numbers (list): Liste des entiers d'origine.
    """
    if not numbers:
        return
    # Calcule la fréquence d'occurrence de chaque entier possible.
    counts = compute_frequencies(numbers)
    # Recherche la fréquence maximale.
    max_count = max(counts)
    # Parcours tous les indices de counts pour trouver ceux ayant la fréquence maximale.
    for value, frequency in enumerate(counts):
        if frequency == max_count:
            # Affiche le nombre qui est un mode (ayant la fréquence maximale).
            print(value)

def main():
    """
    Fonction principale qui lit les données utilisateur, puis affiche les modes.
    """
    # Lit les valeurs depuis l'entrée standard jusqu'à EOF.
    data = read_input()
    # Imprime les modes de la séquence d'entrée.
    print_modes(data)

if __name__ == "__main__":
    main()