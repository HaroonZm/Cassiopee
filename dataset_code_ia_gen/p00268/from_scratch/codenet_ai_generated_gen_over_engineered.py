from collections import deque, defaultdict
from typing import List, Tuple, Dict, Set, Optional

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Wall:
    def __init__(self, p1: int, p2: int):
        self.p1 = p1
        self.p2 = p2
    
    def endpoints(self) -> Tuple[int, int]:
        return (self.p1, self.p2)
    
    def __repr__(self):
        return f"Wall({self.p1},{self.p2})"

class Polygon:
    def __init__(self, vertices: List[Point]):
        self.vertices = vertices

    def edges(self) -> List[Tuple[Point, Point]]:
        edges = []
        n = len(self.vertices)
        for i in range(n):
            edges.append((self.vertices[i], self.vertices[(i+1)%n]))
        return edges

class Graph:
    """Undirected graph representing adjacency of pillars and wall connectivity."""
    def __init__(self, size: int):
        self.size = size
        self.edges: Dict[int, Set[int]] = defaultdict(set)
    
    def add_edge(self, u: int, v: int):
        self.edges[u].add(v)
        self.edges[v].add(u)
    
    def neighbors(self, u: int) -> Set[int]:
        return self.edges[u]

class RoomGraph:
    """
    Represents the connectivity graph of rooms including exterior.
    Nodes represent rooms or exterior.
    Edges represent walls with a hole (allows passage).
    """
    def __init__(self):
        self.region_count = 0
        self.region_map: Dict[int, str] = {}  # region index to type ('room' or 'outside')
        self.adj: Dict[int, Set[int]] = defaultdict(set)  # adjacency between regions
    
    def add_region(self, region_id: int, region_type: str):
        self.region_map[region_id] = region_type
    
    def add_edge(self, r1: int, r2: int):
        self.adj[r1].add(r2)
        self.adj[r2].add(r1)
    
    def neighbors(self, r: int) -> Set[int]:
        return self.adj[r]

# Utility for computational geometry

def ccw(a: Point, b: Point, c: Point) -> int:
    """Counter Clockwise test (cross product sign)"""
    area2 = (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)
    if area2 > 0:
        return 1
    elif area2 < 0:
        return -1
    else:
        return 0

def is_point_in_polygon(p: Point, polygon: Polygon) -> bool:
    """Ray casting algorithm for point-in-polygon. Polygon is convex here."""
    # For convex polygon, check all cross products have the same sign
    n = len(polygon.vertices)
    sign = None
    for i in range(n):
        a = polygon.vertices[i]
        b = polygon.vertices[(i+1) % n]
        res = ccw(a, b, p)
        if res == 0:
            # On boundary
            return True
        if sign is None:
            sign = res
        else:
            if sign != res:
                return False
    return True

def line_intersection(a1: Point, a2: Point, b1: Point, b2: Point) -> Optional[Point]:
    """Returns intersection point of segments a1a2 and b1b2 if they intersect."""
    dx1 = a2.x - a1.x
    dy1 = a2.y - a1.y
    dx2 = b2.x - b1.x
    dy2 = b2.y - b1.y

    denom = dx1*dy2 - dy1*dx2
    if denom == 0:
        return None  # parallel

    dx3 = b1.x - a1.x
    dy3 = b1.y - a1.y

    t1 = (dx3*dy2 - dy3*dx2)/denom
    t2 = (dx3*dy1 - dy3*dx1)/denom

    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        return Point(a1.x + t1*dx1, a1.y + t1*dy1)
    return None


