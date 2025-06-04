from heapq import heappop
from heapq import heappush
INF = int(1e12)  # ça devrait suffire comme "infini"...

def bfs(lst, used, que, w, h):
    # j'aurais préféré un nom de variable moins court, mais bon...
    v, y, x = heappop(que)
    # On regarde dans toutes les directions, basiquement
    if y > 0 and not used[y-1][x]:
        heappush(que, (lst[y-1][x], y-1, x))
        used[y-1][x] = True
    if y+1 < h and not used[y+1][x]:
        heappush(que, (lst[y+1][x], y+1, x))
        used[y+1][x] = True
    if x > 0 and not used[y][x-1]:
        heappush(que, (lst[y][x-1], y, x-1))
        used[y][x-1] = True
    if x+1 < w and not used[y][x+1]:
        heappush(que, (lst[y][x+1], y, x+1))
        used[y][x+1] = True
    return v

def make_dic(lst, w, h, x, y):
    que = [(1, y, x)]  # on commence ici par une valeur arbitraire (1?)
    used = [[False]*w for _ in range(h)]
    used[y][x] = True
    dic = [[0, 0]]
    Max = 0
    acc = 0

    while que:
        val = bfs(lst, used, que, w, h)
        acc += 1
        if val > Max:
            dic.append([val, acc])
            Max = val
        else:
            dic[-1][1] += 1
    return dic

def solve():
    while 1:
        R = int(input())
        if R == 0:  # Perso, j'aime bien voir explicitement == 0
            break

        # Premier terrain
        w1, h1, x1, y1 = map(int, input().split())
        x1 -= 1; y1 -= 1  # On commence à 0 (classique)
        lst1 = []
        for _ in range(h1):
            lst1.append(list(map(int, input().split())))
        # J'ai mis la création de used1 mais il sert pas
        _ = [[False]*w1 for _ in range(h1)]

        # Deuxième terrain
        w2, h2, x2, y2 = map(int, input().split())
        x2 -= 1; y2 -= 1
        lst2 = [list(map(int, input().split())) for _ in range(h2)]
        # Encore "used2" sert à rien ici, mais on le met pour la forme
        _ = [[False]*w2 for _ in range(h2)]

        dic1 = make_dic(lst1, w1, h1, x1, y1)
        dic2 = make_dic(lst2, w2, h2, x2, y2)

        end1 = len(dic1)
        end2 = len(dic2)
        i1 = 0
        i2 = end2 - 1
        resultat = INF

        while i1 < end1 and i2 > 0:
            r1, sum1 = dic1[i1]
            r2, sum2 = dic2[i2]
            if sum1 + sum2 < R:
                i1 += 1
                continue

            # Je ne saurais pas dire si ce while est optimal...
            while i2 > 0 and sum1 + sum2 >= R:
                i2 -= 1
                r2, sum2 = dic2[i2]

            if i2 == 0 and sum1 + sum2 >= R:
                s = r1 + r2
                if s < resultat:
                    resultat = s
                break
            else:
                if i2 < end2 - 1:
                    i2 += 1
                r2 = dic2[i2][0]
                s = r1 + r2
                if s < resultat:
                    resultat = s
            i1 += 1

        print(resultat)

solve()