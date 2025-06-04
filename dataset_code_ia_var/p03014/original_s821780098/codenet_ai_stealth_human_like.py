import sys

# J'augmente la limite de récursion au cas où, même si je sais pas si c'est vraiment utile ici
sys.setrecursionlimit(100000 + 9)

def input():
    # Je trouve readline un peu plus rapide, mais faut faire attention aux espaces
    return sys.stdin.readline().strip()

def resolve():
    H, W = map(int, input().split())
    # On prépare la grille (en vrai on pourrait la faire en une ligne mais bon)
    grid = []
    for i in range(H):
        row = list(input())
        grid.append(row)  # j'aime bien garder le nom "row" pour être clair

    # Préparation des matrices, un peu chiant à initialiser
    l = []
    r = []
    u = []
    d = []
    for _ in range(H):
        l.append([0]*W)
        r.append([0]*W)
        u.append([0]*W)
        d.append([0]*W)

    # On regarde vers la gauche (un classique)
    for i in range(H):
        cnt = 0
        for j in range(W):
            if grid[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
            l[i][j] = cnt
    # On regarde à droite, style similaire mais inversé
    for i in range(H):
        c = 0
        # pas besoin de sorted ou truc fancy, on va à l'envers
        for j in range(W-1, -1, -1):
            if grid[i][j] == '#':
                c = 0
            else:
                c += 1
            r[i][j] = c

    # Pareil pour le haut, mais on boucle différemment
    for j in range(W):
        total = 0
        for i in range(H):
            if grid[i][j] == '#':
                total = 0
            else:
                total += 1
            u[i][j] = total

    # Et pour le bas (encore repompe, mais inversé)
    for j in range(W):
        blah = 0
        for i in range(H-1, -1, -1):
            if grid[i][j] == '#':
                blah = 0
            else:
                blah += 1
            d[i][j] = blah

    # Bon là c'est pas hyper optimisé, mais ça fait le taf
    answer = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                tmp = l[i][j] + r[i][j] + u[i][j] + d[i][j] - 3
                if tmp > answer:
                    answer = tmp
    print(answer)

resolve()