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

# Augmente la limite de récursion pour le programme, utile pour les appels récursifs profonds
sys.setrecursionlimit(10 ** 7)

# Définit des constantes courantes
inf = 10 ** 20  # Représente l'infini pour les comparaisons
eps = 1.0 / 10 ** 10  # Petitesse pour comparer les flottants
mod = 10 ** 9 + 7  # Modulo souvent utilisé dans les problèmes d'arithmétique modulaire

# Déplacements standards pour navigation 4 directions et 8 directions sur une grille
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Haut, droite, bas, gauche
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 8 directions

def LI():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers.
    :return: list[int]
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers -1 (pour les indices 0-based).
    :return: list[int]
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard et retourne une liste de flottants.
    :return: list[float]
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et retourne une liste de chaînes (tokens séparés).
    :return: list[str]
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit un entier depuis l'entrée standard.
    :return: int
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit un flottant depuis l'entrée standard.
    :return: float
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une chaîne depuis l'entrée standard (équivalent à input()).
    :return: str
    """
    return input()

def pf(s):
    """
    Imprime une chaîne et flush la sortie standard.
    :param s: str
    """
    print(s, flush=True)

def bs(f, mi, ma):
    """
    Effectue une recherche binaire pour trouver la plus petite valeur qui invalide la fonction f.
    :param f: Callable[[int], bool] - fonction booléenne de test
    :param mi: int - borne minimale
    :param ma: int - borne maximale (exclue)
    :return: int - borne trouvée
    """
    mm = -1
    while ma > mi:
        mm = (ma + mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

def main():
    """
    Fonction principale du programme.
    Gère la lecture des cas de test, le traitement du problème, puis la sortie des résultats.
    :return: str - toutes les réponses pour chaque cas de test, séparées par des sauts de ligne
    """
    rr = []  # Liste pour stocker les résultats de chaque cas

    def f(hi, hm):
        """
        Résout un cas du problème pour une grille, des mouvements et des points de vie/ressources.
        :param hi: int - Point de vie/ressources initial
        :param hm: int - Point de vie/ressources maximum
        :return: str - 'YES' ou 'NO' selon la réussite du parcours
        """
        n, m = LI()  # Taille de la grille : n lignes et m colonnes
        a = [S() for _ in range(n)]  # Grille de caractères, chaque ligne comme une chaîne
        t = I()  # Nombre d'associations caractère->valeur
        d = {}
        for _ in range(t):
            c, i = LS()
            d[c] = int(i)  # Associe chaque caractère à une valeur entière
        t = I()
        mv = [LS() for _ in range(t)]  # Liste des mouvements (direction, nombre de pas)
        t = I()
        p = [I() for _ in range(t)]  # Liste des points de recharge possibles

        # Convertit la grille de caractères en une grille de valeurs selon le dictionnaire d
        b = [[d[c] for c in s] for s in a]

        cu = [0, 0]  # Position courante sur la grille
        dms = []  # Liste des valeurs rencontrées lors du cheminement
        for c, i in mv:
            i = int(i)
            for _ in range(i):
                if c == 'D':
                    cu[0] += 1
                elif c == 'U':
                    cu[0] -= 1
                elif c == 'R':
                    cu[1] += 1
                else:
                    cu[1] -= 1
                dm = b[cu[0]][cu[1]]
                if dm > 0:
                    dms.append(dm)

        dl = len(dms)  # Nombre d'étapes sur le chemin
        fm = {}  # Mémorisation pour la fonction ff
        sh = hi  # Ressource actuelle
        si = dl  # Index de la première case non franchie

        # Recherche la première étape où la ressource devient insuffisante
        for i in range(dl):
            if dms[i] >= sh:
                si = i
                break
            sh -= dms[i]

        pl = len(p)  # Nombre de bonus utilisables

        def ff(k):
            """
            Calcule l'avancement maximal possible avec une combinaison de bonus.
            :param k: int - masque de bits représentant l'utilisation des bonus
            :return: tuple (position sur le chemin, ressource restante)
            """
            if k == 0:
                return (si, sh)
            if k in fm:
                return fm[k]
            r = (0, sh)
            for i in range(pl):
                if k & (1 << i):
                    ti, th = ff(k - (1 << i))
                    th += p[i]
                    if th > hm:
                        th = hm
                    tj = dl
                    for j in range(ti, dl):
                        if dms[j] >= th:
                            tj = j
                            break
                        th -= dms[j]
                    t_ = (tj, th)
                    if r < t_:
                        r = t_
            fm[k] = r
            return r

        r = ff(2 ** pl - 1)  # Tente toutes les combinaisons de bonus

        # Si la position atteinte est à la fin, c'est réussi
        if r[0] == dl:
            return 'YES'

        return 'NO'

    while True:
        n, m = LI()
        if n == 0:
            break
        rr.append(f(n, m))

    return '\n'.join(map(str, rr))

# Lancement du programme principal
print(main())