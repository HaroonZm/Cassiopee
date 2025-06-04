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

# Augmente la limite de récursion pour permettre des appels récursifs profonds (utile pour certains algorithmes)
sys.setrecursionlimit(10**7)

# Constantes globales
inf = 10 ** 20                # Une très grande valeur pour représenter l'infini
eps = 1.0 / 10 ** 10          # Petite valeur epsilon pour les comparaisons flottantes
mod = 998244353               # Modulo fréquemment utilisé pour la programmation compétitive

def LI():
    """
    Lit une ligne de l'entrée standard, sépare les entrées par les espaces,
    convertit chaque élément en int, et retourne la liste d'entiers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Comme LI(), mais décrémente chaque entier de 1 (utile pour indexation 0-based fréquemment utilisée).
    Lit une ligne de l'entrée standard, sépare, convertit en int, puis fait -1 sur chaque élément.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard, sépare par espace, convertit chaque élément en float,
    et retourne la liste de flottants.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard, découpe selon les espaces et retourne la liste des chaînes obtenues.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne de l'entrée standard, enlève les espaces à la fin et retourne la valeur convertie en int.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne de l'entrée standard, enlève les espaces à la fin et retourne la valeur convertie en float.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée standard via input() et retourne la chaîne correspondante (sans modification).
    """
    return input()

def pf(s):
    """
    Affiche la valeur de s en forçant le flush (utile pour forcer l'affichage direct en cas de buffering).
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale exécutant l'algorithme à partir de l'entrée standard.

    Le but est le suivant :
    Pour chaque ligne (au nombre de n fourni en première entrée), la ligne est découpée et analysée :
    - Si le second élément de la ligne est '(', on retire la valeur du troisième élément à t.
    - Sinon, on ajoute la valeur du troisième élément à t.
    À chaque itération, si t vaut 0, on ajoute "Yes" à la liste de résultats, sinon "No".
    À la fin, on retourne tous les résultats ligne par ligne.
    """
    rr = []      # Liste où seront stockés les résultats ('Yes' ou 'No')
    n = I()      # Nombre de lignes à traiter, lu à partir de l'entrée
    ni = 0       # Compteur des lignes traitées
    t = 0        # Accumulateur utilisé dans la logique de chaque ligne

    while ni < n:
        ni += 1
        a = LS()  # Lecture et découpage de la ligne courante (liste de chaînes)

        if a[1] == '(':
            # Si le second élément est '(', on réduit t de la valeur du troisième élément converti en entier
            t -= int(a[2])
        else:
            # Sinon (ie. autre chose, probablement ')'), on incrémente t de la valeur du troisième élément
            t += int(a[2])

        # Si la variable t vaut 0, on ajoute "Yes" à la liste de résultats, sinon "No"
        if t == 0:
            rr.append('Yes')
        else:
            rr.append('No')

    # On retourne tous les résultats, joints par des sauts de ligne
    return '\n'.join(map(str, rr))

# Point d'entrée du script : lance la fonction principale et affiche le résultat
print(main())