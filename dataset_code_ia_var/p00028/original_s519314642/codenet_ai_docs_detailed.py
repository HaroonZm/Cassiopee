def read_integers():
    """
    Lit des entiers depuis l'entrée standard jusqu'à la fin du flux (EOF).
    Retourne la liste des entiers lus.

    Returns:
        list: une liste d'entiers entrés par l'utilisateur.
    """
    a = []
    try:
        while True:
            # Lire une ligne de l'entrée et convertir en entier, puis ajouter à la liste
            a.append(int(input()))
    except EOFError:
        # Fin du flux d'entrée atteinte ; sortir de la boucle
        pass
    return a

def count_occurrences(numbers, value_range=101):
    """
    Compte le nombre d'occurrences de chaque nombre dans la liste fournie.
    
    Args:
        numbers (list): Liste d'entiers à compter.
        value_range (int): Taille du tableau de comptage, supposant que les valeurs vont de 0 à value_range-1.

    Returns:
        list: Une liste où l'index correspond à la valeur et la valeur à cet index correspond au nombre d'occurrences.
    """
    counts = [0] * value_range
    for n in numbers:
        # Incrémente le compteur pour la valeur rencontrée
        counts[n] += 1
    return counts

def print_most_frequent(numbers, counts):
    """
    Affiche les indices d'éléments dans 'numbers' ayant la fréquence maximale selon 'counts'.
    
    Args:
        numbers (list): La liste initiale d'entiers lus en entrée.
        counts (list): La liste des comptes d'occurrences pour chaque valeur possible.
    """
    max_count = max(counts)  # Recherche de la fréquence maximale
    length = len(numbers)
    for n in range(length):
        # Vérifie si l'élément d'indice n a la fréquence maximale et l'affiche
        if counts[n] == max_count:
            print(n)

def main():
    """
    Fonction principale orchestrant la lecture, le comptage et l'affichage des nombres les plus fréquents.
    """
    # Lire les entiers depuis l'entrée standard
    numbers = read_integers()
    # Compter le nombre d'apparitions de chaque entier (supposé entre 0 et 100 inclus)
    counts = count_occurrences(numbers, value_range=101)
    # Afficher les indices dont le nombre d'occurrences est maximal
    print_most_frequent(numbers, counts)

if __name__ == "__main__":
    main()