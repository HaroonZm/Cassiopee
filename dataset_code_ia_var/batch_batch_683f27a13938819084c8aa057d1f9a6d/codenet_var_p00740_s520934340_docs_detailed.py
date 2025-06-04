import sys

# Augmente la limite de récursion pour permettre des appels récursifs profonds
sys.setrecursionlimit(10 ** 6)

# Importation de modules pour manipuler tableaux triés, collections optimisées et files de priorité
from bisect import *
from collections import *
from heapq import *

# Lambda pour convertir une chaîne en entier et soustraire 1 (utile pour l'indéxation à partir de zéro)
int1 = lambda x: int(x) - 1

# Lambda pour afficher une liste d'éléments ligne par ligne
p2D = lambda x: print(*x, sep="\n")

def II():
    """
    Lit une ligne de l'entrée standard et la convertit en entier.

    Returns:
        int: La valeur entière lue depuis l'entrée standard.
    """
    return int(sys.stdin.readline())

def SI():
    """
    Lit une ligne de l'entrée standard et retire le saut de ligne final.

    Returns:
        str: La chaîne lue depuis l'entrée standard, sans le saut de ligne.
    """
    return sys.stdin.readline()[:-1]

def MI():
    """
    Lit une ligne de l'entrée standard et la convertit en plusieurs entiers.

    Returns:
        iterator of int: Un itérateur sur les entiers lus.
    """
    return map(int, sys.stdin.readline().split())

def MI1():
    """
    Lit une ligne de l'entrée standard, convertit chaque nombre en entier puis enlève 1 à chaque entier.

    Returns:
        iterator of int: Un itérateur sur les entiers (décalés de 1) lus.
    """
    return map(int1, sys.stdin.readline().split())

def MF():
    """
    Lit une ligne de l'entrée standard et la convertit en plusieurs flottants.

    Returns:
        iterator of float: Un itérateur sur les nombres à virgule flottante lus.
    """
    return map(float, sys.stdin.readline().split())

def LI():
    """
    Lit une ligne de l'entrée standard et la convertit en liste d'entiers.

    Returns:
        list of int: Une liste d'entiers lus depuis l'entrée standard.
    """
    return list(map(int, sys.stdin.readline().split()))

def LI1():
    """
    Lit une ligne de l'entrée standard, convertit chaque nombre en entier et enlève 1 à chaque entier, retourne une liste.

    Returns:
        list of int: Une liste d'entiers (décalés de 1) lus depuis l'entrée standard.
    """
    return list(map(int1, sys.stdin.readline().split()))

def LF():
    """
    Lit une ligne de l'entrée standard et la convertit en liste de flottants.

    Returns:
        list of float: Une liste de flottants lus depuis l'entrée standard.
    """
    return list(map(float, sys.stdin.readline().split()))

def LLI(rows_number):
    """
    Lit plusieurs lignes de l'entrée standard et retourne une liste composée de listes d'entiers.

    Args:
        rows_number (int): Le nombre de lignes à lire.

    Returns:
        list of list of int: Une liste de listes d'entiers, chaque sous-liste correspondant à une ligne de l'entrée standard.
    """
    return [LI() for _ in range(rows_number)]

# Liste de couples représentant les 4 directions cardinales (droite, bas, gauche, haut)
dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    """
    Fonction principale qui gère la résolution du problème de distribution de billes/jetons sur un plateau circulaire
    jusqu'à vider tous les jetons sur un joueur. 
    A chaque itération, le joueur courant reçoit un jeton si la pile n'est pas vide, sinon il récupère ses propres jetons.
    Le programme lit plusieurs cas jusqu'à la fin (n==0).
    Affiche l'indice du joueur qui termine la partie pour chaque configuration.
    """
    while True:
        # Lecture du nombre de joueurs n et de la valeur initiale des jetons p0
        n, p0 = MI()
        if n == 0:
            # Condition d'arrêt : nombre de joueurs nul
            break
        i = 0                  # Indice du joueur courant
        s = [0] * n            # s[i] : nombre de jetons détenus par chaque joueur
        p = p0                 # Nombre de jetons restants dans la pile (hors mains des joueurs)
        while True:
            if p:
                # S'il y a au moins un jeton dans la pile, le joueur courant reçoit un jeton
                s[i] += 1
                p -= 1
                # Si le joueur atteint p0 jetons, il gagne, on arrête la simulation
                if s[i] == p0:
                    break
            else:
                # Si la pile est vide, le joueur récupère tous ses jetons et le tour continue
                p += s[i]
                s[i] = 0
            # Passage au joueur suivant (cercle modulaire)
            i = (i + 1) % n
        # Affichage de l'indice du joueur gagnant (commence à 0)
        print(i)

# Appel de la fonction principale
main()