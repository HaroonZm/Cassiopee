def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

sequence = 1
while True:
    n = int(input())
    if n == 0:
        break
    polygon = [tuple(map(int, input().split())) for _ in range(n)]
    area = polygon_area(polygon)
    print(sequence, f"{area:.1f}")
    sequence += 1