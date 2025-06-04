import sys
import bisect
import math
import itertools
import string
import queue
import copy
import numpy as np
import scipy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush

# Augmenter la limite de récursion à un grand nombre pour éviter les erreurs de récursion dans des cas extrêmes
sys.setrecursionlimit(10**8)
# Définir le mod pour les opérations de modulos fréquentes
mod = 10**9 + 7

def inp():
    """
    Lit une valeur entière à partir de l'entrée standard.

    Returns:
        int: La valeur entière lue.
    """
    return int(input())

def inpm():
    """
    Lit une ligne d'entiers séparés par un espace à partir de l'entrée standard.

    Returns:
        tuple: Un tuple contenant les entiers lus.
    """
    return map(int, input().split())

def inpl():
    """
    Lit une ligne d'entiers séparés par un espace et les retourne sous forme de liste.

    Returns:
        list: La liste des entiers lus.
    """
    return list(map(int, input().split()))

def inpls():
    """
    Lit une ligne d'entrées séparées par un espace et les retourne sous forme de liste de chaînes.

    Returns:
        list: La liste des chaînes lues.
    """
    return list(input().split())

def inplm(n):
    """
    Lit n entiers, chaque entier provient d'une ligne séparée.

    Args:
        n (int): Le nombre de lignes à lire.

    Returns:
        list: La liste des entiers lus.
    """
    return [int(input()) for _ in range(n)]

def inplL(n):
    """
    Lit n lignes, chaque ligne étant interprétée comme une liste de caractères (chaîne).

    Args:
        n (int): Le nombre de lignes à lire.

    Returns:
        list: Une liste de listes de caractères.
    """
    return [list(input()) for _ in range(n)]

def inplT(n):
    """
    Lit n lignes, chaque ligne étant convertie en tuple de caractères (chaîne).

    Args:
        n (int): Le nombre de lignes à lire.

    Returns:
        list: Une liste de tuples de caractères.
    """
    return [tuple(input()) for _ in range(n)]

def inpll(n):
    """
    Lit n lignes, chaque ligne contenant des entiers séparés par des espaces,
    et retourne une liste de listes.

    Args:
        n (int): Le nombre de lignes à lire.

    Returns:
        list: Une liste de listes d'entiers.
    """
    return [list(map(int, input().split())) for _ in range(n)]

def inplt(n):
    """
    Lit n lignes, chaque ligne contenant des entiers séparés par des espaces,
    et retourne une liste de tuples.

    Args:
        n (int): Le nombre de lignes à lire.

    Returns:
        list: Une liste de tuples d'entiers.
    """
    return [tuple(map(int, input().split())) for _ in range(n)]

def inplls(n):
    """
    Lit n lignes d'entiers séparés par des espaces et retourne une liste
    triée de listes d'entiers.

    Args:
        n (int): Le nombre de lignes à lire.

    Returns:
        list: Une liste triée de listes d'entiers.
    """
    return sorted([list(map(int, input().split())) for _ in range(n)])


# Lecture de la taille du tableau
n = inp()
# Lecture de la liste des entiers
A = inpl()

# Construction de la somme partielle (table de préfixes)
ruiseki = [0]
for i in range(n):
    # Ajoute la somme cumulée jusqu'à A[i]
    ruiseki.append(ruiseki[i] + A[i])

# On compte la fréquence de chaque valeur de la somme partielle
C = Counter(ruiseki)

# Initialiser la réponse à 0
ans = 0

# Pour chaque valeur de fréquence trouvée dans les préfixes
for c in C.values():
    # S'il n'y a qu'une seule occurrence, il n'y a pas de combinaison possible
    if c == 1:
        continue
    # Pour chaque groupe d'occurrences identiques, le nombre de paires est c * (c - 1) // 2
    ans += c * (c - 1) // 2

# Affiche la réponse finale : le nombre de sous-tableaux dont la somme est nulle
print(ans)