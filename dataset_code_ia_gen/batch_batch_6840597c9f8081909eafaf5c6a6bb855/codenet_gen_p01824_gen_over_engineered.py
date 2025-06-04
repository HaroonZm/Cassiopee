class Coordinates3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def neighbors(self):
        # Neighbors in 6 directions
        return [
            Coordinates3D(self.x - 1, self.y, self.z),
            Coordinates3D(self.x + 1, self.y, self.z),
            Coordinates3D(self.x, self.y - 1, self.z),
            Coordinates3D(self.x, self.y + 1, self.z),
            Coordinates3D(self.x, self.y, self.z - 1),
            Coordinates3D(self.x, self.y, self.z + 1),
        ]

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if not isinstance(other, Coordinates3D):
            return False
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def in_bounds(self, dimensions):
        A, B, C = dimensions.A, dimensions.B, dimensions.C
        return 0 <= self.x < A and 0 <= self.y < B and 0 <= self.z < C


class Dimensions:
    def __init__(self, A: int, B: int, C: int):
        self.A = A
        self.B = B
        self.C = C


class CubeSolid:
    def __init__(self, dimensions: Dimensions, removed_cubes: set):
        self.dimensions = dimensions
        self.removed_cubes = removed_cubes
        self.total_cubes = self.dimensions.A * self.dimensions.B * self.dimensions.C

    def is_removed(self, coord: Coordinates3D) -> bool:
        return coord in self.removed_cubes

    def is_valid_coordinate(self, coord: Coordinates3D) -> bool:
        return coord.in_bounds(self.dimensions)

    def surface_area(self) -> int:
        # The total surface area is sum over all remaining cubes:
        # For each cube, each face that is not adjacent to another cube contributes 1 to surface area.
        # A cube's face is adjacent to another cube if neighbor cube exists and is not removed.
        # Because number of cubes can be huge but N (removed) small, we consider all cubes except removed.

        # Optimization: Instead of iterating over all remaining cubes (possibly huge),
        # we count outer faces by taking into account the removed cubes and boundaries.

        # Each cube has 6 faces.
        # For cubes not removed: number of total cubes: total_cubes - len(removed_cubes)
        remaining_cubes_count = self.total_cubes - len(self.removed_cubes)
        total_area = remaining_cubes_count * 6

        # Adjacent pairs share 2 faces, so subtract them out.
        # We calculate adjacencies of cubes remaining with other cubes remaining.

        # Instead of enumerating existing cubes (too large), we subtract adjacencies lost due to removal:
        # Total adjacency pairs in full solid:
        # adjacent pairs along x-axis: (A-1)*B*C
        # adjacent pairs along y-axis: A*(B-1)*C
        # adjacent pairs along z-axis: A*B*(C-1)
        total_adjacent_pairs = ((self.dimensions.A - 1) * self.dimensions.B * self.dimensions.C +
                                self.dimensions.A * (self.dimensions.B - 1) * self.dimensions.C +
                                self.dimensions.A * self.dimensions.B * (self.dimensions.C - 1))

        # Each adjacency removes 2 faces, total surface area full = 6*total_cubes - 2*total_adjacent_pairs
        full_solid_area = 6 * self.total_cubes - 2 * total_adjacent_pairs

        # Now, removals reduce the number of cubes and add exposed faces.
        # We'll compute the delta from full solid area

        # Delta: area_after_removal = full_solid_area - 6*#removed + 2*exposed_adjacents_among_removed_and_remaining
        # For each removed cube, 6 faces are removed from the solid.
        # However, for each adjacent cube (remaining) to a removed cube, 1 face is added (since that face becomes exposed)
        # Each adjacency between removed and remaining cubes adds 1 to surface area (because the removed cube's face is gone, exposing that face of neighbor cube)
        # But to count total surface area, the formula is:
        # surface_area = full_solid_area - 6*len(removed) + 2 * number_of_adjacent_pairs_between_removed_and_remaining

        # We compute adjacency pairs between removed cubes and remaining cubes
        adjacency_removed_remaining = 0
        removed_set = self.removed_cubes

        for removed_cube in removed_set:
            for neighbor in removed_cube.neighbors():
                if neighbor.in_bounds(self.dimensions) and not (neighbor in removed_set):
                    adjacency_removed_remaining += 1

        # adjacency_removed_remaining counts each adjacency once

        final_area = full_solid_area - 6 * len(removed_set) + 2 * adjacency_removed_remaining

        return final_area


class SurfaceAreaCalculator:
    def __init__(self):
        self.dimensions = None
        self.removed_cubes = set()

    def read_input(self):
        import sys
        input_data = sys.stdin.read().strip().split()
        A, B, C, N = map(int, input_data[0:4])
        self.dimensions = Dimensions(A, B, C)
        self.removed_cubes.clear()
        pos = 4
        for _ in range(N):
            x, y, z = map(int, input_data[pos:pos+3])
            pos += 3
            self.removed_cubes.add(Coordinates3D(x, y, z))

    def compute_and_output(self):
        solid = CubeSolid(self.dimensions, self.removed_cubes)
        ans = solid.surface_area()
        print(ans)


if __name__ == "__main__":
    calculator = SurfaceAreaCalculator()
    calculator.read_input()
    calculator.compute_and_output()