import sys
import math

input=sys.stdin.readline
EPS=1e-9

def intersect(a,b,c,d):
    # check if segments a-b and c-d intersect, return intersection point if yes, else None
    def ccw(p1,p2,p3):
        return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
    if max(a[0],b[0])+EPS < min(c[0],d[0]) or max(c[0],d[0])+EPS < min(a[0],b[0]):
        return None
    if max(a[1],b[1])+EPS < min(c[1],d[1]) or max(c[1],d[1])+EPS < min(a[1],b[1]):
        return None
    d1=ccw(a,b,c)*ccw(a,b,d)
    d2=ccw(c,d,a)*ccw(c,d,b)
    if d1>-EPS and d2>-EPS:
        # check collinear overlapping
        # problem states no overlap so skip
        return None
    if d1<=EPS and d2<=EPS:
        # compute intersection point
        dx1=b[0]-a[0]
        dy1=b[1]-a[1]
        dx2=d[0]-c[0]
        dy2=d[1]-c[1]
        denom=dx1*dy2-dy1*dx2
        if abs(denom)<EPS:
            return None
        t=((c[0]-a[0])*dy2-(c[1]-a[1])*dx2)/denom
        x=a[0]+t*dx1
        y=a[1]+t*dy1
        if (min(a[0],b[0])-EPS<=x<=max(a[0],b[0])+EPS and min(a[1],b[1])-EPS<=y<=max(a[1],b[1])+EPS
           and min(c[0],d[0])-EPS<=x<=max(c[0],d[0])+EPS and min(c[1],d[1])-EPS<=y<=max(c[1],d[1])+EPS):
            return (x,y)
    return None

def dist(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])

T=int(input())
for _ in range(T):
    xa,ya=map(float,input().split())
    xb,yb=map(float,input().split())
    n=int(input())
    lines=[]
    for __ in range(n):
        xs,ys,xt,yt,o,l= input().split()
        xs=float(xs)
        ys=float(ys)
        xt=float(xt)
        yt=float(yt)
        o=int(o)
        l=int(l)
        lines.append(((xs,ys),(xt,yt),o,l))
    # find intersections between new line AB and existing lines
    inters=[]
    A=(xa,ya)
    B=(xb,yb)
    for (p1,p2,o,l) in lines:
        ip=intersect(A,B,p1,p2)
        if ip is not None:
            # calculate distance along new line from A
            d=dist(A,ip)
            inters.append((d,o,l))
    # consider endpoints A and B
    inters.append((0,-1,-1)) # endpoint dummy, owner/type irrelevant
    inters.append((dist(A,B),-1,-1))
    # sort intersections by position along new line
    inters.sort(key=lambda x:x[0])
    # determine structure segment states
    # initialize: can start either High(1) or Low(0), minimal number of entrances
    # States: for each segment, 2 possibilities (High or Low)
    # Transitions:
    # At each intersection (except endpoints), if intersect with existing line:
    # - if own company (o=1), new line must have same elevation as existing line's l
    # - if other company (o=0), new line must have opposite elevation: 1-l
    # For distance in between, no forced switch.
    # Need minimal number of switches from start to end adhering these constraints.

    dp_prev=[0,0]  # dp_prev[h] minimal entrances so far if segment at elevation h

    for i in range(1,len(inters)):
        d,o,l=inters[i]
        ndp=[math.inf,math.inf]
        for cur_elev in [0,1]:
            if o==-1:
                # no constraint, can be either
                pass
            else:
                # constraint applied according to ownership
                if o==1:
                    # same elevation as l
                    if cur_elev!=l:
                        continue
                else:
                    # opposite elevation to l
                    if cur_elev==l:
                        continue
            for prev_elev in [0,1]:
                cost=dp_prev[prev_elev]
                if cur_elev!=prev_elev:
                    cost+=1
                if cost<ndp[cur_elev]:
                    ndp[cur_elev]=cost
        dp_prev=ndp
    print(min(dp_prev))