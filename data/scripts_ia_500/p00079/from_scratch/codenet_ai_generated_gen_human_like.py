import sys

points = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    x_str, y_str = line.split(',')
    x = float(x_str)
    y = float(y_str)
    points.append((x, y))

n = len(points)
area = 0.0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += x1 * y2 - y1 * x2
area = abs(area) / 2
print(f"{area:.6f}")