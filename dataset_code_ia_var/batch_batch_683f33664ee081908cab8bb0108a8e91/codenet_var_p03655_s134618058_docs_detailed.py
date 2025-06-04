import sys
import itertools
import numpy as np
from functools import lru_cache
from operator import itemgetter

# Setup for faster I/O with binary input
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Lecture des paramètres d'entrée
# Les deux vecteurs X et Y, lus à partir de la console.
X = list(map(int, readline().split()))
Y = list(map(int, readline().split()))

# On incrémente les éléments impairs (ceux des indices 1, 3 et 5) de X et Y de 1.
for i in [1, 3, 5]:
    X[i] += 1
    Y[i] += 1

# Séparation des vecteurs X et Y en trois sous-vecteurs chacun
X1 = X[:2]
X2 = X[2:4]
X3 = X[4:]
Y1 = Y[:2]
Y2 = Y[2:4]
Y3 = Y[4:]

def cumprod(arr, MOD):
    """
    Calcule le produit cumulatif modulo MOD sur un tableau numpy, optimisé par lot.

    Parameters
    ----------
    arr : np.ndarray
        Tableau d'entiers pour le produit cumulatif.
    MOD : int
        Modulo pour les résultats.

    Returns
    -------
    np.ndarray
        Tableau contenant les produits cumulatifs modulo MOD.
    """
    L = len(arr)
    Lsq = int(L**0.5 + 1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    # Produit cumulatif le long des colonnes
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    # Produit cumulatif le long des lignes
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U, MOD):
    """
    Calcule les tableaux de factorielles et d'inverses de factorielles modulo MOD jusqu'à U-1.

    Parameters
    ----------
    U : int
        Taille maximale (+1) du tableau de factorielles.
    MOD : int
        Modulo pour les résultats.

    Returns
    -------
    tuple of (np.ndarray, np.ndarray)
        Les tableaux fact et fact_inv où
         - fact[k] = k! % MOD
         - fact_inv[k] = (k!)^(-1) % MOD
    """
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv

# Pré-calcul des factorielles et des inverses jusqu'à U-1 sous modulo MOD.
U = 2 * 10 ** 6 + 10
MOD = 10**9 + 7
fact, fact_inv = make_fact(U, MOD)

@lru_cache(8)
def make_comb(n):
    """
    Construit un tableau contenant C(n, k) pour k = 0..n modulo MOD, de façon vectorisée.

    Parameters
    ----------
    n : int
        Le nombre total d'éléments.

    Returns
    -------
    np.ndarray
        Tableau tel que le k-ième élément est C(n, k) % MOD.
    """
    return fact[n] * fact_inv[:n + 1] % MOD * fact_inv[:n + 1][::-1] % MOD

# Préparation des tâches pour le décompte à inclusion-exclusion.
answer = 0          # La réponse finale
tasks = []          # Liste des tâches à traiter

# Génération de toutes les combinaisons possibles pour les bornes inclusives ou exclusives (pour inclusion-exclusion).
for p in itertools.product([0, 1], repeat=6):
    # Pour chaque dimension, choix soit borne inférieure (0) soit borne supérieure (1)
    x1, x2, x3, y1, y2, y3 = [A[i] for A, i in zip([X1, X2, X3, Y1, Y2, Y3], p)]
    sgn = (-1) ** sum(p)    # Signe pour inclusion-exclusion en fonction du nombre de dimensions "du haut"
    a = x2 - x1
    b = x3 - x2
    c = x2 - x1 + y2 - y1
    d = x3 - x2 + y3 - y2
    c += 2      # Décalages selon la formule du problème
    d += 2
    sgn = -sgn  # Correction du signe (voir la formule d'origine)
    tasks.append((a, b, c, d, sgn))

# Trie les tâches selon c (pour le calcul échelonné plus tard)
tasks.sort(key=itemgetter(2))

# Boucle principale pour accumuler la réponse finale.
for a, b, c, d, sgn in tasks:
    # On veut extraire le coefficient correspondant à A^a B^b dans le développement de
    # (1+A)^c * (1+B)^d / (A-B)^2

    D = a + b + 2
    # Les indices de k (nombre d'apparitions de A) entre L et R inclus pour C(c, k) * C(d, D-k)
    L = max(0, D - d)
    R = min(c, D)
    if L > R:
        continue

    # Préparation des coefficients binomiaux nécessaires
    x = make_comb(c)[L:R + 1]
    L2, R2 = D - R, D - L
    y = make_comb(d)[L2:R2 + 1]
    x = x * y[::-1] % MOD

    # Division par (1-A)^2, équivalente à procéder à deux sommes cumulées
    np.cumsum(x, out=x)
    x %= MOD
    np.cumsum(x, out=x)
    x %= MOD

    # On retrouve le coefficient de A^(a-L) dans le polynôme final
    if 0 <= a - L < len(x):
        answer += sgn * x[a - L]

# Finalisation, passage au modulo
answer %= MOD

# Affichage du résultat
print(answer)