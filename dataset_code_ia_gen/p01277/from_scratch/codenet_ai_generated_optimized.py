import sys
import math
sys.setrecursionlimit(10**7)

input=int(sys.stdin.readline)

def orientation(p, q, r):
    # orientation test for triplet (p,q,r)
    val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    points = sorted(points)
    if len(points)<=1:
        return points
    lower = []
    for p in points:
        while len(lower)>=2 and orientation(lower[-2],lower[-1],p)!=2:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>=2 and orientation(upper[-2],upper[-1],p)!=2:
            upper.pop()
        upper.append(p)
    hull = lower[:-1]+upper[:-1]
    return hull

def dist_sq(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def polygon_area(poly):
    area=0
    n = len(poly)
    for i in range(n):
        j=(i+1)%n
        area += poly[i][0]*poly[j][1]-poly[j][0]*poly[i][1]
    return abs(area)/2

def is_simple_polygon(poly):
    n = len(poly)
    for i in range(n):
        a1 = poly[i]
        a2 = poly[(i+1)%n]
        for j in range(i+1,n):
            if abs(i-j)<=1 or (i==0 and j==n-1) or (j==0 and i==n-1):
                continue
            b1 = poly[j]
            b2 = poly[(j+1)%n]
            if intersect(a1,a2,b1,b2):
                return False
    return True

def on_segment(p,q,r):
    return (min(p[0],r[0])<=q[0]<=max(p[0],r[0]) and min(p[1],r[1])<=q[1]<=max(p[1],r[1]))

def intersect(p1,q1,p2,q2):
    o1 = orientation(p1,q1,p2)
    o2 = orientation(p1,q1,q2)
    o3 = orientation(p2,q2,p1)
    o4 = orientation(p2,q2,q1)

    if o1!=o2 and o3!=o4:
        return True
    if o1==0 and on_segment(p1,p2,q1):
        return True
    if o2==0 and on_segment(p1,q2,q1):
        return True
    if o3==0 and on_segment(p2,p1,q2):
        return True
    if o4==0 and on_segment(p2,q1,q2):
        return True
    return False

def reflect_point(p, a, b):
    # reflect p across line through a,b
    # line vector
    vx = b[0]-a[0]
    vy = b[1]-a[1]
    # vector p->a
    wx = p[0]-a[0]
    wy = p[1]-a[1]
    # projection length
    proj_len = (wx*vx+wy*vy)/(vx*vx+vy*vy)
    # closest point on line
    cx = a[0] + proj_len*vx
    cy = a[1] + proj_len*vy
    # vector from p to closest point
    dx = cx - p[0]
    dy = cy - p[1]
    # reflected point
    rx = p[0]+2*dx
    ry = p[1]+2*dy
    return (rx, ry)

def equal_points(p1, p2):
    return (abs(p1[0]-p2[0])<1e-9 and abs(p1[1]-p2[1])<1e-9)

def normalize(poly):
    # rotate to smallest lex point, then check order to keep ccw
    n = len(poly)
    idx = 0
    for i in range(1,n):
        if poly[i]<poly[idx]:
            idx=i
    res = poly[idx:] + poly[:idx]
    # check area sign (orientation)
    area=0
    for i in range(n):
        x1,y1=res[i]
        x2,y2=res[(i+1)%n]
        area += (x1*y2 - x2*y1)
    if area<0:
        res=res[:1]+res[:0:-1]
    return res

N = input()
points = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

hull = convex_hull(points)
if len(hull)<3:
    print("No")
    sys.exit()

polygon = normalize(hull)

n = len(polygon)

# Try symmetry axis through all pairs of points (including identical points for midpoint axis)
# For each candidate axis, check if polygon is symmetric.

# To verify symmetry efficiently, use set of points to check reflections
pointset = set(polygon)

def check_axis(a,b):
    # check if reflecting polygon across line a,b yields the same polygon
    # for each vertex p, reflected p' should be in polygon
    for p in polygon:
        rp = reflect_point(p,a,b)
        # floating fix
        rp_round = (round(rp[0],6), round(rp[1],6))
        if not any(abs(rp[0]-q[0])<1e-6 and abs(rp[1]-q[1])<1e-6 for q in polygon):
            return False
    return True

# To reduce candidates:
# The symmetry axis passes through
# - midpoint of opposite vertices (for even polygon)
# - line through midpoints of opposite edges (for even polygon)
# - line through vertex and midpoint of opposite edge (for odd polygon)

if n%2==0:
    # even number of vertices: axis passes through midpoints of opposite vertices or through midpoints of opposite edges
    # check axis passing through midpoints of vertex pairs
    for i in range(n//2):
        p1 = polygon[i]
        p2 = polygon[(i+n//2)%n]
        mid = ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
        # axis candidate as perpendicular bisector of p1,p2
        # direction vector perpendicular to p2-p1
        vx = p2[0]-p1[0]
        vy = p2[1]-p1[1]
        # axis line: through mid with normal vector (vx,vy)
        # So line through mid and direction perpendicular (-vy, vx)
        a = (mid[0]-vy, mid[1]+vx)
        b = (mid[0]+vy, mid[1]-vx)
        if check_axis(a,b):
            print("Yes")
            sys.exit()
    # check axis through midpoints of opposite edges
    for i in range(n//2):
        e1p1 = polygon[i]
        e1p2 = polygon[(i+1)%n]
        e2p1 = polygon[(i+n//2)%n]
        e2p2 = polygon[(i+n//2+1)%n]
        m1 = ((e1p1[0]+e1p2[0])/2,(e1p1[1]+e1p2[1])/2)
        m2 = ((e2p1[0]+e2p2[0])/2,(e2p1[1]+e2p2[1])/2)
        if equal_points(m1,m2):
            # axis line through m1,m2 is ill defined (same point)
            continue
        if check_axis(m1,m2):
            print("Yes")
            sys.exit()
else:
    # odd number of vertices: axis passes through vertex and midpoint of opposite edge
    for i in range(n):
        vp = polygon[i]
        e1p1 = polygon[(i+(n//2))%n]
        e1p2 = polygon[(i+(n//2)+1)%n]
        mid = ((e1p1[0]+e1p2[0])/2,(e1p1[1]+e1p2[1])/2)
        if equal_points(vp, mid):
            # degenerate axis line
            continue
        if check_axis(vp, mid):
            print("Yes")
            sys.exit()

print("No")