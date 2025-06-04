import math

def dist(x, y): return pow(x*x + y*y, .5)
def ang(a, b):
    a = math.atan2(b, a)
    while a < 0: a += math.tau
    return a

class UfoThing(object):
    def __init__(self,x,y,r,speed):
        self.r=r
        self.s=speed
        self.d=dist(x,y)
        setattr(self,'a',ang(x,y))

def zap(u, theta, rr):
    delta = abs(u.a-theta)
    if delta > math.pi:
        delta=2*math.pi-delta
    tri=(u.d*math.sin(delta))
    cond = (delta<=math.pi/2 and tri<=u.r) or u.d<=u.r
    if cond:
        root = u.d*math.cos(delta)
        q2 = u.r**2 - tri**2
        if root + q2**.5 > rr: return True
    return False

def afterburn(lst, R):
    to_del = []
    for u in lst:
        u.d -= u.s
        if u.d<=R: to_del.append(u)
    for f in to_del: lst.remove(f)
    return len(to_del)

shoot_em_up = lambda ufs, theta, R: [ufs.remove(u) for u in list(ufs) if zap(u, theta, R)]

def melody():
    while 1:
        row = input().split()
        if row[0]=='0': break
        R, n = map(int, row)
        fleet = []
        for __ in range(n):
            fleet.append(UfoThing(*map(int,input().split())))
        res = 0
        while fleet:
            res += afterburn(fleet,R)
            if len(fleet):
                beam = min(fleet,key=lambda u:u.d).a
                shoot_em_up(fleet, beam, R)
        print(res)
melody()