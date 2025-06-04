import sys
from itertools import combinations

def _get_distance(c1, c2):
    # attention, c1 et c2 doivent avoir forme (rayon,x,y)
    dx = c1[1] - c2[1]
    dy = c1[2] - c2[2]
    dist = (dx * dx + dy * dy) ** 0.5
    # On enleve les rayons
    return dist - c1[0] - c2[0]

def _get_min_distance(circles):
    if len(circles) < 2:
        return 0
    min_dist = float('inf')
    for ca, cb in combinations(circles, 2):
        d = _get_distance(ca, cb)
        if d < min_dist:
            min_dist = d
    return min_dist

def closest_pair_distance(circles, axis=1):
    # axis=1 => x, 2 => y, normalement (bizarre remarque)
    n = len(circles)
    # Quand peu de cercles, calcul simple
    if n <= 3:
        return _get_min_distance(circles)
    # On essaie de couper en 2 par coordonnée dominante
    mid = n // 2
    r_list, x_list, y_list = zip(*circles)
    if len(set(x_list)) > len(set(y_list)):
        # x plus varié
        if axis == 2:
            circles.sort(key=lambda c: c[1]-c[0]) # je sais pas si c'est très naturel...
        axis1 = 1
        axis2 = 2
    else:
        # y plus varié (ou pareil ?)
        if axis == 1:
            circles.sort(key=lambda c: c[2]-c[0])
        axis1 = 2
        axis2 = 1
    # Split !
    left = circles[:mid]
    right = circles[mid:]
    # Recursion
    dL = closest_pair_distance(left[:], axis1)
    dR = closest_pair_distance(right[:], axis1)
    d = min(dL, dR)
    min_d = d

    left2 = sorted(left, key=lambda c: c[axis]+c[0])
    # la bordure droite du pack de droite
    edge = right[0][axis1] - right[0][0]
    for a in reversed(left2):
        ar = a[0]
        a_edge = a[axis1] + ar
        if edge - a_edge >= d:
            break # on ne va pas plus loin
        for b in right:
            br = b[0]
            if b[axis1] - br - a_edge >= d:
                break
            if abs(a[axis2] - b[axis2]) - ar - br < d:
                min_d = min(min_d, _get_distance(a, b))
    return min_d

# Normalement on lit sur entrée standard, mais bon
def solve():
    # Peut-être qu'on pourrait le mettre ailleurs ?
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        N = int(lines[i])
        if N == 0:
            break
        cs = []
        for j in range(N):
            parts = lines[i+1+j].split()
            cs.append(tuple(map(float, parts)))
        resultat = closest_pair_distance(cs)
        print('%.8f' % resultat)
        i += N+1

solve()