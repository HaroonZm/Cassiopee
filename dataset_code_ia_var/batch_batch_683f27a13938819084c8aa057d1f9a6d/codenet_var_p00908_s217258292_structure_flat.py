from collections import deque
from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write

dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
Z = [-1]*(50*50)

while True:
    H_W = readline()
    if not H_W:
        break
    H, W = map(int, H_W.split())
    if H == 0 and W == 0:
        break
    M = [[0]*W for _ in range(H)]
    AS = []
    BS = []
    for i in range(H):
        s = readline().strip()
        Mi = M[i]
        for j, c in enumerate(s):
            if c == '*':
                Mi[j] = -1
            elif c == 'X':
                Mi[j] = 1
                AS.append((j, i))
            elif c == '.':
                BS.append((j, i))
    G = [[] for _ in range(H*W)]
    for y in range(H):
        for x in range(W):
            k = y*W + x
            if M[y][x] == -1:
                continue
            for dx, dy in dd:
                nx = x + dx; ny = y + dy
                if not 0 <= nx < W or not 0 <= ny < H or M[ny][nx] == -1:
                    continue
                G[k].append(ny*W + nx)

    sx, sy = min(AS)
    if sx == 0 and sy == 0:
        write("0\n")
        continue

    (x0, y0), (x1, y1) = BS
    ee = [
        ((-1, 0), (-1, 1)),
        ((0, -1), (1, -1)),
        ((2, 0), (2, 1)),
        ((0, 2), (1, 2)),
    ]
    INF = 10**9
    D = [[[INF]*4 for _ in range(W)] for _ in range(H)]
    d1 = [0]*(H*W)
    d2 = [0]*(H*W)

    # calc(H, W, G, x0, y0, sx, sy, d1):
    d1[:] = Z[:H*W]
    k = y0*W + x0
    que = deque([k])
    d1[k] = 0
    for i in [0, 1]:
        for j in [0, 1]:
            d1[(sy+i)*W + (sx+j)] = -2
    while que:
        v = que.popleft()
        cost = d1[v]
        for w in G[v]:
            if d1[w] == -1:
                d1[w] = cost+1
                que.append(w)

    # calc(H, W, G, x1, y1, sx, sy, d2):
    d2[:] = Z[:H*W]
    k = y1*W + x1
    que2 = deque([k])
    d2[k] = 0
    for i in [0, 1]:
        for j in [0, 1]:
            d2[(sy+i)*W + (sx+j)] = -2
    while que2:
        v = que2.popleft()
        cost = d2[v]
        for w in G[v]:
            if d2[w] == -1:
                d2[w] = cost+1
                que2.append(w)

    que0 = []
    for i in range(4):
        (dx1, dy1), (dx2, dy2) = ee[i]
        x1b = sx+dx1; y1b = sy+dy1
        x2b = sx+dx2; y2b = sy+dy2
        if not 0 <= x1b <= x2b < W or not 0 <= y1b <= y2b < H:
            continue
        k1 = y1b*W + x1b; k2 = y2b*W + x2b
        if d1[k1] == -1 or d2[k2] == -1:
            continue
        d = min(d1[k1] + d2[k2], d1[k2] + d2[k1])
        que0.append((d, sx, sy, i))
        D[sy][sx][i] = d
    heapify(que0)

    while que0:
        cost0, x0p, y0p, t0 = heappop(que0)
        if D[y0p][x0p][t0] < cost0:
            continue
        if x0p == 0 and y0p == 0:
            break
        (dx1, dy1), (dx2, dy2) = ee[t0]
        x1a = x0p + dx1; y1a = y0p + dy1
        x2a = x0p + dx2; y2a = y0p + dy2

        # calc(H, W, G, x1a, y1a, x0p, y0p, d1):
        d1[:] = Z[:H*W]
        k = y1a*W + x1a
        que1a = deque([k])
        d1[k] = 0
        for i in [0, 1]:
            for j in [0, 1]:
                d1[(y0p+i)*W + (x0p+j)] = -2
        while que1a:
            v = que1a.popleft()
            cost = d1[v]
            for w in G[v]:
                if d1[w] == -1:
                    d1[w] = cost+1
                    que1a.append(w)
        # calc(H, W, G, x2a, y2a, x0p, y0p, d2):
        d2[:] = Z[:H*W]
        k = y2a*W + x2a
        que2a = deque([k])
        d2[k] = 0
        for i in [0, 1]:
            for j in [0, 1]:
                d2[(y0p+i)*W + (x0p+j)] = -2
        while que2a:
            v = que2a.popleft()
            cost = d2[v]
            for w in G[v]:
                if d2[w] == -1:
                    d2[w] = cost+1
                    que2a.append(w)

        for t1 in range(4):
            (dx3, dy3), (dx4, dy4) = ee[t1]
            x3 = x0p + dx3; y3 = y0p + dy3
            x4 = x0p + dx4; y4 = y0p + dy4
            if not 0 <= x3 <= x4 < W or not 0 <= y3 <= y4 < H:
                continue
            k3 = y3*W + x3; k4 = y4*W + x4
            if d1[k3] == -1 or d2[k4] == -1:
                continue
            d = min(d1[k3] + d2[k4], d1[k4] + d2[k3]) + 1
            dx, dy = dd[t1]
            nx = x0p + dx; ny = y0p + dy
            if cost0 + d < D[ny][nx][t1^2]:
                D[ny][nx][t1^2] = cost0 + d
                heappush(que0, (cost0 + d, nx, ny, t1^2))

    res = min(D[0][0][2], D[0][0][3])
    if res != INF:
        write("%d\n" % res)
    else:
        write("-1\n")