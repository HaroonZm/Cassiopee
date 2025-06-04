import sys  # Importe le module système, utilisé ici pour l'accès aux entrées standard (stdin)
import numpy as np  # Importe la bibliothèque NumPy pour les tableaux multidimensionnels et le calcul scientifique
import numba  # Importe Numba pour la compilation JIT accélérant les fonctions Python/NumPy spécifiques
from numba import njit, b1, i4, i8, f8  # Importe des types et le décorateur 'njit' pour indiquer à Numba de compiler sans vérification du type Python natif

# Définit trois raccourcis pour la lecture à partir de l'entrée standard (stdin) binaire
read = sys.stdin.buffer.read        # Lit tout le contenu jusqu'à EOF
readline = sys.stdin.buffer.readline  # Lit une ligne à la fois
readlines = sys.stdin.buffer.readlines # Lit toutes les lignes sous forme de liste

# Définit la constante K, normalement utilisée pour la profondeur maximale des sauts binaires (ici 20)
K = 20

# Utilise le décorateur @njit de Numba pour compiler la fonction en code machine pour accélérer son exécution
# Le type des arguments d'entrée est indiqué pour l'optimisation (i8[:] : tableau 1D d'entiers 64 bits, i8 : un entier 64 bits)
@njit((i8[:],i8), cache=True)
def build_sp(X, D):
    # Définit une constante 'INF' très grande utilisée comme valeur sentinelle (ici 2^60)
    INF = 1<<60
    # Stocke la longueur du tableau d'entrée X dans N
    N = len(X)
    # Ajoute la valeur 'INF' à la fin du tableau X (pour faciliter le calcul des indices limites)
    X = np.append(X, INF)
    # Crée un tableau vide sp de forme (K, N+1) et type entier 64 bits. 'sp' va tenir le tableau "sparse table" pour les sauts binaires
    sp = np.empty((K,N+1), np.int64)
    # Crée un autre tableau similaire pour accumuler les sommes associées aux sauts (somme des coordonnées des points d'arrivée)
    sp_sum = np.empty((K,N+1), np.int64)
    # Première couche (saute avec longueur D) : utilise 'searchsorted' pour trouver, pour chaque élément,
    # l'indice du premier élément >= X[n] + D
    sp[0] = np.searchsorted(X, X + D)
    # Pour le dernier élément (-1), définit explicitement la valeur à N (hors des bornes des indices ordinaires)
    sp[0,-1] = N
    # Initialise la première couche du tableau de sommes par la première couche du tableau sp
    sp_sum[0] = sp[0] # Cela stocke pour chaque point la position où il saute
    # Boucle sur les autres couches pour construire les sauts binaires à 2^k étapes
    for k in range(1, K):
        # Pour tous les indices possibles
        for n in range(N+1):
            # L'indice d'arrivée pour un saut de longueur 2^{k-1} depuis n
            to = sp[k-1,n]
            # Calcul du saut de longueur 2^k comme étant deux sauts de longueur 2^{k-1}
            sp[k][n] = sp[k-1][to]
            # Calcule la somme associée au saut binaire de niveau k
            sp_sum[k][n] = sp_sum[k-1,n] + sp_sum[k-1,to]
    # Retourne le tableau de sauts et le tableau de sommes
    return sp, sp_sum

# Cette fonction trouve le plus grand ensemble que l'on peut atteindre en faisant des sauts binaire depuis l'indice l sans dépasser r
@njit((i8[:,:],i8[:,:],i8,i8), cache=True)
def largest_set(sp, sp_sum, l, r):
    # Initialise la réponse ret comme une liste, où ret[0] compte le nombre d'éléments du chemin (commence à 1)
    # et ret[1] accumule la somme des indices/destinations (commence à l)
    ret = [1, l]
    # Parcourt les puissances de 2 décroissantes de K-1 à 0
    for k in range(K-1, -1, -1):
        # Si en faisant un saut de longueur 2^k on reste dans la plage autorisée (ne dépasse pas r)
        if sp[k, l] <= r:
            # On augmente la taille de l'ensemble par 2^k
            ret[0] += 1 << k
            # On ajoute la somme associée à ce parcours
            ret[1] += sp_sum[k, l]
            # Met à jour la position de départ pour le prochain saut binaire
            l = sp[k, l]
    # Retourne la taille du plus grand ensemble atteignable et la somme totale des positions d'arrivée
    return ret

# Fonction principale qui gère la logique du problème, traitant chaque requête
@njit((i8[:],i8,i8[:]), cache=True)
def main(X, D, LR):
    # Stocke la taille du tableau X
    N = len(X)
    # Prépare les "sparse tables" pour avancer et pour reculer (symétriquement)
    spl, spl_sum = build_sp(X, D)
    # Pour parcourir dans l'autre sens, prend le négatif des éléments de X et les inverse
    spr, spr_sum = build_sp(-X[::-1], D)
    # On traite chaque requête deux à deux (chaque requête est un couple l, r)
    for i in range(0, len(LR), 2):
        l, r = LR[i:i+2]      # Récupère le couple l, r
        l, r = l - 1, r - 1   # Passe les indices de 1-based à 0-based
        # Calcule l'ensemble gauche (de l à r) avec sparse table pour avancer
        cl, sl = largest_set(spl, spl_sum, l, r)
        # Calcule l'ensemble droit (symétrique) sur la plage inversée
        cr, sr = largest_set(spr, spr_sum, N - 1 - r, N - 1 - l)
        # Calcule le total adapté avec la somme symétrique
        sr = (N - 1) * cr - sr
        # Affiche la réponse à la requête actuelle
        print(cl + sr - sl)

# Débute le programme principal -- acquisition des entrées
N, D = map(int, readline().split())   # Lit une ligne, la découpe en deux entiers : N (taille) et D (distance)
X = np.array(readline().split(), np.int64)   # Lit une ligne d'entiers pour le tableau X, convertis en int64 et transformés en tableau NumPy
Q = int(readline())   # Lit le nombre de requêtes Q sur la ligne suivante, le convertit en entier
LR = np.array(read().split(), np.int64)   # Lit le restant de l'entrée, découpe en entier, et stocke comme tableau NumPy (ceci contient les indices des requêtes)

# Appelle la fonction principale avec les données traitées
main(X, D, LR)