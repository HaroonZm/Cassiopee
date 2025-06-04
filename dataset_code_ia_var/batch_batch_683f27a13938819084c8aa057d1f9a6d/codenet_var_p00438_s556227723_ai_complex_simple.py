from functools import reduce
from operator import add
from itertools import repeat, count, product, islice
while True:
    try:
        a, b = map(int, input().split())
        if not (a | b):
            break
        n = int(input())
        g = [list(repeat(1, a+1)) for _ in repeat(None, b+1)]
        g[0] = list(repeat(0, a+1))
        [(lambda y: g.__setitem__(y, [0]+g[y][1:]))(y) for y in islice(count(2), b-1)]
        setitem = lambda y, x: g[y].__setitem__(x, 0)
        [setitem(*reversed(tuple(map(int, input().split())))) for _ in repeat(None, n)]
        for x, y in product(range(1, a+1), range(1, b+1)):
            if g[y][x]: g[y][x] = reduce(add, (g[y-1][x], g[y][x-1]))
        print(g[b][a])
    except Exception:
        break