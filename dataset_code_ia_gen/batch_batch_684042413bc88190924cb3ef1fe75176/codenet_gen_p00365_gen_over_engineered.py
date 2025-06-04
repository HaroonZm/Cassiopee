class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        self._validate_date()

    def _is_leap_year(self, year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

    def is_leap_year(self) -> bool:
        return self._is_leap_year(self.year)

    def _days_in_month(self, year: int, month: int) -> int:
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        if month in {4, 6, 9, 11}:
            return 30
        # February handling
        if self._is_leap_year(year):
            return 29
        return 28

    def _validate_date(self):
        if not (1 <= self.month <= 12):
            raise ValueError(f"Invalid month: {self.month}")
        max_day = self._days_in_month(self.year, self.month)
        if not (1 <= self.day <= max_day):
            raise ValueError(f"Invalid day {self.day} for {self.year}-{self.month}")

    def __lt__(self, other: "Date") -> bool:
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __eq__(self, other: "Date") -> bool:
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def copy(self) -> "Date":
        return Date(self.year, self.month, self.day)

    def add_days(self, days: int) -> "Date":
        # slow but correct way for extensibility, just increment day by day
        result = self.copy()
        while days > 0:
            max_day = self._days_in_month(result.year, result.month)
            if result.day + days <= max_day:
                result.day += days
                days = 0
            else:
                days -= (max_day - result.day + 1)
                result.day = 1
                if result.month == 12:
                    result.month = 1
                    result.year += 1
                else:
                    result.month += 1
        return result

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

class Birthday:
    def __init__(self, date: Date):
        self.original_date = date
        self.adjusted_date_cache = {}

    def _adjusted_birthday_for_year(self, year: int) -> Date:
        # Birthday on Feb 29: age increments on March 1st if no Feb 29 in that year
        if self.original_date.month == 2 and self.original_date.day == 29:
            if Date(year, 1, 1)._is_leap_year(year):
                return Date(year, 2, 29)
            else:
                return Date(year, 3, 1)
        else:
            return Date(year, self.original_date.month, self.original_date.day)

    def age_on(self, on_date: Date) -> int:
        # Calculate the age at the very start of "on_date" (age increments at birthday start)
        # If on_date is before the birthday in that year, age is year difference - 1, else year difference.
        birth_year = self.original_date.year
        adjusted_bday = self._adjusted_birthday_for_year(on_date.year)
        if on_date < adjusted_bday:
            return on_date.year - birth_year - 1
        else:
            return on_date.year - birth_year

class AgeDifferenceCalculator:
    def __init__(self, birthday1: Birthday, birthday2: Birthday):
        self.birthday1 = birthday1
        self.birthday2 = birthday2

    def _candidate_critical_dates(self):
        # For sophistication:
        # Candidate dates on which age difference can jump are:
        # birthdays of each in each subsequent year from min birth year to max possible relevant year
        # Since age increments at start of birthday, change in difference can happen at these days.
        # Also consider years up to the max birthday year + difference in start years + 10 for margin.
        start_year = min(self.birthday1.original_date.year, self.birthday2.original_date.year)
        end_year = max(self.birthday1.original_date.year, self.birthday2.original_date.year) + 101  # +100 yrs margin
        critical_dates = []
        for year in range(start_year, end_year+1):
            for bday in (self.birthday1, self.birthday2):
                bd = bday._adjusted_birthday_for_year(year)
                critical_dates.append(bd)
        return critical_dates

    def max_age_difference(self) -> int:
        dates = self._candidate_critical_dates()
        # To avoid redundant calculation, we'll order dates and deduplicate
        unique_dates = sorted({(d.year, d.month, d.day): d for d in dates}.values())
        max_diff = 0
        # For optimistic sophistication, use a generator and caching
        for d in unique_dates:
            age1 = self.birthday1.age_on(d)
            age2 = self.birthday2.age_on(d)
            diff = abs(age1 - age2)
            if diff > max_diff:
                max_diff = diff
        return max_diff

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    y1, m1, d1, y2, m2, d2 = map(int, input_data)
    bd1 = Birthday(Date(y1, m1, d1))
    bd2 = Birthday(Date(y2, m2, d2))
    adc = AgeDifferenceCalculator(bd1, bd2)
    print(adc.max_age_difference())

if __name__ == "__main__":
    main()