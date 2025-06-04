from typing import List, Tuple, Optional
import sys
import math

# Geometrical abstractions

class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Point':
        return Point(self.x + other.dx, self.y + other.dy)

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def as_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Vector:
    __slots__ = ['dx', 'dy']
    def __init__(self, dx: float, dy: float):
        self.dx = dx
        self.dy = dy

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.dx * scalar, self.dy * scalar)

    def __rmul__(self, scalar: float) -> 'Vector':
        return self.__mul__(scalar)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.dx + other.dx, self.dy + other.dy)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.dx - other.dx, self.dy - other.dy)

    def dot(self, other: 'Vector') -> float:
        return self.dx * other.dx + self.dy * other.dy

    def cross(self, other: 'Vector') -> float:
        return self.dx * other.dy - self.dy * other.dx

    def norm(self) -> float:
        return math.hypot(self.dx, self.dy)

    def normalized(self) -> 'Vector':
        n = self.norm()
        if n == 0:
            raise ValueError("Zero length vector cannot be normalized")
        return Vector(self.dx / n, self.dy / n)

    def perpendicular(self) -> 'Vector':
        # Rotate vector 90 degrees CCW
        return Vector(-self.dy, self.dx)

    def __repr__(self):
        return f"Vector({self.dx}, {self.dy})"

class Line:
    # Line in parametric form: point + t * direction_vector
    __slots__ = ['p', 'd']
    def __init__(self, p: Point, d: Vector):
        if d.norm() == 0:
            raise ValueError("Direction vector cannot be zero")
        self.p = p
        self.d = d.normalized()

    def point_at(self, t: float) -> Point:
        return Point(self.p.x + self.d.dx * t, self.p.y + self.d.dy * t)

    def __repr__(self):
        return f"Line(Point={self.p}, Direction={self.d})"

class Polygon:
    # Convex polygon with vertices in CCW order
    __slots__ = ['vertices']
    def __init__(self, vertices: List[Point]):
        if len(vertices) < 3:
            raise ValueError("Polygon must have at least 3 vertices")
        self.vertices = vertices

    def area(self) -> float:
        return abs(self._signed_area())

    def _signed_area(self) -> float:
        area = 0.0
        n = len(self.vertices)
        for i in range(n):
            x1, y1 = self.vertices[i].as_tuple()
            x2, y2 = self.vertices[(i+1) % n].as_tuple()
            area += (x1 * y2 - x2 * y1)
        return area / 2.0

    def centroid(self) -> Point:
        # Computes centroid of polygon (convex or not)
        cx = 0.0
        cy = 0.0
        area = self._signed_area()
        factor = 0.0
        n = len(self.vertices)
        for i in range(n):
            x0, y0 = self.vertices[i].as_tuple()
            x1, y1 = self.vertices[(i+1) % n].as_tuple()
            cross = x0 * y1 - x1 * y0
            cx += (x0 + x1) * cross
            cy += (y0 + y1) * cross
        factor = 1/(6*area) if area != 0 else 0
        return Point(cx * factor, cy * factor)

    def cut_by_line(self, line: Line) -> Tuple[Optional['Polygon'], Optional['Polygon']]:
        # Splits polygon by line, returns (left_polygon, right_polygon)
        # left corresponds to points P where (line.direction perp) dot (P - line.p) >= 0
        # right corresponds to points P where <= 0
        left_pts = []
        right_pts = []

        n = len(self.vertices)
        d_perp = line.d.perpendicular()
        def side(p: Point):
            v = p - line.p
            return d_perp.dot(v)

        for i in range(n):
            cur = self.vertices[i]
            nxt = self.vertices[(i+1) % n]
            cur_side = side(cur)
            nxt_side = side(nxt)

            if cur_side >= -1e-14:
                left_pts.append(cur)
            if cur_side <= 1e-14:
                right_pts.append(cur)

            if cur_side * nxt_side < -1e-14:
                # intersect segment with line
                seg_vec = nxt - cur
                denom = line.d.cross(seg_vec)
                # denom should not be zero since polygon is convex and line intersects edges max twice
                if abs(denom) < 1e-20:
                    continue
                t = line.d.cross(line.p - cur) / denom
                t = max(0.0, min(1.0, t))
                intersect_p = Point(cur.x + seg_vec.dx * t, cur.y + seg_vec.dy * t)
                left_pts.append(intersect_p)
                right_pts.append(intersect_p)

        left_poly = Polygon(left_pts) if len(left_pts) >= 3 else None
        right_poly = Polygon(right_pts) if len(right_pts) >= 3 else None

        return left_poly, right_poly

    def __repr__(self):
        return f"Polygon({self.vertices})"


