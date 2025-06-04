class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def is_within_bounds(self):
        return 0 <= self.x <= 9 and 0 <= self.y <= 9

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class FrogJump:
    # The frog can only jump in these directions from (b): fixed jump offsets
    VALID_JUMPS = [
        Point(-2, -1), Point(-2, 1), Point(-1, 2), Point(1, 2),
        Point(2, 1), Point(2, -1), Point(1, -2), Point(-1, -2)
    ]

    def __init__(self, position: Point):
        self.position = position

    def possible_next_positions(self):
        candidates = [self.position + jump for jump in self.VALID_JUMPS]
        return [p for p in candidates if p.is_within_bounds()]


class Sprinkler:
    # The sprinkler waters 5 positions: itself and orthogonally 4 positions
    # from (c)
    WATER_OFFSETS = [
        Point(0, 0), Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)
    ]

    def __init__(self, position: Point):
        self.position = position
        self.water_positions = set()
        for offset in self.WATER_OFFSETS:
            candidate = position + offset
            if candidate.is_within_bounds():
                self.water_positions.add(candidate)

    def waters(self, point: Point):
        return point in self.water_positions


class Park:
    def __init__(self, frog: FrogJump, sprinklers: list):
        self.frog = frog
        self.sprinklers = sprinklers

    def can_survive(self) -> bool:
        # We must test if there's a position sequence where frog can be on water for each sprinkler
        # exactly one jump at sprinkler activation (frog can only jump once between consecutive sprinklers).
        # The frog initially jumps at the first sprinkler activation.

        n = len(self.sprinklers)

        # dp[i] will be a set of frog positions that can be standing on sprinkler i's watering area.
        dp = [set() for _ in range(n)]

        # Initialize dp[0]: frog jumps once at first sprinkler activation from initial position.
        first_sprinkler = self.sprinklers[0]
        # From initial position, only one jump allowed immediately.
        for pos in self.frog.possible_next_positions():
            if first_sprinkler.waters(pos):
                dp[0].add(pos)
        if not dp[0]:
            return False

        # For each subsequent sprinkler activation i, the frog can jump once from any position in dp[i-1]
        for i in range(1, n):
            sprinkler = self.sprinklers[i]
            new_positions = set()
            for prev_pos in dp[i - 1]:
                # From prev_pos one jump allowed (frog can rest here, so no jumps in between sprinkler activations)
                intermediate_frog = FrogJump(prev_pos)
                for next_pos in intermediate_frog.possible_next_positions():
                    if sprinkler.waters(next_pos):
                        new_positions.add(next_pos)
            dp[i] = new_positions
            if not dp[i]:
                return False

        return True


class InputParser:
    @staticmethod
    def parse_sets():
        import sys
        lines = sys.stdin.read().strip().split('\n')
        i = 0
        while i < len(lines):
            px_py = lines[i].strip()
            if px_py == '0 0':
                break
            px, py = map(int, px_py.split())
            i += 1
            n = int(lines[i].strip())
            i += 1
            sprinkler_line = lines[i].strip()
            sprinkler_coords = list(map(int, sprinkler_line.split()))
            i += 1
            sprinklers = []
            for si in range(n):
                x, y = sprinkler_coords[2*si], sprinkler_coords[2*si+1]
                sprinklers.append(Sprinkler(Point(x, y)))
            yield px, py, sprinklers


def main():
    for px, py, sprinklers in InputParser.parse_sets():
        frog = FrogJump(Point(px, py))
        park = Park(frog, sprinklers)
        print("OK" if park.can_survive() else "NA")


if __name__ == '__main__':
    main()