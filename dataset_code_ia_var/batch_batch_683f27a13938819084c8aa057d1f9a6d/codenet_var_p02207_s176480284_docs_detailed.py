from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
import sys

# Augmente la limite de récursion pour éviter les erreurs sur des entrées de grande profondeur.
sys.setrecursionlimit(10 ** 6)

# Fonctions utilitaires courantes pour la lecture et le traitement d'entrée
int1 = lambda x: int(x) - 1  # Convertit une chaîne en int et décrémente de 1 (utile pour les index à base 0)
p2D = lambda x: print(*x, sep="\n")  # Affiche une liste en format 2D

def II():
    """
    Lit une ligne de l'entrée standard, la convertit en entier et la retourne.
    Returns:
        int: Un entier provenant de l'entrée standard.
    """
    return int(sys.stdin.readline())

def MI():
    """
    Lit une ligne de l'entrée standard, la divise en éléments, les convertit en int et les retourne sous forme d'itérable.
    Returns:
        iterable of int: Les entiers lus.
    """
    return map(int, sys.stdin.readline().split())

def MI1():
    """
    Lit une ligne, convertit les éléments en int, décrémente chacun de 1, et les retourne sous forme d'itérable.
    Returns:
        iterable of int: Les entiers (décalés de -1) lus.
    """
    return map(int1, sys.stdin.readline().split())

def MF():
    """
    Lit une ligne, convertit les éléments en float et les retourne sous forme d'itérable.
    Returns:
        iterable of float: Les flottants lus.
    """
    return map(float, sys.stdin.readline().split())

def LI():
    """
    Lit une ligne, convertit les éléments en int, retourne la liste d'entiers.
    Returns:
        list of int: Liste d'entiers.
    """
    return list(map(int, sys.stdin.readline().split()))

def LI1():
    """
    Lit une ligne, convertit les éléments en int puis décrémente chacun de 1, retourne la liste d'entiers.
    Returns:
        list of int: Liste d'entiers (décalés de -1).
    """
    return list(map(int1, sys.stdin.readline().split()))

def LF():
    """
    Lit une ligne, convertit les éléments en float, retourne la liste de flottants.
    Returns:
        list of float: Liste de flottants.
    """
    return list(map(float, sys.stdin.readline().split()))

def LLI(rows_number):
    """
    Lit plusieurs lignes depuis l'entrée standard, chaque ligne étant convertie en liste d'entiers.
    Args:
        rows_number (int): Le nombre de lignes à lire.
    Returns:
        list of list of int: Liste contenant 'rows_number' listes d'entiers.
    """
    return [LI() for _ in range(rows_number)]

# Directions pour navigation en 2D (droite, bas, gauche, haut).
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    """
    Fonction principale qui traite l'entrée standard pour effectuer un traitement mathématique et répondre à des requêtes.
    Workflow:
        - Lit un nombre 'n' de paires (t, a).
        - Calcule les valeurs associées et préfixes pour un traitement rapide des requêtes.
        - Lit 'q' requêtes où chaque requête demande un calcul spécifique sur un sous-intervalle des données.
        - Affiche le résultat pour chaque requête.
    """
    n = II()  # Nombre d'éléments
    tt = []   # Liste des abscisses/temps/t (selon le contexte du problème)
    aa = []   # Liste des valeurs associées (sera prétraitée)
    for _ in range(n):
        t, a = MI()  # Lit une paire (t, a)
        tt.append(t)  # Ajoute t à la liste
        # Calcule une valeur transformée à partir de a.
        # log10(10 - a) - 1 permet de manipuler la valeur lors des requêtes pour assurer une accumulation précise.
        aa.append(log10(10 - a) - 1)
    # Calcul du tableau des sommes préfixes pour un accès rapide en O(1) sur n'importe quel intervalle
    cm = [0]  # cm[i] = somme préfixe jusqu'à l'indice i-1 de aa
    for a in aa:
        cm.append(cm[-1] + a)

    q = II()  # Nombre de requêtes à traiter
    for _ in range(q):
        l, r = MI()  # Lecture des bornes de la requête
        # Recherche de la première position où tt >= l et tt >= r dans la table des temps/index
        li = bisect_left(tt, l)
        ri = bisect_left(tt, r)
        # Calcule la différence de sommes préfixes, applique la formule demandée et affiche le résultat
        print(pow(10, cm[ri] - cm[li] + 9))

# Lancement de la fonction principale au chargement du script
main()