# Solver abstractions

class ConvexCutSolver:
    def __init__(self, polygon: Polygon):
        self.polygon = polygon
        self.area = polygon.area()
        self.n = len(polygon.vertices)

    def solve(self) -> Optional[Point]:
        """
        Return point P such that cutting along any line through P splits polygon into two sub-polygons of equal area,
        or None if no such point exists.
        """

        # Fundamental observation:
        # We want P such that, for every direction, the line through P orthogonal to that direction divides polygon into equal area halves.
        # Because polygon is convex, the set of chords through polygon are monotone in direction.
        # Such point P (if exists) is unique and can be found via binary search in the polygon.
        #
        # One characterisation: P is the unique point where for all directions,
        # the chord through P divides polygon area equally.
        #
        # This is known as the "center of mass" of sections or the "Convex-Cut" point,
        # For convex polygon, it is the unique point such that the area on either side of any line through it is equal.
        #
        # Intuition and problem constraints suggest the following approach:

        # Algorithm approach (excessively sophisticated!):
        # 1. We reduce problem to finding a point P inside polygon with equal-area half polygon separations.
        # 2. We define a "half-area function" F(P, theta): area to left of line through P perpendicular to direction theta.
        # 3. For all theta in [0, pi), F(P, theta) = half area of polygon.
        # 4. We use a numerically stable multidimensional root finder:
        #    Minimise g(P) = max_theta |F(P, theta) - half_area|
        # 5. If minimal g(P) <= 1e-4, then output P, else NA.

        # Because polygon <= N=50, brute forcing discrete theta directions is feasible.
        # Could optimize further, but let's keep highly abstracted code.


        HALF_AREA = self.area / 2.0

        # Directions for checking (sampling arcs from 0 to pi)
        M = 180  # number of directions
        directions = [self._unit_vector_angle(math.pi * i / M) for i in range(M)]

        # Initial guess: polygon centroid
        P = self.polygon.centroid()

        # Objective function: maximum absolute difference over sample directions
        def max_diff(P: Point) -> float:
            max_d = 0.0
            for d in directions:
                line = Line(P, d.perpendicular())
                left_poly, right_poly = self.polygon.cut_by_line(line)
                left_area = left_poly.area() if left_poly else 0.0
                diff = abs(left_area - HALF_AREA)
                if diff > max_d:
                    max_d = diff
                    if max_d > 1e-3:
                        # Early exit if already worse than tolerance
                        break
            return max_d

        # We attempt local minimization via Nelder-Mead like heuristic for fun

        class NelderMeadOptimizer:
            # A simple 2D Nelder-Mead for this problem, highly explicit

            def __init__(self, func, x0: Tuple[float, float], tol: float = 1e-7, max_iter: int = 1000):
                self.f = func
                self.x = [list(x0), [x0[0]+1e-1, x0[1]], [x0[0], x0[1]+1e-1]]
                self.fvals = [self.f(Point(*p)) for p in self.x]
                self.tol = tol
                self.max_iter = max_iter

            def step(self):
                # order
                idx = sorted(range(3), key=lambda i: self.fvals[i])
                self.x = [self.x[i] for i in idx]
                self.fvals = [self.fvals[i] for i in idx]
                x0, x1, x2 = self.x
                f0, f1, f2 = self.fvals

                centroid = [(x0[0]+x1[0])/2, (x0[1]+x1[1])/2]

                # reflection
                xr = [centroid[0] + (centroid[0] - x2[0]), centroid[1] + (centroid[1] - x2[1])]
                fr = self.f(Point(*xr))
                if fr < f0:
                    # expansion
                    xe = [centroid[0] + 2*(centroid[0] - x2[0]), centroid[1] + 2*(centroid[1] - x2[1])]
                    fe = self.f(Point(*xe))
                    if fe < fr:
                        self.x[2], self.fvals[2] = xe, fe
                    else:
                        self.x[2], self.fvals[2] = xr, fr
                elif fr < f1:
                    self.x[2], self.fvals[2] = xr, fr
                else:
                    # contraction
                    xc = [centroid[0] + 0.5*(x2[0] - centroid[0]), centroid[1] + 0.5*(x2[1] - centroid[1])]
                    fc = self.f(Point(*xc))
                    if fc < f2:
                        self.x[2], self.fvals[2] = xc, fc
                    else:
                        # shrink
                        self.x[1] = [x0[0] + 0.5*(x1[0] - x0[0]), x0[1] + 0.5*(x1[1] - x0[1])]
                        self.fvals[1] = self.f(Point(*self.x[1]))
                        self.x[2] = [x0[0] + 0.5*(x2[0] - x0[0]), x0[1] + 0.5*(x2[1] - x0[1])]
                        self.fvals[2] = self.f(Point(*self.x[2]))

            def optimize(self) -> Tuple[Point, float]:
                for _ in range(self.max_iter):
                    prev_x0 = self.x[0]
                    prev_f0 = self.fvals[0]
                    self.step()
                    if max(abs(self.x[0][0] - prev_x0[0]), abs(self.x[0][1] - prev_x0[1])) < self.tol and abs(self.fvals[0] - prev_f0) < self.tol:
                        break
                return Point(*self.x[0]), self.fvals[0]

        best_point, best_val = NelderMeadOptimizer(max_diff, P.as_tuple()).optimize()

        # Check if best_val within required precision
        if best_val <= 1e-4:
            # Confirm point inside polygon
            if self._point_in_polygon(best_point):
                return best_point

        return None

    def _unit_vector_angle(self, angle_rad: float) -> Vector:
        return Vector(math.cos(angle_rad), math.sin(angle_rad))

    def _point_in_polygon(self, p: Point) -> bool:
        # Ray casting algorithm to confirm point inside polygon
        # polygon is convex but let's keep generic
        cnt = 0
        n = self.n
        vs = self.polygon.vertices
        x, y = p.x, p.y
        for i in range(n):
            x1, y1 = vs[i].x, vs[i].y
            x2, y2 = vs[(i+1)%n].x, vs[(i+1)%n].y
            if self._ray_intersect_seg(x, y, x1, y1, x2, y2):
                cnt += 1
        return cnt % 2 == 1

    def _ray_intersect_seg(self, x: float, y: float, x1: float, y1: float, x2: float, y2: float) -> bool:
        if y1 > y2:
            x1,y1,x2,y2 = x2,y2,x1,y1
        if y == y1 or y == y2:
            y += 1e-10
        if y < y1 or y > y2:
            return False
        if x1 == x2:
            return x <= x1
        xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        return x <= xint


def main():
    input = sys.stdin.readline
    N = int(input())
    vertices = [Point(*map(int, input().split())) for _ in range(N)]
    polygon = Polygon(vertices)
    solver = ConvexCutSolver(polygon)
    res = solver.solve()
    if res is None:
        print("NA")
    else:
        print(f"{res.x:.5f} {res.y:.5f}")

if __name__ == "__main__":
    main()