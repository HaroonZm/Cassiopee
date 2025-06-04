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

# Augmente la limite de récursion pour accepter des appels récursifs profonds
sys.setrecursionlimit(10**7)

# Définition de constantes utiles
inf = 10 ** 20       # Représente un grand nombre infini
eps = 1.0 / 10 ** 10 # Précision pour la comparaison de flottants
mod = 10 ** 9 + 7    # Modulo commun pour les grands entiers
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]                    # Directions cardinales (haut, droite, bas, gauche)
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] # Directions diagonales et cardinales

def LI():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers.

    Returns:
        list[int]: Liste des entiers lus.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers décrémentés de 1.

    Returns:
        list[int]: Liste des entiers (chacun décrémenté de 1).
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard et retourne une liste de flottants.

    Returns:
        list[float]: Liste des flottants lus.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et retourne une liste de chaînes (mots).

    Returns:
        list[str]: Liste des mots lus.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une seule ligne de l'entrée standard et retourne un entier.

    Returns:
        int: L'entier lu.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une seule ligne de l'entrée standard et retourne un flottant.

    Returns:
        float: Le flottant lu.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée standard en utilisant input().

    Returns:
        str: La ligne lue.
    """
    return input()

def pf(s):
    """
    Affiche la chaîne donnée et force l'affichage immédiat (flush).

    Args:
        s (any): Valeur à afficher.
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale qui lit trois chaînes de paires (lettre, nombre),
    effectue une transformation de pattern/règle sur la première chaîne
    en injectant la troisième là où la seconde apparaît, puis retourne
    la chaîne modifiée compressée au format demandé.
    
    Returns:
        str: La chaîne transformée compressée appropriée pour affichage.
    """

    def inp():
        """
        Lit une chaîne depuis l'entrée, la convertit en une liste alternée
        [lettre1, nombre1, lettre2, nombre2, ...], convertissant chaque nombre
        en entier.

        Returns:
            list: Liste alternant lettres (str) et compteurs (int).
        """
        s = LS()
        a = []
        for i in range(len(s) - 1):
            if i % 2 == 0:
                a.append(s[i])           # Ajoute la lettre
            else:
                a.append(int(s[i]))      # Ajoute le nombre associé à la lettre
        return a

    def com(a):
        """
        Comprime une chaîne alternée (lettre, nombre) en fusionnant
        les paires consécutives ayant la même lettre.

        Args:
            a (list): Chaîne initiale sous forme de liste alternée lettres/nombres.

        Returns:
            list: Chaîne compressée où les mêmes lettres voisines sont fusionnées.
        """
        r = a[:2]
        for i in range(2, len(a), 2):
            if a[i] == r[-2]:            # Même lettre que la précédente ?
                r[-1] += a[i + 1]        # Ajoute le compteur à l'existant
            else:
                r += a[i:i + 2]          # Ajoute la nouvelle lettre et son compteur
        return r

    # Lecture/compression des trois chaînes d'entrée
    a = com(inp()) # Chaîne principale
    b = com(inp()) # Motif à remplacer
    c = com(inp()) # Chaîne de remplacement

    r = []        # Résultat de la transformation
    ff = True     # Drapeau pour ne faire l'opération de remplacement qu'une seule fois

    # Cas où le motif b est de longueur 2 (simple lettre+compteur)
    if len(b) == 2:
        b0 = b[0]
        b1 = b[1]
        for i in range(0, len(a), 2):
            if a[i] == b0:
                # Remplacement du motif autant de fois que possible,
                # mais on ne l'effectue qu'une seule fois (ff == True)
                while a[i + 1] >= b1 and ff:
                    r += c
                    a[i + 1] -= b1
                    ff = False           # On ne remplace plus après la première fois
                if a[i + 1] > 0:
                    r += a[i:i + 2]     # On ajoute le reste s'il en reste
            else:
                r += a[i:i + 2]         # Lettre différente, on la garde telle quelle
    else:
        # Cas où le motif b est composé de plusieurs lettres/comptages
        i = 0
        al = len(a)
        bl = len(b)
        be = bl - 2
        while i < al:
            f = True
            # Vérifie que le motif b apparait à la position courante de a
            for j in range(0, bl, 2):
                ii = i + j
                # Vérifie la correspondance de lettres et compteurs selon la position
                if (al <= ii or a[ii] != b[j] or 
                    (a[ii + 1] < b[j + 1] if j in [0, be] else a[ii + 1] != b[j + 1]) or 
                    not ff):
                    f = False
                    break
            if f:
                # Si le motif correspond on "consomme" les lettres correspondantes de a
                for j in range(0, bl, 2):
                    ii = i + j
                    a[ii + 1] -= b[j + 1]
            if a[i + 1] > 0:
                # Si la lettre n'a pas été entièrement consommée, on la conserve
                r += a[i:i + 2]
            if f:
                # On insère la chaîne de remplacement c, seulement la 1ère fois
                r += c
                ff = False
            i += 2

    # Ajoute le marqueur de fin obligatoire
    r += '$'

    # Fusionne/comprime le résultat final et le formate pour affichage
    return ' '.join(map(str, com(r)))

# Lance le traitement principal et affiche le résultat
print(main())