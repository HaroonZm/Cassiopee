import math
from collections import defaultdict, deque
from typing import List, Tuple, Optional, Dict, Set, Iterator, Callable


class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        return f'P({self.x},{self.y})'


class Segment:
    __slots__ = ('start', 'end')
    
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def length(self) -> float:
        return self.start.distance_to(self.end)
    
    def contains_point(self, p: Point) -> bool:
        # Check if point p lies on segment (start-end)
        d1 = self.start.distance_to(p)
        d2 = p.distance_to(self.end)
        d = self.length()
        return abs((d1 + d2) - d) < 1e-9
    
    def intersect(self, other: 'Segment') -> Optional[Point]:
        # Compute intersection point if segments intersect (not just lines)
        p, r = self.start, Point(self.end.x - self.start.x, self.end.y - self.start.y)
        q, s = other.start, Point(other.end.x - other.start.x, other.end.y - other.start.y)
        
        r_cross_s = r.x * s.y - r.y * s.x
        if abs(r_cross_s) < 1e-14:
            # Collinear or parallel -> no intersection at a single point
            return None
        
        q_minus_p = Point(q.x - p.x, q.y - p.y)
        t = (q_minus_p.x * s.y - q_minus_p.y * s.x) / r_cross_s
        u = (q_minus_p.x * r.y - q_minus_p.y * r.x) / r_cross_s
        
        if 0 <= t <= 1 and 0 <= u <= 1:
            # Intersection point is p + t*r
            ix = p.x + t * r.x
            iy = p.y + t * r.y
            return Point(ix, iy)
        return None
    
    def split_at_points(self, pts: List[Point]) -> List['Segment']:
        # Given points on the segment, split the segment into smaller segments in ascending order
        # Points must lie on the segment and be unique
        pts_unique = {p for p in pts if self.contains_point(p)}
        pts_unique.add(self.start)
        pts_unique.add(self.end)
        
        # Sort points along the segment by distance from start
        points_sorted = sorted(pts_unique, key=lambda p: self.start.distance_to(p))
        
        segments = []
        for i in range(len(points_sorted) - 1):
            a, b = points_sorted[i], points_sorted[i+1]
            if a != b:
                segments.append(Segment(a, b))
        return segments
    
    def __repr__(self) -> str:
        return f'Segment({self.start},{self.end})'


class GraphNode:
    __slots__ = ('point', 'edges')
    
    def __init__(self, point: Point):
        self.point = point
        self.edges: List['GraphEdge'] = []
    
    def __repr__(self):
        return f'Node({self.point})'


class GraphEdge:
    __slots__ = ('from_node', 'to_node', 'length')
    
    def __init__(self, from_node: GraphNode, to_node: GraphNode):
        self.from_node = from_node
        self.to_node = to_node
        self.length = from_node.point.distance_to(to_node.point)
    
    def other(self, node: GraphNode) -> GraphNode:
        if node == self.from_node:
            return self.to_node
        elif node == self.to_node:
            return self.from_node
        else:
            raise ValueError("Node not part of this edge.")
    
    def __repr__(self):
        return f'Edge({self.from_node.point}<->{self.to_node.point}, l={self.length:.4f})'


