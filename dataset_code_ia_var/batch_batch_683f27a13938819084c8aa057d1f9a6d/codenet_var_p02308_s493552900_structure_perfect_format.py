cx, cy, r = map(int, input().split())
q = int(input())

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    px = cx - x1
    py = cy - y1
    s2 = dx ** 2 + dy ** 2
    dot = dx * px + dy * py
    crs = dx * py - dy * px
    delta = (s2 * r ** 2 - crs ** 2) ** 0.5
    t1 = (dot + delta) / s2
    t2 = (dot - delta) / s2
    if (dx < 0 or (dx == 0 and dy < 0)) ^ (t1 > t2):
        t1, t2 = t2, t1
    print(x1 + dx * t1, y1 + dy * t1, x1 + dx * t2, y1 + dy * t2)