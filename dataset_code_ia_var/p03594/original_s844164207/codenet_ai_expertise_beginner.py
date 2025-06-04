h, w, d = map(int, input().split())

if d % 2 == 1:
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 1:
                print("R", end="")
            else:
                print("G", end="")
        print()
else:
    # Création d'une grille temporaire
    size = 2 * d
    cell = []
    for i in range(size):
        ligne = []
        for j in range(size):
            ligne.append("A")
        cell.append(ligne)

    for i in range(d):
        for j in range(d):
            # Calcul pour marquer les 'R'
            if (i + j) % 2 == (d // 2 - 1) % 2:
                if abs(i - j) <= d // 2 - 1 and d // 2 - 1 <= i + j <= (d // 2 - 1) * 3:
                    cell[i][j] = "R"
            elif j > 0 and cell[i][j - 1] == "R":
                cell[i][j] = "R"

    # Remplissage de la grille complète
    for i in range(size):
        for j in range(size):
            if cell[(i - d) % size][(j - d) % size] == "R":
                cell[i][j] = "R"
            elif cell[(i - d // 2) % size][(j - d // 2) % size] == "R" or cell[(i + d // 2) % size][(j + d // 2) % size] == "R":
                cell[i][j] = "G"
            elif cell[(i - d) % size][j] == "R" or cell[i][(j - d) % size] == "R":
                cell[i][j] = "B"
            elif cell[i][j] == "A":
                cell[i][j] = "Y"

    # Préparer la réponse
    ans = []
    for i in range(h):
        ligne = []
        for j in range(w):
            val = cell[i % size][j % size]
            ligne.append(val)
        ans.append(ligne)

    # Affichage
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end="")
        print()