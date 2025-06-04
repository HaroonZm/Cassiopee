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

# Définir la profondeur maximale de récursion pour éviter RecursionError sur de grandes expressions
sys.setrecursionlimit(10**7)

# Constantes utilisées dans le programme
inf = 10**20                # Une valeur très grande (utilisée comme +inf)
eps = 1.0 / 10**13          # Précision epsilon (non utilisée ici, mais définie en général)
mod = 10**9+7               # Module courant pour la programmation compétitive
dd = [(-1,0),(0,1),(1,0),(0,-1)]  # Directions pour les grilles (haut, droite, bas, gauche)
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]  # Directions 8-voisins (grille)

def LI():
    """Lit une ligne standard et retourne une liste d'entiers."""
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """Lit une ligne standard et retourne une liste d'entiers (décalés de -1)."""
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """Lit une ligne standard et retourne une liste de flottants."""
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """Lit une ligne standard et retourne une liste de chaînes (spaçées)."""
    return sys.stdin.readline().split()

def I():
    """Lit un entier depuis stdin."""
    return int(sys.stdin.readline())

def F():
    """Lit un flottant depuis stdin."""
    return float(sys.stdin.readline())

def S():
    """Lit une ligne depuis stdin (jusqu'à la nouvelle ligne)."""
    return input()

def pf(s):
    """Affiche s immédiatement (flush stdout)."""
    return print(s, flush=True)

def main():
    """
    Point d'entrée du programme.
    Lit une expression arithmétique depuis stdin, l'analyse, puis trouve
    la valeur maximale que l'on peut obtenir en parenthésant l'expression.

    Returns:
        int: La plus grande valeur atteignable.
    """
    s = S()   # Lit l'expression de l'utilisateur (sous forme de chaîne)
    fm = {}   # Dictionnaire de mémoïsation pour stocker les résultats intermédiaires

    # Analyseur basique: convertit la chaîne s en une liste d'entiers et d'opérateurs/parenthèses
    a = []
    for c in s:
        # Reconnaître un chiffre et l'assembler s'il est consécutif à d'autres chiffres
        if '0' <= c <= '9':
            ci = int(c)
            # Si le précédent élément est un entier, ajouter ce chiffre à l'entier précédent (gestion multi-chiffres)
            if len(a) > 0 and isinstance(a[-1], int):
                a[-1] = a[-1] * 10 + ci
            else:
                a.append(ci)
        else:
            # Ajoute les opérateurs (+, -) et parenthèses
            a.append(c)

    def f(a):
        """
        Fonction récursive qui calcule le minimum et le maximum possibles
        pour une sous-expression représentée par la liste 'a'.

        Args:
            a (list): Sous-expression (liste de chiffres, '+', '-', '(', ')')

        Returns:
            list: [minimum possible, maximum possible] qu'on peut obtenir avec 'a'
        """
        key = tuple(a)
        # Si le résultat est déjà connu pour cette sous-expression, le retourner (mémoïsation)
        if key in fm:
            return fm[key]
        # Cas de base: l'expression est de la forme [x, opérateur, y], impossible, on retourne [inf, -inf]
        if len(a) == 2:
            fm[key] = [inf,-inf]
            return [inf,-inf]
        # Retirer les parenthèses extérieures inutiles
        for i in range(len(a)):
            if a[i] != '(':
                if i > 0:
                    a = a[i:]
                break
        for i in range(len(a)-1,-1,-1):
            if a[i] != ')':
                a = a[:i+1]
                break
        # Si l'expression est simplement un nombre
        if len(a) == 1:
            r = [a[0],a[0]]
            fm[key] = r
            return r

        # On essaie tous les partages par un opérateur valide ('+' ou '-'), sous réserve des positions
        ri = [inf]   # liste des valeurs minimales candidates
        ra = [-inf]  # liste des valeurs maximales candidates
        l = len(a)
        for i in range(1, len(a)-1):
            # On ne considère que les vraies opérations en dehors des parenthèses
            if not a[i] in ['+', '-']:
                continue
            # Vérifie que l'opérateur n'est pas à l'intérieur d'une parenthèse immédiatement ouverte/fermée
            if (i > 1 and a[i-2] == '(') or (i+2 < l and a[i+2] == ')'):
                continue
            fl = f(a[:i])     # valeur (min,max) de la partie gauche
            fr = f(a[i+1:])   # valeur (min,max) de la partie droite
            if a[i] == '+':
                # Min de gauche + min de droite ; Max de gauche + max de droite
                ri.append(fl[0]+fr[0])
                ra.append(fl[1]+fr[1])
            else:
                # Pour le minimum: min de gauche - max de droite ; pour le max: max de gauche - min de droite
                ri.append(fl[0]-fr[1])
                ra.append(fl[1]-fr[0])

        # Prendre la min/max sur tous les candidats
        r = [min(ri), max(ra)]
        fm[key] = r
        return r

    r = f(a)
    # Retourne la valeur maximale atteignable de l'expression
    return r[1]

print(main())