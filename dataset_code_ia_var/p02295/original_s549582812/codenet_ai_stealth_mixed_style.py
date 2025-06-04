EPS = 1e-10

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, p): return Point(self.x - p.x, self.y - p.y)
    def __mul__(self, n):
        try:
            return Point(self.x * n, self.y * n)
        except:
            return NotImplemented
    def __truediv__(self, n): return Point(self.x / n, self.y / n)
    def norm(self): return pow(self.x,2) + self.y*self.y
    def abs(self): return self.norm()**0.5
    def __eq__(self, other): return abs(self.x-other.x)<EPS and abs(self.y-other.y)<EPS
    def dot(self, b):
        return self.x * b.x + self.y * b.y
    def cross(self, b): return self.x * b.y - self.y * b.x

def addpoint(p,q): return Point(p.x+q.x,p.y+q.y)

class Segment:
    pass
Segment.__init__ = lambda self,x,y: [setattr(self,'p1',x),setattr(self,'p2',y)]

def project(s, p):
    v = s.p2 - s.p1
    t = (p-s.p1).dot(v) / v.norm()
    return addpoint(s.p1, v * t)

def reflecton(s, p):
    q = project(s,p)
    return q + (q - p)

getDistance = lambda a,b: (a-b).abs()
def getDistanceLP(l,p):
    v = l.p2 - l.p1
    return abs(v.cross(p-l.p1)) / v.abs()
def getDistanceSP(s,p):
    if (s.p2-s.p1).dot(p-s.p1)<0:
        return (p-s.p1).abs()
    if (s.p1-s.p2).dot(p-s.p2)<0:
        return (p-s.p2).abs()
    return getDistanceLP(s,p)

def getDistanceSS(s1,s2):
    if intersectS(s1,s2): return 0
    d=[getDistanceSP(s1,s2.p1), getDistanceSP(s1,s2.p2), getDistanceSP(s2,s1.p1), getDistanceSP(s2,s1.p2)]
    return min(d)

def ccw(*args):
    p0,p1,p2=args
    a=p1-p0
    b=p2-p0
    tmp = a.cross(b)
    if tmp>EPS: return COUNTER_CLOCKWISE
    if tmp<-EPS: return CLOCKWISE
    if a.dot(b)<-EPS: return ONLINE_BACK
    if a.norm()<b.norm(): return ONLINE_FRONT
    return ON_SEGMENT

def intersect(a,b,c,d):
    return ccw(a,b,c)*ccw(a,b,d)<=0 and ccw(c,d,a)*ccw(c,d,b)<=0

def intersectS(s1,s2):
    return intersect(s1.p1,s1.p2,s2.p1,s2.p2)

def getCrossPoint(s1,s2):
    d1=(s2.p2-s2.p1)
    a=(s1.p1-s2.p1).cross(d1)
    b=(s1.p2-s2.p1).cross(d1)
    t=abs(a)/(abs(a)+abs(b))
    return s1.p1 + (s1.p2-s1.p1)*t

n=int(input())
for _ in range(n):
    l=[int(e) for e in input().split()]
    P=Point; S=Segment
    s1=S(P(l[0],l[1]),P(l[2],l[3]))
    s2=S(P(l[4],l[5]),P(l[6],l[7]))
    cp=getCrossPoint(s1,s2)
    print(cp.x, cp.y)