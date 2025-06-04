#!usr/bin/env python3

# Importation de modules standards de la bibliothèque Python.

# 'defaultdict' permet de créer un dictionnaire avec des valeurs par défaut.
# 'deque' est une liste optimisée pour l'ajout/suppression sur les deux extrémités.
from collections import defaultdict, deque

# 'heappush' et 'heappop' permettent de gérer des files à priorité (tas/min-heap).
from heapq import heappush, heappop

# 'sys' donne accès à des fonctionnalités du système, comme la lecture entrée standard plus efficace.
import sys

# 'math' offre diverses fonctions mathématiques (factorielle, racine, etc.).
import math

# 'bisect' sert pour la recherche et l'insertion dans des listes triées.
import bisect

# 'random' fournit des fonctions générant des nombres pseudo-aléatoires.
import random

# Définition de fonctions utilitaires pour la lecture d'entrée.

# LI() lit une ligne depuis l'entrée standard, la découpe selon les espaces (split()),
# convertit chaque élément en entier (int) et renvoie la liste des entiers.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# I() lit une ligne de l'entrée standard, la convertit en entier et la retourne.
def I():
    return int(sys.stdin.readline())

# LS() lit une ligne, la découpe, transforme chaque bout en liste de caractères : utile pour traiter mots ou chaînes.
def LS():
    return [list(x) for x in sys.stdin.readline().split()]

# S() lit une ligne de l'entrée standard, la convertit en liste de caractères et retire le saut de ligne (\n) final.
def S():
    return list(sys.stdin.readline())[:-1]

# IR(n) lit n entiers scalaires depuis l'entrée standard, la fonction appelle I() n fois et retourne la liste.
def IR(n):
    return [I() for i in range(n)]

# LIR(n) utilise LI() pour lire n lignes, chacune contenant des entiers séparés, retourne une liste de listes d'entiers.
def LIR(n):
    return [LI() for i in range(n)]

# SR(n) lit n lignes depuis l'entrée standard, pour chaque ligne enlève le saut, découpe en liste de caractères.
def SR(n):
    return [S() for i in range(n)]

# LSR(n) utilise LS() pour lire n lignes, chacune découpée en mots puis en liste de caractères.
def LSR(n):
    return [LS() for i in range(n)]

# Modification de la limite maximale de récursion autorisée (utile pour les algorithmes récursifs profonds).
sys.setrecursionlimit(1000000)

# Définition d'une constante 'mod' utilisée pour les calculs de reste modulo un grand nombre premier.
mod = 1000000007

# Fonction pour résoudre le problème A.
def A():
    # Lecture de deux entiers h et w, désignant le nombre de lignes (hauteur) et de colonnes (largeur) de la grille.
    h, w = LI()

    # Lecture des h lignes suivantes, chaque ligne étant convertie en liste de caractères.
    # SR(h) retourne alors une liste de listes de caractères, représentant la grille.
    s = SR(h)

    # Initialisation de la variable 'ans' à 1, représentant la réponse minimale possible.
    ans = 1

    # Parcours de chaque position (y, x) de la grille.
    # On considère toutes les lignes (de 0 à h-1).
    for y in range(h):
        # Pour chaque ligne y, on parcourt toutes les colonnes (de 0 à w-1).
        for x in range(w):
            # On vérifie si la cellule à la position (y, x) contient le caractère "B".
            if s[y][x] == "B":
                # Si la cellule est "B", on parcourt de nouveau toute la grille pour chaque autre "B".
                for y_ in range(h):
                    for x_ in range(w):
                        # On vérifie si la cellule à la position (y_, x_) contient aussi "B".
                        if s[y_][x_] == "B":
                            # Si oui, on calcule la distance de Manhattan entre (y, x) et (y_, x_).
                            # C'est-à-dire |y - y_| + |x - x_|.
                            d = abs(y - y_) + abs(x - x_)
                            # On compare cette distance à la valeur actuelle de 'ans' et on garde le maximum.
                            ans = max(ans, d)

    # Une fois tous les couples de points "B" comparés, on affiche la valeur finale de 'ans'.
    print(ans)
    return

# Les fonctions suivantes sont des versions "squelettes", prêtes à être complétées, nommées alphabétiquement (B, C, ...).
def B():
    # Lecture d'un entier n depuis l'entrée standard
    n = I()
    # Fonction actuellement vide
    return

def C():
    n = I()
    return

def D():
    n = I()
    return

def E():
    n = I()
    return

def F():
    n = I()
    return

def G():
    n = I()
    return

def H():
    n = I()
    return

def I_():
    n = I()
    return

def J():
    n = I()
    return

# Bloc principal vérifiant si ce script est le programme principal exécuté (et non importé comme module)
if __name__ == "__main__":
    # Appel de la fonction A pour exécuter le problème A.
    A()