import sys

sys.setrecursionlimit(10 ** 5 + 10)

def input(): return sys.stdin.readline().strip()

def resolve():
    H, W = map(int, input().split())
    grid = [[_ for _ in input()] for _ in range(H)]

    l = [[0] * W for _ in range(H)]
    r = [[0] * W for _ in range(H)]
    u = [[0] * W for _ in range(H)]
    d = [[0] * W for _ in range(H)]

    for h in range(H):
        cur = 0
        for w in range(W):
            if grid[h][w] == '#':
                cur = 0
            else:
                cur += 1
            l[h][w] = cur

    for h in range(H):
        cur = 0
        for w in reversed(range(W)):
            if grid[h][w] == '#':
                cur = 0
            else:
                cur += 1
            r[h][w] = cur

    for w in range(W):
        cur = 0
        for h in range(H):
            if grid[h][w] == '#':
                cur = 0
            else:
                cur += 1
            u[h][w] = cur

    for w in range(W):
        cur = 0
        for h in reversed(range(H)):
            if grid[h][w] == '#':
                cur = 0
            else:
                cur += 1
            d[h][w] = cur

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, r[h][w] + l[h][w] + u[h][w] + d[h][w] - 3)
    print(ans)

resolve()