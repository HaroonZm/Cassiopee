import sys
input=sys.stdin.readline

def cross(a,b,o):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def on_segment(p,q,r):
    # p,q,r colinear, check if q lies on pr
    return min(p[0],r[0])<q[0]<max(p[0],r[0]) and min(p[1],r[1])<q[1]<max(p[1],r[1])

def segments_intersect(a,b,c,d):
    # returns True if segments ab and cd properly intersect
    # Edges on polygon are excluded (edges themselves not obstacles)
    d1=cross(d,a,c)
    d2=cross(d,b,c)
    d3=cross(a,c,b)
    d4=cross(a,d,b)
    if d1*d2<0 and d3*d4<0:
        return True
    # no edge intersection counted (edges not obstacles)
    return False

def point_in_polygon(p,poly):
    # ray casting method
    cnt=0
    n=len(poly)
    for i in range(n):
        a=poly[i]
        b=poly[(i+1)%n]
        if a[1]==b[1]:
            continue
        if p[1]<min(a[1],b[1]):
            continue
        if p[1]>=max(a[1],b[1]):
            continue
        x=a[0]+(b[0]-a[0])*(p[1]-a[1])/(b[1]-a[1])
        if x>p[0]:
            cnt+=1
    return cnt%2==1

def can_see(o,v,obstacles):
    # check segment ov does not intersect interiors of obstacles
    # edges excluded from obstacle area, so intersection at edge not blocking
    # So only proper intersections count
    for poly in obstacles:
        n=len(poly)
        # If o or v in obstacle interior? problem guarantees no voter inside obstacles.
        # Check if segment intersects polygon edges.
        for i in range(n):
            a=poly[i]
            b=poly[(i+1)%n]
            # skip if any endpoint equal to a or b (then segment endpoint on edge)
            # edges excluded from obstacle so not blocking
            if o==a or o==b or v==a or v==b:
                continue
            if segments_intersect(o,v,a,b):
                return False
        # check if segment passes through interior: shooting from point o to v could cross polygon interior without intersecting edges?
        # not possible in simple polygon, intersection of segment with polygon is edges or inside
        # so edge checks sufficient if polygon no self intersection
        # check if midpoint inside polygon to disambiguate when segment inside polygon (blocker)
        mid = ((o[0]+v[0])/2,(o[1]+v[1])/2)
        if point_in_polygon(mid,poly):
            return False
    return True

N,M=map(int,input().split())
obstacles=[]
for _ in range(N):
    L=int(input())
    poly=[tuple(map(int,input().split())) for __ in range(L)]
    obstacles.append(poly)
voters=[tuple(map(int,input().split())) for _ in range(M)]

# Candidates for speaker position:
# The voters' positions themselves (M points)
# The vertices of the obstacles (sum L <=15)
# The intersection points of lines from polygon vertices to voters? But complexity and precision heavy
# Because the number of voters and obstacles small, brute force on a set of candidate points:
# candidate points = all voters + all polygon vertices
candidates = voters[:]
for poly in obstacles:
    candidates.extend(poly)

max_seen=0
for p in candidates:
    cnt=0
    for v in voters:
        if can_see(p,v,obstacles):
            cnt+=1
    if cnt>max_seen:
        max_seen=cnt

print(max_seen)