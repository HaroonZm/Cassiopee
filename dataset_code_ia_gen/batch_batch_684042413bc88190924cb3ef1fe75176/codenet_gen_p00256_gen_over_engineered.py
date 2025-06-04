from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple


class DateConversionError(Exception):
    pass


@dataclass(frozen=True)
class MayaLongCount:
    baktun: int    # b (0 ≤ b < 13)
    katun: int     # ka (0 ≤ ka < 20)
    tun: int       # t (0 ≤ t < 20)
    uinal: int     # w (0 ≤ w < 18)
    kin: int       # ki (0 ≤ ki < 20)

    # Unit sizes in kin (days)
    KIN = 1
    UINAL = 20 * KIN
    TUN = 18 * UINAL    # 360
    KATUN = 20 * TUN    # 7200
    BAKTUN = 20 * KATUN # 144000

    MAX_BAKTUN = 12
    MAX_KATUN = 19
    MAX_TUN = 19
    MAX_UINAL = 17
    MAX_KIN = 19

    def __post_init__(self):
        object.__setattr__(self, 'baktun', self.baktun)
        object.__setattr__(self, 'katun', self.katun)
        object.__setattr__(self, 'tun', self.tun)
        object.__setattr__(self, 'uinal', self.uinal)
        object.__setattr__(self, 'kin', self.kin)
        # Validate ranges
        if not (0 <= self.baktun < 13):
            raise DateConversionError(f"Invalid baktun {self.baktun}")
        if not (0 <= self.katun < 20):
            raise DateConversionError(f"Invalid katun {self.katun}")
        if not (0 <= self.tun < 20):
            raise DateConversionError(f"Invalid tun {self.tun}")
        if not (0 <= self.uinal < 18):
            raise DateConversionError(f"Invalid uinal {self.uinal}")
        if not (0 <= self.kin < 20):
            raise DateConversionError(f"Invalid kin {self.kin}")

    def total_days(self) -> int:
        # Calculate total days offset from 0.0.0.0.0
        return (self.baktun * self.BAKTUN +
                self.katun * self.KATUN +
                self.tun * self.TUN +
                self.uinal * self.UINAL +
                self.kin * self.KIN)

    @classmethod
    def from_total_days(cls, days: int) -> 'MayaLongCount':
        # Allow days to be >= 0; if larger than one cycle, allow overflow into next cycle
        # Compute each unit by integer division and modulo respecting units' base
        baktun = days // cls.BAKTUN
        days %= cls.BAKTUN
        katun = days // cls.KATUN
        days %= cls.KATUN
        tun = days // cls.TUN
        days %= cls.TUN
        uinal = days // cls.UINAL
        kin = days % cls.UINAL
        # kin modulo is 20, so adjust conversion carefully
        # The above incorrectly treated units; fix below:

        # Correct approach:
        # baktun, remainder
        baktun, rem = divmod(days, cls.BAKTUN)
        # Katun
        katun, rem = divmod(rem, cls.KATUN)
        # Tun
        tun, rem = divmod(rem, cls.TUN)
        # Uinal
        uinal, kin = divmod(rem, cls.UINAL)
        # kin direct

        # Actually above is wrong scheme, we need to start from total days overall and do the division as per units

        baktun, rem = divmod(days, cls.BAKTUN)
        katun, rem = divmod(rem, cls.KATUN)
        tun, rem = divmod(rem, cls.TUN)
        uinal, kin = divmod(rem, cls.UINAL)

        # Wait all above mistake is because days here is remainder days after division by baktun, which is 20*20*18*20=144000 days
        # But days is already days % BAKTUN, it cannot be larger than BAKTUN=144000
        # Let's re-implement carefully

        # Do the breakdown starting from days total

        baktun, remainder = divmod(days, cls.BAKTUN)
        # since BAKTUN=144000 days, we need to assign baktun and remainder correctly
        katun, remainder = divmod(remainder, cls.KATUN)
        tun, remainder = divmod(remainder, cls.TUN)
        uinal, kin = divmod(remainder, cls.UINAL)

        # Wait, in fact:
        # BAKTUN = 144000
        # KATUN = 7200
        # TUN = 360
        # UINAL = 20
        # KIN = 1
        # So let's do exact units:

        baktun, remainder = divmod(days, cls.BAKTUN)       # baktun: days // 144000
        katun, remainder = divmod(remainder, cls.KATUN)    # katun: remainder // 7200
        tun, remainder = divmod(remainder, cls.TUN)        # tun: remainder // 360
        uinal, kin = divmod(remainder, cls.UINAL)          # uinal: remainder // 20, kin: remainder % 20

        return cls(baktun, katun, tun, uinal, kin)

    def __str__(self):
        return f"{self.baktun}.{self.katun}.{self.tun}.{self.uinal}.{self.kin}"


