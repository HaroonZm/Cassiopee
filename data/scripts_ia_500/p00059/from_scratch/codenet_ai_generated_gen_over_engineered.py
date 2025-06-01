from abc import ABC, abstractmethod
from typing import Iterator, List, Tuple, Optional
import sys


class Coordinate(ABC):
    @abstractmethod
    def as_float(self) -> float:
        pass


class FloatCoordinate(Coordinate):
    def __init__(self, value: float):
        self._value = value

    def as_float(self) -> float:
        return self._value


class RectangleInterface(ABC):
    @abstractmethod
    def overlaps(self, other: 'RectangleInterface') -> bool:
        pass


class Rectangle(RectangleInterface):
    def __init__(self, bottom_left: Tuple[Coordinate, Coordinate], top_right: Tuple[Coordinate, Coordinate]):
        self._bl_x = bottom_left[0].as_float()
        self._bl_y = bottom_left[1].as_float()
        self._tr_x = top_right[0].as_float()
        self._tr_y = top_right[1].as_float()
        self._validate()

    def _validate(self) -> None:
        if self._bl_x > self._tr_x or self._bl_y > self._tr_y:
            raise ValueError("Invalid rectangle coordinates: bottom-left must be less than top-right")

    def overlaps(self, other: 'RectangleInterface') -> bool:
        if not isinstance(other, Rectangle):
            raise TypeError("Can only compare overlap with another Rectangle instance")
        horizontal_overlap = not (self._tr_x < other._bl_x or other._tr_x < self._bl_x)
        vertical_overlap = not (self._tr_y < other._bl_y or other._tr_y < self._bl_y)
        # 接しているものも重なっているとみなすため、端が等しい場合もTrue
        return horizontal_overlap and vertical_overlap


class InputParser(ABC):
    @abstractmethod
    def parse(self, line: str) -> List[FloatCoordinate]:
        pass


class FloatInputParser(InputParser):
    def parse(self, line: str) -> List[FloatCoordinate]:
        parts = line.strip().split()
        return [FloatCoordinate(float(p)) for p in parts]


class DataSetProcessor:
    def __init__(self):
        self._parser = FloatInputParser()

    def _construct_rectangle(self, coords: List[FloatCoordinate], start_index: int) -> Rectangle:
        bottom_left = (coords[start_index], coords[start_index + 1])
        top_right = (coords[start_index + 2], coords[start_index + 3])
        return Rectangle(bottom_left, top_right)

    def process(self, data_sets: Iterator[str]) -> Iterator[str]:
        for line in data_sets:
            coords = self._parser.parse(line)
            # 8 values expected per line
            if len(coords) != 8:
                # skip or break if invalid
                continue
            rect_a = self._construct_rectangle(coords, 0)
            rect_b = self._construct_rectangle(coords, 4)
            yield "YES" if rect_a.overlaps(rect_b) else "NO"


class OutputPresenter:
    def output(self, results: Iterator[str]) -> None:
        for result in results:
            print(result)


def main() -> None:
    processor = DataSetProcessor()
    results = processor.process(sys.stdin)
    presenter = OutputPresenter()
    presenter.output(results)


if __name__ == "__main__":
    main()