import sys
import heapq

def main():
    while True:
        # Lire les dimensions et la longueur des commandes
        line = sys.stdin.readline()
        if not line:
            break
        H_W_N = line.strip().split()
        if not H_W_N or H_W_N[0] == '0':
            break
        H, W, N = map(int, H_W_N)

        # Lire la séquence de commandes
        S = sys.stdin.readline().strip()

        # Initialiser la grille et les positions de départ et d'arrivée
        grid = []
        sx = sy = gx = gy = -1
        for i in range(H):
            row = list(sys.stdin.readline().strip())
            for j, c in enumerate(row):
                if c == 'S':
                    sy, sx = i, j
                    row[j] = '.'
                elif c == 'G':
                    gy, gx = i, j
                    row[j] = '.'
            grid.append(row)

        # Conserver la direction après chaque commande
        # 0: haut, 1: gauche, 2: bas, 3: droite
        directions = [1] * (N + 1)
        dir_now = 1
        for i in range(N):
            if S[i] == 'L':
                dir_now = (dir_now - 1) % 4
            else:
                dir_now = (dir_now + 1) % 4
            directions[i + 1] = dir_now

        # Calcul des prochaines possibilités pour chaque direction
        d_next = [N + 1] * 4
        d_map = [None] * (N + 1)
        for i in range(N, -1, -1):
            d_next[directions[i]] = i
            d_map[i] = d_next[:]

        # Initialiser le tableau des coûts
        cost = [[N + 1 for _ in range(W)] for _ in range(H)]
        cost[sy][sx] = 0

        # Mouvements: haut, gauche, bas, droite
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # File de priorité pour Dijkstra
        pq = []
        heapq.heappush(pq, (0, sx, sy))

        while pq:
            now_cost, x, y = heapq.heappop(pq)
            if cost[y][x] < now_cost:
                continue
            d_for_now = d_map[now_cost]
            for k in range(4):
                dx, dy = moves[k]
                ncost = d_for_now[k]
                nx, ny = x + dx, y + dy
                if not (0 <= nx < W and 0 <= ny < H):
                    continue
                if grid[ny][nx] == '#':
                    continue
                if ncost < cost[ny][nx]:
                    cost[ny][nx] = ncost
                    heapq.heappush(pq, (ncost, nx, ny))

        if cost[gy][gx] < N + 1:
            print("Yes")
        else:
            print("No")

main()