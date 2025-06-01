import sys
from abc import ABC, abstractmethod
from typing import List


class DimensionError(Exception):
    pass


class Coordinate:
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def inside(self, cuboid: "Cuboid") -> bool:
        return cuboid.min_x <= self.x <= cuboid.max_x and \
               cuboid.min_y <= self.y <= cuboid.max_y and \
               cuboid.min_z <= self.z <= cuboid.max_z


class Cuboid:
    def __init__(self, center: Coordinate, length_x: float, length_y: float, length_z: float):
        if length_x <= 0 or length_y <= 0 or length_z <= 0:
            raise DimensionError("All lengths must be positive")
        self.center = center
        self.length_x = length_x
        self.length_y = length_y
        self.length_z = length_z

    @property
    def min_x(self):
        return self.center.x - self.length_x / 2

    @property
    def max_x(self):
        return self.center.x + self.length_x / 2

    @property
    def min_y(self):
        return self.center.y - self.length_y / 2

    @property
    def max_y(self):
        return self.center.y + self.length_y / 2

    @property
    def min_z(self):
        return self.center.z - self.length_z / 2

    @property
    def max_z(self):
        return self.center.z + self.length_z / 2

    def contains(self, coord: Coordinate) -> bool:
        return coord.inside(self)

    def volume(self) -> float:
        return self.length_x * self.length_y * self.length_z


class Tank(Cuboid):
    def __init__(self, n: int):
        # Tank centered at origin for conceptual clarity
        super().__init__(Coordinate(0, 0, 0), n, n, 2)
        self.n = n


class Sludge(Cuboid):
    def __init__(self, tank: Tank):
        # Sludge fills the tank to height 1 from bottom z=-1 to z=0
        center = Coordinate(0, 0, -0.5)  # center within tank bottom half
        super().__init__(center, tank.length_x, tank.length_y, 1)


class Tile(ABC):
    SIZE = 1  # 1x1 tile on walls

    @abstractmethod
    def position(self) -> Coordinate:
        pass


class WallTile(Tile):
    def __init__(self, x: int, y: int, z: int):
        self._position = Coordinate(x, y, z)

    def position(self) -> Coordinate:
        return self._position


class WallInterface(ABC):
    @abstractmethod
    def tile_positions(self) -> List[Coordinate]:
        pass


class TankWalls(WallInterface):
    def __init__(self, tank: Tank):
        self.tank = tank

    def tile_positions(self) -> List[Coordinate]:
        positions = []
        n = self.tank.n
        half = n // 2
        # Walls cover the vertical sides of tank from z = -1 to z = 1
        # z coordinates for tiles placed: from floor -1 to ceiling 1 (2 length total)
        # Tiles size 1 means z can be -1 to 0 and 0 to 1 for 2 tiles high
        z_levels = [-1, 0]

        # The inside tank walls coordinate ranges for tiles:
        # x = -half and half-1 for walls at left and right,
        # y = -half and half-1 for front and back walls,

        # Left and Right walls (x fixed)
        for z in z_levels:
            for y in range(-half, half):
                positions.append(Coordinate(-half, y, z))
                positions.append(Coordinate(half - 1, y, z))

        # Front and Back walls (y fixed)
        for z in z_levels:
            for x in range(-half, half):
                positions.append(Coordinate(x, -half, z))
                positions.append(Coordinate(x, half - 1, z))

        return positions


class SludgeContactChecker:
    def __init__(self, sludge: Sludge):
        self.sludge = sludge

    def touches_sludge(self, coord: Coordinate) -> bool:
        # Determine if the tile at coord touches sludge after infinite slow rotation
        # Because tank rotates around z-axis with sludge keeping volume and smooth surface,
        # the sludge touches all inner circumference walls fully in z direction from z=-1 to 0
        #
        # The sludge inside is a cylinder with radius = N/2 and height=1 along z axis,
        # after rotation the sludge wets any vertical wall fully where height between -1 and 0.
        # So tiles in the lower half of the tank walls with z in [-1,0) are touched,
        # tiles placed upper half (z in [0,1)) are untouched,
        # so return True if z == -1 else False
        return coord.z == -1


class FDPRequirementCalculator:
    def __init__(self, tiles: List[WallTile], checker: SludgeContactChecker):
        self.tiles = tiles
        self.checker = checker

    def count_fdp_tiles(self) -> int:
        fdp_count = 0
        for tile in self.tiles:
            if self.checker.touches_sludge(tile.position()):
                fdp_count += 1
        return fdp_count


class HedrosHexahedronSolver:
    def __init__(self):
        self.results = []

    def solve_for_n(self, n: int):
        if n == 0:
            return  # No output for termination input 0
        tank = Tank(n)
        sludge = Sludge(tank)
        walls = TankWalls(tank)
        positions = walls.tile_positions()
        tiles = [WallTile(int(pos.x), int(pos.y), int(pos.z)) for pos in positions]
        checker = SludgeContactChecker(sludge)
        calculator = FDPRequirementCalculator(tiles, checker)
        count = calculator.count_fdp_tiles()
        self.results.append(count)

    def solve_all(self, inputs: List[int]) -> List[int]:
        for n in inputs:
            if n == 0:
                break
            self.solve_for_n(n)
        return self.results


def main():
    solver = HedrosHexahedronSolver()
    inputs = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        inputs.append(n)

    results = solver.solve_all(inputs)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()