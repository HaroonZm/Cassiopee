import sys
from itertools import accumulate

def input():
    return sys.stdin.readline().strip()

def list2d(a, b, c):
    return [[c] * b for i in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for k in range(b)] for i in range(a)]

def list4d(a, b, c, d, e):
    return [[[[e] * d for k in range(c)] for k in range(b)] for i in range(a)]

def ceil(x, y=1):
    return int(-(-x // y))

def INT():
    return int(input())

def MAP():
    return map(int, input().split())

def LIST(N=None):
    if N is None:
        return list(MAP())
    else:
        return [INT() for i in range(N)]

def Yes():
    print('Yes')

def No():
    print('No')

def YES():
    print('YES')

def NO():
    print('NO')

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def compress(A):
    """ 座標圧縮 """
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(set(A))):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped

while True:
    W, H = MAP()
    if W == 0 and H == 0:
        break
    N = INT()
    X = []
    Y = []
    XY = []
    for i in range(N):
        x1, y1, x2, y2 = MAP()
        X += [x1 - 1, x1, x2 - 1, x2]
        Y += [y1 - 1, y1, y2 - 1, y2]
        XY.append((x1, y1, x2, y2))

    X_zipped, _ = compress(X + [-1, 0, W])
    Y_zipped, _ = compress(Y + [-1, 0, H])
    for i in range(N):
        x1, y1, x2, y2 = XY[i]
        XY[i] = (X_zipped[x1], Y_zipped[y1], X_zipped[x2], Y_zipped[y2])

    H, W = len(Y_zipped), len(X_zipped)
    grid = list2d(H, W, 0)

    for i in range(N):
        x1, y1, x2, y2 = XY[i]
        grid[y1][x1] += 1
        grid[y2][x1] -= 1
        grid[y1][x2] -= 1
        grid[y2][x2] += 1

    for i in range(H):
        grid[i] = list(accumulate(grid[i]))
    grid = list(zip(*grid))
    for i in range(W):
        grid[i] = list(accumulate(grid[i]))
    grid = list(zip(*grid))

    grid[0] = [-1] * W
    grid[H - 1] = [-1] * W
    grid = list(zip(*grid))
    grid[0] = [-1] * H
    grid[W - 1] = [-1] * H
    grid = list(zip(*grid))

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited = list2d(H, W, 0)

    def dfs(i, j):
        if visited[i][j] or grid[i][j] != 0:
            return 0
        stack = [(i, j)]
        while stack:
            h, w = stack.pop()
            visited[h][w] = 1
            for dh, dw in directions:
                h2 = h + dh
                w2 = w + dw
                if 0 <= h2 < H and 0 <= w2 < W:
                    if not visited[h2][w2] and grid[h2][w2] == 0:
                        stack.append((h2, w2))
        return 1

    cnt = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            cnt += dfs(i, j)
    print(cnt)