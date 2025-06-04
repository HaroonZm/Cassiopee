#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect

def LI():
    """
    Lit une seule ligne de l'entrée standard, la découpe en éléments séparés par des espaces,
    convertit chaque élément en entier et retourne la liste résultante.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Lit une seule ligne de l'entrée standard et la convertit en entier.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une seule ligne de l'entrée standard, la découpe en éléments séparés par des espaces,
    transforme chaque élément en liste de caractères et retourne une liste de listes.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Lit une seule ligne de l'entrée standard et la convertit en une liste de caractères.
    Retire le saut de ligne final, s'il existe.
    """
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    """
    Lit 'n' lignes chacunes transformées en entiers et retourne la liste d'entiers.
    Args:
        n (int): nombre de lignes à lire.
    Returns:
        list of int: liste d'entiers lus.
    """
    return [I() for _ in range(n)]

def LIR(n):
    """
    Lit 'n' lignes de l'entrée standard. Chaque ligne est convertie en liste d'entiers.
    Args:
        n (int): nombre de lignes à lire.
    Returns:
        list of list of int: matrices listant les lignes lues.
    """
    return [LI() for _ in range(n)]

def SR(n):
    """
    Lit 'n' lignes de l'entrée standard. Chaque ligne est transformée en liste de caractères.
    Args:
        n (int): nombre de lignes à lire.
    Returns:
        list of list of str: liste des lignes sous forme de listes de caractères.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Lit 'n' lignes de l'entrée standard. Chaque ligne est découpée par espace, 
    chaque élément transformé en liste de caractères.
    Args:
        n (int): nombre de lignes à lire.
    Returns:
        list of list of list of str: structure listant les lignes,
        chaque ligne contenant des listes de caractères pour chaque mot.
    """
    return [LS() for _ in range(n)]

# Définit la limite de récursion du système pour éviter les erreurs de dépassement de pile en cas de récursion profonde.
sys.setrecursionlimit(1000000)

# Modulo standard utilisé pour certains calculs d'arithmétique modulaire.
mod = 1000000007

def solve():
    """
    Fonction principale de résolution du problème.
    Lit la valeur de n et la liste a depuis l'entrée standard.
    En fonction de certaines opérations logiques sur n et les sommes/valeurs de la liste a,
    détermine quel joueur gagne et affiche "First" ou "Second".
    
    Plus précisément :
    - Affiche "First" ou "Second" selon un calcul binaire complexe sur la parité de n, 
      la somme des éléments du tableau a et sa valeur minimale.
    """
    n = I()           # Nombre d'éléments à lire
    a = LI()          # Lecture de la liste d'entiers
    # Le résultat est déterminé par une expression combinant parités de n, somme(a) et min(a)
    # Cela sert à évaluer qui gagne selon la configuration du jeu (par exemple, Nim ou variante close).
    # Indices détaillés :
    # - (n & 1)                : parité de n (1 si impair, 0 si pair)
    # - (sum(a) & 1)           : parité de la somme des éléments de a
    # - (min(a) & 1)           : parité du plus petit élément dans a
    # - 1^x                    : inverse le bit (0 devient 1, 1 devient 0)
    # - L’expression finale contrôle quelle sortie afficher.
    print([
        "First",
        "Second"
    ][((n & 1) & (1 ^ sum(a) & 1)) | ((1 ^ n & 1) & (1 ^ sum(a) & 1) & (1 ^ min(a) & 1))])
    return

# Exécution du programme principal si le script est exécuté directement.
if __name__ == "__main__":
    solve()