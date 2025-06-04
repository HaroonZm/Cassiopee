#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect

def LI():
    """
    Lit une ligne de l'entrée standard, la découpe par les espaces et convertit chaque élément en int.

    Returns:
        list of int: Liste d'entiers extraite de la ligne lue.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Lit une ligne de l'entrée standard et la convertit en entier.

    Returns:
        int: L'entier lu.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une ligne de l'entrée standard, la découpe par espaces, puis convertit chaque sous-élément en liste de caractères.

    Returns:
        list of list of str: Liste contenant des listes de caractères pour chaque mot.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Lit une ligne de l'entrée standard et la convertit en liste de caractères (sans retour à la ligne final).

    Returns:
        list of str: Liste de caractères correspondant à la ligne lue.
    """
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    """
    Lit n lignes de l'entrée standard, chaque ligne est convertie en entier.

    Args:
        n (int): Nombre de lignes à lire.

    Returns:
        list of int: Liste des entiers lus.
    """
    return [I() for _ in range(n)]

def LIR(n):
    """
    Lit n lignes de l'entrée standard, chaque ligne est convertie en liste d'entiers.

    Args:
        n (int): Nombre de lignes à lire.

    Returns:
        list of list of int: Liste de listes d'entiers, une par ligne.
    """
    return [LI() for _ in range(n)]

def SR(n):
    """
    Lit n lignes de l'entrée standard, chaque ligne est convertie en liste de caractères.

    Args:
        n (int): Nombre de lignes à lire.

    Returns:
        list of list of str: Liste de listes de caractères, une par ligne.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Lit n lignes de l'entrée standard, chaque ligne est découpée en mots
    puis chaque mot est converti en liste de caractères.

    Args:
        n (int): Nombre de lignes à lire.

    Returns:
        list of list of list of str: Liste contenant pour chaque ligne une liste de mots,
                                    chaque mot étant une liste de caractères.
    """
    return [LS() for _ in range(n)]

# Augmente la limite de profondeur de récursion pour prévenir les erreurs lors de la récursion profonde
sys.setrecursionlimit(1000000)

# Modulo généralement utilisé pour éviter le dépassement de capacité dans les problèmes d'arithmétique modulaire
mod = 1000000007

def solve():
    """
    Fonction principale de résolution du problème.
    Lit un nombre en entrée, regarde le dernier chiffre et affiche une chaîne spécifique :
        - 'hon' si le chiffre est 2, 4, 5, 7 ou 9
        - 'pon' si le chiffre est 0, 1, 6 ou 8
        - 'bon' sinon (donc si le chiffre est 3)
    """
    n = input()  # Lecture de la chaîne de chiffres en entrée
    # Test du dernier caractère pour déterminer le suffixe à afficher
    if n[-1] in "24579":
        print("hon")
    elif n[-1] in "0168":
        print("pon")
    else:
        print("bon")
    return

# Point d'entrée principal du script
if __name__ == "__main__":
    solve()