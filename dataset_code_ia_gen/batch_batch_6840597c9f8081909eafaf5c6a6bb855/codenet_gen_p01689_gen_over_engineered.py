from typing import List, Tuple, Set, Optional
from collections import deque

class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def neighbors(self, max_x: int, max_y: int) -> List['Coordinate']:
        candidates = [Coordinate(self.x - 1, self.y), Coordinate(self.x + 1, self.y),
                      Coordinate(self.x, self.y - 1), Coordinate(self.x, self.y + 1)]
        return [c for c in candidates if 0 <= c.x < max_x and 0 <= c.y < max_y]

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class MapCell:
    WALL = '#'
    EMPTY = '.'
    PLAYER = 'D'

    def __init__(self, type_char: str):
        if type_char not in (self.WALL, self.EMPTY, self.PLAYER):
            raise ValueError(f"Invalid cell type: {type_char}")
        self.type = type_char

    def walkable(self) -> bool:
        return self.type != self.WALL

class GridMap:
    def __init__(self, grid: List[List[MapCell]]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) if self.height > 0 else 0

    def is_walkable(self, coord: Coordinate) -> bool:
        if 0 <= coord.y < self.height and 0 <= coord.x < self.width:
            return self.grid[coord.y][coord.x].walkable()
        return False

    def find_player(self) -> Optional[Coordinate]:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].type == MapCell.PLAYER:
                    return Coordinate(x, y)
        return None

class DMachineResponse:
    def __init__(self, x: int, y: int, s: int):
        self.pos = Coordinate(x, y)
        self.s = s

class TreasureRange:
    """
    Defines the possible treasure locations given the D-machine response parameters and radius array.
    Because the D-machine is somewhat broken, the ranges can be contradictory.
    """
    def __init__(self, center: Coordinate, s: int, radii: List[int]):
        self.center = center
        self.s = s
        self.radii = radii

    def area_contains(self, pos: Coordinate) -> bool:
        # Manhattan or Euclidean is not appropriate, it's squares with radius in chessboard dist
        # It's a square centered at center with side length 2*r + 1
        d = max(abs(pos.x - self.center.x), abs(pos.y - self.center.y))
        if self.s == 0:
            # inside the smallest square of radius r_1
            return d <= self.radii[0]
        if 1 <= self.s <= len(self.radii) - 2:
            # annulus between r_s and r_{s+1}
            inner = self.radii[self.s - 1]
            outer = self.radii[self.s]
            return inner < d <= outer
        if self.s == len(self.radii) - 1:
            # outside the largest square (radius r_d)
            return d > self.radii[-1]
        # else a s value out of expected range - treat as no match:
        return False

