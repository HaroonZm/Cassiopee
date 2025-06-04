from collections import deque
from copy import deepcopy
from typing import List, Tuple, Dict, Set

class Face:
    """Represents a face of the cube with a 3x3 grid of holes."""
    def __init__(self, grid: List[List[str]]):
        self.grid = grid  # 3x3 list of '.' or '*'

    @classmethod
    def from_lines(cls, lines: List[str]) -> 'Face':
        return cls([list(line) for line in lines])

    def rotate_cw(self) -> 'Face':
        """Return a new Face rotated clockwise (90 degrees)."""
        new_grid = [ [self.grid[2-j][i] for j in range(3)] for i in range(3) ]
        return Face(new_grid)

    def rotate_ccw(self) -> 'Face':
        """Return a new Face rotated counterclockwise (90 degrees)."""
        new_grid = [ [self.grid[j][2-i] for j in range(3)] for i in range(3) ]
        return Face(new_grid)

    def __getitem__(self, idx):
        return self.grid[idx]

    def __eq__(self, other):
        if not isinstance(other, Face):
            return False
        return self.grid == other.grid

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.grid))

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

class CubeState:
    """
    Represents the state of the cube with all six faces.
    Faces order: front, right, back, left, top, bottom
    Each face is a Face object.
    """

    def __init__(self, faces: List[Face]):
        self.faces = faces  # list of 6 Face objects

    def __eq__(self, other):
        if not isinstance(other, CubeState):
            return False
        return all(self.faces[i] == other.faces[i] for i in range(6))

    def __hash__(self):
        return hash(tuple(self.faces))

    def clone(self) -> 'CubeState':
        new_faces = [Face([row[:] for row in f.grid]) for f in self.faces]
        return CubeState(new_faces)

    def __str__(self) -> str:
        names = ['front', 'right', 'back', 'left', 'top', 'bottom']
        return '\n'.join(f"{names[i]}:\n{str(self.faces[i])}" for i in range(6))

class DiceRoomPuzzle:
    """
    Core class to model the Dice Room puzzle.
    It tracks the cube configuration and can apply rotations.
    """

    # Faces indices
    F, R, B, L, T, D = range(6)

    def __init__(self, initial_faces: List[Face]):
        self.initial_state = CubeState(initial_faces)

        # Precompute rotation functions for 4 directions
        # The rotations correspond to cube rolling north, east, south, west

    def _roll_north(self, state: CubeState) -> CubeState:
        """
        Rotate the cube as if rolling forward (north).
        According to the problem description, the dice rotates such that front goes to top,
        bottom goes to front, back goes to bottom, top goes to back.
        The right and left faces rotate in place.
        The faces on side remain same but may need internal rotation.
        """
        f, r, b, l, t, d = state.faces

        # New faces after rolling north:
        # front -> top, bottom -> front, back -> bottom, top -> back
        # Need to rotate left and right faces because cube rotated along front-back axis
        # When cube rolls forward, left and right faces rotate 90 degrees.

        new_faces = [None]*6
        new_faces[self.T] = f
        new_faces[self.F] = d
        new_faces[self.D] = b
        new_faces[self.B] = t

        # left face rotates CW
        new_faces[self.L] = l.rotate_cw()
        # right face rotates CCW
        new_faces[self.R] = r.rotate_ccw()

        return CubeState(new_faces)

    def _roll_south(self, state: CubeState) -> CubeState:
        # Opposite of roll north
        f, r, b, l, t, d = state.faces

        new_faces = [None]*6
        new_faces[self.B] = f
        new_faces[self.D] = b
        new_faces[self.F] = t
        new_faces[self.T] = d

        # left face rotates CCW
        new_faces[self.L] = l.rotate_ccw()
        # right face rotates CW
        new_faces[self.R] = r.rotate_cw()

        return CubeState(new_faces)

    def _roll_east(self, state: CubeState) -> CubeState:
        f, r, b, l, t, d = state.faces

        new_faces = [None]*6
        new_faces[self.R] = f
        new_faces[self.D] = r
        new_faces[self.L] = d
        new_faces[self.F] = l

        # top face rotates CW
        new_faces[self.T] = t.rotate_cw()
        # bottom face rotates CCW
        new_faces[self.B] = b.rotate_ccw()

        return CubeState(new_faces)

    def _roll_west(self, state: CubeState) -> CubeState:
        f, r, b, l, t, d = state.faces

        new_faces = [None]*6
        new_faces[self.L] = f
        new_faces[self.F] = r
        new_faces[self.R] = d
        new_faces[self.D] = l

        # top face rotates CCW
        new_faces[self.T] = t.rotate_ccw()
        # bottom face rotates CW
        new_faces[self.B] = b.rotate_cw()

        return CubeState(new_faces)

    def _neighbors(self, state: CubeState) -> List[Tuple[CubeState,int]]:
        """
        Return list of possible next states with cost 1 each.
        The cube can be rolled east, west, north, south.
        """
        return [
            (self._roll_north(state), 1),
            (self._roll_east(state), 1),
            (self._roll_south(state), 1),
            (self._roll_west(state), 1)
        ]

    def can_escape(self, state: CubeState) -> bool:
        """
        According to problem, escape is possible if * at any of bottom three squares on front and back face.
        The "bottom three squares" means the middle cells of the bottom row of front and back faces?
        In the problem statement: "you should have holes on at least one of lower three squares on the front and back side of the room."
        Given a 3x3 grid, "lower three squares" is probably the entire bottom row (row index 2) of front and back.

        So, if any cell in row 2 (the last row) of front or back face has '*', escape is possible.
        """

        for face_idx in [self.F, self.B]:
            row = state.faces[face_idx].grid[2]  # bottom row
            if '*' in row:
                return True
        return False

    def min_rotations_to_escape(self) -> int:
        """
        Use BFS to find minimum rotations from initial state to a state where escape is possible.
        """

        queue = deque()
        visited: Set[CubeState] = set()

        queue.append((self.initial_state, 0))
        visited.add(self.initial_state)

        while queue:
            current_state, dist = queue.popleft()

            if self.can_escape(current_state):
                return dist

            for next_state, cost in self._neighbors(current_state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, dist + cost))

        # Problem states all datasets have solution, so no fallback needed
        raise RuntimeError("No solution found for dataset.")

class InputParser:
    @staticmethod
    def parse_dataset(lines: List[str]) -> List[Face]:
        """
        Parses a dataset consisting of 6 faces * 3 lines each.
        Returns list of 6 Face objects in order: front, right, back, left, top, bottom.
        """
        faces = []
        idx = 0
        for _ in range(6):
            face_lines = lines[idx:idx+3]
            idx += 3
            faces.append(Face.from_lines(face_lines))
        return faces

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()

    datasets = []
    current_dataset_lines = []

    for line in input_lines:
        if line == '#':
            break
        if line.strip() == '' and current_dataset_lines:
            # parse this dataset
            datasets.append(current_dataset_lines)
            current_dataset_lines = []
        elif line.strip() != '':
            current_dataset_lines.append(line)

    # last dataset (if no trailing blank line before #)
    if current_dataset_lines:
        datasets.append(current_dataset_lines)

    for dataset_lines in datasets:
        faces = InputParser.parse_dataset(dataset_lines)
        puzzle = DiceRoomPuzzle(faces)
        ans = puzzle.min_rotations_to_escape()
        print(ans)

if __name__ == "__main__":
    main()