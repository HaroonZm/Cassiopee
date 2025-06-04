import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

# Augmente la limite de récursion pour permettre des appels récursifs profonds si nécessaire
sys.setrecursionlimit(10**7)

# Constantes globales
inf = 10**3           # Valeur d'infini pour ce contexte, utilisée dans certains algorithmes
eps = 1.0 / 10**10    # Petite valeur epsilon pour comparaison de flottants
mod = 10**9 + 7       # Modulo communément utilisé dans les problèmes d'arithmétique modulaire

def LI():
    """
    Lit une ligne depuis l'entrée standard, la découpe selon les espaces,
    convertit chaque élément en entier et retourne la liste résultante.
    Returns:
        list[int]: Liste d'entiers lus depuis l'entrée standard.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne d'entiers, diminue chaque entier de 1 (souvent pour transformer des indices 1-based en 0-based),
    puis retourne la liste résultante.
    Returns:
        list[int]: Liste d'entiers décalés de 1 lus depuis l'entrée standard.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard, la divise en flottants, et retourne la liste résultante.
    Returns:
        list[float]: Liste de nombres flottants lus depuis l'entrée standard.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard, la divise selon les espaces, et retourne la liste résultante.
    Returns:
        list[str]: Liste de chaînes de caractères lus depuis l'entrée standard.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne de l'entrée standard et la convertit en entier.
    Returns:
        int: L'entier lu depuis l'entrée standard.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne de l'entrée standard et la convertit en flottant.
    Returns:
        float: Le nombre flottant lu depuis l'entrée standard.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne depuis l'entrée standard avec input().
    Returns:
        str: La chaîne de caractères lue depuis l'entrée standard.
    """
    return input()

def pf(s):
    """
    Affiche la valeur passée en argument puis force le flush du buffer de sortie standard.
    Args:
        s (Any): Valeur à afficher.
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale de traitement du programme.
    Pour chaque entier 'n' fourni (lecture continue jusqu'à ce que n == 0),
    calcule le nombre de manières d'écrire n comme somme de plusieurs entiers consécutifs positifs.
    Retourne les résultats pour chaque 'n' sous forme de chaînes, une par ligne.

    Returns:
        str: Les résultats pour chaque entrée, séparés par des retours à la ligne.
    """
    rr = []  # Liste pour stocker les résultats pour chaque test

    while True:
        n = I()  # Lit la prochaine valeur de n depuis l'entrée
        if n == 0:
            break  # Termine la boucle si l'entrée vaut 0

        r = 0  # Compteur du nombre de façons d'exprimer n comme somme d'entiers consécutifs

        # Teste pour chaque valeur de départ possible i (début de la suite)
        for i in range(1, n):
            t = i  # La somme commence à i
            next_i = i
            # Ajoute des nombres consécutifs jusqu'à ce que la somme atteigne ou dépasse n
            while t < n:
                next_i += 1   # Passage au nombre suivant
                t += next_i   # Ajout à la somme
            if t == n:
                r += 1  # Si la somme est égale à n, incrémente le compteur

        rr.append(r)  # Ajoute le résultat pour ce n à la liste des résultats

    # Concatène tous les résultats en une seule chaîne, séparée par des retours à la ligne
    return '\n'.join(map(str, rr))

# Exécution du programme principal
print(main())