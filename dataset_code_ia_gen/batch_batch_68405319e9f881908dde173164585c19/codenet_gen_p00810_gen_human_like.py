import sys
import math
import random

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def is_in_sphere(p, c, r):
    return dist(p, c) <= r + 1e-14

def sphere_of(points):
    if not points:
        return ((0,0,0), 0)
    elif len(points) == 1:
        return (points[0], 0)
    elif len(points) == 2:
        c = tuple((points[0][i] + points[1][i]) / 2 for i in range(3))
        r = dist(points[0], c)
        return (c, r)
    elif len(points) == 3:
        return circumscribed_sphere_3(points[0], points[1], points[2])
    else:
        return circumscribed_sphere_4(points[0], points[1], points[2], points[3])

def circumscribed_sphere_3(a, b, c):
    # Find the circumscribed sphere of 3 points (circle in 3D)
    # Compute plane normal
    AB = [b[i] - a[i] for i in range(3)]
    AC = [c[i] - a[i] for i in range(3)]
    def cross(u,v):
        return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
    def dot(u,v):
        return sum(u[i]*v[i] for i in range(3))
    n = cross(AB, AC)
    norm_n = math.sqrt(dot(n,n))
    if norm_n == 0:
        # Points are colinear, sphere is defined by the two furthest points
        dists = [(dist(a,b), (a,b)), (dist(a,c), (a,c)), (dist(b,c), (b,c))]
        dists.sort()
        far_pts = dists[-1][1]
        c_ = tuple((far_pts[0][i] + far_pts[1][i])/2 for i in range(3))
        r_ = dist(far_pts[0], c_)
        return (c_, r_)
    n = tuple(n[i]/norm_n for i in range(3))

    def proj_onto(u, v):
        # project u on v
        dp = dot(u,v)
        norm_v_sq = dot(v,v)
        return tuple(dp/norm_v_sq * v[i] for i in range(3))
    AB_mid = tuple((a[i] + b[i])/2 for i in range(3))
    AC_mid = tuple((a[i] + c[i])/2 for i in range(3))
    # direction of perpendicular bisectors in plane
    AB_perp = cross(n, AB)
    AC_perp = cross(n, AC)

    # Solve for intersection of two lines: 
    # AB_mid + t * AB_perp = AC_mid + s * AC_perp
    # rearranged as t*AB_perp - s*AC_perp = AC_mid - AB_mid
    def sub(u,v): return tuple(u[i]-v[i] for i in range(3))
    def scalar_multiply(v, s): return tuple(v[i]*s for i in range(3))

    right = sub(AC_mid, AB_mid)

    # We solve in 2D (plane), choose axes u and v
    # Create coordinate system on plane
    u = AB
    unorm = math.sqrt(dot(u,u))
    u = tuple(u[i]/unorm for i in range(3))
    v = cross(n,u)

    def to2d(p):
        ap = sub(p, AB_mid)
        return (dot(ap,u), dot(ap,v))
    abp = to2d(AB_perp)
    acp = to2d(AC_perp)
    r2d = to2d(right)

    # Solve 2x2
    denom = abp[0]*acp[1] - abp[1]*acp[0]
    if abs(denom) < 1e-20:
        # Lines parallel, fallback to farthest two points
        dists = [(dist(a,b), (a,b)), (dist(a,c), (a,c)), (dist(b,c), (b,c))]
        dists.sort()
        far_pts = dists[-1][1]
        c_ = tuple((far_pts[0][i] + far_pts[1][i])/2 for i in range(3))
        r_ = dist(far_pts[0], c_)
        return (c_, r_)
    t = (r2d[0]*acp[1] - r2d[1]*acp[0]) / denom
    center = tuple(AB_mid[i] + t*AB_perp[i] for i in range(3))
    radius = dist(center, a)
    return (center, radius)

def circumscribed_sphere_4(a,b,c,d):
    # Solve for sphere through 4 points, linear system
    # https://math.stackexchange.com/questions/1460093/find-center-and-radius-of-sphere-given-4-points-in-3d
    import numpy as np

    A = np.array([
        [b[0]-a[0], b[1]-a[1], b[2]-a[2]],
        [c[0]-a[0], c[1]-a[1], c[2]-a[2]],
        [d[0]-a[0], d[1]-a[1], d[2]-a[2]],
    ])
    B = np.array([
        [(b[0]**2 - a[0]**2 + b[1]**2 - a[1]**2 + b[2]**2 - a[2]**2)/2],
        [(c[0]**2 - a[0]**2 + c[1]**2 - a[1]**2 + c[2]**2 - a[2]**2)/2],
        [(d[0]**2 - a[0]**2 + d[1]**2 - a[1]**2 + d[2]**2 - a[2]**2)/2],
    ])
    try:
        center = np.linalg.solve(A,B).flatten()
    except np.linalg.LinAlgError:
        # Points are coplanar or singular; fallback: use max dist two points
        pts = [a,b,c,d]
        maxd = 0
        pair = (a,b)
        for i in range(4):
            for j in range(i+1,4):
                d_ = dist(pts[i], pts[j])
                if d_ > maxd:
                    maxd = d_
                    pair = (pts[i], pts[j])
        c_ = tuple((pair[0][i] + pair[1][i])/2 for i in range(3))
        r_ = dist(pair[0], c_)
        return (c_, r_)
    radius = dist(center, a)
    return (tuple(center), radius)

def welzl(P, R, n):
    if n == 0 or len(R) == 4:
        return sphere_of(R)
    p = P[n-1]
    c, r = welzl(P, R, n-1)
    if is_in_sphere(p, c, r):
        return (c,r)
    else:
        return welzl(P, R + [p], n-1)

def minimal_enclosing_sphere(points):
    P = points[:]
    random.shuffle(P)
    return welzl(P, [], len(P))


def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        if n_line == '0':
            break
        n = int(n_line)
        idx += 1
        pts = []
        for _ in range(n):
            x,y,z = map(float, input_lines[idx].split())
            idx += 1
            pts.append((x,y,z))
        c, r = minimal_enclosing_sphere(pts)
        print(f"{r:.5f}")

if __name__ == "__main__":
    main()