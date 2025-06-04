class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"({self.x},{self.y})"

class Segment:
    def __init__(self, start: Point, end: Point):
        if (start.x, start.y) < (end.x, end.y):
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
    def __hash__(self):
        return hash((self.start, self.end))
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    def is_vertical(self):
        return self.start.x == self.end.x
    def is_horizontal(self):
        return self.start.y == self.end.y
    def __repr__(self):
        return f"[{self.start}->{self.end}]"

class Rectangle:
    def __init__(self, l: int, t: int, r: int, b: int):
        # top-left (l,t), bottom-right (r,b)
        self.l = l
        self.t = t
        self.r = r
        self.b = b
    def edges(self):
        # returns four segments corresponding to the rectangle edges
        # top edge: (l,t) to (r,t)
        # bottom edge: (l,b) to (r,b)
        # left edge: (l,b) to (l,t)
        # right edge: (r,b) to (r,t)
        top = Segment(Point(self.l, self.t), Point(self.r, self.t))
        bottom = Segment(Point(self.l, self.b), Point(self.r, self.b))
        left = Segment(Point(self.l, self.b), Point(self.l, self.t))
        right = Segment(Point(self.r, self.b), Point(self.r, self.t))
        return [top, bottom, left, right]

class PlaneGraph:
    def __init__(self):
        self.vertices = set()  # set of Points
        self.edges = dict()    # adjacency: Point -> set of Points

    def add_vertex(self, p: Point):
        if p not in self.vertices:
            self.vertices.add(p)
            self.edges[p] = set()

    def add_edge(self, p1: Point, p2: Point):
        self.add_vertex(p1)
        self.add_vertex(p2)
        self.edges[p1].add(p2)
        self.edges[p2].add(p1)

    def number_of_edges(self):
        # each edge counted once
        return sum(len(neigh) for neigh in self.edges.values()) // 2

    def number_of_vertices(self):
        return len(self.vertices)

def intersect_segments(seg1: Segment, seg2: Segment):
    # Only consider axis-aligned segments
    # seg1 and seg2 are either hor or vert
    if seg1.is_vertical() and seg2.is_horizontal():
        # vertical seg1: x=seg1.start.x, y in [seg1.start.y, seg1.end.y]
        # horizontal seg2: y=seg2.start.y, x in [seg2.start.x, seg2.end.x]
        x = seg1.start.x
        y = seg2.start.y
        if (min(seg1.start.y, seg1.end.y) <= y <= max(seg1.start.y, seg1.end.y) and
            min(seg2.start.x, seg2.end.x) <= x <= max(seg2.start.x, seg2.end.x)):
            return Point(x, y)
    elif seg1.is_horizontal() and seg2.is_vertical():
        return intersect_segments(seg2, seg1)
    return None

def segment_split_points(segment: Segment, points: set):
    # Given a segment and a set of points on it, split it into edges between adjacent points
    # points are guaranteed to lie on the segment
    if segment.is_horizontal():
        y = segment.start.y
        xs = [p.x for p in points]
        xs = sorted(set(xs))
        edges = []
        for i in range(len(xs)-1):
            p1 = Point(xs[i], y)
            p2 = Point(xs[i+1], y)
            edges.append((p1,p2))
        return edges
    else:  # vertical
        x = segment.start.x
        ys = [p.y for p in points]
        ys = sorted(set(ys))
        edges = []
        for i in range(len(ys)-1):
            p1 = Point(x, ys[i])
            p2 = Point(x, ys[i+1])
            edges.append((p1,p2))
        return edges

def build_graph_from_rectangles(rectangles):
    # We build the planar graph induced by all rectangle edges and their intersections.
    # Step 1: Collect all edges
    edges = []
    for rect in rectangles:
        edges.extend(rect.edges())

    # Step 2: Collect all vertices: each rectangle corner + intersection points of edges
    vertex_set = set()
    for e in edges:
        vertex_set.add(e.start)
        vertex_set.add(e.end)

    # Step 3: Find intersections between edges and add those points
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            inter = intersect_segments(edges[i], edges[j])
            if inter is not None:
                vertex_set.add(inter)

    # Step 4: For each edge, find all points lying on it (its ends plus intersections), sort them, create subedges
    graph = PlaneGraph()
    for e in edges:
        pts_on_e = [p for p in vertex_set if on_segment(p, e)]
        sub_edges = segment_split_points(e, pts_on_e)
        for (p1, p2) in sub_edges:
            graph.add_edge(p1, p2)
    return graph

def on_segment(p: Point, segment: Segment):
    # Check point p lies on segment (including endpoints)
    if segment.is_horizontal():
        y = segment.start.y
        if p.y != y:
            return False
        return min(segment.start.x, segment.end.x) <= p.x <= max(segment.start.x, segment.end.x)
    else:
        x = segment.start.x
        if p.x != x:
            return False
        return min(segment.start.y, segment.end.y) <= p.y <= max(segment.start.y, segment.end.y)

def count_regions(rectangles):
    graph = build_graph_from_rectangles(rectangles)
    V = graph.number_of_vertices()
    E = graph.number_of_edges()

    # Count connected components -BUT the arrangement of rectangle edges in plane will be connected?
    # Actually, if no rectangles no edges, so 1 region (whole plane).
    # If rectangles exist, the whole arrangement of edges is connected (edges either overlap or rectangles overlap)
    # But to be robust, let's compute number of connected components in graph
    visited = set()
    def dfs(node):
        stack = [node]
        while stack:
            u = stack.pop()
            for w in graph.edges[u]:
                if w not in visited:
                    visited.add(w)
                    stack.append(w)

    cc = 0
    for v in graph.vertices:
        if v not in visited:
            visited.add(v)
            dfs(v)
            cc += 1

    # Using Euler's formula for planar graph:
    # F = E - V + CC + 1
    # The number of faces/regions in the plane partitioned by these polygons.
    return E - V + cc + 1

def parse_input():
    import sys
    rectangles_data = []
    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            break
        if not line:
            continue
        n = int(line)
        rects = []
        for _ in range(n):
            l,t,r,b = map(int, sys.stdin.readline().split())
            # input: l t r b, but problem states top left (l,t), bottom right (r,b),
            # with t > b, and l < r
            rects.append(Rectangle(l,t,r,b))
        rectangles_data.append(rects)
    return rectangles_data

def main():
    rectangles_data = parse_input()
    for rects in rectangles_data:
        print(count_regions(rects))

if __name__ == "__main__":
    main()