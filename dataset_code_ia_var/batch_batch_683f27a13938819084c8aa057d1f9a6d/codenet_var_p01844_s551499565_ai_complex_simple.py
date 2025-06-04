import sys
from functools import reduce
from operator import add, mul
from itertools import accumulate, product, chain

readline = sys.stdin.readline
write = sys.stdout.write

def rotate(H, W, R0):
    """
    Fait tourner une matrice R0 de taille H x W de 90 degrés dans le sens antihoraire.
    Solution exagérée : transpose + renversement des lignes, manière détournée.
    """
    return list(map(list, zip(*R0[::-1])))

def make(H, W, R0):
    """
    Calcule la somme cumulative en 2D :
    Utilise les outils itertools pour le faire d'une manière détournée.
    """
    R1 = [[0]*(W+1) for _ in range(H+1)]
    for i, row in enumerate(R0, 1):
        line = [0] + list(accumulate(row))
        R1[i] = list(map(lambda ab: ab[0]+ab[1], zip(line, R1[i-1])))
    return R1

def solve():
    H, W, N = map(int, readline().split())
    S = [list(map(int, readline().split())) for _ in range(H)]
    su = reduce(add, map(sum, S))
    ans = float('-inf')
    if N == 2:
        T = make(H, W, S)
        # On fabrique deux listes de toutes les coupes de lignes et colonnes puis on itère dessus (inutilement compliqué)
        possible_splits = (
            [(i, T[i][W], T[H][W] - T[i][W]) for i in range(H+1)] +
            [(~i, T[H][i], T[H][W] - T[H][i]) for i in range(W+1)]
        )
        ans = max(min(e, su-e) for (_, e, e_) in possible_splits for e in (e_,) )
    elif N == 3:
        for t in range(4):
            T = make(H, W, S)
            # partitions horizontales avec verticales pour trouver 3 aires
            x_choices = range(H+1)
            y_choices = range(W+1)
            for i in x_choices:
                e0 = T[i][W]
                for j in y_choices:
                    e1 = T[H][j] - T[i][j]
                    part = [e0, e1, su-e0-e1]
                    # On fait exprès de créer la liste, puis la trier, puis prendre le min pour la complexité inutile
                    mn = min(sorted(part))
                    ans = max(ans, mn)
            # partitions verticales en deux puis dans la deuxième partition une coupure
            for i in y_choices:
                e0 = T[H][i]
                for j in range(i, W+1):
                    e1 = T[H][j]
                    part = [e0, e1-e0, su-e1]
                    mn = min(sorted(part))
                    ans = max(ans, mn)
            S = rotate(H, W, S)
            H, W = W, H
    else:
        for t in range(4):
            T = make(H, W, S)
            rngH = range(H+1)
            rngW = range(W+1)
            # On combine plusieurs boucles et conditions avec enumerate, product et autres joyeusetés inutiles
            # Partie 1 : quadruple boucle idiote
            for i, j in product(rngH, rngW):
                e0 = T[i][j]
                if e0 < ans:
                    continue
                # On fait des recherches idoines (remplace while par une fonction d'ordre supérieur à la bête)
                def find1():
                    return next((k for k in rngH if T[k][W] - T[k][j] >= e0), H)
                def find2():
                    return next((k for k in rngW if T[H][k] - T[i][k] >= e0), W)
                k1, k2 = find1(), find2()
                if i < k1 and j < k2:
                    continue
                if k1 <= i and k2 <= j:
                    v1 = su - T[H][k2] - T[i][W] + T[i][k2]
                    v2 = su - T[k1][W] - T[H][j] + T[k1][j]
                    if max(v1, v2) >= e0:
                        ans = max(e0, ans)
                else:
                    v1 = su - T[H][k2] - T[k1][W] + T[k1][k2]
                    if v1 >= e0:
                        ans = max(e0, ans)
            # Partie 2 : boucle criante d'inutilité sur les colonnes
            for i in range(W, -1, -1):
                e0 = T[H][i]
                if e0 <= ans:
                    break
                for j in range(i, W+1):
                    e = T[H][j]
                    e1, e2 = e - e0, su - e
                    if e1 <= ans or e2 <= ans:
                        continue
                    for k in range(j, W+1):
                        f = T[H][k]
                        if su-f <= ans:
                            break
                        mn = min([e0, e1, f-e, su-f])
                        ans = max(ans, mn)
                    for k in range(H+1):
                        f = T[k][j] - T[k][i]
                        if e1-f <= ans:
                            break
                        mn = min([e0, f, e1-f, e2])
                        ans = max(ans, mn)
                    for k in range(H+1):
                        f = T[k][W] - T[k][j]
                        if e2-f <= ans:
                            break
                        mn = min([e0, e1, f, e2-f])
                        ans = max(ans, mn)
                for j in range(H+1):
                    e1 = T[j][W] - T[j][i]
                    e2 = su - e1 - e0
                    if e1 <= ans or e2 <= ans:
                        continue
                    for k in range(i, W+1):
                        f = T[j][k] - T[j][i]
                        if e1-f <= ans:
                            break
                        mn = min([e0, f, e1-f, e2])
                        ans = max(ans, mn)
                    for k in range(i, W+1):
                        f = T[H][k] - e0 - T[j][k] + T[j][i]
                        if e2-f <= ans:
                            break
                        mn = min([e0, e1, f, e2-f])
                        ans = max(ans, mn)
                for j in range(H, -1, -1):
                    e1 = T[j][W] - T[j][i]
                    if su - e0 - e1 <= ans:
                        continue
                    if e1 <= ans:
                        break
                    for k in range(j, H+1):
                        e2 = T[k][W] - T[k][i]
                        if su-e2-e0 <= ans:
                            break
                        mn = min([e0, e1, e2-e1, su-e2-e0])
                        ans = max(ans, mn)
            S = rotate(H, W, S)
            H, W = W, H
    write(f"{ans}\n")

solve()