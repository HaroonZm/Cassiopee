import math
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator


class Latitude:
    """
    Represents latitude on Earth.
    Accepts degrees from 90 (North) to -90 (South, represented as negative).
    """
    def __init__(self, degrees: float):
        if not -90.0 <= degrees <= 90.0:
            raise ValueError(f"Latitude must be within [-90, 90], got {degrees}")
        self.degrees = degrees

    def to_radians(self) -> float:
        return math.radians(self.degrees)


class Longitude:
    """
    Represents longitude on Earth.
    Accepts degrees from 0 to 360 (0 ~ 180 East, 180 ~ 360 West represented by 180~360).
    """
    def __init__(self, degrees: float):
        if not 0.0 <= degrees <= 360.0:
            raise ValueError(f"Longitude must be within [0,360], got {degrees}")
        self.degrees = degrees

    def to_radians(self) -> float:
        return math.radians(self.degrees)


class Coordinate:
    """
    Encapsulates a geographic coordinate as latitude and longitude objects.
    """
    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude


class GreatCircleDistanceCalculator(ABC):
    """
    Abstract base class for distance calculation between two coordinates on a sphere.
    """
    @abstractmethod
    def calculate(self, point1: Coordinate, point2: Coordinate) -> float:
        pass


class EarthGreatCircleDistanceCalculator(GreatCircleDistanceCalculator):
    """
    Earth-specific implementation using spherical law of cosines.
    Assumes Earth radius = 6378.1 km according to the problem statement.
    """
    EARTH_RADIUS_KM = 6378.1

    def calculate(self, point1: Coordinate, point2: Coordinate) -> float:
        lat1 = point1.latitude.to_radians()
        lon1 = point1.longitude.to_radians()
        lat2 = point2.latitude.to_radians()
        lon2 = point2.longitude.to_radians()

        # spherical law of cosines formula for central angle
        central_angle = math.acos(
            math.sin(lat1) * math.sin(lat2) +
            math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2))
        )
        return self.EARTH_RADIUS_KM * central_angle


class InputReader:
    """
    Reads input datasets until the termination signal (-1 -1 -1 -1).
    Yields tuples of (a, b, c, d) as floats.
    """
    def __init__(self, source: Iterator[str]):
        self.source = source

    def __iter__(self) -> Iterator[Tuple[float, float, float, float]]:
        for line in self.source:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 4:
                continue
            a, b, c, d = map(float, parts)
            if a == b == c == d == -1.0:
                break
            yield a, b, c, d


class OutputWriter:
    """
    Writes results to the output.
    """
    def __init__(self):
        self._lines: List[str] = []

    def write(self, value: int):
        self._lines.append(str(value))

    def flush(self) -> None:
        print("\n".join(self._lines))


class DistanceApplication:
    """
    Main application orchestrating reading input, calculating distances, and outputting results.
    """
    def __init__(self, calculator: GreatCircleDistanceCalculator, reader: InputReader, writer: OutputWriter):
        self.calculator = calculator
        self.reader = reader
        self.writer = writer

    def run(self) -> None:
        for a, b, c, d in self.reader:
            coord1 = Coordinate(Latitude(a), Longitude(b))
            coord2 = Coordinate(Latitude(c), Longitude(d))
            distance_km = self.calculator.calculate(coord1, coord2)
            rounded_distance = round(distance_km)
            self.writer.write(rounded_distance)
        self.writer.flush()


def main():
    import sys
    # Initialize components with possible future extensibility in mind
    reader = InputReader(source=sys.stdin)
    calculator = EarthGreatCircleDistanceCalculator()
    writer = OutputWriter()
    app = DistanceApplication(calculator=calculator, reader=reader, writer=writer)
    app.run()


if __name__ == "__main__":
    main()