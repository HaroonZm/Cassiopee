# Déplacements possibles : droite, bas, gauche, haut
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(position, min_coord, max_coord, grid):
    x, y = position
    if grid[y][x] == "#":
        return 0
    count = 1
    grid[y][x] = "#"
    for move in directions:
        nx = x + move[0]
        ny = y + move[1]
        # Vérifie que la nouvelle position est valide
        if min_coord[0] <= nx < max_coord[0] and min_coord[1] <= ny < max_coord[1]:
            count += dfs((nx, ny), min_coord, max_coord, grid)
    return count

while True:
    line = raw_input()
    W_H = line.split(" ")
    W = int(W_H[0])
    H = int(W_H[1])
    if W == 0 and H == 0:
        break
    grid = []
    # Lire chaque ligne de la grille
    for _ in range(H):
        row = raw_input()
        grid.append(list(row))
    # Trouver la position de départ
    start_pos = None
    for y in range(H):
        for x in range(W):
            if grid[y][x] == "@":
                start_pos = (x, y)
                break
        if start_pos is not None:
            break
    result = dfs(start_pos, (0,0), (W,H), grid)
    print(result)