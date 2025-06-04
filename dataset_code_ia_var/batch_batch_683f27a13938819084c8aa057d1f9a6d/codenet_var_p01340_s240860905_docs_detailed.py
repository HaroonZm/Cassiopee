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

# Augmente la limite de récursion pour supporter des appels récursifs profonds
sys.setrecursionlimit(10**7)

# Constantes globales utiles pour certains algorithmes
inf = 10 ** 20  # Représente un "infini" numérique
eps = 1.0 / 10 ** 13  # Petite valeur epsilon (précision / tolérance)
mod = 10 ** 9 + 7  # Modulo typique pour les problèmes de type compétitif
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Déplacements 4 directions (haut, droite, bas, gauche)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Déplacements 8 directions

def LI():
    """
    Lit une ligne de l'entrée standard, la découpe en entiers, et renvoie la liste obtenue.

    Returns:
        list[int]: liste des entiers lus de l'entrée.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Comme LI(), mais décrémente chaque entier de la liste (utile pour passer à un indexage 0-based).

    Returns:
        list[int]: liste des entiers (indexés à partir de zéro).
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne, découpe en flottants et retourne la liste.

    Returns:
        list[float]: liste des flottants lus de l'entrée.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et retourne une liste de mots (séparés par des espaces).

    Returns:
        list[str]: liste de chaînes.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit un entier sur une ligne de l'entrée standard.

    Returns:
        int: l'entier lu.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit un flottant sur une ligne de l'entrée standard.

    Returns:
        float: le flottant lu.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de texte de l'entrée standard (hors saut de ligne final).

    Returns:
        str: chaîne de caractères lue.
    """
    return input()

def pf(s):
    """
    Affiche une chaîne de caractères puis s'assure que le tampon de sortie est vidé immédiatement.

    Args:
        s (object): valeur à afficher.
    """
    return print(s, flush=True)

def main():
    """
    Point d'entrée principal du programme.
    Lit une grille de caractères représentant un plateau, identifie la pièce de départ et compte le nombre de cibles 'o'.
    Recherche alors récursivement un chemin depuis la position de départ pour "manger" toutes les cibles, 
    en évitant les allers-retours contraires (i.e. ne pas repartir dans la direction opposée au dernier coup).
    Pour chaque cible touchée, la pièce remplace la position précédente par '.', avance à la cible et recommence,
    jusqu'à ce que toutes les cibles aient été ramassées.
    
    Returns:
        str: la séquence de déplacements pour collecter toutes les cibles, ou None si impossible.
    """
    # Lecture des dimensions de la grille
    h, w = LI()
    # Lecture de la grille (liste de listes de caractères)
    a = [[c for c in S()] for _ in range(h)]

    s = None  # Position et direction initiale de la pièce de départ (i, j, direction)
    lc = 0    # Compteur du nombre de cases à "manger" ('o')
    
    # Recherche la position de départ et compte le nombre de cibles
    for i in range(h):
        for j in range(w):
            c = a[i][j]
            if c == '.':
                continue  # Case vide, rien à faire
            if c == 'o':
                lc += 1   # Compte les cibles
                continue
            s = (i, j, c)  # Trouve la pièce de départ (i, j, direction sous forme de 'R', 'L', 'U' ou 'D')

    def f(i, j, c, d):
        """
        Fonction récursive pour tenter de parcourir la grille à partir de la position (i, j),
        dans la direction c, après avoir déjà collecté d cases 'o'.

        Args:
            i (int): ligne actuelle
            j (int): colonne actuelle
            c (str): direction du dernier déplacement (ou caractère de départ)
            d (int): nombre de cibles déjà mangées

        Returns:
            tuple[bool, str or None]: (est-ce possible ?, chemin correspondant)
        """
        # Si toutes les cibles ont été mangées, réussite
        if d == lc:
            return (True, '')

        # Marque la position actuelle comme vide
        a[i][j] = '.'

        # Essaye d'aller vers le bas, si le dernier coup n'était pas vers le haut
        if c != 'U':
            for k in range(i + 1, h):
                if a[k][j] == 'o':
                    rf, rs = f(k, j, 'D', d + 1)
                    if rf:
                        return (True, 'D' + rs)
                    break  # Ne peut sauter qu'à la première cible rencontrée

        # Essaye d'aller vers le haut, si le dernier coup n'était pas vers le bas
        if c != 'D':
            for k in range(i - 1, -1, -1):
                if a[k][j] == 'o':
                    rf, rs = f(k, j, 'U', d + 1)
                    if rf:
                        return (True, 'U' + rs)
                    break

        # Essaye d'aller vers la droite, si le dernier coup n'était pas vers la gauche
        if c != 'L':
            for k in range(j + 1, w):
                if a[i][k] == 'o':
                    rf, rs = f(i, k, 'R', d + 1)
                    if rf:
                        return (True, 'R' + rs)
                    break

        # Essaye d'aller vers la gauche, si le dernier coup n'était pas vers la droite
        if c != 'R':
            for k in range(j - 1, -1, -1):
                if a[i][k] == 'o':
                    rf, rs = f(i, k, 'L', d + 1)
                    if rf:
                        return (True, 'L' + rs)
                    break

        # Remet la cible (backtracking) et indique un échec pour ce chemin
        a[i][j] = 'o'
        return (False, None)

    # Démarre la recherche récursive à partir de la position initiale
    rf, rs = f(s[0], s[1], s[2], 0)
    return rs

# Lance le programme principal et affiche le résultat
print(main())