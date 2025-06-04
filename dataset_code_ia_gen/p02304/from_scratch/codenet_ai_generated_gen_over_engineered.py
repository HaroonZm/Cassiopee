class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Segment:
    __slots__ = ('p1', 'p2')
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self._normalize()

    def _normalize(self):
        # Sort points so that p1 is always the "smaller" coordinate w.r.t. traversal
        if (self.p1.x, self.p1.y) > (self.p2.x, self.p2.y):
            self.p1, self.p2 = self.p2, self.p1

    def is_horizontal(self):
        return self.p1.y == self.p2.y

    def is_vertical(self):
        return self.p1.x == self.p2.x

    def __repr__(self):
        return f"Segment({self.p1}, {self.p2})"

class Event:
    __slots__ = ('x', 'type', 'segment', 'y')
    # type: "H_START", "H_END", "VERTICAL"
    def __init__(self, x: int, type: str, segment: Segment, y: int = None):
        self.x = x
        self.type = type
        self.segment = segment
        self.y = y if y is not None else (segment.p1.y if segment.is_horizontal() else segment.p1.y)

    def __lt__(self, other):
        # Order by x, then vertical, then horizontal start, then horizontal end (to process verticals between horizontal starts and ends)
        order = {"VERTICAL": 0, "H_START": 1, "H_END": 2}
        if self.x != other.x: 
            return self.x < other.x
        return order[self.type] < order[other.type]

    def __repr__(self):
        return f"Event(x={self.x}, type={self.type}, y={self.y})"

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.data = [0]*(size+1)

    def update(self, idx, delta=1):
        while idx <= self.size:
            self.data[idx] += delta
            idx += idx & (-idx)

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.data[idx]
            idx -= idx & (-idx)
        return s

    def range_query(self, left, right):
        if right < left:
            return 0
        return self.query(right) - self.query(left - 1)

class CoordinateCompressor:
    def __init__(self):
        self._values = []
        self._mapping = None

    def add(self, val):
        self._values.append(val)

    def build(self):
        unique = sorted(set(self._values))
        self._mapping = {v: i+1 for i, v in enumerate(unique)}

    def compress(self, val):
        return self._mapping[val]

class SegmentIntersectionCounter:
    def __init__(self, segments):
        self.segments = segments
        self.events = []
        self.coord_comp = CoordinateCompressor()

    def prepare(self):
        # Build events and collect all y-coord for compression
        for seg in self.segments:
            if seg.is_horizontal():
                # horizontal segment: add start and end events
                self.events.append(Event(seg.p1.x, "H_START", seg, seg.p1.y))
                self.events.append(Event(seg.p2.x, "H_END", seg, seg.p2.y))
                self.coord_comp.add(seg.p1.y)
            elif seg.is_vertical():
                # vertical segment: add vertical event at x, with y range for query
                self.coord_comp.add(seg.p1.y)
                self.coord_comp.add(seg.p2.y)
                self.events.append(Event(seg.p1.x, "VERTICAL", seg))
            else:
                raise ValueError("Segments must be axis-aligned")

        self.coord_comp.build()
        self.events.sort()

    def count_intersections(self):
        fenw = FenwickTree(len(self.coord_comp._mapping))
        intersections = 0
        for event in self.events:
            if event.type == "H_START":
                cy = self.coord_comp.compress(event.y)
                fenw.update(cy, +1)
            elif event.type == "H_END":
                cy = self.coord_comp.compress(event.y)
                fenw.update(cy, -1)
            elif event.type == "VERTICAL":
                seg = event.segment
                y1c = self.coord_comp.compress(seg.p1.y)
                y2c = self.coord_comp.compress(seg.p2.y)
                low, high = min(y1c, y2c), max(y1c, y2c)
                intersections += fenw.range_query(low, high)
        return intersections

class SegmentIntersectionProblemSolver:
    def __init__(self):
        self.segments = []

    def parse_input(self):
        import sys
        input = sys.stdin.readline
        n = int(input())
        for _ in range(n):
            x1,y1,x2,y2 = map(int, input().split())
            p1 = Point(x1,y1)
            p2 = Point(x2,y2)
            seg = Segment(p1,p2)
            self.segments.append(seg)

    def solve(self):
        self.parse_input()
        counter = SegmentIntersectionCounter(self.segments)
        counter.prepare()
        result = counter.count_intersections()
        print(result)

if __name__ == "__main__":
    solver = SegmentIntersectionProblemSolver()
    solver.solve()