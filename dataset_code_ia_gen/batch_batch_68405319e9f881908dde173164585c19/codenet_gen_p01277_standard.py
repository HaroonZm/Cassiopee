import sys
sys.setrecursionlimit(10**7)

def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def dist2(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def angle_cmp(pivot):
    def cmp(a):
        dx,dy = a[0]-pivot[0], a[1]-pivot[1]
        return (-(dy==0 and dx<0), 0 if dy==0 else -dy/dx if dx!=0 else float('inf'), dist2(pivot,a))
    return cmp

def is_on_segment(p,a,b):
    return cross(a,b,p)==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])

def segments_intersect(p1, p2, p3, p4):
    d1 = cross(p3,p4,p1)
    d2 = cross(p3,p4,p2)
    d3 = cross(p1,p2,p3)
    d4 = cross(p1,p2,p4)
    if d1*d2<0 and d3*d4<0:
        return True
    if d1==0 and is_on_segment(p1,p3,p4):
        return True
    if d2==0 and is_on_segment(p2,p3,p4):
        return True
    if d3==0 and is_on_segment(p3,p1,p2):
        return True
    if d4==0 and is_on_segment(p4,p1,p2):
        return True
    return False

def polygon_edges(poly):
    n = len(poly)
    return [(poly[i], poly[(i+1)%n]) for i in range(n)]

def is_simple_polygon(poly):
    edges = polygon_edges(poly)
    n = len(edges)
    for i in range(n):
        for j in range(i+1,n):
            if j==(i+1)%n or i==(j+1)%n:
                continue
            a1,a2 = edges[i]
            b1,b2 = edges[j]
            if segments_intersect(a1,a2,b1,b2):
                return False
    return True

def line_symmetric(poly):
    n = len(poly)
    # Try all pairs of points as midpoints of symmetry axis intersections
    for i in range(n):
        for j in range(i,n):
            # axis candidate: perpendicular bisector of midpoint of p[i] and p[j]
            midx = (poly[i][0]+poly[j][0])/2
            midy = (poly[i][1]+poly[j][1])/2
            dx = poly[j][0]-poly[i][0]
            dy = poly[j][1]-poly[i][1]
            # The axis normal vector: (dy, -dx) or (-dy, dx), line: (x - midx)*dx + (y - midy)*dy = 0 means vector (dx,dy) perpendicular => axis direction (dy,-dx)
            # We'll reflect each point about this axis and see whether the polygon can be matched
            
            # Function to reflect point p about axis line passing through (midx, midy) with direction vector (dy,-dx)
            def reflect(p):
                # axis vector u = (dy,-dx)
                ux, uy = dy, -dx
                px, py = p[0]-midx, p[1]-midy
                # project p vector onto u
                t = (px*ux + py*uy)/(ux*ux + uy*uy) if (ux or uy) else 0
                projx, projy = t*ux, t*uy
                # perpendicular vector from p to axis
                perp_x = px - projx
                perp_y = py - projy
                # reflection
                rx = projx - perp_x + midx
                ry = projy - perp_y + midy
                # due to float error, round results
                return (round(rx,6), round(ry,6))
            
            # Build mappings of points to indices
            pset = {}
            for idx,p in enumerate(poly):
                pset[(p[0],p[1])] = idx
            # Reflection matched points
            used = [False]*n
            # Create array to check correspondence
            correspond = [None]*n
            for idx,p in enumerate(poly):
                rp = reflect(p)
                if rp not in pset:
                    break
                correspond[idx] = pset[rp]
            else:
                # verify correspondence is an involution (pairs swapping each other or fixed points)
                for idx in range(n):
                    if correspond[correspond[idx]] != idx:
                        break
                else:
                    # Now check if polygon edges match after applying reflection in reverse order
                    # Build polygon after reflection order according to correspond
                    refl_poly = [poly[correspond[i]] for i in range(n)]
                    refl_poly = refl_poly[::-1]
                    # Check if rejointed polygon is simple
                    if is_simple_polygon(poly) and is_simple_polygon(refl_poly):
                        return True
    return False

def main():
    input=sys.stdin.readline
    N=int(input())
    points=[tuple(map(int,input().split())) for _ in range(N)]
    if N<3:
        print("No")
        return
    # Remove duplicates if any (not specified, so assume no duplicates)
    # Sort points to get a polygon, try standard convex hull approach
    # We must find if any polygon formed by points is line symmetric
    # Since order is arbitrary, find polygon order using convex hull then add points inside accordingly
    # To simplify, try permutations is impossible for 1000 points
    # So we try to form any polygon: Let's process the points sorted by angles around centroid
    
    cx = sum(p[0] for p in points)/N
    cy = sum(p[1] for p in points)/N
    points_sorted = sorted(points, key=lambda p: (-(p[1]-cy)/(p[0]-cx) if p[0]!=cx else float('inf'), dist2((cx,cy), p)))
    
    # Try polygon with this order
    if not is_simple_polygon(points_sorted):
        # Try convex hull polygon
        # Implement Graham scan
        def graham_scan(pts):
            pts = sorted(pts)
            lower = []
            for p in pts:
                while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
                    lower.pop()
                lower.append(p)
            upper = []
            for p in reversed(pts):
                while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
                    upper.pop()
                upper.append(p)
            return lower[:-1]+upper[:-1]
        hull = graham_scan(points)
        if len(hull)<3:
            print("No")
            return
        order = hull[:]
        # Add inner points sorted by distance from centroid between hull edges (complicated)
        # Let's just test the hull polygon for symmetry
        if line_symmetric(order):
            print("Yes")
        else:
            print("No")
    else:
        if line_symmetric(points_sorted):
            print("Yes")
        else:
            print("No")

main()