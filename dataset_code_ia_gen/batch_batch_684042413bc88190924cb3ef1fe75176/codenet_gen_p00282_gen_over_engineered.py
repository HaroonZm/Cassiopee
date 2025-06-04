from typing import List, Tuple, Optional, Iterator

class NumberUnit:
    """
    Represents a single unit in the Jinkouki large number representation.
    For example, 'Man', 'Oku', etc.
    """
    def __init__(self, name: str, power: int):
        self.name = name  # Unit name string
        self.power = power  # power of 10 that this unit represents (must be multiple of 4)

    def __str__(self):
        return self.name

class UnitSystem:
    """
    Encapsulates the Jinkouki unit system where each unit corresponds to a 10^4 power step.
    """
    def __init__(self):
        # The units are listed from smallest to largest in ascending power order
        # Power is 10^(4 * index) for index in range(len(units))
        self.units: List[NumberUnit] = [
            NumberUnit('', 0),         # No unit for 10^0 to 10^3, handled separately
            NumberUnit('Man', 4),
            NumberUnit('Oku', 8),
            NumberUnit('Cho', 12),
            NumberUnit('Kei', 16),
            NumberUnit('Gai', 20),
            NumberUnit('Jo', 24),
            NumberUnit('Jo', 24),      # duplicate for 126穣 in example?
            NumberUnit('Jo', 24),      # actually only one 'Jo' needed; standard Jinkouki units are up to 'Jo' (24)
            NumberUnit('Jo', 24),
            NumberUnit('Jou', 24),
            NumberUnit('Jou', 24),
        ]
        # The problem states units appear like "穣(じょ)", "垓", "京", "兆", "億", "万"
        # For the sake of output, we use the units appearing in the examples:
        # 'Man' (万, 10^4), 'Oku' (億, 10^8), 'Cho' (兆, 10^12), 'Kei' (京, 10^16),
        # 'Gai' (垓, 10^20), 'Jo' (穣, 10^24)
        # These are 7 units indexed 0 to 6 (0: no unit)
        self.units = [
            NumberUnit('', 0),
            NumberUnit('Man', 4),
            NumberUnit('Oku', 8),
            NumberUnit('Cho', 12),
            NumberUnit('Kei', 16),
            NumberUnit('Gai', 20),
            NumberUnit('Jo', 24),
        ]

    def get_unit_for_power(self, power: int) -> Optional[NumberUnit]:
        # Given the power (multiple of 4), return the corresponding unit from the table.
        for unit in self.units:
            if unit.power == power:
                return unit
        return None

    def max_power(self) -> int:
        # Return maximum power defined
        return self.units[-1].power

    def powers_descending(self) -> List[int]:
        # Return all powers in descending order
        return [unit.power for unit in reversed(self.units)]

class LargeNumber:
    """
    Handles large numbers and their decomposition into segments of units of 4 digits (up to 9999 per unit).
    Used to format numbers in Jinkouki style.
    """
    def __init__(self, number: int, unit_system: UnitSystem):
        """
        number: the integer to represent
        unit_system: the UnitSystem to use for formatting output
        """
        self.number = number
        self.unit_system = unit_system
        self.segments = self._decompose_to_segments()

    def _decompose_to_segments(self) -> List[Tuple[int, int]]:
        """
        Decompose the integer number into segments corresponding to units,
        at each segment is an integer between 0 and 9999 inclusive.
        Return list of tuples: (segment_value, unit_power)
        """
        segments = []
        n = self.number
        # Process segments from largest unit down to smallest unit (power 0)
        # Each segment corresponds to 10^(unit_power)
        # Each segment value at most 9999
        # 1 Man = 10^4, so segments correspond to groups of 4 digits
        powers_desc = self.unit_system.powers_descending()
        for pwr in powers_desc:
            divisor = 10 ** pwr
            segment_value = n // divisor
            if pwr != 0:
                segment_value %= 10**4
            else:
                # pwr == 0 means digits below 10^4 (i.e. 0-9999)
                segment_value = n % 10**4
            segments.append((segment_value, pwr))
        # Filter out leading segments that are 0 to avoid extra zeros on head
        while segments and segments[0][0] == 0:
            segments.pop(0)
        # But if no segments remain, the number is zero (should not happen since input ≥1)
        if not segments:
            segments = [(0,0)]
        return segments

    def format(self) -> str:
        """
        Format the large number segments into the Jinkouki styled string.
        Conditions:
        - Each segment value is from 1-9999 (except possibly zero)
        - segments with zero values are skipped (no zeros printed)
        - unit string is appended to segment value except for the smallest unit (power=0) which has no unit
        - no leading zeros printed
        """
        parts = []
        for value, power in self.segments:
            if value == 0:
                continue
            unit = self.unit_system.get_unit_for_power(power)
            if power == 0:
                # no unit for smallest segment
                parts.append(str(value))
            else:
                parts.append(f"{value}{unit}")
        if not parts:
            # number is zero
            return '0'
        return ''.join(parts)

class JinkoukiFormatter:
    """
    Main controller class that computes m^n and formats into Jinkouki units.
    Designed with extensibility for other unit systems or output formats.
    """
    def __init__(self):
        self.unit_system = UnitSystem()

    def compute_power(self, base: int, exponent: int) -> int:
        """
        Compute base ** exponent.
        """
        return pow(base, exponent)

    def format_power(self, base: int, exponent: int) -> str:
        """
        Compute base^exponent and format in Jinkouki style.
        """
        number = self.compute_power(base, exponent)
        # number < 10^72 (from problem constraint)
        ln = LargeNumber(number, self.unit_system)
        return ln.format()

def parse_input(input_str: str) -> Iterator[Tuple[int,int]]:
    """
    Parse input lines and yield tuples (m, n)
    Stops when a line with '0 0' is encountered.
    """
    for line in input_str.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        m, n = map(int, parts)
        if m == 0 and n == 0:
            break
        yield m, n

def main():
    import sys
    formatter = JinkoukiFormatter()
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        parts=line.split()
        if len(parts)!=2:
            continue
        m,n=map(int, parts)
        if m==0 and n==0:
            break
        print(formatter.format_power(m,n))

if __name__ == '__main__':
    main()