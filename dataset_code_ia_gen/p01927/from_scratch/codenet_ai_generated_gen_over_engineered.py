import sys
import math
import heapq
from typing import List, Tuple, Dict, Optional, Set

class Vector2D:
    __slots__ = ['x', 'y']
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other:'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other:'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def dot(self, other:'Vector2D') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other:'Vector2D') -> float:
        return self.x * other.y - self.y * other.x

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def distance_to(self, other:'Vector2D') -> float:
        return (self - other).length()

    def normalize(self) -> 'Vector2D':
        l = self.length()
        if l == 0:
            return Vector2D(0,0)
        return Vector2D(self.x / l, self.y / l)

    def angle_with(self, other:'Vector2D') -> float:
        # Returns angle from self to other in radians, between -pi and pi
        dot = self.dot(other)
        det = self.cross(other)
        return math.atan2(det, dot)

    def project_onto(self, other:'Vector2D') -> 'Vector2D':
        # Project self onto vector other
        other_n = other.normalize()
        return other_n * self.dot(other_n)

    def __repr__(self) -> str:
        return f"V({self.x},{self.y})"

class Polygon:
    def __init__(self, vertices: List[Vector2D]):
        self.vertices = vertices
        self.n = len(vertices)
        self.edges = [(vertices[i], vertices[(i+1)%self.n]) for i in range(self.n)]

    def contains_point(self, p: Vector2D) -> bool:
        # Since convex polygon, use cross products to check if point is inside
        # Point is inside iff it is always on same side of all edges
        prev = 0
        for i in range(self.n):
            A = self.vertices[i]
            B = self.vertices[(i+1)%self.n]
            v1 = B - A
            v2 = p - A
            cp = v1.cross(v2)
            if cp == 0:
                # On boundary
                return True
            if cp * prev < 0:
                if prev != 0:
                    return False
            else:
                prev = cp if prev == 0 else prev
        return True if prev != 0 else False

    def is_point_on_boundary(self, p: Vector2D) -> bool:
        # Check if point lies on polygon boundary (edges)
        for A,B in self.edges:
            if _point_on_segment(p, A, B):
                return True
        return False

    def __repr__(self) -> str:
        return f"Polygon({self.vertices})"

def _point_on_segment(p: Vector2D, a: Vector2D, b: Vector2D) -> bool:
    # Check if point p lies on segment ab (inclusive)
    cross = (b - a).cross(p - a)
    if abs(cross) > 1e-10:
        return False
    dot = (p - a).dot(b - a)
    if dot < -1e-10:
        return False
    if dot > (b - a).dot(b - a) + 1e-10:
        return False
    return True

def segments_intersect(a1: Vector2D, a2: Vector2D, b1: Vector2D, b2: Vector2D) -> bool:
    # Check if line segments a1a2 and b1b2 intersect
    d1 = (a2 - a1)
    d2 = (b2 - b1)
    def direction(a,b,c):
        return (c - a).cross(b - a)
    d = d1.cross(d2)
    if abs(d) < 1e-14:
        # Colinear or parallel
        # Check overlapping if colinear
        if abs(direction(a1,a2,b1)) > 1e-14:
            return False
        # Otherwise check projections overlap
        if _point_on_segment(b1, a1, a2) or _point_on_segment(b2, a1, a2) or _point_on_segment(a1, b1, b2) or _point_on_segment(a2, b1, b2):
            return True
        return False
    t = (b1 - a1).cross(d2) / d
    u = (b1 - a1).cross(d1) / d
    return 0 <= t <= 1 and 0 <= u <= 1

class Ray:
    def __init__(self, origin: Vector2D, direction: Vector2D):
        self.origin = origin
        self.direction = direction.normalize()

    def point_at(self, t: float) -> Vector2D:
        return self.origin + self.direction * t

    def intersects_segment(self, a: Vector2D, b: Vector2D) -> Optional[Vector2D]:
        # Compute intersection point between ray and segment ab if any
        v1 = self.origin - a
        v2 = b - a
        v3 = Vector2D(-self.direction.y, self.direction.x)
        denom = v2.dot(v3)
        if abs(denom) < 1e-15:
            return None
        t1 = v2.cross(v1) / denom
        t2 = v1.dot(v3) / denom
        if t1 < -1e-15:
            return None
        if t2 < -1e-15 or t2 > 1 + 1e-15:
            return None
        return self.point_at(t1)

