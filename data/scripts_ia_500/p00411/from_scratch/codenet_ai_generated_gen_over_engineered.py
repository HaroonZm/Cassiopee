from abc import ABC, abstractmethod
from typing import Tuple


class AngleTimeConverterInterface(ABC):
    @abstractmethod
    def convert_angle_to_time(self, angle: float) -> float:
        pass


class StopwatchAngleTimeConverter(AngleTimeConverterInterface):
    def __init__(self, reference_angle: float, reference_time: float):
        if not (0 < reference_angle < 360):
            raise ValueError("reference_angle must be in (0, 360) degrees.")
        if reference_time <= 0:
            raise ValueError("reference_time must be positive.")
        self._reference_angle = reference_angle
        self._reference_time = reference_time
        self._angular_velocity = self._compute_angular_velocity()

    def _compute_angular_velocity(self) -> float:
        # Angular velocity in degrees per second
        return self._reference_angle / self._reference_time

    def convert_angle_to_time(self, angle: float) -> float:
        if not (0 <= angle < 360):
            raise ValueError("angle must be in [0, 360) degrees.")
        return angle / self._angular_velocity


class StopwatchInputParser:
    @staticmethod
    def parse_input(input_line: str) -> Tuple[int, int, int]:
        parts = input_line.strip().split()
        if len(parts) != 3:
            raise ValueError("Input must contain exactly three integers.")
        a, t, r = map(int, parts)
        if not (1 <= a <= 359):
            raise ValueError("a must be between 1 and 359 degrees inclusive.")
        if not (1 <= t <= 1000):
            raise ValueError("t must be between 1 and 1000 seconds inclusive.")
        if not (0 <= r <= 359):
            raise ValueError("r must be between 0 and 359 degrees inclusive.")
        return a, t, r


class StopwatchApplication:
    def __init__(self, converter_cls=StopwatchAngleTimeConverter, parser_cls=StopwatchInputParser):
        self._converter_cls = converter_cls
        self._parser_cls = parser_cls

    def run(self):
        raw_input = input()
        a, t, r = self._parser_cls.parse_input(raw_input)
        converter = self._converter_cls(a, t)
        elapsed_time = converter.convert_angle_to_time(r)
        print(f"{elapsed_time:.6f}")


if __name__ == "__main__":
    app = StopwatchApplication()
    app.run()