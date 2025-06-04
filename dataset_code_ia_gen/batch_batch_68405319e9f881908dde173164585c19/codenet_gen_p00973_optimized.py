import sys
import math
input=sys.stdin.readline

def polygon_area(poly):
    area=0
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]
        x2,y2=poly[(i+1)%n]
        area+=x1*y2 - x2*y1
    return abs(area)/2

def interpolate(p0,p1,t):
    return (p0[0]+(p1[0]-p0[0])*t, p0[1]+(p1[1]-p0[1])*t)

def dist(p,q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

n=int(input())
poly=[tuple(map(int,input().split())) for _ in range(n)]

area=polygon_area(poly)
half_area=area/2

# Precompute cumulative areas of triangles (0,i,i+1)
cumulative=[0]*(n+1)
for i in range(1,n):
    x0,y0=poly[0]
    x1,y1=poly[i]
    x2,y2=poly[i+1 if i+1<n else 0]
    tri_area=abs(x0*(y1-y2)+x1*(y2-y0)+x2*(y0-y1))/2
    cumulative[i+1]=cumulative[i]+tri_area

# For point 0 fixed, find for each i the point j>=i such that area(0,i,j) = half_area
# Using two pointers: for each i, move j forward to find area closest to half_area
# But area here refers to area between vertices 0,i,j in polygon, jagged shape
# Instead, use another approach:

# We'll "walk" along the polygon edges to find points that cut polygon into two halves by area
# Implement two-pointer approach:
# We consider chords between points i and j, and the polygon split by the chord
# The polygon is convex, so area(v_i..v_j) can be obtained efficiently

prefix_area=[0]*(n+1)
for i in range(n):
    x1,y1=poly[i]
    x2,y2=poly[(i+1)%n]
    prefix_area[i+1]=prefix_area[i]+(x1*y2 - x2*y1)/2

def area_between(i,j):
    # area of polygonal chain v_i to v_j along CCW order plus chord (j,i)
    if j<i:
        j+=n
    s=prefix_area[j]-prefix_area[i]
    xj,yj=poly[j%n]
    xi,yi=poly[i]
    return s + (xj*yi - xi*yj)/2

res_min=float('inf')
res_max=0.0

j=1
for i in range(n):
    if j<=i:
        j=i+1
    # Move j forward to get area(v_i..v_j) closest to half_area
    while True:
        a1=area_between(i,j%n)
        a2=area_between(i,(j+1)%n)
        if abs(a2 - half_area) < abs(a1 - half_area):
            j+=1
        else:
            break
    # Now chords (i,j%n) and (i,(j+1)%n) are candidates
    for jj in [j,j+1]:
        jj_mod=jj%n
        a=area_between(i,jj_mod)
        diff=a - half_area
        if diff==0:
            # perfect cut, chord from poly[i] to poly[jj_mod]
            length=dist(poly[i], poly[jj_mod])
            if length<res_min:
                res_min=length
            if length>res_max:
                res_max=length
        else:
            # the chord endpoints are discrete; try to find a better point on edge jj_mod->jj_mod+1 to exactly get half_area
            # We do binary search along edge jj_mod->(jj_mod+1)%n to find point p such that area_between(i,p)=half_area
            p1=poly[jj_mod]
            p2=poly[(jj_mod+1)%n]

            # To compute area_between(i,p) for p on edge jj_mod->jj_mod+1 compute area as:
            # area_between(i,jj_mod) + partial area between jj_mod and p along polygon edges
            # area between i and p along polygon edges = area_between(i,jj_mod) + t * area(edge jj_mod->jj_mod+1 triangle)
            # But we prefer using linear interpolation and polygon area formula

            # Define function f(t)=area_between(i, point at t on edge jj_mod->jj_mod+1) - half_area
            # We can binary search t in [0,1] for f(t)=0

            def area_t(t):
                # point p = interpolate(p1,p2,t)
                # polygon chain i to p = polygon chain i to jj_mod + triangle (poly[i], p1, p)
                # area_between(i,p) = area_between(i,jj_mod) + area of triangle poly[i], p1, p
                base=area_between(i,jj_mod)
                x0,y0=poly[i]
                x1,y1=p1
                x= x1 + (p2[0]-x1)*t
                y= y1 + (p2[1]-y1)*t
                tri_area=abs(x0*(y1 - y) + x1*(y - y0) + x*(y0 - y1))/2
                return base+tri_area

            low=0.0
            high=1.0
            for _ in range(50):
                mid=(low+high)/2
                val=area_t(mid)
                if val>half_area:
                    high=mid
                else:
                    low=mid
            t= (low+high)/2
            point=interpolate(p1,p2,t)
            length=dist(poly[i], point)
            if length<res_min:
                res_min=length
            if length>res_max:
                res_max=length

print(res_min)
print(res_max)