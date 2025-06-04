from itertools import cycle, islice, repeat, product, chain
from operator import add
from functools import reduce

dxy = tuple(zip(*(
    tuple(map(lambda s: int(s[0] == 'E') - int(s[0] == 'W'), chain('E', 'S', 'W', 'N'))),
    tuple(map(lambda s: int(s[0] == 'S') - int(s[0] == 'N'), chain('E', 'S', 'W', 'N')))
)))

while True:
    H, W, L = map(int, raw_input().split())
    if not H:
        break
    c = list(islice((raw_input() for _ in repeat(0)), H))
    y, x, d = next(
        (h, w, "ESWN".index(c[h][w]))
        for h, w in product(range(H), range(W))
        if c[h][w] in "ESWN"
    )

    visited = [[[~0]*4 for _ in repeat(0, W)] for _ in repeat(0, H)]
    visited[y][x][d] = 0
    step, inloop = 0, False

    while L:
        dx, dy = ([(a,b) for a, b in dxy][d])
        nx, ny = map(add, (x, y), (dx, dy))
        if not (0 <= nx < W and 0 <= ny < H and c[ny][nx] != "#"):
            d = (d + 1) % 4
        else:
            x, y = nx, ny
            step += 1
            L -= 1
        if visited[y][x][d] > ~0 and not inloop:
            loop_len = step - visited[y][x][d]
            L %= loop_len
            L += loop_len
            inloop = True
        visited[y][x][d] = step
    print "%d %d %s" % (y+1, x+1, "ESWN"[d])