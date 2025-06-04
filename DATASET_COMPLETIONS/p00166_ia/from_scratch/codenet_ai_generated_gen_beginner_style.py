import math

def polygon_area(radius, angles):
    # angles: list of center angles between vertices in degrees
    # we compute coordinates of vertices on the circle of given radius
    points = []
    current_angle = 0
    points.append((radius * math.cos(math.radians(current_angle)),
                   radius * math.sin(math.radians(current_angle))))
    for v in angles:
        current_angle += v
        points.append((radius * math.cos(math.radians(current_angle)),
                       radius * math.sin(math.radians(current_angle))))
    # shoelace formula for area
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        area += x1*y2 - y1*x2
    return abs(area)/2

while True:
    m = int(input())
    if m == 0:
        break
    angles1 = []
    for _ in range(m-1):
        v = int(input())
        angles1.append(v)
    n = int(input())
    angles2 = []
    for _ in range(n-1):
        v = int(input())
        angles2.append(v)
    # since all polygons inscribed in same circle, radius can be 1
    area1 = polygon_area(1, angles1)
    area2 = polygon_area(1, angles2)
    if abs(area1 - area2) < 1e-9:
        print(0)
    elif area1 > area2:
        print(1)
    else:
        print(2)