class WaterPipeNetwork:
    """
    Represents the entire water pipe network with pipe segments split into nodes at intersections
    and valves, source, and repair points.
    Provides functionality to build a graph, identify valves, and run min-cut to find minimal 
    pipe length cut to isolate repairing point from source.
    """
    def __init__(self):
        self.pipe_segments: List[Segment] = []
        self.valve_points: Set[Point] = set()
        self.source_point: Optional[Point] = None
        self.repair_point: Optional[Point] = None
        self.graph_nodes: Dict[Point, GraphNode] = {}
        self.adjacency: Dict[GraphNode, List[GraphEdge]] = defaultdict(list)
    
    def add_pipe_segment(self, start: Tuple[int,int], end: Tuple[int,int]):
        self.pipe_segments.append(Segment(Point(*start), Point(*end)))
    
    def add_valve(self, x: int, y: int):
        self.valve_points.add(Point(x,y))
    
    def set_source(self, x: int, y: int):
        self.source_point = Point(x,y)
    
    def set_repairing_point(self, x: int, y: int):
        self.repair_point = Point(x,y)
    
    def build_graph(self):
        """
        Build a graph by:
        - finding all intersection points between pipe segments,
        - splitting pipe segments at intersection points, valve points, source and repair points,
        - creating graph nodes for each distinct point,
        - connecting nodes with edges representing pipe lengths.
        """
        # Gather all points to split each pipe segment: intersections, valves, source, repair
        all_special_points = set(self.valve_points)
        if self.source_point is not None:
            all_special_points.add(self.source_point)
        if self.repair_point is not None:
            all_special_points.add(self.repair_point)
        
        intersections_map: Dict[int, Set[Point]] = defaultdict(set)
        
        # Find intersections between segments
        for i, seg1 in enumerate(self.pipe_segments):
            intersections_map[i].add(seg1.start)
            intersections_map[i].add(seg1.end)
        n = len(self.pipe_segments)
        for i in range(n):
            for j in range(i+1, n):
                ipt = self.pipe_segments[i].intersect(self.pipe_segments[j])
                if ipt:
                    intersections_map[i].add(ipt)
                    intersections_map[j].add(ipt)
        
        # Add all valves and special points that lie on each pipe segment
        for i, seg in enumerate(self.pipe_segments):
            for p in all_special_points:
                if seg.contains_point(p):
                    intersections_map[i].add(p)
        
        # Split each pipe segment into smaller segments on intersection/valves/source/repair points
        subdivided_segments: List[Segment] = []
        for i, seg in enumerate(self.pipe_segments):
            points_for_seg = list(intersections_map[i])
            splits = seg.split_at_points(points_for_seg)
            subdivided_segments.extend(splits)
        
        # Create nodes for all unique points of subdivided segments
        unique_points: Set[Point] = set()
        for seg in subdivided_segments:
            unique_points.add(seg.start)
            unique_points.add(seg.end)
        
        # Create graph nodes indexed by Point
        self.graph_nodes = {p: GraphNode(p) for p in unique_points}
        
        # Create edges (bidirectional) between nodes of subdivided segments
        for seg in subdivided_segments:
            n1 = self.graph_nodes[seg.start]
            n2 = self.graph_nodes[seg.end]
            edge1 = GraphEdge(n1, n2)
            # Connect both ways in adjacency list
            self.adjacency[n1].append(edge1)
            self.adjacency[n2].append(edge1)
            n1.edges.append(edge1)
            n2.edges.append(edge1)
    
    def find_closest_node(self, point: Point) -> GraphNode:
        # The point is expected to be exactly a node, or this method assumes so
        node = self.graph_nodes.get(point)
        if node is None:
            raise RuntimeError(f"Point {point} not found in graph nodes.")
        return node
    
    def min_cut_between_source_and_repair(self) -> float:
        """
        Calculate the minimal sum of edge lengths that must be cut to isolate repair point from source.
        Valve nodes are considered as potential cut points that can be closed.
        The problem reduces to a min s-t cut in an undirected weighted graph but edges represent pipes.
        We want to cut edges at valves or pipe segments adjacent to valves.
        
        Strategy:
        - Build a flow network with capacities = lengths on edges.
        - "Valve nodes" will have infinite capacity "cut" ability (they can separate flow by cutting edges adjacent).
        - But since problem states stop valves stop flow on the pipe segment they lie on,
          the minimal segment length to cut corresponds to min edge set separating source and repair that can be cut by closing valves.
        
        Approach:
        - Split each node into two with capacity (inf if valve else inf or 0) to model node cuts.
        - Edges keep capacity corresponding to pipe length.
        - Run min cut between source and repair nodes.
        
        But the problem states valves are points on segments; closing valve stops water beyond that point.
        So valve "nodes" can be considered as cut points with zero cost to close valve (cost not length).
        But cutting edges adjacent to valve stops the water.
        Minimizing total length of pipes cut means cutting edges (with valve ability where we can stop water).
        
        We simulate valve closures as infinite capacity cuts at those points,
        allowing to cut the network at those nodes at effectively zero "pipe length cost".
        
        The minimal length cut is minimal sum of pipe segments cut to isolate source from repair, 
        respecting valve cutting positions.
        
        Implement Stoer-Wagner global min cut is complex here because graph is undirected weighted.
        
        We'll model the problem as a flow network:
        - To model valve points: split vertex into in/out with infinite capacity to "close" valve safely.
        - To model pipe edges: capacity equal pipe length.
        
        Then run min-cut max-flow from source to repair.
        """
        # Build flow network
        # Each node: split into node_in and node_out
        # Capacity node_in->node_out = inf if valve node else inf, to allow cutting nodes if valve
        
        # Edges between node_out to neighbor node_in with capacity = pipe length
        
        # For simplicity, only valve nodes get node_in->node_out capacity = inf,
        # other nodes have node_in->node_out capacity = inf to allow cutting edge mostly via edges.
        
        # Build node mapping for node_in and node_out indexing
        
        # Assign indices for nodes
        node_list = list(self.graph_nodes.values())
        node_index = {node: idx for idx,node in enumerate(node_list)}
        N = len(node_list)
        
        graph = FlowNetwork(2*N)
        
        def node_in(i): return i
        def node_out(i): return i + N
        
        INF = 10**15
        
        valve_points_set = self.valve_points
        
        # Build node split edges
        for i,node in enumerate(node_list):
            # Node capacity: infinite for all (to allow edge cuts)
            # Valve nodes could be modelled specifically if needed
            graph.add_edge(node_in(i), node_out(i), INF)
        
        # Build edges between node_out and neighbor node_in with capacity pipe length
        # As the graph is undirected, add edges both ways
        for node in node_list:
            i = node_index[node]
            for edge in node.edges:
                other = edge.other(node)
                j = node_index[other]
                # Add edge from node_out(i) to node_in(j)
                graph.add_edge(node_out(i), node_in(j), edge.length)
        
        # Define source and sink
        try:
            source_node = self.graph_nodes[self.source_point]
            sink_node = self.graph_nodes[self.repair_point]
        except Exception:
            return -1
        
        s = node_out(node_index[source_node])
        t = node_in(node_index[sink_node])
        
        max_flow = graph.max_flow(s, t)
        
        # If max_flow >= INF/10 then no finite cut exists -> print -1
        if max_flow >= INF/10:
            return -1
        return max_flow


