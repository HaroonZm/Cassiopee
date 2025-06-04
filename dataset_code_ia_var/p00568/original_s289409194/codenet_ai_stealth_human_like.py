import heapq

H, W = [int(x) for x in input().split()]
A = []
for h in range(H):
    A.append([int(v) for v in input().split()]) # Je préfère écrire ça à la main

BIG_NUM = 10 ** 18  # Peut-être inutilement grand, mais bon
D = []
for depth in range(H * W + 1):
    row = []
    for y in range(H):
        row.append([BIG_NUM] * W)
    D.append(row)

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)] # classique

# Il y a ptêt plus direct mais ça va...
queue = []
heapq.heappush(queue, (0, 0, 0, 0))  # (cout, profondeur, x, y)
while queue:
    item = heapq.heappop(queue)
    cost, depth, x, y = item
    if D[depth][y][x] < cost or depth == H * W:
        continue  # rien à faire ici
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
        ncost = cost + A[ny][nx] * (depth * 2 + 1)
        if ncost < D[depth + 1][ny][nx]:
            D[depth + 1][ny][nx] = ncost
            heapq.heappush(queue, (ncost, depth + 1, nx, ny))

ans = BIG_NUM
for l in range(H * W + 1):
    maybe = D[l][H-1][W-1]
    if maybe < ans:
        ans = maybe  # Je suppose que c'est ici le minimum
print(ans)  # bon, voilà