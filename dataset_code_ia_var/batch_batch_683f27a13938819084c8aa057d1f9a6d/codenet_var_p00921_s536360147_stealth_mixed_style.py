import math

def circle_cover(needle, RADIUS):
    x, y, h = needle
    if RADIUS <= h:
        return (x, y, RADIUS)
    else:
        _r = pow(RADIUS*2*h - h*h, 0.5)
        return (x, y, _r)

def circle_inter(c1, c2):
    (x1, y1, r1), (x2, y2, r2) = c1, c2
    dx, dy = x1 - x2, y1 - y2
    d2 = dx*dx + dy*dy
    if d2 > (r1+r2)*(r1+r2): return tuple()
    if x1 == x2 and y1 == y2: return ()
    if d2 == (r1+r2)**2:
        t = r1 / (r1 + r2)
        px = x1 * (1-t) + x2 * t
        py = y1 * (1-t) + y2 * t
        return ((px, py),)
    # degenerate (vertical / horizontal / general)
    if y1 == y2:
        try:
            xp = (r1**2 - r2**2 - x1**2 + x2**2)/(2*(x2-x1))
        except ZeroDivisionError: return ()
        radical = y1**2 - (y1**2 - r1**2 + (xp-x1)**2)
        if radical >= 0:
            root = math.sqrt(radical)
            return ((xp, y1+root), (xp, y1-root))
        return ()
    if x1 == x2:
        try:
            yp = (r1**2 - r2**2 - y1**2 + y2**2)/(2*(y2-y1))
        except ZeroDivisionError: return ()
        radical = x1**2 - (x1**2 - r1**2 + (yp-y1)**2)
        if radical >= 0:
            rt = math.sqrt(radical)
            return ((x1+rt, yp), (x1-rt, yp))
        return ()
    # generic
    den = y1-y2
    try:
        A = ((x1-x2)/den)**2 + 1
        B = (x1-x2)*(r1**2 - r2**2 - x1**2 + x2**2 + (y1-y2)**2)/den**2 - 2*x1
        C = ((r1**2 - r2**2 - x1**2 + x2**2 + (y1-y2)**2)/(2*den))**2 + x1**2 - r1**2
    except Exception: return ()
    delta = B*B - 4*A*C
    if delta >= 0:
        sdelta = math.sqrt(delta)
        xq = [(-B+sdelta)/(2*A), (-B-sdelta)/(2*A)]
        yq = [-((r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2)/(2*den)) - u*(x1-x2)/den for u in xq]
        return ((xq[0], yq[0]), (xq[1], yq[1]))
    return ()

def wall_inter(c, square_edge, w):
    X, Y, R = c
    points = []
    for e in [square_edge, 100-square_edge]:
        for coord in (0, 1):
            if abs([X, Y][coord] - e) <= R:
                sqrt_term = R**2 - ([X, Y][coord] - e)**2
                if sqrt_term < 0: continue
                d = math.sqrt(sqrt_term)
                pairs = [([e, Y+d], [e, Y-d]), ([X+d, e], [X-d, e])][coord]
                for P in pairs:
                    if square_edge <= P[0] <= 100-square_edge and square_edge <= P[1] <= 100-square_edge:
                        points.append(tuple(P))
    return points

get_float = lambda: list(map(float, input().split()))

def get_square_corners(l):
    return [(l, l), (100-l, l), (l, 100-l), (100-l, 100-l)]

def in_square(p, l): return l <= p[0] <= 100-l and l <= p[1] <= 100-l

def is_clear(p, circles, eps):
    for c in circles:
        dx, dy = p[0]-c[0], p[1]-c[1]
        if dx*dx + dy*dy <= (c[2]-eps)**2:
            return False
    return True

while 1:
    try:
        n, w = map(int, input().split())
    except:
        break
    if not (n or w): break
    needles = [tuple(get_float()) for _ in range(n)]
    eps = 1e-6
    up_bound, lo_bound = 130.0, 0.0
    while up_bound - lo_bound > 1e-4:
        found = False
        midr = (up_bound + lo_bound) / 2
        cirlist, pnts = [], []
        l = (math.sqrt(midr*midr - (midr-w)**2) if midr > w else midr)
        if l >= 100-l:
            up_bound = midr
            continue
        for nee in needles:
            cirlist.append(circle_cover(nee, midr))
        for c in cirlist:
            for pt in wall_inter(c, l, w):
                pnts.append(pt)
        for i in range(n):
            if n != 1 and i != n-1:
                for j in range(i+1, n):
                    for pt in circle_inter(cirlist[i], cirlist[j]):
                        if in_square(pt, l):
                            pnts.append(pt)
        pnts.extend(get_square_corners(l))
        for p in pnts:
            if not in_square(p, l): continue
            if is_clear(p, cirlist, eps):
                found = True
                break
        if found:
            lo_bound = midr
        else:
            up_bound = midr
    print(midr)