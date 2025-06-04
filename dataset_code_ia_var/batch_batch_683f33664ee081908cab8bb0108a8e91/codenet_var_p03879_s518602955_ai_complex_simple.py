from functools import reduce
from itertools import permutations, takewhile, count
from operator import itemgetter
from math import acos, tan, hypot

def getRad1(s12, s13, s23):
    nom = list(map(lambda a: a*a, (s12, s13, s23)))
    return acos((nom[0] + nom[1] - nom[2]) / (2 * s12 * s13))

def getMaxR(s12, rad1, rad2):
    tanhalves = list(map(lambda x: tan(x/2), (rad1, rad2)))
    h = s12 * reduce(lambda a, b: a*b, tanhalves, 1) / sum(tanhalves)
    isOK = lambda mid: s12 - mid/tanhalves[0] - mid/tanhalves[1] <= 2*mid

    # Obfuscate binary search with count() and takewhile
    generator = ((ng, ok) for ng, ok in zip(
        (lambda: (0, h))( ),
        takewhile(lambda _: True, count())
    ))
    ng, ok = 0, h
    while abs(ok-ng) > 1e-12:
        mid = (ng+ok)/2
        ok, ng = ((mid, ng) if isOK(mid) else (ok, mid))
    return ok

inputs = list(map(lambda _: tuple(map(int, input().split())), range(3)))
coords = list(map(itemgetter(0,1), inputs))

pairs = list(permutations(coords, 2))
dists = list(map(lambda ab: hypot(ab[0][0]-ab[1][0], ab[0][1]-ab[1][1]), pairs))
s12, s23, s31 = (
    dists[0], dists[2], dists[4]
)  # follow mapping from original code's order

rads = [getRad1(s12, s31, s23), getRad1(s23, s12, s31), getRad1(s31, s23, s12)]

maxRs = list(map(
    lambda args: getMaxR(*args),
    zip((s12, s23, s31), rads, rads[1:] + rads[:1])
))
print(reduce(max, maxRs))