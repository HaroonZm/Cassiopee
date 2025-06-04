import math
from typing import List, Tuple, Set, Dict, Optional


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class Edge:
    def __init__(self, u: int, v: int, points: List[Point]):
        self.u = u
        self.v = v
        self.points = points  # [Point_u, Point_v]
        self.length = points[0].distance_to(points[1])

    def __lt__(self, other: 'Edge') -> bool:
        return self.length < other.length

    def connects(self, a: int, b: int) -> bool:
        return (self.u == a and self.v == b) or (self.u == b and self.v == a)

    def shares_endpoint_with(self, other: 'Edge') -> bool:
        return self.u == other.u or self.u == other.v or self.v == other.u or self.v == other.v


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, a: int) -> int:
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True


class VillageGraph:
    def __init__(self, points: List[Point], edges_indices: List[Tuple[int, int]]):
        self.points = points
        self.N = len(points)
        self.original_edges: List[Edge] = []
        for u, v in edges_indices:
            self.original_edges.append(Edge(u, v, [points[u], points[v]]))
        self.edge_map: Dict[Tuple[int,int], Edge] = { (min(e.u,e.v), max(e.u,e.v)): e for e in self.original_edges }

    def all_edges(self) -> List[Edge]:
        edges = []
        for i in range(self.N):
            for j in range(i+1, self.N):
                edge = Edge(i, j, [self.points[i], self.points[j]])
                edges.append(edge)
        return edges


class BoundaryConditionChecker:
    @staticmethod
    def is_inside_polygon(polygon: List[Point], a: Point, b: Point) -> bool:
        # We check if segment ab is entirely inside or on polygon boundary.
        # Because polygon is convex (convex hull), check segment is inside polygon if:
        # segment does not cross outside polygon edges.
        # Actually, for convex polygon segment ab inside iff both endpoints inside polygon, and line doesn't cross outside
        # But "the line between any two villages does not pass outside"
        # We check line ab against polygon edges for intersection excluding endpoints on polygon vertices.
        # We only need to confirm segment ab does not cross polygon exterior.
        return BoundaryConditionChecker.segment_inside_convex_polygon(polygon, a, b)

    @staticmethod
    def segment_inside_convex_polygon(polygon: List[Point], a: Point, b: Point) -> bool:
        # polygon is convex polygon represented as list of its vertices in CCW order.
        # We'll check the segment ab lies inside or on polygon boundary.
        # It is true iff for every polygon edge e, points a and b are on the same side or on the edge line.
        # So for each edge, determine the signed side of a and b.

        def cross(o: Point, p: Point, q: Point) -> float:
            return (p.x - o.x)*(q.y - o.y) - (p.y - o.y)*(q.x - o.x)

        n = len(polygon)
        for i in range(n):
            p1 = polygon[i]
            p2 = polygon[(i+1) % n]
            c_a = cross(p1, p2, a)
            c_b = cross(p1, p2, b)
            # If c_a and c_b have product <0, then a and b are on opposite sides -> segment goes outside polygon
            # If c_a == 0 or c_b == 0 => point lies on edge line, allowed.
            if c_a < -1e-14 and c_b > 1e-14:
                return False
            if c_a > 1e-14 and c_b < -1e-14:
                return False
        return True

    @staticmethod
    def polygon_has_edge(edges: List[Edge], polygon_subset: Set[int]) -> bool:
        # Checks if the polygon boundary edges all exists in edges (path subset)
        # polygon_subset are indices of polygon vertices in order.
        n = len(polygon_subset)
        ps = list(polygon_subset)
        # polygon given only as indices, polygon vertices should be sorted CCW, but this function requires a polygon order.
        # So polygon_subset must be a list in order
        # So will receive ordered polygon indices

        # For the polygon edges defined by consecutive polygon vertices in polygon_subset,
        # check if each edge exists in edges.

        edge_set = {(min(e.u,e.v), max(e.u,e.v)) for e in edges}
        for i in range(len(ps)):
            a = ps[i]
            b = ps[(i+1) % len(ps)]
            if (min(a,b), max(a,b)) not in edge_set:
                return False
        return True


class ConvexHullCalculator:
    @staticmethod
    def convex_hull(points: List[Point]) -> List[int]:
        # Returns indices of points forming the convex hull in CCW order, no duplicates.
        # Using Andrew's monotone chain algorithm.

        pts = [(p.x, p.y, i) for i, p in enumerate(points)]
        pts.sort(key=lambda x: (x[0], x[1]))

        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        hull = lower[:-1] + upper[:-1]
        # hull points in CCW order with no duplicates

        indices = [p[2] for p in hull]
        return indices


