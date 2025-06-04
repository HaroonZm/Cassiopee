#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools

# Augmenter la limite de récursion pour permettre de nombreux appels récursifs
sys.setrecursionlimit(10**5)

# Affectation à des alias pour des fonctions courantes ou objets utilisés
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right

def LI():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste d'entiers.
    Returns:
        list[int]: La liste des entiers lus.
    """
    return list(map(int, stdin.readline().split()))

def LF():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste de flottants.
    Returns:
        list[float]: La liste des flottants lus.
    """
    return list(map(float, stdin.readline().split()))

def LI_():
    """
    Lit une ligne de l'entrée standard, la convertit en une liste d'entiers (indexés à partir de 0).
    Returns:
        list[int]: Liste d'entiers dont chaque élément a été décrémenté de 1.
    """
    return list(map(lambda x: int(x)-1, stdin.readline().split()))

def II():
    """
    Lit un entier de l'entrée standard.
    Returns:
        int: L'entier lu.
    """
    return int(stdin.readline())

def IF():
    """
    Lit un nombre flottant de l'entrée standard.
    Returns:
        float: Le flottant lu.
    """
    return float(stdin.readline())

def LS():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste de listes de caractères.
    Returns:
        list[list[str]]: Liste contenant des listes de caractères (chaque mot est éclaté en caractères).
    """
    return list(map(list, stdin.readline().split()))

def S():
    """
    Lit une ligne de l'entrée standard et la convertit en liste de caractères sans le retour à la ligne.
    Returns:
        list[str]: Liste des caractères de la ligne lue.
    """
    return list(stdin.readline().rstrip())

def IR(n):
    """
    Lit n entiers (un par ligne) de l'entrée standard et les retourne sous forme de liste.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[int]: Liste de n entiers.
    """
    return [II() for _ in range(n)]

def LIR(n):
    """
    Lit n lignes, chaque ligne contenant des entiers séparés par des espaces, et retourne une liste de listes.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[list[int]]: Liste de n sous-listes d'entiers.
    """
    return [LI() for _ in range(n)]

def FR(n):
    """
    Lit n flottants (un par ligne) de l'entrée standard et retourne une liste.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[float]: Liste de n flottants.
    """
    return [IF() for _ in range(n)]

def LFR(n):
    """
    Lit n lignes, chaque ligne contenant des flottants séparés par des espaces, et retourne une liste de listes.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[list[int]]: Liste de n sous-listes de flottants.
    """
    return [LI() for _ in range(n)]  # Erreur probable d'origine, mais reprise fidèlement.

def LIR_(n):
    """
    Lit n lignes, chaque ligne contenant des entiers séparés par des espaces, indexés à partir de 0.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[list[int]]: Liste de n sous-listes d'entiers indexés à partir de 0.
    """
    return [LI_() for _ in range(n)]

def SR(n):
    """
    Lit n lignes, chaque ligne étant convertie en une liste de caractères sans retour à la ligne.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[list[str]]: Liste de n listes de caractères.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Lit n lignes, chaque ligne étant décomposée en mots puis chaque mot en caractères.
    Args:
        n (int): Le nombre de lignes à lire.
    Returns:
        list[list[list[str]]]: Liste de n listes de mots eux-mêmes éclatés en listes de caractères.
    """
    return [LS() for _ in range(n)]

# Constantes communes
mod = 10 ** 9 + 7        # Modulo classique pour problèmes arithmétiques
inf = float('INF')       # Représente l'infini

def A():
    """
    Fonction de résolution du problème A.
    Suppose qu'on doit minimiser un coût pour atteindre une certaine somme à l'aide d'objets de coûts et durées données.
    """
    n = II()        # La cible finale à atteindre
    p = LI()        # Liste des coûts associés aux objets
    t = LI()        # Liste des durées associées aux objets
    dp = [inf] * (10 ** 5)  # Tableau pour la programmation dynamique, initialisé à l'infini
    dp[0] = 0       # Coût pour une somme de 0 est 0

    # Remplissage du tableau dp (technique du sac à dos/monnaie)
    for i in range(10 ** 5):
        for num, ti in enumerate(t):
            if i - ti >= 0:
                dp[i] = min(dp[i], dp[i - ti] + p[num])

    # Optimisation du dp sur la partie décroissante
    for i in range(10 ** 5 - 1, 0, -1):
        dp[i - 1] = min(dp[i], dp[i - 1])

    print(dp[n])
    return

def B():
    """
    Fonction de résolution du problème B.
    Pour chaque nombre, compte les diviseurs et, à partir de ce comptage, construit un préfixe cumulatif fonction du nombre de diviseurs.
    En particulier, si un nombre a au moins 5 diviseurs, il compte dans le préfixe.
    """

    def yaku(n):
        """
        Calcule le nombre de diviseurs de n (approximativement, potentielle incohérence sur n-1).
        Args:
            n (int): Le nombre cible.
        Returns:
            int: Nombre de diviseurs comptés (en doublant chaque fois pour i et n // i).
        """
        res = 0
        if n == 0:
            return 0
        for i in range(1, int(math.sqrt(n - 1)) + 1):
            if n % i == 0:
                res += 2
        if float.is_integer(math.sqrt(n)):
            res += 1
        return res

    q = II()    # Nombre de requêtes

    # Pré-calcul du nombre de diviseurs pour tous les entiers jusqu'à 10^5
    ya = [yaku(i) for i in range(10 ** 5 + 1)]
    ya[0] = 0

    # Marque 1 si le nombre courant possède au moins 5 diviseurs, 0 sinon
    for i in range(1, 10 ** 5 + 1):
        if ya[i] >= 5:
            ya[i] = 1
        else:
            ya[i] = 0
        # Construction du tableau préfixe cumulatif
        ya[i] += ya[i - 1]

    # Traitement des q requêtes
    for _ in range(q):
        n = II()
        print(ya[n])
    return

def C():
    """
    Fonction squelette pour le problème C (non implémentée).
    """
    return

def D():
    """
    Fonction de résolution du problème D.
    Donne une valeur basée sur la divisibilité de b par a, ou de règles arithmétiques données.
    Si b est un multiple de a ou a == 2, la réponse est -1.
    Sinon, on essaie de trouver le plus petit nombre c répondant à certains critères sur a et b.
    """
    a, b = LI()     # Lecture de deux entiers a et b
    # Vérification des cas d'échec immédiat
    if b % a == 0 or a == 2:
        print(-1)
    else:
        x = b // a + 1
        c = a * x
        # Vérification du critère sur c et impression selon le cas
        if x < c // b + c % b:
            print(c)
        else:
            print(-1)

def E():
    """
    Fonction squelette pour le problème E (non implémentée).
    """
    return

def F():
    """
    Fonction squelette pour le problème F (non implémentée).
    """
    return

def G():
    """
    Fonction squelette pour le problème G (non implémentée).
    """
    return

def H():
    """
    Fonction squelette pour le problème H (non implémentée).
    """
    return

# Solveur principal pour lancer le problème D (modifiable pour lancer d'autres fonctions)
if __name__ == '__main__':
    D()