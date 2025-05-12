def cross(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def dot(c1, c2):
    return c1.real * c2.real + c1.imag * c2.imag

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    cross_ab = cross(a, b)
    if cross_ab > 0:
        return 1
    elif cross_ab < 0:
        return -1
    elif dot(a, b) < 0:
        return 1
    elif abs(a) < abs(b):
        return -1
    else:
        return 0

def intersect(p1, p2, p3, p4):
    # p1 and p2 are end points of a segment.
    # p3 and p4 are end points of the other segment.
    if (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0) and \
       (ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0):
        return True
    else:
        return False

def get_distance_sp(sp1, sp2, p):
    a = sp2 - sp1
    b = p - sp1
    if dot(a, b) < 0:
        return abs(b)
    c = sp1 - sp2
    d = p - sp2
    if dot(c, d) < 0:
        return abs(d)
    return abs(cross(a, b) / a)

def solve():
    from sys import stdin
    lines = stdin.readlines()
    
    while True:
        N = int(lines[0])
        if N == 0:
            break
        sx, sy, ex, ey = map(int, lines[1].split())
        sp = sx + sy * 1j
        ep = ex + ey * 1j
        R = []
        for l in lines[2:2+N]:
            D = []
            x1, y1, x2, y2, h = map(int, l.split())
            bp1 = x1 + y1 * 1j
            bp2 = x2 + y1 * 1j
            bp3 = x2 + y2 * 1j
            bp4 = x1 + y2 * 1j
            if intersect(sp, ep, bp1, bp2) or intersect(sp, ep, bp2, bp3) or \
            intersect(sp, ep, bp3, bp4) or intersect(sp, ep, bp4, bp1) or \
            (x1 <= sx <= x2 and y1 <= sy <= y2) or \
            (x1 <= ex <= x2 and y1 <= ey <= y2):
                print(0)
                break
            else:
                D.append(get_distance_sp(sp, ep, bp1))
                D.append(get_distance_sp(sp, ep, bp2))
                D.append(get_distance_sp(sp, ep, bp3))
                D.append(get_distance_sp(sp, ep, bp4))
                D.append(get_distance_sp(bp1, bp2, sp))
                D.append(get_distance_sp(bp1, bp2, ep))
                D.append(get_distance_sp(bp2, bp3, sp))
                D.append(get_distance_sp(bp2, bp3, ep))
                D.append(get_distance_sp(bp3, bp4, sp))
                D.append(get_distance_sp(bp3, bp4, ep))
                D.append(get_distance_sp(bp4, bp1, sp))
                D.append(get_distance_sp(bp4, bp1, ep))
                
                d = min(D)
                if h < d:
                    R.append((d ** 2 + h ** 2) / (2 * h))
                else:
                    R.append(d)
        else:
            print(min(R))
        lines = lines[2+N:]

solve()