class SolarVector:
    def __init__(self, theta_deg: float, phi_deg: float):
        theta = math.radians(theta_deg)
        phi = math.radians(phi_deg)
        # Convert solar angles to vector direction on ground xy plane
        # Theta is azimuth from +x axis CCW
        # Phi is elevation from horizontal
        # The sun vector is unit vector towards the sun
        self.direction3d = (
            math.cos(phi) * math.cos(theta),
            math.cos(phi) * math.sin(theta),
            math.sin(phi)
        )
        # Shadow direction on XY plane (the inverse of sun vector projection on ground)
        self.shadow_direction = Vector2D(-self.direction3d[0], -self.direction3d[1]).normalize()

    def is_point_in_shadow_of_segment(self, p: Vector2D, seg_start: Vector2D, seg_end: Vector2D, height: float) -> bool:
        # Check if from point p towards sun direction (inverse shadow_direction) there is segmentation on the elevated building segment
        # Because buildings are extruded vertically, shadow is cast on ground in direction opposite sun.
        # For 2D problem, we check if between p and sun in XY plane there is building segment with height sufficient to block sun.
        # Sun is assumed infinitely far away, so if p and building segment project on sun line and building height blocks sun elevation, point is in shadow.
        # Given problem states that if building lies on line from sun to point, point is in shadow

        # Vector from p back towards sun (reverse shadow direction)
        dir_sun = Vector2D(self.direction3d[0], self.direction3d[1]).normalize()

        # Check if building edge segment between seg_start and seg_end is intersected by ray from p in sun direction
        # For this problem, since sun is at infinite distance, building shadows can be checked via checking if building segment projects along that line
        # We'll use a tolerance by projecting points onto the line and checking intervals
        # To check if building segment lies on line between p and sun

        # Project segment onto line from p towards sun
        to_start = seg_start - p
        to_end = seg_end - p
        sun_dir = dir_sun

        # Check cross product zero (colinear) with sun_dir
        cross_start = sun_dir.cross(to_start)
        cross_end = sun_dir.cross(to_end)
        eps = 1e-10
        if abs(cross_start) > eps or abs(cross_end) > eps:
            return False

        # Now check if seg_start or seg_end lies in front of p along sun_dir (ray)
        dot_start = to_start.dot(sun_dir)
        dot_end = to_end.dot(sun_dir)
        if dot_start <= eps and dot_end <= eps:
            return False  # segment is behind or at p

        # Also check that the segment overlaps the positive ray from p
        # Segment interval [min(dot_start,dot_end), max(dot_start,dot_end)]
        if max(dot_start,dot_end) < eps:
            return False

        # If segment overlaps ray, point p is in shadow for this building edge segment if height is > 0
        # Since height > 0 always for buildings, return True
        return True

class Edge:
    def __init__(self, a: Vector2D, b: Vector2D, building_height: int, building_index: int, idx_in_building: int):
        self.a = a
        self.b = b
        self.height = building_height
        self.buildi = building_index
        self.idx = idx_in_building
        self.length = a.distance_to(b)

    def as_tuple(self) -> Tuple[Vector2D, Vector2D]:
        return (self.a, self.b)

    def __repr__(self) -> str:
        return f"Edge({self.a}, {self.b}, h={self.height})"

class Graph:
    def __init__(self):
        self.nodes: List[Vector2D] = []
        self.adj: Dict[int, List[Tuple[int, float, bool]]] = {}
        # adjacency: node->list of tuples (neighbor_node, distance, shaded_bool)

    def add_node(self, p: Vector2D) -> int:
        self.nodes.append(p)
        idx = len(self.nodes)-1
        self.adj[idx] = []
        return idx

    def add_edge(self, u: int, v: int, dist: float, shaded: bool):
        self.adj[u].append((v, dist, shaded))
        self.adj[v].append((u, dist, shaded))

    def __len__(self) -> int:
        return len(self.nodes)

def point_segment_distance(p: Vector2D, a: Vector2D, b: Vector2D) -> float:
    # Distance from point p to segment ab
    ap = p - a
    ab = b - a
    ab_len2 = ab.dot(ab)
    if ab_len2 == 0:
        return ap.length()
    t = ap.dot(ab) / ab_len2
    t = max(0.0, min(1.0, t))
    proj = a + ab * t
    return (p - proj).length()

def segment_block_sun(p1: Vector2D, p2: Vector2D, buildings: List[Tuple[Polygon,int]], solar: SolarVector) -> bool:
    # Check if segment from p1 to p2 lies in building interior
    # Also we check building shadows if segment, or if segment touches building boundaries

    # We'll only allow walking outside and on boundary
    # So if segment intersects building interiors, disallow

    # But buildings don't intersect each other

    # However, shadows and sunlight depend on sun direction

    # For simplicity here, later the edges that lie on building boundaries become special with zero sun exposure

    return False # We do detailed check elsewhere

def segment_intersects_buildings(p1: Vector2D, p2: Vector2D, buildings: List[Polygon]) -> bool:
    # Check if segment intersects polygon interior
    # It's allowed to walk along polygon boundary

    for poly in buildings:
        if _segment_intersects_polygon(p1, p2, poly):
            return True
    return False