@dataclass(frozen=True)
class GregorianDate:
    year: int      # y (2012 ≤ y ≤ 10,000,000)
    month: int     # m (1 ≤ m ≤ 12)
    day: int       # d (1 ≤ d ≤ 31)

    # Month days normal year (index 0 unused)
    DAYS_IN_MONTH_NORMAL = [0, 31, 28, 31, 30, 31, 30,
                            31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year: int) -> bool:
        # Leap year rules:
        # 4の倍数の年のうち、100で割り切れない年か、400で割り切れる年である
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def days_in_month(cls, year: int, month: int) -> int:
        if month != 2:
            return cls.DAYS_IN_MONTH_NORMAL[month]
        else:
            return 29 if cls.is_leap_year(year) else 28

    def is_valid(self) -> bool:
        if not (2012 <= self.year <= 10_000_000):
            return False
        if not (1 <= self.month <= 12):
            return False
        max_day = self.days_in_month(self.year, self.month)
        if not (1 <= self.day <= max_day):
            return False
        return True

    def to_ordinal(self) -> int:
        # Calculate days since 2012-12-21 counted as day 0
        # Algorithm:
        # sum days of full years 2012..(year-1)
        # plus days from beginning of this year to (month, day)
        # minus days from beginning of 2012 to 12/21 (offset zero baseline)
        # We'll use a precise day count method for large years:
        # Use a proleptic Gregorian calendar

        # Count days from 0001-01-01 to given date, then subtract days to baseline 2012-12-21
        def count_leap(year):
            # count leap days up to year (inclusive of year?)
            # For days elapsed before Jan 1 of given year:
            # count_leap_days = year//4 - year//100 + year//400 for years before
            return year // 4 - year // 100 + year // 400

        def days_until_year_start(y):
            # Days from 0001-01-01 to y-01-01
            return 365 * (y - 1) + count_leap(y - 1)

        def days_until_date(y, m, d):
            days = days_until_year_start(y)
            for mm in range(1, m):
                days += self.days_in_month(y, mm)
            days += d - 1
            return days

        base_days = days_until_date(2012, 12, 21)
        current_days = days_until_date(self.year, self.month, self.day)
        return current_days - base_days


    @classmethod
    def from_ordinal(cls, ordinal: int) -> 'GregorianDate':
        # Compute Gregorian date from days offset since 2012-12-21 (day 0)
        # ordinal may be 0 or positive

        # We find the year by approximate estimate then refine
        # days_until_date(2012,12,21) = base_days, so return year=2012 by default

        # Using inverse of days_until_date:
        # we want y such that days_until_year_start(y) <= ordinal + base_days < days_until_year_start(y+1)
        # base_days = days_until_date(2012,12,21)

        base_days = GregorianDate(2012, 12, 21,).to_ordinal() + base_days_fix()

        # Actually base_days_fix is base_days itself from to_ordinal above,

        # Using days_until_year_start(y) = 365*(y-1)+leaps

        # For simplicity we apply a binary search on year

        def days_until_year_start(y):
            leaps = y // 4 - y // 100 + y // 400
            return 365 * (y - 1) + leaps

        target_days = ordinal + days_until_date(2012,12,21)

        # lower bound and upper bound for year
        low = 2012
        high = 10000001  # inclusive max is 10,000,000 so buffer

        while low < high:
            mid = (low + high) // 2
            mid_day = days_until_year_start(mid)
            if mid_day <= target_days:
                low = mid + 1
            else:
                high = mid

        year = low - 1

        # calculate day of year
        day_of_year = target_days - days_until_year_start(year) + 1

        # find month and day in month
        months = []
        for m in range(1, 13):
            months.append(cls.days_in_month(year, m))

        month = 1
        while month <= 12 and day_of_year > months[month - 1]:
            day_of_year -= months[month - 1]
            month += 1
        day = day_of_year

        return cls(year, month, day)


