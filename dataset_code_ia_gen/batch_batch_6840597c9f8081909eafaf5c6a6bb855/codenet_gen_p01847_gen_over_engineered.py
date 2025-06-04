from typing import List, Tuple, Optional
from abc import ABC, abstractmethod


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return (self.x, self.y) == (other.x, other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other: "Point") -> int:
        return self.x * other.y - self.y * other.x


class Polygon(ABC):
    def __init__(self, vertices: List[Point]) -> None:
        self.vertices = vertices

    @abstractmethod
    def area(self) -> int:
        pass

    @abstractmethod
    def clip_with(self, other: "Polygon") -> Optional["Polygon"]:
        pass


class AxisAlignedRectangle(Polygon):
    def __init__(self, vertices: List[Point]) -> None:
        if len(vertices) != 4:
            raise ValueError("Rectangle must have exactly 4 vertices")
        super().__init__(vertices)
        xs = [v.x for v in vertices]
        ys = [v.y for v in vertices]
        self.min_x, self.max_x = min(xs), max(xs)
        self.min_y, self.max_y = min(ys), max(ys)

    def area(self) -> int:
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)

    def clip_with(self, other: "Polygon") -> Optional[Polygon]:
        # Since this is a rectangle, use Sutherland-Hodgman polygon clipping with a polygon
        result = sutherland_hodgman_clip(other.vertices, self.vertices)
        if not result:
            return None
        return SimplePolygon(result)


class SimplePolygon(Polygon):
    def area(self) -> int:
        area = 0
        n = len(self.vertices)
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i].x * self.vertices[j].y
            area -= self.vertices[j].x * self.vertices[i].y
        return abs(area) // 2

    def clip_with(self, other: "Polygon") -> Optional[Polygon]:
        # Clip self with other polygon
        clipped = sutherland_hodgman_clip(self.vertices, other.vertices)
        if not clipped:
            return None
        return SimplePolygon(clipped)


def is_inside(p: Point, edge_start: Point, edge_end: Point) -> bool:
    # Check if point p is inside edge (to the left)
    # For polygon edges defined counterclockwise, inside is left side
    return ((edge_end - edge_start).cross(p - edge_start)) >= 0


def compute_intersection(p1: Point, p2: Point, q1: Point, q2: Point) -> Point:
    # Compute intersection point of line segments p1p2 and q1q2
    # Using line-line intersection formula
    A1 = p2.y - p1.y
    B1 = p1.x - p2.x
    C1 = A1 * p1.x + B1 * p1.y

    A2 = q2.y - q1.y
    B2 = q1.x - q2.x
    C2 = A2 * q1.x + B2 * q1.y

    det = A1 * B2 - A2 * B1
    # det cannot be zero as polygons are simple and edges won't be parallel here for clipping
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    # Since input coords are integer, intersection must also be integer for axis aligned polygons in problem context
    # But to be safe, round to nearest int
    return Point(int(round(x)), int(round(y)))


def sutherland_hodgman_clip(subject_polygon: List[Point], clip_polygon: List[Point]) -> List[Point]:
    """Clip a polygon with another polygon using the Sutherland-Hodgman algorithm."""
    output_list = subject_polygon
    cp_count = len(clip_polygon)

    for i in range(cp_count):
        input_list = output_list
        output_list = []
        if not input_list:
            break

        edge_start = clip_polygon[i]
        edge_end = clip_polygon[(i + 1) % cp_count]

        s = input_list[-1]
        for e in input_list:
            if is_inside(e, edge_start, edge_end):
                if not is_inside(s, edge_start, edge_end):
                    intersection_point = compute_intersection(s, e, edge_start, edge_end)
                    output_list.append(intersection_point)
                output_list.append(e)
            elif is_inside(s, edge_start, edge_end):
                intersection_point = compute_intersection(s, e, edge_start, edge_end)
                output_list.append(intersection_point)
            s = e

    return output_list


class WindowCurtainModel:
    """Model representing windows and curtains and the intersection logic for coverage."""

    def __init__(self, window_vertices: List[Tuple[int, int]], curtain_vertices: List[Tuple[int, int]]) -> None:
        self.window = SimplePolygon([Point(x, y) for x, y in window_vertices])
        self.curtain = AxisAlignedRectangle([Point(a, b) for a, b in curtain_vertices])

    def uncovered_area(self) -> int:
        covered_polygon = self.window.clip_with(self.curtain)
        covered_area = covered_polygon.area() if covered_polygon else 0
        window_area = self.window.area()
        return window_area - covered_area


class InputParser:
    """Parser to read input data sets until a zero is encountered."""

    def __init__(self) -> None:
        pass

    def parse(self) -> List[Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]]:
        datasets = []
        while True:
            try:
                line = input().strip()
                if line == "0":
                    break
                N = int(line)
                window_vertices = []
                for _ in range(N):
                    x, y = map(int, input().split())
                    window_vertices.append((x, y))
                curtain_vertices = []
                for _ in range(4):
                    a, b = map(int, input().split())
                    curtain_vertices.append((a, b))
                datasets.append((window_vertices, curtain_vertices))
            except EOFError:
                break
        return datasets


class SolutionRunner:
    """Encapsulates the complete solving routine."""

    def __init__(self) -> None:
        self.parser = InputParser()

    def run(self) -> None:
        datasets = self.parser.parse()
        for window_vertices, curtain_vertices in datasets:
            model = WindowCurtainModel(window_vertices, curtain_vertices)
            print(model.uncovered_area())


if __name__ == "__main__":
    SolutionRunner().run()