class VillageRoadPlanner:
    def __init__(self, points: List[Point], edges_indices: List[Tuple[int, int]]):
        self.graph = VillageGraph(points, edges_indices)
        self.N = len(points)
        self.original_edges = self.graph.original_edges
        self.uf_initial = UnionFind(self.N)
        for e in self.original_edges:
            self.uf_initial.union(e.u, e.v)

    def compute(self) -> float:
        # Step 1: Compute convex hull polygon of all points
        hull_indices = ConvexHullCalculator.convex_hull(self.graph.points)  # CCW order
        hull_set = set(hull_indices)

        # Step 2: Check edges on hull exist in original edges, else they need to be constructed
        # We'll build the minimal total length that includes all needed hull edges
        # Step 3: Build graph edges which are original edges or hull polygon edges (added if missing)

        # Build hull polygon edges
        hull_edges = []
        points = self.graph.points
        for i in range(len(hull_indices)):
            u = hull_indices[i]
            v = hull_indices[(i+1) % len(hull_indices)]
            e = self.graph.edge_map.get((min(u,v), max(u,v)))
            if e is None:
                # Constructed edge
                e = Edge(u, v, [points[u], points[v]])
            hull_edges.append(e)

        # Now create a union find for hull edges to enforce boundary edges
        uf = UnionFind(self.N)
        for e in hull_edges:
            uf.union(e.u, e.v)

        # Step 4: From the original edges that are not on hull, add edges that:
        # (a) do not violate the convex hull boundary condition:
        # For every pair of points u,v: the segment must be inside or on hull polygon, so check segment inside polygon condition
        # (b) maintains graph connectivity.
        # We aim to minimize total cost of edges selected including hull edges.

        # We'll generate candidate edges:
        # - mandatory hull edges
        # - original edges inside polygon satisfying condition

        # Step 5: All points are inside or on hull polygon.
        # The polygon is convex hull.
        # So any segment between points inside polygon should also be inside polygon, but problem states condition:
        # segment between any two villages shall not go outside polygon.

        # So check for each edge in original edges if segment inside polygon.

        # And also the original edges on hull must be used.

        # Step 6: Kruskal MST over all nodes with mandatory hull edges included:
        # Start uf with hull edges, then add original edges allowed ordered by length incrementally to connect all

        # Prepare the polygon points list for polygon checks
        polygon_points = [points[i] for i in hull_indices]

        # Candidate edges: original edges that are NOT hull edges, and inside polygon
        candidates: List[Edge] = []
        hull_edge_set = {(min(e.u,e.v), max(e.u,e.v)) for e in hull_edges}
        for e in self.original_edges:
            edge_key = (min(e.u,e.v), max(e.u,e.v))
            if edge_key in hull_edge_set:
                continue
            # Check inside polygon condition:
            a = points[e.u]
            b = points[e.v]
            if BoundaryConditionChecker.is_inside_polygon(polygon_points, a, b):
                candidates.append(e)
        # Also consider constructed edges on hull that are not original edges
        # these constructed hull edges: length will be added, must be mandatory

        for e in hull_edges:
            edge_key = (min(e.u,e.v), max(e.u,e.v))
            if edge_key not in self.graph.edge_map:
                candidates.append(e)

        # Sort candidates by length ascending
        candidates.sort(key=lambda e: e.length)

        # Kruskal with forced hull edges unioned first:
        for e in hull_edges:
            uf.union(e.u, e.v)

        # Add candidates to connect all
        for e in candidates:
            uf.union(e.u, e.v)

        # Verify connectivity
        roots = {uf.find(i) for i in range(self.N)}
        if len(roots) != 1:
            # Not fully connected, need to add inside edges ignoring polygon condition, or fail
            # but problem guarantees connectivity by original edges, so skip

            # But this should not happen since initial graph is connected.
            pass

        # Step 7: Now find MST that includes hull edges and stay inside polygon boundary

        # We try method: MST forced with hull edges included plus other allowed edges

        uf2 = UnionFind(self.N)
        for e in hull_edges:
            uf2.union(e.u, e.v)

        mst_edges = list(hull_edges)
        for e in candidates:
            if uf2.find(e.u) != uf2.find(e.v):
                uf2.union(e.u, e.v)
                mst_edges.append(e)

        # Final total length
        total_length = sum(e.length for e in mst_edges)

        return total_length


def main():
    import sys
    input = sys.stdin.readline

    V, R = map(int, input().split())
    points = []
    for _ in range(V):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    edges_indices = []
    for _ in range(R):
        s, t = map(int, input().split())
        edges_indices.append((s-1, t-1))

    planner = VillageRoadPlanner(points, edges_indices)
    res = planner.compute()
    print(f"{res:.10f}")


if __name__ == "__main__":
    main()