from math import radians, cos, sin
import sys

class InscribedPolygon:
    def __init__(self, vertex_count: int, center_angles: list[int]) -> None:
        self.vertex_count = vertex_count
        self.center_angles = center_angles
        self.vertices = self._compute_vertices()

    def _compute_vertices(self) -> list[complex]:
        # Compute absolute angles of each vertex on the inscribed circle assuming radius 1,
        # starting from 0 degrees and accumulating center angles counterclockwise.
        angles = self._accumulate_angles()
        return [complex(cos(a), sin(a)) for a in angles]

    def _accumulate_angles(self) -> list[float]:
        # Sum center angles to get absolute angles of vertices
        angles = [0.0]
        for v in self.center_angles:
            angles.append(angles[-1] + radians(v))
        # Last vertex implicitly closes at 360 degrees for consistency,
        # but not strictly necessary for polygon construction.
        return angles

    def area(self) -> float:
        # Compute polygon area on unit circle using shoelace formula on vertices
        x = [p.real for p in self.vertices]
        y = [p.imag for p in self.vertices]
        # Close polygon by adding the first vertex at the end
        x.append(x[0])
        y.append(y[0])
        area_sum = 0.0
        for i in range(self.vertex_count):
            area_sum += x[i] * y[i + 1] - y[i] * x[i + 1]
        return abs(area_sum) * 0.5

class PolygonAreaComparator:
    def __init__(self, polygons: list[InscribedPolygon]) -> None:
        self.first_polygon = polygons[0]
        self.second_polygon = polygons[1]

    def compare(self) -> int:
        area1 = self.first_polygon.area()
        area2 = self.second_polygon.area()
        # Compared with tolerance to avoid floating point equality issues,
        # though with integer angles on unit circle this should suffice.
        eps = 1e-14
        if abs(area1 - area2) < eps:
            return 0
        elif area1 > area2:
            return 1
        else:
            return 2

class InputParser:
    def __init__(self, stream) -> None:
        self.stream = stream

    def __iter__(self):
        return self

    def __next__(self) -> tuple[InscribedPolygon, InscribedPolygon]:
        # read first polygon
        line = self._read_non_empty_line()
        if line is None:
            raise StopIteration
        m = int(line)
        if m == 0:
            raise StopIteration
        angles_m = [int(self._read_non_empty_line()) for _ in range(m-1)]

        # read second polygon
        n = int(self._read_non_empty_line())
        angles_n = [int(self._read_non_empty_line()) for _ in range(n-1)]

        poly1 = InscribedPolygon(m, angles_m)
        poly2 = InscribedPolygon(n, angles_n)
        return (poly1, poly2)

    def _read_non_empty_line(self) -> str | None:
        while True:
            line = self.stream.readline()
            if not line:
                return None
            clean_line = line.strip()
            if clean_line:
                return clean_line

def main():
    parser = InputParser(sys.stdin)
    for poly1, poly2 in parser:
        comparator = PolygonAreaComparator([poly1, poly2])
        print(comparator.compare())

if __name__ == "__main__":
    main()