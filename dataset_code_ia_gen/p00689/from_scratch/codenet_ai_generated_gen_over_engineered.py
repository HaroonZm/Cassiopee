import math
import sys
from typing import Tuple, List, Optional, Iterable


class Vector2D:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def normalize(self) -> 'Vector2D':
        l = self.length()
        if l == 0:
            return Vector2D(0.0, 0.0)
        return Vector2D(self.x / l, self.y / l)

    def dot(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Vector2D') -> float:
        return self.x * other.y - self.y * other.x

    def angle_to_right(self, other: 'Vector2D') -> float:
        # Returns angle from self to other turning right (clockwise) between 0 and 2pi
        # Because clockwise is right turn: angle is 2*pi - CCW_angle
        ccw_angle = math.atan2(other.cross(self), other.dot(self))
        if ccw_angle < 0:
            ccw_angle += 2 * math.pi
        right_angle = 2 * math.pi - ccw_angle
        if right_angle >= 2 * math.pi:
            right_angle -= 2 * math.pi
        return right_angle

    def __repr__(self):
        return f"Vector2D({self.x:.3f},{self.y:.3f})"

    
class Flag:
    __slots__ = ('position',)

    def __init__(self, x: float, y: float):
        self.position = Vector2D(x, y)

    def distance_from(self, point: Vector2D) -> float:
        return (self.position - point).length()


class SpiralFootrace:
    def __init__(self, flags: List[Flag]):
        # The start flag is fixed at origin
        # We insert (0,0) flag explicitly
        self.flags: List[Flag] = [Flag(0.0, 0.0)] + flags
        self.visited = [False] * len(self.flags)
        self.visited[0] = True  # starting point is visited
        self.path_length: float = 0.0
        self.current_index: int = 0
        self.facing_direction: Vector2D = Vector2D(0.0, 1.0)  # initial direction: north

    def solve(self) -> float:
        visit_count = 1
        total_flags = len(self.flags)
        while visit_count < total_flags:
            next_index = self._select_next_flag(self.current_index, self.facing_direction)
            if next_index is None:
                break  # no more flags to visit
            self._advance_to(next_index)
            visit_count += 1
        return self.path_length

    def _select_next_flag(self, current_index: int, facing: Vector2D) -> Optional[int]:
        current_pos = self.flags[current_index].position
        candidates = []
        for i, flag in enumerate(self.flags):
            if self.visited[i]:
                continue
            direction_vec = (flag.position - current_pos)
            # If direction vector zero (same point), skip
            if direction_vec.x == 0 and direction_vec.y == 0:
                continue
            angle = facing.angle_to_right(direction_vec)
            dist = direction_vec.length()
            candidates.append((angle, dist, i))
        if not candidates:
            return None
        # Sort by smallest angle to the right, then nearest distance
        candidates.sort(key=lambda x: (x[0], x[1]))
        return candidates[0][2]

    def _advance_to(self, next_index: int):
        current_pos = self.flags[self.current_index].position
        next_pos = self.flags[next_index].position
        vector = next_pos - current_pos
        dist = vector.length()
        self.path_length += dist
        self.current_index = next_index
        self.visited[next_index] = True
        self.facing_direction = vector.normalize()


class InputParser:
    def __init__(self, source: Iterable[str]):
        self.source = source

    def parse_all_cases(self) -> Iterable[List[Tuple[int, int]]]:
        it = iter(self.source)
        while True:
            line = self._read_non_empty_line(it)
            if line is None:
                break
            n = int(line)
            if n == 0:
                break
            flags = []
            while len(flags) < n:
                line = self._read_non_empty_line(it)
                if line is None:
                    raise EOFError("Unexpected end of input while reading flags")
                parts = line.split()
                for i in range(0, len(parts), 2):
                    x = int(parts[i])
                    y = int(parts[i + 1])
                    flags.append((x, y))
            yield flags

    @staticmethod
    def _read_non_empty_line(it) -> Optional[str]:
        for line in it:
            line = line.strip()
            if line:
                return line
        return None


def main():
    parser = InputParser(sys.stdin)
    for flag_positions in parser.parse_all_cases():
        flags = [Flag(x, y) for (x, y) in flag_positions]
        race = SpiralFootrace(flags)
        length = race.solve()
        print(f"{length:.1f}")


if __name__ == "__main__":
    main()