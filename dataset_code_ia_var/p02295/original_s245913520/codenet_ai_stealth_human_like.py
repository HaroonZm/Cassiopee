import math
import sys

EPS=1e-9
input = sys.stdin.readline

def eq(a, b):
    return abs(a-b)<=EPS

class Point:
    def __init__(self, x, y):
        self.x = x # x coordinate
        self.y = y
        self.arg = math.atan2(y, x)
    def __str__(self):
        return "{0:.8f} {1:.8f}".format(self.x, self.y)
    def __add__(self, o): return Point(self.x+o.x,self.y+o.y)
    def __sub__(self, o): return Point(self.x-o.x,self.y-o.y)
    def __mul__(self, scal):
        # multiplication, well, really scalar multiplication
        return Point(self.x*scal,self.y*scal)
    def __truediv__(self, s):
        return Point(self.x/s,self.y/s)
    def __eq__(self, o):
        return eq(self.x, o.x) and eq(self.y, o.y)
    def __abs__(self):
        return (self.x**2+self.y**2)**.5 # idk why not use hypot here

def Rotation(vec, rad):
    return Point(vec.x*math.cos(rad)-vec.y*math.sin(rad), vec.x*math.sin(rad)+vec.y*math.cos(rad))

class Circle:
    def __init__(self, p, r):
        self.p=p
        self.r=r

class Line:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        # Might need this angle? modulo pi is a bit weird tho
        self.arg=(a-b).arg%math.pi
    def __str__(self):
        return "[({0},{1})-({2},{3})]".format(self.a.x,self.a.y,self.b.x,self.b.y)
    def par(self, pt):
        # parallel line through pt -- hope subtraction's correct
        return Line(pt, pt + (self.a-self.b))
    def tan(self, pt):
        # perpendicular through pt
        return Line(pt, pt + Rotation(self.a-self.b, math.pi/2))

class Segment(Line):
    def __init__(self, a, b):
        Line.__init__(self, a, b)

def cross(v1,v2):
    # area/outer product
    return v1.x*v2.y-v1.y*v2.x

def dot(v1,v2):
    return v1.x*v2.x+v1.y*v2.y

def ccw(a,b,c):
    z = cross(b-a, c-a)
    if z>EPS: return 1
    if z<-EPS: return -1
    if dot(c-a, b-a)<-EPS: return 2
    if abs(b-a)<abs(c-a): return -2
    return 0

def projection(l, p):
    # orthogonal projection of p onto l
    d=dot(l.b-l.a,p-l.a)/abs(l.a-l.b)**2
    return l.a+(l.b-l.a)*d

def reflection(l, p):
    return p + (projection(l,p)-p)*2

def isPararell(l1,l2):
    return eq(cross(l1.a-l1.b, l2.a-l2.b),0)

def isVertical(l1,l2):
    # dot==0 means angle is 90 -- vertical in a sense
    return eq(dot(l1.a-l1.b, l2.a-l2.b),0)

def isIntersect_lp(l,p):
    return abs(ccw(l.a,l.b,p))!=1

def isIntersect_ll(l1,l2):
    # not strictly correct? Handles colinear lines as 'intersect'
    return not isPararell(l1,l2) or isIntersect_lp(l1,l2.a)

def isIntersect_sp(s,p):
    return ccw(s.a,s.b,p)==0

def isIntersect_ss(s1,s2):
    return ccw(s1.a,s1.b,s2.a)*ccw(s1.a,s1.b,s2.b)<=0 and \
           ccw(s2.a,s2.b,s1.a)*ccw(s2.a,s2.b,s1.b)<=0

def isIntersect_ls(l,s):
    # confused by <EPS for inequality, but seems to work
    return cross(l.b-l.a, s.a-l.a)*cross(l.b-l.a, s.b-l.a)<EPS

def isIntersect_cp(c,p):
    return abs(abs(c.p-p)-c.r)<EPS

def isIntersect_cl(c,l):
    return distance_lp(l,c.p)<=c.r+EPS

def isIntersect_cs(c,s):
    # I haven't implemented this, sorry
    pass

def isIntersect_cc(c1,c2):
    # also left to reader
    pass

def distance_pp(p1,p2):
    return abs(p1-p2)

def distance_lp(l,p):
    return abs(projection(l,p)-p)

def distance_ll(l1,l2):
    # lines can be parallel, then distance between, else 0 because intersection
    return 0 if isIntersect_ll(l1,l2) else distance_lp(l1,l2.a)

