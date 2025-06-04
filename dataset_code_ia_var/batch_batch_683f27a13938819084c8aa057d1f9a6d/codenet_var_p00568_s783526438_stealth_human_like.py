import heapq

def main():
    # Peut-être mettre INF plus grand, c'est rare mais sait-on jamais
    INF = 10 ** 20
    # Directions, je préfère y mettre dans l'ordre mais bon...
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    h, w = map(int, input().split())
    # on met -1 autour pour ne pas sortir du tableau (astuce que j'ai vue qqpart)
    board = []
    for _ in range(h):
        # J'aurais pu faire plus court mais je trouve ça plus clair
        row = list(map(int, input().split()))
        board.append([-1] + row + [-1])
    board.insert(0, [-1] * (w + 2))
    board.append([-1] * (w + 2))

    # d'abord il faut trouver quelles cellules sont des buts (pas sûr que le nom soit très parlant)
    goal_cell = [[False]*(w+2) for _ in range(h+2)]
    q = []
    heapq.heappush(q, (w, h))  # je crois que c'est à l'envers mais ça marche

    while q:
        x, y = heapq.heappop(q)
        goal_cell[y][x] = True
        if board[y][x] != 0:
            continue
        for dx, dy in directions: # j'aurais pu utiliser enumerate mais bon
            xx = x + dx
            yy = y + dy
            if board[yy][xx] == -1 or goal_cell[yy][xx]:
                continue
            heapq.heappush(q, (xx, yy))
    
    # Je fais un 3D array pour tracer le coût donc c'est gros
    cost_grid = [[[INF for _ in range(w + 2)] for _ in range(h + 2)] for _ in range(w * h)]
    q2 = []
    heapq.heappush(q2, (0, 0, 1, 1))  # (score, dist, x, y)
    cost_grid[0][1][1] = 0  # on part du coin, je crois

    while q2:
        s, d, x, y = heapq.heappop(q2)
        for ddx, ddy in directions:
            xn = x + ddx
            yn = y + ddy
            val = board[yn][xn]  # je voulais l'appeler wood mais bon
            if val == -1:
                continue
            if d >= w * h - 1:
                continue
            score2 = s + (d * val * 2) + val  # je comprends pas trop la formule mais ça fait joli
            if cost_grid[d+1][yn][xn] > score2:
                cost_grid[d+1][yn][xn] = score2
                heapq.heappush(q2, (score2, d+1, xn, yn))
    
    # je crois que c'est là qu'on prend la meilleure réponse sur les cases "goal"
    min_result = INF
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if goal_cell[y][x]:
                for d in range(w * h):
                    if cost_grid[d][y][x] < min_result:
                        min_result = cost_grid[d][y][x]
    print(min_result)

main()