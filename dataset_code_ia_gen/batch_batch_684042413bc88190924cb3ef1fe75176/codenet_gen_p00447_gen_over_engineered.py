class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, vector: 'Vector') -> 'Point':
        return Point(self.x + vector.dx, self.y + vector.dy)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Vector:
    __slots__ = ('dx', 'dy')

    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.dx == other.dx and self.dy == other.dy

class StarPattern:
    def __init__(self, stars: list[Point]):
        if not stars:
            raise ValueError("StarPattern requires at least one star")
        self.stars = stars
        self.reference_star = stars[0]
        self.relative_positions = self._calculate_relative_positions()

    def _calculate_relative_positions(self) -> set:
        # Positions of stars relative to the reference star
        return {star - self.reference_star for star in self.stars[1:]}

class StarMap:
    def __init__(self, stars: list[Point]):
        self.stars = stars
        self.star_set = set(stars)

    def contains_pattern_at(self, pattern: StarPattern, top_star_candidate: Point) -> bool:
        offset = Vector(top_star_candidate.x - pattern.reference_star.x,
                        top_star_candidate.y - pattern.reference_star.y)
        # Check that all stars in the pattern (offset by vector) exist in star map
        for relative_pos in pattern.relative_positions:
            check_point = Point(top_star_candidate.x + relative_pos.dx,
                                top_star_candidate.y + relative_pos.dy)
            if check_point not in self.star_set:
                return False
        return True

    def find_pattern_offset(self, pattern: StarPattern) -> Vector | None:
        # Iterate over all stars in star map, attempt to match pattern reference star
        for candidate in self.stars:
            if self.contains_pattern_at(pattern, candidate):
                dx = candidate.x - pattern.reference_star.x
                dy = candidate.y - pattern.reference_star.y
                return Vector(dx, dy)
        return None

class StarPatternDetector:
    def __init__(self):
        self.results = []

    def read_pattern(self, input_iter) -> StarPattern | None:
        try:
            m = int(next(input_iter))
        except StopIteration:
            return None
        if m == 0:
            return None
        stars = []
        for _ in range(m):
            x_str, y_str = next(input_iter).split()
            stars.append(Point(int(x_str), int(y_str)))
        return StarPattern(stars)

    def read_star_map(self, input_iter) -> StarMap:
        n = int(next(input_iter))
        stars = []
        for _ in range(n):
            x_str, y_str = next(input_iter).split()
            stars.append(Point(int(x_str), int(y_str)))
        return StarMap(stars)

    def process(self, input_lines: list[str]):
        input_iter = iter(line.strip() for line in input_lines if line.strip())
        while True:
            pattern = self.read_pattern(input_iter)
            if pattern is None:
                break
            star_map = self.read_star_map(input_iter)
            offset = star_map.find_pattern_offset(pattern)
            self.results.append(offset)

    def output_results(self):
        for offset in self.results:
            if offset is not None:
                print(offset.dx, offset.dy)

def main():
    import sys
    detector = StarPatternDetector()
    detector.process(sys.stdin)
    detector.output_results()

if __name__ == '__main__':
    main()