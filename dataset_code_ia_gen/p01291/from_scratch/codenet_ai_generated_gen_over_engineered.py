import sys
import math
from collections import deque
from typing import List, Tuple, Dict, Optional, Set, Iterator


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return f"Point({self.x},{self.y})"


class Edge:
    __slots__ = ['start', 'end']

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def intersects_segment(self, p1: Point, p2: Point) -> bool:
        """Check if this edge intersects the segment p1-p2"""
        def ccw(a: Point, b: Point, c: Point) -> bool:
            return (b - a).cross(c - a) > 0

        A, B = self.start, self.end
        return (ccw(A, p1, p2) != ccw(B, p1, p2)) and (ccw(A, B, p1) != ccw(A, B, p2))


class Polygon:
    __slots__ = ['vertices']

    def __init__(self, vertices: List[Point]):
        self.vertices = vertices

    def edges(self) -> Iterator[Edge]:
        n = len(self.vertices)
        for i in range(n):
            yield Edge(self.vertices[i], self.vertices[(i + 1) % n])

    def contains_point(self, p: Point) -> bool:
        # Winding number method for polygon contains point test
        wn = 0
        n = len(self.vertices)
        for i in range(n):
            v1 = self.vertices[i]
            v2 = self.vertices[(i + 1) % n]
            if v1.y <= p.y:
                if v2.y > p.y and (v2 - v1).cross(p - v1) > 0:
                    wn += 1
            else:
                if v2.y <= p.y and (v2 - v1).cross(p - v1) < 0:
                    wn -= 1
        return wn != 0

    def intersects_segment(self, p1: Point, p2: Point) -> bool:
        # Check if segment p1p2 intersects polygon edges or if p1 or p2 inside polygon
        if self.contains_point(p1) or self.contains_point(p2):
            return True
        for edge in self.edges():
            if edge.intersects_segment(p1, p2):
                return True
        return False


class FlowNetwork:
    __slots__ = ['graph']

    class Edge:
        __slots__ = ['to', 'rev', 'cap']

        def __init__(self, to: int, rev: int, cap: float):
            self.to = to
            self.rev = rev
            self.cap = cap

    def __init__(self, n: int):
        self.graph: List[List[FlowNetwork.Edge]] = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: float):
        forward = FlowNetwork.Edge(to, len(self.graph[to]), cap)
        backward = FlowNetwork.Edge(fr, len(self.graph[fr]), 0.0)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs_level(self, s: int, t: int, level: List[int]) -> bool:
        for i in range(len(level)):
            level[i] = -1
        queue = deque([s])
        level[s] = 0
        while queue:
            v = queue.popleft()
            for e in self.graph[v]:
                if e.cap > 1e-15 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    queue.append(e.to)
        return level[t] != -1

    def dfs_flow(self, v: int, t: int, f: float, iter_: List[int], level: List[int]) -> float:
        if v == t:
            return f
        while iter_[v] < len(self.graph[v]):
            e = self.graph[v][iter_[v]]
            if e.cap > 1e-15 and level[v] < level[e.to]:
                d = self.dfs_flow(e.to, t, min(f, e.cap), iter_, level)
                if d > 1e-15:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
            iter_[v] += 1
        return 0.0

    def max_flow(self, s: int, t: int) -> float:
        flow = 0.0
        level = [-1] * len(self.graph)
        INF = float('inf')
        while self.bfs_level(s, t, level):
            iter_ = [0] * len(self.graph)
            while True:
                f = self.dfs_flow(s, t, INF, iter_, level)
                if f <= 1e-15:
                    break
                flow += f
        return flow


