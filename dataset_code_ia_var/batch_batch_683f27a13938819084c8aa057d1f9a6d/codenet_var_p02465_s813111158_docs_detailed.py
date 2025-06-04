def get_integer_set_from_input():
    """
    Lit une ligne de l'entrée standard contenant des entiers séparés par des espaces
    et retourne un ensemble (set) de ces entiers.

    Returns:
        set: Un ensemble d'entiers lus depuis l'entrée standard.
    """
    # Lecture d'une ligne, transformation en entiers, puis en ensemble
    return set(map(int, input().split()))

def print_sorted_difference(s1, s2):
    """
    Calcule la différence entre deux ensembles d'entiers, trie le résultat,
    et affiche chaque élément de la différence sur une nouvelle ligne si la différence n'est pas vide.

    Args:
        s1 (set): Premier ensemble d'entiers.
        s2 (set): Second ensemble d'entiers à soustraire du premier.
    """
    # Calcul de la différence entre s1 et s2
    difference = s1.difference(s2)
    # Trie la différence et la convertit en liste
    sorted_diff = sorted(difference)
    # Si la liste n'est pas vide, affiche chaque élément sur une nouvelle ligne
    if sorted_diff:
        print('\n'.join(map(str, sorted_diff)))

def main():
    """
    Fonction principale qui gère la lecture des ensembles d'entiers,
    puis affiche les éléments présents uniquement dans le premier ensemble.
    """
    input()  # Lecture du nombre d'éléments du premier ensemble (ignoré)
    s1 = get_integer_set_from_input()  # Lecture des éléments du premier ensemble
    input()  # Lecture du nombre d'éléments du second ensemble (ignoré)
    s2 = get_integer_set_from_input()  # Lecture des éléments du second ensemble
    print_sorted_difference(s1, s2)  # Affichage de la différence triée

if __name__ == "__main__":
    main()