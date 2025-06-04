def dot(c1, c2):
    return c1.real * c2.real + c1.imag * c2.imag

def cross(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def on_segment(p, a, b):
    v1 = a - p
    v2 = b - p
    return cross(v1, v2) == 0 and dot(v1, v2) < 0

def ccw(p0, p1, p2):
    return cross(p1 - p0, p2 - p0) > 0

def intersect(p1, p2, p3, p4):
    crs1 = cross(p2 - p1, p3 - p1)
    crs2 = cross(p2 - p1, p4 - p1)
    if crs1 == 0 and crs2 == 0:
        return dot(p1 - p3, p2 - p3) < 0 or dot(p1 - p4, p2 - p4) < 0
    crs3 = cross(p4 - p3, p1 - p3)
    crs4 = cross(p4 - p3, p2 - p3)
    return crs1 * crs2 <= 0 and crs3 * crs4 <= 0

def andrew(point_list):
    u = []
    l = []
    u.append(point_list[0])
    u.append(point_list[1])
    l.append(point_list[-1])
    l.append(point_list[-2])
    for p in point_list[2:]:
        while ccw(u[-2], u[-1], p):
            u.pop()
            if len(u) == 1:
                break
        u.append(p)
    for p in point_list[-3::-1]:
        while ccw(l[-2], l[-1], p):
            l.pop()
            if len(l) == 1:
                break
        l.append(p)
    u.pop()
    l.pop()
    return u + l

def contains(polygon, point):
    for p1, p2 in zip(polygon, polygon[1:] + polygon[:1]):
        a = p1 - point
        b = p2 - point
        cross_ab = cross(a, b)
        if cross_ab > 0:
            return False
        elif cross_ab == 0 and dot(a, b) > 0:
            return False
    return True

def string_to_complex(s):
    x, y = map(int, s.split())
    return x + y * 1j

def solve():
    from sys import stdin
    file_input = stdin
    lines = file_input.readlines()
    while True:
        n, m = map(int, lines[0].split())
        if n == 0 and m == 0:
            break
        if n == 1 and m == 1:
            print('YES')
            lines = lines[1+n+m:]
            continue
        pts1 = list(map(string_to_complex, lines[1:1+n]))
        pts2 = list(map(string_to_complex, lines[1+n:1+n+m]))
        if n == 1 and m == 2:
            if on_segment(pts1[0], pts2[0], pts2[1]):
                print('NO')
            else:
                print('YES')
        elif n == 2 and m == 1:
            if on_segment(pts2[0], pts1[0], pts1[1]):
                print('NO')
            else:
                print('YES')
        elif n == 2 and m == 2:
            if intersect(pts1[0], pts1[1], pts2[0], pts2[1]):
                print('NO')
            else:
                print('YES')
        elif n == 1:
            p = pts1[0]
            cvx = andrew(sorted(pts2, key=lambda c: (c.real, c.imag)))
            if contains(cvx, p):
                print('NO')
            else:
                print('YES')
        elif m == 1:
            p = pts2[0]
            cvx = andrew(sorted(pts1, key=lambda c: (c.real, c.imag)))
            if contains(cvx, p):
                print('NO')
            else:
                print('YES')
        elif n == 2:
            p1, p2 = pts1
            cvx = andrew(sorted(pts2, key=lambda c: (c.real, c.imag)))
            if contains(cvx, p1) or contains(cvx, p2):
                print('NO')
            else:
                for q1, q2 in zip(cvx, cvx[1:] + cvx[:1]):
                    if intersect(p1, p2, q1, q2):
                        print('NO')
                        break
                else:
                    print('YES')
        elif m == 2:
            p1, p2 = pts2
            cvx = andrew(sorted(pts1, key=lambda c: (c.real, c.imag)))
            if contains(cvx, p1) or contains(cvx, p2):
                print('NO')
            else:
                for q1, q2 in zip(cvx, cvx[1:] + cvx[:1]):
                    if intersect(p1, p2, q1, q2):
                        print('NO')
                        break
                else:
                    print('YES')
        else:
            cvx1 = andrew(sorted(pts1, key=lambda c: (c.real, c.imag)))
            cvx2 = andrew(sorted(pts2, key=lambda c: (c.real, c.imag)))
            for p in cvx2:
                if contains(cvx1, p):
                    print('NO')
                    break
            else:
                for p in cvx1:
                    if contains(cvx2, p):
                        print('NO')
                        break
                else:
                    for r1, r2 in zip(cvx1, cvx1[1:] + cvx1[:1]):
                        for s1, s2 in zip(cvx2, cvx2[1:] + cvx2[:1]):
                            if intersect(r1, r2, s1, s2):
                                print('NO')
                                break
                        else:
                            continue
                        break
                    else:
                        print('YES')
        lines = lines[1+n+m:]

solve()