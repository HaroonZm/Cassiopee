import sys
from itertools import accumulate
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def compress(A):
    zipped = {}
    unzipped = {}
    for i, a in enumerate(sorted(set(A))):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped

while True:
    W, H = map(int, sys.stdin.readline().split())
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
    X_zipped, _ = compress(X + [-1, 0, W])
    Y_zipped, _ = compress(Y + [-1, 0, H])
    for i in range(N):
        x1, y1, x2, y2 = XY[i]
        XY[i] = (X_zipped[x1], Y_zipped[y1], X_zipped[x2], Y_zipped[y2])
    H_c = len(Y_zipped)
    W_c = len(X_zipped)
    grid = [[0]*W_c for _ in range(H_c)]
    for i in range(N):
        x1, y1, x2, y2 = XY[i]
        grid[y1][x1] += 1
        grid[y2][x1] -= 1
        grid[y1][x2] -= 1
        grid[y2][x2] += 1
    for i in range(H_c):
        grid[i] = list(accumulate(grid[i]))
    grid = list(zip(*grid))
    for i in range(W_c):
        grid[i] = list(accumulate(grid[i]))
    grid = list(zip(*grid))
    grid = [list(row) for row in grid]
    grid[0] = [-1]*W_c
    grid[H_c-1] = [-1]*W_c
    grid = list(zip(*grid))
    grid = [list(row) for row in grid]
    grid[0] = [-1]*H_c
    grid[W_c-1] = [-1]*H_c
    grid = list(zip(*grid))
    grid = [list(row) for row in grid]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = [[0]*W_c for _ in range(H_c)]
    cnt = 0
    for i in range(1, H_c-1):
        for j in range(1, W_c-1):
            if visited[i][j] or grid[i][j] != 0:
                continue
            stack = [(i,j)]
            while stack:
                h,w = stack.pop()
                if visited[h][w]:
                    continue
                visited[h][w] = 1
                for dh,dw in directions:
                    h2 = h+dh
                    w2 = w+dw
                    if 0 <= h2 < H_c and 0 <= w2 < W_c and not visited[h2][w2] and grid[h2][w2] == 0:
                        stack.append((h2,w2))
            cnt += 1
    print(cnt)