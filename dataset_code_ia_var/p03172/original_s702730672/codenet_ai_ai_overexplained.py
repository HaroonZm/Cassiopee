import sys  # Importe le module sys, utilisé ici pour gérer les entrées standard et configurer la récursion.
input = sys.stdin.readline  # Redéfinit la fonction input pour lire rapidement une ligne à la fois depuis l'entrée standard.
sys.setrecursionlimit(10 ** 7)  # Augmente la limite de récursion. Cela permet d'éviter les erreurs de récursion pour des appels profonds.

"""
Ce bloc de commentaire donne une intuition mathématique sur ce que fait le programme :
 - L'idée est de multiplier plusieurs polynômes de la forme (1 + x + ... + x^a)
 - Cela revient à multiplier (1 - x^{a+1}) et (1-x)^{-1}
 - Mais ici l'implémentation est algorithmique et non symbolique.
"""

import numpy as np  # Importe la bibliothèque NumPy, qui fournit des fonctions pour le calcul numérique efficace sur des tableaux.
MOD = 10 ** 9 + 7  # Définit une constante modulo, un grand nombre premier, utilisé pour éviter les débordements et respecter les contraintes.
N, K = map(int, input().split())  # Lit une ligne depuis l'entrée standard, la découpe en deux entiers N et K.

# Crée un tableau NumPy de type entier 64 bits rempli de zéros, de taille K+1.
# Ce tableau 'dp' maintient le nombre de façons d’obtenir une somme donnée avec les conditions du problème.
dp = np.zeros(K + 1, dtype=np.int64)

dp[0] = 1  # Initialise dp[0] à 1, car il y a exactement une façon d’obtenir la somme 0 : ne rien sélectionner.

# Boucle sur chaque entier 'a' obtenu à partir de la deuxième ligne de l’entrée,
# qui contient N entiers représentant les paramètres de chaque polynôme.
for a in map(int, input().split()):
    # Effectue une copie du tableau 'dp' courant pour s’en servir lors du calcul actualisé.
    # Ceci évite d'écraser les données nécessaires pendant la mise à jour.
    # 'prev' contiendra l’état de 'dp' avant l’itération actuelle.
    prev = dp.copy()

    # Modifie 'dp' à partir de l’index a+1 jusqu’à la fin :
    # Pour chaque case, on soustrait prev jusqu’à l’index -(a + 1) (le début du tableau moins a+1).
    # Cela correspond à enlever toutes les combinaisons qui excèdent la contrainte pour 'a'.
    dp[a + 1:] -= prev[:-(a + 1)]

    # Calcule la somme cumulative (c'est-à-dire à chaque position, la somme de tous les éléments précédents) dans dp.
    # La somme cumulative permet d’incrémenter rapidement tous les états possibles selon la contrainte courante.
    # On utilise l’argument 'out=dp' pour que la somme cumulative soit écrite directement dans le tableau d’origine.
    np.cumsum(dp, out=dp)

    # Applique le modulo MOD à chaque élément du tableau dp.
    # On utilise l'opérateur '%='. Cela garantit que tous les éléments restent dans les bornes du problème,
    # et qu’il n’y a pas d’overflow pour les grands nombres intermédiaires.
    dp %= MOD

# À la fin de la boucle, dp[K] contient le résultat final : 
# le nombre de façons de composer la somme K selon les contraintes.
answer = dp[K]  # Stocke ce résultat dans la variable answer.

print(answer)  # Affiche la réponse finale.