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

# Augmente la limite de récursion afin d'éviter les erreurs de récursion profonde.
sys.setrecursionlimit(10**7)

# Constantes globales utilisées dans le code.
inf = 10**20  # Valeur représentant l'infini.
eps = 1.0 / 10**13  # Précision epsilon pour les calculs flottants.
mod = 10**9 + 9  # Modulo utilisé éventuellement pour les calculs.
dd = [(-1,0), (0,1), (1,0), (0,-1)]  # Déplacements dans les 4 directions (haut, droite, bas, gauche).
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]  # Déplacements dans les 8 directions.

def LI():
    """
    Lit une ligne depuis l'entrée standard et renvoie une liste d'entiers.
    :return: list[int]
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne depuis l'entrée standard et renvoie une liste d'entiers décrémentés de 1.
    :return: list[int]
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne depuis l'entrée standard et renvoie une liste de flottants.
    :return: list[float]
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne depuis l'entrée standard et renvoie une liste de chaînes (par espaces).
    :return: list[str]
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne depuis l'entrée standard et renvoie un entier.
    :return: int
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne depuis l'entrée standard et renvoie un flottant.
    :return: float
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne depuis l'entrée standard et renvoie la chaîne saisie par l'utilisateur.
    :return: str
    """
    return input()

def pf(s):
    """
    Affiche la chaîne s et force le flush du tampon de sortie.
    :param s: chaîne à afficher
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale du programme.  
    Elle lit les cas de test, applique la fonction f à chaque ensemble d'entrées, 
    et retourne la liste des résultats séparés par des retours à la ligne.
    :return: str
    """
    rr = []  # Liste des résultats pour chaque cas de test

    def f(n, s, w, q):
        """
        Génère une séquence de chiffres à partir de l'état initial, 
        applique un algorithme dépendant des paramètres, 
        puis compte des occurrences selon la valeur de q.

        :param n: longueur de la séquence à générer
        :param s: graine de départ pour la génération de la séquence
        :param w: paramètre pour le calcul de l'état suivant
        :param q: paramètre de divisibilité/partition
        :return: int, résultat de l'analyse de la séquence générée
        """
        g = s  # Valeur courante de l'état interne
        a = []  # Liste pour stocker la séquence de chiffres générés

        # Génération de la séquence
        for i in range(n):
            # Extraire le chiffre courant en se basant sur la valeur actuelle de g
            a.append(g // 7 % 10)
            # Mettre à jour la valeur de g pour l'itération prochaine
            if g % 2 == 1:
                g = (g // 2) ^ w
            else:
                g //= 2

        # Cas simple : q divisible par 2 ou 5, traitement direct :
        if q % 2 == 0 or q % 5 == 0:
            r = 0  # Compteur du résultat à renvoyer
            t = 0  # Compteur d'occurrences de chiffres positifs depuis le début
            for c in a:
                if c > 0:
                    t += 1
                if c % q == 0:
                    r += t
            return r

        # Cas général : calcul utilisant du reste modulo q pour des suffixes
        b = [0] * (n + 1)  # Liste pour stocker les valeurs de suffixes modulo q
        k = 1  # Puissance successive de 10 modulo q à chaque position
        # Calculer pour chaque position les valeurs de suffixes modulo q
        for i in range(n-1, -1, -1):
            b[i] = (b[i+1] + a[i] * k) % q
            k = k * 10 % q

        d = collections.defaultdict(int)  # Dictionnaire pour compter les occurrences déjà vues de chaque suffixe
        r = 0  # Résultat final à retourner

        # Boucle sur la séquence pour compter les paires valides
        for i in range(n):
            if a[i] > 0:
                d[b[i]] += 1
            r += d[b[i+1]]
        return r

    # Boucle principale de lecture des cas de test
    while True:
        n, m, l, o = LI()
        if n == 0:
            break  # Fin de l'entrée : n==0
        rr.append(f(n, m, l, o))

    # Retourne les résultats ligne par ligne
    return '\n'.join(map(str, rr))

# Point d’entrée du script
print(main())