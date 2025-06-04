from abc import ABC, abstractmethod
from typing import Tuple, List

class LeapYearChecker(ABC):
    @abstractmethod
    def is_leap_year(self, year: int) -> bool:
        pass

class GregorianLeapYearChecker(LeapYearChecker):
    def is_leap_year(self, year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

class DayOfWeekCalculator(ABC):
    @abstractmethod
    def day_of_week(self, date: Date) -> str:
        pass

class FixedYearDayOfWeekCalculator(DayOfWeekCalculator):
    def __init__(self, year: int, start_day_of_week: str, leap_year_checker: LeapYearChecker):
        self.year = year
        self.start_day_of_week = start_day_of_week
        self.leap_year_checker = leap_year_checker
        self.days_in_month = self._initialize_days_in_month()
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.start_index = self.weekdays.index(start_day_of_week)

    def _initialize_days_in_month(self) -> List[int]:
        # Initialize for a non-leap year, then adjust if leap year
        dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30, 31]
        if self.leap_year_checker.is_leap_year(self.year):
            dim[1] = 29
        return dim

    def _days_elapsed_since_start_of_year(self, month: int, day: int) -> int:
        # Calculate days elapsed from Jan 1 to given month/day, zero-based
        days = sum(self.days_in_month[:month - 1]) + (day - 1)
        return days

    def day_of_week(self, date: Date) -> str:
        days_elapsed = self._days_elapsed_since_start_of_year(date.month, date.day)
        day_index = (self.start_index + days_elapsed) % 7
        return self.weekdays[day_index]

class InputParser:
    def parse(self) -> List[Tuple[int,int]]:
        result = []
        while True:
            line = input().strip()
            if line == '0 0':
                break
            m,s = line.split()
            m_int,s_int = int(m), int(s)
            result.append((m_int, s_int))
        return result

class DayFinderApplication:
    def __init__(self):
        self.year = 2004
        self.start_day = "Thursday"
        self.leap_year_checker = GregorianLeapYearChecker()
        self.calculator = FixedYearDayOfWeekCalculator(self.year, self.start_day, self.leap_year_checker)
        self.parser = InputParser()

    def run(self):
        dates = self.parser.parse()
        for m, d in dates:
            date = Date(self.year, m, d)
            print(self.calculator.day_of_week(date))

if __name__ == "__main__":
    app = DayFinderApplication()
    app.run()