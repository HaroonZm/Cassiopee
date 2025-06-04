from typing import List, Set, Tuple, Iterator

class Coordinate3D:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    def neighbors(self, max_dim: int) -> Iterator['Coordinate3D']:
        # Generate all 26 neighbors in 3D, excluding self
        for dz in (-1, 0, 1):
            nz = self.z + dz
            if 0 <= nz < max_dim:
                for dy in (-1, 0, 1):
                    ny = self.y + dy
                    if 0 <= ny < max_dim:
                        for dx in (-1, 0, 1):
                            nx = self.x + dx
                            if 0 <= nx < max_dim:
                                if dx != 0 or dy != 0 or dz != 0:
                                    yield Coordinate3D(nx, ny, nz)
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    def __hash__(self):
        return hash((self.x, self.y, self.z))

class Grid3D:
    def __init__(self, size: int):
        self.size = size
        # Represent 3D grid as set of occupied Coordinates for efficiency
        self.occupied: Set[Coordinate3D] = set()
    def set_cell(self, coord: Coordinate3D, alive: bool) -> None:
        if alive:
            self.occupied.add(coord)
        else:
            self.occupied.discard(coord)
    def is_alive(self, coord: Coordinate3D) -> bool:
        return coord in self.occupied
    def alive_neighbors_count(self, coord: Coordinate3D) -> int:
        count = 0
        for n in coord.neighbors(self.size):
            if n in self.occupied:
                count += 1
        return count
    def all_coordinates(self) -> Iterator[Coordinate3D]:
        for z in range(self.size):
            for y in range(self.size):
                for x in range(self.size):
                    yield Coordinate3D(x, y, z)
    def copy(self) -> 'Grid3D':
        new_grid = Grid3D(self.size)
        new_grid.occupied = set(self.occupied)
        return new_grid
    def __str__(self):
        # For output formatting per layer z=0..4
        layers = []
        for z in range(self.size):
            layer_lines = []
            for y in range(self.size):
                line_chars = []
                for x in range(self.size):
                    line_chars.append('1' if Coordinate3D(x, y, z) in self.occupied else '0')
                layer_lines.append("".join(line_chars))
            layers.append("\n".join(layer_lines))
        return "\n\n".join(layers)

class BirthDeathRules:
    def __init__(self, birth_counts: Set[int], survival_counts: Set[int]):
        self.birth_counts = birth_counts
        self.survival_counts = survival_counts
    def will_be_born(self, neighbor_count: int) -> bool:
        return neighbor_count in self.birth_counts
    def will_survive(self, neighbor_count: int) -> bool:
        return neighbor_count in self.survival_counts

class Simulation3D:
    def __init__(self, initial_grid: Grid3D, rules: BirthDeathRules, days: int):
        self.grid = initial_grid
        self.rules = rules
        self.days = days
    def step(self):
        new_grid = self.grid.copy()
        # We compute next states without modifying old state during checks
        changed_coords = set()
        # To optimize, we consider all coordinates or at least all occupied + neighbors
        candidates = set()
        for coord in self.grid.occupied:
            candidates.add(coord)
            for n in coord.neighbors(self.grid.size):
                candidates.add(n)

        for coord in candidates:
            alive = self.grid.is_alive(coord)
            count = self.grid.alive_neighbors_count(coord)
            if not alive and self.rules.will_be_born(count):
                new_grid.set_cell(coord, True)
            elif alive and not self.rules.will_survive(count):
                new_grid.set_cell(coord, False)
            # else no change

        self.grid = new_grid
    def run(self):
        for _ in range(self.days):
            self.step()

class InputParser:
    GRID_SIZE = 5
    def __init__(self):
        self.test_cases = []
    def parse_input(self):
        case_id = 1
        while True:
            N_line = ''
            while N_line.strip() == '':
                N_line = input()
            N = int(N_line.strip())
            if N == 0:
                break
            initial_grid = Grid3D(self.GRID_SIZE)
            # Read 5 layers, each layer 5 lines
            for z in range(self.GRID_SIZE):
                for y in range(self.GRID_SIZE):
                    line = input()
                    # line is length 5 string of 0/1
                    for x, ch in enumerate(line.strip()):
                        alive = ch == '1'
                        initial_grid.set_cell(Coordinate3D(x,y,z), alive)
                # One empty line after each layer
                input()
            # read M1 and a_i
            M1_line = input().strip()
            while M1_line == '':
                M1_line = input().strip()
            M1 = int(M1_line)
            a_values = []
            if M1 > 0:
                # May be in multiple lines, read enough values
                while len(a_values) < M1:
                    line = input().strip()
                    if line == '':
                        continue
                    a_values.extend(map(int, line.split()))
            # read M2 and b_j
            M2_line = input().strip()
            while M2_line == '':
                M2_line = input().strip()
            M2 = int(M2_line)
            b_values = []
            if M2 > 0:
                while len(b_values) < M2:
                    line = input().strip()
                    if line == '':
                        continue
                    b_values.extend(map(int, line.split()))
            self.test_cases.append( (case_id, N, initial_grid, BirthDeathRules(set(a_values), set(b_values))) )
            case_id += 1

class OutputWriter:
    @staticmethod
    def write(case_id: int, grid: Grid3D):
        print(f"Case {case_id}:")
        for z in range(grid.size):
            for y in range(grid.size):
                line_chars = []
                for x in range(grid.size):
                    line_chars.append('1' if Coordinate3D(x,y,z) in grid.occupied else '0')
                print("".join(line_chars))
            print()

def main():
    parser = InputParser()
    parser.parse_input()

    for case_id, N, initial_grid, rules in parser.test_cases:
        sim = Simulation3D(initial_grid, rules, N)
        sim.run()
        OutputWriter.write(case_id, sim.grid)

if __name__ == '__main__':
    main()