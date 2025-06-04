import sys  # Importe le module sys, qui fournit l'accès à certaines variables et fonctions utilisées ou maintenues par l'interpréteur Python

input = sys.stdin.readline  # Assigne à 'input' la fonction 'readline' de sys.stdin, pour lire une ligne depuis l'entrée standard (souvent plus rapide que le 'input' natif)

import numpy as np  # Importe le module numpy, aliasé en 'np', qui est une bibliothèque pour le calcul mathématique de matrices et tableaux multidimensionnels, très utilisée en science des données et pour traiter de gros volumes de données numériques

# Ce code gère un problème de programmation dynamique où on doit décider, pour chaque nombre d'une séquence, s'il faut le placer tel quel, le déplacer à gauche ou à droite, chaque opération ayant un certain coût.

# On lit une ligne d'entrée, on la découpe en trois entiers et on les affecte à N, A et B respectivement.
# N est le nombre d'éléments de la séquence, A est le coût de déplacer un nombre à droite, et B celui pour le déplacer à gauche.
N, A, B = map(int, input().split())  # 'split()' sépare la ligne en morceaux selon les espaces, 'map(int, ...)' convertit chaque morceau en un entier.

# On lit la ligne suivante de l'entrée, on la découpe en chaînes de caractères, puis on convertit chacune de ces chaînes en un entier, stockés dans la liste P.
P = [int(x) for x in input().split()]  # Crée une liste d'entiers à partir de l'entrée, qui représente la séquence à traiter

# On définit une grande valeur qui représentera l'infini pour notre algorithme (c'est une convention en programmation pour des valeurs impossibles d'atteindre dans le contexte)
INF = 10 ** 18  # 10 puissance 18 est utilisé ici comme une valeur infiniment grande pour initialiser le tableau dynamique

# On crée un tableau numpy d'entiers de taille N+1 et on l'initialise avec la valeur INF. Le tableau 'dp' est utilisé pour stocker les coûts minimaux selon différents états du problème.
# Cela représente, pour chaque nombre, le coût minimal obtenu jusqu'à présent pour une certaine situation (voir logique du problème original pour le sens exact).
dp = np.full(N + 1, INF, dtype=np.int64)  # np.full crée un tableau rempli avec la même valeur. 'dtype=np.int64' précise le type de chaque élément (entier 64 bits).

# On définit la base de la programmation dynamique : le coût pour commencer (aucune opération encore faite) est nul.
dp[0] = 0  # Zéro signifie qu'on n'a encore rien fait donc pas de coût à ce point.

# On parcourt chaque élément 'p' de la liste P, qui est la séquence des nombres à traiter.
for p in P:
    # Étape 1 : On souhaite "placer" le nombre p dans la séquence courante.
    # Pour cela, on cherche le coût minimal possible parmi toutes les positions précédentes possibles, soit jusqu'à l'indice p-1 inclus. 'dp[:p]' va de 0 jusqu'à p-1.
    # On met à jour dp[p] avec cette valeur minimale trouvée (c'est-à-dire, quel est le coût minimum d'arriver à placer jusqu'au point p sans rien faire de spécial pour p).
    dp[p] = dp[:p].min()  # dp[:p] extrait la sous-partie du tableau dp jusqu'à l'indice p (non inclus). .min() donne la plus petite valeur dans cette tranche.

    # Étape 2 : Considérer le déplacement vers la gauche. On suppose qu'on pousse tous les éléments à partir de p+1 vers la gauche, ce qui entraîne un coût pour chaque déplacement.
    # On ajoute le coût B à toutes les positions à droite de 'p' (c'est-à-dire de p+1 jusqu'à N inclus) pour tenir compte du coût de ce déplacement pour chaque possibilité future.
    dp[p + 1:] += B  # dp[p+1:] sélectionne tous les indices à partir de p+1 jusqu'à la fin du tableau, et on leur ajoute le coût B (déplacement vers la gauche).

    # Étape 3 : Considérer le déplacement vers la droite. On suppose qu'on pousse tous les éléments avant 'p' vers la droite, ce qui a aussi un coût.
    # On ajoute le coût A à toutes les positions avant 'p' (c'est-à-dire de 0 jusqu'à p-1 inclus).
    dp[:p] += A  # dp[:p] sélectionne tous les indices avant p, et ajoute A à chacune de ces cases (déplacement vers la droite).

# À la fin, on cherche le coût minimal final dans le tableau dp, car plusieurs chemins/méthodes peuvent arriver à des coûts différents selon les choix faits (déplacer à gauche/droite ou rien faire).
answer = dp.min()  # On cherche la valeur minimale dans le tableau dp, qui représente le coût minimal pour arranger la séquence selon les règles données.

print(answer)  # Affiche le résultat final, c'est-à-dire le coût minimal trouvé pour traiter la séquence entière.