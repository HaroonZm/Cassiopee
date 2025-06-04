n = 0
points = []
import sys
for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    x_str,y_str = line.split(',')
    x,y = float(x_str), float(y_str)
    points.append((x,y))
n = len(points)

area = 0.0
for i in range(n):
    x1,y1 = points[i]
    x2,y2 = points[(i+1)%n]
    area += x1*y2 - y1*x2
area = abs(area)/2.0
print(f"{area:.6f}")