def _segment_intersects_polygon(a: Vector2D, b: Vector2D, poly: Polygon) -> bool:
    # segment intersects polygon interior or boundary excluding endpoints?
    # We accept if segment lies on polygon boundary (edges)
    # Thus, if segment crosses polygon interior, return True

    # Use simplistic approach: check segment against polygon edges for intersection except at endpoints

    for edge_start, edge_end in poly.edges:
        if (_point_compare(a, edge_start) and _point_compare(b, edge_end)) or (_point_compare(a, edge_end) and _point_compare(b, edge_start)):
            # same segment as polygon edge, allowed
            return False
        if (a == edge_start or a == edge_end or b == edge_start or b == edge_end):
            # endpoint shared, allowed
            continue
        if segments_intersect(a,b,edge_start, edge_end):
            # intersection inside at point other than vertices, segment passes polygon boundary
            # if intersection at endpoints handled above
            return True

    # Now check if midpoint is inside polygon ==> segment crosses interior
    mid = (a + b) * 0.5
    if poly.contains_point(mid):
        return True
    return False

def _point_compare(a: Vector2D, b: Vector2D) -> bool:
    return abs(a.x - b.x) < 1e-14 and abs(a.y - b.y) < 1e-14

def compute_shadow_status_on_segment(p1: Vector2D, p2: Vector2D, buildings: List[Tuple[Polygon,int]], solar_vec: SolarVector) -> bool:
    # For segment p1->p2, determine if walking on segment is shaded or sunlit
    # According to problem, walking on building boundaries (edges) always shaded (no sun)
    # And being behind or in shadow of building is shaded
    # For other parts (walking through free space) we check line from start to sun, if blocked by building

    # We split segment into small parts to check? Inefficient but safe
    # Instead, we can check midpoint of segment to determine sun exposure

    mid = (p1 + p2) * 0.5
    # If midpoint is on building boundary -> shaded
    for poly, h in buildings:
        if poly.is_point_on_boundary(mid):
            return True

    # Check if midpoint is in shadow of at least one building

    for poly, h in buildings:
        # Check if midpoint is shadowed by building poly with height h
        # For shadow we check if midpoint is behind building from sun direction

        # Iterate building edges and test if midpoint lies in shadow cast by edge
        for i in range(len(poly.vertices)):
            a = poly.vertices[i]
            b = poly.vertices[(i+1)%len(poly.vertices)]
            if solar_vec.is_point_in_shadow_of_segment(mid, a, b, h):
                return True

    # Otherwise sunlit
    return False

def dijkstra_shortest_path(graph: Graph, start_idx: int, goal_idx: int) -> float:
    # Use Dijkstra to find minimal cumulative sun exposure length from start to goal.
    # Edges have weight = distance, and we want minimal sum of distance where sun is exposure.
    # Actually we want minimal "sun exposure feet" so weights are "distance if sunlit else 0"

    # For that we will use edge weights = distance if edge sunlit else 0
    # Find shortest total sunlit distance path between start and goal

    # Distances array store minimal sum sunlit distance from start
    dist = [math.inf] * len(graph)
    dist[start_idx] = 0.0
    pq = [(0.0, start_idx)]
    while pq:
        cur_cost, u = heapq.heappop(pq)
        if dist[u] < cur_cost - 1e-15:
            continue
        if u == goal_idx:
            return cur_cost
        for v, w, shaded in graph.adj[u]:
            add_cost = 0.0 if shaded else w
            nd = cur_cost + add_cost
            if nd + 1e-15 < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist[goal_idx]

class ICPCPlanner:
    def __init__(self):
        self.buildings: List[Tuple[Polygon,int]] = []
        self.solar: Optional[SolarVector] = None
        self.S: Optional[Vector2D] = None
        self.T: Optional[Vector2D] = None
        self.graph = Graph()

    def load_data(self, input_iter):
        self.buildings.clear()
        N_line = next(input_iter).strip()
        if N_line == "0":
            return False
        N = int(N_line)
        for _ in range(N):
            line = next(input_iter).strip()
            NV, H, *rest = map(int, line.split())
            coords = []
            while len(rest) < 2*NV:
                rest.extend(map(int, next(input_iter).strip().split()))
            for i in range(NV):
                x = rest[2*i]
                y = rest[2*i+1]
                coords.append(Vector2D(x,y))
            self.buildings.append((Polygon(coords), H))
        # Read solar angles
        theta_phi = next(input_iter).strip()
        while theta_phi == "":
            theta_phi = next(input_iter).strip()
        theta, phi = map(float, theta_phi.split())
        self.solar = SolarVector(theta, phi)
        # Read S and T
        pos_line = next(input_iter).strip()
        while pos_line == "":
            pos_line = next(input_iter).strip()
        Sx, Sy, Tx, Ty = map(float, pos_line.split())
        self.S = Vector2D(Sx, Sy)
        self.T = Vector2D(Tx, Ty)
        return True

    def build_visibility_graph(self):
        # We construct nodes placed at:
        # - S and T
        # - All building polygon vertices
        # - Potentially intersection points on edges (unlikely needed for this problem)
        # Connect edges:
        # - Between consecutive vertices along each building polygon (edges with zero sun exposure)
        # - Between all pairs of nodes that have free line of sight without crossing buildings interiors
        # Each edge is assigned with sun exposure amount according to