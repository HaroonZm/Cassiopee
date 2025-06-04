import math
import sys
from typing import List, Tuple, Iterator


class Circle:
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r

    def contains_point(self, px: float, py: float) -> bool:
        return (px - self.x) ** 2 + (py - self.y) ** 2 < self.r ** 2

    def circumference(self) -> float:
        return 2 * math.pi * self.r

    def __repr__(self):
        return f"Circle(({self.x}, {self.y}), r={self.r})"


class MysteryCircles:
    def __init__(self, circles: List[Circle]):
        self.circles = circles

    def _arc_length_exclusive(self, circle_idx: int, arc_precision: int = 10000) -> float:
        """Calculate the total length of circumference of one circle not covered by any other circle."""
        circle = self.circles[circle_idx]
        total_length = 0.0

        # We sample points on the circumference uniformly
        delta_theta = 2 * math.pi / arc_precision

        # Because we need the arc length, we accumulate arc segments where the point is exclusive to the circle
        # i.e. point is on circle's circumference but outside all other circles
        length_accum = 0.0
        prev_exclusive = False
        for i in range(arc_precision + 1):  # +1 to include the last point at 2pi closing the loop
            theta = i * delta_theta
            px = circle.x + circle.r * math.cos(theta)
            py = circle.y + circle.r * math.sin(theta)
            # Check if point is outside all other circles
            is_exclusive = True
            for j, other in enumerate(self.circles):
                if j == circle_idx:
                    continue
                # For the special case of floating error margin on circumference, inclusion is strict inside < r^2
                # So point on circumference is not considered inside other circles
                if other.contains_point(px, py):
                    is_exclusive = False
                    break

            if is_exclusive:
                if prev_exclusive:
                    # Add the arc segment length between previous point and this point on circumference
                    # arc length between angles delta_theta * radius
                    length_accum += delta_theta * circle.r
                else:
                    # Starting a new exclusive arc section
                    length_accum += 0  # no length to add yet
            else:
                total_length += length_accum
                length_accum = 0.0
            prev_exclusive = is_exclusive

        # In case the last points wrapped around an exclusive segment
        total_length += length_accum
        return total_length

    def total_exclusive_length(self) -> float:
        # Sum the exclusive arc lengths of all circles
        length_sum = 0.0
        for idx in range(len(self.circles)):
            length_sum += self._arc_length_exclusive(idx)
        return length_sum


class InputParser:
    def __init__(self, stream: Iterator[str]):
        self.stream = stream

    def __iter__(self):
        return self

    def __next__(self) -> List[Circle]:
        while True:
            line = next(self.stream).strip()
            if line == '':
                continue
            n = int(line)
            if n == 0:
                raise StopIteration
            circles = []
            for _ in range(n):
                x, y, r = map(float, next(self.stream).strip().split())
                circles.append(Circle(x, y, r))
            return circles


def main():
    parser = InputParser(iter(sys.stdin.readline, ''))
    results = []
    for circles in parser:
        mystery_circles = MysteryCircles(circles)
        length = mystery_circles.total_exclusive_length()
        results.append(length)
    for res in results:
        print(f"{res:.12f}")


if __name__ == "__main__":
    main()