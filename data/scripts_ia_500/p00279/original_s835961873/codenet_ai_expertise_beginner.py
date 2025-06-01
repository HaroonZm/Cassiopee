import sys
import math
import operator

def triangle(a, b, c):
    cross_product = (b.real - a.real)*(c.imag - a.imag) - (b.imag - a.imag)*(c.real - a.real)
    return abs(cross_product) / 2

def solve(point_i, points):
    points = sorted(points, key=lambda p: (p.real - point_i.real) / abs(p - point_i), reverse=True)

    max_q = max(q)
    n = len(points)
    # Initialize a 3D list filled with (inf,)
    area = [[[ (float('inf'), ) for _ in range(n)] for _ in range(n)] for _ in range(max_q + 1)]

    for j in range(n-1):
        for k in range(j+1, n):
            area[3][j][k] = (triangle(point_i, points[j], points[k]), (point_i, points[j], points[k]))

    for i in range(4, max_q + 1):
        for j in range(n):
            for k in range(j+1, n):
                if area[i-1][j][k][0] == float('inf'):
                    continue
                for s in range(k+1, n):
                    # Check polygon convexity by triangle area > 0
                    area_triangle = triangle(points[j], points[k], points[s])
                    if area_triangle <= 0:
                        continue
                    tmp_area = area[3][k][s][0] + area[i-1][j][k][0]
                    if area[i][k][s][0] <= tmp_area:
                        continue
                    area[i][k][s] = (tmp_area, area[i-1][j][k][1] + (points[s],))

    min_space = [(float('inf'), )] * (max_q + 1)
    for i in range(3, max_q + 1):
        min_space[i] = min([item for sublist in area[i] for item in sublist], key=lambda x: x[0])
    return min_space

f = sys.stdin

n = int(f.readline())
xy = []
for _ in range(n):
    x_str, y_str = f.readline().split()
    x = int(x_str)
    y = int(y_str)
    xy.append(complex(x, y))

m = int(f.readline())
q = []
for _ in range(m):
    q.append(int(f.readline()))

id_map = {point: idx + 1 for idx, point in enumerate(xy)}
xy.sort(key=lambda p: (p.imag, p.real))

min_space = [(float('inf'), )] * (max(q) + 1)

while len(xy) > 2:
    first = xy.pop(0)
    temp = solve(first, xy)
    min_space = [min(ms, t, key=lambda x: x[0]) for ms, t in zip(min_space, temp)]

for qi in q:
    if min_space[qi][0] == float('inf'):
        print("NA")
    else:
        print(*[id_map[p] for p in min_space[qi][1]])