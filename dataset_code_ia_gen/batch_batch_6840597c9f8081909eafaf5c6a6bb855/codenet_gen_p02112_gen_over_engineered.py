from typing import List, Protocol
from dataclasses import dataclass


class DateConverter(Protocol):
    def to_day_of_year(self, month: int, day: int) -> int:
        ...

    def from_day_of_year(self, day_of_year: int) -> (int, int):
        ...


class SimpleDateConverter:
    """Convert (month, day) to day_of_year and vice versa for fixed 12 months * 30 days calendar."""

    MONTH_DAYS = 30
    MONTHS = 12
    DAYS_IN_YEAR = MONTH_DAYS * MONTHS

    def to_day_of_year(self, month: int, day: int) -> int:
        # 1-based month and day to 1-based day of year
        return (month - 1) * self.MONTH_DAYS + day

    def from_day_of_year(self, day_of_year: int) -> (int, int):
        # Given 1-based day_of_year, returns (month, day)
        month = (day_of_year - 1) // self.MONTH_DAYS + 1
        day = (day_of_year - 1) % self.MONTH_DAYS + 1
        return month, day


@dataclass(frozen=True)
class HolidayPeriod:
    start_day: int
    length: int
    S: int

    def contains(self, day: int, year_days: int) -> bool:
        # handle wrapping around the year
        end_day = (self.start_day + self.length - 1 - 1) % year_days + 1
        # If period does not wrap around:
        if self.start_day <= end_day:
            return self.start_day <= day <= end_day
        # If wraps around:
        else:
            return day >= self.start_day or day <= end_day

    def distance_to_start(self, day: int, year_days: int) -> int:
        """Distance from day to the start of holiday period considering year wrap."""
        diff = (day - self.start_day) % year_days
        return min(diff, year_days - diff)

    def distance_to_end(self, day: int, year_days: int) -> int:
        """Distance from day to the end of holiday period considering year wrap."""
        end_day = (self.start_day + self.length - 1 - 1) % year_days + 1
        diff = (day - end_day) % year_days
        return min(diff, year_days - diff)

    def influence(self, day: int, year_days: int) -> int:
        if self.contains(day, year_days):
            return self.S
        else:
            dist_to_start = self.distance_to_start(day, year_days)
            dist_to_end = self.distance_to_end(day, year_days)
            mindist = min(dist_to_start, dist_to_end)
            val = self.S - mindist
            return val if val > 0 else 0


class CrowdInfluenceCalculator:
    def __init__(self, holidays: List[HolidayPeriod], year_days: int):
        self.holidays = holidays
        self.year_days = year_days

    def congestion_on_day(self, day: int) -> int:
        influences = [holiday.influence(day, self.year_days) for holiday in self.holidays]
        return max(influences) if influences else 0

    def minimal_congestion_in_year(self) -> int:
        return min(self.congestion_on_day(day) for day in range(1, self.year_days + 1))


def main() -> None:
    import sys

    reader = sys.stdin
    N = int(reader.readline())
    date_conv = SimpleDateConverter()
    year_days = date_conv.MONTHS * date_conv.MONTH_DAYS

    holidays: List[HolidayPeriod] = []
    for _ in range(N):
        M, D, V, S = map(int, reader.readline().split())
        start_day = date_conv.to_day_of_year(M, D)
        holidays.append(HolidayPeriod(start_day=start_day, length=V, S=S))

    calculator = CrowdInfluenceCalculator(holidays=holidays, year_days=year_days)
    print(calculator.minimal_congestion_in_year())


if __name__ == "__main__":
    main()