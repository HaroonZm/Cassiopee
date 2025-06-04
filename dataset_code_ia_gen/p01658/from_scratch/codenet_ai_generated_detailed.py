import sys
sys.setrecursionlimit(10**7)

# Ce problème est complexe car après avoir mangé une pièce,
# les pièces adjacentes changent de goût (douce <-> piquante),
# et on doit respecter une condition stricte pour pouvoir manger une pièce :
# - aucune pièce au-dessus (même colonne, ligne au-dessus)
# - au moins une pièce à gauche ou à droite absente (bord ou vide)
#
# L'objectif est de manger le maximum de pièces sucrées.
#
# Approche :
# On peut modéliser l problème comme une recherche en profondeur (DFS)
# avec backtracking sur l'état de la grille.
#
# Les états possibles sont trop nombreux (2^(M*N) goûts),
# avec une deuxième dimension : si la pièce est encore présente ou non.
#
# Heureusement, la taille max est 100x100 = 10000 pièces environ,
# ce qui est trop grand pour un DFS brut.
#
# Solution pratique :
# On va simuler la descente *colonne par colonne* ou ligne par ligne,
# en tenant compte que la pièce à manger doit avoir aucune pièce au-dessus,
# donc les pièces ne peuvent être mangées que en partant du haut (comme dans un jeu de lignes).
#
# On peut remarquer que pour qu'un pièce soit sélectionnable, il faut que la ligne au-dessus soit vide à cette colonne,
# donc on doit manger les pièces par ordre descendant, en ne pouvant avancer que si les conditions latérales sont respectées.
#
# Ainsi on peut représenter l'état actuel par une "hauteur" pour chaque colonne
# : le nombre de pièces déjà mangées en partant d'en haut (ou l'indice du prochain pièce disponible).
#
# Cela limite l'état à une liste de hauteurs (M entiers)
#
# Puis, à chaque étape, on peut essayer de manger une pièce sélectionnable.
#
# On effectue un DFS sur ces hauteurs.
#
# On utilise la heuristique suivante :
# - La condition "aucune pièce au-dessus" signifie que pour la colonne c,
#   la pièce à manger est à hauteur h_c.
# - La condition "au moins à gauche ou à droite pas de pièce" signifie que
#   sur c-1 ou c+1,
#   la hauteur de la pièce est >= h_c (c'est à dire qu'on a déjà mangé plus haut),
#   ce qui signifie qu'il n'y a pas de pièce sur le côté.
#
# Après avoir mangé une pièce, on inverse le gout des pièces adjacentes qui ne sont pas encore mangées.
#
# On mémorise les états visités (cache), pour ne pas revenir dessus.
#
# Pour représenter l'état des goûts des pièces restantes,
# on peut stocker un tableau 2D de booléens 0/1.
#
# Le grand défi est la mémoire / performance.
#
# On doit faire un compromis :
# - on mémorise seulement l'état des hauteurs (tuple des hauteurs)
# - on ne mémorise pas l'état complet du gout (trop volumineux)
# - on applique un maximum de pruning.
#
# En pratique, M et N sont jusqu'à 100, impossible de faire un backtracking complet efficace,
# donc on prendra M,N plus petits.
#
# Ici, le code est un patron pour un backtracking recherchant max.
#
# On va multiplier la mémoire de l'état en représentant aussi le goût des pièces restantes.
# Mais pour que ce soit calculable, on fera un cache limité.
#
# REMARQUE:
# Ce problème est très difficile en pratique.
# On propose une solution récursive avec memo, qui marche avec des petits exemples.
#
# On fera une fonction récursive qui :
# - cherche les pièces sélectionnables en fonction de l'état
# - pour chaque pièce sélectionnable :
#      - mange cette pièce (compte +1 si sucré)
#      - inverse le gout des pièces adjacentes restantes
#      - appel récursif
#      - restauration état
#
# Puis on renvoie le max.

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

# Etat sera la liste des lignes mangées par colonne (hauteur)
# On maintient aussi un tableau 2D de booléens "present" indiquant si la pièce est encore présente
# et un tableau indiquant pour les pièces présentes leur goût.


from copy import deepcopy

# Fonction pour vérifier si la pièce (r,c) est sélectionnable
def can_eat(r, c, present):
    # Condition 1: pas de pièce au dessus
    if r > 0 and present[r-1][c]:
        return False
    # Condition 2: au moins à gauche ou à droite pas de pièce
    left_absent = (c == 0) or (not present[r][c-1])
    right_absent = (c == N-1) or (not present[r][c+1])
    if not (left_absent or right_absent):
        return False
    return True

# Fonction pour inverser gout des pièces adjacentes non mangées après avoir manger (r,c)
def invert_adj(r, c, present, taste):
    # Adjacent cells (up, down, left, right)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < M and 0 <= nc < N:
            if present[nr][nc]:
                # inversion du goût
                taste[nr][nc] = 1 - taste[nr][nc]

# Memo dictionnaire d'états : pour réduire, on encode present et taste en tuple
# mais c'est très lourd. Pour faisabilité, on mémorise uniquement present et taste sous forme string.
# Cela est coûteux mais fonctionnera jusqu'à un certain point.
#
# Pour optimiser, on encode present et taste en bitmask par ligne.
#
# Ici on encode en tuples de tuples.

from functools import lru_cache

# Conversion en tuples immutables pour cache
def to_tuple_2d(arr):
    return tuple(tuple(row) for row in arr)

# La fonction récursive qui retourne le nb max de pièces sucrées qu'on peut manger
def dfs(present, taste):
    # Convertir en tuples
    key = (to_tuple_2d(present), to_tuple_2d(taste))
    if key in memo:
        return memo[key]

    max_sweet = 0
    # Parcourir toutes les pièces présentes
    for r in range(M):
        for c in range(N):
            if present[r][c] and can_eat(r, c, present):
                # On peut manger cette pièce
                # Sauvegarder état
                present[r][c] = False
                original_taste = []
                # Inverser adjacents
                # sauvegarder gout adj avant inversion
                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < M and 0 <= nc < N:
                        if present[nr][nc]:
                            original_taste.append((nr,nc,taste[nr][nc]))
                            taste[nr][nc] = 1 - taste[nr][nc]
                # Compter +1 si sucré
                count = taste[r][c]
                # appel récursif
                res = dfs(present, taste)
                total = count + res
                if total > max_sweet:
                    max_sweet = total
                # Restauration
                present[r][c] = True
                for nr, nc, val in original_taste:
                    taste[nr][nc] = val

    memo[key] = max_sweet
    return max_sweet

# Initial state
present_init = [[True]*N for _ in range(M)]
taste_init = deepcopy(board)
memo = {}

print(dfs(present_init, taste_init))