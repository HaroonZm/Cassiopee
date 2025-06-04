from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *
from heapq import *

def read():
    """
    Lit un entier depuis l'entrée standard.
    Returns:
        int: L'entier saisi par l'utilisateur.
    """
    return int(input())

def reads():
    """
    Lit une ligne depuis l'entrée standard, la découpe en éléments séparés par des espaces
    et convertit chaque élément en entier.
    Returns:
        list of int: Liste des entiers lus de l'entrée.
    """
    return [int(x) for x in input().split()]

# Lecture du nombre d'éléments dans la séquence
N = read()

# Lecture de la séquence d'entiers
A = reads()

# Comptage des éléments impairs dans la séquence
c1 = sum(a % 2 == 1 for a in A)  # nombre d'entiers impairs

# Comptage des éléments qui sont multiples de 2 mais pas de 4 (reste 2 modulo 4)
c2 = sum(a % 4 == 2 for a in A)  # nombre d'entiers ≡ 2 (mod 4)

# Comptage des éléments qui sont des multiples de 4 (reste 0 modulo 4)
c4 = sum(a % 4 == 0 for a in A)  # nombre d'entiers ≡ 0 (mod 4), i.e., multiples de 4

# Décision basée sur les règles du problème (habituellement liées à un problème de partition)
if c1 > c4 + 1 or (c1 == c4 + 1 and c2 > 0):
    # Cas où il n'est pas possible de partitionner/réorganiser la séquence selon la règle définie
    print("No")
else:
    # Cas où la condition est respectée
    print("Yes")