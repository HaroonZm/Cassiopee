import math
import random

def intersection_simple(cx, cy, r, x1, y1, x2, y2):
    xd = x2 - x1
    yd = y2 - y1
    X = x1 - cx
    Y = y1 - cy
    a = xd * xd + yd * yd
    b = xd * X + yd * Y
    c = X * X + Y * Y - r * r
    D = b * b - a * c
    result = []
    if D > 0:
        d = math.sqrt(D)
        if 0 < -b - d < a:
            s = (-b - d) / a
            ix = x1 + xd * s
            iy = y1 + yd * s
            result.append((ix, iy))
        if 0 < -b + d < a:
            s = (-b + d) / a
            ix = x1 + xd * s
            iy = y1 + yd * s
            result.append((ix, iy))
    elif D == 0:
        if 0 < -b < a:
            s = -b / a
            ix = x1 + xd * s
            iy = y1 + yd * s
            result.append((ix, iy))
    return result

def calc_area(x0, y0, x1, y1, rr):
    if x0 * x0 + y0 * y0 - rr <= 1e-8 and x1 * x1 + y1 * y1 - rr <= 1e-8:
        return (x0 * y1 - x1 * y0) / 2.0
    theta = math.atan2(x0 * y1 - x1 * y0, x0 * x1 + y0 * y1)
    return theta * rr / 2.0

n, r = map(int, input().split())
P = []
for i in range(n):
    x, y = map(int, input().split())
    P.append([x, y])

def solve(xb, yb):
    rr = r * r
    ans = 0.0
    for i in range(n):
        x0, y0 = P[i - 1]
        x1, y1 = P[i]
        x0 = x0 - xb
        y0 = y0 - yb
        x1 = x1 - xb
        y1 = y1 - yb
        result = intersection_simple(0, 0, r, x0, y0, x1, y1)
        px = x0
        py = y0
        for x, y in result:
            ans += calc_area(px, py, x, y, rr)
            px = x
            py = y
        ans += calc_area(px, py, x1, y1, rr)
    return ans

# Calcul du centre moyen
x0 = 0.0
y0 = 0.0
for x, y in P:
    x0 += x
    y0 += y
x0 /= n
y0 /= n

ans = solve(x0, y0)

random.seed()
for i in range(1000):
    best_area = ans
    new_point = None
    for j in range(100):
        dx = random.randint(-1000000, 1000000) / 10000.0 / (i + 1)
        dy = random.randint(-1000000, 1000000) / 10000.0 / (i + 1)
        area = solve(x0 + dx, y0 + dy)
        if best_area < area:
            best_area = area
            new_point = (x0 + dx, y0 + dy)
    if new_point is not None:
        ans = best_area
        x0, y0 = new_point

print(ans)