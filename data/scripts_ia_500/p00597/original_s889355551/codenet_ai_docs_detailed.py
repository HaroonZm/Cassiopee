#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

# Augmente la limite maximale de récursion pour permettre des appels récursifs profonds
sys.setrecursionlimit(10000000)

def compute_answer(n):
    """
    Calcule une valeur spécifique basée sur la valeur entière d'entrée n selon une formule itérative.

    La fonction initialise 'ans' à 1, puis multiplie et ajoute des constants en fonction de
    la moitié de n (moins un), de la parité de n, et de son égalité à 1 :
      - Pour chaque i dans [0, n/2 - 2], ans = ans * 3 + 1
      - Si n == 1, ans = 1
      - Sinon si n est impair, ans = ans * 4 + 1
      - Sinon (n pair) ans = ans * 2

    Args:
        n (int): nombre entier positif

    Returns:
        int: le résultat calculé selon la formule définie
    """
    ans = 1
    # Utilisation de la division entière pour éviter les erreurs avec les float (Python 3)
    # La boucle s'exécute de 0 à (n//2)-2 inclus, donc (n//2 - 1) itérations au total
    for i in range(n // 2 - 1):
        ans = ans * 3 + 1

    if n == 1:
        ans = 1
    elif n % 2 == 1:
        ans = ans * 4 + 1
    else:
        ans = ans * 2

    return ans

def main():
    """
    Fonction principale lisant des entiers depuis l'entrée standard et affichant le résultat
    calculé pour chacun via la fonction compute_answer.
    """
    for line in sys.stdin:
        # Supprime les espaces superflus et convertit en entier
        n = int(line.strip())
        # Calcule la réponse selon la procédure spécifiée
        ans = compute_answer(n)
        # Affiche le résultat calculé
        print(ans)

if __name__ == "__main__":
    main()