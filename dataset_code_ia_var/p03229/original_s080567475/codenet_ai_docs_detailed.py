import sys
import math
from functools import lru_cache
from collections import deque

# Augmente la limite de récursion pour permettre des appels récursifs profonds
sys.setrecursionlimit(10**9)

# Constante pour le modulo utilisé dans certains problèmes, même si ici il ne sert pas
MOD = 10**9 + 7

def input():
    """
    Lit une ligne d'entrée standard et retire le saut de ligne final.
    Returns:
        str: la ligne lue sans le caractère de nouvelle ligne.
    """
    return sys.stdin.readline()[:-1]

def mi():
    """
    Lit une ligne d'entrée standard et convertit les éléments en entiers.
    Returns:
        map: itérateur des entiers de la ligne lue.
    """
    return map(int, input().split())

def ii():
    """
    Lit une ligne d'entrée standard et la convertit en entier.
    Returns:
        int: l'entier lu.
    """
    return int(input())

def i2(n):
    """
    Lit 'n' lignes contenant des entiers, convertit chaque ligne en une liste,
    puis transpose la matrice résultante.
    Args:
        n (int): nombre de lignes à lire.
    Returns:
        list: matrice transposée des valeurs lues.
    """
    tmp = [list(mi()) for i in range(n)]  # Lecture des lignes
    return [list(i) for i in zip(*tmp)]   # Transposition des lignes

# Lecture du nombre d'éléments et des valeurs du tableau
N = ii()
A = [ii() for _ in range(N)]

# Trie le tableau dans l'ordre croissant
A.sort()

# Initialisation des listes pour stocker différentes partitions du tableau
u1, u2 = [], []
l1, l2 = [], []

# Partition du tableau en parties basses et hautes selon deux manières différentes
for i in range(N):
    # Première partition : l1 prend la première moitié, u1 la seconde
    if i < N // 2:
        l1.append(A[i])
    else:
        u1.append(A[i])
    # Seconde partition : l2 prend la première moitié arrondie au supérieur, u2 le reste
    if i < (N + 1) // 2:
        l2.append(A[i])
    else:
        u2.append(A[i])

# Calcul du résultat selon que N est pair ou impair
if N % 2:
    # Si le nombre d'éléments est impair, on applique deux formules pour trouver la solution optimale
    # On considère les deux types de partitions et prend le maximum
    ans = max(
        (2 * sum(u1) - u1[0] - u1[1]) - 2 * sum(l1),
        2 * sum(u2) - (2 * sum(l2) - l2[-1] - l2[-2])
    )
else:
    # Si le nombre d'éléments est pair, on applique une seule formule
    ans = (2 * sum(u1) - u1[0]) - (2 * sum(l1) - l1[-1])

# Affiche la réponse calculée
print(ans)