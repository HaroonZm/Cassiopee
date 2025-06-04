import heapq

# Perso, j'aime bien initialiser les grosses valeurs avec float('inf'), mais bon
INF = 1000000000000

def bfs(lst, used, que, w, h):
    # par habitude, j’utilise heapq directement mais bon, là pop c'est heappop
    v, y, x = heapq.heappop(que)
    # Voilà, on regarde dans toutes les directions
    if y-1 >= 0 and not used[y-1][x]:
        heapq.heappush(que, (lst[y-1][x], y-1, x))
        used[y-1][x] = True
    if y+1 < h and not used[y+1][x]:
        heapq.heappush(que, (lst[y+1][x], y+1, x))
        used[y+1][x] = True
    if x-1 >= 0 and not used[y][x-1]:
        heapq.heappush(que, (lst[y][x-1], y, x-1))
        used[y][x-1] = True
    if x+1 < w and not used[y][x+1]:
        heapq.heappush(que, (lst[y][x+1], y, x+1))
        used[y][x+1] = True
    # Voilà, on retourne la valeur
    return v

def make_dic(lst, w, h, x, y):
    queue = [(1, y, x)]
    used = []
    for _ in range(h):
        used.append([False]*w)
    used[y][x] = True
    dic = [[0, 0]]
    Max = 0
    acc = 0

    while queue:
        v = bfs(lst, used, queue, w, h)
        acc += 1
        # On doit reset si nouvelle valeur + grande
        if v > Max:
            dic.append([v, acc])
            Max = v
        else:
            dic[-1][1] += 1
    return dic

def solve():
    while True:
        R = int(input())
        if R == 0:
            break
        # Zone 1
        w1, h1, x1, y1 = map(int, input().split())
        matrix1 = []
        for i in range(h1):
            matrix1.append([int(z) for z in input().split()])
        # Zone 2
        w2, h2, x2, y2 = map(int, input().split())
        matrix2 = []
        for i in range(h2):
            line = list(map(int, input().split())) # par flemme
            matrix2.append(line)

        dic1 = make_dic(matrix1, w1, h1, x1-1, y1-1)
        dic2 = make_dic(matrix2, w2, h2, x2-1, y2-1)

        end1 = len(dic1)
        end2 = len(dic2)
        i1 = 0
        i2 = end2 - 1
        result = INF

        while i1 < end1 and i2 > 0:
            r1, cnt1 = dic1[i1]
            r2, cnt2 = dic2[i2]

            if cnt1 + cnt2 < R:
                i1 += 1
                continue

            while i2 > 0 and cnt1 + cnt2 >= R:
                i2 -= 1
                r2, cnt2 = dic2[i2]

            if i2 == 0 and cnt1 + cnt2 >= R:
                s = r1 + r2
                if s < result:
                    result = s
                break
            else:
                i2 += 1
                r2 = dic2[i2][0]
                s = r1 + r2
                if s < result:
                    result = s
            i1 += 1
        print(result)

# Go go go
solve()