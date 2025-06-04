from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce

# Augmente la limite de récursion pour les cas où la profondeur d'appel est très élevée
sys.setrecursionlimit(2147483647)

# Définition d'une valeur d'infini utilisée pour les grands entiers
INF = 10 ** 13

def LI():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste d'entiers.
    
    Returns:
        list: Liste des entiers lus.
    """
    return list(map(int, sys.stdin.readline().split()))

def I():
    """
    Lit une ligne de l'entrée standard et la convertit en entier.
    
    Returns:
        int: Entier lu.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une ligne de l'entrée standard, la nettoie et la découpe en une liste de chaînes.
    
    Returns:
        list: Liste des chaînes lues.
    """
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

def S():
    """
    Lit une ligne de l'entrée standard et la retourne sous forme de chaîne.
    
    Returns:
        str: Chaîne lue.
    """
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')

def IR(n):
    """
    Lit n entiers (un par ligne) à partir de l'entrée standard.
    
    Args:
        n (int): Nombre de lignes à lire.

    Returns:
        list: Liste des entiers lus.
    """
    return [I() for i in range(n)]

def LIR(n):
    """
    Lit n lignes à partir de l'entrée standard.
    Chaque ligne est convertie en une liste d'entiers.
    
    Args:
        n (int): Nombre de lignes à lire.
    
    Returns:
        list: Liste de listes d'entiers.
    """
    return [LI() for i in range(n)]

def SR(n):
    """
    Lit n chaînes (une par ligne) à partir de l'entrée standard.
    
    Args:
        n (int): Nombre de lignes à lire.
    
    Returns:
        list: Liste de chaînes lues.
    """
    return [S() for i in range(n)]

def LSR(n):
    """
    Lit n lignes depuis l'entrée standard et les découpe en listes de chaînes.
    
    Args:
        n (int): Nombre de lignes à lire.
    
    Returns:
        list: Liste de listes de chaînes.
    """
    return [LS() for i in range(n)]

def SRL(n):
    """
    Lit n lignes à partir de l'entrée standard, convertit chaque ligne en une liste de caractères.
    
    Args:
        n (int): Nombre de lignes à lire.
    
    Returns:
        list: Liste de listes de caractères.
    """
    return [list(S()) for i in range(n)]

def MSRL(n):
    """
    Lit n lignes à partir de l'entrée standard, chaque ligne représentant des chiffres.
    Convertit chaque ligne en une liste d'entiers.
    
    Args:
        n (int): Nombre de lignes à lire.
    
    Returns:
        list: Liste de listes d'entiers.
    """
    return [[int(j) for j in list(S())] for i in range(n)]

# Modulo utilisé pour éviter les débordements numériques
mod = 10 ** 9 + 7

# Lecture du nombre d'éléments
n = I()    # Nombre d'éléments, lu depuis l'entrée

# Lecture des valeurs H, ajoute une valeur '1' à la fin
H = LI() + [1]   # Liste des hauteurs/valeurs, à laquelle on ajoute '1' à la fin pour la gestion en bordure

# Initialisation du tableau dp (programmation dynamique), tous les états à 1
dp = [1] * (n + 1)  # dp[i] correspond au nombre de façons d'atteindre l'état i à l'étape courante

# Boucle sur chaque étape k, modification dynamique du dp selon H
for k in range(n):
    # Crée une nouvelle liste pour les nouveaux états à cette étape
    new_dp = [0] * (n + 1)  # Mise à zéro avant mise à jour

    # Boucle sur chaque état possible à cette étape
    for i in range(n + 1):

        # Si la valeur courante H[i] est strictement supérieure à H[k]
        if H[i] > H[k]:
            # Double les façons j'atteins le nouvel état en partant de dp[k]
            new_dp[i] = dp[k] * 2

        # Si la valeur précédente est inférieure ou égale à H[i]
        elif H[k - 1] <= H[i]:
            # Prends le dp[i], multiplie par 2*2^{différence des hauteurs}, gestion modulaire
            new_dp[i] = dp[i] * 2 * pow(2, H[k] - H[i], mod)
        
        # Si la valeur précédente est strictement supérieure à la courante
        elif H[k - 1] > H[k]:
            # Mise à jour basée sur la différence du chemin précédent
            new_dp[i] = dp[i] - dp[k] + dp[k] * 2
        
        # Cas général restant pour gestion de transitions complexes
        else:
            new_dp[i] = (dp[i] - dp[k - 1] + dp[k - 1] * 2) * pow(2, H[k] - H[k - 1], mod)
        
        # Prend le reste modulaire pour éviter les débordements négatifs/positifs
        new_dp[i] %= mod

    # Transférer la référence du tableau nouvellement calculé
    dp = new_dp

# Affiche la valeur finale du dp au dernier état
print(dp[-1])