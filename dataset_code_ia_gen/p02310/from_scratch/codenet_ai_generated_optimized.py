import math

px, py = map(int, input().split())
cx, cy, r = map(int, input().split())

dx, dy = px - cx, py - cy
d_sq = dx*dx + dy*dy
d = math.sqrt(d_sq)

l = r*r / d_sq
m = r * math.sqrt(d_sq - r*r) / d_sq

x1 = cx + dx * l - dy * m
y1 = cy + dy * l + dx * m
x2 = cx + dx * l + dy * m
y2 = cy + dy * l - dx * m

pts = [(x1, y1), (x2, y2)]
pts.sort(key=lambda p: (p[0], p[1]))

for x, y in pts:
    print(f"{x:.10f} {y:.10f}")