anslist = []

def sarch(i, j, visited):
    # On regarde en haut
    if i > 0:
        if visited[i - 1][j] == 0:
            visited[i - 1][j] = 1
            sarch(i - 1, j, visited)
    # On regarde en bas
    if i < len(visited) - 1:
        if visited[i + 1][j] == 0:
            visited[i + 1][j] = 1
            sarch(i + 1, j, visited)
    # On regarde à gauche
    if j > 0:
        if visited[i][j - 1] == 0:
            visited[i][j - 1] = 1
            sarch(i, j - 1, visited)
    # On regarde à droite
    if j < len(visited[0]) - 1:
        if visited[i][j + 1] == 0:
            visited[i][j + 1] = 1
            sarch(i, j + 1, visited)
    return visited

while True:
    # Lire la taille de la grille
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = []
    for i in range(h):
        ligne = input()
        grid.append(list(ligne))
    # Initialisation de visited
    visited = []
    for i in range(h):
        ligne = []
        for j in range(w):
            if grid[i][j] == "@":
                ligne.append(1)
                starti = i
                startj = j
            elif grid[i][j] == "#":
                ligne.append(-1)
            else:
                ligne.append(0)
        visited.append(ligne)
    # Lancer la recherche
    sarch(starti, startj, visited)
    ans = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                ans += 1
    anslist.append(ans)

for resultat in anslist:
    print(resultat)