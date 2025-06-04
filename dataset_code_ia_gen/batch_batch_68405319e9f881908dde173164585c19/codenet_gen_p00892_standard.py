import sys

def polygon_area(poly):
    area = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def polygon_intersection(subjectPolygon, clipPolygon):
    def inside(p, cp1, cp2):
        return (cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
    def intersection(cp1, cp2, s, e):
        dc = (cp1[0] - cp2[0], cp1[1] - cp2[1])
        dp = (s[0] - e[0], s[1] - e[1])
        n1 = cp1[0]*cp2[1] - cp1[1]*cp2[0]
        n2 = s[0]*e[1] - s[1]*e[0]
        denom = dc[0]*dp[1] - dc[1]*dp[0]
        if denom == 0:
            return (0,0)
        x = (n1*dp[0] - n2*dc[0]) / denom
        y = (n1*dp[1] - n2*dc[1]) / denom
        return (x,y)

    outputList = subjectPolygon
    cp1 = clipPolygon[-1]
    for cp2 in clipPolygon:
        inputList = outputList
        outputList = []
        if not inputList:
            break
        s = inputList[-1]
        for e in inputList:
            if inside(e, cp1, cp2):
                if not inside(s, cp1, cp2):
                    outputList.append(intersection(cp1, cp2, s, e))
                outputList.append(e)
            elif inside(s, cp1, cp2):
                outputList.append(intersection(cp1, cp2, s, e))
            s = e
        cp1 = cp2
    return outputList

for line in sys.stdin:
    if line.strip() == '':
        continue
    m, n = map(int, line.split())
    if m == 0 and n == 0:
        break
    C1 = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    C2 = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    xs1 = [x for x, y in C1]
    ys1 = [y for x, y in C1]
    xs2 = [x for x, z in C2]
    zs2 = [z for x, z in C2]

    # Project prisms intersection onto the xy-plane
    # intersection poly in xy-plane is intersection of C1 and projection of C2 onto xy-plane (x,z->x,0) extruded infinitely in y
    # by symmetry, the intersection 3D volume is the double integral over x of intersection area of intervals in y and z

    # The volume is integral over x of length(y intersection) * length(z intersection)

    # For prism 1: cross-sectional polygon C1 in xy-plane
    # For prism 2: cross-sectional polygon C2 in xz-plane
    # Both are infinite height along z and y respectively

    # So intersection volume = ∫ over x of height_y(x) * height_z(x) dx

    # height_y(x) is interval length on y in prism 1 for given x
    # height_z(x) is interval length on z in prism 2 for given x

    # get intervals on y for C1 at x
    # get intervals on z for C2 at x

    # Since polygons are convex, the slices at x are continuous intervals or empty

    import bisect

    def get_interval(poly):
        """Return a list of edges sorted by x, to do linear interpolation for y or z at x"""
        edges = []
        n = len(poly)
        for i in range(n):
            x1, y1 = poly[i]
            x2, y2 = poly[(i+1)%n]
            if x1 == x2:
                xmin = x1
                ymin, ymax = sorted([y1,y2])
                edges.append(('v',xmin,ymin,ymax))
            else:
                if x1 < x2:
                    edges.append(('e', x1, y1, x2, y2))
                else:
                    edges.append(('e', x2, y2, x1, y1))
        # sort edges by their xmin for binary search
        edges.sort(key=lambda e:e[1])
        return edges

    def get_y_at_x(p1, p2, x):
        # linear interpolate y at x between p1 and p2
        x1, y1 = p1
        x2, y2 = p2
        return y1 + (y2 - y1)*(x - x1)/(x2 - x1)

    def slice_interval(poly):
        # For a given polygon in 2D (x,y), compute the vertical interval(s) at x
        xs = [p[0] for p in poly]
        xmin, xmax = min(xs), max(xs)
        # polygon is convex, interval is continuous segment or none
        # intersect polygon with vertical line at x to find y intersections
        # polygon edges crossing vertical line at x:

        # For efficiency we'll just compute y intersections with edges at given x

        def intersect_x(x, p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:
                if x == x1:
                    return [y1, y2]
                else:
                    return []
            elif (x1 <= x <= x2) or (x2 <= x <= x1):
                y = y1 + (y2 - y1)*(x - x1)/(x2 - x1)
                return [y]
            return []

        intersections = []
        n = len(poly)
        for i in range(n):
            p1 = poly[i]
            p2 = poly[(i+1)%n]
            intersections.extend(intersect_x(x, p1, p2))
        intersections = sorted(intersections)
        if len(intersections) < 2:
            return (0,0)
        return (intersections[0], intersections[-1])

    # get all unique xs from both polygons to prepare integration points
    xs = sorted(set([p[0] for p in C1] + [p[0] for p in C2]))

    # subdivide intervals between xs for integration points
    xs_all = []
    for i in range(len(xs)-1):
        xs_all.append(xs[i])
        xs_all.append((xs[i]+xs[i+1])/2)
    xs_all.append(xs[-1])
    xs_all = sorted(set(xs_all))

    volume = 0.0
    for i in range(len(xs_all)-1):
        x1 = xs_all[i]
        x2 = xs_all[i+1]
        # at x1 and x2 get intervals for y and z

        y_int1 = slice_interval(C1, x1)
        y_int2 = slice_interval(C1, x2)
        z_int1 = slice_interval(C2, x1)
        z_int2 = slice_interval(C2, x2)

        # intersection interval length for y and z at each x (y from C1, z from C2)
        ly1 = max(0, y_int1[1] - y_int1[0])
        ly2 = max(0, y_int2[1] - y_int2[0])
        lz1 = max(0, z_int1[1] - z_int1[0])
        lz2 = max(0, z_int2[1] - z_int2[0])

        # volume over [x1,x2] approximated as trapezoidal of ly*lz
        vol1 = ly1 * lz1
        vol2 = ly2 * lz2
        volume += (vol1 + vol2)*(x2 - x1)/2

    print(volume)