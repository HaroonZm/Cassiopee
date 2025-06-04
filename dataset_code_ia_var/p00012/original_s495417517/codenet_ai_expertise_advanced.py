from sys import stdin

def solve_linear_system(a, b, c, d, e, f):
    det = a * e - b * d
    if det == 0:
        raise ValueError("Singular matrix")
    x = (e * c - b * f) / det
    y = (-d * c + a * f) / det
    return x, y

def point_in_triangle(coords):
    x1, y1, x2, y2, x3, y3, xp, yp = coords
    s, t = solve_linear_system(
        x2 - x1, x3 - x1, xp - x1,
        y2 - y1, y3 - y1, yp - y1
    )
    return 0 < s < 1 and 0 < t < 1 and 0 < s + t < 1

for line in map(str.split, stdin):
    if not line or len(line) < 8:
        continue
    vals = list(map(float, line))
    print('YES' if point_in_triangle(vals) else 'NO')