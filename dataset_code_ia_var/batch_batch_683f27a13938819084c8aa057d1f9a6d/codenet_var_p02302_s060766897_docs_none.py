n = input()
ps = [map(int, raw_input().split()) for i in xrange(n)]
def intersection(p1, p2, q1, q2):
    dx0 = p2[0] - p1[0]
    dy0 = p2[1] - p1[1]
    dx1 = q2[0] - q1[0]
    dy1 = q2[1] - q1[1]
    a = dy0*dx1
    b = dy1*dx0
    c = dx0*dx1
    d = dy0*dy1
    if a == b:
        return None
    x = (a*p1[0] - b*q1[0] + c*(q1[1] - p1[1])) / float(a - b)
    y = (b*p1[1] - a*q1[1] + d*(q1[0] - p1[0])) / float(b - a)
    return x, y
def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
def calc_area(ps):
    return abs(sum(ps[i][0]*ps[i-1][1] - ps[i][1]*ps[i-1][0] for i in xrange(len(ps)))) / 2.
for t in xrange(input()):
    vs = []
    x1, y1, x2, y2 = map(int, raw_input().split())
    p1 = (x1, y1)
    p2 = (x2, y2)
    for i in xrange(n):
        q1 = ps[i-1]
        q2 = ps[i]
        if cross(p1, p2, q1) * cross(p1, p2, q2) <= 0:
            r = intersection(p1, p2, q1, q2)
            if r is not None:
                vs.append(r)
        if cross(p1, p2, q2) >= 0:
            vs.append(q2)
    print "%.09f" % calc_area(vs)