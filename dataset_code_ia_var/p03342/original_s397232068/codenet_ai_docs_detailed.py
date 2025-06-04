import sys
import queue
import math
import copy
import itertools
from fractions import gcd

# Augmente la limite de récursion pour permettre les appels récursifs profonds
sys.setrecursionlimit(10**7)

# Définit une valeur représentant l'infini pour le problème
INF = 10**18

# Définit la constante du modulo si besoin d'opérations sous un large modulo
MOD = 10**9 + 7

# Fonction utilitaire pour lire une ligne d'entiers depuis l'entrée standard
LI = lambda: [int(x) for x in sys.stdin.readline().split()]

# Fonction utilitaire pour lire une ligne d'entiers et décrémenter chacun de 1 depuis l'entrée standard
_LI = lambda: [int(x) - 1 for x in sys.stdin.readline().split()]

def main():
    """
    Fonction principale qui lit les entrées, traite le problème et affiche la solution.

    Le problème : Compter le nombre de sous-tableaux dans un tableau où le XOR de tous les éléments dans la fenêtre
    est unique (aucun bits partagés). Cela s'effectue grâce à une approche à deux pointeurs (sliding window).
    """

    # Lecture de la taille du tableau
    N = int(input())

    # Lecture du tableau d'entrée suivi d'un ajout d'une valeur sentinelle (-1) pour éviter les dépassements d'indice
    A = LI() + [-1]

    # Initialise le total des sous-tableaux valides
    ans = 0

    # Initialise les deux pointeurs et le XOR cumulatif de la fenêtre courante
    l = 0  # bord gauche de la fenêtre
    r = 0  # bord droit de la fenêtre
    xor = 0  # XOR cumulatif des éléments entre l et r
    s = 0  # stockage temporaire utilisé lors de la réduction de la fenêtre

    # Balaye le tableau avec deux pointeurs pour maintenir la propriété du XOR unique
    while r < N:
        if xor & A[r] == 0:
            # Si l'ajout de A[r] ne partage aucun bit avec le XOR courant (aucune superposition), on étend la fenêtre
            xor ^= A[r]
            r += 1
            # On ajoute le nombre de sous-tableaux se terminant en r-1 et commençant entre l et r-1
            ans += (r - l)
        else:
            # S'il y a partage de bits, il faut réduire la fenêtre depuis la gauche jusqu'à ce qu'on puisse rajouter A[r]
            s = xor & A[r]
            while s:
                # On enlève les bits superposés en retirant le terme de gauche et en avançant l
                s -= s & A[l]
                xor ^= A[l]
                l += 1
                # Si nécessaire, on pourrait interrompre ici (cas particulier, non utilisé ici)

    print(ans)

if __name__ == "__main__":
    main()