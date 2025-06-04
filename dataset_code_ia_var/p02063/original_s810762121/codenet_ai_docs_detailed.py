import sys
from operator import itemgetter
from collections import Counter, deque
from math import ceil, floor, sqrt
from copy import deepcopy
import heapq
from functools import reduce
# Pour Python 3.5+, la fonction gcd est dans math, pas fractions
try:
    from math import gcd  
except ImportError:
    from fractions import gcd

# Définir la limite de récursivité à une grande valeur, utile dans certains problèmes récursifs/profondes DFS
sys.setrecursionlimit(200000)

# Utiliser la fonction readline pour une lecture plus rapide de l'entrée standard
input = sys.stdin.readline

def ii():
    """
    Lit une ligne de l'entrée standard, la convertit en int et la retourne.

    Returns:
        int: Le nombre entier lu.
    """
    return int(input())

def mi():
    """
    Lit une ligne de l'entrée standard, divise la ligne par espaces, et retourne un itérable converti en entiers.

    Returns:
        map(int): Un itérable contenant des entiers.
    """
    return map(int, input().rstrip().split())

def lmi():
    """
    Lit une ligne de l'entrée standard, divise la ligne par espaces, convertit tous les éléments en entiers,
    et retourne une liste d'entiers.

    Returns:
        list of int: Liste d'entiers lus.
    """
    return list(map(int, input().rstrip().split()))

def li():
    """
    Lit une ligne de l'entrée standard et retourne la liste des caractères (en tant que chaîne de caractères).

    Returns:
        list of str: Liste des caractères de la ligne lue.
    """
    return list(input().rstrip())

def debug(*args, sep=" ", end="\n"):
    """
    Affiche les arguments passés pour le débogage, mais seulement si l'exécution n'est pas optimisée (__debug__ est True).

    Args:
        *args: Valeurs à afficher.
        sep (str): Séparateur des valeurs. Défaut : " ".
        end (str): Caractère de fin de ligne. Défaut : "\n".
    """
    if not __debug__:
        print("debug:", *args, file=sys.stderr, sep=sep, end=end)

def exit(*arg):
    """
    Affiche les arguments puis quitte le programme immédiatement.

    Args:
        *arg: Les valeurs à afficher avant de sortir.
    """
    print(*arg)
    sys.exit()

def main():
    """
    Fonction principale du programme.
    Lit deux entiers A et B depuis l'entrée standard,
    puis résout un problème selon des conditions sur A et B.

    Le problème consiste probablement à trouver une valeur minimale sous contraintes.
    Logique:
        1. Si B > (A - 1)^2: affiche -1 et termine.
        2. Si B est divisible par (A - 1) : affiche A * ceil(B / A)
        3. Sinon, calcule a = B // (A - 1) et b = B % (A - 1)
            a. Si a < b : affiche A * ceil(B / A)
            b. Sinon : affiche -1

    Returns:
        None
    """
    # Lecture de deux entiers A et B depuis l'entrée standard
    A, B = mi()
    # Si B dépasse la borne maximale autorisée, il n'y a pas de solution
    if B > (A - 1) ** 2:
        print(-1)
        sys.exit()
    # Si B est divisible par (A - 1), un calcul direct permet de trouver le résultat
    if B % (A - 1) == 0:
        print(A * ceil(B / A))
    else:
        # Sinon, il faut analyser a et b selon la division euclidienne
        a = B // (A - 1)
        b = B % (A - 1)
        if a < b:
            print(A * ceil(B / A))
        else:
            print(-1)

    # ========= Analyses/Tests additionnels sur les méthodes dynamiques (commentés) =========
    # Les lignes suivantes sont des commentaires de tentative de programmation dynamique,
    # qui ne sont pas exécutées dans la version actuelle.
    #
    # dp1 = [float('inf')] * 100
    # dp2 = [float('inf')] * 100
    # dp1[0] = dp2[0] = 0
    # for i in range(1, 100):
    #     dp1[i] = min(dp1[i], dp1[i - 1] + 1)
    #     if i >= A:
    #         dp1[i] = min(dp1[i], dp1[i - A] + 1)
    #     if i >= B:
    #         dp1[i] = min(dp1[i], dp1[i - B] + 1)
    # for i in range(1, 100):
    #     if i >= B:
    #         dp2[i] = dp2[i - B] + 1
    #     elif i >= A:
    #         dp2[i] = dp2[i - A] + 1
    #     else:
    #         dp2[i] = dp2[i - 1] + 1
    # for i in range(100):
    #     if dp1[i] != dp2[i]:
    #         print(A, B)
    #         break
    # for i in range(100):
    #     if dp1[i] != dp2[i]:
    #         debug(i, dp1[i], dp2[i], "?")

if __name__ == '__main__':
    # Point d'entrée du script. Appelle la fonction principale si le module est exécuté directement.
    main()