class TreasurePossibilityMatrix:
    """
    Represents which grid cells can possibly contain the treasure after analyzing all responses.
    Each cell can be:
      - True: possibly treasure exists here
      - False: impossible to contain treasure
    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = [[True for _ in range(width)] for __ in range(height)]

    def intersect_with_response(self, grid_map: GridMap, response: DMachineResponse, radii: List[int]):
        new_matrix = [[False for _ in range(self.width)] for __ in range(self.height)]
        trange = TreasureRange(response.pos, response.s, radii)
        for y in range(self.height):
            for x in range(self.width):
                if not self.matrix[y][x]:
                    continue
                if not grid_map.is_walkable(Coordinate(x, y)):
                    # treasure cannot be in wall cells
                    continue
                if trange.area_contains(Coordinate(x, y)):
                    new_matrix[y][x] = True
        self.matrix = new_matrix

    def union_with_outside_response(self, grid_map: GridMap, response: DMachineResponse, radii: List[int]):
        """
        For s = d (max index) meaning treasure is outside the largest square.
        We implement filtering for this separately to not miss cells outside radius.
        """
        new_matrix = [[False for _ in range(self.width)] for __ in range(self.height)]
        max_r = radii[-1]
        cx, cy = response.pos.x, response.pos.y
        for y in range(self.height):
            for x in range(self.width):
                if not self.matrix[y][x]:
                    continue
                if not grid_map.is_walkable(Coordinate(x, y)):
                    continue
                dist = max(abs(x - cx), abs(y - cy))
                if dist > max_r:
                    new_matrix[y][x] = True
        self.matrix = new_matrix

    def has_no_possibility(self) -> bool:
        for row in self.matrix:
            if any(row):
                return False
        return True

    def possible_coords(self) -> List[Coordinate]:
        result = []
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x]:
                    result.append(Coordinate(x, y))
        return result

    def count_possibilities(self) -> int:
        return sum(sum(1 for c in row if c) for row in self.matrix)

class MovementGraph:
    """
    Encapsulate BFS shortest path or reachability between player and possible treasure locations.
    """
    def __init__(self, grid_map: GridMap):
        self.grid_map = grid_map

    def reachable_from(self, start: Coordinate) -> Set[Coordinate]:
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            pos = queue.popleft()
            for n in pos.neighbors(self.grid_map.width, self.grid_map.height):
                if n in visited:
                    continue
                if self.grid_map.is_walkable(n):
                    visited.add(n)
                    queue.append(n)
        return visited

class DowsingMachineSolver:
    def __init__(self, h: int, w: int, d: int, n_uses: int,
                 grid: List[List[str]],
                 radii: List[int],
                 responses: List[Tuple[int, int, int]]):
        self.height = h
        self.width = w
        self.d = d
        self.n_uses = n_uses
        self.grid_chars = grid
        self.radii = radii
        self.responses = [DMachineResponse(x, y, s) for (x, y, s) in responses]

        self.grid_map = self.build_map()
        self.player_pos = self.grid_map.find_player()
        if self.player_pos is None:
            raise RuntimeError("No player 'D' found on map.")

    def build_map(self) -> GridMap:
        map_cells = [[MapCell(c) for c in row] for row in self.grid_chars]
        return GridMap(map_cells)

    def calculate_treasure_possibility(self) -> TreasurePossibilityMatrix:
        matrix = TreasurePossibilityMatrix(self.width, self.height)
        # Applying the knowledge from all responses to narrow down possible treasure locations.
        # For each response, constraint the possibility matrix.
        for resp in self.responses:
            if resp.s == self.d:
                # Outside largest square
                matrix.union_with_outside_response(self.grid_map, resp, self.radii)
            else:
                matrix.intersect_with_response(self.grid_map, resp, self.radii)
            if matrix.has_no_possibility():
                # No possible treasure location satisfies all responses
                break
        return matrix

    def detect_broken(self, possibility_matrix: TreasurePossibilityMatrix) -> bool:
        # If no possible treasure locations remain, it means contradictory responses
        return possibility_matrix.has_no_possibility()

    def analyze_reachability(self, possibility_matrix: TreasurePossibilityMatrix) -> str:
        # There is exactly one treasure cell (somewhere with True in possibility_matrix).
        # We have to consider admit possibility that:
        # * all possible treasures can be reached from player position => "Yes"
        # * none can be reached => "No"
        # * some can be reached and some not => "Unknown"
        poss_coords = possibility_matrix.possible_coords()
        movement_graph = MovementGraph(self.grid_map)
        player_reachables = movement_graph.reachable_from(self.player_pos)

        can_reach = [pos in player_reachables for pos in poss_coords]

        if all(can_reach):
            return "Yes"
        if not any(can_reach):
            return "No"
        return "Unknown"

    def solve(self) -> str:
        # Step 1: compute treasure posibility matrix
        possibility_matrix = self.calculate_treasure_possibility()
        # Step 2: check if broken
        if self.detect_broken(possibility_matrix):
            return "Broken"
        # Step 3: analyze reachability of all possible treasure positions from player
        return self.analyze_reachability(possibility_matrix)

def main():
    h, w, d, n = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    radii = list(map(int, input().split()))
    responses = [tuple(map(int, input().split())) for _ in range(n)]

    solver = DowsingMachineSolver(h, w, d, n, grid, radii, responses)
    print(solver.solve())

if __name__ == "__main__":
    main()