import sys

def max_square_area(points):
    point_set = set(points)
    max_area = 0
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1

            # Rotate vector (dx, dy) by 90 degrees to get perpendicular vector
            perp_dx = -dy
            perp_dy = dx

            # Third and fourth points when going clockwise
            x3 = x2 + perp_dx
            y3 = y2 + perp_dy
            x4 = x1 + perp_dx
            y4 = y1 + perp_dy
            if (x3, y3) in point_set and (x4, y4) in point_set:
                area = dx*dx + dy*dy
                if area > max_area:
                    max_area = area

            # Third and fourth points when going counter-clockwise
            perp_dx = dy
            perp_dy = -dx
            x3 = x2 + perp_dx
            y3 = y2 + perp_dy
            x4 = x1 + perp_dx
            y4 = y1 + perp_dy
            if (x3, y3) in point_set and (x4, y4) in point_set:
                area = dx*dx + dy*dy
                if area > max_area:
                    max_area = area
    return max_area

while True:
    line = sys.stdin.readline()
    if not line:
        break
    n = int(line.strip())
    if n == 0:
        break
    points = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    result = max_square_area(points)
    print(result)