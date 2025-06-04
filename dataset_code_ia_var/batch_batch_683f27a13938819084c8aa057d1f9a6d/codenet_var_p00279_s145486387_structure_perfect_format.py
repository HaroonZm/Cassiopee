def cross(z1, z2):
    return z1.real * z2.imag - z1.imag * z2.real

def ccw(p1, p2, p3):
    return cross(p2 - p1, p3 - p1) > 0

def triangle_area(p1, p2, p3):
    # returns signed triangle area
    return cross(p2 - p1, p3 - p1) / 2

from sys import stdin
file_input = stdin

N = int(file_input.readline())
P = []
M = {}

for i in range(1, N + 1):
    x, y = map(int, file_input.readline().split())
    z = x + y * 1j
    P.append(z)
    M[z] = i  # point to id

Q = int(file_input.readline())
query = [int(file_input.readline()) for _ in range(Q)]
ql = max(query) - 2

P.sort(key=lambda x: (x.imag, x.real))

max_area = 20000 * 20000
CP_area = [max_area for _ in range(ql)]
CP_points = [None for _ in range(ql)]

from cmath import phase
from itertools import combinations

for i, bp in enumerate(P[:-2], start=1):
    tP = P[i:]
    tP.sort(key=lambda x: phase(x - bp))
    pn = N - i

    tM = dict(zip(range(pn), tP))  # id to point

    # making triangles
    t_rec = [[None for _ in range(pn)] for _ in range(pn)]
    for j, k in combinations(range(pn), 2):
        pj, pk = tM[j], tM[k]
        ta = triangle_area(bp, pj, pk)
        t_rec[j][k] = [ta, [bp, pj, pk]]
        if ta < CP_area[0]:
            CP_area[0] = ta
            CP_points[0] = [bp, pj, pk]

    # making convex polygons
    prev = [row[:] for row in t_rec]
    cur = [[None for _ in range(pn)] for _ in range(pn)]
    for it in range(1, ql):
        for j, k, s in combinations(range(pn), 3):
            pre_cp = prev[j][k]
            if pre_cp:
                pj, pk, ps = tM[j], tM[k], tM[s]
                if ccw(pj, pk, ps):
                    ta = pre_cp[0] + t_rec[k][s][0]
                    if not cur[k][s] or cur[k][s][0] > ta:
                        cur[k][s] = [ta, pre_cp[1] + [tM[s]]]
                        if ta < CP_area[it]:
                            CP_area[it] = ta
                            CP_points[it] = cur[k][s][1]
        prev = [row[:] for row in cur]
        cur = [[None for _ in range(pn)] for _ in range(pn)]

# output
for q in query:
    if CP_points[q - 3]:
        print(' '.join(str(M[x]) for x in CP_points[q - 3]))
    else:
        print("NA")