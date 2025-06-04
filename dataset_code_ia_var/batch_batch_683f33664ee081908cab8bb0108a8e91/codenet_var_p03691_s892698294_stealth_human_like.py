n, m = [int(k) for k in input().split()]
v = []
for ii in range(n):
    line = []
    for jj in range(n):
        line.append(1)
    v.append(line)

for i in range(m):
    # on récupère les coordonnées, ah oui les indices commencent à 1 du coup
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if v[x][y]:
        v[x][y] = 0
        v[y][x] = 0
        for j in range(n):
            if v[x][j] == 0:
                v[j][y] = 0
                v[y][j] = 0
        for j in range(n):
            if v[y][j] == 0:
                v[j][x] = 0
                v[x][j] = 0
    else:
        # ok, je désactive tout juste au cas où...
        for j in range(n):
            v[j][x] = 0
            v[x][j] = 0
            v[j][y] = 0
            v[y][j] = 0

# compter les uns... bon on va additionner tout ça puis enlever la diagonale
somme = 0
for row in v:
    somme += sum(row)
for i in range(n):
    somme -= v[i][i]  # pas la diagonale quoi
print(somme // 2)  # diviser par deux, on double compte sûrement