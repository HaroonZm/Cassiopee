from math import cos, sin, radians
import sys

class Point2D:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Point2D':
        return Point2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> 'Point2D':
        return Point2D(self.x / scalar, self.y / scalar)

    def rotate_around(self, center: 'Point2D', angle_deg: float) -> 'Point2D':
        angle_rad = radians(angle_deg)
        translated = self - center
        cos_a = cos(angle_rad)
        sin_a = sin(angle_rad)
        rotated = Point2D(
            translated.x * cos_a - translated.y * sin_a,
            translated.x * sin_a + translated.y * cos_a
        )
        return rotated + center

    def __repr__(self):
        return f"{self.x:.8f} {self.y:.8f}"

class KochCurveSegment:
    def __init__(self, start: Point2D, end: Point2D):
        self.start = start
        self.end = end

    def subdivide(self):
        vec = self.end - self.start
        s = self.start + vec * (1/3)
        t = self.start + vec * (2/3)
        # Peak point u is s rotated around t by 60 degrees CCW or equivalently s rotated around s by +60 deg
        # We use s here as center for rotation of vector s->t by +60 deg, or equivalently s + (t-s).rotate(60)
        # But careful: peak is s + (t-s).rotated +60 degrees
        u = s + (t - s).rotate_around(Point2D(0,0), 60)
        return (   
            KochCurveSegment(self.start, s),
            KochCurveSegment(s, u),
            KochCurveSegment(u, t),
            KochCurveSegment(t, self.end)
        )

    def __repr__(self):
        return f"Seg({self.start}, {self.end})"

def build_koch_curve(segments, depth):
    if depth == 0:
        return segments
    new_segments = []
    for seg in segments:
        new_segments.extend(seg.subdivide())
    return build_koch_curve(new_segments, depth - 1)

class KochCurve:
    def __init__(self, depth: int):
        self.depth = depth
        self.start_point = Point2D(0.0,0.0)
        self.end_point = Point2D(100.0,0.0)
        self.segments = [KochCurveSegment(self.start_point, self.end_point)]

    def generate(self):
        self.segments = build_koch_curve(self.segments, self.depth)

    def points(self):
        # segments list contains segments in order
        # To print the points of the curve as unbroken line:
        # print start of first segment and then end of each segment
        pts = [self.segments[0].start]
        for seg in self.segments:
            pts.append(seg.end)
        return pts

def main():
    input_data = sys.stdin.read().strip()
    n = int(input_data)
    # Prepare specialized subclass for rotate vector around zero
    # We patch Point2D for vector rotate_around self at origin
    def rotate_vector(self, angle_deg):
        angle_rad = radians(angle_deg)
        cos_a = cos(angle_rad)
        sin_a = sin(angle_rad)
        return Point2D(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )
    Point2D.rotate_around = lambda self, center, angle_deg: (
        (self - center).rotate_vector(angle_deg) + center)
    Point2D.rotate_vector = rotate_vector

    koch = KochCurve(n)
    koch.generate()
    points = koch.points()
    for p in points:
        print(f"{p.x:.8f} {p.y:.8f}")

if __name__ == "__main__":
    main()