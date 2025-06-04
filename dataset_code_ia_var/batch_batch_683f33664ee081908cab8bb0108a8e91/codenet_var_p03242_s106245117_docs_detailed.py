import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

def S():
    """
    Lit une ligne depuis l'entrée standard, enlève les espaces de fin et retourne la chaîne de caractères obtenue.

    Returns:
        str: Ligne d'entrée sans saut de ligne ni espaces de fin.
    """
    return sys.stdin.readline().rstrip()

def M():
    """
    Lit une ligne depuis l'entrée standard, enlève les espaces de fin, divise la ligne en éléments séparés par des espaces,
    convertit chacun de ces éléments en entier et retourne un itérable map des entiers.

    Returns:
        map: Un itérable contenant les entiers extraits depuis la ligne.
    """
    return map(int, sys.stdin.readline().rstrip().split())

def I():
    """
    Lit une ligne depuis l'entrée standard, enlève les espaces de fin et convertit la chaîne résultante en entier.

    Returns:
        int: Entier extrait depuis la ligne d'entrée.
    """
    return int(sys.stdin.readline().rstrip())

def LI():
    """
    Lit une ligne depuis l'entrée standard, enlève les espaces de fin, divise la ligne en éléments séparés par des espaces,
    convertit chacun de ces éléments en entier et retourne une liste d'entiers.

    Returns:
        list: Liste de tous les entiers lus sur la ligne.
    """
    return list(map(int, sys.stdin.readline().rstrip().split()))

def LS():
    """
    Lit une ligne depuis l'entrée standard, enlève les espaces de fin, puis divise la chaîne en une liste de sous-chaînes
    séparées par des espaces.

    Returns:
        list: Liste de chaînes représentant les éléments de la ligne séparés par espaces.
    """
    return list(sys.stdin.readline().rstrip().split())

# Lit une chaîne de caractères depuis l'entrée standard.
N = S()

# Initialise la liste 'ans' qui contiendra le résultat transformé.
ans = []

# Parcourt chaque caractère de la chaîne N.
for c in N:
    # Si le caractère est '1', remplace par '9' dans la liste de sortie.
    if c == '1':
        ans.append('9')
    # Sinon, remplace n'importe quel autre caractère par '1'.
    else:
        ans.append('1')

# Concatène la liste des caractères en une chaîne et affiche le résultat final.
print(''.join(ans))