import sys
import math
from collections import deque

def dist(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])

def on_segment(p,q,r):
    return (min(p[0],r[0]) <= q[0] <= max(p[0],r[0]) and
            min(p[1],r[1]) <= q[1] <= max(p[1],r[1]))

def orientation(p,q,r):
    val = (q[1]-p[1])*(r[0]-q[0])-(q[0]-p[0])*(r[1]-q[1])
    if abs(val)<1e-14: return 0
    return 1 if val>0 else 2

def segments_intersect(p1,q1,p2,q2):
    o1=orientation(p1,q1,p2)
    o2=orientation(p1,q1,q2)
    o3=orientation(p2,q2,p1)
    o4=orientation(p2,q2,q1)
    if o1!=o2 and o3!=o4:
        return True
    if o1==0 and on_segment(p1,p2,q1): return True
    if o2==0 and on_segment(p1,q2,q1): return True
    if o3==0 and on_segment(p2,p1,q2): return True
    if o4==0 and on_segment(p2,q1,q2): return True
    return False

def point_in_poly(pt,poly):
    # convex polygon with CCW points
    n=len(poly)
    prev=orientation(poly[0],poly[1],pt)
    for i in range(1,n):
        o=orientation(poly[i],poly[(i+1)%n],pt)
        if o==0:
            if on_segment(poly[i],pt,poly[(i+1)%n]):
                return True
            else:
                return False
        if o!=prev and o!=0:
            return False
    return True

def line_poly_intersect(p1,p2,poly,h,sun_dir3d):
    # Check if segment p1-p2 shadows on poly
    # Shadow if some building's pillar intersects line sunlight ray from p
    # The line from p is in direction sun_dir2d (projection x,y)
    # If building's polygon projects on line between p and sun infinitely (vertical pillar),
    # consider vertical extent of building (height h) and sun elevation (phi).
    # If the height of pillar occluding line from sun is enough, p is shaded.
    # But problem states:
    # "あなたが立っている地点と太陽を一直線に結んだ線上に建物がある場合，あなたは建物の陰にいる"
    # So p is shaded if ray from p to sun intersects building polygon vertically within building height.

    # Because sun is infinite distance, the shadow test is if the ray from p to sun intersects polygon at any height less than building height (with sun’s elevation angle).
    # Project polygon edges in 2D and check if line from p points to sun hits polygon.

    # Here we just check if line from p to sun along sun_dir hits polygon.

    EPS=1e-9
    # Find intersection of ray from p1 along -sun_dir with polygon edges
    # If intersection distance along ray from p1 is between 0 and infinite, check vertical obstruction height.
    # sun_dir3d is unit vector in 3D direction of sun
    sun_dir2d=(sun_dir3d[0],sun_dir3d[1])
    ray_p=p1
    ray_dir=(-sun_dir2d[0],-sun_dir2d[1])
    # normalize ray_dir
    norm=math.hypot(ray_dir[0],ray_dir[1])
    ray_dir=(ray_dir[0]/norm,ray_dir[1]/norm)
    intrs=[]
    n = len(poly)
    for i in range(n):
        a=poly[i]
        b=poly[(i+1)%n]
        # segment a-b
        # parametric line a + t*(b-a)
        # ray param s >=0: ray_p + s*ray_dir
        dx = b[0]-a[0]
        dy = b[1]-a[1]
        det = dx*(-ray_dir[1]) + dy*ray_dir[0]
        if abs(det) < EPS:
            continue
        t = ((ray_p[0]-a[0])*(-ray_dir[1]) - (ray_p[1]-a[1])*(-ray_dir[0]))/det
        s = (dx*(ray_p[1]-a[1]) - dy*(ray_p[0]-a[0]))/det
        if 0<= t <=1 and s >= 0:
            intrs.append((s,a[0]+dx*t,a[1]+dy*t))
    if not intrs:
        return False
    s_min = min(intrs,key=lambda x:x[0])[0]
    # Now compute vertical obstruction
    # height of sun ray at distance s_min
    # vertical height to ground at p1 is 0, sun elevation angle phi, height = s_min * tan(phi)
    shadow_height = s_min * math.tan(math.radians(sun_dir3d[2]))
    # if building height h >= shadow_height => shaded
    return h >= shadow_height-EPS

def is_shadowed(pt, buildings, sun_dir3d):
    # pt: 2d point
    # sun_dir3d: (cosθ*cosφ, sinθ*cosφ, sinφ), sun elevation angle in deg
    for poly,h in buildings:
        if line_poly_intersect(pt, None, poly, h, sun_dir3d):
            return True
    return False

def segment_on_building_edge(p1,p2,buildings):
    # Check if segment lies exactly on building edge (walking on eaves, no sun)
    for poly,h in buildings:
        n=len(poly)
        for i in range(n):
            a=poly[i]
            b=poly[(i+1)%n]
            # check if segment p1-p2 is subset of segment a-b
            # 1) colinear and p1,p2 lying on a-b
            o1=orientation(a,b,p1)
            o2=orientation(a,b,p2)
            if o1==0 and o2==0:
                if on_segment(a,p1,b) and on_segment(a,p2,b):
                    return True
    return False