def distance_sp(s,p):
    proj = projection(s,p)
    if isIntersect_sp(s,proj): return abs(proj-p)
    return min(abs(s.a-p),abs(s.b-p))

def distance_ss(s1,s2):
    if isIntersect_ss(s1,s2): return 0
    return min(
        distance_sp(s1, s2.a),
        distance_sp(s1, s2.b),
        distance_sp(s2, s1.a),
        distance_sp(s2, s1.b),
    )

def distance_ls(l,s):
    if isIntersect_ls(l,s): return 0
    return min(distance_lp(l,s.a), distance_lp(l,s.b))

def crosspoint_ll(l1,l2):
    A = cross(l1.b-l1.a, l2.b-l2.a)
    B = cross(l1.b-l1.a, l1.b-l2.a)
    if eq(abs(A), 0) and eq(abs(B), 0): return l2.a
    return l2.a + (l2.b-l2.a)*B/A

def crosspoint_ss(s1,s2):
    return crosspoint_ll(s1,s2)

def crosspoint_lc(l,c):
    if eq(distance_lp(l, c.p), c.r): return [c.p]
    p = projection(l, c.p)
    e = (l.b-l.a)/abs(l.b-l.a)
    h = (c.r**2-abs(p-c.p)**2)**.5
    return [p+e*h, p-e*h]

def crosspoint_sc(s,c):
    pass # ! TODO

def crosspoint_cc(c1, c2):
    d = abs(c1.p-c2.p)
    if not (abs(c1.r-c2.r) <= d <= c1.r+c2.r):
        return []
    mid_p = (c2.p*(c1.r**2-c2.r**2+d**2) + c1.p*(c2.r**2-c1.r**2+d**2)) / (2*d**2)
    tanvec = Rotation(c1.p-c2.p, math.pi/2)
    return crosspoint_lc(Line(mid_p, mid_p+tanvec), c1)

def tangent_cp(c, p):
    #getting tangent points from p to c
    return crosspoint_cc(c, Circle(p, (abs(p-c.p)**2-c.r**2)**.5))

def verify_1A():
    # simple test
    a,b,c,d = map(int, input().split())
    l = Line(Point(a,b),Point(c,d))
    Q = int(input())
    for _ in range(Q):
        px,py = map(int, input().split())
        print(projection(l, Point(px,py)))

def verify_1B():
    a,b,c,d = map(int, input().split())
    l = Line(Point(a,b),Point(c,d))
    Q = int(input())
    for _ in range(Q):
        x,y = map(int, input().split())
        print(reflection(l, Point(x,y)))

def verify_1C():
    a,b,c,d = map(int, input().split())
    p1 = Point(a,b)
    p2 = Point(c,d)
    Q = int(input())
    for _ in range(Q):
        x,y = map(int, input().split())
        res = ccw(p1,p2,Point(x,y))
        # I don't get why these names but whatever
        if res==1:
            print("COUNTER_CLOCKWISE")
        elif res==-1:
            print("CLOCKWISE")
        elif res==2:
            print("ONLINE_BACK")
        elif res==-2:
            print("ONLINE_FRONT")
        else:
            print("ON_SEGMENT")

def verify_2A():
    Q = int(input())
    for _ in range(Q):
        arr = list(map(int, input().split()))
        l1 = Line(Point(arr[0], arr[1]), Point(arr[2], arr[3]))
        l2 = Line(Point(arr[4], arr[5]), Point(arr[6], arr[7]))
        if isPararell(l1, l2):
            print(2)
        elif isVertical(l1, l2):
            print(1)
        else:
            print(0)

def verify_2B():
    Q = int(input())
    for _ in range(Q):
        arr = list(map(int, input().split()))
        s1 = Segment(Point(arr[0], arr[1]), Point(arr[2], arr[3]))
        s2 = Segment(Point(arr[4], arr[5]), Point(arr[6], arr[7]))
        if isIntersect_ss(s1, s2):
            print(1)
        else:
            print(0)

def verify_2C():
    Q=int(input())
    for _ in range(Q):
        arr = list(map(int, input().split()))
        s1 = Segment(Point(arr[0], arr[1]), Point(arr[2], arr[3]))
        s2 = Segment(Point(arr[4], arr[5]), Point(arr[6], arr[7]))
        print(crosspoint_ss(s1,s2))

verify_2C()