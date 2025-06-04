import sys
import math
import heapq

input=sys.stdin.readline

def euclid(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])

def dijkstra(n,graph,start,end):
    dist=[math.inf]*n
    dist[start]=0
    h=[(0,start)]
    while h:
        cd,u=heapq.heappop(h)
        if dist[u]<cd:
            continue
        if u==end:
            return cd
        for v,w in graph[u]:
            nd=cd+w
            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(h,(nd,v))
    return math.inf

NA,NB=map(int,input().split())
A=[tuple(map(int,input().split())) for _ in range(NA)]
B=[tuple(map(int,input().split())) for _ in range(NB)]

def build_graph(points):
    n=len(points)
    graph=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            d=euclid(points[i],points[j])
            graph[i].append((j,d))
            graph[j].append((i,d))
    return graph

def check_cross(p1,p2,p3,p4):
    # Check if two line segments p1p2 and p3p4 intersect (excluding endpoints)
    def ccw(a,b,c):
        return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
    return (ccw(p1,p3,p4) != ccw(p2,p3,p4)) and (ccw(p1,p2,p3) != ccw(p1,p2,p4))

# We want to build minimal-length connected path from A[0] to A[1] using only A points, similarly for B,
# with edges as straight lines between any pair of points in the same group.
# But the condition: the paths for A and B must not cross.
# Since we can build any edges inside A and B freely, minimal Steiner path is shortest path in complete graph.
# However, the only constraint is that line segments of path A and path B do not intersect.
# Paths are sequences of edges (line segments).

# Approach:
# 1) Compute minimal path length from A[0] to A[1] in complete graph on A (any edges allowed).
# 2) Same for B.
# 3) But minimal paths in complete graph are trivial (just the direct edge), and edges can cross between the two sets
# Because the minimal path for each is possibly a single edge between their two special points.
#
# The constraint says their path edges cannot cross between the two groups.
#
# So if the direct edge connecting A[0]-A[1] and B[0]-B[1] crosses => no solution if both paths are the direct edges.
#
# But it's allowed to use intermediate points inside the same group to find a path avoiding crossing.
#
# So we need to find two simple paths: one in A graph from A[0]->A[1], another in B graph from B[0]->B[1],
# such that any edge from path A does not cross any edge from path B.
#
# Since edges inside same tribe can intersect, no problem inside the group.
#
# Problem is to find minimal sum of edge lengths/path lengths subject to no crossing between the two paths' edges.
#
# It's similar to finding shortest paths in each group with forbidden edges/path combinations that cross with the other's path.
#
# The complexity to search all paths is huge.
#
# Alternative solution:
# Since intersection of edges occurs only when the edges cross geometrically,
# and because all points are distinct and non-collinear (no 3 points on a line),
# and also because any edges inside same group are allowed,
# we can check the following:
#
# If the segments A[0]-A[1] and B[0]-B[1] do not cross, then minimal total length is
# length(A[0]-A[1]) + length(B[0]-B[1]) (direct edge in each).
#
# If these two edges cross, maybe using other points to construct path helps to avoid crossing edges between groups.

# What's the minimal length for each group alone?
# Minimal path between two points with arbitrary other points in the group may only reduce length if we can use multi-hop edges that sum to smaller length than direct edge.
# But triangle inequality applies: sum of smaller edges will always be >= direct edge.
# So the direct edge is the minimal path between two points.

# Thus the minimal length for group A is dist(A[0],A[1])
# minimal length for B is dist(B[0],B[1])

# The problem is the crossing between A's path edge(s) and B's path edge(s).
# If direct edges cross => not allowed paths.
#
# Then what about multi-hop paths?
# In A, select path between A[0] and A[1],
# In B, select path between B[0] and B[1],
# and check if any pair of edges in A's path and B's path cross.
#
# If yes, no solution.
#
# So:
# We want to find two paths (shortest) inside A and B's points respectively, from given nodes, so that no edges of A's path and B's path cross.
# If no such paths, output -1.

# We can model this as:
# For A: compute MST or shortest path with edges that do not cross any edges used by B's path, similarly for B.
# But interdependent: we don't know B's path before finding A's and vice versa.

# A brute force would be too large (up to 1000 points per tribe).

# Key insight:
# Since edges inside each tribe can be composed arbitrarily, and forbidden only if crossing edges with other tribe,
# and because no three points are colinear and coordinates small,
# Let's try:
# Direct path A: edge (A0,A1)
# Direct path B: edge (B0,B1)
# if they do not cross, output sum of distances direct edges.

# Else:
# Then try all possible edges between A0->some A point->A1 and check if with path for B direct edge (B0,B1) crossing is avoided

# Similarly for B.

# Since 1000 points is manageable, do the following:
# For A:
# - Build graph of edges between all pairwise points (complete graph)
# - For all edges in A, only keep edges that do NOT cross the direct edge (B0,B1)
#
# Dijkstra from A0 to A1 on this filtered graph (A edges that don't cross B0-B1)
#
# For B:
# Same, filtering edges that do NOT cross A0-A1 direct edge.

# Then check if solutions exist:

# If both paths exist (no crossing edges with respective other tribe's direct edge), sum their lengths.

# Check if the minimal sum is with no crossing edges.

# If no, output -1.

# If both direct edges cross, and filtering like that leads to no path, then -1.

# But problem states that edges inside same group can cross. Only crossing between two tribes' paths forbidden.

# So only crossing edges between A and B group path edges forbidden.

# We will try:

# 1) Check if direct edges cross: if no, output sum of direct edges length.

# Else:

# 2) For each tribe:

# Build graph with edges between all pairs which do NOT cross the other tribe's direct edge.

# Find shortest path.

# If either path does not exist, output -1.

# Else output sum.

# This is a heuristic considering paths only as to prevent crossing with other tribe's direct edge.

# Because if other tribe uses multi-hop path, it's too complex to check all pairs crossings.

# But problem suggests it's acceptable to only check crossing between path edges.

# If both tribes' paths are connected using edges not crossing other tribe's direct edge, their paths won't cross.

# Let's implement this.

def edges_cross_check(p1,p2,q1,q2):
    # exclude sharing endpoints
    if p1==q1 or p1==q2 or p2==q1 or p2==q2:
        return False
    return check_cross(p1,p2,q1,q2)

def build_filtered_graph(points, forbidden_edge):
    n=len(points)
    graph=[[] for _ in range(n)]
    f1,f2=forbidden_edge
    for i in range(n):
        for j in range(i+1,n):
            if not edges_cross_check(points[i],points[j],f1,f2):
                d=euclid(points[i],points[j])
                graph[i].append((j,d))
                graph[j].append((i,d))
    return graph

def solve():
    A0,A1=A[0],A[1]
    B0,B1=B[0],B[1]
    A_dist=euclid(A0,A1)
    B_dist=euclid(B0,B1)
    cross=edges_cross_check(A0,A1,B0,B1)
    if not cross:
        print(A_dist+B_dist)
        return
    # Else, try to avoid crossing by multi-hop paths
    G_A=build_filtered_graph(A,(B0,B1))
    resA=dijkstra(NA,G_A,0,1)
    G_B=build_filtered_graph(B,(A0,A1))
    resB=dijkstra(NB,G_B,0,1)
    if resA==math.inf or resB==math.inf:
        print(-1)
        return
    print(resA+resB)

solve()