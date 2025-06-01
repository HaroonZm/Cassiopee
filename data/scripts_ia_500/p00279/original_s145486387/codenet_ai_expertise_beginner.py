def cross(z1, z2):
    return z1.real * z2.imag - z1.imag * z2.real

def ccw(p1, p2, p3):
    return cross(p2 - p1, p3 - p1) > 0

def triangle_area(p1, p2, p3):
    return cross(p2 - p1, p3 - p1) / 2

import sys
from cmath import phase
from itertools import combinations

input_lines = sys.stdin.readlines()
N = int(input_lines[0])
P = []
M = {}
for i in range(N):
    x, y = map(int, input_lines[i+1].split())
    point = x + y * 1j
    P.append(point)
    M[point] = i + 1

Q = int(input_lines[N+1])
query = [int(line) for line in input_lines[N+2:N+2+Q]]
max_q = max(query)
ql = max_q - 2

P.sort(key=lambda p: (p.imag, p.real))

max_area = 20000 * 20000
CP_area = [max_area] * ql
CP_points = [None] * ql

for i in range(len(P) - 2):
    base_point = P[i]
    rest_points = P[i+1:]
    rest_points.sort(key=lambda p: phase(p - base_point))
    pn = len(rest_points)
    index_to_point = {j: rest_points[j] for j in range(pn)}

    # Calculate areas of triangles between base_point and pairs of points
    t_rec = [[None] * pn for _ in range(pn)]
    for j, k in combinations(range(pn), 2):
        pj = index_to_point[j]
        pk = index_to_point[k]
        area = triangle_area(base_point, pj, pk)
        t_rec[j][k] = [area, [base_point, pj, pk]]
        if area < CP_area[0]:
            CP_area[0] = area
            CP_points[0] = [base_point, pj, pk]

    prev = t_rec
    cur = [[None] * pn for _ in range(pn)]

    for size in range(1, ql):
        for j, k, s in combinations(range(pn), 3):
            pre = prev[j][k]
            if pre is not None:
                pj, pk, ps = index_to_point[j], index_to_point[k], index_to_point[s]
                if ccw(pj, pk, ps):
                    new_area = pre[0] + t_rec[k][s][0]
                    if cur[k][s] is None or cur[k][s][0] > new_area:
                        cur[k][s] = [new_area, pre[1] + [ps]]
                        if new_area < CP_area[size]:
                            CP_area[size] = new_area
                            CP_points[size] = cur[k][s][1]
        prev = [row[:] for row in cur]
        cur = [[None] * pn for _ in range(pn)]

for q in query:
    idx = q - 3
    if 0 <= idx < len(CP_points) and CP_points[idx] is not None:
        points_ids = [str(M[p]) for p in CP_points[idx]]
        print(' '.join(points_ids))
    else:
        print("NA")