import math

EPS = 1e-10  # Tolerance for floating-point comparisons

class Point:
    """
    Represents a 2D point or vector with basic arithmetic and utility operations.
    """

    def __init__(self, x, y):
        """
        Initialize a Point with coordinates x and y.

        Args:
            x (float): x coordinate.
            y (float): y coordinate.
        """
        self.x = x
        self.y = y

    def __sub__(self, p):
        """
        Subtract another Point from this Point (vector subtraction).

        Args:
            p (Point): The point to subtract.

        Returns:
            Point: The result of self - p.
        """
        return Point(self.x - p.x, self.y - p.y)

    def __add__(self, p):
        """
        Add another Point to this Point (vector addition).

        Args:
            p (Point): The point to add.

        Returns:
            Point: The result of self + p.
        """
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, a):
        """
        Scale the Point by a scalar (multiplication).

        Args:
            a (float): Scalar multiplier.

        Returns:
            Point: The result of scaling the point.
        """
        return Point(self.x * a, self.y * a)

    def __truediv__(self, a):
        """
        Scale the Point by dividing with a scalar.

        Args:
            a (float): Scalar divisor.

        Returns:
            Point: The scaled point.
        """
        return Point(self.x / a, self.y / a)

    def __str__(self):
        """
        Human-readable string representation.

        Returns:
            str: String representation as 'x,y'.
        """
        return f"{self.x},{self.y}"

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: String representation as 'Point(x,y)'.
        """
        return f"Point({self.x},{self.y})"

    def __lt__(self, other):
        """
        Less-than comparator for sorting points by y, then x.

        Args:
            other (Point): Point to compare to.

        Returns:
            bool: True if self < other.
        """
        if abs(self.y - other.y) < EPS:
            return self.x < other.x
        return self.y < other.y

    def __eq__(self, other):
        """
        Point equality within a tolerance EPS.

        Args:
            other (Point): Point to compare to.

        Returns:
            bool: True if points are equal within EPS.
        """
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

class Segment:
    """
    Represents a 2D line segment defined by endpoints p1 and p2.
    """

    def __init__(self, p1, p2):
        """
        Initialize a Segment.

        Args:
            p1 (Point): Starting point of segment.
            p2 (Point): Ending point of segment.
        """
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        """
        Human-readable string representation.

        Returns:
            str: String as 'segment:(p1;p2)'
        """
        return f"segment:({self.p1};{self.p2})"

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: String as 'segment:(p1;p2)'
        """
        return f"segment:({self.p1};{self.p2})"

class Circle:
    """
    Represents a circle in 2D space.
    """

    def __init__(self, c, r):
        """
        Initialize the Circle.

        Args:
            c (Point): Center of the circle.
            r (float): Radius of the circle.
        """
        self.c = c
        self.r = r

    def __str__(self):
        """
        Human-readable string representation.

        Returns:
            str: String representing the circle.
        """
        return f'Circle:(center point: {self.c}; radius: {self.r})'

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: String representing the circle.
        """
        return f'Circle:(center point: {self.c}; radius: {self.r})'

class Polygon:
    """
    Represents a 2D polygon as a list of Points.
    """

    def __init__(self, ps=None):
        """
        Initialize the Polygon.

        Args:
            ps (list(Point), optional): List of points. Defaults to empty.
        """
        if ps is None:
            ps = []
        self.ps = ps
        self.size = len(ps)

    def __getitem__(self, i):
        """
        Enable indexing through Polygon points.

        Args:
            i (int): Index.

        Returns:
            Point: Point at index i.
        """
        return self.ps[i]

    def __setitem__(self, i, p):
        """
        Set the point at a given index.

        Args:
            i (int): Index.
            p (Point): The point to set.
        """
        self.ps[i] = p

    def __iter__(self):
        """
        Enable iteration over points.

        Returns:
            list(Point): The list of points.
        """
        return iter(self.ps)

    def addpoint(self, i, p):
        """
        Insert a point in the polygon at position i.

        Args:
            i (int): Index to insert at.
            p (Point): Point to insert.
        """
        self.ps.insert(i, p)
        self.size += 1

    def delpoint(self, i):
        """
        Remove and return the point at index i.

        Args:
            i (int): Index to remove.

        Returns:
            Point: Removed point.
        """
        self.size -= 1
        return self.ps.pop(i)

    def sortYX(self):
        """
        Sort the polygon points by y ascending, then x ascending.
        """
        self.ps.sort()

    def __str__(self):
        """
        Human-readable string representation.

        Returns:
            str: String as 'Polygon:(p1,p2,...)'
        """
        return f'Polygon:{tuple(self.ps)}'

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: String as 'Polygon:(p1,p2,...)'
        """
        return f'Polygon:{tuple(self.ps)}'

    def __len__(self):
        """
        Number of points in polygon.

        Returns:
            int: The number of points.
        """
        return len(self.ps)

    def __eq__(self, other):
        """
        Equality based on polygon vertices.

        Args:
            other (Polygon): Polygon to compare.

        Returns:
            bool: True if all vertices are equal.
        """
        return self.ps == other.ps

    def draw(self):
        """
        Draw the polygon using Turtle graphics (visualization).
        """
        import turtle
        turtle.screensize(800, 800, "black")
        turtle.title("Polygon convex hull")
        turtle.setworldcoordinates(-400, -400, 400, 400)
        t = turtle.Turtle()
        t.pencolor("red")
        for pt in self.ps:
            t.goto(pt.x, pt.y)
            t.dot(10, 'white')

# ================== Vector & Point Operations ==================

