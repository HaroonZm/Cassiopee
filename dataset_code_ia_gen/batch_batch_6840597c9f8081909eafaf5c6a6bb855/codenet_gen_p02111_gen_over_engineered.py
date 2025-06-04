from abc import ABC, abstractmethod
from dataclasses import dataclass

class Angle(ABC):
    @abstractmethod
    def degrees(self) -> float:
        pass

@dataclass(frozen=True)
class DegreeAngle(Angle):
    value: int

    def __post_init__(self):
        if not (0 <= self.value <= 359):
            raise ValueError("Angle must be between 0 and 359 degrees inclusive")

    def degrees(self) -> float:
        return float(self.value)

class Time(ABC):
    @abstractmethod
    def hour(self) -> int:
        pass

    @abstractmethod
    def minute(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

@dataclass(frozen=True)
class ClockTime(Time):
    h: int  # 0 ≤ h ≤ 11
    m: int  # 0 ≤ m ≤ 59

    def __post_init__(self):
        if not (0 <= self.h <= 11):
            raise ValueError("Hour must be between 0 and 11 inclusive")
        if not (0 <= self.m <= 59):
            raise ValueError("Minute must be between 0 and 59 inclusive")

    def hour(self) -> int:
        return self.h

    def minute(self) -> int:
        return self.m

    def __str__(self) -> str:
        return f"{self.h} {self.m}"

class AngleToTimeConverter(ABC):
    @abstractmethod
    def convert(self, angle: Angle) -> Time:
        pass

class AnalogClockAngleToTimeConverter(AngleToTimeConverter):
    """
    Converts the angle of the hour hand on an analog clock into a time (hour, minute).
    The problem states that the angle is measured clockwise from 12 o'clock which is 0 degrees.
    Each hour represents 30 degrees (360°/12).
    The hour hand moves continuously: each degree corresponds to 2 minutes (because 30° = 60 min).
    """

    def convert(self, angle: Angle) -> Time:
        deg = angle.degrees()
        # total minutes indicated = (deg * 2) because 30deg = 60min => 1deg = 2min
        total_minutes = deg * 2
        # hour between 0 and 11
        h = int(total_minutes // 60) % 12
        m = int(total_minutes % 60)
        return ClockTime(h, m)

class InputReader:
    def read_angle(self) -> Angle:
        val = int(input().strip())
        return DegreeAngle(val)

class OutputWriter:
    def write_time(self, time: Time) -> None:
        print(time)

class ClockApplication:
    """
    Encapsulates the entire process of reading input,
    converting angle to time, and printing the result.
    This abstraction supports easy future expansion with new input/output methods,
    or support for multiple clock types.
    """
    def __init__(self,
                 reader: InputReader,
                 converter: AngleToTimeConverter,
                 writer: OutputWriter):
        self.reader = reader
        self.converter = converter
        self.writer = writer

    def run(self) -> None:
        angle = self.reader.read_angle()
        time = self.converter.convert(angle)
        self.writer.write_time(time)

if __name__ == "__main__":
    app = ClockApplication(
        reader=InputReader(),
        converter=AnalogClockAngleToTimeConverter(),
        writer=OutputWriter()
    )
    app.run()