def segment_blocked(p1,p2,buildings):
    # Check if segment p1-p2 intersects any building polygon interior (building walls)
    for poly,h in buildings:
        n=len(poly)
        for i in range(n):
            a=poly[i]
            b=poly[(i+1)%n]
            if (segments_intersect(p1,p2,a,b)):
                # ensure not just touching at endpoint on building edge
                # if segment exactly matches edge: allowed
                if segment_on_building_edge(p1,p2,[(poly,h)]):
                    continue
                # else intersection means blocked
                # Also check if intersection point is endpoint of segment and equal to building vertex: allowed
                # But problem states starting and target points are outside building and on no edges.
                # So this intersection is real, blocked
                return True
        # Also check if segment is inside building:
        mid = ((p1[0]+p2[0])*0.5, (p1[1]+p2[1])*0.5)
        if point_in_poly(mid,poly):
            return True
    return False

def build_visibility_graph(nodes, buildings, sun_dir3d, sun_2d_dir):
    n=len(nodes)
    graph=[[] for _ in range(n)]
    shadowed=[False]*n
    for i,p in enumerate(nodes):
        shadowed[i]=is_shadowed(p,buildings,sun_dir3d)
    for i in range(n):
        for j in range(i+1,n):
            p1=nodes[i]
            p2=nodes[j]
            if segment_blocked(p1,p2,buildings):
                continue
            on_edge = segment_on_building_edge(p1,p2,buildings)
            d=dist(p1,p2)
            if on_edge:
                w=0.0
            else:
                # length over sun: if nodes i and j are both shadowed, segment is fully shaded (w=0)
                # if neither shadowed, w=d
                # if one shadowed one not, check points along segment? We'll approximate by sampling
                if shadowed[i] and shadowed[j]:
                    w=0.0
                elif not shadowed[i] and not shadowed[j]:
                    w=d
                else:
                    # sample points along segment
                    samples = max(2,int(d*10))
                    sunwalk=0.0
                    last_shadowed=is_shadowed(p1,buildings,sun_dir3d)
                    prev_point=p1
                    for k in range(1,samples+1):
                        t=k/samples
                        x=p1[0]+t*(p2[0]-p1[0])
                        y=p1[1]+t*(p2[1]-p1[1])
                        cur_shadowed=is_shadowed((x,y),buildings,sun_dir3d)
                        dx=math.hypot(x-prev_point[0], y-prev_point[1])
                        if not cur_shadowed:
                            sunwalk+=dx
                        prev_point=(x,y)
                    w=sunwalk
            graph[i].append((j,w))
            graph[j].append((i,w))
    return graph, shadowed

def dijkstra(graph, start, end):
    import heapq
    n=len(graph)
    dist_arr=[math.inf]*n
    dist_arr[start]=0
    hq=[(0,start)]
    while hq:
        cd,u=heapq.heappop(hq)
        if dist_arr[u]<cd:
            continue
        if u==end:
            return cd
        for v,w in graph[u]:
            nd=cd+w
            if dist_arr[v]>nd:
                dist_arr[v]=nd
                heapq.heappush(hq,(nd,v))
    return dist_arr[end]

def main():
    input=sys.stdin.read().strip().split()
    idx=0
    while True:
        if idx>=len(input):
            break
        N=int(input[idx])
        idx+=1
        if N==0:
            break
        buildings=[]
        for _ in range(N):
            NV=int(input[idx]); idx+=1
            H=int(input[idx]); idx+=1
            poly=[]
            for __ in range(NV):
                x=int(input[idx]); y=int(input[idx+1])
                idx+=2
                poly.append((x,y))
            buildings.append((poly,H))
        theta=float(input[idx]); idx+=1
        phi=float(input[idx]); idx+=1
        Sx=int(input[idx]); Sy=int(input[idx+1])
        Tx=int(input[idx+2]); Ty=int(input[idx+3])
        idx+=4

        # sun dir 3d vector, theta from +x CCW, phi elevation from horizon
        rad_theta=math.radians(theta)
        rad_phi=math.radians(phi)
        sun_dir3d=(math.cos(rad_theta)*math.cos(rad_phi), math.sin(rad_theta)*math.cos(rad_phi), math.sin(rad_phi))
        sun_2d_dir=(sun_dir3d[0], sun_dir3d[1])

        # nodes: S,T and all polygon vertices
        nodes=[(Sx,Sy),(Tx,Ty)]
        base=2
        for poly,_ in buildings:
            nodes.extend(poly)

        graph,shadowed = build_visibility_graph(nodes, buildings, sun_dir3d, sun_2d_dir)

        ans=dijkstra(graph,0,1)
        print(f"{ans:.5f}")

if __name__=="__main__":
    main()