from collections import deque
from typing import Tuple, Dict, List, Optional, Set, Iterator


# Define types for clarity
Position = Tuple[int, int]
Orientation = Tuple[str, str, str, str, str, str]  # top, bottom, north, south, east, west faces


class Cube:
    """
    Cube class models the colored cube and its rolling behavior.
    Faces are stored as a tuple of 6 colors in order:
    top, bottom, north, south, east, west
    """
    def __init__(self, faces: Orientation):
        self.faces = faces

    def roll(self, direction: str) -> 'Cube':
        """
        Returns a new Cube instance after rolling in the direction
        direction: one of 'N', 'S', 'E', 'W'.
        """
        t, b, n, s, e, w = self.faces
        if direction == 'N':
            # Roll forward (north): top->south, south->bottom, bottom->north, north->top
            return Cube((s, n, t, b, e, w))
        elif direction == 'S':
            # Roll backward (south): top->north, north->bottom, bottom->south, south->top
            return Cube((n, s, b, t, e, w))
        elif direction == 'E':
            # Roll right (east): top->west, west->bottom, bottom->east, east->top
            return Cube((w, e, n, s, t, b))
        elif direction == 'W':
            # Roll left (west): top->east, east->bottom, bottom->west, west->top
            return Cube((e, w, n, s, b, t))
        else:
            raise ValueError(f"Invalid roll direction: {direction}")

    @property
    def top(self) -> str:
        return self.faces[0]

    def __hash__(self):
        return hash(self.faces)

    def __eq__(self, other):
        return isinstance(other, Cube) and self.faces == other.faces


class Bed:
    """
    Bed class models the bed map with colored squares.
    """
    COLORS = {'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k'}

    def __init__(self, w: int, d: int, grid: List[str]):
        self.width = w
        self.depth = d
        self.grid = grid  # list of strings, each w chars

    def color_at(self, pos: Position) -> str:
        x, y = pos
        return self.grid[y][x]

    def in_bounds(self, pos: Position) -> bool:
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.depth

    def is_black(self, pos: Position) -> bool:
        return self.color_at(pos) == 'k'

    def is_white(self, pos: Position) -> bool:
        return self.color_at(pos) == 'w'

    def is_colored(self, pos: Position) -> bool:
        return self.color_at(pos) in {'r', 'g', 'b', 'c', 'm', 'y'}

    def find_char(self, ch: str) -> Position:
        for y in range(self.depth):
            for x in range(self.width):
                if self.grid[y][x] == ch:
                    return (x, y)
        raise ValueError(f"Character {ch} not in bed")

    def find_white_initial(self) -> Position:
        # The single '#' mark cell is a white cell and initial position of cube
        for y in range(self.depth):
            for x in range(self.width):
                if self.grid[y][x] == '#':
                    return (x, y)
        raise ValueError("No initial '#' white square found")

    def all_color_positions(self) -> Dict[str, Position]:
        """
        Return a dict {color_char: (x,y)} for all colored squares present (r,g,b,c,m,y)
        """
        res = {}
        for y in range(self.depth):
            for x in range(self.width):
                c = self.grid[y][x]
                if c in {'r','g','b','c','m','y'}:
                    res[c] = (x,y)
        return res


