from collections import deque
from itertools import starmap

D = (
    ((-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)),
    ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0))
)

def func(y, x, n, m):
    cover = [[-1] * m for _ in range(n)]
    q = deque([(y, x, 0)])
    while q:
        y, x, step = q.popleft()
        if cover[y][x] >= 0:
            continue
        cover[y][x] = step
        shifts = D[y & 1]
        for dx, dy in shifts:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                q.append((ny, nx, step + 1))
    return cover

def solve(m, n, spos, tpos):
    scover = [func(y-1, x-1, n, m) for x, y in spos]
    min_cover = [[min(sc[y][x] for sc in scover) for x in range(m)] for y in range(n)]
    def count(cover):
        return sum(
            cover[y][x] < min_cover[y][x]
            for y in range(n) for x in range(m)
        )
    return max(
        count(func(y-1, x-1, n, m))
        for x, y in tpos
    )

import sys

def genlines():
    for line in sys.stdin:
        yield line.rstrip('\n')

lines = genlines()
while True:
    try:
        data = next(lines)
        if data == "0":
            break
        m, n = map(int, data.split())
        s = int(next(lines))
        spos = [tuple(map(int, next(lines).split())) for _ in range(s)]
        t = int(next(lines))
        tpos = [tuple(map(int, next(lines).split())) for _ in range(t)]
        print(solve(m, n, spos, tpos))
    except StopIteration:
        break