class CorridorModel:
    def __init__(self, width: float, pillars: List[Polygon]):
        self.width = width
        self.pillars = pillars
        # We will create a visibility graph between special points called nodes, build residual graph,
        # then solve max-flow from bottom to top boundaries.

    def _build_horizontal_cut_lines(self) -> List[float]:
        """Extract all y coordinates of pillar vertices plus 0 and very large maxY to define horizontal bands."""
        ys = set([0.0])
        max_y = 0.0
        for p in self.pillars:
            for v in p.vertices:
                ys.add(v.y)
                max_y = max(max_y, v.y)
        ys.add(max_y + 1.0)  # add a top beyond all pillars
        return sorted(ys)

    def _build_nodes(self, horizontal_lines: List[float]) -> List[List[Point]]:
        """
        We create nodes on each horizontal line: initial corridor edges 0 and W,
        and add pillar edges intersections projected on the line.
        """
        nodes_per_line: List[List[Point]] = []
        # For each horizontal line, find segments of free space (outside pillars) in [0,W]
        for y in horizontal_lines:
            segments = self._free_segments_at_y(y)
            # We'll mark node points at segment ends and optionally intermediate points
            pts = []
            for seg in segments:
                pts.append(Point(seg[0], y))
                pts.append(Point(seg[1], y))
            # remove duplicates and sort left to right
            pts = sorted(list({(p.x, p.y): p for p in pts}.values()), key=lambda p: p.x)
            nodes_per_line.append(pts)
        return nodes_per_line

    def _free_segments_at_y(self, y: float) -> List[Tuple[float, float]]:
        """
        Return horizontal free x segments in corridor [0,W] at height y,
        excluding pillar horizontal projections.
        """
        intervals = []  # we will subtract pillar shadow intervals on this line
        corridors = [(0.0, self.width)]
        # For each pillar, get intersection intervals at line y
        for poly in self.pillars:
            xs = []
            n = len(poly.vertices)
            for i in range(n):
                a = poly.vertices[i]
                b = poly.vertices[(i + 1) % n]
                # Check if the segment crosses y level
                if (a.y - y) * (b.y - y) < 0:  # crosses y line
                    # Solve linear interpolation for x at y
                    x = a.x + (b.x - a.x) * (y - a.y) / (b.y - a.y)
                    xs.append(x)
                elif abs(a.y - y) < 1e-15 and abs(b.y - y) < 1e-15:
                    # horizontal edge on y line, include interval between a.x and b.x
                    xs.append(a.x)
                    xs.append(b.x)
            xs.sort()
            # xs should be even number of points, pairs define pillar shadow intervals on y
            for i in range(0, len(xs) - 1, 2):
                left = xs[i]
                right = xs[i + 1]
                intervals.append((left, right))
        if not intervals:
            return corridors
        # Merge pillar intervals
        intervals.sort()
        merged = []
        cur_left, cur_right = intervals[0]
        for li, ri in intervals[1:]:
            if li <= cur_right + 1e-15:
                cur_right = max(cur_right, ri)
            else:
                merged.append((cur_left, cur_right))
                cur_left, cur_right = li, ri
        merged.append((cur_left, cur_right))
        # Subtract merged intervals from corridor
        free_segments = []
        left = 0.0
        for li, ri in merged:
            if li > left + 1e-15:
                free_segments.append((left, min(li, self.width)))
            left = max(left, ri)
        if left < self.width - 1e-15:
            free_segments.append((left, self.width))
        # Filter invalid segments (length < 1e-14)
        free_segments = [(l, r) for l, r in free_segments if r - l > 1e-14]
        return free_segments if free_segments else corridors

    def _can_connect(self, p1: Point, p2: Point) -> bool:
        # Check segment p1p2 does not intersect any pillar or walls (except if at corridor edges at x=0 or x=W)
        if p1.x < -1e-10 or p1.x > self.width + 1e-10:
            return False
        if p2.x < -1e-10 or p2.x > self.width + 1e-10:
            return False
        segment = (p1, p2)
        for poly in self.pillars:
            if poly.intersects_segment(p1, p2):
                return False
        return True

    def build_flow_network(self) -> Tuple[FlowNetwork, int, int]:
        """
        Construct the flow network graph from the corridor model:
        Each node splits in two vertices (in,out) with capacity the length of free horizontal segment.
        Vertical edges have infinite capacity.
        Source is a special node connected to all bottom line nodes.
        Sink is connected from all top line nodes.
        """
        lines = self._build_horizontal_cut_lines()
        nodes_per_line = self._build_nodes(lines)

        node_id_map: Dict[Tuple[int, int], int] = {}
        # We'll assign id to each in and out vertex of each point
        # in vertex = 2* id, out vertex = 2* id + 1
        id_counter = 0
        for i, nodes in enumerate(nodes_per_line):
            for j, p in enumerate(nodes):
                node_id_map[(i, j)] = id_counter
                id_counter += 1

        # Create flow network with 2 vertices per node for splitting capacity
        n = id_counter * 2 + 2
        network = FlowNetwork(n)
        SRC = n - 2
        SNK = n - 1

        # Add edges for splitting nodes (in->out) with capacity equal to segment length between neighbors on same line
        for i, nodes in enumerate(nodes_per_line):
            # nodes describe points where free segments start/end
            # capacity of node: segment length right of the point on line i
            # For a pair of consecutive points (nodes[j], nodes[j+1]) the free horizontal segment length is nodes[j+1].x - nodes[j].x
            for j in range(len(nodes)):
                node_id = node_id_map[(i, j)]
                # Find capacity: for point j the out capacity is horizontal free length from this point to next on same line if any
                cap = 0.0
                if j + 1 < len(nodes):
                    cap = nodes[j + 1].x - nodes[j].x
                    if cap < 0:
                        cap = 0
                if cap > 1e-15:
                    # Add edge in->out with capacity = segment length
                    network.add_edge(node_id * 2, node_id * 2 + 1, cap)
                else:
                    # If no capacity segment, still add infinite capacity edge to allow vertical edge?
                    network.add_edge(node_id * 2, node_id * 2 + 1, 0.0)

        # Add vertical edges (out of a node line i to in of node line i+1) if visible (no pillar)
        for i in range(len(nodes_per_line) - 1):
            line_a = nodes_per_line[i]
            line_b = nodes_per_line[i + 1]
            idx_map_b = {round(p.x, 8): j for j, p in enumerate(line_b)}  # to quickly find nodes by x
            for j_a, p_a in enumerate(line_a):
                out_a = node_id_map[(i, j_a)] * 2 + 1
                # Vertical connections only between nodes with same x (to keep graph sane)
                # Because free segments may differ between horizontal lines,
                # connect nodes with same x if segment is free and vertical segment p_a->p_b is free
                # Actually, we connect all pairs where segment p_a->p_b is free provided p_b in next line
                # but trying only same x points (precision required)
                x_key = round(p_a.x, 8)
                if x_key in idx_map_b:
                    j_b = idx_map_b[x_key]
                    p_b = line_b[j_b]
                    in_b = node_id_map[(i + 1, j_b)] * 2
                    if self._can_connect(p_a, p_b):
                        network.add_edge(out_a, in_b, float('inf'))

        # Connect source to all bottom line nodes' in vertex
        for j, p in enumerate(nodes_per_line[0]):
            nodeid = node_id_map[(0, j)] * 2
            network.add_edge(SRC, nodeid, float('inf'))

        # Connect all top line nodes' out vertex to sink
        top_index = len(nodes_per_line) - 1
        for j, p in enumerate(nodes_per_line[top_index]):
            nodeid = node_id_map[(top_index, j)] * 2 + 1
            network.add_edge(nodeid, SNK, float('inf'))

        return network, SRC, SNK


def read_datasets() -> Iterator[Tuple[float, List[Polygon]]]:
    input_iter = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            line = next(input_iter)
            if line == "0 0":
                break
            W, N = map(int, line.split())
            pillars = []
            for _ in range(N):
                M = int(next(input_iter))
                vertices = []
                for __ in range(M):
                    x, y = map(float, next(input_iter).split())
                    vertices.append(Point(x, y))
                pillars.append(Polygon(vertices))
            yield W, pillars
        except StopIteration:
            break


def main() -> None:
    for W, pillars in read_datasets():
        model = CorridorModel(W, pillars)
        flownet, SRC, SNK = model.build_flow_network()
        res = flownet.max_flow(SRC, SNK)
        print(f"{res:.8f}")


if __name__ == '__main__':
    main()