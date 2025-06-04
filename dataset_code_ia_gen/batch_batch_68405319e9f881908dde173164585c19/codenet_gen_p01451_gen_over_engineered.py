import sys
import math
from typing import List, Tuple, Protocol, runtime_checkable, Optional

@runtime_checkable
class PointProtocol(Protocol):
    x: float
    y: float

class Point(PointProtocol):
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def distance_to(self, other: 'PointProtocol') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)
    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

class GraphEdge:
    __slots__ = ('start', 'end', 'weight')
    def __init__(self, start: int, end: int, weight: float):
        self.start = start
        self.end = end
        self.weight = weight
    def __lt__(self, other: 'GraphEdge'):
        return self.weight < other.weight
    def __repr__(self) -> str:
        return f"Edge({self.start}-{self.end}: {self.weight})"

class DisjointSetUnion:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a: int, b: int) -> bool:
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return False
        if self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = b_root
        else:
            self.parent[b_root] = a_root
            if self.rank[a_root] == self.rank[b_root]:
                self.rank[a_root] += 1
        return True
    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

class MinimalTotalRoadLengthCalculator:
    def __init__(self, points: List[Point], source_idx: int, target_idx: int):
        self.points = points
        self.source_idx = source_idx
        self.target_idx = target_idx
        self.n = len(points)
    def construct_complete_graph_edges(self) -> List[GraphEdge]:
        edges = []
        for i in range(self.n):
            p_i = self.points[i]
            for j in range(i+1, self.n):
                p_j = self.points[j]
                dist = p_i.distance_to(p_j)
                edges.append(GraphEdge(i, j, dist))
        return edges
    def minimum_spanning_tree_with_path_check(self) -> Optional[float]:
        # Compute MST with Kruskal
        edges = self.construct_complete_graph_edges()
        edges.sort()
        dsu = DisjointSetUnion(self.n)
        mst_weight = 0.0
        mst_adj = [[] for _ in range(self.n)]
        # Build MST
        edges_used = 0
        for e in edges:
            if dsu.union(e.start, e.end):
                mst_weight += e.weight
                mst_adj[e.start].append(e.end)
                mst_adj[e.end].append(e.start)
                edges_used += 1
                if edges_used == self.n - 1:
                    break
        if not dsu.connected(self.source_idx, self.target_idx):
            # No path in MST from source to target, no solution
            return None
        # Now check path length from source to target along MST edges
        # Find shortest path length (actually MST edges form a tree, so unique path)
        visited = [False]*self.n
        path_length = [0.0]*self.n
        def dfs(current: int, parent: int) -> bool:
            if current == self.target_idx:
                return True
            visited[current] = True
            for nxt in mst_adj[current]:
                if nxt == parent:
                    continue
                if not visited[nxt]:
                    path_length[nxt] = path_length[current] + self.points[current].distance_to(self.points[nxt])
                    if dfs(nxt, current):
                        return True
            return False
        path_length[self.source_idx] = 0.0
        dfs(self.source_idx, -1)
        return mst_weight, path_length[self.target_idx]

class IntersectionUtil:
    @staticmethod
    def segments_intersect(p1: PointProtocol, p2: PointProtocol, q1: PointProtocol, q2: PointProtocol) -> bool:
        # Uses orientation testing
        def orientation(a: PointProtocol, b: PointProtocol, c: PointProtocol) -> int:
            # >0 ccw, <0 cw, 0 colinear
            val = (b.y - a.y)*(c.x - b.x) - (b.x - a.x)*(c.y - b.y)
            if val > 0:
                return 1
            elif val < 0:
                return 2
            return 0
        o1 = orientation(p1, p2, q1)
        o2 = orientation(p1, p2, q2)
        o3 = orientation(q1, q2, p1)
        o4 = orientation(q1, q2, p2)
        if o1 != o2 and o3 != o4:
            return True
        return False

class Path:
    def __init__(self, node_order: List[int], points: List[Point]):
        self.node_order = node_order
        self.points = points
    def edges(self) -> List[Tuple[Point, Point]]:
        return [(self.points[self.node_order[i]], self.points[self.node_order[i+1]]) for i in range(len(self.node_order)-1)]

