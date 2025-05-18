# Your code here!

EPS = 0.0000000001

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0
                                                                      
class Point:
    
    global EPS
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
        
    def __add__(a, b):
        s = a.x + b.x
        t = a.y + b.y
        return Point(s, t)
        
    def __sub__(a, b):
        s = a.x - b.x
        t = a.y - b.y
        return Point(s, t)
            
    def __mul__(self, a):
        s = a * self.x
        t = a * self.y
        return Point(s, t)
        
    def __truediv__(self, a):
        s = self.x / a
        t = self.y / a
        return Point(s, t)
            
            
            
            
    def norm(self):
        return self.x * self.x + self.y * self.y
        
    def abs(self):
        return self.norm() ** 0.5
            
    
            
            
    def __eq__(self, other):
        return abs(self.x - other.y) < self.EPS and abs(self.y - other.y) < self.EPS
            
            
            
    def dot(self, b):
        return self.x * b.x + self.y * b.y
        
    def cross(self, b):
        return self.x * b.y - self.y * b.x
    
    
class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def project(s, p):
    base = s.p2 - s.p1
    hypo = p - s.p1
    r = hypo.dot(base) / base.norm()
    return s.p1 + base * r

def reflecton(s, p):
    return p + (project(s,p) - p) * 2

def getDistance(a, b):
    return (a-b).abs()

def getDistanceLP(l, p):
    return abs((l.p2-l.p1).cross(p-l.p1)) / ((l.p2-l.p1).abs())

def getDistanceSP(s, p):
    if (s.p2 - s.p1).dot(p-s.p1) < 0:
        return (p-s.p1).abs()
    elif (s.p1 - s.p2).dot(p-s.p2) < 0:
        return (p-s.p2).abs()
    return getDistanceLP(s,p)

def getDistanceSS(s1, s2):
    if intersectS(s1, s2):
        return 0
    return min(getDistanceSP(s1, s2.p1), getDistanceSP(s1, s2.p2), getDistanceSP(s2, s1.p1), getDistanceSP(s2, s1.p2))

def ccw(p0, p1, p2):
    a = p1-p0
    b = p2-p0
    
    if a.cross(b) > 0:
        return COUNTER_CLOCKWISE
    elif a.cross(b) <0:
        return CLOCKWISE
    elif a.dot(b) < 0:
        return ONLINE_BACK
    elif a.abs() < b.abs():
        return ONLINE_FRONT
    else:
        return ON_SEGMENT

def intersect(p1, p2, p3, p4):
    return ccw(p1, p2, p3) *ccw(p1, p2, p4) <=0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0

def intersectS(s1, s2):
    return intersect(s1.p1, s1.p2, s2.p1, s2.p2)

def getCrossPoint(s1, s2):
    base = s2.p2-s2.p1
    a = s1.p1-s2.p1
    b = s1.p2-s2.p1
    
    d1 = abs(a.cross(base))
    d2 = abs(b.cross(base))
    
    t = d1 / (d1+d2)
    return s1.p1 + (s1.p2-s1.p1) * t

n = int(input())
for i in range(n):
    
    nums=list(map(int,input().split()))
    s1 = Segment(Point(nums[0], nums[1]), Point(nums[2], nums[3]))
    s2 = Segment(Point(nums[4], nums[5]), Point(nums[6], nums[7]))
    print(getCrossPoint(s1, s2).x, getCrossPoint(s1, s2).y)