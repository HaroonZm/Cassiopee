import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

while True:
    inp = sys.stdin.readline()
    if not inp:
        break
    W_H = inp.strip().split()
    if not W_H:
        continue
    W, H = map(int, W_H)
    if W == 0 and H == 0:
        break
    N = int(sys.stdin.readline())
    X = []
    Y = []
    XY = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        X += [x1-1, x1, x2-1, x2]
        Y += [y1-1, y1, y2-1, y2]
        XY.append((x1, y1, x2, y2))
    # ------- compression
    zipped_X = {}
    unzipped_X = {}
    for idx, a in enumerate(sorted(set(X + [-1, 0, W]))):
        zipped_X[a] = idx
        unzipped_X[idx] = a
    zipped_Y = {}
    unzipped_Y = {}
    for idx, a in enumerate(sorted(set(Y + [-1, 0, H]))):
        zipped_Y[a] = idx
        unzipped_Y[idx] = a
    for i in range(N):
        x1, y1, x2, y2 = XY[i]
        XY[i] = (zipped_X[x1], zipped_Y[y1], zipped_X[x2], zipped_Y[y2])
    H2 = len(zipped_Y)
    W2 = len(zipped_X)
    grid = [[0]*W2 for _ in range(H2)]
    for i in range(N):
        x1, y1, x2, y2 = XY[i]
        grid[y1][x1] += 1
        grid[y2][x1] -= 1
        grid[y1][x2] -= 1
        grid[y2][x2] += 1
    for i in range(H2):
        acc = 0
        for j in range(W2):
            acc += grid[i][j]
            grid[i][j] = acc
    for j in range(W2):
        acc = 0
        for i in range(H2):
            acc += grid[i][j]
            grid[i][j] = acc
    # frame -1
    for j in range(W2):
        grid[0][j] = -1
        grid[H2-1][j] = -1
    for i in range(H2):
        grid[i][0] = -1
        grid[i][W2-1] = -1
    # directions
    dir4 = ((1,0),(-1,0),(0,1),(0,-1))
    visited = [[0]*W2 for _ in range(H2)]
    cnt = 0
    i = 1
    while i < H2-1:
        j = 1
        while j < W2-1:
            if visited[i][j] or grid[i][j] != 0:
                j += 1
                continue
            stack = [(i,j)]
            visited[i][j] = 1
            while stack:
                h, w = stack.pop()
                for dh, dw in dir4:
                    ni = h + dh
                    nj = w + dw
                    if 0 <= ni < H2 and 0 <= nj < W2 and not visited[ni][nj] and grid[ni][nj]==0:
                        visited[ni][nj] = 1
                        stack.append((ni,nj))
            cnt += 1
            j += 1
        i += 1
    print(cnt)