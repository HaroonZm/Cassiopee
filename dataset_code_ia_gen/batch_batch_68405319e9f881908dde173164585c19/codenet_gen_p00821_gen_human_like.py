import sys

def polygon_edges(vertices):
    m = len(vertices)
    for i in range(m):
        yield vertices[i], vertices[(i + 1) % m]

def edge_intersects_unit_square(p1, p2, x0, y0):
    # Check if the edge intersects the unit square [x0,x0+1] x [y0,y0+1].
    # We check if the segment overlaps the square by checking segments intersections with each edge of the square,
    # or if one endpoint is inside the square or if square is fully inside polygon (not needed here).
    # Since polygon is simple, edge intersection suffices.
    x1, y1 = p1
    x2, y2 = p2

    # Quick rejection if edge bbox does not intersect the square bbox (square is [x0,x0+1] x [y0,y0+1])
    if x1 < x0 and x2 < x0:
        return False
    if x1 > x0 + 1 and x2 > x0 + 1:
        return False
    if y1 < y0 and y2 < y0:
        return False
    if y1 > y0 + 1 and y2 > y0 + 1:
        return False

    # Check if the line segment intersects any segment of the unit square
    square_edges = [((x0, y0), (x0 + 1, y0)),
                    ((x0 + 1, y0), (x0 + 1, y0 + 1)),
                    ((x0 + 1, y0 + 1), (x0, y0 + 1)),
                    ((x0, y0 + 1), (x0, y0))]

    def ccw(A, B, C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(A,B,C,D):
        # returns True if line segments AB and CD intersect
        return (ccw(A,C,D) != ccw(B,C,D)) and (ccw(A,B,C) != ccw(A,B,D))

    for se1, se2 in square_edges:
        if intersect(p1,p2,se1,se2):
            return True

    # If no edge intersection, check if one endpoint inside square
    if x0 <= x1 <= x0 + 1 and y0 <= y1 <= y0 + 1:
        return True
    if x0 <= x2 <= x0 + 1 and y0 <= y2 <= y0 + 1:
        return True

    return False

def point_in_polygon(point, vertices):
    # Ray casting algorithm for point in polygon
    x, y = point
    cnt = 0
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        if y1 == y2:
            continue
        if y < min(y1, y2):
            continue
        if y >= max(y1, y2):
            continue
        # Compute x coordinate of intersection of polygon edge with horizontal line at y
        interx = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        if interx > x:
            cnt += 1
    return (cnt % 2) == 1

def polygon_area_approx(vertices):
    # Determine bounding box
    xs = [v[0] for v in vertices]
    ys = [v[1] for v in vertices]

    xmin = int(min(xs))
    xmax = int(max(xs))
    ymin = int(min(ys))
    ymax = int(max(ys))

    count = 0
    edges = list(polygon_edges(vertices))

    # For each unit square in bounding box, check if it intersects polygon
    # To be efficient, we try to short-circuit:

    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            # First, check if polygon edges intersect this square
            intersects = False
            for p1, p2 in edges:
                if edge_intersects_unit_square(p1, p2, x, y):
                    intersects = True
                    break
            if intersects:
                count += 1
                continue
            # If no edge intersection, check if square center is inside polygon
            # Using center at (x+0.5, y+0.5)
            if point_in_polygon((x + 0.5, y + 0.5), vertices):
                count += 1
    return count

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        m = input_lines[idx].strip()
        idx += 1
        if m == '0':
            break
        m = int(m)
        vertices = []
        for _ in range(m):
            x,y = map(int, input_lines[idx].split())
            idx += 1
            vertices.append((x,y))
        print(polygon_area_approx(vertices))

if __name__ == "__main__":
    main()