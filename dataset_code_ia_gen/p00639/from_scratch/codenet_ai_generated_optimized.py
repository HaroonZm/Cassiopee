import sys
import math

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def mul(a,s):
    return (a[0]*s, a[1]*s)

def norm(a):
    return math.hypot(a[0], a[1])

def reflect(v, n):
    # v reflected on normal n (normalized)
    d = dot(v, n)
    return sub(v, mul(n, 2*d))

def solve(D, px, py, vx, vy):
    P = (px, py)
    V = (vx, vy)
    R = 1.0
    EPS = 1e-14

    if norm(V) < 1e-12:
        # no velocity, no hits
        return None

    dist_total = 0.0
    while dist_total + EPS < D:
        # if projectile crosses origin => hits lab
        # try to find t > 0 such that P + V*t = (0,0)
        # => t = -P/V componentwise (must be same for x and y)
        # check if origin is on path segment before next reflection
        # first find intersection with circle x^2+y^2=R^2
        # line: X = P + V*t
        # solve (P_x + V_x t)^2 + (P_y + V_y t)^2 = R^2
        a = V[0]*V[0]+V[1]*V[1]
        b = 2*(P[0]*V[0]+P[1]*V[1])
        c = P[0]*P[0]+P[1]*P[1]-R*R
        disc = b*b - 4*a*c
        if disc < -EPS:
            # no intersection circle ahead, so path is line segment "as is"
            # check if hits origin on line segment
            if P == (0,0):
                return dist_total
            t0 = float('inf')
        else:
            disc = max(0.0, disc)
            t1 = (-b - math.sqrt(disc))/(2*a)
            t2 = (-b + math.sqrt(disc))/(2*a)
            # find smallest positive t for circle intersection > EPS
            ts = [t for t in [t1,t2] if t > EPS]
            if ts:
                t_circle = min(ts)
            else:
                t_circle = float('inf')

        # check if hits origin before t_circle
        # solve for t: P+tV = 0 => t_x = -P_x/V_x if V_x!=0 else None
        # same for y. If both exist and equal within EPS, and t>0 and t<t_circle:
        # hits origin
        tx = -P[0]/V[0] if abs(V[0])>EPS else None
        ty = -P[1]/V[1] if abs(V[1])>EPS else None
        if tx is not None and ty is not None:
            if abs(tx - ty) < 1e-13 and tx > EPS and tx < t_circle+EPS:
                dist_hit = dist_total + norm(mul(V, tx))
                if dist_hit <= D+EPS:
                    return dist_hit
        elif tx is not None and abs(P[1]) < EPS:
            # y is 0, check if passes origin at tx
            if tx > EPS and tx < t_circle+EPS:
                dist_hit = dist_total + norm(mul(V, tx))
                if dist_hit <= D+EPS:
                    return dist_hit
        elif ty is not None and abs(P[0]) < EPS:
            if ty > EPS and ty < t_circle+EPS:
                dist_hit = dist_total + norm(mul(V, ty))
                if dist_hit <= D+EPS:
                    return dist_hit
        elif P == (0,0):
            return dist_total

        # now move to next reflection point or until D reached
        dist_to_circle = norm(mul(V, t_circle)) if t_circle != float('inf') else float('inf')

        if dist_total + dist_to_circle > D:
            # travel max remaining distance and no hit origin, impossible
            break

        # update position and velocity at reflection
        P = add(P, mul(V, t_circle))
        dist_total += dist_to_circle

        n = (P[0]/R, P[1]/R)  # normal vector at reflection point (normalized)
        V = reflect(V, n)

    return None


for line in sys.stdin:
    D = float(line.strip())
    if D == 0.0:
        break
    px, py, vx, vy = map(float, sys.stdin.readline().strip().split())
    res = solve(D, px, py, vx, vy)
    if res is None:
        print("impossible")
    else:
        print("%.8f" % res)