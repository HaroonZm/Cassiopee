import sys
import math

def polygon_area(poly):
    area = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        area += x1*y2 - y1*x2
    return abs(area)/2

def polygon_contains(poly, p):
    # Convex polygon point inside test via cross products
    n = len(poly)
    x, y = p
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        cross = (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1)
        if cross < -1e-14:  # strictly less: point outside or on concave side
            return False
    return True

def seg_circle_intersections(p1, p2, c, r):
    # Returns intersection points of segment p1p2 with circle center c radius r
    # Source: geometric formulas
    x1, y1 = p1
    x2, y2 = p2
    cx, cy = c
    dx = x2 - x1
    dy = y2 - y1
    fx = x1 - cx
    fy = y1 - cy

    a = dx*dx + dy*dy
    b = 2*(fx*dx + fy*dy)
    c_val = fx*fx + fy*fy - r*r

    disc = b*b - 4*a*c_val
    if disc < -1e-14:
        return []
    elif disc < 1e-14:
        t = -b/(2*a)
        if 0 <= t <= 1:
            return [(x1 + t*dx, y1 + t*dy)]
        else:
            return []
    else:
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc)/(2*a)
        t2 = (-b + sqrt_disc)/(2*a)
        points = []
        if 0 <= t1 <= 1:
            points.append((x1 + t1*dx, y1 + t1*dy))
        if 0 <= t2 <= 1:
            points.append((x1 + t2*dx, y1 + t2*dy))
        return points

def clip_polygon_with_circle(poly, c, r):
    # Clip convex polygon by disk: polygon ∩ disk
    # We do this by polygon clipping with the circle boundary.
    # For each edge, add intersection points with circle, and clip away polygon parts outside the circle.
    # We'll do a polygon clipping with the circle by walking through edges.

    def point_in_circle(p):
        x, y = p
        cx, cy = c
        return (x - cx)**2 + (y - cy)**2 <= r*r + 1e-14

    new_poly = []
    n = len(poly)
    for i in range(n):
        curr = poly[i]
        nxt = poly[(i+1)%n]
        curr_in = point_in_circle(curr)
        nxt_in = point_in_circle(nxt)

        if curr_in:
            new_poly.append(curr)
        inters = seg_circle_intersections(curr, nxt, c, r)
        # For stable polygon ordering, add intersection points in order of parameter on segment
        def param_t(p):
            x1, y1 = curr
            x2, y2 = nxt
            px, py = p
            dx = x2 - x1
            if abs(dx) > 1e-14:
                return (px - x1)/dx
            else:
                dy = y2 - y1
                return (py - y1)/dy if abs(dy) > 1e-14 else 0
        inters = sorted(inters, key=param_t)
        for p in inters:
            if not (any(abs(p[0]-np[0])<1e-14 and abs(p[1]-np[1])<1e-14 for np in new_poly)):
                new_poly.append(p)

    # After this, we have a polygon clipping the original polygon with circle boundary.
    # But adding intersections might create non-convex sets (the intersection is convex though).
    # Because the original polygon is convex and intersection with circle remains convex,
    # the polygon formed by this "walk" is convex.

    # We might have duplicated or out of order points, let's reorder polygon points by angle around center:
    if not new_poly:
        return []

    # Sort by angle around circle center for consistency
    cx, cy = c
    new_poly = list(set(new_poly))  # deduplicate
    new_poly.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    return new_poly

def area_of_intersection(poly, c, r):
    # Compute area of polygon ∩ disk with center c radius r
    # We approximate polygon clipped by circle:
    clipped = clip_polygon_with_circle(poly, c, r)
    if not clipped:
        # no intersection polygon points: maybe disk inside polygon or no intersection
        # As fallback, if circle center inside polygon, area is π r^2
        if polygon_contains(poly, c):
            return math.pi*r*r
        else:
            # No intersection
            return 0.0
    else:
        # Polygon clipped by circle boundary
        # Since the clipped polygon is inside both polygon and circle,
        # but clipped polygon might not represent full intersection
        # Because the intersection along curved circle arcs might be missing

        # So approach:
        # polygon ∩ disk = polygon clipped to circle boundary, with boundary parts possibly replaced by circle arcs

        # We'll compute area of polygon clipped by circle polygon approximation,
        # then add the circular segments' areas where polygon edges go outside circle.

        # To do this exactly we would need a complex polygon with circular arcs.
        # Instead, we use a method:
        #   - polygon ∩ disk area =
        #       area(polygon clipped by circle, approximated by polygon) + 
        #       sum of circular segments replacing clipped arcs

        # We try a polygon clipping by circle approximated:
        # For our small constraints and convex polygon, let's do this:

        # We'll build a polygon clipping the polygon with the circle polygon approximated by many vertices

        # Alternative approach: approximate circle by many-side polygon
        # Then clip polygon by this approx circle polygon by Sutherland-Hodgman polygon clipping.

        pass

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def sutherland_hodgman(subjectPolygon, clipPolygon):
    def inside(p, cp1, cp2):
        return cross(cp1, cp2, p) >= -1e-14

    def computeIntersection(s, e, cp1, cp2):
        dc = (cp1[0] - cp2[0], cp1[1] - cp2[1])
        dp = (s[0] - e[0], s[1] - e[1])
        n1 = cp1[0]*cp2[1] - cp1[1]*cp2[0]
        n2 = s[0]*e[1] - s[1]*e[0]
        denom = dc[0]*dp[1] - dc[1]*dp[0]
        if abs(denom) < 1e-14:
            return e  # lines are parallel, unlikely when clipping with convex polygon
        x = (n1*dp[0] - n2*dc[0])/denom
        y = (n1*dp[1] - n2*dc[1])/denom
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
                    inter = computeIntersection(s,e,cp1,cp2)
                    outputList.append(inter)
                outputList.append(e)
            elif inside(s, cp1, cp2):
                inter = computeIntersection(s,e,cp1,cp2)
                outputList.append(inter)
            s = e
        cp1 = cp2
    return outputList

