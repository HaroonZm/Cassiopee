import sys
from math import isclose

def polygon_area(points):
    """
    Compute the area of a polygon given as a list of points (x, y)
    using the shoelace formula.
    Points are assumed to be in counterclockwise order.
    """
    area = 0.0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

def polygon_intersection(poly1, poly2):
    """
    Compute the intersection polygon of two convex polygons poly1 and poly2
    using the Sutherland-Hodgman polygon clipping algorithm.
    Both polygons are lists of points (x, y) in CCW order.
    Returns the intersection polygon as a list of points.
    If there is no intersection, returns empty list.
    """

    def inside(p, edge_start, edge_end):
        # Check if point p is on the left side of edge from edge_start to edge_end
        # using the cross product (z-component)
        x, y = p
        x1, y1 = edge_start
        x2, y2 = edge_end
        return (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1) >= 0

    def intersection(s, e, cp1, cp2):
        # Compute the intersection point of line segment s-e with edge cp1-cp2
        x1, y1 = s
        x2, y2 = e
        x3, y3 = cp1
        x4, y4 = cp2

        # Solve line-line intersection:
        # (x1,y1)+(t)((x2-x1),(y2-y1)) = (x3,y3)+(u)((x4-x3),(y4-y3))
        denom = (y4 - y3)*(x2 - x1) - (x4 - x3)*(y2 - y1)
        # denom == 0 means lines are parallel, but since polygons are convex and edges should intersect, denom!=0
        if isclose(denom, 0.0):
            # Parallel lines, no intersection, returning None (should not happen in polygon clipping)
            return None
        t = ((x4 - x3)*(y1 - y3) - (y4 - y3)*(x1 - x3)) / denom
        return (x1 + t*(x2 - x1), y1 + t*(y2 - y1))

    output_list = poly1
    cp1 = None
    cp2 = None
    for i in range(len(poly2)):
        input_list = output_list
        output_list = []
        cp1 = poly2[i]
        cp2 = poly2[(i + 1) % len(poly2)]
        if not input_list:
            # No polygon to clip
            break
        s = input_list[-1]
        for e in input_list:
            if inside(e, cp1, cp2):
                if not inside(s, cp1, cp2):
                    # Edge from s to e crosses into polygon poly2
                    ip = intersection(s, e, cp1, cp2)
                    if ip is not None:
                        output_list.append(ip)
                output_list.append(e)
            elif inside(s, cp1, cp2):
                # Edge from s to e crosses out of polygon poly2
                ip = intersection(s, e, cp1, cp2)
                if ip is not None:
                    output_list.append(ip)
            s = e
    return output_list

