class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other:'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def dot(self, other:'Point') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other:'Point') -> float:
        return self.x * other.y - self.y * other.x

    def norm(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Polyline:
    def __init__(self, points:list[Point]):
        self.points = points

    def translate(self, dx: float, dy:float) -> 'Polyline':
        return Polyline([Point(p.x + dx, p.y + dy) for p in self.points])

    def rotate(self, theta_rad: float, center: Point) -> 'Polyline':
        from math import cos, sin
        cos_t = cos(theta_rad)
        sin_t = sin(theta_rad)
        def rotate_point(p: Point) -> Point:
            v = p - center
            x_new = v.x * cos_t - v.y * sin_t + center.x
            y_new = v.x * sin_t + v.y * cos_t + center.y
            return Point(x_new, y_new)
        return Polyline([rotate_point(p) for p in self.points])

    def min_y(self) -> float:
        return min(p.y for p in self.points)

    def max_y(self) -> float:
        return max(p.y for p in self.points)

    def min_x(self) -> float:
        return min(p.x for p in self.points)

    def max_x(self) -> float:
        return max(p.x for p in self.points)

    def can_pass_through_hole(self) -> bool:
        # Strategy:
        # The polyline can be moved by translation and rotation preserving shape.
        # The hole is at (0,0) on y=0 line.
        # We want to check if we can translate + rotate to have all y < 0, with passing the hole (0,0).
        # Passing hole means some vertex can be at (0,0) after transformations.
        #
        # Because shape is rigid, transforming vertex i to hole (0,0) means we translate by (-x_i, -y_i)
        # Then we can rotate freely around (0,0).
        # Check if exist rotation angle so that all points have y < 0 after rotation.
        #
        # The problem reduces to:
        # For each vertex i to be at hole, translate polyline by (-x_i, -y_i)
        # There exists rotation angle theta so that all points rotated around origin have y<0.
        #
        # Instead of search of theta in [0,2pi], we do a computational geometry approach:
        # - For each i, compute angles for other points' vectors from origin.
        #   Find if there's an interval of pi length where all points' angles lie.
        # - If such an interval exists, rotate so all points are in lower half plane (y<0).
        #
        # If yes for any i, return True else False.

        import math

        EPS = 1e-14

        for i, base in enumerate(self.points):
            # Translate so base point at origin
            translated = [Point(p.x - base.x, p.y - base.y) for p in self.points]

            angles = []
            for k,p in enumerate(translated):
                if k == i:
                    continue
                angle = math.atan2(p.y, p.x)
                if angle < 0:
                    angle += 2 * math.pi
                angles.append(angle)
            angles.sort()
            m = len(angles)
            angles += [a + 2 * math.pi for a in angles]  # duplicate for circular search

            # Try to find a arc length of pi covering all angles
            # If yes, we can rotate so that all points lie within pi interval -> can put below y=0
            left = 0
            possible = False
            for right in range(m*2):
                while angles[right] - angles[left] > math.pi + EPS:
                    left += 1
                if right - left + 1 >= m:
                    # all points fit in interval length <= pi
                    possible = True
                    break
            if possible:
                return True
        return False


def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    points = []
    for _ in range(n):
        x,y = map(int, input().split())
        points.append(Point(x,y))
    poly = Polyline(points)
    if poly.can_pass_through_hole():
        print("Possible")
    else:
        print("Impossible")


if __name__ == "__main__":
    main()