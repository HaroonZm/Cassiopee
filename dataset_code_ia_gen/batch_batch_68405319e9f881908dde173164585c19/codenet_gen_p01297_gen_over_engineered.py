from math import hypot, isclose

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def distance_to(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class LineSegment:
    __slots__ = ('p1', 'p2')
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def length(self) -> float:
        return self.p1.distance_to(self.p2)
    def distance_to_point(self, p: Point) -> float:
        # Compute distance from point p to this segment
        # Project point p onto the line, then clamp to segment ends
        vx, vy = self.p2.x - self.p1.x, self.p2.y - self.p1.y
        wx, wy = p.x - self.p1.x, p.y - self.p1.y
        c1 = vx*wx + vy*wy
        if c1 <= 0:
            return p.distance_to(self.p1)
        c2 = vx*vx + vy*vy
        if c2 <= c1:
            return p.distance_to(self.p2)
        b = c1 / c2
        pb = Point(self.p1.x + b*vx, self.p1.y + b*vy)
        return p.distance_to(pb)
    def __repr__(self):
        return f"LineSegment({self.p1}, {self.p2})"

class Laser:
    __slots__ = ('line', 'thickness')
    def __init__(self, p1: Point, p2: Point, thickness: float):
        self.line = LineSegment(p1, p2)
        self.thickness = thickness
    def safe_distance(self) -> float:
        # minimal distance from machine center to laser line is at least this
        # laser is a band with thickness, so half thickness margin plus machine radius
        return self.thickness/2
    def overlaps(self, c: Point, r: float) -> bool:
        # Returns True if circle with center c and radius r overlaps with laser
        dist = self.line.distance_to_point(c)
        # overlap if distance <= laser half thickness + r
        return dist <= (self.thickness/2 + r - 1e-12)
    def __repr__(self):
        return f"Laser({self.line}, thickness={self.thickness})"

class Screen:
    def __init__(self, width: int, height: int, radius: float):
        self.width = width
        self.height = height
        self.radius = radius
        self.lasers = []
    def add_laser(self, laser: Laser):
        self.lasers.append(laser)
    def _point_valid(self, point: Point) -> bool:
        # Check machine fits entirely inside screen
        return (self.radius <= point.x <= self.width - self.radius and
                self.radius <= point.y <= self.height - self.radius)
    def is_safe(self, point: Point) -> bool:
        if not self._point_valid(point):
            return False
        for laser in self.lasers:
            if laser.overlaps(point, self.radius):
                return False
        return True
    def has_safe_area(self) -> bool:
        # To solve this, we want to find any point in the rectangle,
        # distance >= radius from edges, that is not overlapping any laser zone.
        #
        # Observation: laser safe zone contour is union of (line band) thickened by half thickness+r.
        # Since lasers are few (N <= 100), perform a sampling grid with adaptive checks.
        #
        # But problem is that laser beams are infinite in length, covering entire screen.
        # So safe areas are bounded by laser bands covering the screen except gaps between them.
        #
        # Implement a quadtree-like recursive subdivision refinement.
        
        class QuadTreeNode:
            def __init__(self, x0, y0, x1, y1, depth):
                self.x0 = x0
                self.y0 = y0
                self.x1 = x1
                self.y1 = y1
                self.depth = depth
                self.covered = None  # None means unknown, True means no safe, False means safe area exists
            def corners(self):
                return [Point(self.x0, self.y0), Point(self.x1, self.y0),
                        Point(self.x0, self.y1), Point(self.x1, self.y1)]
            def center(self):
                return Point((self.x0+self.x1)/2, (self.y0+self.y1)/2)
            def size(self):
                return max(self.x1 - self.x0, self.y1 - self.y0)
        
        # check if all points in box are definitely covered or definitely free
        # first check center and corners, if all safe or all unsafe, conclude
        # else subdivide if depth allows
        #
        # minimal box size threshold set based on radius, to detect safe spots of radius size
        
        MIN_SIZE = self.radius/2
        MAX_DEPTH = 12
        
        def check_covered(node: QuadTreeNode) -> bool:
            # True if all covered (no safe area), False if any safe area detected
            # Return True means covered, no safe area in node boundary
            
            points_to_check = node.corners() + [node.center()]
            statuses = []
            for p in points_to_check:
                if not self._point_valid(p):
                    statuses.append(True)  # outside screen as covered => no safe
                    continue
                safe = self.is_safe(p)
                statuses.append(not safe)  # covered means not safe
            
            # if all points indicate covered => whole node covered
            if all(statuses):
                return True
            # if all points indicate safe => whole node safe => safe area exists
            if not any(statuses):
                return False
            
            # Mixed signals: subdivide if possible
            if node.depth >= MAX_DEPTH or node.size() < MIN_SIZE:
                # We can't subdivide anymore, pessimistically treat as covered
                return True
            
            mx = (node.x0 + node.x1)/2
            my = (node.y0 + node.y1)/2
            childs = [QuadTreeNode(node.x0, node.y0, mx, my, node.depth+1),
                      QuadTreeNode(mx, node.y0, node.x1, my, node.depth+1),
                      QuadTreeNode(node.x0, my, mx, node.y1, node.depth+1),
                      QuadTreeNode(mx, my, node.x1, node.y1, node.depth+1)]
            for child in childs:
                if not check_covered(child):
                    return False
            return True
        
        root = QuadTreeNode(self.radius, self.radius, self.width - self.radius, self.height - self.radius, 0)
        
        return not check_covered(root)

def parse_input():
    import sys
    for line in sys.stdin:
        if not line.strip():
            continue
        W, H, N, R = map(int, line.strip().split())
        if W == 0 and H == 0 and N == 0 and R == 0:
            break
        screen = Screen(W, H, R)
        for _ in range(N):
            coords = sys.stdin.readline().strip().split()
            x1, y1, x2, y2, t = map(int, coords)
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            laser = Laser(p1, p2, t)
            screen.add_laser(laser)
        yield screen

def main():
    for screen in parse_input():
        print("Yes" if screen.has_safe_area() else "No")

if __name__ == "__main__":
    main()