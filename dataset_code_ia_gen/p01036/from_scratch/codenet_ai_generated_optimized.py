import sys
import math
input=sys.stdin.readline

def polygon_area(poly):
    area=0
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]
        x2,y2=poly[(i+1)%n]
        area+=x1*y2 - y1*x2
    return abs(area)*0.5

def is_on_segment(px,py,x1,y1,x2,y2):
    # Check if point (px,py) lies exactly on segment (x1,y1)-(x2,y2)
    cross=(x2 - x1)*(py - y1)-(y2 - y1)*(px - x1)
    if abs(cross)>1e-12:
        return False
    dot=(px - x1)*(x2 - x1)+(py - y1)*(y2 - y1)
    if dot<0:
        return False
    sq_len=(x2 - x1)**2+(y2 - y1)**2
    if dot>sq_len:
        return False
    return True

def point_in_poly(px,py,poly):
    # Strict inside (no points on edges)
    inside=False
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]
        x2,y2=poly[(i+1)%n]
        # Check edge
        if is_on_segment(px,py,x1,y1,x2,y2):
            return False
        if ((y1>py) != (y2>py)):
            x_inters=(x2 - x1)*(py - y1)/(y2 - y1)+x1
            if x_inters>px:
                inside=not inside
    return inside

def clip_polygon(subjectPolygon, clipPolygon):
    def inside(p, cp1, cp2):
        return (cp2[0]-cp1[0])*(p[1]-cp1[1]) - (cp2[1]-cp1[1])*(p[0]-cp1[0]) >=0
    def intersection(cp1, cp2, s, e):
        dc = (cp1[0]-cp2[0], cp1[1]-cp2[1])
        dp = (s[0]-e[0], s[1]-e[1])
        n1 = cp1[0]*cp2[1]-cp1[1]*cp2[0]
        n2 = s[0]*e[1]-s[1]*e[0]
        denom = dc[0]*dp[1]-dc[1]*dp[0]
        if abs(denom)<1e-15:
            return s
        x = (n1*dp[0]-n2*dc[0])/denom
        y = (n1*dp[1]-n2*dc[1])/denom
        return (x,y)
    outputList=subjectPolygon
    cp1=clipPolygon[-1]
    for cp2 in clipPolygon:
        inputList=outputList
        outputList=[]
        if not inputList:
            break
        s=inputList[-1]
        for e in inputList:
            if inside(e,cp1,cp2):
                if not inside(s,cp1,cp2):
                    outputList.append(intersection(cp1,cp2,s,e))
                outputList.append(e)
            elif inside(s,cp1,cp2):
                outputList.append(intersection(cp1,cp2,s,e))
            s=e
        cp1=cp2
    return outputList

def create_circle_poly(cx,cy,r,seg=60):
    poly=[]
    for i in range(seg):
        angle=2*math.pi*i/seg
        poly.append((cx+r*math.cos(angle),cy+r*math.sin(angle)))
    return poly

n,cx,cy,r=map(int,input().split())
polys=[]
for _ in range(n):
    p,score= map(int,input().split())
    poly=[tuple(map(int,input().split())) for __ in range(p)]
    polys.append((poly,score))

circle=create_circle_poly(cx,cy,r,60)
circle_area=math.pi*r*r

expect=0.0
for poly,score in polys:
    inter=clip_polygon(poly,circle)
    if not inter:
        continue
    area=polygon_area(inter)
    if area<1e-15:
        continue
    expect+=score*area/circle_area

print(expect)