def build_circle_polygon(c, r, steps=360):
    cx, cy = c
    pts = []
    for i in range(steps):
        angle = 2*math.pi*i/steps
        pts.append((cx + r*math.cos(angle), cy + r*math.sin(angle)))
    return pts

def main():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    r = int(input_data[1])
    coords = list(map(int, input_data[2:]))

    poly = [(coords[2*i], coords[2*i+1]) for i in range(n)]

    # The approach:
    # The intersection polygon = polygon clipped by circle polygon approx
    # We approximate the circle by a 360-gon

    circle_poly = build_circle_polygon((0,0), r, 360)  # center not known yet

    # We want to place the disk in any position to maximize the polygon ∩ disk area
    # Because polygon is convex, maximum overlap disk center is inside polygon
    # But disk can be placed anywhere.

    # For small n=10 max, we try this:
    # We test candidate centers among:
    #   - polygon vertices
    #   - polygon edges sampled points
    #   - polygon centroid
    # And refine by gradient ascent / numeric optimization to find best center.

    # First compute polygon centroid as starting guess
    # Use polygon centroid formula
    area_poly = 0
    cx = 0
    cy = 0
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i+1)%n]
        crossp = x0*y1 - x1*y0
        area_poly += crossp
        cx += (x0 + x1)*crossp
        cy += (y0 + y1)*crossp
    area_poly = area_poly / 2
    if abs(area_poly) < 1e-14:
        cx = sum(p[0] for p in poly)/n
        cy = sum(p[1] for p in poly)/n
    else:
        cx /= (6*area_poly)
        cy /= (6*area_poly)

    start_points = []
    for v in poly:
        start_points.append(v)
    # add midpoints of edges
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i+1)%n]
        mid = ((x0 + x1)/2, (y0 + y1)/2)
        start_points.append(mid)
    start_points.append((cx, cy))

    # Also sample points inside polygon on a grid for better coverage
    min_x = min(p[0] for p in poly)
    max_x = max(p[0] for p in poly)
    min_y = min(p[1] for p in poly)
    max_y = max(p[1] for p in poly)

    for dx in [i*(max_x - min_x)/4 for i in range(5)]:
        for dy in [j*(max_y - min_y)/4 for j in range(5)]:
            px = min_x + dx
            py = min_y + dy
            if polygon_contains(poly, (px, py)):
                start_points.append((px, py))

    # Build circle polygon once, centered at origin
    circle_polygon_origin = build_circle_polygon((0,0), r, 360)

    def intersection_area(center):
        cx, cy = center
        # Shift polygon by -center
        # Actually clip polygon with circle center at center
        # Do polygon clipping with circle polygon translated to center
        circle_poly_c = [(p[0]+cx, p[1]+cy) for p in circle_polygon_origin]
        clipped = sutherland_hodgman(poly, circle_poly_c)
        if not clipped:
            return 0.0
        return polygon_area(clipped)

    def gradient_ascent(start, steps=60, step_size=2):
        pos = start
        for _ in range(steps):
            base = intersection_area(pos)
            grads = []
            delta = 1e-3
            for dx, dy in [(delta,0),(0,delta),(-delta,0),(0,-delta)]:
                pos2 = (pos[0]+dx, pos[1]+dy)
                val = intersection_area(pos2)
                grads.append((val - base, dx, dy))
            # average gradient approx
            gx = (grads[0][0] - grads[2][0])/(2*delta)
            gy = (grads[1][0] - grads[3][0])/(2*delta)
            length = math.hypot(gx, gy)
            if length < 1e-10:
                break
            # move step_size in gradient direction
            nx = pos[0] + step_size * gx / length
            ny = pos[1] + step_size * gy / length
            # Keep nx, ny inside bounding box expanded by r
            nx = max(min_x - r, min(max_x + r, nx))
            ny = max(min_y - r, min(max_y + r, ny))
            pos = (nx, ny)
        return intersection_area(pos)

    max_area = 0.0
    for sp in start_points:
        a = gradient_ascent(sp)
        if a > max_area:
            max_area = a

    print(f"{max_area:.6f}")

if __name__ == "__main__":
    main()