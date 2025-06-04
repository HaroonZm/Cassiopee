from math import acos, sin, hypot
from functools import partial

def angle(ax, ay, ox, oy, bx, by):
    """Calcule l'angle formé en O par les points A et B."""
    oa_x, oa_y = ax - ox, ay - oy
    ob_x, ob_y = bx - ox, by - oy
    dot = oa_x * ob_x + oa_y * ob_y
    norm = hypot(oa_x, oa_y) * hypot(ob_x, ob_y)
    return acos(dot / norm) if norm else 0.0

def circumcircle(x1, y1, x2, y2, x3, y3):
    """Calcule le cercle circonscrit à un triangle."""
    p = ((x1, y1), (x2, y2), (x3, y3))
    angs = [angle(*p[(i+2)%3], *p[i], *p[(i+1)%3]) for i in range(3)]
    s2 = list(map(lambda a: sin(2*a), angs))
    sx = sum(s2[i]*p[i][0] for i in range(3))
    sy = sum(s2[i]*p[i][1] for i in range(3))
    denom = sum(s2)
    px, py = sx/denom, sy/denom
    r = hypot(x2-x3, y2-y3) / (2 * sin(angs[1]))
    return px, py, r

def main():
    import sys
    lines = (line for line in sys.stdin if line.strip())
    n = int(next(lines))
    fcirc = partial(map, float)
    for _ in range(n):
        params = tuple(fcirc(next(lines).split()))
        print("{:.3f} {:.3f} {:.3f}".format(*circumcircle(*params)))

if __name__ == "__main__":
    main()