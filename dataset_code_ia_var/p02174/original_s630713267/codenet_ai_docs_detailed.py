#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    """
    Lit une ligne depuis l'entrée standard, la découpe sur les espaces, convertit chaque élément en entier.
    Retourne :
        list[int] : une liste d'entiers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Lit une ligne depuis l'entrée standard et la convertit en entier.
    Retourne :
        int : la valeur entière lue.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une ligne depuis l'entrée standard, la découpe sur les espaces, convertit chaque sous-élément en liste de caractères.
    Retourne :
        list[list[str]] : une liste où chaque élément est une liste de caractères représentant un mot.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Lit une ligne depuis l'entrée standard et la convertit en une liste de caractères, sans le retour à la ligne final.
    Retourne :
        list[str] : une liste de caractères, sans le '\n' final.
    """
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    """
    Lit n entiers depuis l'entrée standard, un par ligne.
    Arguments :
        n (int) : le nombre d'entiers à lire.
    Retourne :
        list[int] : une liste contenant les n entiers lus.
    """
    return [I() for _ in range(n)]

def LIR(n):
    """
    Lit n lignes, chaque ligne étant une série d'entiers séparés par des espaces.
    Arguments :
        n (int) : le nombre de lignes à lire.
    Retourne :
        list[list[int]] : une liste contenant n sous-listes d'entiers.
    """
    return [LI() for _ in range(n)]

def SR(n):
    """
    Lit n lignes depuis l'entrée standard, chaque ligne étant convertie en une liste de caractères.
    Arguments :
        n (int) : le nombre de lignes à lire.
    Retourne :
        list[list[str]] : une liste de n listes de caractères.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Lit n lignes depuis l'entrée standard, chaque ligne étant découpée en mots, 
    chaque mot converti en une liste de caractères.
    Arguments :
        n (int) : le nombre de lignes à lire.
    Retourne :
        list[list[list[str]]] : une liste contenant n sous-listes de mots (chaque mot est une liste de caractères).
    """
    return [LS() for _ in range(n)]

# Augmentation de la limite de récursion pour permettre des appels récursifs profonds dans certains algorithmes.
sys.setrecursionlimit(1000000)

# Définition du modulo à utiliser dans les opérations arithmétiques pour éviter les débordements d'entiers.
mod = 998244353

def solve():
    """
    Fonction principale qui résout le problème donné :
    - Lit le nombre d'éléments n.
    - Lit une liste x de n entiers.
    - Pour chaque indice i, calcule une contribution basée sur (2^(n-i-1) * x[i] * (x[i]+1)^i) modulo 'mod'
    - Additionne toutes ces contributions pour obtenir la réponse finale (modulo 'mod') et l'affiche.
    Aucun argument d'entrée.
    Affiche :
        int : le résultat calculé.
    """
    # Lire le nombre d'éléments
    n = I()
    # Lire la liste de n entiers
    x = LI()
    ans = 0  # Initialisation de la réponse
    # Pour chaque élément de la liste
    for i in range(n):
        xi = x[i]
        # Contribution de l'élément xi
        contrib = pow(2, n-i-1, mod) * xi * pow(xi + 1, i, mod)
        ans += contrib
        # Assurer l'invariance du modulo pour éviter les débordements
        if ans >= mod:
            ans %= mod
    print(ans)
    return

if __name__ == "__main__":
    # Démarre le processus principal
    solve()