import sys
import math
from heapq import heappush, heappop

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def min_dist_to_monsters(p, monsters):
    return min(dist(p,m) for m in monsters) if monsters else float('inf')

def min_dist_count(p, monsters):
    dists = [dist(p,m) for m in monsters]
    if not dists:
        return 0
    mind = min(dists)
    return sum(1 for v in dists if abs(v-mind)<1e-10)

def inside_area(p):
    return 0.0<=p[0]<=4.0 and 0.0<=p[1]<=4.0

def can_be_safe(p, monsters):
    cnt = min_dist_count(p, monsters)
    return cnt>=2

def solve(monsters):
    start_points = [(0,y) for y in [i*0.5 for i in range(9)] if can_be_safe((0,y),monsters)]
    end_x = 4.0
    EPS=1e-7

    nodes = []
    nodes.extend(start_points)
    nodes.extend(monsters)
    nodes.append((end_x,0.0))
    nodes.append((end_x,4.0))

    # filter end points if safe
    end_points = []
    for y in [i*0.5 for i in range(9)]:
        p = (end_x,y)
        if can_be_safe(p, monsters):
            nodes.append(p)
            end_points.append(p)
    if not end_points:
        return 'impossible'

    # Build graph of edges between nodes where the path is safe all along
    # We approximate safety over each edge by small steps along the segment
    graph = {i:[] for i in range(len(nodes))}
    n = len(nodes)
    for i in range(n):
        for j in range(i+1,n):
            a,b = nodes[i], nodes[j]
            # Check if whole segment is inside region and safe
            length = dist(a,b)
            if length==0:
                continue
            steps = max(10,int(length/0.05))
            safe = True
            for k in range(steps+1):
                t = k/steps
                x = a[0]+(b[0]-a[0])*t
                y = a[1]+(b[1]-a[1])*t
                p = (x,y)
                if not inside_area(p) or not can_be_safe(p, monsters):
                    safe = False
                    break
            if safe:
                graph[i].append((j,length))
                graph[j].append((i,length))

    # Start nodes indices
    start_ids = [i for i,p in enumerate(nodes) if p in start_points]
    end_ids = [i for i,p in enumerate(nodes) if p in end_points]

    # Dijkstra from all start points
    dist_arr = [float('inf')]*n
    hq = []
    for s in start_ids:
        dist_arr[s]=0.0
        heappush(hq,(0.0,s))

    while hq:
        cd,u=heappop(hq)
        if dist_arr[u]<cd-1e-10:
            continue
        if u in end_ids:
            return '{:.12f}'.format(cd)
        for v,w in graph[u]:
            nd = cd+w
            if nd<dist_arr[v]-1e-10:
                dist_arr[v]=nd
                heappush(hq,(nd,v))
    return 'impossible'

input=sys.stdin.readline
while True:
    n=int(input())
    if n==0:
        break
    monsters = [tuple(map(float, input().split())) for _ in range(n)]
    print(solve(monsters))