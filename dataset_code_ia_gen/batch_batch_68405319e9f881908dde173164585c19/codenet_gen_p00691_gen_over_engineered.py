from abc import ABC, abstractmethod
from typing import Iterator, Tuple, Optional


class InputReader(ABC):
    @abstractmethod
    def read_next(self) -> Optional[int]:
        pass


class StdInputReader(InputReader):
    def read_next(self) -> Optional[int]:
        while True:
            line = input()
            line = line.strip()
            if not line.isdigit():
                continue
            n = int(line)
            if n == 0:
                return None
            return n


class FermatLastTheoremVerifier(ABC):
    @abstractmethod
    def verify(self, z: int) -> int:
        pass


class CubicSumMaximizer(FermatLastTheoremVerifier):
    def __init__(self, power: int):
        self.power = power
        self._cache = {}

    def verify(self, z: int) -> int:
        # Check cache
        if z in self._cache:
            return self._cache[z]

        z_pow = z ** self.power

        # Since n=3, brute force with clever limiting:
        max_sum = 0
        limit = z  # All x,y in (1..z)
        # To speed up, we take advantage that x^3 + y^3 <= z^3 and sort search order

        # Precompute cubes
        cubes = [i ** self.power for i in range(limit + 1)]

        # Use two pointers approach to find max of x^3 + y^3 <= z^3
        # Iterate over x ascending and y descending to approach limit efficiently
        x = 1
        y = limit
        while x <= limit and y >= 1:
            s = cubes[x] + cubes[y]
            if s <= z_pow:
                if s > max_sum:
                    max_sum = s
                x += 1
            else:
                y -= 1

        diff = z_pow - max_sum
        self._cache[z] = diff
        return diff


class OutputWriter(ABC):
    @abstractmethod
    def write(self, result: int) -> None:
        pass


class StdOutputWriter(OutputWriter):
    def write(self, result: int) -> None:
        print(result)


class FermatLastTheoremApp:
    def __init__(
        self,
        input_reader: InputReader,
        verifier: FermatLastTheoremVerifier,
        output_writer: OutputWriter,
    ):
        self.input_reader = input_reader
        self.verifier = verifier
        self.output_writer = output_writer

    def run(self):
        while True:
            z = self.input_reader.read_next()
            if z is None:
                break
            res = self.verifier.verify(z)
            self.output_writer.write(res)


if __name__ == "__main__":
    reader = StdInputReader()
    verifier = CubicSumMaximizer(power=3)
    writer = StdOutputWriter()
    app = FermatLastTheoremApp(reader, verifier, writer)
    app.run()