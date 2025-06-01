import math
from collections import deque
from math import hypot, atan2, pi, sin, cos, sqrt

class Ufo:
    __slots__ = ('dist', 'angle', 'rad', 'v')
    def __init__(self, x, y, r, v):
        self.dist = hypot(x, y)
        self.angle = atan2(y, x) % (2 * pi)
        self.rad = r
        self.v = v

def reach(ufos, R):
    removed = 0
    for ufo in ufos:
        ufo.dist -= ufo.v
    while ufos and ufos[0].dist <= R:
        ufos.popleft()
        removed += 1
    return removed

def is_dead(ufo, laser, R):
    diff = abs(ufo.angle - laser)
    diff = diff if diff <= pi else 2 * pi - diff
    dist_sin = ufo.dist * sin(diff)
    dist_cos = ufo.dist * cos(diff)
    if (diff <= pi / 2 and dist_sin <= ufo.rad) or (ufo.dist <= ufo.rad):
        sec = sqrt(ufo.rad ** 2 - dist_sin ** 2)
        return dist_cos + sec > R
    return False

def shoot(ufos, laser, R):
    ufos[:] = [ufo for ufo in ufos if not is_dead(ufo, laser, R)]

def main():
    from sys import stdin
    input_iter = iter(stdin.read().split())
    while True:
        R = int(next(input_iter))
        if R == 0:
            break
        n = int(next(input_iter))
        ufos = deque(sorted((Ufo(int(next(input_iter)), int(next(input_iter)), int(next(input_iter)), int(next(input_iter))) for _ in range(n)), key=lambda u: u.dist))
        ans = 0
        while ufos:
            ans += reach(ufos, R)
            if ufos:
                laser = ufos[0].angle
                shoot(ufos, laser, R)
                ufos = deque(sorted(ufos, key=lambda u: u.dist))
        print(ans)

main()