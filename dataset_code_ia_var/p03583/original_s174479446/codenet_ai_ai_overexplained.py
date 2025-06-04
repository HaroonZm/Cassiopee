import sys  # Ceci importe le module sys, qui fournit des fonctions et variables utilisées pour manipuler différentes parties du système d'exécution Python, comme les flux d'E/S standard.
import re  # Ceci importe le module re, qui fournit des opérations de recherche de motifs à l'aide d'expressions régulières.
from collections import deque, defaultdict, Counter  # Ceci importe trois classes du module collections :
# deque — permet de créer des files/deques (double-ended queue),
# defaultdict — permet de créer un dictionnaire avec une valeur par défaut automatique,
# Counter — conçu pour compter des objets hashables.
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians  # Ceci importe plusieurs fonctions et constantes mathématiques courantes :
# ceil — arrondi supérieur,
# sqrt — racine carrée,
# hypot — norme euclidienne (hypothénuse),
# factorial — factorielle entière,
# pi — constante Pi (≈3.14159),
# sin, cos — fonctions trigonométriques,
# radians — conversion degrés → radians.
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement  
# Ceci importe plusieurs outils pour effectuer des opérations itératives avancées :
# accumulate — accumulation partielle,
# permutations — permutations de séquences,
# combinations — combinaisons possibles,
# product — produit cartésien,
# groupby — regroupe les données,
# combinations_with_replacement — combinaisons avec répétitions.
from operator import itemgetter, mul  # Ceci importe deux fonctions du module operator :
# itemgetter — extrait des éléments d’une séquence,
# mul — multiplication de deux éléments.
from copy import deepcopy  # Ceci importe deepcopy, qui permet de faire une copie indépendante (profonde) d'un objet.
from string import ascii_lowercase, ascii_uppercase, digits  # Ceci importe :
# ascii_lowercase — la chaîne 'abcdefghijklmnopqrstuvwxyz',
# ascii_uppercase — la chaîne 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
# digits — la chaîne '0123456789'.
from bisect import bisect, bisect_left  # Ceci importe deux fonctions du module bisect :
# bisect — insère une valeur dans une liste triée,
# bisect_left — trouve l'emplacement d'insert de gauche.
from fractions import gcd  # Ceci importe gcd (greatest common divisor), plus grand commun diviseur.
from heapq import heappush, heappop  # Ceci importe heappush et heappop, utiles pour manipuler des files de priorité (heaps).
from functools import reduce  # Cette fonction applique une fonction de façon cumulative à une séquence.

# On redéfinit la fonction input pour utiliser la lecture d'une ligne depuis l'entrée standard (sys.stdin).
# .readline() lit une ligne, .strip() retire les espaces et sauts de lignes inutiles.
def input():
    return sys.stdin.readline().strip()

# Ici INT() est une fonction personnalisée pour lire un entier depuis l'entrée standard.
def INT():
    return int(input())

# MAP() lit une ligne, sépare les éléments par espaces, puis les convertit tous en entiers grâce à map(int, ...).
def MAP():
    return map(int, input().split())

# LIST() fait de même que MAP(), mais encapsule le résultat dans une liste.
def LIST():
    return list(map(int, input().split()))

# ZIP(n) permet de lire n lignes, et de "Zipper" chaque i-ème élément de ces lignes ensemble.
def ZIP(n):
    return zip(*(MAP() for _ in range(n)))

# On ajuste la limite maximale de récursion pour éviter un dépassement de pile dans certains algorithmes récursifs lourds.
sys.setrecursionlimit(10 ** 9)

# INF représente l'infini, souvent utilisé comme valeur sentinelle dans les algorithmes.
INF = float('inf')

# mod est souvent utilisé dans les problèmes de programmation pour faire des calculs modulo un grand nombre premier.
mod = 10 ** 9 + 7

# On lit un entier N depuis l'entrée standard en utilisant notre fonction INT().
N = INT()

# On va chercher trois entiers positifs h, n, w tels que la formule du problème soit satisfaite.
# La plage de h et n est arbitrairement fixée de 1 à 3500 inclus.
for h in range(1, 3501):  # On parcourt toutes les valeurs possibles de h de 1 à 3500.
    for n in range(1, 3501):  # Pour chaque h, on parcourt toutes les valeurs possibles de n.
        # On vérifie si le dénominateur vaut 0 pour éviter une division par zéro.
        if 4 * h * n - N * n - N * h == 0:
            continue  # On saute cette itération si le dénominateur est nul.
        # On calcule la valeur de w selon la formule donnée dans l'énoncé.
        w = N * h * n / (4 * h * n - N * n - N * h)
        # w.is_integer() vérifie que w est un entier, 1 <= w s'assure que w est positif et
        # qu'il vaut au moins 1 car w représente une dimension (probablement).
        if w.is_integer() and 1 <= w:
            # Affiche les trois valeurs trouvées,
            # int(w) convertit explicitement w en un entier (au cas où).
            print(h, n, int(w))
            # On termine le programme dès qu’une solution est trouvée.
            exit()