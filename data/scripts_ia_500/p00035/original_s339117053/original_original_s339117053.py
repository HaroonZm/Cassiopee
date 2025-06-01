import collections

Point = collections.namedtuple("Point", "x y")
Line = collections.namedtuple("Line", "first second")

def cross(line1, line2):
    def get_s(a, b, c):
        x1 = a.x - c.x
        x2 = b.x - c.x
        y1 = a.y - c.y
        y2 = b.y - c.y
        return (x1 * y2) - (x2 * y1)

    s1 = get_s(line1.first, line1.second, line2.first)
    s2 = get_s(line1.first, line1.second, line2.second)

    if not (s1 > 0) ^ (s2 > 0):
        return False

    s3 = get_s(line2.first, line2.second, line1.first)
    s4 = get_s(line2.first, line2.second, line1.second)

    if not (s3 > 0) ^ (s4 > 0):
        return False

    return True

if __name__ == '__main__':
    while 1:
        try:
            xa, ya, xb, yb, xc, yc, xd, yd = map(float, raw_input().split(','))
            A = Point(xa, ya)
            B = Point(xb, yb)
            C = Point(xc, yc)
            D = Point(xd, yd)
            points = [A, B, C, D]
            f = False
            for i in xrange(4):
                line1 = Line(points[(i + 0) % 4], points[(i + 2) % 4])
                line2 = Line(points[(i + 1) % 4], points[(i + 3) % 4])
                if not cross(line1, line2):
                    f = True

            for i in xrange(4):
                line1 = Line(points[i], points[(i + 1) % 4])
                line2 = Line(points[(i + 2) % 4], points[(i + 3) % 4])
                if cross(line1, line2):
                    f = True

            if f:
                print "NO"
            else:
                print "YES"
        except EOFError:
            break