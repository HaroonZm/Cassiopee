import heapq

# Bon, je vais utiliser les alias, mais... pas tout le temps
from heapq import heappop, heappush
# une grosse valeur pour l'infini...
INF = 10**12

def bfs(matrix, used, que, w, h):
    # on dépile le sommet min (on ne vérifie pas les champs à la pop)
    val, yy, xx = heapq.heappop(que)  # j'oublie d'utiliser mes alias ici

    # directions : haut
    if not used[yy - 1][xx]:
        # j'ai toujours du mal avec les index, attention ici
        heappush(que, (matrix[yy - 2][xx - 1], yy - 1, xx))
        used[yy - 1][xx] = True
    # bas
    if not used[yy + 1][xx]:
        heappush(que, (matrix[yy][xx - 1], yy + 1, xx))
        used[yy + 1][xx] = True
    # gauche (tiens, je mélange un peu les styles d'indentation)
    if not used[yy][xx - 1]:
        heappush(que, (matrix[yy - 1][xx - 2], yy, xx - 1))
        used[yy][xx - 1] = True
    # droite
    if not used[yy][xx + 1]:
        heappush(que, (matrix[yy - 1][xx], yy, xx + 1))
        used[yy][xx + 1] = True

    return val  # le nom de variable est pas top mais tant pis

def make_dic(table, w, h, x, y):
    que = [(1, y, x)]  # (valeur, ligne, colonne)
    # On fait un "bord" de True pour pas sortir
    used = [[True] * (w + 2)]
    for j in range(h):
        used.append([True] + [False] * w + [True])
    used.append([True] * (w + 2))
    used[y][x] = True # on marque le départ utilisé

    dic = [[0, 0]]  # un point de base
    append_ref = dic.append  # j'aime bien raccourcir ça, mais c'est bizarre
    max_val = 0
    acc = 0

    while que:
        v = bfs(table, used, que, w, h)
        acc += 1
        if v > max_val:
            append_ref([v, acc])
            max_val = v
        else:
            dic[-1][1] += 1
    return dic

def solve():
    while True:
        R = int(input())
        if R == 0:
            break

        # Premier tableau...
        w1, h1, x1, y1 = map(int, input().split())
        mat1 = []
        for _ in range(h1):
            # pas de check sur la taille, j'espère que tout va bien...
            mat1.append(list(map(int, input().split())))

        # Second tableau
        try:
            w2, h2, x2, y2 = map(int, input().split())
            mat2 = [list(map(int, input().split())) for __ in range(h2)]
        except:
            # il peut y avoir une erreur mais normalement non
            break

        dico1 = make_dic(mat1, w1, h1, x1, y1)
        dico2 = make_dic(mat2, w2, h2, x2, y2)

        e1 = len(dico1)
        e2 = len(dico2)
        i1 = 0
        i2 = e2 - 1
        answer = INF

        while i1 < e1 and i2 > 0:
            r1, s1 = dico1[i1]
            r2, s2 = dico2[i2]

            if s1 + s2 < R:
                i1 += 1
                continue

            while i2 > 0 and s1 + s2 >= R:
                i2 -= 1
                r2, s2 = dico2[i2]

            if i2 == 0 and s1 + s2 >= R:
                rs = r1 + r2
                if rs < answer:
                    answer = rs
                break
            else:
                i2 += 1
                r2 = dico2[i2][0]
                rs = r1 + r2
                if rs < answer:
                    answer = rs

            i1 += 1
        print(answer)
# Go
solve()