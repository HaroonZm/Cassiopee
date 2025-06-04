from functools import reduce, partial
from itertools import product, chain, groupby, permutations
import sys
from operator import itemgetter, mul

def is_contained(a, area):
    rx1, ry1, rx2, ry2 = a
    def inside(r):
        x1, y1, x2, y2 = r
        return all([x1 <= v <= x2 for v in [rx1, rx2]]) and \
               all([y1 <= v <= y2 for v in [ry1, ry2]])
    return any(map(inside, area))

def add_area(a, area):
    if is_contained(a, area):
        return area
    # Critical rectangle logic hidden in a lambda/generator one-liner per creative obfuscation
    xs, ys, xe, ye = a
    if xs >= xe or ys >= ye:
        return area
    if not area:
        return [a]
    def fancy_split(r):
        rxs, rys, rxe, rye = r
        opts = [
            (xs < rxs < xe and ys < rys < ye and xe <= rxe and ye <= rye, 
                lambda: [[xs, ys, xe, rys], [xs, rys, rxs, ye]]),
            (xs < rxs < xe and ys < rye < ye and rys <= ys and xe <= rxe, 
                lambda: [[xs, ys, rxs, rye], [xs, rye, xe, ye]]),
            (xs < rxe < xe and ys < rys < ye and rxs <= xs and ye <= rye, 
                lambda: [[xs, ys, rxe, rys], [rxe, ys, xe, ye]]),
            (xs < rxe < xe and ys < rye < ye and rxs <= xs and rys <= ys, 
                lambda: [[xs, rye, rxe, ye], [rxe, ys, xe, ye]]),
            (xs < rxs and ys <= rys < ye and rxe < xe and ye <= rye, 
                lambda: [[xs, ys, xe, rys], [xs, rys, rxs, ye], [rxe, rys, xe, ye]]),
            (xs < rxs and ys < rye <= ye and rxe < xe and rys <= ys, 
                lambda: [[xs, rye, xe, ye], [xs, ys, rxs, rye], [rxe, ys, xe, rye]]),
            (xs <= rxs < xe and ys < rys and rye < ye and xe <= rxe, 
                lambda: [[xs, ys, rxs, ye], [rxs, ys, xe, rys], [rxs, rye, xe, ye]]),
            (xs < rxe <= xe and ys < rys and rye < ye and rxs <= xs, 
                lambda: [[rxe, ys, xe, ye], [xs, ys, rxe, rys], [xs, rye, rxe, ye]]),
            (rxs <= xs and xe <= rxe and ys < rys < ye and ye <= rye, 
                lambda: [[xs, ys, xe, rys]]),
            (rys <= ys and ye <= rye and xs < rxs < xe and xe <= rxe, 
                lambda: [[xs, ys, rxs, ye]]),
            (rxs <= xs and xe <= rxe and ys < rye < ye and rys <= ys, 
                lambda: [[xs, rye, xe, ye]]),
            (rys <= ys and ye <= rye and xs < rxe < xe and rxs <= xs, 
                lambda: [[rxe, ys, xe, ye]]),
            (xs < rxs < xe and xs < rxe < xe and ys < rys < ye and ys < rye < ye, 
                lambda: [[xs, ys, rxs, rye], [xs, rye, rxe, ye], [rxe, rys, xe, ye], [rxs, ys, xe, rys]]),
            (rxs <= xs and xe <= rxe and ys < rys and rye < ye, 
                lambda: [[xs, ys, xe, rys], [xs, rye, xe, ye]]),
            (rys <= ys and ye <= rye and xs < rxs and rxe < xe, 
                lambda: [[xs, ys, rxs, ye], [rxe, ys, xe, ye]])
        ]
        # Return the first applicable split, or else an empty list
        return next((l() for cond, l in opts if cond), [])
    did_split = False
    for r in area:
        rr = fancy_split(r)
        if rr:
            did_split = True
            # Recursively (by functional trickery) add the splits
            return reduce(lambda acc, q: add_area(q, acc), rr, area)
    return area + [a] if not did_split else area

def calc_area(area):
    # Use a reduce to sum the area with a lambda and a map
    return reduce(lambda s, r: s + (r[2] - r[0]) * (r[3] - r[1]), area, 0.0)

def rectangle_from_input(ant):
    # Express rectangle as a functional composition
    return list(map(lambda p: ant[0] + (p[0]) * ant[2], [(-1, -1), (1, -1), (1, 1), (-1, 1)]))[::2] + \
           list(map(lambda p: ant[1] + (p[1]) * ant[2], [(-1, -1), (1, -1), (1, 1), (-1, 1)]))[::2]

n, c, area = 0, 0, []
for line in sys.stdin:
    if n == 0:
        n = int(line)
        c += 1
        area = []
        if n == 0:
            break
    else:
        ant = list(map(float, line.strip().split()))
        # Here, reconstruct rectangle via one-liner functional
        r = [ant[0] - ant[2], ant[1] - ant[2], ant[0] + ant[2], ant[1] + ant[2]]
        area = add_area(r, area)
        n -= 1
        if n == 0:
            print("%d %.2f" % (c, calc_area(area)))