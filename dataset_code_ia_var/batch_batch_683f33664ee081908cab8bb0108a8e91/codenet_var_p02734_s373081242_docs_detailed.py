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
import copy
import functools
import time
import random

# Augmente la limite de récursion pour supporter des appels récursifs profonds
sys.setrecursionlimit(10 ** 7)

# Constantes utiles pour les problèmes mathématiques et algorithmiques
inf = 10 ** 20                 # Représente "l'infini"
eps = 1.0 / (10 ** 10)         # Précision epsilon pour comparaison de flottants
mod = 10 ** 9 + 7              # Modulo fréquemment utilisé (nombre premier)
mod2 = 998244353               # Autre modulo souvent utilisé (nombre premier)

# Déplacements sur une grille à 4 directions (haut, droite, bas, gauche)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# Déplacements sur une grille à 8 directions (y compris diagonales)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    """
    Lit une ligne depuis l'entrée standard, la sépare par espaces, la convertit en entiers et retourne la liste d'entiers.
    Returns:
        list of int: Liste des entiers lus sur la ligne standard.
    """
    return list(map(int, sys.stdin.readline().split()))

def LLI():
    """
    Lit toutes les lignes restantes depuis l'entrée standard. Pour chaque ligne, la sépare par espaces et la convertit en liste d'entiers.
    Returns:
        list of list of int: Liste de listes d'entiers pour chaque ligne d'entrée.
    """
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

def LI_():
    """
    Lit une ligne depuis l'entrée standard, sépare par espaces, convertit en entiers en soustrayant 1 à chacun (pour obtenir des indices base zéro), et retourne la liste.
    Returns:
        list of int: Liste des entiers (chaque valeur d'entrée diminuée de 1).
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne depuis l'entrée standard, la sépare par espaces, la convertit en flottants et retourne la liste.
    Returns:
        list of float: Liste des flottants lus sur la ligne standard.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne depuis l'entrée standard et la sépare en une liste de chaînes de caractères par espaces.
    Returns:
        list of str: Liste des chaînes (mots) lues.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne depuis l'entrée standard et la convertit en entier.
    Returns:
        int: L'entier lu.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne depuis l'entrée standard et la convertit en flottant.
    Returns:
        float: Le flottant lu.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée utilisateur via la fonction input().
    Returns:
        str: La chaîne entrée par l'utilisateur.
    """
    return input()

def pf(s):
    """
    Affiche la chaîne s et force la vidange du buffer de sortie (flush).
    Args:
        s (str): La chaîne à afficher.
    """
    return print(s, flush=True)

def pe(s):
    """
    Affiche une chaîne s sur la sortie d'erreur (stderr).
    Args:
        s (str): La chaîne à afficher sur stderr.
    """
    return print(str(s), file=sys.stderr)

def JA(a, sep):
    """
    Convertit tous les éléments d'une liste en chaînes de caractères et les joint avec un séparateur donné.
    Args:
        a (list): Liste d'éléments à joindre.
        sep (str): Séparateur utilisé.
    Returns:
        str: Chaîne résultante.
    """
    return sep.join(map(str, a))

def JAA(a, s, t):
    """
    Pour une liste de listes, convertit chaque élément en str, joint les éléments internes de chaque sous-liste avec `t`, puis joint chaque sous-chaîne obtenue avec `s`.
    Args:
        a (list of list): Liste de listes à joindre.
        s (str): Séparateur entre les sous-listes.
        t (str): Séparateur à l'intérieur de chaque sous-liste.
    Returns:
        str: Chaîne résultante de la jointure.
    """
    return s.join(t.join(map(str, b)) for b in a)

def main():
    """
    Fonction principale du programme. Lit les données d'entrée, exécute le traitement dynamique et retourne le résultat final modulo mod2.
    Retour:
        int: Résultat du calcul dynamique (voir description ci-dessous).
    
    Description algorithmique:
        - Lit deux entiers n et s.
        - Lit une liste de n entiers a.
        - Met en place un tableau dynamique dp où dp[x] représente le nombre de façons d'obtenir la somme x avec les éléments de a considérés jusqu'ici.
        - Effectue des transitions dynamiques pour chaque élément de a, en considérant leur valeur et leur position.
        - Le résultat final est dp[s] modulo mod2.
    """
    n, s = LI()          # Lecture de deux entiers : n (taille de la liste), s (cible de la somme)
    a = LI()             # Lecture de la liste d'entiers de taille n
    r = 0                # Variable inutilisée (peut servir à debugger/usage futur)
    dp = [0] * (s + 1)   # Tableau dynamique, dp[x] = nombre de façons d'obtenir la somme x
    dp[0] = 1            # Il y a 1 façon de faire la somme 0 : en choisissant rien

    for i in range(n):
        ai = a[i]        # Valeur du i-ème élément
        if ai > s:
            # Si la valeur courante est supérieure à s, elle ne peut contribuer à aucune somme <= s
            dp[0] += 1   # On incrémente dp[0] (pour comptabiliser le fait d'ignorer cet élément)
            continue

        # Mise à jour spéciale pour dp[s] en tenant compte de l'élément courant et de sa position
        dp[s] += dp[s - ai] * (n - i)
        dp[s] %= mod2    # On prend le résultat modulo mod2 à chaque mise à jour

        # On met à jour dp[x] pour toutes les sommes possibles en descendant, 
        # pour éviter les interférences lors de l'itération
        for j in range(s - 1, ai - 1, -1):
            dp[j] += dp[j - ai]
            dp[j] %= mod2

        dp[0] += 1       # On incrémente dp[0] à chaque itération (compte du "choix vide" itératif)

    return dp[-1] % mod2 # On retourne dp[s] modulo mod2, nombre total de façons d'obtenir la somme s

print(main())