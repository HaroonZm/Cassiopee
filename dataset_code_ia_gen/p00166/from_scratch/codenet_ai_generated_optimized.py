import sys
import math

def polygon_area(angles):
    angles.append(360 - sum(angles))
    coords = [(1, 0)]
    angle_sum = 0
    for v in angles:
        angle_sum += v
        rad = math.radians(angle_sum)
        coords.append((math.cos(rad), math.sin(rad)))
    # Shoelace formula
    area = 0
    for i in range(len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+1) % len(coords)]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

input = sys.stdin.read().strip().split()
i = 0
while True:
    if i >= len(input):
        break
    m = int(input[i])
    i += 1
    if m == 0:
        break
    angles1 = list(map(int, input[i:i+m-1]))
    i += m - 1
    n = int(input[i])
    i += 1
    angles2 = list(map(int, input[i:i+n-1]))
    i += n - 1
    a1 = polygon_area(angles1)
    a2 = polygon_area(angles2)
    if abs(a1 - a2) < 1e-10:
        print(0)
    elif a1 > a2:
        print(1)
    else:
        print(2)