class FlowEdge:
    __slots__ = ('to', 'rev', 'capacity', 'original_capacity')
    def __init__(self, to: int, rev: int, capacity: float):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.original_capacity = capacity


class FlowNetwork:
    """
    Dinic max flow implementation to handle floating point capacities.
    """
    def __init__(self, n: int):
        self.n = n
        self.graph: List[List[FlowEdge]] = [[] for _ in range(n)]
    
    def add_edge(self, fr: int, to: int, capacity: float):
        forward = FlowEdge(to, len(self.graph[to]), capacity)
        backward = FlowEdge(fr, len(self.graph[fr]), 0.0)
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
                if e.capacity > 1e-14 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    queue.append(e.to)
        return level[t] >= 0
    
    def dfs_flow(self, v: int, t: int, f: float, level: List[int], iter_: List[int]) -> float:
        if v == t:
            return f
        while iter_[v] < len(self.graph[v]):
            e = self.graph[v][iter_[v]]
            if e.capacity > 1e-14 and level[v] < level[e.to]:
                d = self.dfs_flow(e.to, t, min(f, e.capacity), level, iter_)
                if d > 1e-14:
                    e.capacity -= d
                    self.graph[e.to][e.rev].capacity += d
                    return d
            iter_[v] += 1
        return 0.0
    
    def max_flow(self, s: int, t: int) -> float:
        flow = 0.0
        level = [-1]*self.n
        INF = 1e18
        while self.bfs_level(s, t, level):
            iter_ = [0]*self.n
            while True:
                f = self.dfs_flow(s, t, INF, level, iter_)
                if f < 1e-14:
                    break
                flow += f
        return flow


def read_ints() -> List[int]:
    return list(map(int, input().split()))

def main():
    N, M = read_ints()
    network = WaterPipeNetwork()
    
    for _ in range(N):
        x_s, y_s, x_d, y_d = read_ints()
        network.add_pipe_segment((x_s, y_s), (x_d, y_d))
    for _ in range(M):
        x_v, y_v = read_ints()
        network.add_valve(x_v, y_v)
    x_b, y_b = read_ints()
    network.set_source(x_b, y_b)
    x_c, y_c = read_ints()
    network.set_repairing_point(x_c, y_c)
    
    network.build_graph()
    result = network.min_cut_between_source_and_repair()
    if result < 0:
        print(-1)
    else:
        print(f"{result:.6f}")

if __name__ == "__main__":
    main()