# Helpers for base_days fix caching to avoid redundant computations
_base_days_cache = None

def days_until_date(y, m, d):
    def count_leap(year):
        return year // 4 - year // 100 + year // 400

    def days_until_year_start(yy):
        return 365 * (yy - 1) + count_leap(yy - 1)

    days = days_until_year_start(y)
    for mm in range(1, m):
        days += GregorianDate.days_in_month(y, mm)
    days += d - 1
    return days

def base_days_fix():
    global _base_days_cache
    if _base_days_cache is None:
        _base_days_cache = days_until_date(2012, 12, 21)
    return _base_days_cache


class DateConverter(ABC):
    @abstractmethod
    def convert(self, value: str) -> str:
        pass


class MayaToGregorianConverter(DateConverter):
    def convert(self, value: str) -> str:
        # input: b.ka.t.w.ki
        parts = value.split('.')
        if len(parts) != 5:
            raise DateConversionError("Invalid MayaLongCount input")
        b, ka, t, w, ki = map(int, parts)
        maya_date = MayaLongCount(b, ka, t, w, ki)
        days_offset = maya_date.total_days()
        # baseline: Maya 0.0.0.0.0 maps to 2012-12-21 days offset 0
        # So days_offset may exceed max cycle; allowed
        # Gregorian date = baseline + days_offset
        ordinal_days = days_offset
        gregorian_date = GregorianDate.from_ordinal(ordinal_days)
        if not gregorian_date.is_valid():
            raise DateConversionError("Converted Gregorian date invalid")
        return f"{gregorian_date.year}.{gregorian_date.month}.{gregorian_date.day}"


class GregorianToMayaConverter(DateConverter):
    def convert(self, value: str) -> str:
        # input: y.m.d
        parts = value.split('.')
        if len(parts) != 3:
            raise DateConversionError("Invalid Gregorian input")
        y, m, d = map(int, parts)
        g_date = GregorianDate(y, m, d)
        if not g_date.is_valid():
            raise DateConversionError("Invalid Gregorian date")
        days_diff = g_date.to_ordinal()
        # days_diff may exceed Maya cycle length; output as is
        maya_date = MayaLongCount.from_total_days(days_diff)
        return str(maya_date)


def identify_input_type(input_str: str) -> str:
    # Heuristic: if has 5 parts => Maya, if 3 => Gregorian, else error
    parts = input_str.split('.')
    if len(parts) == 5:
        return 'maya'
    elif len(parts) == 3:
        return 'gregorian'
    else:
        return 'unknown'


class DateConversionSystem:
    def __init__(self):
        self._converters = {
            'maya': MayaToGregorianConverter(),
            'gregorian': GregorianToMayaConverter(),
        }

    def convert_line(self, line: str) -> str:
        line = line.strip()
        if line == '#':
            return None
        input_type = identify_input_type(line)
        if input_type == 'unknown':
            raise DateConversionError("Unknown input format")
        converter = self._converters[input_type]
        return converter.convert(line)


def main():
    import sys
    converter_system = DateConversionSystem()

    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        try:
            result = converter_system.convert_line(line)
            if result is not None:
                print(result)
        except DateConversionError:
            # Per problem statement no specified error output, silently ignore or continue
            pass


if __name__ == "__main__":
    main()