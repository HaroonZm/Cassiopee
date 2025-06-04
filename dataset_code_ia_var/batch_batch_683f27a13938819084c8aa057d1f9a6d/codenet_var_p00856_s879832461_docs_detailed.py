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

# Augmentation de la limite de récursion pour les grands cas
sys.setrecursionlimit(10**7)

# Définition de constantes utiles
inf = 10**20           # Valeur représentant l'infini
eps = 1.0 / 10**10     # Petite valeur epsilon pour comparer des float
mod = 998244353        # Exemple de modulo, commun en programmation compétitive

def LI():
    """
    Lit une ligne d'entrée standard, la découpe en morceaux et convertit chaque morceau en entier.
    Retourne :
        list[int] : Liste des entiers lus.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne d'entrée standard, la découpe en morceaux, convertit chaque morceau en entier et retire 1 à chacun (utilisé pour des indices 0-based).
    Retourne :
        list[int] : Liste des entiers (décalés de -1).
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne d'entrée standard et la convertit en liste de flottants.
    Retourne :
        list[float] : Liste des float lus.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne d'entrée standard, la découpe en mots.
    Retourne :
        list[str] : Liste de chaînes lues.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit un entier sur une ligne.
    Retourne :
        int : Entier lu.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit un flottant sur une ligne.
    Retourne :
        float : Flottant lu.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une chaîne sur une ligne.
    Retourne :
        str : Chaîne lue.
    """
    return input()

def pf(s):
    """
    Affiche une valeur avec flush automatique de la sortie standard.
    Arguments :
        s : Valeur à afficher.
    Retourne :
        None
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale qui lit et traite des jeux de données pour simuler un jeu de dés avec des cases spéciales.
    Implémente une simulation dynamique pour calculer la probabilité d'atteindre la case n en t tours exacts.

    Pour chaque jeu de test :
        - n : nombre de cases sur le plateau
        - t : nombre maximal de tours autorisés
        - l : nombre de cases 'chance'
        - b : nombre de cases 'malus'
        Les indices des cases 'chance' et 'malus' sont ensuite lus.

    La transition dynamique s'effectue ainsi :
        - À chaque tour et à chaque position, on simule le lancer d'un dé (1 à 6).
        - Si le déplacement déborde le plateau, on réfléchit en sens inverse (rebond).
        - Si la nouvelle case est 'chance', on avance d'un tour.
        - Si la nouvelle case est 'malus', on retourne au départ.
        - Si on atteint la dernière case, le nombre de tours devient t (on force la sortie).
        On accumule dans une table r[i][j] la probabilité d'être en position j au tour i.

    Retourne :
       str : Chaque probabilité d'atteindre la case finale en t tours, formatée avec 9 décimales, séparée par des sauts de ligne.
    """
    rr = []  # Liste résultant stockant les probabilités pour chaque jeu de test

    while True:
        # Lecture des paramètres du jeu
        n, t, l, b = LI()
        if n == 0:
            # Condition de sortie
            break

        # Lecture des indices des cases 'chance' (ls) et 'malus' (bs)
        ls = set([I() for _ in range(l)])  # Indices des cases 'chance'
        bs = set([I() for _ in range(b)])  # Indices des cases 'malus'

        # Création de la table dynamique r[i][j] : probabilité d'être sur j à l'étape i
        r = [[0] * (n+1) for _ in range(t+2)]
        r[0][0] = 1  # Initialement, on est en position 0, tour 0, avec certitude

        for i in range(t):
            for j in range(n):
                if r[i][j] == 0:
                    # Pas besoin de traiter les états inutiles
                    continue

                # On simule tous les lancers de dé possibles (1 à 6)
                for k in range(1, 7):
                    nj = j + k  # Nouvelle position en avançant de k

                    # Si on dépasse la case n, on rebondit depuis la fin
                    if nj > n:
                        nj = n - (nj - n)

                    ni = i + 1  # Nouveau nombre de tours

                    # Si la case arrivée est de type 'chance', on consomme un tour en plus
                    if nj in ls:
                        ni += 1

                    # Si la case est 'malus', on retourne au début
                    if nj in bs:
                        nj = 0

                    # Si on atteint la dernière case, on passe direct au dernier tour
                    if nj == n:
                        ni = t

                    # Mise à jour de la probabilité dans la table ; chaque lancer a une probabilité de 1/6
                    r[ni][nj] += r[i][j] / 6.0

        # Enregistrement du résultat formaté à 9 décimales
        rr.append('{:0.9f}'.format(r[t][n]))

    # On retourne tous les résultats sur des lignes séparées
    return '\n'.join(map(str, rr))

# Exécution de la fonction principale et affichage du résultat
print(main())