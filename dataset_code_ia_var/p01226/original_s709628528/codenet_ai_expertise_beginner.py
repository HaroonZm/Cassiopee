def move(y, x):
    # Met à jour la direction et essaie d'avancer
    p[2] = y
    p[3] = x
    ny = p[0] + y
    nx = p[1] + x
    if a[ny][nx] == ".":
        p[0] = ny
        p[1] = nx

def shoot():
    # Tire dans la direction actuelle jusqu'à rencontrer quelque chose
    y = p[0] + p[2]
    x = p[1] + p[3]
    while True:
        if a[y][x] == "*":
            a[y][x] = "."
            break
        elif a[y][x] == "#":
            break
        y = y + p[2]
        x = x + p[3]

# Début du programme
t = int(input())
for test in range(t):
    if test > 0:
        print()

    h, w = map(int, input().split())
    # Remplir la carte avec une bordure
    a = []
    bordure = ["#"] * (w + 2)
    a.append(bordure)
    for _ in range(h):
        ligne = list(input())
        a.append(["#"] + ligne + ["#"])
    a.append(bordure[:])

    # Chercher la position et la direction du char
    trouve = False
    for i in range(1, h+1):
        for j in range(1, w+1):
            case = a[i][j]
            if case == ">":
                p = [i, j, 0, 1]  # [ligne, colonne, delta_ligne, delta_colonne]
                a[i][j] = "."
                trouve = True
                break
            elif case == "<":
                p = [i, j, 0, -1]
                a[i][j] = "."
                trouve = True
                break
            elif case == "^":
                p = [i, j, -1, 0]
                a[i][j] = "."
                trouve = True
                break
            elif case == "v":
                p = [i, j, 1, 0]
                a[i][j] = "."
                trouve = True
                break
        if trouve:
            break

    n = int(input())
    commandes = input()

    for k in range(n):
        if commandes[k] == "U":
            move(-1, 0)
        elif commandes[k] == "D":
            move(1, 0)
        elif commandes[k] == "L":
            move(0, -1)
        elif commandes[k] == "R":
            move(0, 1)
        elif commandes[k] == "S":
            shoot()

    # Remettre le char sur la carte
    if p[2] == 0 and p[3] == 1:
        a[p[0]][p[1]] = ">"
    elif p[2] == 0 and p[3] == -1:
        a[p[0]][p[1]] = "<"
    elif p[2] == -1 and p[3] == 0:
        a[p[0]][p[1]] = "^"
    elif p[2] == 1 and p[3] == 0:
        a[p[0]][p[1]] = "v"

    # Afficher la carte sans les bordures
    for i in range(1, h+1):
        print("".join(a[i][1:w+1]))