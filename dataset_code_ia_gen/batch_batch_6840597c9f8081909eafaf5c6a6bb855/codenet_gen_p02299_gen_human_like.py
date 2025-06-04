def on_segment(px, py, qx, qy, rx, ry):
    # Check if point q lies on segment pr
    return (min(px, rx) <= qx <= max(px, rx)) and (min(py, ry) <= qy <= max(py, ry))

def orientation(px, py, qx, qy, rx, ry):
    # Calculate orientation of ordered triplet (p, q, r)
    val = (qy - py) * (rx - qx) - (qx - px) * (ry - qy)
    if val == 0:
        return 0  # colinear
    return 1 if val > 0 else 2  # clock or counterclock wise

def point_on_edge(px, py, polygon):
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]
        if orientation(x1, y1, px, py, x2, y2) == 0 and on_segment(x1, y1, px, py, x2, y2):
            return True
    return False

def point_in_polygon(px, py, polygon):
    n = len(polygon)
    count = 0
    INF = 10001  # beyond coordinate range
    x_extreme, y_extreme = INF, py
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Check if the line segment from (px, py) to (x_extreme, y_extreme) intersects with side (x1, y1)-(x2, y2)
        o1 = orientation(x1, y1, x2, y2, px, py)
        o2 = orientation(x1, y1, x2, y2, x_extreme, y_extreme)
        o3 = orientation(px, py, x_extreme, y_extreme, x1, y1)
        o4 = orientation(px, py, x_extreme, y_extreme, x2, y2)

        if o1 != o2 and o3 != o4:
            count += 1
        else:
            # Handle special case when points are colinear
            if o1 == 0 and on_segment(x1, y1, px, py, x2, y2):
                return True  # point is on edge

    return count % 2 == 1

def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    polygon = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        if point_on_edge(x, y, polygon):
            print(1)
        elif point_in_polygon(x, y, polygon):
            print(2)
        else:
            print(0)

if __name__ == "__main__":
    main()