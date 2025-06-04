from functools import reduce
from itertools import product, chain, accumulate, count, takewhile

while True:
    h, w = tuple(map(int, input().split()))
    if (h | w) == 0:
        break
    h, w = h - 1, w - 1
    n = int(input())
    obstacles = set(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n))

    terrain = [[1]* (w+1) for _ in range(h+1)]
    for x, y in obstacles:
        terrain[x][y] = 0

    mtx = [[0] * (w + 2) for _ in range(h + 2)]
    mtx[0][0] = terrain[0][0]

    coords = product(range(h + 1), range(w + 1))
    for i, j in coords:
        mtx[i + 1][j] += mtx[i][j] * terrain[i][j]
        mtx[i][j + 1] += mtx[i][j] * terrain[i][j]

    print(mtx[h][w] if terrain[h][w] else 0)