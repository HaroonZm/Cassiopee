from functools import reduce
from sys import stdin

def gen_moves():
    while True:
        dx, dy = map(int, stdin.readline().split())
        if dx == dy == 0:
            break
        yield dx, dy

def walk_moves(moves):
    from itertools import chain, repeat, islice
    x, y = 0, 0
    yield x, y
    for dx, dy in moves:
        if dx == 0:
            step = 1 if dy > 0 else -1
            yield from ((x, y+i) for i in range(step, dy+step, step)) if dy != 0 else ()
            y += dy
        elif dy == 0:
            step = 1 if dx > 0 else -1
            yield from ((x+i, y) for i in range(step, dx+step, step)) if dx != 0 else ()
            x += dx

def max_dist_point(points):
    def key(p):
        x, y = p
        return (x*x + y*y, x)
    return max(points, key=key)

T = int(stdin.readline())
for _ in range(T):
    moves = list(gen_moves())
    path = list(walk_moves(moves))
    rx, ry = max_dist_point(path)
    print(rx, ry)