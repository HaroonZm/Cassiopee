from math import gcd
from functools import reduce
from sys import stdin

def lcm_base(x, y):
    """
    Calcule le plus petit commun multiple (PPCM) de deux entiers x et y.
    
    Args:
        x (int): Premier entier.
        y (int): Deuxième entier.
    
    Returns:
        int: Le PPCM de x et y.
    """
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    """
    Calcule le PPCM d'un nombre variable d'entiers.

    Args:
        *numbers (int): Une suite d'entiers.

    Returns:
        int: Le PPCM de tous les entiers passés en arguments.
    """
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    """
    Calcule le PPCM d'une liste d'entiers.

    Args:
        numbers (list[int]): Liste d'entiers.

    Returns:
        int: Le PPCM de tous les entiers dans la liste.
    """
    return reduce(lcm_base, numbers, 1)

while True:
    # Lecture d'un entier n depuis l'entrée standard
    n = int(stdin.readline())
    # Si n vaut 0, on termine la boucle principale (fin du programme)
    if not n:
        break
    # Lecture de n lignes, chacune contenant deux entiers. Chaque ligne est stockée comme une liste [numérateur, dénominateur]
    s = [list(map(int, stdin.readline().split())) for _ in range(n)]

    # Calcul du PPCM de tous les dénominateurs des fractions lues
    lcmde = lcm_list([r[1] for r in s])

    # Calcul du PPCM des numérateurs ajustés au PPCM des dénominateurs (en les ramenant à un dénominateur commun)
    lcmnu = lcm_list([r[0] * lcmde // r[1] for r in s])

    # Pour chaque fraction, calcul et affichage d'un entier selon la formule :
    # (lcmnu * dénominateur) // lcmde // numérateur
    # Cela représente le facteur qui permet d'homogénéiser les fractions selon les PPCM choisis
    print("\n".join(str(lcmnu * r[1] // lcmde // r[0]) for r in s))