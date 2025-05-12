import itertools

def _get_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def _get_min_distance(points):
    min_d = 400
    for p1, p2 in itertools.combinations(points, 2):
        min_d = min(min_d, _get_distance(p1, p2))
    return min_d

def closest_pair_distance(points):
    n = len(points)
    if n <= 3:
        return _get_min_distance(points)
    else:
        mid = n // 2
        px, py = zip(*points)
        if len(set(px)) > len(set(py)):
            points.sort(key = lambda p: p[0])
            # axis: x; 0, y; 1
            axis1 = 0
            axis2 = 1
        else:
            points.sort(key = lambda p: p[1])
            axis1 = 1
            axis2 = 0
        A_points = points[:mid]
        B_points = points[mid:]
        d_Amin = closest_pair_distance(A_points.copy())
        d_Bmin = closest_pair_distance(B_points.copy())
        dist = min(d_Amin, d_Bmin)
        min_d = dist
        for ap in A_points[::-1]:
            if B_points[0][axis1] - ap[axis1] >= dist:
                break
            for bp in B_points:
                if bp[axis1] - ap[axis1] >= dist:
                    break
                if ap[axis2] - dist < bp[axis2] < ap[axis2] + dist:
                    min_d = min(min_d, _get_distance(ap, bp))
        return min_d

# Acceptance of input
import sys

file_input = sys.stdin

n = int(file_input.readline())

P = [tuple(map(float, line.split())) for line in file_input]

# Solve
ans = closest_pair_distance(P)

print('{:f}'.format(ans))