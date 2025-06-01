from abc import ABC, abstractmethod
import sys
from typing import List, Tuple


class AlgebraicEntity(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass


class Quaternion(AlgebraicEntity):
    __slots__ = ('x', 'y', 'z', 'w')

    def __init__(self, x: int, y: int, z: int, w: int):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other: 'Quaternion') -> 'Quaternion':
        return Quaternion(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )

    def __mul__(self, other: 'Quaternion') -> 'Quaternion':
        # Quaternion multiplication rules based on i,j,k multiplication table
        x1, y1, z1, w1 = self.x, self.y, self.z, self.w
        x2, y2, z2, w2 = other.x, other.y, other.z, other.w

        # Apply Hamilton product:
        # (x1 + y1i + z1j + w1k)(x2 + y2i + z2j + w2k) =
        # (x1x2 - y1y2 - z1z2 - w1w2) +
        # (x1y2 + y1x2 + z1w2 - w1z2)i +
        # (x1z2 - y1w2 + z1x2 + w1y2)j +
        # (x1w2 + y1z2 - z1y2 + w1x2)k
        x = x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2
        y = x1 * y2 + y1 * x2 + z1 * w2 - w1 * z2
        z = x1 * z2 - y1 * w2 + z1 * x2 + w1 * y2
        w = x1 * w2 + y1 * z2 - z1 * y2 + w1 * x2

        return Quaternion(x, y, z, w)

    def __repr__(self):
        return f"{self.x} {self.y} {self.z} {self.w}"


class InputProcessor:
    def __init__(self):
        self.data_sets: List[List[Tuple[Quaternion, Quaternion]]] = []

    def read(self):
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while True:
            if idx >= len(lines):
                break
            n_line = lines[idx].strip()
            idx += 1
            if n_line == '0':
                break
            n = int(n_line)
            pairs = []
            for _ in range(n):
                if idx >= len(lines):
                    break
                parts = list(map(int, lines[idx].strip().split()))
                idx += 1
                q1 = Quaternion(parts[0], parts[1], parts[2], parts[3])
                q2 = Quaternion(parts[4], parts[5], parts[6], parts[7])
                pairs.append((q1, q2))
            self.data_sets.append(pairs)


class OutputProcessor:
    @staticmethod
    def output(results: List[List[Quaternion]]):
        for result_set in results:
            for q in result_set:
                print(q)


class QuaternionCalculationEngine:
    def __init__(self, data_sets: List[List[Tuple[Quaternion, Quaternion]]]):
        self.data_sets = data_sets

    def compute_all(self) -> List[List[Quaternion]]:
        results = []
        for pair_list in self.data_sets:
            result_list = []
            for q1, q2 in pair_list:
                prod = q1 * q2
                result_list.append(prod)
            results.append(result_list)
        return results


def main():
    # Extensible management interface:
    input_processor = InputProcessor()
    input_processor.read()

    calculation_engine = QuaternionCalculationEngine(input_processor.data_sets)
    results = calculation_engine.compute_all()

    OutputProcessor.output(results)


if __name__ == "__main__":
    main()