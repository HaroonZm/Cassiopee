import numpy as np  # Importe le module numpy, qui permet de manipuler efficacement des tableaux de données numériques
import heapq  # Importe le module heapq pour utiliser des files de priorité (tas) min, facilitant l'extraction rapide des plus petits éléments

# Lecture des trois entiers X, Y, Z à partir d'une entrée standard, séparés par des espaces
# Ces entiers sont convertis depuis des chaînes (lues avec input()) en entiers avec map(int, ...)
X, Y, Z = map(int, input().split())

# Création de trois tableaux numpy (A_np, B_np, C_np) de longueur X + Y + Z, initialisés à zéro
# dtype='int' assure que les éléments sont de type entier
A_np = np.zeros(X+Y+Z, dtype='int')
B_np = np.zeros(X+Y+Z, dtype='int')
C_np = np.zeros(X+Y+Z, dtype='int')

# Remplissage des trois tableaux avec les valeurs lues en entrée
# Pour chaque i de 0 à X+Y+Z - 1 (c'est-à-dire pour chaque élément à lire)
for i in range(X+Y+Z):
    # Lecture d'une ligne contenant trois entiers a, b, c séparés par des espaces
    # map(int, input().split()) convertit chaque valeur lue en entier
    a, b, c = map(int, input().split())
    # Stockage de ces valeurs dans les tableaux correspondants à l'indice i
    A_np[i] = a
    B_np[i] = b
    C_np[i] = c
    
# ---- Étape 1 : ordonner les items ----
# Calcul d'un ordre de tri basé sur la différence (A_np - C_np) pour tous les éléments
# np.argsort retourne les indices qui triés donneraient le tableau (A_np - C_np) croissant
order_A_C = np.argsort(A_np - C_np)
# Création de nouveaux tableaux triés selon cet ordre : cela signifie qu'on trie tous les éléments
# (ainsi que leurs valeurs associées des autres tableaux) selon la valeur croissante de A_np - C_np
A_np_s = A_np[order_A_C]
B_np_s = B_np[order_A_C]
C_np_s = C_np[order_A_C]

# ---- Étape 2 : calcul de la solution de base ----
# Sélection des Z premiers éléments comme devant être en catégorie "Gold"
# Ensuite, les Y suivants sont en catégorie "Silver"
# Le reste (les X suivants) est en catégorie "Bronze"
# res_base additionne : somme des c pour les Gold, somme des b pour les Silver, somme des a pour les Bronze
# C_np_s[:Z] : Les Z premiers éléments triés (Gold). On applique sum() pour avoir leur total.
# B_np_s[Z:(Z+Y)] : Les Y éléments suivants (Silver)
# A_np_s[(Z+Y):] : Le reste pour Bronze
res_base = C_np_s[:Z].sum() + B_np_s[Z:(Z+Y)].sum() + A_np_s[(Z+Y):].sum()

# ---- Étape 3 : optimisation gauche (Gold -> Silver) avec un tas ----
# Initialisation d'une liste des différences C-B pour les Z premiers éléments
# Cela représente la perte/gain en passant de Gold (C) à Silver (B)
C_B_heapq = list(C_np_s[:Z] - B_np_s[:Z])
# Transforme la liste en un tas (min-heap), c.-à-d. l'élément minimal sera toujours en tête
heapq.heapify(C_B_heapq)

# Initialisation d'un tableau pour cumulativement stocker les gains/pertes de cette modification à gauche
# Y+1 valeurs car on envisage 0 à Y conversions du côté gauche
plus_left = np.zeros(Y+1, dtype='int')
# Boucle sur chaque k de 0 à Y-1 pour simuler le déplacement progressif d'éléments de Silver vers Gold
for k in range(Y):
    # heapq.heappushpop insère la nouvelle valeur C_np_s[Z+k] - B_np_s[Z+k], puis retire et retourne la plus petite valeur du tas
    r = heapq.heappushpop(C_B_heapq, C_np_s[Z+k] - B_np_s[Z+k])
    # Calcul cumulatif : on retire r (le plus petit précédent), rajoute la nouvelle différence (toujours C-B d'un nouvel élément Silver => Gold)
    plus_left[k+1] = plus_left[k] - r + C_np_s[Z+k] - B_np_s[Z+k]

# ---- Étape 4 : optimisation droite (Bronze -> Silver) avec un tas ----
# Initialisation d'une liste des différences A-B pour les éléments considérés comme Bronze au départ
# Cela simule le passage de Bronze (A) à Silver (B)
A_B_heapq = list(A_np_s[(Z+Y):] - B_np_s[(Z+Y):])
# Transformation en min-heap
heapq.heapify(A_B_heapq)

# Initialisation d'un tableau pour cumulativement stocker les gains/pertes de cette modification à droite
plus_right = np.zeros(Y+1, dtype='int')
# Cette fois on part de la droite, donc on balaye à l'envers pour simuler le passage progressif de Bronze à Silver
for k in range(Y):
    # On sélectionne les éléments en partant de la fin : Z+Y-1-k
    r = heapq.heappushpop(A_B_heapq, A_np_s[Z+Y-1-k] - B_np_s[Z+Y-1-k])
    # On remplit plus_right dans l'autre sens (de droite à gauche)
    plus_right[Y-k-1] = plus_right[Y-k] - r + A_np_s[Z+Y-1-k] - B_np_s[Z+Y-1-k]
    
# ---- Étape 5 : calcul final ----
# On additionne les deux optimisations de chaque côté pour chaque possible partition, on prend la meilleure combinaison (maximum)
# (plus_left+plus_right) donne, pour chaque nombre de transferts k, le total des gains possibles pour k à gauche et Y-k à droite
# .max() trouve la valeur maximale sur toutes les répartitions possibles
# On additionne le tout à la solution de base et on affiche le résultat final maximal possible
print((plus_left+plus_right).max() + res_base)