class TravelingCubeSolver:
    """
    Solve the traveling cube problem with a highly extensible, layered approach.
    """

    # Directions and vector shifts
    DIRECTIONS = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    def __init__(self, bed: Bed, visit_order: str):
        self.bed = bed
        self.visit_order = visit_order
        self.color_positions = bed.all_color_positions()
        self.initial_pos = bed.find_white_initial()

        # Initial cube face colors fixed by problem description:
        # top=r, bottom=c, north=g, south=m, east=b, west=y, but permuted by input order of faces in input line
        # Note: The last input line is the permutation of 'rgbcmy' which assigns the colored cube's initial face colors order:
        # We must decode this correctly:
        #
        # The problem states initial:
        # top red (r)
        # bottom cyan (c)
        # north green (g)
        # south magenta (m)
        # east blue (b)
        # west yellow (y)
        #
        # The last line input is a permutation of 'rgbcmy' - it's the order of the colors of the cube's faces 
        # in the order top, bottom, north, south, east, west - so we must reorder accordingly.
        self.initial_faces_input = 'rgbcmy'
        # To be set by input line with the actual permutation string
        self.initial_faces: Orientation = ('r','c','g','m','b','y')  # default to this

    def set_initial_faces(self, perm: str):
        # perm is 6-length string permutation of 'rgbcmy'
        # We decode the face colors relative to indices:
        # indices: 0=top,1=bottom,2=north,3=south,4=east,5=west
        # The problem gives the canonical order:
        # top -> 'r'
        # bottom -> 'c'
        # north -> 'g'
        # south -> 'm'
        # east -> 'b'
        # west -> 'y'
        # But the input line perm is a permutation of these colors
        #
        # I.e. each position of perm gives the color at that position in the cube initial faces order
        # We must map canonical face positions to the perm order. So since the initial canonical order is:
        # (r,c,g,m,b,y)
        # and perm is a permutation of those chars,
        # the faces colors after perm are just this perm string characters in order top to west
        assert sorted(perm) == sorted('rgbcmy'), f"Invalid face colors permutation line {perm}"
        self.initial_faces = tuple(perm)

    def solve(self) -> Optional[int]:
        """
        Return minimum steps to achieve the visit_order visiting sequence
        or None if unreachable.
        """
        # We will model the problem as multi-stage BFS with a joint state:
        # (position, cube_orientation, visit_index)
        # Where:
        # - position: (x, y) on the bed grid
        # - cube_orientation: the cube's 6-face colors in order
        # - visit_index: how many colored squares in visit_order have been visited (current target to visit is visit_order[visit_index])

        # BFS must search shortest step count from start at:
        # pos = initial position (the '#', a white cell)
        # cube = Cube with initial_faces colors
        # visit_index = 0 (to visit first colored square in visit_order)

        start_cube = Cube(self.initial_faces)
        start_state = (self.initial_pos, start_cube.faces, 0)

        # Visited states to prevent cycles:
        # Key: (x,y, cube_orientation tuple, visit_index)
        visited = set()
        visited.add(start_state)

        queue = deque([(self.initial_pos, start_cube, 0, 0)])  # pos, cube object, visit_index, steps

        color_targets = self.visit_order

        while queue:
            pos, cube, v_idx, steps = queue.popleft()
            if v_idx == 6:
                # All targets visited
                return steps
            # Current target color to visit next
            target_color = color_targets[v_idx]

            x, y = pos
            for d in self.DIRECTIONS.keys():
                dx, dy = self.DIRECTIONS[d]
                nx, ny = x+dx, y+dy
                npos = (nx, ny)

                if not self.bed.in_bounds(npos):
                    continue
                ccolor = self.bed.color_at(npos)
                if ccolor == 'k':
                    # Cannot roll onto black squares
                    continue
                # Apply the roll to cube to get new orientation
                new_cube = cube.roll(d)

                # Check the cube top color matches required condition if chromatic square
                if ccolor in {'r','g','b','c','m','y'}:
                    # Cube top face after roll must be equal to square color
                    if new_cube.top != ccolor:
                        continue

                # Check visit rules:
                # chromatic squares can be visited only once in order of visit_order,
                # white squares can be visited arbitrarily many times,
                # black squares forbidden (already checked).
                # Also the cube must visit chromatic squares in order visit_order.

                # Determine the next visit state after moving to npos
                next_v_idx = v_idx
                # If ccolor is target color to visit now and the pos is at that colored square, we move forward in the list
                if v_idx < 6 and ccolor == target_color:
                    # The cube visits the current target color on this step
                    next_v_idx = v_idx + 1

                # To guarantee the chromatic squares visited only once in order, we only advance visit index in order.
                # Visiting chromatic squares out of order or twice is blocked by this logic.

                state_key = (npos, new_cube.faces, next_v_idx)
                if state_key in visited:
                    continue
                visited.add(state_key)
                queue.append((npos, new_cube, next_v_idx, steps+1))

        return None


def main() -> None:
    import sys
    input_lines = iter(sys.stdin.read().splitlines())

    while True:
        hdr = next(input_lines).strip()
        if hdr == '0 0':
            break
        w, d = map(int, hdr.split())
        grid = []
        for _ in range(d):
            line = next(input_lines)
            # Replace '#' with 'w' internally but remember initial '#' position
            # However, the problem states '#' means white and starting cube position
            # We'll keep '#' to detect initial after reading all lines
            grid.append(line)

        visit_order = next(input_lines).strip()
        bed = Bed(w, d, grid)
        solver = TravelingCubeSolver(bed, visit_order)
        solver.set_initial_faces(visit_order)  # According to problem input, the last line is cube face perm
        # Actually problem states last line is the permutation of 'rgbcmy' and shows the cube's face colors order
        # Problem sample inputs seem to provide this line for each dataset
        # We must call set_initial_faces once per dataset to set the initial cube orientation before BFS

        result = solver.solve()
        if result is None:
            print("unreachable")
        else:
            print(result)


if __name__ == "__main__":
    main()