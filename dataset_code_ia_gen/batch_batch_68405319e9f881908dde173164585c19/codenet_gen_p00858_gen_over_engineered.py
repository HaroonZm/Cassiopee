from typing import List, Tuple, Dict, Set, Optional, Iterable
from math import sqrt, acos, degrees, isclose
from collections import defaultdict, deque
import heapq

# Define fundamental geometric abstractions anticipating extensions

class Point:
    __slots__ = ('x','y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point): return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def distance_to(self, other: 'Point') -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def vector_to(self, other:'Point') -> 'Vector':
        return Vector(other.x - self.x, other.y - self.y)

    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Vector:
    __slots__ = ('dx','dy')
    def __init__(self, dx: float, dy: float):
        self.dx = dx
        self.dy = dy

    def norm(self) -> float:
        return sqrt(self.dx**2 + self.dy**2)

    def dot(self, other: 'Vector') -> float:
        return self.dx*other.dx + self.dy*other.dy

    def angle_with(self, other: 'Vector') -> float:
        # Angle in degrees between 0 and 180
        # Defensive: if degenerate vector, return None
        norm1 = self.norm()
        norm2 = other.norm()
        if norm1 == 0 or norm2 == 0:
            return None
        cos_theta = self.dot(other)/(norm1*norm2)
        # Clamp to avoid floating point errors
        cos_theta = max(-1,min(1,cos_theta))
        return degrees(acos(cos_theta))

    def __repr__(self):
        return f"Vector({self.dx},{self.dy})"

class Segment:
    __slots__ = ('p1','p2')
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def length(self) -> float:
        return self.p1.distance_to(self.p2)

    def __repr__(self):
        return f"Segment({self.p1},{self.p2})"

class GraphNode:
    # Node to represent a point in the graph for pathfinding
    __slots__ = ('point','edges')
    def __init__(self, point: Point):
        self.point = point
        self.edges: List['GraphEdge'] = []

    def __repr__(self):
        return f"GraphNode({self.point})"

class GraphEdge:
    __slots__ = ('target','weight')
    def __init__(self, target: GraphNode, weight: float):
        self.target = target
        self.weight = weight

    def __repr__(self):
        return f"GraphEdge(to={self.target.point}, w={self.weight:.2f})"

# Enum-like types for roles (anticipating future extensions)
class SegmentRole:
    STREET = "street"
    SIGN = "sign"

class TrafficDirectionality:
    BIDIRECTIONAL = 0
    FORBID_FROM_ACUTE_TO_OBTUSE = 1
    FORBID_BOTH_DIRECTIONS_IF_RECTANGULAR = 2

# Core class to represent the entire map with streets and signs
class StreetMap:
    def __init__(self):
        self.segments: List[Tuple[Segment,str]] = []  # segment and role (street or sign)
        self.point_to_segments: Dict[Point, Set[Segment]] = defaultdict(set)
        self.graph_nodes: Dict[Point, GraphNode] = dict()
        self.street_segments: Set[Segment] = set()
        self.sign_segments: Set[Segment] = set()
        self.adj_matrix_directionality: Dict[Tuple[Point,Point], TrafficDirectionality] = dict()
        # For accessibility to intersections (points connected by at least 2 street segs)
        self.intersections: Set[Point] = set()

    def add_segment(self, segment: Segment, role: str):
        self.segments.append((segment, role))
        self.point_to_segments[segment.p1].add(segment)
        self.point_to_segments[segment.p2].add(segment)
        if role == SegmentRole.STREET:
            self.street_segments.add(segment)
        else:
            self.sign_segments.add(segment)

    def build_graph_and_restrictions(self):
        # Step 1: Build nodes for each point that appear on street segments
        street_points = set()
        for segment, role in self.segments:
            if role == SegmentRole.STREET:
                street_points.add(segment.p1)
                street_points.add(segment.p2)
        # Instantiate GraphNodes
        for p in street_points:
            self.graph_nodes[p] = GraphNode(p)
        # Step 2: Establish edges between points adjacent on a street (initially bidirectional)
        # We track edges in adjacency dict: Tuple[p1,p2] -> weight
        edges_bidirectional: Dict[Tuple[Point,Point], float] = dict()
        for segment in self.street_segments:
            length = segment.length()
            edges_bidirectional[(segment.p1, segment.p2)] = length
            edges_bidirectional[(segment.p2, segment.p1)] = length

        # Step 3: Determine restrictions from sign segments and remove/restrict edges accordingly
        # Prepare helper dictionaries: For each sign segment, locate the touching street segment and endpoints
        # Signs: One end touches exactly one street segment, other end is open
        # We must enforce: cars may not move from obtuse angle side to acute at the touching point,
        # or neither if angle is 90°
        # This is directional restriction at a node

        # For efficiency, map points to street segments touching them (endpoints)
        point_to_streetsegments: Dict[Point, Set[Segment]] = defaultdict(set)
        for seg in self.street_segments:
            point_to_streetsegments[seg.p1].add(seg)
            point_to_streetsegments[seg.p2].add(seg)

        # Locate the touching point for each sign, the street seg it touches and direction
        for sign_segment in self.sign_segments:
            sp1 = sign_segment.p1
            sp2 = sign_segment.p2
            # One end touches exactly one street segment
            # Identify which endpoint touches the street segment
            touching_point = None
            open_point = None
            touching_street_segment = None
            if len(point_to_streetsegments[sp1]) == 1:
                touching_point = sp1
                open_point = sp2
                touching_street_segment = next(iter(point_to_streetsegments[sp1]))
            elif len(point_to_streetsegments[sp2]) == 1:
                touching_point = sp2
                open_point = sp1
                touching_street_segment = next(iter(point_to_streetsegments[sp2]))
            else:
                # In case sign endpoint touches no or multiple street segments - invalid per spec
                continue

            # Compute the angle at touching_point between the street segment and the sign segment
            # Vector for street: from touching_point to other end of street seg
            if touching_point == touching_street_segment.p1:
                vec_street = touching_point.vector_to(touching_street_segment.p2)
            else:
                vec_street = touching_point.vector_to(touching_street_segment.p1)
            # Vector for sign segment: from touching_point to open_point
            vec_sign = touching_point.vector_to(open_point)

            angle = vec_sign.angle_with(vec_street)
            if angle is None:
                # degenerate vector
                continue

            # Determine if angle is acute or obtuse relative to street vector
            # We want to classify as:
            # direction forbidden from obtuse to acute.
            # acute angle < 90°
            # obtuse angle > 90°
            # rectangular = 90°

            # Because vector angles are unsigned, angle is between 0 and 180 degrees
            if isclose(angle, 90.0, abs_tol=1e-9):
                # 90°, forbidden both directions at touching point along street seg
                # Remove both directions on street segment edge that connects touching_point
                # to the other endpoint
                p_other = (touching_street_segment.p2 if touching_point == touching_street_segment.p1 else touching_street_segment.p1)
                if (touching_point, p_other) in edges_bidirectional:
                    del edges_bidirectional[(touching_point, p_other)]
                if (p_other, touching_point) in edges_bidirectional:
                    del edges_bidirectional[(p_other, touching_point)]
                # Mark directional restriction for clarity
                self.adj_matrix_directionality[(touching_point, p_other)] = TrafficDirectionality.FORBID_BOTH_DIRECTIONS_IF_RECTANGULAR
                self.adj_matrix_directionality[(p_other, touching_point)] = TrafficDirectionality.FORBID_BOTH_DIRECTIONS_IF_RECTANGULAR
            else:
                # Distinguish acute vs obtuse
                # Angle is between sign vector and street vector
                # We define the obtuse side as the side of street vertex with obtuse angle to sign
                # In terms of directed edges this disables moves going from obtuse side to acute side.

                # We need to determine which endpoint of the street segment corresponds to acute vs obtuse angle
                # At touching_point, angle between sign vector and street vector is 'angle'
                # The other end: the vector from other street endpoint to touching_point will form the complementary angle (180-angle)

                # Since the touching point is one endpoint of the street segment, the other end is the "other endpoint"
                p_other = (touching_street_segment.p2 if touching_point == touching_street_segment.p1 else touching_street_segment.p1)

                # Calculate vectors from the point p_other to touching_point and sign to check angles at other endpoint
                # Angle at other endpoint referencing same sign is not relevant; we only restrict movement at touching_point

                # Determine acute and obtuse endpoints:
                # acute angle at touching_point side, obtuse angle at p_other side if angle > 90 for touching_point

                # movement forbidden from obtuse side to acute side means forbidden edge from vertex with obtuse angle to vertex with acute angle
                # if angle < 90 => touching_point acute, obtuse side = p_other
                # so forbid movement p_other -> touching_point
                #
                # if angle > 90 => touching_point obtuse, acute side = p_other
                # so forbid movement touching_point -> p_other

                if angle < 90:
                    # touching_point is acute angle side
                    # forbid movement from obtuse (p_other) to acute (touching_point)
                    if (p_other, touching_point) in edges_bidirectional:
                        del edges_bidirectional[(p_other, touching_point)]
                    self.adj_matrix_directionality[(p_other, touching_point)] = TrafficDirectionality.FORBID_FROM_ACUTE_TO_OBTUSE
                else:
                    # touching_point is obtuse
                    # forbid movement from obtuse (touching_point) to acute (p_other)
                    if (touching_point, p_other) in edges_bidirectional:
                        del edges_bidirectional[(touching_point, p_other)]
                    self.adj_matrix_directionality[(touching_point, p_other)] = TrafficDirectionality.FORBID_FROM_ACUTE_TO_OBTUSE

        # Step 4: Create GraphEdges according to remaining edges_bidirectional dict
        for (src, dst), weight in edges_bidirectional.items():
            if src in self.graph_nodes and dst in self.graph_nodes:
                self.graph_nodes[src].edges.append(GraphEdge(self.graph_nodes[dst], weight))

        # Step 5: Identify street intersections: points that are endpoints of at least two street segments
        for p in street_points:
            if len(point_to_streetsegments[p]) >= 2:
                self.intersections.add(p)

    def dijkstra_shortest_path(self, start: Point, goal: Point) -> Optional[List[Point]]:
        # Standard Dijkstra with min-heap priority queue
        if start not in self.graph_nodes or goal not in self.graph_nodes:
            return None
        dist: Dict[Point,float] = {p: float('inf') for p in self.graph_nodes}
        prev: Dict[Point, Optional[Point]] = {p: None for p in self.graph_nodes}
        dist[start] = 0.0
        heap: List[Tuple[float, Point]] = [(0.0, start)]

        while heap:
            current_dist, current_point = heapq.heappop(heap)
            if current_dist > dist[current_point]:
                continue
            if current_point == goal:
                break
            current_node = self.graph_nodes[current_point]
            for edge in current_node.edges:
                neighbor_point = edge.target.point
                ndist = current_dist + edge.weight
                if ndist < dist[neighbor_point]:
                    dist[neighbor_point] = ndist
                    prev[neighbor_point] = current_point
                    heapq.heappush(heap, (ndist, neighbor_point))

        if dist[goal] == float('inf'):
            return None

        # Reconstruct path from goal to start
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        return path

    def extract_street_intersections_on_path(self, path: List[Point]) -> List[Point]:
        # Returns the points in path that are street intersections
        intersections_in_path = [p for p in path if p in self.intersections]
        # Ensure both start and goal points can be included if intersections:
        # Problem says the start and goal points are located on street endpoints. Start and goal may or may not be an intersection.
        # We include only points where at least two street segments meet (intersections)
        return intersections_in_path

class InputDataParser:
    def __init__(self, input_lines: Iterable[str]):
        self.lines = input_lines
        self.line_iter = iter(self.lines)

    def __iter__(self):
        return self

    def __next__(self):
        # parse one dataset or raise StopIteration
        while True:
            line = next(self.line_iter).strip()
            if line == '':
                continue
            if line == '0':
                raise StopIteration
            n = int(line)
            start_line = next(self.line_iter).strip()
            x_s, y_s = map(int, start_line.split())
            goal_line = next(self.line_iter).strip()
            x_g, y_g = map(int, goal_line.split())
            segments = []
            for _ in range(n):
                line_seg = next(self.line_iter).strip()
                x1,y1,x2,y2 = map(int, line_seg.split())
                segments.append( (x1,y1,x2,y2) )
            return (n, x_s, y_s, x_g, y_g, segments)

def main():
    import sys
    input_parser = InputDataParser(sys.stdin)
    for dataset in input_parser:
        n,x_s,y_s,x_g,y_g,segments_data = dataset
        street_map = StreetMap()
        # Here we must distinguish streets vs signs
        # Assumptions:
        # Streets connect points that appear more than once combined or based on problem statement:
        # In example problem, signs connect an endpoint that touches exactly one street segment and the other end is open.
        # Let's mark segments that have their endpoints with point counts:
        # We count all endpoints frequencies in all segments first to help determine signs vs streets.

        point_count: Dict[Tuple[int,int], int] = defaultdict(int)
        for x1,y1,x2,y2 in segments_data:
            point_count[(x1,y1)] += 1
            point_count[(x2,y2)] += 1

        # We define a heuristic for streets vs signs based on problem statement:
        # Endpoints of signs: one endpoint touches exactly one line segment representing a street;  
        # and other endpoint is open (probably appears only on this segment).

        # But we must initially interpret all as streets then reclassify
        # Because every segment can be street or sign, but no intersections between segments except at endpoints.

        # To distinguish:
        # 1) We assume segments with endpoints such that one endpoint appears on exactly one street segment: 
        # We'll classify those segments with an endpoint touching exactly one street segment and the other endpoint open
        # after initial pass.

        # Initial pass: all segments are streets tentatively. Then reclassify segments that look like signs:

        # We also need to know the street segments per point simultaneously.
        # Let's build a map from point to segment indices
        point_to_segs: Dict[Tuple[int,int], List[int]] = defaultdict(list)
        for i,(x1,y1,x2,y2) in enumerate(segments_data):
            point_to_segs[(x1,y1)].append(i)
            point_to_segs[(x2,y2)].append(i)

        # Let's find candidate signs:
        # Signs are segments where one endpoint touches exactly one street segment and other endpoint touches zero (?) segments other than itself
        # But initially all segments are street, so this logic must be revisited: per problem the sign endpoint touching a street segment has to appear on exactly that one street segment
        # The open endpoint appears only here

        # From problem:
        # Each end point of every street touches one or more streets, but no signs.

        # We'll iterate segments decide which are streets: if both endpoints touch >= 2 segments (or any with more than one segment), count as street segment
        # else sign

        # Because we don't know sign classification easily, alternatively
        # Idea: we know from problem that signs are line segments that do NOT intersect or overlap, that one endpoint touches ONE street segment and other end open.
        # So signs connect to exactly one street endpoint at exactly one point

        # Construct frequency of points touching segments:
        point_touch_counts = {pt: len(segs) for pt,segs in point_to_segs.items()}

        # Let's assume segments with both endpoints having point_touch_counts > 1 are streets.
        # Else sign.

        # Additionally, verify the connection rules:
        # If a segment has an endpoint with count == 1, it is a sign;

        roles = []
        for i,(x1,y1,x2,y2) in enumerate(segments_data):
            count1 = point_touch_counts[(x1,y1)]
            count2 = point_touch_counts[(x2,y2)]
            # If both endpoints appear on multiple segments => likely street
            if count1 > 1 and count2 > 1:
                roles.append(SegmentRole.STREET)
            else:
                # Else sign
                roles.append(SegmentRole.SIGN)

        # Now add the segments to the street_map with their roles
        for (x1,y