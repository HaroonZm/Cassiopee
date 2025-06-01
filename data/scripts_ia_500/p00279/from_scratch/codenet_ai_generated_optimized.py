import sys
import math
from itertools import combinations

sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def cross(a,b,o):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def area_poly(poly):
    area=0
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]
        x2,y2=poly[(i+1)%n]
        area+=x1*y2 - y1*x2
    return abs(area)/2

def is_convex(points):
    n=len(points)
    if n<3:
        return False
    prev=0
    for i in range(n):
        a=points[i]
        b=points[(i+1)%n]
        c=points[(i+2)%n]
        cr = cross(b,c,a)
        if cr==0:
            return False
        if prev==0:
            prev=1 if cr>0 else -1
        else:
            cur=1 if cr>0 else -1
            if cur!=prev:
                return False
    return True

def polygon_area_indices(indices, pts):
    poly = [pts[i] for i in indices]
    return area_poly(poly)

def sort_vertices(indices, pts):
    # order points counterclockwise starting from one with minimal y, then minimal x
    poly = [ (pts[i][0], pts[i][1], i) for i in indices]
    # find start vertex
    start = min(poly,key=lambda x:(x[1],x[0]))
    start_idx = poly.index(start)
    n=len(poly)
    # reorder list so start is first
    poly = poly[start_idx:] + poly[:start_idx]
    # check if CCW or CW, fix
    def cross2(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    if n>=3:
        if cross2(poly[0],poly[1],poly[2])<0:
            poly = poly[:1]+poly[:0:-1]
    return [p[2]+1 for p in poly]

N=int(input())
points=[tuple(map(int,input().split())) for _ in range(N)]
Q=int(input())
queries=[int(input()) for _ in range(Q)]

pts=points

# Precompute all k-subsets convex polygons with minimal area for each k
# Because N<=40 and k>=3, direct combinations of all size k is too large for large k
# We use backtracking with pruning + convexity check

# For each k, store minimal polygon area found and index set
min_area_for_k = dict()
min_poly_for_k = dict()

# To accelerate, precompute convex hull of all points as they given no 3 colinear points
# Unfortunately, the minimal polygon might not be convex hull points only. So we try all subsets

# Because problem is small N and output guarantees uniqueness, we do search:

# Optimization: For k=3, just check all triples (<=40^3=64000)
# For general k, use backtracking pruning with early area pruning
# Implement a recursive builder that keeps polygon convex at each step

# Instead, do as follows:
# 1) Sort points by x,y to have consistent order
# 2) For each k and combos of points, check convexity and area (combination count high)
# 3) Because N=40 and max k=N, we can do for small k fully, and for large k impossible to check all combos.
# But problem constraints: for all queries k<=N and Q<=N
# We can do:
# - For k<=6, brute-force all combos feasible
# - For k>6, we do heuristics or pruning, but problem states minimal polygon unique and difference at least 0.0001, so we can try to generate fast.

# Because problem wants minimal area convex polygon of size k from points, and no 3 points colinear:
# We can generate all subsets of size k, check if convex, if yes check area

# Count combos for N=40:
# C(40,7)=18643560 too big

# So final plan:
# Use a dedicated backtracking with pruning:
# Backtracking generate polygons in ccw order (indices increasing)
# At each step, check local convexity and area pruning
# Because N is small, it may suffice

# Because the problem finally is hardest, we will implement backtracking per k


pts_xy = points

def can_add_vertex(polygon, candidate):
    # polygon is list of indices in ccw order, candidate is index to try adding at end
    l = len(polygon)
    if l<2:
        return True
    a=pts_xy[polygon[-2]]
    b=pts_xy[polygon[-1]]
    c=pts_xy[candidate]
    # Check if angle at b with c is convex
    if cross(b,c,a)<=0:
        return False
    return True

def backtracking(k):
    res_area = float('inf')
    res_poly = None
    
    polygon = []
    used = [False]*N
    
    # We start from minimal point (lowest y, then x) to prevent duplicates
    start = min(range(N), key=lambda i:(pts_xy[i][1],pts_xy[i][0]))
    polygon.append(start)
    used[start]=True
    
    def dfs(depth):
        nonlocal res_area,res_poly
        if depth==k:
            # check if adding edge from last to first is convex
            if cross(pts_xy[polygon[-1]], pts_xy[polygon[0]], pts_xy[polygon[-2]])<=0:
                return
            # check if polygon is convex
            poly_pts = [pts_xy[i] for i in polygon]
            if not is_convex(poly_pts):
                return
            ar = area_poly(poly_pts)
            if ar<res_area:
                res_area=ar
                res_poly=polygon[:]
            return
        for nxt in range(N):
            if used[nxt]:
                continue
            # Require indices strictly increasing after start to avoid duplicates
            # Because polygon vertices are cyclic, ensure next index > polygon[-1] except first step
            if depth==1 and nxt<=start:
                continue
            # Check local convexity
            if depth>=2:
                a=pts_xy[polygon[-2]]
                b=pts_xy[polygon[-1]]
                c=pts_xy[nxt]
                if cross(b,c,a)<=0:
                    continue
            used[nxt]=True
            polygon.append(nxt)
            # Prune: Calculate partial area, if already larger than current best, prune
            if depth>=2:
                poly_pts = [pts_xy[i] for i in polygon]
                ar = area_poly(poly_pts)
                if ar>=res_area:
                    polygon.pop()
                    used[nxt]=False
                    continue
            dfs(depth+1)
            polygon.pop()
            used[nxt]=False
    
    dfs(1)
    if res_poly is None:
        return None
    # reorder polygon with start point minimal y,x and ccw order
    idxs = sort_vertices(res_poly, pts_xy)
    return idxs

cache_results = dict()
for k in set(queries):
    cache_results[k]=backtracking(k)

for k in queries:
    ans = cache_results[k]
    if ans is None:
        print("NA")
    else:
        print(*ans)