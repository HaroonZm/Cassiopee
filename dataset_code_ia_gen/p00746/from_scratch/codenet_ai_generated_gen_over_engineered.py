from typing import List, Tuple, Dict, Protocol
from enum import Enum, auto


class Direction(Enum):
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3

    @staticmethod
    def from_int(value: int) -> 'Direction':
        mapping = {
            0: Direction.LEFT,
            1: Direction.DOWN,
            2: Direction.RIGHT,
            3: Direction.UP,
        }
        return mapping[value]


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def neighbor(self, direction: Direction) -> 'Position':
        if direction == Direction.LEFT:
            return Position(self.x - 1, self.y)
        elif direction == Direction.DOWN:
            return Position(self.x, self.y - 1)
        elif direction == Direction.RIGHT:
            return Position(self.x + 1, self.y)
        elif direction == Direction.UP:
            return Position(self.x, self.y + 1)
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def __repr__(self):
        return f"Position({self.x}, {self.y})"


class Drawable(Protocol):
    def place(self, base_index: int, direction: Direction) -> None:
        ...

    def bounds(self) -> Tuple[int, int, int, int]:
        ...


class SquareArtPiece(Drawable):
    def __init__(self, n_squares: int):
        self.n_squares = n_squares
        self.positions: Dict[int, Position] = {0: Position(0, 0)}
        # Track min and max for width and height calculation incrementally
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def place(self, base_index: int, direction: Direction) -> None:
        if base_index not in self.positions:
            raise ValueError(f"Base square {base_index} is not placed yet.")
        new_index = len(self.positions)
        if new_index >= self.n_squares:
            raise ValueError("All squares have already been placed.")
        base_pos = self.positions[base_index]
        new_pos = base_pos.neighbor(direction)
        # No overlap is guaranteed, but let's assert it
        if new_pos in self.positions.values():
            raise ValueError("Overlap detected, invalid placement.")
        self.positions[new_index] = new_pos
        # Update bounds
        self.min_x = min(self.min_x, new_pos.x)
        self.max_x = max(self.max_x, new_pos.x)
        self.min_y = min(self.min_y, new_pos.y)
        self.max_y = max(self.max_y, new_pos.y)

    def place_at_index(self, square_index: int, base_index: int, direction: Direction) -> None:
        # Used for placing squares in arbitrary order
        if base_index not in self.positions:
            raise ValueError(f"Base square {base_index} not placed yet.")
        if square_index in self.positions:
            raise ValueError(f"Square {square_index} already placed.")
        base_pos = self.positions[base_index]
        new_pos = base_pos.neighbor(direction)
        if new_pos in self.positions.values():
            raise ValueError("Overlap detected, invalid placement.")
        self.positions[square_index] = new_pos
        self.min_x = min(self.min_x, new_pos.x)
        self.max_x = max(self.max_x, new_pos.x)
        self.min_y = min(self.min_y, new_pos.y)
        self.max_y = max(self.max_y, new_pos.y)

    def bounds(self) -> Tuple[int, int]:
        width = self.max_x - self.min_x + 1
        height = self.max_y - self.min_y + 1
        return width, height


class ArtFactory:
    def __init__(self):
        pass

    def build_art_piece(self, n: int, instructions: List[Tuple[int, int]]) -> SquareArtPiece:
        art = SquareArtPiece(n)
        # Instructions are (ni, di) for i=1..n-1, numbered square i, placed next to ni to direction di
        # Since instructions may come in any order, place squares accordingly
        # We will process instructions incrementally:
        # For i in 1 to n-1, the input says square i placed adjacent to ni in direction di
        # We keep a map of pending placement so we can place when base square is ready
        to_place = {i: (ni, Direction.from_int(di)) for i, (ni, di) in enumerate(instructions, start=1)}
        placed = {0}
        while to_place:
            to_remove = []
            for sq_i, (base_i, dir_i) in to_place.items():
                if base_i in placed:
                    art.place_at_index(sq_i, base_i, dir_i)
                    placed.add(sq_i)
                    to_remove.append(sq_i)
            if not to_remove:
                # No squares placed this iteration, cycle or error
                raise RuntimeError("Cannot resolve placement of squares, input malformed.")
            for rem in to_remove:
                del to_place[rem]
        return art


class InputParser:
    @staticmethod
    def parse_inputs() -> List[Tuple[int, List[Tuple[int, int]]]]:
        datasets = []
        while True:
            line = ''
            while line.strip() == '':
                line = input()
            n = int(line.strip())
            if n == 0:
                break
            instructions = []
            count = n - 1
            while count > 0:
                line = input().strip()
                while line == '':
                    line = input().strip()
                parts = line.split()
                if len(parts) != 2:
                    # Defensive: skip faulty input lines
                    continue
                ni, di = int(parts[0]), int(parts[1])
                instructions.append((ni, di))
                count -= 1
            datasets.append((n, instructions))
        return datasets


class OutputFormatter:
    @staticmethod
    def format_and_print(width: int, height: int) -> None:
        # According to spec: "output a line that contains the width and the height of the piece of artwork as decimal numbers, separated by a space."
        print(f"{width} {height}")


class PabloSquarsonHeadache:
    def __init__(self):
        self.factory = ArtFactory()
        self.parser = InputParser()
        self.formatter = OutputFormatter()

    def run(self) -> None:
        datasets = self.parser.parse_inputs()
        for n, instructions in datasets:
            art_piece = self.factory.build_art_piece(n, instructions)
            w, h = art_piece.bounds()
            self.formatter.format_and_print(w, h)


if __name__ == "__main__":
    app = PabloSquarsonHeadache()
    app.run()