import math

def read_n():
    return int(raw_input())

def read_points(n):
    return [list(map(float, raw_input().split())) for _ in xrange(n)]

def sorted_points(points):
    return sorted(points)

def xd_yd(x1, y1, x2, y2):
    return x2 - x1, y2 - y1

def d_from_xd_yd(xd, yd):
    return xd**2 + yd**2

def k_from_d(d):
    return math.sqrt((4.0 - d) / d) / 2.0

def xc_yc(x1, y1, x2, y2):
    return (x1 + x2) / 2.0, (y1 + y2) / 2.0

def update_xd_yd(xd, yd, k):
    return xd * k, yd * k

def get_centers(x1, y1, x2, y2, xd, yd, xc, yc):
    return [[xc - yd, yc + xd], [xc + yd, yc - xd]]

def circle_center(x1, y1, x2, y2):
    xd, yd = xd_yd(x1, y1, x2, y2)
    d = d_from_xd_yd(xd, yd)
    k = k_from_d(d)
    xc, yc = xc_yc(x1, y1, x2, y2)
    xd, yd = update_xd_yd(xd, yd, k)
    return get_centers(x1, y1, x2, y2, xd, yd, xc, yc)

def point_in_unit_circle(ex, ey, dx, dy):
    if ex - dx >= 1.0: return False
    if dx - ex >= 1.0: return False
    if abs(ey - dy) > 1.0: return False
    if (ex - dx) ** 2 + (ey - dy) ** 2 > 1.0: return False
    return True

def can_form_circle(bx, by, cx, cy):
    if cx - bx >= 2.0:
        return False
    if abs(by - cy) > 2.0:
        return False
    if (bx - cx) ** 2 + (by - cy) ** 2 > 4.0:
        return False
    return True

def count_points_in_circle(cent, i, j, p, prev, n):
    ex, ey = cent
    count = 2
    for k in xrange(prev, n):
        if k == i or k == j:
            continue
        dx, dy = p[k]
        if ex - dx >= 1.0:
            continue
        if dx - ex >= 1.0:
            break
        if point_in_unit_circle(ex, ey, dx, dy):
            count += 1
    return count

def update_max(ans, count):
    return max(ans, count)

def solution_loop():
    while True:
        n = read_n()
        if n == 0:
            break
        points = read_points(n)
        p = sorted_points(points)
        prev = 0
        ans = 1
        for i in xrange(n):
            bx, by = p[i]
            while bx - p[prev][0] >= 2.0:
                prev += 1
            for j in xrange(i + 1, n):
                cx, cy = p[j]
                if not can_form_circle(bx, by, cx, cy):
                    break
                centers = circle_center(bx, by, cx, cy)
                for cent in centers:
                    count = count_points_in_circle(cent, i, j, p, prev, n)
                    ans = update_max(ans, count)
        print ans

solution_loop()