import math
import functools
import itertools
import operator
import collections

class Ufo:
    def __init__(self, x, y, r, v):
        self.dist, self.angle = *complex(x, y).__abs__(), ((lambda z: z if z >= 0 else z + 2 * math.pi)(math.atan2(y, x))),
        self.rad = r
        self.v = v

def get_dist(x, y):
    return functools.reduce(lambda acc, z: acc + z**2, (x, y), 0) ** (1/2)

def get_angle(x, y):
    return (lambda a: a if a >= 0 else a + math.tau)(math.atan2(y, x))

def reach(ufos, R):
    survivors = []
    rekt = []
    for ufo in ufos:
        ufo.dist = operator.sub(ufo.dist, ufo.v)
        [rekt, survivors][ufo.dist > R].append(ufo)
    ufos[:] = survivors
    return len(rekt)

def is_dead(ufo, laser, R):
    delta = abs(ufo.angle - laser)
    phi = [delta, math.tau - delta][delta > math.pi]
    peri = ufo.dist * math.sin(phi)
    rest = ufo.dist * math.cos(phi)
    root = (ufo.rad ** 2 - peri ** 2) ** 0.5 if ufo.rad ** 2 - peri ** 2 > 0 else 0
    zones = (phi <= math.pi/2 and peri <= ufo.rad) or (ufo.dist <= ufo.rad)
    crit = rest + root > R
    return bool(zones and crit)

def shoot(ufos, laser, R):
    killed = [u for u in ufos if is_dead(u, laser, R)]
    ufos[:] = [u for u in ufos if u not in killed]

def main():
    iter_input = iter(lambda: input(), None)
    while True:
        Rn = next(iter_input).split()
        R, n = map(int, Rn)
        if not int(R):
            break
        ufo_pack = [Ufo(*map(int, next(iter_input).split())) for _ in range(int(n))]
        f = lambda: min(ufo_pack, key=operator.attrgetter('dist')).angle
        c = itertools.count()
        ans = sum(itertools.starmap(
            lambda _: reach(ufo_pack, R),
            itertools.takewhile(lambda _: ufo_pack, enumerate(c))
        ))
        while ufo_pack:
            laser = f()
            shoot(ufo_pack, laser, R)
            ans += reach(ufo_pack, R)
        print(ans)
main()