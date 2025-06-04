import sys
import math
input=sys.stdin.readline

def angle_between(dx, dy):
    return math.degrees(math.atan2(dy, dx))%360

def normalize(a):
    if a<0: a+=360
    if a>=360: a-=360
    return a

def interval_intersection(a1,a2,b1,b2):
    # work in 0..360 range, intervals may wrap
    def to_list(s,e):
        if e>=s:
            return [(s,e)]
        else:
            return [(s,360),(0,e)]
    a_int=to_list(a1,a2)
    b_int=to_list(b1,b2)
    res=[]
    for as_,ae in a_int:
        for bs,be in b_int:
            s=max(as_,bs)
            e=min(ae,be)
            if s<=e:
                res.append((s,e))
    return res

def merge_intervals(intvs):
    # merge overlapping, intervals in 0..180
    intvs.sort()
    merged=[]
    for s,e in intvs:
        if not merged or merged[-1][1]<s:
            merged.append([s,e])
        else:
            if merged[-1][1]<e:
                merged[-1][1]=e
    return merged

n,w,d=map(int,input().split())
members=[input().split() for _ in range(n)]
members=[(int(x),int(y),f) for x,y,f in members]

walls=[]
# walls: (x,y): west x=0, east x=w, south y=0, north y=d
for i in range(w+1):
    walls.append((i,0))
    walls.append((i,d))
for j in range(1,d):
    walls.append((0,j))
    walls.append((w,j))

members_data=[]
for x,y,f in members:
    base_angle={'N':90,'E':0,'S':270,'W':180}[f]
    left_bound=base_angle-45
    right_bound=base_angle+45
    base_angle=normalize(base_angle)
    left_bound=normalize(left_bound)
    right_bound=normalize(right_bound)
    # store as start,right intervals normalized 0-360, handling wrapping below
    members_data.append((x,y,left_bound,right_bound))

def member_view_intervals(member):
    x,y,left,right=member
    intvs=[]
    wall_angles=[]
    for wx,wy in walls:
        dx=wx-x
        dy=wy - y
        a=angle_between(dx,dy)
        wall_angles.append((a,wx,wy))
    wall_angles.sort()
    angles=[wa[0] for wa in wall_angles]+[wall_angles[0][0]+360]
    for i in range(len(wall_angles)):
        a1=angles[i]
        a2=angles[i+1]
        # interval between walls along the wall
        # check midpoint between a1 and a2 to see if perpendicular hits wall
        mid=(a1+a2)/2
        # clamp mid to 0-360:
        midm=mid
        if midm>=360:
            midm-=360
        # Check if mid angle actually points to wall segment between i and i+1
        # The interval on the wall between wall_angles[i] and wall_angles[(i+1)%len]
        # is set by wall_angles[i] and wall_angles[i+1]
        # we do not need precise point, angular intervals suffice.
        # We add interval (a1,a2) as possible viewing of the wall segment
        intvs.append( (a1,a2) )
    return intvs

# For each member, find intervals on 0-360 representing their possible viewing wall arcs.

members_wall_intervals=[]

for idx,(x,y,left,right) in enumerate(members_data):
    vs=[] # visible arcs on wall 0-360 degrees
    wall_arcs=member_view_intervals((x,y,left,right))
    # For each arc on the wall, if arc overlaps the member field of view, keep that portion
    for (s,e) in wall_arcs:
        # intersection with member field of view (left,right)
        inter=interval_intersection(s,e,left,right)
        for (is_,ie) in inter:
            is_ = normalize(is_)
            ie = normalize(ie)
            # note is_<=ie or wrapping?
            members_wall_intervals.append( (idx,is_,ie) )


# Now for each member we get intervals on circle representing possible clock positions.
# The clock can be any point on wall, so an angle (0-360) direction from member position.

# We want to place minimal number of clocks (angles) so that for every member,
# at least one clock angle lies inside some visible interval of that member.

# Build a list of intervals combined per member

member_intervals = [[] for _ in range(n)]
for idx,is_,ie in members_wall_intervals:
    member_intervals[idx].append((is_,ie))

# Normalize intervals to 0-360 range, combine wrapping intervals split into two.

def split_wrap_intervals(intvs):
    res=[]
    for s,e in intvs:
        s=normalize(s)
        e=normalize(e)
        if e<s:
            res.append((s,360))
            res.append((0,e))
        else:
            res.append((s,e))
    return res

for i in range(n):
    member_intervals[i]=split_wrap_intervals(member_intervals[i])
    member_intervals[i]=merge_intervals(member_intervals[i])

# For convenience, treat intervals as half-open [start,end], collecting all as (start,end,members_set)

# We want a minimum set of points on circle to cover all members intervals.

# We solve as a hitting set for intervals on a circle:
# Unroll circle doubled to [0,720), duplicate intervals by adding +360,
# then do greedy.

events = []
for i in range(n):
    for s,e in member_intervals[i]:
        events.append((s,i))
        # duplicate interval at s+360
        events.append((s+360,i))
        # store ends for use in sorting below
        events.append((e,i))
        events.append((e+360,i))

intervals=[]
for i in range(n):
    for s,e in member_intervals[i]:
        intervals.append((s,e,i))
        intervals.append((s+360,e+360,i))

intervals.sort(key=lambda x:x[1]) # sort by end angle ascending

covered = set()
res = 0
points = []

for s,e,i_ in intervals:
    if i_ in covered:
        continue
    # place point at interval end e
    res +=1
    points.append(e)
    # cover all intervals containing e:
    for j,(js,je,mi) in enumerate(intervals):
        if mi not in covered and js <= e <= je:
            covered.add(mi)
    if len(covered) == n:
        break

print(res)