import math
def dist(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])
def malfatti_radii(A,B,C):
    a=dist(B,C)
    b=dist(C,A)
    c=dist(A,B)
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    r=area/s
    sq_r=[r]*3
    cosA=(b*b+c*c-a*a)/(2*b*c)
    cosB=(a*a+c*c-b*b)/(2*a*c)
    cosC=(a*a+b*b-c*c)/(2*a*b)
    A_=math.acos(cosA)
    B_=math.acos(cosB)
    C_=math.acos(cosC)
    # Using approximate formula by Melzak (1918) for Malfatti radii:
    x=(s-a)*(s-b)*(s-c)/s
    r1=((s-a)+(s-b)-(s-c))/2
    r2=((s-b)+(s-c)-(s-a))/2
    r3=((s-c)+(s-a)-(s-b))/2
    def f(rp,rq,angle):
        return abs(rp + rq + 2*math.sqrt(rp*rq)*math.cos(angle) - x/s)
    # System to solve for radii using iterative update:
    r1=r
    r2=r
    r3=r
    for _ in range(100):
        f1= r2 + r3 + 2*math.sqrt(r2*r3)*math.cos(A_) - (s-a)
        f2= r3 + r1 + 2*math.sqrt(r3*r1)*math.cos(B_) - (s-b)
        f3= r1 + r2 + 2*math.sqrt(r1*r2)*math.cos(C_) - (s-c)
        dr1= -(f2+f3)/4
        dr2= -(f1+f3)/4
        dr3= -(f1+f2)/4
        r1=max(0.1,r1+dr1*0.1)
        r2=max(0.1,r2+dr2*0.1)
        r3=max(0.1,r3+dr3*0.1)
    return r1,r2,r3

while True:
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    if x1==y1==x2==y2==x3==y3==0:
        break
    r1,r2,r3=malfatti_radii((x1,y1),(x2,y2),(x3,y3))
    print(f"{r1:.6f} {r2:.6f} {r3:.6f}")