#!/usr/bin/env python3
# AGC17 B - Réécriture commentée et documentée

import sys
import math
import bisect
from heapq import heappush, heappop, heappushpop
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations
from operator import itemgetter

# Définition de constantes utiles :
mod = 10**9 + 7  # Constante de modulo (non utilisée ici)
inf = float('inf')  # Représente l'infini

# On augmente la limite de récursion si jamais on en a besoin pour ce problème (pas utile ici mais peut servir)
sys.setrecursionlimit(1000000000)

def I():
    """
    Lit une ligne d'entrée standard et la convertit en entier.
    Returns:
        int: L'entier lu depuis l'entrée standard.
    """
    return int(sys.stdin.readline())

def LI():
    """
    Lit une ligne depuis l'entrée standard, découpe sur les espaces et convertit chaque élément en entier.
    Returns:
        list of int: La liste des entiers extraits de la ligne saisie.
    """
    return list(map(int, sys.stdin.readline().split()))

# Lecture de l'entrée :
n, a, b, c, d = LI()
# n : Nombre de segments/générations
# a, b : Valeurs de départ et valeur recherchée, respectivement
# c, d : Paramètres de génération de bornes gauche et droite

# Construction de la liste de segments possibles :
f = defaultdict(list)  # Dictionnaire par défaut inutilisé ici
lst = []  # Contiendra les paires de bornes (gauche, droite)
s, t = 0, n-1  # s démarre à 0 (compteur ascendant), t à n-1 (compteur descendant)

for _ in range(n):
    # Calcule les bornes (i, j) pour l'intervalle courant :
    left = a + s*c - t*d
    right = a + s*d - t*c
    lst.append((left, right))
    s += 1  # Incrémente le compteur montant
    t -= 1  # Décrémente le compteur descendant

# Recherche si b appartient à l'un des intervalles calculés :
for i, j in lst:
    # Vérifie si b est inclus dans [i, j] (inclusif)
    if i <= b <= j:
        print('YES')
        quit()  # Arrête immédiatement le programme dès qu'une solution est trouvée

# Si la boucle termine sans trouver de segment contenant b :
print('NO')