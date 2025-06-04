#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

# Augmente la limite de récursion du système pour éviter les erreurs de dépassement de pile
sys.setrecursionlimit(10000000)

def compute_answer(n):
    """
    Calcule une valeur spécifique basée sur la valeur entière n selon une certaine logique :
    - Effectue une boucle pour (n // 2 - 1) itérations, multipliant 'ans' par 3 puis ajoutant 1 à chaque fois.
    - Si n == 1, 'ans' reste 1.
    - Si n est impair, 'ans' est multiplié par 4 puis majoré de 1.
    - Si n est pair, 'ans' est multiplié par 2.
    
    Args:
        n (int): L'entier d'entrée pour le calcul.
    
    Returns:
        int: Le résultat du calcul selon les règles décrites.
    """
    ans = 1
    # Boucle pour appliquer la formule 'ans = ans * 3 + 1' (n // 2 - 1) fois
    for i in range(n // 2 - 1):
        ans = ans * 3 + 1
    # Cas particulier où n vaut 1
    if n == 1:
        ans = 1
    # Si n est impair, appliquer une transformation spécifique
    elif n % 2 == 1:
        ans = ans * 4 + 1
    # Si n est pair, appliquer une autre transformation
    else:
        ans = ans * 2
    return ans

def main():
    """
    Lit les entrées depuis l'entrée standard, calcule et affiche le résultat pour chaque ligne saisie.
    """
    # Parcourt chaque ligne de l'entrée standard
    for line in sys.stdin:
        # Conversion de la ligne lue en entier
        n = int(line)
        # Calcul du résultat correspondant
        ans = compute_answer(n)
        # Affichage du résultat
        print(ans)

# Point d'entrée du programme
if __name__ == '__main__':
    main()