class FloorPlan:
    def __init__(self, pillars: List[Point], walls: List[Wall]):
        self.pillars = pillars
        self.walls = walls
        self.C = len(pillars)
        self.W = len(walls)
        self.graph = Graph(self.C)
        for w in walls:
            self.graph.add_edge(w.p1 - 1, w.p2 - 1)  # zero-based index
        self.outer_polygon = Polygon(pillars)
        self.region_labels: List[int] = []
        self.edge_to_regions: Dict[int, Tuple[int, int]] = {}
        self.region_graph = RoomGraph()
    
    def find_regions(self):
        """
        Partition the plane into regions (rooms and outside).
        Each region is a node in the region graph.
        Assign IDs to each region.
        The outside region is region 0.
        """
        # This is a planar graph dual construction.
        # To find faces (regions), use DCEL or face-finding method.
        # Here we implement a half-edge approach to find faces.

        # Build adjacency with edges uniquely identified (min,max)
        edge_map = {}
        adj = defaultdict(set)
        for w in self.walls:
            u = w.p1 - 1
            v = w.p2 - 1
            adj[u].add(v)
            adj[v].add(u)
            edge_map[(min(u,v), max(u,v))] = w

        # Order adjacency by polar angle for each vertex
        # to walk around faces in CCW order
        ordered_adj = {}
        for u in range(self.C):
            neighbors = list(adj[u])
            origin = self.pillars[u]
            def angle(v):
                p = self.pillars[v]
                return (p.y - origin.y, p.x - origin.x) # We use atan2 but comparison ops
            neighbors.sort(key=lambda n: (-(self.pillars[n].y - origin.y)/(abs(self.pillars[n].x - origin.x)+1e-12) if self.pillars[n].x - origin.x != 0 else float('inf'), self.pillars[n].x))
            ordered_adj[u] = neighbors
        
        # Build half-edges data
        class HalfEdge:
            def __init__(self, origin: int, twin=None, nexthe=None, face=None):
                self.origin = origin
                self.twin = twin
                self.next = nexthe
                self.face = face
            def __repr__(self):
                return f"HalfEdge(origin={self.origin})"

        # Create all half edges (both directions)
        half_edges = {}
        for (u, v) in edge_map.keys():
            he_uv = HalfEdge(u)
            he_vu = HalfEdge(v)
            he_uv.twin = he_vu
            he_vu.twin = he_uv
            half_edges[(u,v)] = he_uv
            half_edges[(v,u)] = he_vu

        # Set next of each half edge (to form cycles for faces)
        for u in range(self.C):
            neighbors = ordered_adj[u]
            n = len(neighbors)
            for i, v in enumerate(neighbors):
                # half edge from u to v
                he = half_edges[(u,v)]

                # Find next half edge: from v to w, where w is neighbor of v just after u in CCW order
                neighbors_v = ordered_adj[v]
                idx = neighbors_v.index(u)
                w = neighbors_v[(idx - 1) % len(neighbors_v)]  # Previous neighbor (CCW)
                he.next = half_edges[(v,w)]

        # Find faces by traversing half edges not assigned a face
        faces = []
        visited = set()
        for he in half_edges.values():
            if he.face is not None:
                continue
            face_verts = []
            current = he
            while True:
                face_verts.append(current.origin)
                current.face = len(faces)
                current = current.next
                if current == he:
                    break
            faces.append(face_verts)

        # Determine which face is outside (biggest polygon area or contains a point outside)
        def polygon_area(indices: List[int]) -> float:
            pts = [self.pillars[i] for i in indices]
            area = 0
            n = len(pts)
            for i in range(n):
                j = (i+1)%n
                area += pts[i].x*pts[j].y - pts[j].x*pts[i].y
            return abs(area)/2

        # Approx guess: The outside face is the one with the largest area
        areas = [polygon_area(face) for face in faces]
        outside_face_index = areas.index(max(areas))

        # Map face index to region IDs, outside is 0
        self.region_graph = RoomGraph()
        for idx, face in enumerate(faces):
            rtype = 'outside' if idx == outside_face_index else 'room'
            self.region_graph.add_region(idx, rtype)

        # For each wall (edge), find which two faces are adjacent.
        # Every edge belongs to two faces (twins half edges)
        # So from half_edges, we assign edge to two faces
        for (u,v), he in half_edges.items():
            f1 = he.face
            f2 = he.twin.face
            if f1 != f2:
                self.region_graph.add_edge(f1, f2)

        self.region_count = len(faces)
        self.faces = faces
        self.outside_face_index = outside_face_index

    def max_holes_to_outside(self) -> int:
        """
        Calculate maximum minimal number of holes to pass from any room to outside.
        This is max distance in terms of edges to outside in the region graph,
        computed by BFS from outside region.
        """
        dist = [-1]*self.region_count
        dist[self.outside_face_index] = 0
        queue = deque([self.outside_face_index])
        while queue:
            u = queue.popleft()
            for v in self.region_graph.neighbors(u):
                if dist[v] == -1:
                    dist[v] = dist[u]+1
                    queue.append(v)
        # For rooms (not outside), find max dist, dist is number of holes to cross
        max_dist = 0
        for idx, rtype in self.region_graph.region_map.items():
            if rtype == 'room' and dist[idx] > max_dist:
                max_dist = dist[idx]
        return max_dist

def parse_input() -> List[Tuple[List[Point], List[Wall]]]:
    datasets = []
    while True:
        line = input()
        if not line:
            break
        C, W = map(int, line.strip().split())
        if C == 0 and W == 0:
            break
        pillars = []
        for _ in range(C):
            x, y = map(int, input().split())
            pillars.append(Point(x,y))
        walls = []
        for _ in range(W):
            s, t = map(int, input().split())
            walls.append(Wall(s,t))
        datasets.append((pillars, walls))
    return datasets

def main():
    datasets = parse_input()
    for pillars, walls in datasets:
        fp = FloorPlan(pillars, walls)
        fp.find_regions()
        print(fp.max_holes_to_outside())

if __name__ == '__main__':
    main()