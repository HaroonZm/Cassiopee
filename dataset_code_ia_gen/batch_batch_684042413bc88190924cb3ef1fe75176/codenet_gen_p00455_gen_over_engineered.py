from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple, List

@dataclass(frozen=True)
class Time:
    hour: int
    minute: int
    second: int

    def to_seconds(self) -> int:
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def from_seconds(seconds: int) -> 'Time':
        h = seconds // 3600
        seconds %= 3600
        m = seconds // 60
        s = seconds % 60
        return Time(h, m, s)

    def __sub__(self, other: 'Time') -> 'TimeDifference':
        diff_seconds = self.to_seconds() - other.to_seconds()
        if diff_seconds < 0:
            raise ValueError("End time must be after start time.")
        return TimeDifference.from_seconds(diff_seconds)

class TimeDifference:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def from_seconds(total_seconds: int) -> 'TimeDifference':
        h = total_seconds // 3600
        total_seconds %= 3600
        m = total_seconds // 60
        s = total_seconds % 60
        return TimeDifference(h, m, s)

    def __str__(self):
        return f"{self.hours} {self.minutes} {self.seconds}"

class EmployeeTimeCard(ABC):
    @abstractmethod
    def calculate_work_duration(self) -> TimeDifference:
        pass

class BasicEmployeeTimeCard(EmployeeTimeCard):
    def __init__(self, start: Time, end: Time):
        self.start = start
        self.end = end
        self._validate_times()

    def _validate_times(self):
        # Constraints per problem statement
        if not (7 <= self.start.hour <= 22):
            raise ValueError(f"Start hour {self.start.hour} is out of valid range.")
        if not (0 <= self.start.minute <= 59 and 0 <= self.start.second <= 59):
            raise ValueError("Invalid start minute or second.")
        if not (0 <= self.end.hour <= 22):
            raise ValueError(f"End hour {self.end.hour} is out of valid range.")
        if not (0 <= self.end.minute <= 59 and 0 <= self.end.second <= 59):
            raise ValueError("Invalid end minute or second.")
        start_sec = self.start.to_seconds()
        end_sec = self.end.to_seconds()
        if end_sec <= start_sec:
            raise ValueError("End time must be after start time.")
        if self.end.hour >= 23:
            raise ValueError("End time must be before 23:00:00.")

    def calculate_work_duration(self) -> TimeDifference:
        return self.end - self.start

class TimeCardProcessor:
    def __init__(self, employee_cards: List[EmployeeTimeCard]):
        self.employee_cards = employee_cards

    def process_all(self) -> List[TimeDifference]:
        durations = []
        for card in self.employee_cards:
            durations.append(card.calculate_work_duration())
        return durations

class InputParser:
    @staticmethod
    def parse_time_triplet(triplet: Tuple[int, int, int]) -> Time:
        h, m, s = triplet
        return Time(h, m, s)

    @staticmethod
    def parse_line(line: str) -> Tuple[Time, Time]:
        parts = list(map(int, line.strip().split()))
        if len(parts) != 6:
            raise ValueError("Input line must contain exactly 6 integers.")
        start = InputParser.parse_time_triplet(tuple(parts[0:3]))
        end = InputParser.parse_time_triplet(tuple(parts[3:6]))
        return start, end

def main():
    inputs = [input() for _ in range(3)]
    employee_cards = []
    for line in inputs:
        start, end = InputParser.parse_line(line)
        card = BasicEmployeeTimeCard(start, end)
        employee_cards.append(card)

    processor = TimeCardProcessor(employee_cards)
    durations = processor.process_all()
    for duration in durations:
        print(duration)

if __name__ == "__main__":
    main()