def norm(p):
    """
    Returns the squared norm (magnitude squared) of vector p.

    Args:
        p (Point): The vector/point.

    Returns:
        float: Squared magnitude.
    """
    return p.x * p.x + p.y * p.y

def length(p):
    """
    Returns the Euclidean length of vector p.

    Args:
        p (Point): The vector/point.

    Returns:
        float: The length.
    """
    return math.sqrt(p.x * p.x + p.y * p.y)

def dot(a, b):
    """
    Returns the dot (scalar) product of two vectors.

    Args:
        a (Point): Vector a.
        b (Point): Vector b.

    Returns:
        float: Dot product a·b.
    """
    return a.x * b.x + a.y * b.y

def cross(a, b):
    """
    Returns the cross (vector) product of two vectors a and b.

    Args:
        a (Point): Vector a.
        b (Point): Vector b.

    Returns:
        float: Cross product (signed area of 2D parallelogram).
    """
    return a.x * b.y - a.y * b.x

def project(s, p):
    """
    Projects point p onto segment s (the line determined by s).

    Args:
        s (Segment): The segment.
        p (Point): The point to project.

    Returns:
        Point: The projected point.
    """
    base = s.p2 - s.p1  # Direction vector of segment
    r = dot(p - s.p1, base) / norm(base)
    return s.p1 + base * r

def getDistance(a, b):
    """
    Computes Euclidean distance between two points.

    Args:
        a (Point): First point.
        b (Point): Second point.

    Returns:
        float: The distance.
    """
    return length(a - b)

def getDistanceLP(l, p):
    """
    Returns the minimum distance from the line defined by segment l to point p.

    Args:
        l (Segment): The defining segment (acts as a line).
        p (Point): The external point.

    Returns:
        float: The perpendicular distance.
    """
    return abs(cross(l.p2 - l.p1, p - l.p1) / length(l.p2 - l.p1))

def getDistanceSP(s, p):
    """
    Returns the shortest distance from segment s to point p.

    Args:
        s (Segment): The segment.
        p (Point): The point.

    Returns:
        float: Shortest distance.
    """
    if dot(s.p2 - s.p1, p - s.p1) < 0.0:
        return length(p - s.p1)
    if dot(s.p1 - s.p2, p - s.p2) < 0.0:
        return length(p - s.p2)
    return getDistanceLP(s, p)

def isOrthogonalSG(s1, s2):
    """
    Checks if two segments are orthogonal (perpendicular).

    Args:
        s1 (Segment): First segment.
        s2 (Segment): Second segment.

    Returns:
        bool: True if segments are perpendicular.
    """
    return abs(dot(s1.p2 - s1.p1, s2.p2 - s2.p1)) < EPS

def isParallelLN(s1, s2):
    """
    Checks if two segments are parallel.

    Args:
        s1 (Segment): First segment.
        s2 (Segment): Second segment.

    Returns:
        bool: True if segments are parallel.
    """
    return abs(cross(s1.p2 - s1.p1, s2.p2 - s2.p1)) < EPS

# Enumeration for counter-clockwise test
COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = -2
ONLINE_FRONT = 2
ON_SEGMENT = 0

def ccw(p0, p1, p2):
    """
    Counter-clockwise test for points p0, p1, p2.

    Args:
        p0 (Point): Pivot point.
        p1 (Point): First vector endpoint.
        p2 (Point): Second vector endpoint.

    Returns:
        int: One of COUNTER_CLOCKWISE, CLOCKWISE, ONLINE_BACK, ONLINE_FRONT, ON_SEGMENT
    """
    a = p1 - p0
    b = p2 - p0
    c = cross(a, b)
    if c > EPS:
        return COUNTER_CLOCKWISE
    if c < -EPS:
        return CLOCKWISE
    if dot(a, b) < -EPS:
        return ONLINE_BACK
    if norm(a) < norm(b):
        return ONLINE_FRONT
    return ON_SEGMENT

def toleft(p0, p1, p2):
    """
    Determines the relative position of p2 to the directed segment p0->p1.

    Args:
        p0 (Point): Start of base segment.
        p1 (Point): End of base segment.
        p2 (Point): Query point.

    Returns:
        int:
            1   if p2 is left of p0p1 (ccw),
            -1  if right,
            2   if p2 collinear and beyond p1,
            -2  if p2 collinear and before p0
    """
    a = p1 - p0
    b = p2 - p0
    tmp = cross(a, b)
    if tmp > EPS:
        return 1
    elif abs(tmp) < EPS and norm(a) <= norm(b):
        return 2  # Collinear, p2 on right extension of p0p1
    elif abs(tmp) < EPS and norm(a) > norm(b):
        return -2  # Collinear, p2 on left extension
    else:
        return -1

def reflect(s, p):
    """
    Reflect point p across segment s (about the supporting line).

    Args:
        s (Segment): The line (segment) as axis of reflection.
        p (Point): The point to reflect.

    Returns:
        Point: The symmetric reflection of p about the line.
    """
    return p + (project(s, p) - p) * 2.0

# --------------------- Main Execution Section ----------------------

if __name__ == "__main__":
    # Read the coordinates of the reference segment
    s = [int(x) for x in input().split()]
    p1 = Point(s[0], s[1])
    p2 = Point(s[2], s[3])
    sg = Segment(p1, p2)

    # Read the number of queries
    q = int(input())

    # For each query, reflect the input point about the segment and print the result
    for _ in range(q):
        s = [int(x) for x in input().split()]
        p3 = Point(s[0], s[1])
        pt = reflect(sg, p3)
        print(pt.x, pt.y)