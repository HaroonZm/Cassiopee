H, W = map(int, input().split())
A = []
for i in range(H):
    row = list(map(int, input().split()))
    A.append(row)

INF = 10**18

# D[d][y][x] = coût minimal pour être à (x, y) après d déplacements
D = []
for d in range(H*W + 1):
    layer = []
    for y in range(H):
        line = []
        for x in range(W):
            line.append(INF)
        layer.append(line)
    D.append(layer)

directions = [(-1,0), (1,0), (0,-1), (0,1)]

queue = []
# On utilise une liste comme file, pas un tas, pour simplifier
# Mais on va juste mettre le point de départ
D[0][0][0] = 0
queue.append((0, 0, 0, 0))  # (coût, déplacements, x, y)

while queue:
    item = queue.pop(0)  # On enlève le premier élément (FIFO)
    cost = item[0]
    d = item[1]
    x = item[2]
    y = item[3]

    if d == H*W:
        continue

    if D[d][y][x] < cost:
        continue

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue

        nd = cost + A[ny][nx] * (d * 2 + 1)

        if nd < D[d + 1][ny][nx]:
            D[d + 1][ny][nx] = nd
            queue.append((nd, d + 1, nx, ny))

ans = INF
for i in range(H * W + 1):
    if D[i][H-1][W-1] < ans:
        ans = D[i][H-1][W-1]

print(ans)