from collections import defaultdict, deque
from typing import List, Tuple, Dict, Set

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Wall:
    def __init__(self, s: int, t: int):
        self.s = s
        self.t = t

    def endpoints(self) -> Tuple[int,int]:
        return (self.s, self.t)

class Graph:
    def __init__(self, size:int):
        self.adj: Dict[int, List[int]] = defaultdict(list)
        self.size = size

    def add_edge(self, u:int, v:int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def neighbors(self, u:int) -> List[int]:
        return self.adj[u]

class Polygon:
    def __init__(self, vertices: List[Point]):
        self.vertices = vertices
    
    def edges(self) -> List[Tuple[Point, Point]]:
        evs = []
        n = len(self.vertices)
        for i in range(n):
            evs.append((self.vertices[i], self.vertices[(i+1)%n]))
        return evs

    def contains_point(self, p: Point) -> bool:
        # Ray casting algorithm for point-in-polygon test
        cnt = 0
        n = len(self.vertices)
        for i in range(n):
            a = self.vertices[i]
            b = self.vertices[(i+1)%n]
            if self._intersect_ray_horizontal(p, a, b):
                cnt += 1
        return cnt % 2 == 1
    
    def _intersect_ray_horizontal(self, p: Point, a: Point, b: Point) -> bool:
        # Check if horizontal ray rightward from p crosses segment ab
        if a.y > b.y:
            a, b = b, a
        if p.y == a.y or p.y == b.y:
            p = Point(p.x, p.y + 1e-9)  # perturb point to avoid ambiguity
        if p.y < a.y or p.y > b.y:
            return False
        if b.y - a.y == 0:
            return False
        x_int = a.x + (p.y - a.y)*(b.x - a.x)/(b.y - a.y)
        return x_int > p.x

class Room:
    def __init__(self, boundary: Polygon, id_: int):
        self.boundary = boundary
        self.id_ = id_

class FloorPlan:
    def __init__(self, pillars: List[Point], walls: List[Wall]):
        self.pillars = pillars
        self.walls = walls
        self.pillar_count = len(pillars)
        self.wall_count = len(walls)
        self.vertex_graph = Graph(self.pillar_count)
        self.construct_vertex_graph()
        self.rooms = []
        self.outer_face = None
        self.construct_faces()

    def construct_vertex_graph(self):
        for w in self.walls:
            self.vertex_graph.add_edge(w.s - 1, w.t - 1)

    def construct_faces(self):
        # Use a planar embedding algorithm to extract faces from edges
        # Here, because the polygon is convex, we can find faces by 
        # gathering cycles around vertices in CCW order.
        # We'll apply a known technique for extracting faces from planar graphs:
        # 1. For each edge, construct two half-edges (one in each direction).
        # 2. Sort adjacency in CCW order around each vertex.
        # 3. Traverse around edges in order to form faces.

        # Build adjacency with geometry info to sort neighbors CCW
        adj_ccw = []
        for v in range(self.pillar_count):
            base = self.pillars[v]
            neighbors = self.vertex_graph.neighbors(v)
            def angle(u):
                p = self.pillars[u]
                return (-(p.y - base.y), p.x - base.x)  # sort by polar angle CCW (custom)
            neighbors_sorted = sorted(neighbors, key=angle)
            adj_ccw.append(neighbors_sorted)

        # Construct half-edge structures: from v to each neighbor in adj_ccw[v]
        halfedges = dict()  # key = (u,v), value = next halfedge in CCW face cycle
        for u in range(self.pillar_count):
            nb = adj_ccw[u]
            nb_len = len(nb)
            for i, v in enumerate(nb):
                # Find the neighbor w of v such that half-edge (v,w) follows (u,v) CCW around face
                wlist = adj_ccw[v]
                # Find position of u in v's neighbor list
                try:
                    pos = wlist.index(u)
                    # Next halfedge after (u,v) is (v, wlist[(pos-1) % len])
                    w = wlist[(pos - 1) % len(wlist)]
                    halfedges[(u,v)] = (v,w)
                except ValueError:
                    # Should not happen (undirected graph)
                    pass

        visited_halfedges: Set[Tuple[int,int]] = set()
        faces = []
        for he in halfedges:
            if he in visited_halfedges:
                continue
            face = []
            cur = he
            while True:
                visited_halfedges.add(cur)
                face.append(cur[0])
                cur = halfedges[cur]
                if cur == he:
                    break
            # The face is a list of vertices (pillars) forming the polygon boundary
            # Ignore outer face for now (determine later)
            faces.append(face)

        # Identify outer face by area (face with largest area)
        polygons = []
        for f in faces:
            pts = [self.pillars[i] for i in f]
            polygons.append((f, self.polygon_area(pts)))

        polygons.sort(key=lambda x: abs(x[1]))
        # outer face assumed as polygon with largest (abs) negative area (CW polygon)
        # but if area positive, largest area is outer face
        # We define positive area as CCW orientation
        # Here, check sign for each polygon area

        # Separate outer face and rooms
        outer = None
        rooms = []
        max_area_abs = 0
        max_area_sign = None
        for f, a in polygons:
            abs_a = abs(a)
            if abs_a > max_area_abs:
                max_area_abs = abs_a
                max_area_sign = a
        # outer face area sign assumed negative or positive largest:
        # We choose face with area whose absolute value == max_area_abs
        # and matches the orientation for outer face intuitively (likely negative)
        # Here we pick the polygon with largest absolute area as outer face
        for f,a in polygons:
            if abs(a) == max_area_abs:
                outer = Polygon([self.pillars[i] for i in f])
            else:
                rooms.append(Room(Polygon([self.pillars[i] for i in f]), id_=len(self.rooms)))
                self.rooms.append(rooms[-1])

        self.outer_face = outer

    def polygon_area(self, pts: List[Point]) -> float:
        area = 0.0
        n = len(pts)
        for i in range(n):
            j = (i+1) % n
            area += pts[i].x * pts[j].y - pts[j].x * pts[i].y
        return area / 2

    def which_face_contains(self, pillar_id: int) -> int:
        # Search which face contains the pillar point (or near it)
        # But pillars are vertices, so polygon contains them
        # We assume pillar is part of that polygon vertex list
        # Each face polygon has the corresponding pillars in CCW order
        # Output the id of the room that contains that pillar

        pid = pillar_id - 1
        for room in self.rooms:
            if pid in [self.pillars.index(vertex) if vertex in self.pillars else -1 for vertex in room.boundary.vertices]:
                # polygon contains this vertex, so pillar on boundary
                # pillar belongs to this room or could belong to outer
                # But pillar on boundary shared by multiple rooms.
                # We'll pick by pillar adjacency in which room polygons.
                # Here just pick room which includes this pillar vertex
                # The problem guarantees placement inside convex polygon
                # so this approximation is enough.
                # To be more exact, check adjacency, but this suffices for problem context
                return room.id_
        return -1 # outside rooms ie outside face

class DualGraph:
    def __init__(self, floor_plan: FloorPlan):
        self.floor_plan = floor_plan
        # rooms and outer face as nodes
        # nodes: 0..num_rooms-1 for rooms, one extra for outer face
        self.n_rooms = len(floor_plan.rooms)
        self.outer_id = self.n_rooms  # outer face node
        self.adj: Dict[int, List[int]] = defaultdict(list)
        self.build_dual_graph()

    def build_dual_graph(self):
        # Build dual graph: nodes = rooms + outer face
        # edges between faces sharing a wall
        # For each wall (edge between 2 pillars), find which 2 faces it separates
        # Then add an edge between those faces in dual graph
        # We identify face on one side and face on the other side

        # To find faces adjacent to edge (u,v):
        # Each edge belongs to exactly two faces in planar graph: clockwise face and counterclockwise face
        # Using half-edge structure can help, but for simplicity, we assign faces from FloorPlan's faces.

        # We will create a mapping from pillar pairs (wall) to faces which own them.
        edge_to_faces: Dict[Tuple[int,int], List[int]] = defaultdict(list)
        for i, room in enumerate(self.floor_plan.rooms):
            verts = room.boundary.vertices
            for j in range(len(verts)):
                a = self.floor_plan.pillars.index(verts[j])
                b = self.floor_plan.pillars.index(verts[(j+1)%len(verts)])
                edge = (min(a,b), max(a,b))
                edge_to_faces[edge].append(i)
        # Add outer face edges
        outer_verts = self.floor_plan.outer_face.vertices
        for j in range(len(outer_verts)):
            a = self.floor_plan.pillars.index(outer_verts[j])
            b = self.floor_plan.pillars.index(outer_verts[(j+1)%len(outer_verts)])
            edge = (min(a,b), max(a,b))
            edge_to_faces[edge].append(self.outer_id)

        # Now build adjacency in the dual graph:
        # For each edge shared by two faces, connect them
        for edge, faces in edge_to_faces.items():
            if len(faces) == 2:
                f1, f2 = faces
                self.adj[f1].append(f2)
                self.adj[f2].append(f1)
            elif len(faces) == 1:
                # edge adjacent to only one face? should be outer face and one room so must be length 2 mostly.
                pass

    def max_dist_to_outer(self) -> int:
        # For each room node, find shortest path to outer (in edges)
        # The problem requests maximum among rooms of minimal #edges to outer
        dist = [-1]*(self.n_rooms+1)
        dist[self.outer_id] = 0
        queue = deque([self.outer_id])
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        # max dist among rooms (exclude outer)
        max_val = 0
        for i in range(self.n_rooms):
            if dist[i] > max_val:
                max_val = dist[i]
        return max_val

def read_dataset() -> Tuple[List[Point], List[Wall]]:
    import sys
    line = sys.stdin.readline()
    if not line:
        return [], []
    c_w = line.strip().split()
    if len(c_w) < 2:
        return [], []
    c, w = map(int, c_w)
    if c == 0 and w == 0:
        return [], []
    pillars = []
    for _ in range(c):
        x, y = map(int, sys.stdin.readline().strip().split())
        pillars.append(Point(x,y))
    walls = []
    for _ in range(w):
        s, t = map(int, sys.stdin.readline().strip().split())
        walls.append(Wall(s,t))
    return pillars, walls

def main():
    import sys
    sys.setrecursionlimit(10**7)
    while True:
        pillars, walls = read_dataset()
        if not pillars and not walls:
            break
        # Build floor plan representation and compute answer
        floor_plan = FloorPlan(pillars, walls)
        dual = DualGraph(floor_plan)
        ans = dual.max_dist_to_outer()
        print(ans)

if __name__ == "__main__":
    main()