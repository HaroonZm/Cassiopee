class Direction(Enum):
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    EAST = 'EAST'
    WEST = 'WEST'

class Movement:
    def __init__(self, direction: Direction, step: int = 1):
        self.direction = direction
        self.step = step

    def __neg__(self):
        opposite = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }
        return Movement(opposite[self.direction], self.step)

    def __add__(self, other):
        if not isinstance(other, Movement):
            return NotImplemented
        if self.direction == other.direction:
            return Movement(self.direction, self.step + other.step)
        elif self.direction == Direction.NORTH and other.direction == Direction.SOUTH:
            diff = self.step - other.step
            if diff > 0:
                return Movement(Direction.NORTH, diff)
            elif diff < 0:
                return Movement(Direction.SOUTH, -diff)
            else:
                return None
        elif self.direction == Direction.SOUTH and other.direction == Direction.NORTH:
            diff = self.step - other.step
            if diff > 0:
                return Movement(Direction.SOUTH, diff)
            elif diff < 0:
                return Movement(Direction.NORTH, -diff)
            else:
                return None
        elif self.direction == Direction.EAST and other.direction == Direction.WEST:
            diff = self.step - other.step
            if diff > 0:
                return Movement(Direction.EAST, diff)
            elif diff < 0:
                return Movement(Direction.WEST, -diff)
            else:
                return None
        elif self.direction == Direction.WEST and other.direction == Direction.EAST:
            diff = self.step - other.step
            if diff > 0:
                return Movement(Direction.WEST, diff)
            elif diff < 0:
                return Movement(Direction.EAST, -diff)
            else:
                return None
        else:
            # Different directions, cannot combine
            return (self, other)

    def __eq__(self, other):
        return isinstance(other, Movement) and self.direction == other.direction and self.step == other.step

    def __repr__(self):
        return f"Movement({self.direction}, {self.step})"

class DirectionMapper:
    def __init__(self):
        self.mapping = {}
        for c in (chr(i) for i in range(ord('A'), ord('M') + 1)):
            self.mapping[c] = Direction.NORTH
        for c in (chr(i) for i in range(ord('N'), ord('Z') + 1)):
            self.mapping[c] = Direction.SOUTH
        for c in (chr(i) for i in range(ord('a'), ord('m') + 1)):
            self.mapping[c] = Direction.EAST
        for c in (chr(i) for i in range(ord('n'), ord('z') + 1)):
            self.mapping[c] = Direction.WEST

    def char_to_direction(self, c: str) -> Direction:
        return self.mapping[c]

class MovementAggregator:
    def __init__(self):
        self.north_steps = 0
        self.south_steps = 0
        self.east_steps = 0
        self.west_steps = 0

    def add_movement(self, movement: Movement):
        if movement.direction == Direction.NORTH:
            self.north_steps += movement.step
        elif movement.direction == Direction.SOUTH:
            self.south_steps += movement.step
        elif movement.direction == Direction.EAST:
            self.east_steps += movement.step
        elif movement.direction == Direction.WEST:
            self.west_steps += movement.step

    def combine(self):
        vertical = self.north_steps - self.south_steps
        horizontal = self.east_steps - self.west_steps
        return vertical, horizontal

class ShortestCryptEncoder:
    def __init__(self):
        self.dir_mapper = DirectionMapper()

    def encode(self, vertical: int, horizontal: int) -> str:
        res = []
        if vertical > 0:
            # north direction 'A' to 'M', arbitrarily choose 'A'
            res.append('A' * vertical)
        elif vertical < 0:
            # south direction 'N' to 'Z', choose 'N'
            res.append('N' * (-vertical))
        if horizontal > 0:
            # east direction 'a' to 'm', choose 'a'
            res.append('a' * horizontal)
        elif horizontal < 0:
            # west direction 'n' to 'z', choose 'n'
            res.append('n' * (-horizontal))
        return ''.join(res)

class CryptProcessor:
    def __init__(self, n: int, s: str):
        self.n = n
        self.s = s
        self.dir_mapper = DirectionMapper()
        self.aggregator = MovementAggregator()
        self.encoder = ShortestCryptEncoder()

    def process(self):
        for c in self.s:
            direction = self.dir_mapper.char_to_direction(c)
            movement = Movement(direction, 1)
            self.aggregator.add_movement(movement)
        vertical, horizontal = self.aggregator.combine()
        shortest = self.encoder.encode(vertical, horizontal)
        return shortest

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    s = input().rstrip('\n')
    processor = CryptProcessor(n, s)
    shortest = processor.process()
    print(len(shortest))
    print(shortest)

if __name__ == '__main__':
    from enum import Enum
    main()