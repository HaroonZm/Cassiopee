MAX_X = 2000
MAX_Y = 2000

# Crée une grille de zéros
s = []
for i in range(MAX_X):
    ligne = []
    for j in range(MAX_Y):
        ligne.append(0)
    s.append(ligne)

# Lis les deux rectangles et les place dans la grille
for t in range(2):
    temp = input().split()
    x = int(temp[0])
    y = int(temp[1])
    w = int(temp[2])
    h = int(temp[3])

    for i in range(x, x + w):
        for j in range(y, y + h):
            s[i][j] = s[i][j] + 1

# Compte les cases couvertes exactement une fois
c = 0
for i in range(MAX_X):
    for j in range(MAX_Y):
        if s[i][j] == 1:
            c = c + 1

print(c)