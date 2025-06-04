import sys
# Augoment la limite de récursion pour permettre des appels récursifs profonds si nécessaire
sys.setrecursionlimit(1 << 25)

# Définition des fonctions de lecture rapide depuis l'entrée standard
readline = sys.stdin.buffer.readline  # lecture rapide de lignes comme bytes
read = sys.stdin.readline            # lecture rapide de lignes comme chaînes de caractères

import numpy as np
from functools import partial

# Définition de versions typées (int64) de fonctions numpy fréquemment utilisées
array = partial(np.array, dtype=np.int64)
zeros = partial(np.zeros, dtype=np.int64)
full = partial(np.full, dtype=np.int64)

def ints():
    """
    Lit une ligne de l'entrée standard (bufferisée), 
    la découpe en nombres entiers séparés par des espaces 
    et renvoie un tableau numpy d'entiers 64 bits.
    
    Returns:
        np.ndarray: Array d'entiers lus depuis une ligne.
    """
    return np.fromstring(readline(), sep=' ', dtype=np.int64)

def read_matrix(H, W) -> np.ndarray:
    """
    Lit une matrice de H lignes et W colonnes depuis l'entrée standard.
    Chaque ligne contient W entiers séparés par des espaces.
    
    Args:
        H (int): Nombre de lignes de la matrice.
        W (int): Nombre de colonnes de la matrice.
        
    Returns:
        np.ndarray: Un tableau numpy de forme (H, W), dtype int64.
    """
    lines = []
    # Lecture de H lignes sous forme de chaînes
    for _ in range(H):
        lines.append(read())
    # Les lignes sont concaténées pour tout transformer en une string unique
    lines = ' '.join(lines)
    # Conversion de la string en une matrice numpy de type int64
    return np.fromstring(lines, sep=' ', dtype=np.int64).reshape(H, W)

# Quelques constantes utiles pour les calculs
MOD = 10 ** 9 + 7
INF = 2 ** 31  # 2147483648, une "infinite" valeur supérieure à 10^9

# Lecture des paramètres du problème : taille de la matrice et puissance d'exponentiation
N, K = ints()
# Lecture de la matrice carrée de taille N x N
A = read_matrix(N, N)

def matmul_mod(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Multiplie deux matrices X et Y modulo MOD, de manière explicite (boucles imbriquées).
    
    Args:
        X (np.ndarray): Matrice de dimension (n, m).
        Y (np.ndarray): Matrice de dimension (m, p).
        
    Returns:
        np.ndarray: Produit matriciel (n, p), chaque élément modulo MOD.
    """
    MOD = 10 ** 9 + 7
    ret = np.empty((X.shape[0], Y.shape[1]), dtype=np.int64)
    # Parcours de chaque élément de la matrice résultat
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            # Produit scalaire ligne i de X et colonne j de Y, modulo MOD
            tmp = (X[i, :] * Y[:, j]) % MOD
            ret[i, j] = tmp.sum() % MOD
    return ret

def matmul_mod_try(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Variante de multiplication de matrices modulo MOD, plus optimisée en utilisant la transposée.
    
    Args:
        X (np.ndarray): Matrice de dimension (n, m).
        Y (np.ndarray): Matrice de dimension (m, p).
        
    Returns:
        np.ndarray: Produit matriciel (n, p), chaque élément modulo MOD.
    """
    MOD = 10 ** 9 + 7
    ret = np.empty((X.shape[0], Y.shape[1]), dtype=np.int64)
    YT = Y.T
    for i in range(X.shape[0]):
        Xi = X[i, :]
        tmp = (YT * Xi) % MOD
        # Calcul du produit scalaire pour chaque colonne (après transposition)
        ret[i, :] = tmp.sum(1) % MOD
    return ret

def matmul_mod_fast(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Version rapide (vectorisée) de la multiplication de matrices modulo MOD.
    Cette méthode exploite la diffusion automatique (broadcasting) de numpy pour accélérer le calcul.
    
    Args:
        X (np.ndarray): Matrice de dimension (n, m).
        Y (np.ndarray): Matrice de dimension (m, p).
        
    Returns:
        np.ndarray: Produit matriciel (n, p), chaque élément modulo MOD.
    """
    MOD = 10 ** 9 + 7
    # Préparation des matrices pour la diffusion
    X3d = X[:, :, np.newaxis].transpose(0, 2, 1)  # (n, 1, m)
    Y3d = Y[:, :, np.newaxis].transpose(2, 1, 0)  # (1, p, m)
    # Multiplication élément par élément, somme sur la dernière dimension
    return ((X3d * Y3d) % MOD).sum(2) % MOD

# Copie défensive de la matrice A (au cas où celle-ci serait modifiée ultérieurement)
A_double = np.asanyarray(A, dtype=np.int64)
# Création de la matrice identité, qui sera utilisée pour la puissance de matrice
ans = np.eye(N, dtype=np.int64)

# Exponentiation rapide de la matrice A à la puissance K modulo MOD
for j in range(int(K).bit_length()):
    if (K >> j) & 1:
        # Multiplie ans par la version courante de A_double si le j-ième bit de K est à 1
        ans = matmul_mod_fast(ans, A_double)
    # Met à jour A_double à sa propre puissance de 2 (carré)
    A_double = matmul_mod_fast(A_double, A_double)

# Affiche la somme de tous les éléments de la matrice résultat, modulo MOD
print(ans.sum() % MOD)