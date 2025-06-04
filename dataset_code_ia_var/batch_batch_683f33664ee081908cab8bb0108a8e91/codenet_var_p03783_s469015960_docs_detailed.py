"""
seishin.py

Ce module implémente un algorithme pour traiter une séquence de paires d'entiers (P), chacune représentant un segment ou intervalles [l_i, r_i]. 
L'objectif est de minimiser une certaine "distance" lors de la transition d'un segment à l'autre, en utilisant deux tas pour modéliser l'état courant.
L'algorithme repose sur une structure de tas min et de tas max, avec des variables de décalage, afin de maintenir des bornes et d'accumuler un coût (res) minimal.

Auteur: <Votre Nom>
Date: <Date>
"""

import sys
from heapq import heappush, heappop

def main():
    """
    Point d'entrée principal du programme.
    Lit les entrées, initialise les structures et lance le calcul.
    Affiche le résultat final.
    """
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    print(minimize_total_distance(N, P))

def minimize_total_distance(N, P):
    """
    Calcule le coût minimal de transition entre segments donnés.

    Args:
        N (int): Nombre de segments.
        P (List[List[int]]): Liste de N paires [l_i, r_i] représentant les bornes des segments.

    Returns:
        int: Le coût total minimal pour parcourir les segments selon les règles de transition.
    """
    INF = 10 ** 18  # Valeur d'infini pour initialisation

    l0, r0 = P[0]  # Premier segment

    # Initialisation des deux tas:
    # L est un max-heap simulé (on insère les opposés)
    # R est un min-heap
    L = [-l0 + 1]  # Max-heap (négatif du point de départ - ajusté)
    R = [l0 - 1]   # Min-heap (point de départ ajusté)
    s = t = 0      # Décalages cumulés pour chaque tas (pour gérer la translation au fil de l'itération)

    res = 0  # Résultat total

    for i in range(N-1):
        l0, r0 = P[i]
        l1, r1 = P[i+1]

        # Décalage cumulatif à chaque étape
        s += (r1 - l1)
        t += (r0 - l0)

        # On cherche à maintenir l1-1 (point d'insertion médian) entre les bornes des tas
        if -s - L[0] <= l1 - 1 <= t + R[0]:
            # Le médian est déjà dans la fourchette : simple insertion dans les deux tas
            heappush(L, -l1 + 1 - s)
            heappush(R, l1 - 1 - t)
            # Aucun coût additionnel
        elif l1 - 1 < -s - L[0]:
            # Trop petit, on doit ré-équilibrer
            heappush(L, -l1 + 1 - s)
            heappush(L, -l1 + 1 - s)
            p = -heappop(L) - s  # Retire et ajuste le plus grand (max-heap)
            heappush(R, p - t)
            res += p - (l1 - 1)  # Coût de déplacement à droite du médian
        elif t + R[0] < l1 - 1:
            # Trop grand, on doit ré-équilibrer
            heappush(R, l1 - 1 - t)
            heappush(R, l1 - 1 - t)
            p = heappop(R) + t  # Retire et ajuste le plus petit (min-heap)
            heappush(L, -p - s)
            res += (l1 - 1) - p  # Coût de déplacement à gauche du médian

        # (Optionnel: appels de debug pour visualiser l'état des tas)
        # debug(L, s, t, R)

    return res

def debug(L, s, t, R):
    """
    Affiche l'état courant des tas et des décalages pour le debug.

    Args:
        L (list): Tas max (sous forme de max-heap inversé avec valeurs négatives).
        s (int): Décalage accumulé pour le tas L.
        t (int): Décalage accumulé pour le tas R.
        R (list): Tas min (heapq par défaut).

    Returns:
        None
    """
    L0 = L[:]
    Q1 = []
    Q2 = []

    while L0:
        Q1.append(-s - heappop(L0))
    R0 = R[:]
    while R0:
        Q2.append(t + heappop(R0))
    print("debug:", *(Q1[::-1] + Q2))

if __name__ == "__main__":
    main()