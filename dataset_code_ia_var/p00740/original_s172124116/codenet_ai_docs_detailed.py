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

# Augmente la limite de récursion pour permettre des appels récursifs plus profonds si besoin
sys.setrecursionlimit(10**7)

# Constantes globales
inf = 10**3                # Une valeur d'infini utilisé dans certains algorithmes (pas utilisée ici)
eps = 1.0 / 10**10         # Petite valeur d'erreur pour les comparaisons flottantes (pas utilisée ici)
mod = 10**9+7              # Un modulo commun (pas utilisé ici)

def LI():
    """
    Lecture d'une ligne d'entrée standard, 
    découpe et conversion de chaque élément en entier.

    Returns:
        list[int]: Une liste d'entiers lus à partir de l'entrée.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lecture d'une ligne d'entrée standard, 
    découpe et conversion de chaque élément en entier diminué de 1.
    Utile pour les index commençant à 0.

    Returns:
        list[int]: Une liste d'entiers (indexé à partir de 0) lus à partir de l'entrée.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lecture d'une ligne d'entrée standard et conversion en float.

    Returns:
        list[float]: Une liste de flottants lus à partir de l'entrée.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lecture d'une ligne d'entrée standard et segmentation en mots (chaînes).

    Returns:
        list[str]: Une liste de chaînes lues à partir de l'entrée.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lecture d'un entier à partir de l'entrée standard.

    Returns:
        int: L'entier lu.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lecture d'un nombre flottant à partir de l'entrée standard.

    Returns:
        float: Le float lu.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lecture d'une ligne complète à partir de l'entrée standard.

    Returns:
        str: La chaîne lue.
    """
    return input()

def pf(s):
    """
    Affiche une valeur sur la sortie standard et force le vidage du tampon.

    Args:
        s (Any): L'objet à imprimer.
    """
    print(s, flush=True)

def main():
    """
    Fonction principale qui résout le problème suivant :
    Pour chaque groupe d'entrées (n, p) où n est le nombre de joueurs et p le nombre de pierres,
    simulez un tour de distribution de pierres par un meneur tournant, l'objectif étant de trouver
    quel joueur recevra la dernière pierre restante. Pour chaque cas, retourne l'index du gagnant.

    Entrée:
        Plusieurs lignes, chacune avec deux entiers n (nombre de joueurs) et p (nombre de pierres).
        Fin lorsque n == 0.

    Retourne:
        str: Les index des joueurs gagnants pour chaque cas, séparés par des sauts de ligne.
    """
    rr = []  # Liste des résultats à retourner (index du gagnant pour chaque cas)
    while True:
        n, p = LI()        # Lecture du nombre de joueurs et du nombre de pierres
        mp = p             # Sauvegarde du nombre initial de pierres pour comparaison ultérieure
        if n == 0:         # Condition d'arrêt : aucune entrée à traiter
            break
        a = [0] * n        # Initialisation du stock de chaque joueur à 0
        i = 0              # Index du joueur courant
        while True:
            if p == 0:
                # Si la réserve de pierres est vide, le joueur courant prend toutes ses pierres pour les redistribuer.
                p = a[i]
                a[i] = 0
            else:
                # Donne une pierre au joueur courant
                a[i] += 1
                p -= 1
                # Si un joueur atteint le total initial de pierres, il gagne et la manche s'arrête
                if a[i] == mp:
                    break
            # Passe au joueur suivant (rotation circulaire)
            i = (i + 1) % n
        rr.append(i)       # Ajoute l'index du joueur gagnant

    return '\n'.join(map(str, rr))   # Format et retourne la liste des gagnants sous forme de texte

# Appel du point d'entrée principal du script
print(main())