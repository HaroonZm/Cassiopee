from abc import ABC, abstractmethod
from typing import List, Tuple

class Piece(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

    @abstractmethod
    def perimeter(self) -> int:
        pass

    @abstractmethod
    def cut(self, cut_start: int) -> Tuple['Piece', 'Piece']:
        pass

    @abstractmethod
    def edges(self) -> List[int]:
        pass

    @abstractmethod
    def width(self) -> int:
        pass

    @abstractmethod
    def depth(self) -> int:
        pass


class RectangularPiece(Piece):
    def __init__(self, w: int, d: int):
        if w < 1 or d < 1:
            raise ValueError("Width and depth must be positive integers.")
        self._w = w
        self._d = d

    def area(self) -> int:
        return self._w * self._d

    def width(self) -> int:
        return self._w

    def depth(self) -> int:
        return self._d

    def perimeter(self) -> int:
        # Perimeter of top view rectangle
        return 2 * (self._w + self._d)

    def edges(self) -> List[int]:
        # Edges lengths in order: top, right, bottom, left
        return [self._w, self._d, self._w, self._d]

    def cut(self, cut_start: int) -> Tuple['RectangularPiece', 'RectangularPiece']:
        # Simulates cutting this piece starting at cut_start distance clockwise from NW corner
        perim = self.perimeter()
        if cut_start <= 0 or cut_start >= perim:
            raise ValueError("cut_start must be within the perimeter, not at corners.")

        # Determine on which edge the cut_start lies (0-based index: 0 top, 1 right, 2 bottom, 3 left)
        edges = self.edges()
        accumulated = 0
        edge_index = -1
        for i, length in enumerate(edges):
            if accumulated < cut_start < accumulated + length:
                edge_index = i
                offset = cut_start - accumulated
                break
            accumulated += length
        else:
            # cut_start cannot be a corner so this should never happen
            raise ValueError("cut_start cannot be at a corner.")

        # The cut surface is orthogonal to the side face on which the starting point exists
        # That means we cut perpendicular to that edge inside the piece, splitting it into two.
        # Since the cake is always rectangular and vertical,
        # the cut line is aligned with edges either vertical or horizontal
        # Compute new subpieces dimensions depending on the edge cut.

        # For edges:
        # 0: top edge (cut surface vertical line parallel to vertical edges)
        # 1: right edge (cut surface horizontal line parallel to horizontal edges)
        # 2: bottom edge (same as top edge)
        # 3: left edge (same as right edge)

        if edge_index == 0:  # top edge
            # cut perpendicular to top edge -> vertical cut at position offset from NW corner eastwards
            cut_pos = offset
            if cut_pos <= 0 or cut_pos >= self._w:
                raise ValueError("Invalid cut position along width.")
            left_piece = RectangularPiece(cut_pos, self._d)
            right_piece = RectangularPiece(self._w - cut_pos, self._d)
        elif edge_index == 1:  # right edge
            # cut perpendicular to right edge -> horizontal cut at position offset from NE corner southwards
            cut_pos = offset
            if cut_pos <= 0 or cut_pos >= self._d:
                raise ValueError("Invalid cut position along depth.")
            upper_piece = RectangularPiece(self._w, cut_pos)
            lower_piece = RectangularPiece(self._w, self._d - cut_pos)
            left_piece, right_piece = upper_piece, lower_piece
        elif edge_index == 2:  # bottom edge
            # bottom edge counted cw from NW corner: starting point from SE corner going westward 
            # cut perpendicular to bottom edge -> vertical cut similar to top edge
            cut_pos = self._w - offset
            if cut_pos <= 0 or cut_pos >= self._w:
                raise ValueError("Invalid cut position along width.")
            left_piece = RectangularPiece(cut_pos, self._d)
            right_piece = RectangularPiece(self._w - cut_pos, self._d)
        else:  # edge_index == 3 left edge
            # cut perpendicular to left edge -> horizontal cut similar to right edge
            cut_pos = self._d - offset
            if cut_pos <= 0 or cut_pos >= self._d:
                raise ValueError("Invalid cut position along depth.")
            upper_piece = RectangularPiece(self._w, cut_pos)
            lower_piece = RectangularPiece(self._w, self._d - cut_pos)
            left_piece, right_piece = upper_piece, lower_piece

        # Return pieces such that the smaller area piece has smaller ID later on
        pieces = [left_piece, right_piece]
        pieces.sort(key=lambda p: p.area())
        return pieces[0], pieces[1]


class CakeCuttingSimulator:
    def __init__(self, initial_width: int, initial_depth: int):
        self.pieces: List[Piece] = [RectangularPiece(initial_width, initial_depth)]
        # Initially only one piece with ID 1

    def perform_cut(self, piece_id: int, cut_start: int):
        # piece_id 1-based
        idx = piece_id - 1
        target_piece = self.pieces[idx]

        # Cut the target piece
        p1, p2 = target_piece.cut(cut_start)

        # Replace target piece with the two new pieces maintaining ID assignment policy
        # Remove old piece
        self.pieces.pop(idx)
        # Add new pieces
        self.pieces.append(p1)
        self.pieces.append(p2)
        # Reassign IDs by sorting pieces by area ascending, stable for same area
        self.pieces.sort(key=lambda p: p.area())

    def get_sorted_areas(self) -> List[int]:
        return sorted(p.area() for p in self.pieces)


class InputParser:
    def __init__(self, lines: List[str]):
        self.lines = lines
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[int, int, int, List[Tuple[int,int]]]:
        if self.index >= len(self.lines):
            raise StopIteration

        line = self.lines[self.index].strip()
        if not line:
            self.index += 1
            return self.__next__()

        nwd = line.split()
        if len(nwd) < 3:
            self.index += 1
            return self.__next__()

        n, w, d = map(int, nwd)
        self.index += 1
        if n == 0 and w == 0 and d == 0:
            raise StopIteration

        cuts = []
        for _ in range(n):
            p_s_line = self.lines[self.index].strip()
            self.index += 1
            p_i, s_i = map(int, p_s_line.split())
            cuts.append((p_i, s_i))

        return n, w, d, cuts


def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    parser = InputParser(input_lines)
    try:
        while True:
            n, w, d, cuts = next(parser)
            simulator = CakeCuttingSimulator(w, d)
            for idx, (pi, si) in enumerate(cuts, start=1):
                simulator.perform_cut(pi, si)
            areas = simulator.get_sorted_areas()
            print(' '.join(map(str, areas)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()