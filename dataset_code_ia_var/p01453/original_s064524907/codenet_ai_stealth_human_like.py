import sys
from collections import deque
# je lis tout depuis stdin, c'est plus pratique
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    W, H = map(int, input().split()) # largeur, hauteur => important
    S = []
    for _ in range(H):
        S.append(input().strip()) # grab la map ligne par ligne

    # Initialisation
    grid_status = [[0]*W for _ in range(H)]  # Vrai si on peut passer
    portals = []
    tot_spaces = 0
    sx = sy = gx = gy = -1

    for row in range(H):
        line = S[row]
        for col in range(W):
            cell = line[col]
            if cell == 's':
                sx, sy = col, row
                grid_status[row][col] = 1
                tot_spaces += 1
            elif cell == 'g':
                gx, gy = col, row
            elif cell == '*':
                portals.append((col, row))
            elif cell == '.':
                tot_spaces += 1
                grid_status[row][col] = 1

    # Déplacements possibles
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    INF = 10**18

    # distances des portails
    dist_from_portal = [[INF]*W for _ in range(H)]
    queue = deque(portals)
    for x, y in portals:
        dist_from_portal[y][x] = 0
    while queue:
        x, y = queue.popleft()
        curr = dist_from_portal[y][x] + 1
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:  # bounds
                if S[ny][nx] != '*' and S[ny][nx] != '#' and dist_from_portal[ny][nx] == INF:
                    dist_from_portal[ny][nx] = curr
                    queue.append((nx, ny))
            # sinon c'est impassable

    # distance depuis goal (pourquoi pas)
    dist_from_goal = [[INF]*W for _ in range(H)]
    queue = deque([(gx, gy)])
    dist_from_goal[gy][gx] = 0
    while queue:
        x, y = queue.popleft()
        curr = dist_from_goal[y][x] + 1
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:
                if S[ny][nx] != '*' and S[ny][nx] != '#' and dist_from_goal[ny][nx] == INF:
                    dist_from_goal[ny][nx] = curr
                    queue.append((nx, ny))
            # on saute les murs bien sûr

    # Recherche binaire. Ça pue un peu mais ça passe
    left = 0
    right = 10**21
    BASE = 10**9
    for _ in range(71):
        mid = (left + right) // 2
        res = 0
        # pour chaque case jouable
        for i in range(H):
            for j in range(W):
                if grid_status[i][j]:
                    a = dist_from_portal[i][j]*BASE + mid
                    b = dist_from_goal[i][j]*BASE
                    res += min(a, b)
        if mid*tot_spaces > res:
            right = mid
        else:
            left = mid

    # Affiche le score final
    score = min(dist_from_portal[sy][sx] + left / BASE, dist_from_goal[sy][sx])
    # arrondi sur 16 chiffres, ça ira bien
    output("%.16f\n" % score)

solve()