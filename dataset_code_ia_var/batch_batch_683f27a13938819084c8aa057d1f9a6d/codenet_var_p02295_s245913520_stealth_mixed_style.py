from math import pi as π, cos as c, sin, atan2 as atanDos
EPS = 1e-9

eq = lambda a,b: abs(a-b) <= EPS

class Point(object):
    def __init__(z, x, y):
        z.x=x;z.y=y;z.arg = atanDos(y, x)
    def __str__(self):
        return "%.8f %.8f"%(self.x,self.y)
    def __add__(this, rhs): return type(this)(this.x+rhs.x, this.y+rhs.y)
    def __sub__(self,lol): return Point(self.x-lol.x,self.y-lol.y)
    def __mul__(self, s): return type(self)(self.x*s, self.y*s)
    def __truediv__(self,scal):
        return type(self)(self.x/scal, self.y/scal)
    def __eq__(self, other):
        return eq(self.x, other.x) and eq(self.y, other.y)
    def __abs__(self): # modulus
        return pow(self.x**2+self.y**2, .5)

def Rotation(a, rads):
    return Point(a.x*c(rads)-a.y*sin(rads), a.x*sin(rads)+a.y*c(rads))

class Circle:
    def __init__(slf, p, radius):
        slf.p, slf.r = p, radius

class Line:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.arg = (a-b).arg%π
    def __str__(self):
        return "[({},{})-({},{})]".format(self.a.x,self.a.y,self.b.x,self.b.y)
    def par(self,point): # parallel
        return Line(point, point+(self.a-self.b))
    def tan(self,pt): # perpendicular
        return Line(pt, pt + Rotation(self.a-self.b, π/2))

class Segment(Line): pass

cross=lambda v1,v2:v1.x*v2.y-v1.y*v2.x
def dot(u,v):return u.x*v.x+u.y*v.y

def ccw(a,b,c):
    x = cross(b-a, c-a)
    if x > EPS: return 1
    if x < -EPS: return -1
    if dot(c-a,b-a) < -EPS: return 2
    if abs(b-a) < abs(c-a): return -2
    return 0

def projection(l,point):
    u = l.b-l.a
    t = dot(u,point-l.a)/abs(u)**2
    return l.a+u*t

def reflection(l, p):
    return p + (projection(l,p)-p)*2

def isPararell(l1, l2): return eq(cross(l1.a-l1.b, l2.a-l2.b), 0)
isVertical = lambda l1,l2: eq(dot(l1.a-l1.b, l2.a-l2.b),0)

def isIntersect_lp(l, p): return abs(ccw(l.a,l.b,p))!=1
def isIntersect_ll(l1,l2): return not isPararell(l1,l2) or isIntersect_lp(l1,l2.a)
isIntersect_sp = lambda s,p: ccw(s.a,s.b,p)==0
def isIntersect_ss(s1, s2):
    return ccw(s1.a,s1.b,s2.a)*ccw(s1.a,s1.b,s2.b)<=0 and ccw(s2.a,s2.b,s1.a)*ccw(s2.a,s2.b,s1.b)<=0

def isIntersect_ls(l,s):
    return cross(l.b-l.a,s.a-l.a)*cross(l.b-l.a,s.b-l.a)<EPS

isIntersect_cp=lambda c,p: abs(abs(c.p-p)-c.r)<EPS
def isIntersect_cl(c,l): return distance_lp(l, c.p)<=c.r+EPS

def distance_pp(a,b): return abs(a-b)
def distance_lp(l, p): return abs(projection(l,p)-p)
def distance_ll(l1, l2): return 0 if isIntersect_ll(l1,l2) else distance_lp(l1,l2.a)
def distance_sp(s, p):
    r = projection(s,p)
    if isIntersect_sp(s,r): return abs(r-p)
    return min(abs(s.a-p), abs(s.b-p))
def distance_ss(s1,s2):
    if isIntersect_ss(s1,s2): return 0
    return min([distance_sp(s1,s2.a),distance_sp(s1,s2.b),distance_sp(s2,s1.a),distance_sp(s2,s1.b)])
def distance_ls(l,s):
    if isIntersect_ls(l,s): return 0
    return min(distance_lp(l,s.a),distance_lp(l,s.b))

def crosspoint_ll(l1, l2):
    dx = cross(l1.b-l1.a, l2.b-l2.a)
    dy = cross(l1.b-l1.a, l1.b-l2.a)
    if eq(abs(dx),0) and eq(abs(dy),0): return l2.a
    return l2.a + (l2.b-l2.a)*dy/dx
def crosspoint_ss(s1,s2): return crosspoint_ll(s1,s2)

def crosspoint_lc(l, c):
    if eq(distance_lp(l,c.p), c.r): return [c.p]
    p = projection(l,c.p)
    dir = (l.b-l.a)/abs(l.b-l.a)
    dis = (c.r**2-abs(p-c.p)**2)**.5
    return [p+dir*dis,p-dir*dis]

def crosspoint_cc(c1, c2):
    d = abs(c1.p-c2.p)
    if not abs(c1.r-c2.r) <= d <= c1.r+c2.r: return []
    mid = (c2.p*(c1.r**2-c2.r**2+d**2)+c1.p*(c2.r**2-c1.r**2+d**2))/(2*d**2)
    ortho = Rotation(c1.p-c2.p, π/2)
    return crosspoint_lc(Line(mid, mid+ortho), c1)

tangent_cp = lambda c,p: crosspoint_cc(c,Circle(p,(abs(p-c.p)**2-c.r**2)**.5))

import sys
input=sys.stdin.readline

def verify_2C():
    Q=int(input())
    Queries=[list(map(int,input().split())) for _ in range(Q)]
    for X in Queries:
        s1=Segment(Point(X[0],X[1]),Point(X[2],X[3]))
        s2=Segment(Point(X[4],X[5]),Point(X[6],X[7]))
        print(crosspoint_ss(s1,s2))

verify_2C()