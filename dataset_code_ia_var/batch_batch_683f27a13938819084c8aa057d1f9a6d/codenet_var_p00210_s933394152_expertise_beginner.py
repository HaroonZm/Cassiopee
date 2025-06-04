# Définition des directions (dx, dy)
directions = [
    (1, 0),    # E (Est)
    (0, -1),   # N (Nord)
    (-1, 0),   # W (Ouest)
    (0, 1)     # S (Sud)
]
ENWS = "ENWS"
# Ordre de priorité pour tenter les directions
try_dirs = [-1, 0, 1, 2]
# Pour le tri après
sort_index = [2, 3, 0, 1]

while True:
    # Lecture de la taille de la grille
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    # Lecture de la grille
    S = []
    for i in range(H):
        S.append(input())

    # Initialiser la grille d'occupation et les positions
    positions = []
    visited = []
    for i in range(H):
        visited.append([-1]*W)
    for i in range(H):
        for j in range(W):
            char = S[i][j]
            if char in ENWS:
                positions.append([i, j, ENWS.index(char)])  # y, x, direction
                visited[i][j] = 1
            elif char == '#':
                visited[i][j] = W*H  # Mur infranchissable

    # Nombre de pièces à ramasser
    remaining = len(positions)
    time = 0
    while remaining > 0 and time <= 180:
        # Essayer de changer la direction si bloqué
        for p in positions:
            y, x, direction = p
            if direction == -1:
                continue  # Déjà arrivé sur 'X'
            for d in try_dirs:
                nx = x + directions[(direction + d) % 4][0]
                ny = y + directions[(direction + d) % 4][1]
                if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == -1:
                    # Peut avancer dans cette direction
                    p[2] = (direction + d) % 4
                    break

        # Trier les robots pour éviter les collisions étranges
        positions.sort(key=lambda x: sort_index[x[2]])
        to_empty = []
        for p in positions:
            y, x, direction = p
            if direction == -1:
                continue
            dx, dy = directions[direction]
            nx = x + dx
            ny = y + dy
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == -1:
                visited[ny][nx] = 1
                if S[ny][nx] == 'X':
                    remaining -= 1
                    p[2] = -1  # Marque comme arrivé
                    to_empty.append((ny, nx))
                else:
                    p[0] = ny
                    p[1] = nx
                to_empty.append((y, x))
        for y, x in to_empty:
            visited[y][x] = -1
        time += 1

    if time <= 180 and remaining == 0:
        print(time)
    else:
        print("NA")