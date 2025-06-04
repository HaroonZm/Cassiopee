import sys
import math

# Epsilon for floating point comparisons
EPS = 1e-10

# Structure for points
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Subtract two points (vector subtraction)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Cross product of two vectors (points treated as vectors from origin)
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # Dot product of two vectors
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Distance squared between two points
    def dist2(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return dx*dx + dy*dy

# Segment between two points
class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # Checks if point q lies on this segment
    def on_segment(self, q):
        # q must be colinear with p1p2 and lie within bounding rectangle
        vec1 = self.p2 - self.p1
        vec2 = q - self.p1
        cross = vec1.cross(vec2)
        if abs(cross) > EPS:
            return False
        dot = vec1.dot(vec2)
        length2 = vec1.dot(vec1)
        return -EPS <= dot <= length2 + EPS

# Check intersection between two line segments
def segments_intersect(s1, s2):
    p = s1.p1
    r = s1.p2 - s1.p1
    q = s2.p1
    s = s2.p2 - s2.p1

    rxs = r.cross(s)
    q_p = q - p
    q_pxr = q_p.cross(r)

    # If r x s = 0 and (q-p) x r = 0, they are colinear
    if abs(rxs) < EPS and abs(q_pxr) < EPS:
        # Check for overlap of projections on x and y
        t0 = q_p.dot(r) / r.dot(r)
        t1 = t0 + s.dot(r) / r.dot(r)
        if t0 > t1:
            t0, t1 = t1, t0
        # If intervals [t0, t1] and [0,1] intersect, segments overlap
        if t0 > 1 + EPS or t1 < -EPS:
            return False, None
        # They overlap, but per problem, no three segments share same intersection and
        # segments have at most one intersection, so treat it as no intersection (handle separately)
        return False, None

    # If r x s = 0 and (q-p) x r != 0, parallel and non-intersecting
    if abs(rxs) < EPS and abs(q_pxr) >= EPS:
        return False, None

    # Otherwise, compute t and u where intersection might occur
    t = q_p.cross(s) / rxs
    u = q_p.cross(r) / rxs

    # Check if intersection occurs within both segments
    if -EPS <= t <= 1 + EPS and -EPS <= u <= 1 + EPS:
        # Compute intersection point
        intersec = Point(p.x + t * r.x, p.y + t * r.y)
        return True, intersec
    return False, None

# Given all segments, compute all intersection points and cut segments accordingly
def build_graph(segments):
    # For each segment, we store all points (original endpoints + intersections) on it
    seg_points = [[] for _ in range(len(segments))]

    # Add original endpoints to each segment list
    for i, seg in enumerate(segments):
        seg_points[i].append(seg.p1)
        seg_points[i].append(seg.p2)

    # Find intersections between pairs of segments
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            inter, point = segments_intersect(segments[i], segments[j])
            if inter:
                # Add the intersection point to both segments point list
                seg_points[i].append(point)
                seg_points[j].append(point)

    # For each segment, sort points along the segment by parametric distance t along the segment
    small_segments = []
    for i, seg in enumerate(segments):
        p_start = seg.p1
        p_end = seg.p2
        vec = p_end - p_start
        # Compute param t for each point on the segment
        def param_t(pt):
            if abs(vec.x) >= abs(vec.y):
                return (pt.x - p_start.x) / (vec.x if abs(vec.x) > EPS else 1)
            else:
                return (pt.y - p_start.y) / (vec.y if abs(vec.y) > EPS else 1)

        unique_points = []
        # Remove duplicates by using dist and coordinate tolerance
        pts = seg_points[i]
        # Sort points by parameter t along segment
        pts.sort(key=param_t)
        # Filter points very close to each other to avoid floating errors
        filtered = []
        for pt in pts:
            if not filtered:
                filtered.append(pt)
            else:
                last = filtered[-1]
                if last.dist2(pt) > 1e-12:
                    filtered.append(pt)
        seg_points[i] = filtered

        # Create small segments between consecutive points
        for k in range(len(filtered) - 1):
            a = filtered[k]
            b = filtered[k+1]
            # Add edge for smaller segment
            small_segments.append((a, b))
    return small_segments

# Determine if origin is inside polygon defined by edges.
# The edges form a planar graph with multiple faces.
# Our goal: check if origin is inside any of the closed faces.
#
# Approach:
# 1) Build planar graph of nodes and edges.
# 2) Find all polygonal faces.
# 3) For each face (polygon), check if origin (0,0) lies inside the polygon.
#
# To find faces:
# - Use DCEL or half-edge structure, or
# - Use a simpler approach: build adjacency, then traverse to find cycles (as polygon boundaries).
#
# Because problem size is small (max 100 lines, after intersection max ~few hundred edges),
# an Euler traversal of graph edges to find faces is doable.
#
# Algorithm:
# - Build graph: each node has list of adjacent nodes with edges.
# - Sort adjacency of each node counterclockwise by angle.
# - For each directed edge not visited, traverse next edges by turning left around node to find a face boundary.
# - Each face boundary detected is a polygon.
#
# Finally, check if origin (0,0) is inside any polygon (face) with area > 0 (outer face is normally infinite and area negative or zero).
#
# If origin is inside any polygon face, print "yes" else "no".

# Helper: angle between vector from p1 to p2 and x-axis
def angle(p1, p2):
    return math.atan2(p2.y - p1.y, p2.x - p1.x)

# Point in polygon test (ray casting)
def point_in_polygon(polygon, pt):
    # polygon: list of Point in order
    cnt = 0
    n = len(polygon)
    for i in range(n):
        a = polygon[i]
        b = polygon[(i+1)%n]
        if on_segment(a,b,pt):
            return True  # On boundary considered inside
        if ((a.y > pt.y) != (b.y > pt.y)):
            xint = (b.x - a.x)*(pt.y - a.y)/(b.y - a.y) + a.x
            if xint > pt.x - EPS:
                cnt += 1
    return (cnt % 2) == 1

def on_segment(a,b,p):
    # Check if p lies exactly on segment ab
    vec1 = b - a
    vec2 = p - a
    cross = vec1.cross(vec2)
    if abs(cross) > EPS:
        return False
    dot = vec1.dot(vec2)
    if dot < -EPS:
        return False
    if dot - vec1.dot(vec1) > EPS:
        return False
    return True

# Build graph as adjacency from edges
def build_adjacency(edges):
    # Assign IDs to points for indexing nodes
    # Use dictionary with coordinates rounded to 12 decimals as keys to avoid floating errors
    points_map = {}
    points_list = []

    def key(pt):
        return (round(pt.x,12), round(pt.y,12))

    for a,b in edges:
        if key(a) not in points_map:
            points_map[key(a)] = len(points_list)
            points_list.append(a)
        if key(b) not in points_map:
            points_map[key(b)] = len(points_list)
            points_list.append(b)

    adj = [[] for _ in range(len(points_list))]
    for a,b in edges:
        u = points_map[key(a)]
        v = points_map[key(b)]
        adj[u].append(v)
        adj[v].append(u)
    return points_list, adj

# Sort adjacency lists of each node CCW by angle
def sort_adjacency(points_list, adj):
    for u in range(len(points_list)):
        p = points_list[u]
        def ang(v):
            return (math.atan2(points_list[v].y - p.y, points_list[v].x - p.x) + 2*math.pi) % (2*math.pi)
        adj[u].sort(key=ang)

# Half-edge structure for face traversal
class HalfEdge:
    def __init__(self, u, v, next_h=None):
        self.u = u
        self.v = v
        self.next = next_h
        self.face = None

def find_faces(points_list, adj):
    n = len(points_list)
    # For each directed edge, we create half-edge object
    # key: (u,v)
    half_edges = {}
    # Build mapping from directed edge to index in adjacency to find next CCW edge easily
    pos_in_adj = [{} for _ in range(n)]
    for u in range(n):
        for i,v in enumerate(adj[u]):
            pos_in_adj[u][v] = i

    # Create half edges
    for u in range(n):
        for v in adj[u]:
            half_edges[(u,v)] = HalfEdge(u,v)

    # Set next pointers: for half-edge (u,v), next half-edge is (v,w)
    # where w is the next neighbor after u in CCW order around v
    for (u,v), he in half_edges.items():
        idx = pos_in_adj[v][u]
        next_idx = (idx - 1) % len(adj[v])  # -1 because CCW order and roads arranged CCW (standard technique)
        w = adj[v][next_idx]
        he.next = half_edges[(v,w)]

    faces = []
    visited = set()
    # Traverse all half edges to find face cycles
    for he_key, he in half_edges.items():
        if he_key in visited:
            continue
        face = []
        cur = he
        while True:
            visited.add((cur.u, cur.v))
            face.append(points_list[cur.u])
            cur = cur.next
            if cur == he:
                break
        faces.append(face)
    return faces

def polygon_area(poly):
    area = 0.0
    n = len(poly)
    for i in range(n):
        a = poly[i]
        b = poly[(i+1)%n]
        area += a.x*b.y - a.y*b.x
    return area/2

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n = int(line)
        if n == 0:
            break
        segments = []
        for _ in range(n):
            x1,y1,x2,y2 = map(int,input().split())
            p1 = Point(x1,y1)
            p2 = Point(x2,y2)
            segments.append(Segment(p1,p2))

        # 1) Build all small segments by adding intersection points and splitting original segments
        small_segments = build_graph(segments)

        # 2) Build adjacency graph for nodes
        points_list, adj = build_adjacency(small_segments)

        # 3) Sort adjacency lists CCW to prepare for face traversal
        sort_adjacency(points_list, adj)

        # 4) Find polygonal faces from half edges
        faces = find_faces(points_list, adj)

        origin = Point(0,0)
        trapped = False
        for face in faces:
            area = polygon_area(face)
            # Ignore faces with near zero or negative area (could be external face)
            if abs(area) < EPS:
                continue
            # We consider only faces with positive area (CCW order)
            # If face is CW, reverse to CCW for point-in-polygon test
            if area < 0:
                face.reverse()
            if point_in_polygon(face, origin):
                trapped = True
                break

        print("yes" if trapped else "no")

if __name__ == "__main__":
    main()