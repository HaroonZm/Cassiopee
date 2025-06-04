import itertools
import copy

# Créer le damier, 8 par 8, initialisé à .
board = [['.'] * 8 for bla in range(8)]

N = int(input()) # Nombre d'indices donnés

def check(row, col, b):
    # On regarde toutes les directions pour vérifier si une reine y traîne
    for i in range(8):
        if b[row][i] == 'Q': return False
        if b[i][col] == 'Q': return False
    # Diagonales à la main, c'est un peu verbeux, sorry
    for i in range(-8, 8):
        x, y = row + i, col + i
        if 0 <= x < 8 and 0 <= y < 8:
            if b[x][y] == 'Q': return False
        y2 = col - i
        if 0 <= x < 8 and 0 <= y2 < 8:
            if b[x][y2] == 'Q': return False
    return True

# Liste des cases à remplir : N lignes de 2 entiers
rc = []
for _ in range(N):
    rc.append(list(map(int, input().split())))

def main():
    # Pour toutes les permutations possibles des colonnes
    for permut in itertools.permutations(range(8)):
        cur = copy.deepcopy(board)
        for row_ind, val in enumerate(permut):
            cur[row_ind][val] = 'Q'
        # Vérification des indices imposés
        ok = True
        for idx in range(N):
            required = rc[idx]
            if cur[required[0]][required[1]] != 'Q':
                ok = False
                break
        if not ok: continue
        legit = True
        for row_ind, val in enumerate(permut):
            cur[row_ind][val] = '.'
            if not check(row_ind, val, cur):
                legit = False
                break
            cur[row_ind][val] = 'Q'
        if legit:
            return cur
    # Bon, là normalement on trouve toujours une solution (sauf erreur...)

tmp = main()
for t in tmp:
    # Version bourrine, warning : print une ligne avec les bonnes Q
    print(''.join(['Q' if c == 'Q' else '.' for c in t]))