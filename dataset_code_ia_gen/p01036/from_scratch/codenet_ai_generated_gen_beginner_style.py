import sys
import math

sys.setrecursionlimit(10**7)

def point_on_line(px, py, x1, y1, x2, y2):
    # Check if point (px,py) lies on the line segment (x1,y1)-(x2,y2)
    if min(x1, x2) - 1e-14 <= px <= max(x1, x2) + 1e-14 and min(y1, y2) - 1e-14 <= py <= max(y1, y2) + 1e-14:
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) < 1e-14 and abs(px - x1) < 1e-14:
            return True
        if abs(dy) < 1e-14 and abs(py - y1) < 1e-14:
            return True
        if abs(dx) > 1e-14:
            t = (px - x1) / dx
            return abs(y1 + dy*t - py) < 1e-14
    return False

def is_point_in_polygon(px, py, polygon):
    # polygon: list of (x,y) tuples
    n = len(polygon)
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]
        # Check if point lies exactly on edge
        if point_on_line(px, py, x1, y1, x2, y2):
            return False  # On edge is no score

    # Ray casting algorithm to check inside polygon
    count = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]
        # Check if the horizontal ray to the right intersects with edge
        if y1 == y2:
            continue
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if py <= y1 or py > y2:
            continue
        x_int = (py - y1) * (x2 - x1) / (y2 - y1) + x1
        if x_int > px:
            count += 1
    return count % 2 == 1

def main():
    input_line = input().split()
    n = int(input_line[0])
    cx = int(input_line[1])
    cy = int(input_line[2])
    r = int(input_line[3])

    polygons = []
    for _ in range(n):
        line = input().split()
        p = int(line[0])
        score = int(line[1])
        coords = []
        for __ in range(p):
            xy = input().split()
            x = int(xy[0])
            y = int(xy[1])
            coords.append((x,y))
        polygons.append((p,score, coords))

    samples = 200000  # Number of random samples for Monte Carlo
    count_in_circle = 0
    total_score = 0.0

    import random

    for _ in range(samples):
        # Random point in circle uniform distribution
        angle = random.uniform(0, 2*math.pi)
        length = r * math.sqrt(random.uniform(0,1))
        x = cx + length * math.cos(angle)
        y = cy + length * math.sin(angle)

        point_score = 0
        for (p,score,polygon) in polygons:
            if is_point_in_polygon(x,y,polygon):
                point_score = score
                break
        total_score += point_score

    expected_value = total_score / samples

    print("{0:.10f}".format(expected_value))

if __name__ == "__main__":
    main()