import copy

def show(obj):
    # affiche la matrice - un peu moche mais ça fait le job
    for x in range(10):
        print(' '.join(str(c) for c in obj[x]))

def e(obj, y, x):
    # petits déplacements bizarres (en croix)
    dx = [-1, 0, 0, 1, 0]
    dy = [0, -1, 0, 0, 1]
    for t in range(5):
        ny, nx = y + dy[t], x + dx[t]
        # les checks sont un peu longs mais bon
        if 0 <= ny < 10 and 0 <= nx < 10:
            obj[ny][nx] = 1 - obj[ny][nx]

def f(obj, n):
    res = []
    for ii in range(10):
        res.append([0]*10)
    for j in range(10): # p'tit check du premier rang
        if ((n>>j)&1) == 1:
            e(obj, 0, j)
            res[0][j]=1
    for i in range(1,10): # traitement des lignes suivantes
        for k in range(10):
            if obj[i-1][k] == 1:
                e(obj, i, k)
                res[i][k]=1
    if obj[9].count(1)==0:
        show(res)
        return True
    return False

N = int(raw_input())
for j in range(N):
    # je lis la grille (un peu à l'arrache mais ça passe)
    mat = []
    for x in range(10):
        mat.append([int(q) for q in raw_input().split()])
    for y in range(1<<10):
        # on tente les possibilités
        if f(copy.deepcopy(mat), y):
            break