from collections import Counter

def read_and_ignore_line():
    """
    Lit une ligne d'entrée et ignore la valeur.
    Utilisé pour gérer les entrées inutilisées (souvent la taille d'une séquence).
    """
    input()

def read_int_set():
    """
    Lis une ligne d'entiers depuis l'entrée standard et retourne un ensemble (set) de ces entiers.

    Returns:
        set: Un ensemble contenant tous les entiers de la ligne.
    """
    return set(map(int, input().split()))

def count_elements_in_set(target_set):
    """
    Lit une ligne d'entiers et compte combien sont présents dans le set fourni.

    Args:
        target_set (set): Un ensemble d'entiers à comparer.

    Returns:
        int: Le nombre d'éléments de la nouvelle entrée présents dans le set.
    """
    # On crée un générateur de booléens pour chaque entier de la séquence, True si présent dans le set
    presence_flags = (n in target_set for n in map(int, input().split()))
    # On compte le nombre de True (présence dans le set) grâce au Counter
    count_true = Counter(presence_flags)[True]
    return count_true

# Ignorer la ligne indiquant la taille du premier ensemble
read_and_ignore_line()

# Lecture du premier ensemble d'entiers
s = read_int_set()

# Ignorer la ligne indiquant la taille du deuxième ensemble
read_and_ignore_line()

# Comptage et affichage du nombre d'éléments présents dans le premier ensemble
print(count_elements_in_set(s))