class RoadNetwork:
    def __init__(self, points: List[Point]):
        self.points = points
        self.n = len(points)
        self.edges: List[GraphEdge] = []
        self.adj: List[List[int]] = [[] for _ in range(self.n)]
    def build_complete_edges(self):
        self.edges.clear()
        for i in range(self.n):
            p_i = self.points[i]
            for j in range(i+1, self.n):
                p_j = self.points[j]
                dist = p_i.distance_to(p_j)
                self.edges.append(GraphEdge(i, j, dist))
    def build_min_network(self) -> Tuple[List[List[int]], float]:
        self.build_complete_edges()
        self.edges.sort()
        dsu = DisjointSetUnion(self.n)
        self.adj = [[] for _ in range(self.n)]
        total = 0.0
        edge_count = 0
        for e in self.edges:
            if dsu.union(e.start, e.end):
                total += e.weight
                self.adj[e.start].append(e.end)
                self.adj[e.end].append(e.start)
                edge_count +=1
                if edge_count == self.n - 1:
                    break
        return self.adj, total
    def shortest_path_edges_order(self, start: int, goal: int) -> Optional[List[int]]:
        # BFS traversal to find unique path on tree
        from collections import deque
        parents = [-1]*self.n
        q = deque([start])
        found = False
        while q and not found:
            current = q.popleft()
            if current == goal:
                found = True
                break
            for nxt in self.adj[current]:
                if parents[nxt] == -1 and nxt != start:
                    parents[nxt] = current
                    q.append(nxt)
        if not found:
            return None
        # Reconstruct path
        path = []
        cur = goal
        while cur != -1:
            path.append(cur)
            cur = parents[cur]
        path.reverse()
        return path

class SophisticatedSolver:
    def __init__(self,
                 tata_points: List[Point],
                 tsutete_points: List[Point]):
        self.tata = tata_points
        self.tsutete = tsutete_points
        self.na = len(tata_points)
        self.nb = len(tsutete_points)
    def solve(self) -> float:
        # Compute MST and path for Totata
        tata_network = RoadNetwork(self.tata)
        tata_network.build_min_network()
        tata_path = tata_network.shortest_path_edges_order(0,1)
        if tata_path is None:
            return -1

        # Compute MST and path for Tsutete
        tsutete_network = RoadNetwork(self.tsutete)
        tsutete_network.build_min_network()
        tsutete_path = tsutete_network.shortest_path_edges_order(0,1)
        if tsutete_path is None:
            return -1

        # Extract paths edges as segments in global coords
        def path_segments(points: List[Point], path_nodes: List[int]) -> List[Tuple[Point, Point]]:
            return [(points[path_nodes[i]], points[path_nodes[i+1]]) for i in range(len(path_nodes)-1)]
        tata_segments = path_segments(self.tata, tata_path)
        tsutete_segments = path_segments(self.tsutete, tsutete_path)

        # We need to check if any pair of segments (one from tata, one from tsutete)
        # intersect when considered in the full 2D coordinate system (note these are disjoint sets,
        # so their global coordinates do not overlap)
        # but we need to check intersection of any such pairs as per problem statement.
        # Since they live in different coordinate sets, no sharing of nodes,
        # but intersection between their paths might be possible.

        # Actually: Since their coordinates sets are disjoint (totata and tsutete points),
        # roads connections are within their groups only. The problem states:
        # "トタタ族が通る道とツテテ族が通る道を交差させることはできない。"
        # So the paths' segments cannot intersect.

        # We must check for intersections between segments of the two paths.

        # Because no points overlap, intersection can only happen if segments cross visually.
        # So we just check all pairs of segments.

        for sa in tata_segments:
            for sb in tsutete_segments:
                if IntersectionUtil.segments_intersect(sa[0], sa[1], sb[0], sb[1]):
                    return -1

        # If no intersections found, sum MST lengths
        # MST provides minimal total length of roads for each tribe, fulfilling connectivity.
        total_length = 0.0
        # Compute Tata MST length
        for i in range(self.na):
            for j in tata_network.adj[i]:
                if i < j:
                    total_length += self.tata[i].distance_to(self.tata[j])
        # Compute Tsutete MST length
        for i in range(self.nb):
            for j in tsutete_network.adj[i]:
                if i < j:
                    total_length += self.tsutete[i].distance_to(self.tsutete[j])

        return total_length

def parse_input() -> Tuple[List[Point], List[Point]]:
    input_data = sys.stdin.read().strip().split()
    NA = int(input_data[0])
    NB = int(input_data[1])
    offset = 2
    tata_points = []
    for i in range(NA):
        x = int(input_data[offset + 2*i])
        y = int(input_data[offset + 2*i + 1])
        tata_points.append(Point(x,y))
    offset += 2*NA
    tsutete_points = []
    for i in range(NB):
        x = int(input_data[offset + 2*i])
        y = int(input_data[offset + 2*i + 1])
        tsutete_points.append(Point(x,y))
    return tata_points, tsutete_points

def main():
    tata_points, tsutete_points = parse_input()
    solver = SophisticatedSolver(tata_points, tsutete_points)
    result = solver.solve()
    if result < 0:
        print(-1)
    else:
        print(f"{result:.12f}")

if __name__ == "__main__":
    main()