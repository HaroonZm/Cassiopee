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

# Augmenter la limite de récursion pour gérer des entrées massives potentielles
sys.setrecursionlimit(10**7)

# Définitions de constantes générales
inf = 10**20       # Valeur représentant l'infini pour les comparaisons
eps = 1.0 / 10**10 # Une petite valeur servant d'epsilon pour la précision flottante
mod = 998244353    # Un modulo classique pour les problèmes de nombres entiers
# Déplacements orthogonaux (haut, droite, bas, gauche)
dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# Déplacements en 8 directions (voisinnage de Moore)
ddn = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def LI():
    """
    Lit une ligne d'entrée standard et la convertit en une liste d'entiers.

    Returns:
        list[int]: Liste d'entiers issue de l'entrée.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne d'entrée et la convertit en liste d'entiers décrémentés de 1 (utile pour les indices 0-based).

    Returns:
        list[int]: Liste d'entiers 0-based issue de l'entrée.
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne d'entrée et la convertit en liste de flottants.

    Returns:
        list[float]: Liste de flottants issue de l'entrée.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne d'entrée et la sépare en une liste de chaînes selon les espaces.

    Returns:
        list[str]: Liste de chaînes (tokens) issue de l'entrée.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une valeur d'entrée et la convertit en entier.

    Returns:
        int: L'entier lu.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une valeur d'entrée et la convertit en flottant.

    Returns:
        float: Le flottant lu.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée standard.

    Returns:
        str: La chaîne lue depuis l'entrée standard.
    """
    return input()

def pf(s):
    """
    Affiche une chaîne avec flush immédiat de la sortie standard.

    Args:
        s (str): La chaîne à afficher.
    """
    print(s, flush=True)

def main():
    """
    Point d'entrée principal du script.
    Ce programme résout un problème (potentiellement d'alignement ou de permutation)
    en lisant des données, générant deux configurations "t", et détermine le minimum
    d'opérations nécessaires pour aligner certains éléments, en comparant avec l'entrée "b".
    Le résultat final est affiché.

    Returns:
        str: Sortie jointe en lignes (ici potentiellement une seule).
    """
    rr = []

    while True:
        # Lire n (nombre d'éléments) et m (nombre de groupes/types)
        n, m = LI()
        # Lire la liste b (cible de permutation/comparaison)
        b = LI()
        # Lire la liste p (compte des éléments de chaque type/groupe)
        p = LI()
        r = inf  # Initier le résultat minimum à l'infini pour prise du min
        t = []

        # Première configuration: construction d'une liste t en alternant 0/1 (selon l'index mod 2)
        for i in range(m):
            t += [i % 2] * p[i]

        # Comparer la distribution des types obtenus à celle de "b" via Counters
        if sorted(collections.Counter(t).items()) == sorted(collections.Counter(b).items()):
            tr = 0      # Nombre minimal d'opérations pour cette configuration
            pi = 0      # Index de recherche dans b des '1'
            for i in range(n):
                if t[i] != 1:
                    continue
                while b[pi] != 1:
                    pi += 1
                # Distance entre la position actuelle dans t et la prochaine position de '1' dans b
                tr += abs(i - pi)
                pi += 1
            r = tr  # Mettre à jour le minimum

        # Deuxième configuration: alternance décalée (i+1)%2
        t = []
        for i in range(m):
            t += [(i + 1) % 2] * p[i]

        if sorted(collections.Counter(t).items()) == sorted(collections.Counter(b).items()):
            tr = 0
            pi = 0
            for i in range(n):
                if t[i] != 1:
                    continue
                while b[pi] != 1:
                    pi += 1
                tr += abs(i - pi)
                pi += 1
            # Prendre le minimum entre cette solution et la précédente
            if r > tr:
                r = tr

        rr.append(r)
        break  # Sortir de la boucle principale (semble conçu pour 1 seule itération)

    # Retourner le résultat sous forme de chaîne, séparée par des sauts de ligne
    return '\n'.join(map(str, rr))

# Exécuter la fonction principale et afficher le résultat
print(main())