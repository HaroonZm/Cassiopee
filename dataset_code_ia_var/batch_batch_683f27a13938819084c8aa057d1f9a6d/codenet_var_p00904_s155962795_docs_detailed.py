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

# Augmenter la limite maximale de récursion pour éviter les erreurs de récursion dans certains environnements
sys.setrecursionlimit(10 ** 7)

# Définition de constantes globales largement utilisées dans la résolution de problèmes mathématiques ou algorithmiques
inf = 10 ** 20  # Une valeur représentant l'infini
eps = 1.0 / 10 ** 10  # Une petite valeur epsilon, utile pour les comparaisons flottantes
mod = 998244353  # Un module premier fréquemment utilisé dans les concours de programmation
dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Déplacements basiques (haut, droite, bas, gauche) sur une grille
ddn = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]  # Cases voisines à 8 directions

def LI():
    """
    Lit une ligne de l'entrée standard, la découpe en éléments, puis convertit chacun en entier.
    
    Returns:
        list: Une liste d'entiers lus depuis la console.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne de l'entrée standard, la découpe en éléments, puis convertit chacun en entier avec -1.
    Utile pour utiliser des indexations basées sur 0.
    
    Returns:
        list: Une liste d'entiers (chacun diminué de 1) lus depuis la console.
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard, la découpe en éléments, puis convertit chacun en float.
    
    Returns:
        list: Une liste de flottants lus depuis la console.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et la découpe en mots.
    
    Returns:
        list: Une liste de chaînes de caractères, segments de la ligne lue.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne de l'entrée standard et convertit en entier.
    
    Returns:
        int: L'entier lu depuis la console.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne de l'entrée standard et convertit en float.
    
    Returns:
        float: Le flottant lu depuis la console.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée standard à l'aide de input().
    
    Returns:
        str: La chaîne de caractères lue depuis la console.
    """
    return input()

def pf(s):
    """
    Affiche une chaîne de caractères immédiatement (flush le buffer).
    
    Args:
        s: La chaîne à afficher.
    """
    return print(s, flush=True)

def main():
    """
    Programme principal.
    
    Effectue le calcul suivant :
    Pour chaque couple d'entiers (a, b) lu en entrée,
    calcule t = a^2 + b^2.
    Pour chaque t, détermine si t admet une décomposition particulière en deux sommes de carrés distinctes (>1).
    Si c'est le cas, retourne 'C', sinon 'P', pour chaque couple.
    
    Returns:
        str: Une chaîne multi-lignes où chaque ligne correspond à la lettre ('C' ou 'P') pour chaque couple (a, b) lu.
    """
    rr = []  # Liste des résultats à afficher

    # Génération de tous les entiers pouvant être exprimés comme la somme de deux carrés, jusqu'à M
    M = 20000
    s = set()
    upper = int(M ** 0.5) + 1
    for i in range(upper):
        for j in range(upper):
            t = i ** 2 + j ** 2
            if t > 1:
                s.add(t)  # Nous n'incluons pas 0 ni 1

    n = I()  # Nombre de couples à traiter
    ni = 0
    while ni < n:
        ni += 1
        a, b = LI()
        t = a ** 2 + b ** 2  # Calcul de la somme des carrés
        r = 'P'  # Par défaut, le résultat est 'P'
        # Recherche d'une décomposition particulière de t
        for c in s:
            # Vérifie si c divise t et si t // c fait aussi partie de s
            if t % c == 0 and t // c in s:
                r = 'C'
                break

        rr.append(r)

    # Retourne chaque résultat sur une ligne séparée
    return '\n'.join(map(str, rr))

# Point d'entrée du programme. Affiche le résultat de main().
print(main())