import sys
import math

def circles_overlap(c1, c2):
    dx = c1[0] - c2[0]
    dy = c1[1] - c2[1]
    return dx*dx + dy*dy <= 4.0 + 1e-14

def circle_intersections(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    if d > 2 or d < 1e-14:
        return []
    a = d / 2
    h = math.sqrt(1 - a * a)
    xm = x1 + dx * 0.5
    ym = y1 + dy * 0.5
    rx = -dy * (h / d)
    ry = dx * (h / d)
    return [(xm + rx, ym + ry), (xm - rx, ym - ry)]

def inside_any_circle(px, py, circles):
    for (x, y) in circles:
        dx = px - x
        dy = py - y
        if dx*dx + dy*dy <= 1.0 + 1e-14:
            return True
    return False

def count_overlaps(px, py, circles):
    cnt = 0
    for (x, y) in circles:
        dx = px - x
        dy = py - y
        if dx*dx + dy*dy <= 1.0 + 1e-14:
            cnt += 1
    return cnt

lines = sys.stdin.read().strip().split('\n')
i = 0
while True:
    if i >= len(lines):
        break
    n = int(lines[i])
    i += 1
    if n == 0:
        break
    circles = []
    for _ in range(n):
        x, y = lines[i].split(',')
        x, y = float(x), float(y)
        circles.append((x,y))
        i += 1
    candidates = []
    candidates.extend(circles)
    for j in range(n):
        for k in range(j+1,n):
            if circles_overlap(circles[j], circles[k]):
                pts = circle_intersections(circles[j], circles[k])
                candidates.extend(pts)
    max_count = 1
    for px, py in candidates:
        c = count_overlaps(px, py, circles)
        if c > max_count:
            max_count = c
    print(max_count)