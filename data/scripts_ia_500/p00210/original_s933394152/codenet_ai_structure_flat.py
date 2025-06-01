dd = ((1, 0), (0, -1), (-1, 0), (0, 1))
ENWS = "ENWS"
ds = [-1, 0, 1, 2]
ss = [2, 3, 0, 1]
while 1:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    S = [input() for _ in range(H)]
    U = [[-1]*W for _ in range(H)]
    ps = []
    for i in range(H):
        for j in range(W):
            c = S[i][j]
            if c in ENWS:
                ps.append([i, j, ENWS.index(c)])
                U[i][j] = 1
            elif c == '#':
                U[i][j] = W*H
    rest = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'X':
                rest += 1
    t = 0
    while rest > 0 and t <= 180:
        for p in ps:
            if p[2] == -1:
                continue
            y, x, c = p
            for d in ds:
                dx, dy = dd[(c + d) % 4]
                nx, ny = x + dx, y + dy
                if 0 <= ny < H and 0 <= nx < W and U[ny][nx] == -1:
                    p[2] = (c + d) % 4
                    break
        ps.sort(key=lambda x: ss[x[2]])
        qs = []
        for p in ps:
            if p[2] == -1:
                continue
            y, x, c = p
            dx, dy = dd[c]
            nx, ny = x + dx, y + dy
            if 0 <= ny < H and 0 <= nx < W and U[ny][nx] == -1:
                U[ny][nx] = 1
                if S[ny][nx] == 'X':
                    rest -= 1
                    p[2] = -1
                    qs.append((ny, nx))
                else:
                    p[0], p[1] = ny, nx
                qs.append((y, x))
        for y, x in qs:
            U[y][x] = -1
        t += 1
    if t <= 180:
        print(t)
    else:
        print("NA")