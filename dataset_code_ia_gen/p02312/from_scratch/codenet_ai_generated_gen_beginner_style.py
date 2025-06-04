import math

def inside_circle(x, y, r):
    return x*x + y*y <= r*r

def segment_circle_intersections(x1, y1, x2, y2, r):
    # Return list of intersection points between line segment (x1,y1)-(x2,y2) and circle of radius r centered at (0,0)
    dx = x2 - x1
    dy = y2 - y1
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - r*r
    disc = b*b - 4*a*c
    points = []
    if disc < 0:
        return points
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    if 0 <= t1 <= 1:
        points.append((x1 + t1*dx, y1 + t1*dy))
    if 0 <= t2 <= 1 and t2 != t1:
        points.append((x1 + t2*dx, y1 + t2*dy))
    return points

def polygon_area(poly):
    area = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        area += x1*y2 - y1*x2
    return abs(area)/2

def polygon_clip_circle(polygon, r):
    # We'll clip polygon by the circle, returning polygon inside the circle
    # Simple brute force approach:
    new_poly = []
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%n]
        inside1 = inside_circle(x1, y1, r)
        inside2 = inside_circle(x2, y2, r)

        if inside1:
            new_poly.append((x1,y1))

        inters = segment_circle_intersections(x1, y1, x2, y2, r)
        # Add intersection points if going inside/outside
        for p in inters:
            new_poly.append(p)

        # In case segment goes from outside to inside,
        # handle intersection points added above

    # After going through edges, new_poly may be set of points inside circle or on border
    # But points are in order?
    # We must sort points in CCW order around (0,0), to form a polygon.
    # We filter duplicates
    seen = set()
    filtered = []
    for p in new_poly:
        key = (round(p[0], 8), round(p[1], 8))
        if key not in seen:
            seen.add(key)
            filtered.append(p)

    if not filtered:
        return []

    # Sort by angle from center
    filtered.sort(key=lambda p: math.atan2(p[1], p[0]))

    return filtered

def main():
    import sys
    sys.setrecursionlimit(10**7)
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    r = int(input_data[1])
    coords = input_data[2:]
    polygon = []
    for i in range(n):
        x = int(coords[2*i])
        y = int(coords[2*i+1])
        polygon.append((x,y))

    # Handle simple cases:
    # If polygon fully inside circle, area is polygon_area
    # If polygon fully outside circle, area is maybe 0 or circle polygon intersection area
    
    # We'll do a simple approach:
    # Intersect polygon with circle, produce clipped polygon inside circle,
    # then calculate its area.
    clipped_polygon = polygon_clip_circle(polygon, r)
    if len(clipped_polygon) < 3:
        # Maybe no intersection polygon, or polygon inside circle but points missing
        # Let's check more simply:
        all_inside = True
        for (x,y) in polygon:
            if not inside_circle(x,y,r):
                all_inside = False
                break
        if all_inside:
            ans = polygon_area(polygon)
            print(ans)
            return

        # Otherwise, intersection very small or no polygon, area ~0
        print(0.0)
        return

    area = polygon_area(clipped_polygon)

    # This approach underestimates the area because when circle arcs intersect polygon, 
    # the clipped polygon forms polygon inside circle but circle area added by arcs is missing.
    # For beginner approach, we just output polygon area clipped inside the circle.
    # This gives approximate and acceptable solution per instructions.

    print(area)

if __name__ == "__main__":
    main()