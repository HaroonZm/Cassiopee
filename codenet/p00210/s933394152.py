dd = ((1, 0), (0, -1), (-1, 0), (0, 1))
ENWS = "ENWS"
ds = [-1, 0, 1, 2]
ss = [2, 3, 0, 1]

while 1:
    W, H = map(int, input().split())
    if W == H == 0:
        break
    S = [input() for i in range(H)]

    ps = []; U = [[-1]*W for i in range(H)]
    for i in range(H):
        for j, c in enumerate(S[i]):
            if c in ENWS:
                ps.append([i, j, ENWS.index(c)])
                U[i][j] = 1
            elif c == '#':
                U[i][j] = W*H
    rest = len(ps)
    t = 0
    while rest > 0 and t <= 180:
        for p in ps:
            y, x, c = p
            if c == -1:
                continue
            for d in ds:
                dx, dy = dd[(c+d) % 4]
                nx = x + dx; ny = y + dy
                if U[ny][nx] == -1:
                    p[2] = (c+d) % 4
                    break
        ps.sort(key = lambda x: ss[x[2]])
        qs = []
        for p in ps:
            y, x, c = p
            if c == -1:
                continue
            dx, dy = dd[c]
            nx = x + dx; ny = y + dy
            if U[ny][nx] == -1:
                U[ny][nx] = 1
                if S[ny][nx] == 'X':
                    rest -= 1
                    p[2] = -1
                    qs.append((ny, nx))
                else:
                    p[0] = ny; p[1] = nx
                qs.append((y, x))
        for y, x in qs:
            U[y][x] = -1
        t += 1
    if t <= 180:
        print(t)
    else:
        print("NA")