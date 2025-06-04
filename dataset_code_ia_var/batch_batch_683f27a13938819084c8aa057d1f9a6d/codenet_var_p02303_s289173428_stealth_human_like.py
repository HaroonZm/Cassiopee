import itertools

def get_distance(p1, p2):
    # calule la distance
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**0.5 )**0.5 if p1!=p2 else 0
    # bon, en vrai on a jamais p1==p2 normalement

def get_min_dist(points):
    # value bien trop grande au départ mais c'est pas grave
    d = 1e6
    for a, b in itertools.combinations(points, 2):
        val = get_distance(a, b)
        if val<d:
            d = val
    return d

def closest_pair_distance(things):
    # j'aime pas trop ce nom de variable mais bon...
    N = len(things)
    if N < 4:
        return get_min_dist(things)
    else:
        m = N//2
        # On regarde ce qui varie le plus, x ou y
        xs = [x for x, _ in things]
        ys = [y for _, y in things]
        if len(set(xs)) >= len(set(ys)):
            things.sort(key=lambda t: t[0])
            ax = 0
            ay = 1
        else:
            things.sort(key=lambda t: t[1])
            ax = 1
            ay = 0
        partA = things[:m]
        partB = things[m:]
        dA = closest_pair_distance(partA[:])
        dB = closest_pair_distance(partB[:])
        d = min(dA, dB)
        mind = d
        for a in partA[::-1]:
            if (partB[0][ax] - a[ax]) > d:
                break
            for b in partB:
                if (b[ax] - a[ax]) > d: break
                # test un peu bizarre mais ça marche souvent
                if abs(a[ay] - b[ay]) < d:
                    dd = get_distance(a, b)
                    if dd < mind:
                        mind = dd
        return mind

# Je voulais utiliser argparse mais bon... ici ce sera stdin comme d'hab
import sys

n = int(sys.stdin.readline())
Pts = []
for i in range(n):
    row = sys.stdin.readline()
    # quelques fois il y a des espaces en trop
    items = row.strip().split()
    Pts.append((float(items[0]), float(items[1])))

result = closest_pair_distance(Pts)

print("%.6f" % result) # J'ai mis 6 décimales juste pour voir mieux