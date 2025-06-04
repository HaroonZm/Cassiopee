import sys
import numpy as np

# Utilisation de l'entrée standard pour la lecture rapide
readline = sys.stdin.readline
readlines = sys.stdin.readlines

# Extension de la limite de récursion pour éviter les erreurs lors d'appels récursifs profonds
sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7  # Modulo utilisé pour éviter le dépassement lors des calculs

# Lecture des variables globales N, A, B, C depuis l'entrée standard
N, A, B, C = map(int, readline().split())

# Si B est impair, il n'existe pas de solution selon les contraintes du problème
if B & 1:
    print(0)
    exit()

def cumprod(arr):
    """
    Calcule le produit cumulatif modulo MOD d'un tableau numpy, optimisé par un découpage en blocs.

    Parameters
    ----------
    arr : np.ndarray
        Tableau numpy d'entiers à multiplier cumulativement, dimension 1.

    Returns
    -------
    np.ndarray
        Tableau des produits cumulatifs, modulo MOD.
    """
    L = len(arr)
    # Détermine la taille d'un bloc carré légèrement supérieure à la racine carrée de L
    Lsq = int(L ** .5 + 1)
    arr = np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)
    # Produit cumulatif par colonnes (première direction)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    # Produit cumulatif par lignes (deuxième direction)
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    # Mise à plat & récupération des éléments initiaux
    return arr.ravel()[:L]

# Pré-calcul des factorielles et de leur inverse modulo MOD pour accélérer les calculs combinatoires

U = 10 ** 5  # Taille maximale pour la pré-calculation de factorielle
x = np.arange(U, dtype=np.int64)
x[0] = 1  # 0! = 1
fact = cumprod(x)  # Tableau des factorielles jusqu'à U-1

# Calcul de l'inverse multiplicatif (modulaire) des factorielles
x = np.arange(U, 0, -1, dtype=np.int64)
x[0] = pow(int(fact[-1]), MOD - 2, MOD)  # (U-1)!^{-1} modulo MOD
fact_inv = cumprod(x)[::-1]  # Inverses des factorielles de 0 à U-1

# B doit être pair, on considère B2 pour les combinaisons
B2 = B // 2
answer = 0  # Variable pour accumuler la réponse finale

# Boucle principale pour compter toutes les compositions possibles en fonction de m
for m in range(C // 3 + 1):
    if B2 == 0:
        # Cas particulier où il n'y a pas d'élément "2,3^n,2" à répartir.
        a = C - 3 * m  # Nombre d'occurrences de l'élément 1 restant
        b = m          # Nombre d'occurrences de l'élément "333"
        c = A - a      # Nombre d'occurrences de l'élément restant pour compléter la somme A
        if a < 0 or c < 0:
            continue  # Les compositions impossibles sont ignorées
        # Calcul combinatoire pour (a+b+c)!/(a!b!c!) modulo MOD : nombre de répartitions
        x = fact[a + b + c] * fact_inv[a] % MOD
        x = x * fact_inv[b] % MOD
        x = x * fact_inv[c] % MOD
        answer = (answer + x) % MOD
        continue

    # Pour les autres cas, on doit aussi répartir les "2,3^n,2" et d'autres contraintes
    n_min = max(0, A - C + 3 * m)  # Bornes sur n selon les valeurs possibles

    # Calcul serait équivalent à de la combinatoire multinomiale pour les répartitions:
    # Nombre de façons de choisir n, m et les indices associés dans les partitions réalisables

    # Produit de factorielles et de leur inverse pour les coefficients multinomiaux
    # x = (B2+A+m)! / (B2)! / (A-n_min)! / (n_min)! / (m)!
    x = fact[B2 + A + m] * fact_inv[m] % MOD * fact_inv[B2] % MOD
    x = x * fact_inv[A - n_min::-1] % MOD
    x = x * fact_inv[n_min:A + 1] % MOD

    # Y est destiné à compter les répartitions possibles de certains éléments supplémentaires
    # pour respecter une contrainte de somme
    # Calculation encodée dans les slices numpy (par vectorisation pour la performance)
    # y = (B2-1 + C - 3*m - A + n_min)! / (B2-1)! / (C-3*m-A+n_min)!
    y = fact[B2 - 1 + C - 3 * m - A + n_min:B2 + C - 3 * m] * fact_inv[B2 - 1] % MOD
    y = y * fact_inv[C - 3 * m - A + n_min:C - 3 * m + 1] % MOD

    # Incrémente la réponse avec la somme de toutes les combinaisons trouvées ce tour-là
    answer = (answer + (x * y % MOD).sum()) % MOD

# Affichage de la réponse finale modulo MOD
print(answer)