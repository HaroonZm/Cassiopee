from math import gcd
from functools import reduce
from abc import ABC, abstractmethod
from typing import Tuple, Iterator, Optional


class MovementRule(ABC):
    @abstractmethod
    def step(self, position: int) -> int:
        pass

    @abstractmethod
    def cycle_length(self) -> int:
        pass


class CoordinateMovement(MovementRule):
    def __init__(self, a: int, m: int):
        if a <= 1 or m <= 1 or a >= 2**15 or m >= 2**15:
            raise ValueError("a and m must be positive integers with 1 < a,m < 2^15")
        if gcd(a, m) != 1:
            raise ValueError("a and m must be coprime")
        self.a = a
        self.m = m

    def step(self, position: int) -> int:
        # position is from 1 to m, step applies the transformation mod m but result 1-based
        return ((self.a * (position - 1)) % self.m) + 1

    def cycle_length(self) -> int:
        # we want the smallest positive integer k such that a^k ≡ 1 mod m
        # Since gcd(a,m)=1, a is invertible mod m
        current = 1
        k = 1
        while True:
            current = (current * self.a) % self.m
            if current == 1:
                return k
            k += 1


class ElectronicFly:
    def __init__(self, movement_x: CoordinateMovement,
                 movement_y: CoordinateMovement,
                 movement_z: CoordinateMovement):
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.movement_z = movement_z

    def returning_cycle(self) -> int:
        # The fly returns to (1,1,1) when all three coords return simultaneously to 1
        # So we find the cycle lengths of each coordinate and compute their lcm
        cx = self.movement_x.cycle_length()
        cy = self.movement_y.cycle_length()
        cz = self.movement_z.cycle_length()
        return lcm3(cx, cy, cz)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def lcm3(a: int, b: int, c: int) -> int:
    return lcm(a, lcm(b, c))


class DataParser:
    def __init__(self, lines: Iterator[str]):
        self.lines = lines

    def datasets(self) -> Iterator[Tuple[int,int,int,int,int,int]]:
        for line in self.lines:
            parts = line.strip().split()
            if len(parts) != 6:
                continue
            a1, m1, a2, m2, a3, m3 = map(int, parts)
            if (a1, m1, a2, m2, a3, m3) == (0,0,0,0,0,0):
                break
            yield a1, m1, a2, m2, a3, m3


class SolutionController:
    def __init__(self, input_lines: Iterator[str]):
        self.parser = DataParser(input_lines)

    def run(self) -> Iterator[int]:
        for a1, m1, a2, m2, a3, m3 in self.parser.datasets():
            # Instantiate coordinate movements with validation of coprimality
            try:
                mv_x = CoordinateMovement(a1, m1)
                mv_y = CoordinateMovement(a2, m2)
                mv_z = CoordinateMovement(a3, m3)
            except ValueError:
                # The problem guarantees conditions, but safety fallback:
                yield -1
                continue

            efly = ElectronicFly(mv_x, mv_y, mv_z)
            yield efly.returning_cycle()


def main():
    import sys
    controller = SolutionController(iter(sys.stdin))
    for result in controller.run():
        print(result)


if __name__ == "__main__":
    main()