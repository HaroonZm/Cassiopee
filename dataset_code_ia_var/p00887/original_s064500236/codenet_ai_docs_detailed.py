import sys
import queue
import math
import copy
import itertools

def LI():
    """
    Lit une ligne de l'entrée standard, divise la chaîne selon les espaces,
    convertit chaque élément en entier, et retourne la liste correspondante.

    Returns:
        list[int]: Liste des entiers lus de la ligne.
    """
    return [int(x) for x in sys.stdin.readline().split()]

while True:
    # Lecture des paramètres M (largeur), N (hauteur), D (distance de diffusion)
    M, N, D = LI()
    if N == 0:
        # Si N est zéro, c'est la condition de sortie de la boucle principale
        break

    # S : Liste des états (0 ou 1) de toutes les cases, linéarisée
    S = []
    for _ in range(N):
        # On lit chaque ligne et on l'ajoute à la liste S
        S.extend(LI())

    # x : Matrice des systèmes d'équations pour le système linéaire mod 2 (binaire)
    x = []
    for i in range(N):
        for j in range(M):
            # y : vecteur représentant l'effet d'une pression sur la case (i, j)
            y = [0 for _ in range(N * M)]
            for p in range(-D, D + 1):
                # L'effet d'une pression s'étend dans une forme de losange de rayon D
                q1 = j + (D - abs(p))
                q2 = j - (D - abs(p))
                # Si l'on reste dans la grille, on active la case concernée
                if 0 <= i + p < N and 0 <= q1 < M:
                    y[(i+p) * M + q1] = 1
                if 0 <= i + p < N and 0 <= q2 < M:
                    y[(i+p) * M + q2] = 1
            # La case centrale est toujours incluse
            y[i * M + j] = 1
            x.append(y)
    # On ajoute le vecteur représentant l'état final désiré (cible)
    x.append(S)

    # z : Liste d'entiers représentant les lignes du système sous forme compacte (bits)
    z = []
    for i in range(N * M):
        b = 0
        for j in range(N * M + 1):
            b <<= 1
            b += x[j][i]
        z.append(b)

    # c : Liste de booléens pour marquer si une ligne a déjà été utilisée comme pivot
    c = [True for _ in range(N * M)]
    b = 1 << (N * M)  # Position du bit pour le terme constant au pivot
    for i in range(N * M):
        for j in range(N * M):
            if z[j] & b and c[j]:
                for k in range(N * M):
                    if k == j or (z[k] & b) == 0:
                        continue
                    # On élimine la variable correspondante par opération XOR
                    z[k] ^= z[j]
                    c[j] = False
                break
        b >>= 1

    # Si le système a une ou plusieurs équations inconsistantes (non résolubles), il y a 0 solution
    if z.count(1):
        print(0)
    else:
        # Si aucune inconsistance, il y a au moins une solution (1 ici car recherche solution unique)
        print(1)