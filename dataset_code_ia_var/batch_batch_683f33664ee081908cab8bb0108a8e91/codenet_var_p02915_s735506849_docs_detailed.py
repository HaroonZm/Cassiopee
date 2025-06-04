import sys

def get_array():
    """
    Lit une ligne de l'entrée standard, divise la chaîne obtenue en éléments séparés par des espaces,
    et convertit chaque élément en entier pour retourner une liste d'entiers.

    Returns:
        list: Liste d'entiers lus sur une seule ligne de l'entrée standard.
    """
    return list(map(int, sys.stdin.readline().strip().split()))

def get_ints():
    """
    Lit une ligne de l'entrée standard, divise la chaîne obtenue en éléments séparés par des espaces,
    et convertit chaque élément en entier pour retourner un itérable d'entiers.

    Returns:
        map: Un objet map contenant les entiers lus sur une seule ligne de l'entrée standard.
    """
    return map(int, sys.stdin.readline().strip().split())

def input():
    """
    Lit une ligne de l'entrée standard et supprime les espaces en début et fin de ligne.

    Returns:
        str: La ligne lue, sans espaces de début ou de fin.
    """
    return sys.stdin.readline().strip()

# Lecture d'un entier depuis l'entrée standard
n = int(input())

# Calcul et affichage du cube de l'entier lu
print(pow(n, 3))