def main():
    input = sys.stdin.read().strip().split()
    idx = 0
    while True:
        if idx+1 >= len(input):
            break
        m = int(input[idx])
        n = int(input[idx+1])
        idx += 2
        if m == 0 and n == 0:
            break
        # Read polygon C1 vertices (x1,y1)
        C1 = []
        for _ in range(m):
            x = int(input[idx])
            y = int(input[idx+1])
            idx += 2
            C1.append((x, y))
        # Read polygon C2 vertices (x2,z2)
        C2 = []
        for _ in range(n):
            x = int(input[idx])
            z = int(input[idx+1])
            idx += 2
            C2.append((x, z))

        # The intersection volume is the area of intersection of C1 and C2 projected on x
        # dimensions times the y-z intersection between the two prisms.
        # Prism P1 extends infinitely in the z direction with cross section C1 in xy plane.
        # Prism P2 extends infinitely in the y direction with cross section C2 in xz plane.
        # The intersection volume is integral over x of intersection length in y multiplied by intersection length in z.

        # Since P1 extends infinitely in z, P2 infinitely in y,
        # the intersection volume consists of points (x,y,z) such that:
        # (x,y) in C1 and (x,z) in C2 simultaneously.
        # So for each x, find vertical slices: intervals of y for C1 at that x, intervals of z for C2 at that x,
        # then volume = integral over x of (y_interval_length * z_interval_length)

        # Because polygons are convex and defined in 2D, we can find for each polygon
        # the y-interval at given x (for C1) and z-interval at given x (for C2).

        # Let's find the intersection x-range (common range in x for both polygons)
        xs1 = [p[0] for p in C1]
        xs2 = [p[0] for p in C2]
        xmin = max(min(xs1), min(xs2))
        xmax = min(max(xs1), max(xs2))
        if xmin > xmax:
            # No overlap in x dimension means zero volume
            print(0.0)
            continue

        def get_interval(polygon, x, coord1_idx, coord2_idx):
            """
            Given a polygon and x, find the interval of coord2 (y or z)
            such that (x, coord2) lies within the polygon.

            polygon: list of points in CCW order
            coord1_idx: index of coordinate to fix (0 for x)
            coord2_idx: index of coordinate to get interval (1 for y or z)
            Returns (min_val, max_val) or None if outside polygon at x.
            """
            intervals = []
            n = len(polygon)
            for i in range(n):
                p1 = polygon[i]
                p2 = polygon[(i + 1) % n]
                x1 = p1[coord1_idx]
                x2 = p2[coord1_idx]
                if x1 == x2:
                    # Vertical edge for x? If x == x1==x2,
                    # The edge spans y or z between p1 and p2.
                    if isclose(x, x1):
                        intervals.append((min(p1[coord2_idx], p2[coord2_idx]), max(p1[coord2_idx], p2[coord2_idx])))
                    # else skip
                else:
                    # Edge crosses x if x between x1 and x2
                    if (x1 <= x <= x2) or (x2 <= x <= x1):
                        # Linearly interpolate coord2 at x
                        t = (x - x1) / (x2 - x1)
                        val = p1[coord2_idx] + t * (p2[coord2_idx] - p1[coord2_idx])
                        intervals.append(val)
            # intervals should contain pairs or a set of values, for convex polygon these appear in pairs
            if len(intervals) == 0:
                return None
            elif len(intervals) == 1:
                # touch at a vertex (probably zero length segment)
                return (intervals[0], intervals[0])
            else:
                # Separate scalar interval values from pairs:
                # intervals can contain floats or tuples (from vertical edges)
                # Separate flats and tuples:
                flats = [v for v in intervals if isinstance(v, float) or isinstance(v, int)]
                spans = [v for v in intervals if isinstance(v, tuple)]
                # For polygon edges crossing x, we get floats, they should be paired (two intersections)
                if len(flats) == 2:
                    low, high = min(flats), max(flats)
                else:
                    low, high = None, None
                # For vertical edges if x==x1
                for span in spans:
                    low_span, high_span = span
                    if low is None:
                        low, high = low_span, high_span
                    else:
                        low = min(low, low_span)
                        high = max(high, high_span)
                if low is None:
                    return None
                return (low, high)

        # We will integrate over x from xmin to xmax using sampling (adaptive)
        # Because polygons have at most 100 vertices, polygon edges change linear.
        # Using a fine step size should be sufficient (e.g. 0.001)
        # Sum(y_interval_length * z_interval_length * dx) over x

        dx = 1e-3
        volume = 0.0
        x = xmin
        while x <= xmax + 1e-12:
            iy = get_interval(C1, x, 0, 1)  # y interval at x in C1 polygon
            iz = get_interval(C2, x, 0, 1)  # z interval at x in C2 polygon, coordinate '1' means z here, since polygon points are (x,z)
            if iy is not None and iz is not None:
                y_len = iy[1] - iy[0]
                z_len = iz[1] - iz[0]
                # If lengths negative or zero means no intersection at this x
                if y_len > 0 and z_len > 0:
                    volume += y_len * z_len * dx
            x += dx

        print(volume)

if __name__ == "__main__":
    main()