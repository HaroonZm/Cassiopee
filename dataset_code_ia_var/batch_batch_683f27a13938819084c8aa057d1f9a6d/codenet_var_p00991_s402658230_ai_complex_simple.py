from functools import reduce
from operator import mul
from math import isclose

def comb(x, y):
    if y > x - y:
        y = x - y
    return reduce(lambda a, b: a * b[0] // b[1], zip(range(x, x - y, -1), range(1, y + 1)), 1)

w, h, ax, ay, bx, by = map(int, input().split())

dx = min((lambda a, b: min(w - abs(a - b), abs(a - b)))(ax, bx), w - min(ax, bx, w - abs(ax - bx)))
dy = min((lambda a, b: min(h - abs(a - b), abs(a - b)))(ay, by), h - min(ay, by, h - abs(ay - by)))

symx = int(isclose(dx * 2, w))
symy = int(isclose(dy * 2, h))

factors = [2 if t else 1 for t in (symx, symy)]

ans = reduce(mul, factors, 1) * comb(dx + dy, dx)

print(ans % 100000007)